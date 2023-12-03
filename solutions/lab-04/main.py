import spacy
import textacy
import datasets as ds
import pickle
import datetime
from multiprocessing import get_context
from collections import Counter
from core import reduce_counters, batched, Timer

dataset_path = 'clarin-knext/fiqa-pl'
dataset_name = 'corpus'

def token_list_to_str_list(tokens: list) -> list[str]:
    return [str(token) for token in tokens]

def compute_ngrams_single_text(tokens: list) -> Counter:
    ngrams = textacy.extract.basics.ngrams(tokens, n=2, min_freq=1)
    return Counter(map())


def main():
    # print('Loading dataset', end=' ', flush=True)
    # timer = Timer()
    # fiqa_ds = ds.load_dataset(dataset_path, dataset_name)[dataset_name]
    # texts = fiqa_ds['text']
    # print(timer.elapsed())

    # # Jako, że nie widziałem możliwości, aby zmodyfikować tekst w Tokenie
    # # (a potrzebujemy zrobić lowercase), więc konwertuję najpierw cały tekst,
    # # a potem tokenizuję.
    # print('Converting to lower', end=' ', flush=True)
    # timer.start()
    # for i, text in enumerate(texts):
    #     texts[i] = text.lower()
    # print(timer.elapsed())

    # # Tokenizer dla j. polskiego
    # spacy_nlp = spacy.load('pl_core_news_sm')
    # tokenizer = spacy_nlp.tokenizer

    # # Tokenizacja
    # print('Tokenization', end=' ', flush=True)
    # timer.start()
    # tokenized_texts = list(tokenizer.pipe(texts, batch_size=200))
    # print(timer.elapsed())

    # print('Merging docs', end=' ', flush=True)
    # timer.start()
    # joined_doc = spacy.tokens.Doc.from_docs(tokenized_texts)
    # del tokenized_texts
    # print(timer.elapsed())

    # counters = None

    # with get_context('spawn').Pool(8) as pool:
    #     print('Computing bigrams', end=' ', flush=True)
    #     context_timer = Timer()
    #     counters: list[Counter] = pool.map(compute_ngrams_single_text, tokenized_texts)
    #     print(context_timer.elapsed())

    #     print('Reducing counters', end=' ', flush=True)
    #     context_timer.start()
    #     n_counters = len(counters)
    #     while n_counters > 1:
    #         counters = pool.map(reduce_counters, batched(counters, 4))
    #     print(context_timer.elapsed())

    # assert len(counters) == 1
    # bigram_counter = counters[0]

    # with open('bigram_counter.pickle', 'wb') as file:
    #     pickle.dump(bigram_counter, file)

    print(Counter((i for i in range(10))))



if __name__ == '__main__':
    main()