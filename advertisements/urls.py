from django.conf.urls import patterns, include, url
from .views import (
    ClickRegisterView,
    PanelAdView,
    PreviewView,
    ProviderPermissionRedirectView,
    ProviderListView,
    ProviderStatisticsView,
    AdvertStatisticsView,
    ProviderRequestView,
    PublicAdListView,
)


providerpatterns = patterns('advertisements.views',

    url(r'^$', ProviderPermissionRedirectView.as_view(), name="home"),
    url(r'^list/$', ProviderListView.as_view(), name='list'),

    url(r'^(?P<provider_pk>\d+)/$', ProviderStatisticsView.as_view(), name="stats"),

    url(r'^(?P<provider_pk>\d+)/request/$', ProviderRequestView.as_view(), name="request"),
    url(r'^ad/(?P<advert_pk>\d+)/$', AdvertStatisticsView.as_view(), name="advert_statistics"),
)

urlpatterns = patterns('advertisements.views',
    url(r'^c/(?P<ad_identifier>\d+:.+)/$', ClickRegisterView.as_view(), name='go'),
    url(r'^(?P<panel_pk>\d+)/$', PanelAdView.as_view(), name="panel"),
    url(r'^preview/(?P<width>\d+)/(?P<height>\d+)/(?P<cols>\d+)/(?P<rows>\d+)/$', PreviewView.as_view(), name="preview_size"),
    url(r'^public/', PublicAdListView.as_view()),
)
