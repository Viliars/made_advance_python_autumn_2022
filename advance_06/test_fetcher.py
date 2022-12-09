import tempfile
from unittest.mock import AsyncMock, patch, call
from pathlib import Path
import os
import pytest
from fetcher import download_all

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_download_all():
    tmpfile = tempfile.NamedTemporaryFile()

    with open(tmpfile.name, "w") as fout:
        print("test1\ntest2\ntest3\ntest4", file=fout)

    tmpdir = tempfile.TemporaryDirectory()

    async_mock1 = AsyncMock()
    async_mock1.text.return_value = "test"

    async_mock2 = AsyncMock(return_value=async_mock1)

    with patch("aiohttp.ClientSession.get") as gmock:
        gmock.side_effect = async_mock2

        await download_all(tmpfile.name, tmpdir.name, 2)

        assert gmock.call_count == 4
        assert gmock.call_args_list == [
            call(arg) for arg in ["test1", "test2", "test3", "test4"]
        ]

    assert len(os.listdir(tmpdir.name)) == 4

    tmpdir_path = Path(tmpdir.name)

    for file in os.listdir(tmpdir.name):
        with (tmpdir_path / file).open("r") as fin:
            text = fin.read()
            assert text == "test"

    tmpfile.close()
    tmpdir.cleanup()
