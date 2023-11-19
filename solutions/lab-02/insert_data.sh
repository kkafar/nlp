#!/bin/bash

export ES_URL="https://localhost:9200"
export API_KEY="YzVFX2dJc0JJTExuSDZuSDBnTHI6R190UmFUT3lSUEd2WnlGeVAxUlkzdw=="
CERT_PATH="/home/kkafara/studies/cs/9_term/nlp/software/elasticsearch-8.10.4/config/certs/http_ca.crt"

# curl -X PUT "${ES_URL}/customer/_doc/1?pretty" -H 'Content-Type: application/json' -d'
# {
#   "name": "John Doe"
# }
# '

docid=1

while read line; do
  # echo $line
  # curl --cacert ${CERT_PATH} -X PUT "${ES_URL}/search-test-1/_doc/1?pretty" -H 'Content-Type: application/json' -d'
  # {
  #   "name": "John Doe"
  # }
  # '

  # curl --cacert ${CERT_PATH} -X POST "${ES_URL}/_bulk?pretty&pipeline=ent-search-generic-ingestion" \
  
  # record="{ \"index\" : { \"_index\" : \"search-test-1\" } }\\n${line}\n"
  # echo -e "${record}" > query.txt
  # echo $record
  curl --cacert ${CERT_PATH} -X POST "${ES_URL}/search-test-1/_doc/${docid}?pretty" \
    -H "Authorization: ApiKey "${API_KEY}"" \
    -H "Content-Type: application/json" \
    -d "${line}"

  docid=$((docid + 1))
done < ../../data/fiqa-pl/corpus.jsonl
