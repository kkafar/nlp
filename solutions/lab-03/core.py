from collections import Counter
from itertools import islice
from functools import reduce

def token_filter(token: str) -> bool:
    return len(token) > 2

def to_lower(token: str) -> str:
    token.lower()

def process_tokens(tokens: list[str]) -> Counter:
    return Counter(map(lambda tok: str(tok).lower(), filter(token_filter, tokens)))

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
