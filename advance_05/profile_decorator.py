from cProfile import Profile
import pstats
import functools
import io


def profile_deco(func):
    func.profile = Profile()

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        return func.profile.runcall(func, *args, **kwargs)

    def _print_stat():
        try:
            s = io.StringIO()
            sortby = "cumulative"
            ps = pstats.Stats(func.profile, stream=s).sort_stats(sortby)
            ps.print_stats()
            print(s.getvalue())
        except TypeError:
            print(f'!!! The function "{func.__name__}" has never been called !!!')

    _wrapper.print_stat = _print_stat

    return _wrapper


@profile_deco
def add(a, b):
    return a + b


@profile_deco
def sub(a, b):
    return a - b


@profile_deco
def mul(a, b):
    return a * b


add(1, 2)
add(4, 5)

add.print_stat()

for _ in range(10000000):
    sub(4, 3)

sub.print_stat()

mul.print_stat()
