from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .mongo_client import get_mongo_client, get_database


class SimpleAPIView(APIView):
    def get(self, request):
      data = {'message': 'Hello from project1'}
      return Response(data, status=status.HTTP_200_OK)
    
    @csrf_exempt
    def crear_usuario(request):
        if request.method == 'POST':
          try:

              data = json.loads(request.body)

              client = get_mongo_client()
              db = get_database(client, 'informacion_usuarios')  
              collection = db['usuarios']  

              result = collection.insert_one(data)

              return JsonResponse({'message': 'Usuario exitosamente creado', 'inserted_id': str(result.inserted_id)}, status=200)

          except json.JSONDecodeError:
              return JsonResponse({'error': 'Invalid JSON'}, status=400)
          except Exception as e:
              return JsonResponse({'error': str(e)}, status=500)
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
  
    @csrf_exempt
    def actualiar_usuario(request):
      if request.method == 'POST':
        try:

            data = json.loads(request.body)

            query = {'documento': data.get('documento')}  

            new_values = {"$set": data}

            client = get_mongo_client()
            db = get_database(client, 'informacion_usuarios')
            collection = db['usuarios']  

            result = collection.update_one(query, new_values)

            if result.matched_count > 0:
                return JsonResponse({'message': 'Información del usuario actualizada'}, status=200)
            else:
                return JsonResponse({'error': 'No se encontré un cliente que corresponde al documento entregado'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
      return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
    
    def get_lista_usuarios(request):
       if request.method == "GET":
          try:
              client = get_mongo_client()
              db = get_database(client, 'informacion_usuarios') 
              collection = db['usuarios'] 

              data = list(collection.find())

              json_data = []
              for document in data:
                  json_data.append(document)

              return JsonResponse(json_data, safe=False, status=200)

          except Exception as e:
              return JsonResponse({'error': str(e)}, status=500)
      
    def get_usuario(request):
       if request.method == "GET":
          try:
              data = json.loads(request.body)
              documento = data.get('documento')
              client = get_mongo_client()
              db = get_database(client, 'informacion_usuarios') 
              collection = db['usuarios']  
              document = collection.find_one({'_id': documento}) 

              if document:
                  return JsonResponse(document, status=200)
              else:
                  return JsonResponse({'error': 'Document not found'}, status=404)

          except Exception as e:
              return JsonResponse({'error': str(e)}, status=500)