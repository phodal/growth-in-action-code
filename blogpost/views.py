from django.shortcuts import render_to_response, get_object_or_404
from djpjax import pjax

from blogpost.models import Blogpost

def index(request):
    return render_to_response('index.html', {
        'posts': Blogpost.objects.all()[:5]
    })

@pjax(pjax_template="pjax.html", additional_templates={"#pjax-inner-content": "pjax_inner.html"})
def view_post(request, slug):
    return render_to_response('blogpost_detail.html', {
        'post': get_object_or_404(Blogpost, slug=slug)
    })
