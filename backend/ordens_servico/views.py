from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class VoiceCommandView(APIView):
    def post(self, request):
        command = request.data.get('command')
        if not command:
            return Response({'error': 'Comando não fornecido.'}, status=status.HTTP_400_BAD_REQUEST)
        # Exemplo de processamento de comando
        if command.lower() == 'criar ordem de serviço':
            # Aqui você pode chamar a lógica para criar uma ordem de serviço
            return Response({'message': 'Ordem de serviço criada!'}, status=status.HTTP_201_CREATED)
        # Outros comandos podem ser tratados aqui
        return Response({'message': 'Comando não reconhecido.'}, status=status.HTTP_400_BAD_REQUEST)
