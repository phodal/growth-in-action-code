from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import serializers, viewsets
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from blogpost.models import Blogpost


class BlogpsotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogpost
        fields = ('title', 'author', 'body', 'slug', 'id')


@api_view(['GET', 'POST', 'OPTIONS'])
def blogpostList(request):
    if request.method == 'GET':
        blogObject = Blogpost.objects.all()
        blogpost = BlogpsotSerializer(blogObject, many=True)
        return Response(blogpost.data)

    elif request.method == 'POST' or request.method == "OPTIONS":
        blogpost = BlogpsotSerializer(data=request.data)
        if blogpost.is_valid():
            blogpost.save()
            return Response(blogpost.data, status=status.HTTP_201_CREATED)
        return Response(blogpost.errors, status=status.HTTP_400_BAD_REQUEST)


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
