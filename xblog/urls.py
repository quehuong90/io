from django.conf.urls import patterns, include, url
from django.contrib import admin

#from django_markdown import flatpages

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^', include('apps.blog.urls')),
)


#admin.autodiscover()
#flatpages.register()
#urlpatterns += [ url(r'^admin/', include(admin.site.urls)), ]