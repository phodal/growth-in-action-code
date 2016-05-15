from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site

from blogpost.models import Blogpost


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    protocol = "http"

    def items(self):
        return Blogpost.objects

    def lastmod(self, obj):
        return obj.posted

    def get_urls(self, page=1, site=None, protocol=None):
        return ""
