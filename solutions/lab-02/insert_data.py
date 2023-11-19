from elasticsearch import Elasticsearch
import json

client = Elasticsearch(
    "https://localhost:9200",
    api_key="bnBFb2dZc0JJTExuSDZuSEV1TjU6S21EQ0VINTVROUtFRGZISEJISmtGQQ==",
    ca_certs="/home/kkafara/studies/cs/9_term/nlp/software/elasticsearch-8.10.4/config/certs/http_ca.crt"
)

datafile = "/home/kkafara/studies/cs/9_term/nlp/nlp/data/fiqa-pl/corpus.jsonl"
documents = []


def append_document(documents, newdoc):
    documents.append({"index": {"_index": "search-test-nosyn", "_id": str(newdoc['id'])}})
    documents.append(newdoc)


with open(datafile, 'r') as file:
    i = 1
    while line := file.readline():
        doc = json.loads(line)
        if doc['metadata'] is not None:
            del doc['metadata']
        doc['id'] = i
        append_document(documents, doc)
        i += 1

client.bulk(operations=documents, pipeline="ent-search-generic-ingestion")
