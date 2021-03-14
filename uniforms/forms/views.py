from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Form
from .serializers import FormSerializer, FormListSerializer
from .mixin import PermissionMixin

class FormViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    permissions_by_action = {'list': (IsAuthenticatedOrReadOnly,)}

    def retrieve(self, request, user_id=None):
        form = Form.objects.filter(user_id__exact=user_id)
        serializer = self.get_serializer(form.first())

        return Response(serializer.data)

    def list(self, request, discipline=None):
        form = Form.objects.filter(discipline=discipline, is_valid=1)
        page = self.paginate_queryset(form)
        serializer = FormListSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)

    def create(self, request, user_id=None):
        serializer = self.get_serializer()
        form, created = serializer.create(request.data, user_id=user_id)

        form.check_edit_permission()

        if created:
            return Response(data={'status': 'created'}, status=201)
        else:
            return Response(data={'status': 'updated'}, status=201)