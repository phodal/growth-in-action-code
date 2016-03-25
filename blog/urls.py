from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers
from blogpost.api import BlogpostSet

apiRouter = routers.DefaultRouter()
apiRouter.register(r'blogpost', BlogpostSet)

urlpatterns = patterns('',
    (r'^$', 'blogpost.views.index'),
    url(r'^blog/(?P<slug>[^\.]+).html', 'blogpost.views.view_post', name='view_blog_post'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(apiRouter.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
