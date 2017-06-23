from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from blogpost.models import Blogpost
from rest_framework import permissions

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or
                    request.user and
                    request.user.is_authenticated()):
            return True
        return False


class BlogpostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogpost
        fields = ('title', 'author', 'body', 'slug', 'id')


class BlogpostSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = BlogpostSerializer
    search_fields = 'title'

    def get_queryset(self):
        return Blogpost.objects.all()

    def list(self, request):
        queryset = Blogpost.objects.all()

        search_param = self.request.query_params.get('title', None)
        if search_param is not None:
            queryset = Blogpost.objects.filter(title__contains=search_param)

        serializer = BlogpostSerializer(queryset, many=True)
        return Response(serializer.data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'last_login')


class UserDetail(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [JSONWebTokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        search_param = self.request.query_params.get('username', None)
        if search_param is not None:
            queryset = User.objects.filter(username__contains=search_param)

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
