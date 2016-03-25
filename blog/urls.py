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
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^api-token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
