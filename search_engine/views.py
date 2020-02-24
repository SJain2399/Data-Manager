from django.shortcuts import render
from django.http import HttpResponse
import elasticsearch
from elasticsearch import Elasticsearch
import json
# Create your views here.
def first(request):
    print(elasticsearch.VERSION)
    return HttpResponse("Hello from search engine")
    
def matchStr(request):
    body = request.Params['stringExp']
    print(body)
    stringExp = body['stringExp']
    elastic_client = Elasticsearch(hosts=["192.168.56.101:9200"])
    result = elastic_client.search(index="drive", body={"query": {"match": {"name": stringExp}}})
    print ("query hits:", result["hits"]["hits"])