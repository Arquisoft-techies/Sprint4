import requests
from django.http import JsonResponse

def orquestador_view(request):
    if request.method == 'POST':
        # Procesar la solicitud del usuario
        data_from_user = request.POST.get('data')
        
        # Enviar la solicitud al microservicio
        response = requests.post('http://localhost:8001/api/orquestador/', json=data_from_user)

        # Analizar y devolver la respuesta del microservicio al usuario
        if response.status_code == 200:
            data_from_microservicio = response.json()
            return JsonResponse(data_from_microservicio)
        else:
            return JsonResponse({'error': 'Could not communicate with microservice'}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)