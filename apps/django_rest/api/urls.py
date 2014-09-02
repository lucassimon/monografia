# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

# Third-party app imports

# Imports from your apps
from .views import (
    api_root,
    PersonList,
    PersonDetail,
    ContactList,
    ContactDetail
)

urlpatterns = patterns(
    'api.views',    
    url(
        r'^$',
        api_root
    ),
    url(
        r'^v1/pessoas/$',
        PersonList.as_view(),
        name='person-list'
    ),
    url(
        r'^v1/pessoas/(?P<pk>\d+)/$',
        PersonDetail.as_view(),
        name='person-detail'
    ),
    url(
        r'^v1/contatos/$',
        ContactList.as_view(),
        name='contact-list'
    ),
    url(
        r'^v1/contatos/(?P<pk>\d+)/$',
        ContactDetail.as_view(),
        name='contact-detail'
    ),
)
