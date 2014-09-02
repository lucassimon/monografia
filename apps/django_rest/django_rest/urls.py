from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from django.contrib import admin
admin.autodiscover()

sitemaps = {
    # Place sitemaps here
}


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'django_rest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(
        r'^admin/',
        include(admin.site.urls)
    ),
    url(
        r'^api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    ),
    url(r'^api/', include('api.urls')),

    # SEO API's
    url(
        r'^sitemap.xml$',
        'django.contrib.sitemaps.views.sitemap',
        {
            'sitemaps': sitemaps
        }
    ),

)

urlpatterns = format_suffix_patterns(
    urlpatterns,
    allowed=['json', 'api']
)

