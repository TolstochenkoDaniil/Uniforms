from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Form
from .serializers import FormSerializer, FormListSerializer

class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request, user_id=None):
        form = Form.objects.filter(user_id__exact=user_id)
        serializer = self.get_serializer(form.first())
        
        return Response(serializer.data)

    def list(self, request, discipline=None):
        form = Form.objects.filter(discipline=discipline)
        serializer = FormListSerializer(form, many=True)
        
        return Response(serializer.data)
    
    def create(self, request, user_id=None):
        serializer = self.get_serializer()
        _, created = serializer.create(request.data, user_id=user_id)
        
        if created:
            return Response(data={'status': 'created'}, status=201)
        else:
            return Response(data={'status': 'updated'}, status=201)