from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from blogpost.models import Blogpost


class BlogpsotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogpost
        fields = ('title', 'author', 'body', 'slug')

# ViewSets define the view behavior.
class BlogpostSet(viewsets.ModelViewSet):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpsotSerializer

