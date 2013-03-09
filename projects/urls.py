__author__ = 'djakson'

from projects.views import ProjectView, ProjectDetail, ProjectList, SprintList, SprintTaskList, SprintDetail, \
    SprintTaskDetail, SprintTaskCreate, SprintCreate

from django.conf.urls import url, patterns

urlpatterns = patterns('projects.views',

                       url(r'^projects/$', ProjectList.as_view(), name='project_list'),
                       url(r'^project/create/$', ProjectView.as_view(), name='create_project'),
                       url(r'^(?P<pk>\d+)/$', ProjectDetail.as_view(), name='project_detail'),


                       url(r'^(?P<project_pk>\d+)/sprints/$', SprintList.as_view(), name="sprint_list"),
                       url(r'^(?P<project_pk>\d+)/sprint/(?P<pk>\d+)/$', SprintDetail.as_view(), name='sprint_detail'),
                       url(r'^(?P<project_pk>\d+)/sprint/create/$', SprintCreate.as_view(), name='sprint_create'),
                       url(r'^(?P<project_pk>\d+)/sprint/(?P<sprint_pk>\d+)/task$', SprintTaskList.as_view(),
                           name='sprint_task_list'),
                       url(r'^(?P<project_pk>\d+)/sprint/(?P<sprint_pk>\d+)/task/(?P<pk>\d+)/$',
                           SprintTaskDetail.as_view(), name='sprint_task_detail'),
                       url(r'^(?P<project_pk>\d+)/task/$', SprintTaskList.as_view(), name="project_tasks"),


                       url(r'^(?P<project_pk>\d+)/task/create/$', SprintTaskList.as_view(), name="new_task_project"),
                       url(r'^(?P<project_pk>\d+)/sprint/(?P<sprint_pk>\d+)/task/create/$', SprintTaskCreate.as_view(),
                           name="new_task_sprint"),

)