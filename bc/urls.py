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
    url(r'^$', 'user_login', name='user_login'),
    url(r'^Home/(?P<username>[-\w]+)/$', 'home', name='bc_home'),
    url(r'^FormPage/(?P<username>[-\w]+)/$', 'form_page', name='bc_form_page'),
    url(r'^AddPreference/(?P<username>[-\w]+)/$', 'add_preference', name='bc_branch_create'),
    url(r'^EditPreference/(?P<pk>\d+)/$', 'edit_preference', name='bc_branch_edit'),
    url(r'^DeletePreference/(?P<pk>\d+)/$', 'delete_preference', name='bc_branch_delete'),
    url(r'^AddInfo/(?P<username>[-\w]+)/$', 'add_info', name='bc_candidate_create'),
    url(r'^EditInfo/(?P<pk>\d+)/$', 'edit_info', name='bc_candidate_edit'),
    url(r'^ExportData/(?P<username>[-\w]+)/$', 'export_data', name='bc_branch_export'),
    url(r'^ImportData/(?P<username>[-\w]+)/$', 'import_data', name="bc_branch_import"),
    url(r'^RunAlgorithm/(?P<username>[-\w]+)/$', 'run_branch_change_algorithm', name='bc_branch_algorithm'),    
    url(r'^View/(?P<username>[-\w]+)$', 'preview_forms',name='bc_preview'),
)