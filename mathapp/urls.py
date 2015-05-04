# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

import mathapp

urlpatterns = patterns('',
    # waiting for result
    url(r'^add/(?P<a>\d+)/(?P<b>\d+)/$', 'mathapp.views.add_view'),
    url(r'^mul/(?P<a>\d+)/(?P<b>\d+)/$', 'mathapp.views.mul_view'),
    url(r'^fac/(?P<n>\d+)/$', 'mathapp.views.fac_view'),
    
    # delayed
    url(r'^d/add/(?P<a>\d+)/(?P<b>\d+)/$', 'mathapp.views.add_delay_view'),
    url(r'^d/mul/(?P<a>\d+)/(?P<b>\d+)/$', 'mathapp.views.mul_delay_view'),
    url(r'^d/fac/(?P<n>\d+)/$', 'mathapp.views.fac_delay_view'),
    
    # numbers saved in separate model
    url(r'^d2/add/(?P<a>\d+)/(?P<b>\d+)/$', 'mathapp.views.add_2_delay_view'),
    url(r'^d2/mul/(?P<a>\d+)/(?P<b>\d+)/$', 'mathapp.views.mul_2_delay_view'),
    url(r'^d2/fac/(?P<n>\d+)/$', 'mathapp.views.fac_2_delay_view'),
    
    # view tasks
    url(r'^t/add/(?P<pk>\d+)/$', 'mathapp.views.add_task_view', name='task_add'),
    url(r'^t/mul/(?P<pk>\d+)/$', 'mathapp.views.mul_task_view', name='task_mul'),
    url(r'^t/fac/(?P<pk>\d+)/$', 'mathapp.views.fac_task_view', name='task_fac'),
)
