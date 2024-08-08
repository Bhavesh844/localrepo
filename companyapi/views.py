from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def homepage(request):
    print('successfully')
    l=[1,2,3,4,5,6,7]
    return JsonResponse(l,safe=False)   