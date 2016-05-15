from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from blogpost.models import Blogpost
from django.apps import apps as django_apps

class PageSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['main']

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Blogpost.objects.all()

    def lastmod(self, obj):
        return obj.posted

class FlatPageSitemap(Sitemap):
    priority = 0.8

    def items(self):
        Site = django_apps.get_model('sites.Site')
        current_site = Site.objects.get_current()
        return current_site.flatpage_set.filter(registration_required=False)
