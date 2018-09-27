"""cleanblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve

import xadmin
from blog.feed import AllPostRssFeed
from cleanblog.settings import MEDIA_ROOT

xadmin.autodiscover()

from xadmin.plugins import xversion

xversion.register_models()

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'', include('blog.urls')),
    url(r'', include('comments.urls')),
    url(r'mdeditor/', include('mdeditor.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^all/rss/$', AllPostRssFeed(), name='rss'),
]
