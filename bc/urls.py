"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url

urlpatterns = patterns('bc.views',
    url(r'^user/(?P<username>[-\w]+)/$', 'branch_user', name='bc_branch_user'),
    url(r'^create/$', 'branch_create', name='bc_branch_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'branch_edit', name='bc_branch_edit'),
    url(r'^delete/(?P<pk>\d+)/$', 'branch_delete', name='bc_branch_delete'),
    url(r'^$', 'branch_list', name='bc_branch_list'),
    url(r'^export/$', 'branch_export', name='bc_branch_export'),
    url(r'^import/$', 'branch_import', name="bc_branch_import"),
    url(r'^algorithm/$', 'branch_algorithm', name='bc_branch_algorithm'),
    url(r'^Create/$', 'candidate_create', name='bc_candidate_create'),
    url(r'^Edit/(?P<pk>\d+)/$', 'candidate_edit', name='bc_candidate_edit'),
    
)