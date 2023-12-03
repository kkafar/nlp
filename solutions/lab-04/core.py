from collections import Counter
from itertools import islice
from functools import reduce
from datetime import datetime, timedelta

class Timer:
    def __init__(self):
        self.start_time: datetime = datetime.now()

    def start(self):
        self.start_time = datetime.now()

    def elapsed(self):
        return datetime.now() - self.start_time

def reduce_counters(counters: list[Counter]) -> Counter:
    return reduce(lambda a, b: a + b, counters)

def batched(iterable, n):
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch