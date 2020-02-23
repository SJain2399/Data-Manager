from django.shortcuts import render
from django.http import HttpResponse
import elasticsearch
from elasticsearch import Elasticsearch

# Create your views here.
def first(request):
    print(elasticsearch.VERSION)
    return HttpResponse("Hello from search engine")
    
def matchStr(string):
    elastic_client = Elasticsearch(hosts=["192.168.56.101:9200"])
    result = elastic_client.search(index="drive", body={"query": {"match": {"name": string}}})
    print ("query hits:", result["hits"]["hits"])