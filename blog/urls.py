from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from rest_framework import routers

from blogpost import views as blogpostViews
from rest_framework_jwt import views as DRFViews
from blogpost.api import BlogpostSet, UserDetail

from sitemap.sitemaps import BlogSitemap, PageSitemap, FlatPageSitemap

apiRouter = routers.DefaultRouter()
apiRouter.register(r'blogpost', BlogpostSet, 'Blogpost')
apiRouter.register(r'user', UserDetail, 'User')

sitemaps =  {
    "page": PageSitemap,
    'flatpages': FlatPageSitemap,
    "blog": BlogSitemap
}

urlpatterns = patterns('',
    url(r'^$', blogpostViews.index, name='main'),
    url(r'^blog/(?P<slug>[^\.]+).html', blogpostViews.view_post, name='view_blog_post'),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(apiRouter.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', DRFViews.obtain_jwt_token),
    url(r'^api-token-refresh/', DRFViews.refresh_jwt_token),
    url(r'^api-token-verify/', DRFViews.verify_jwt_token),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
