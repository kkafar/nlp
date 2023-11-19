#!/bin/bash

export ES_URL="https://localhost:9200"
export API_KEY="YzVFX2dJc0JJTExuSDZuSDBnTHI6R190UmFUT3lSUEd2WnlGeVAxUlkzdw=="
CERT_PATH="/home/kkafara/studies/cs/9_term/nlp/software/elasticsearch-8.10.4/config/certs/http_ca.crt"

curl --cacert ${CERT_PATH} "${ES_URL}/search-test-1" \
  -H "Authorization: ApiKey "${API_KEY}"" \
  -H "Content-Type: application/json"


curl --cacert ${CERT_PATH} -X POST "${ES_URL}/_bulk?pretty&pipeline=ent-search-generic-ingestion" \
  -H "Authorization: ApiKey "${API_KEY}"" \
  -H "Content-Type: application/json" \
  -d'
{ "index" : { "_index" : "search-test-1" } }
{"name": "Snow Crash", "author": "Neal Stephenson", "release_date": "1992-06-01", "page_count": 470, "_extract_binary_content": true, "_reduce_whitespace": true, "_run_ml_inference": false}
{ "index" : { "_index" : "search-test-1" } }
{"name": "Revelation Space", "author": "Alastair Reynolds", "release_date": "2000-03-15", "page_count": 585, "_extract_binary_content": true, "_reduce_whitespace": true, "_run_ml_inference": false}
{ "index" : { "_index" : "search-test-1" } }
{"name": "1984", "author": "George Orwell", "release_date": "1985-06-01", "page_count": 328, "_extract_binary_content": true, "_reduce_whitespace": true, "_run_ml_inference": false}
{ "index" : { "_index" : "search-test-1" } }
{"name": "Fahrenheit 451", "author": "Ray Bradbury", "release_date": "1953-10-15", "page_count": 227, "_extract_binary_content": true, "_reduce_whitespace": true, "_run_ml_inference": false}
{ "index" : { "_index" : "search-test-1" } }
{"name": "Brave New World", "author": "Aldous Huxley", "release_date": "1932-06-01", "page_count": 268, "_extract_binary_content": true, "_reduce_whitespace": true, "_run_ml_inference": false}
{ "index" : { "_index" : "search-test-1" } }
{"name": "The Handmaid'"'"'s Tale", "author": "Margaret Atwood", "release_date": "1985-06-01", "page_count": 311, "_extract_binary_content": true, "_reduce_whitespace": true, "_run_ml_inference": false}
'
