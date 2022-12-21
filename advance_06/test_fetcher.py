import tempfile
from unittest.mock import AsyncMock, patch, call
from pathlib import Path
import os
import asyncio
import pytest
from fetcher import save_page, download_page, worker, download_all

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_save_page():
    tmpfile = tempfile.NamedTemporaryFile()
    path = Path(tmpfile.name)
    data = "test"

    await save_page(data, path)

    with path.open("r") as fin:
        text = fin.read()
        assert text == "test"


@pytest.mark.asyncio
async def test_download_page():
    async_mock1 = AsyncMock()
    async_mock1.text.return_value = "hello test"

    async_mock2 = AsyncMock()
    async_mock2.get.return_value = async_mock1

    result = await download_page("test", async_mock2)

    assert result == "hello test"

    assert async_mock1.text.call_count == 1
    assert async_mock1.text.call_args_list == [call()]

    assert async_mock2.get.call_count == 1
    assert async_mock2.get.call_args_list == [call('test')]


@pytest.mark.asyncio
async def test_worker():
    queue = asyncio.Queue()

    async_mock1 = AsyncMock()
    async_mock1.text.side_effect = [f"test{i}" for i in range(5)]

    async_mock2 = AsyncMock()
    async_mock2.get.return_value = async_mock1

    worker_task = asyncio.create_task(worker(queue, async_mock2))

    tmpdir = tempfile.TemporaryDirectory()
    output_path = Path(tmpdir.name)

    for number in range(5):
        await queue.put(("test", output_path / f"{number}.txt"))

    await queue.join()

    worker_task.cancel()

    for number in range(5):
        with (output_path / f"{number}.txt").open("r") as fin:
            text = fin.read()
            assert text == f"test{number}"

    tmpdir.cleanup()


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
