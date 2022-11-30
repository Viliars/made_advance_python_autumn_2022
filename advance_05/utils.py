import time
import functools


def timeit(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        name = kwargs["name"]
        del kwargs["name"]
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        elapsed_time_ms = int(elapsed_time * 1_000)
        print(f"timetest [{name}] finished in {elapsed_time_ms} ms")
        return result

    return _wrapper
