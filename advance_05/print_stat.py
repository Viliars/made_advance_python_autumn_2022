import pstats

p = pstats.Stats("stats.txt")
p.strip_dirs().sort_stats("cumulative").print_stats()
