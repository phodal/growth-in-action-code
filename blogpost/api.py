from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from blogpost.models import Blogpost


class BlogpsotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogpost
        fields = ('title', 'author', 'body', 'slug', 'id')


# ViewSets define the view behavior.
class BlogpostSet(viewsets.ModelViewSet):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpsotSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'last_login')


class UserDetail(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
