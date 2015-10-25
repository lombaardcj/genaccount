from django.conf.urls import url

from django.views.generic.dates import ArchiveIndexView

from . import views
from .models import Account

urlpatterns=[
    #ex: /genaccount/
#    url(r'^$', views.index, name='index'),

    #ex: /genaccount/acclist/
#    url(r'^acclist/$', views.accountlist, name='accountlist'),
    
    #ex: /genaccount/acclist/5/
#    url(r'^acclist/(?P<account_id>[0-9]+)/$', views.detail, name='detail'),

    #ex: /genaccount/showaccount/1/
#    url(r'^showaccount/(?P<pk>[0-9]+)/$', views.showaccount, name='showaccount'),


    #ex: /polls/5/results/
#    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    
    #ex: /polls/5/vote/
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^gen/$',
        views.AccountList.as_view(),
        name='account_list'),

    url(r'^gen/archiveindex/$',
        ArchiveIndexView.as_view(model=Account, date_field="created_on"),
        name='account_list'),
    url(r'^gen/archiveweek/$',
        ArchiveIndexView.as_view(model=Account, date_field="created_on"),
        name='account_list'),
    url(r'^gen/(?P<pk>[0-9]+)/$',
        views.AccountDetail.as_view(),
        name='account_detail'),
    url(r'^gen/create/$',
        views.AccountCreate.as_view(),
        name='account_create'),
    url(r'^gen/(?P<pk>[0-9]+)/update/$',
        views.AccountUpdate.as_view(),
        name='account_edit'),
    url(r'^gen/(?P<pk>[0-9]+)/delete/$',
        views.AccountDelete.as_view(),
        name='account_delete'),
]
