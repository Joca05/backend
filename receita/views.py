from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Receita, Categoria, Interacao
from .serializers import ReceitaSerializer, CategoriaSerializer, InteracaoSerializer



class ReceitaListarCriarView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        receitas = Receita.objects.all()
        serializer = ReceitaSerializer(receitas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReceitaSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReceitaRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return Receita.objects.get(pk=pk)

    def put(self, request, pk):
        receita = self.get_object(pk)
        serializer = ReceitaSerializer(receita, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        receita = self.get_object(pk)
        receita.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CategoriaListarCriarView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return Categoria.objects.get(pk=pk)

    def put(self, request, pk):
        categoria = self.get_object(pk)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        categoria = self.get_object(pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class InteracaoListarCriarView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        interacoes = Interacao.objects.all()
        serializer = InteracaoSerializer(interacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InteracaoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InteracaoRetrieveDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return Interacao.objects.get(pk=pk)

    def delete(self, request, pk):
        interacao = self.get_object(pk)
        interacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
