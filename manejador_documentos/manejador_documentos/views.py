from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from manejador_documentos.logic.documentos_logic import guardar_documento_logic


class SimpleAPIView(APIView):
    def get(self, request):
        data = {'message': 'Conexion manejador de documentos'}
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        tipo = request.data.get('tipo')
        ruta = request.data.get('ruta')
        identificacion = request.data.get('identificacion') 
        
        if not tipo or not ruta or not identificacion:
            return Response({'error': 'Faltan datos requeridos'}, status=status.HTTP_400_BAD_REQUEST)
        
        documento = guardar_documento_logic(tipo, ruta, identificacion)
        return Response({'message': 'Documento guardado', 'documento_id': documento.Id}, status=status.HTTP_201_CREATED)