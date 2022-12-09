import asyncio
import argparse
from pathlib import Path
import aiohttp
import aiofiles


async def save_page(data, path):
    async with aiofiles.open(path, mode="w") as fout:
        await fout.write(data)


async def download_page(url, session):
    resp = await session.get(url)
    return await resp.text()


async def worker(queue: asyncio.Queue, session: aiohttp.ClientSession):
    while True:
        url, save_path = await queue.get()

        try:
            page = await download_page(url, session)
            await save_page(page, save_path)
        finally:
            queue.task_done()


async def download_all(file: str, save_dir: str, workers: int):
    queue = asyncio.Queue(workers)
    save_dir_path = Path(save_dir)
    save_dir_path.mkdir(exist_ok=True)
    i = 0

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(worker(queue, session)) for _ in range(workers)]

        async with aiofiles.open(file, mode="r") as fin:
            async for url in fin:
                await queue.put((url.strip(), save_dir_path / f"{i}.html"))
                i += 1

        await queue.join()

        for task in tasks:
            task.cancel()


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("workers", type=int, help="Workers count")
    parser.add_argument("file", type=str, help="File with urls")
    parser.add_argument("--save_dir", default="download", type=str, help="Save Dir")

    args = parser.parse_args()

    await download_all(args.file, args.save_dir, args.workers)


if __name__ == "__main__":
    asyncio.run(main())
