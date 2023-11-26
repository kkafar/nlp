import datasets as ds
import spacy
from multiprocessing import get_context
from collections import Counter
from core import process_tokens, reduce_counters, batched
from functools import reduce
import json

dataset_name = 'clarin-knext/fiqa-pl'
dataset_config_name = 'corpus'

def main():
    dataset = ds.load_dataset(dataset_name, dataset_config_name)
    corpus = dataset[dataset_config_name]

    spacy_nlp = spacy.load('pl_core_news_sm')
    tokenizer = spacy_nlp.tokenizer

    texts = corpus['text']

    tokenized_texts = list(tokenizer.pipe(texts, batch_size=200))

    print('processing')

    counters = None
    with get_context('spawn').Pool(10) as pool:
        counters: list[Counter] = pool.map(process_tokens, tokenized_texts)

        print('reducing')
        n_counters = len(counters)
        while n_counters > 1:
            counters = pool.map(reduce_counters, batched(counters, 4))
            n_counters = len(counters)

    assert len(counters) == 1
    counter = counters[0]

    print(counter.most_common(10), counter.total())

    with open('local.frequencylist.json', 'w') as file:
        json.dump(counter, file, indent=2)


def second_main():
    with open('local.frequencylist.json', 'r') as file:
        count_map = json.load(file)
        counter = Counter(count_map)
        print(counter.most_common(10))

if __name__ == "__main__":
    main()
    # second_main()

