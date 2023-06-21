from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Apoderado
from .serializers import ApoderadoSerializer

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class ApoderadoView(APIView):
    
    def get(self,request):
        dataApoderado = Apoderado.objects.all()
        serApoderado = ApoderadoSerializer(dataApoderado,many=True)
        return Response(serApoderado.data)
    
    def post(self,request):
        serApoderado = ApoderadoSerializer(data=request.data)
        serApoderado.is_valid(raise_exception=True)
        serApoderado.save()
        
        return Response(serApoderado.data)
    
class ApoderadoDetailView(APIView):
    
    def get(self,request,apoderado_id):
        dataApoderado = Apoderado.objects.get(pk=apoderado_id)
        serApoderado = ApoderadoSerializer(dataApoderado)
        return Response(serApoderado.data)
    
    def put(self,request,apoderado_id):
        dataApoderado = Apoderado.objects.get(pk=apoderado_id)
        serApoderado = ApoderadoSerializer(dataApoderado,data=request.data)
        serApoderado.is_valid(raise_exception=True)
        serApoderado.save()
        return Response(serApoderado.data)
    
    def delete(self,request,apoderado_id):
        dataApoderado = Apoderado.objects.get(pk=apoderado_id)
        serApoderado = ApoderadoSerializer(dataApoderado)
        dataApoderado.delete()
        return Response(serApoderado.data)

