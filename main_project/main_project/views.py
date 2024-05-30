import requests
from django.http import JsonResponse
from django.shortcuts import render

def orquestador_view(request):
    if request.method == 'GET':
        """if 'data_ms1' in request.POST:
            data = request.POST.get('data_ms1')
            response = requests.post('http://localhost:8001/api/simple/', json={'data': data})
            return JsonResponse(response.json())
        elif 'data_ms2' in request.POST:
            data = request.POST.get('data_ms2')
            response = requests.post('http://localhost:8002/api/simple/', json={'data': data})
            return JsonResponse(response.json())
        elif 'data_ms3' in request.POST:
            data = request.POST.get('data_ms3')
            response = requests.post('http://localhost:8003/api/simple/', json={'data': data})
            return JsonResponse(response.json())"""
    return render(request, 'orquestador.html')