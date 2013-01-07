from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView
from blog.models import Post
urlpatterns = patterns('blog.views',
	url(r'^$', ListView.as_view(queryset=Post.objects.order_by("-created"), context_object_name="post_list", paginate_by=5,), name="main"),
	url(r'blog/post/(?P<pk>\d+)/$', DetailView.as_view(model=Post,),name="post_detail_view"),
	url(r'about/$', TemplateView.as_view(template_name="blog/about.html"), name="about"),
	url(r'resume/$', TemplateView.as_view(template_name="blog/resume.html"), name="resume"),
)
