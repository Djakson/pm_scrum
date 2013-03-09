# coding=utf-8
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, ListView
from models import Project, Sprint, SprintTask
from django.utils.translation import ugettext as _
from django.core import urlresolvers as url


class ProjectView(CreateView):
    """
    создание нового проекта
    """
    template_name = 'projects/project/create.html'
    model = Project
    redirect_to = '/'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        self.request.breadcrumbs(
            [(_("Projects"), url.reverse('project_list')), (_('new project'), url.reverse('create_project'))])
        return context


class ProjectDetail(DetailView):
    template_name = 'projects/project/detail.html'
    model = Project
    queryset = Project.objects.all()
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        self.request.breadcrumbs([(_("Projects"), url.reverse('project_list')),
                                  (self.object.name, url.reverse('project_detail', kwargs={'pk': self.object.pk}))])
        return context


class ProjectList(ListView):
    """
    список проектов
    """
    template_name = 'projects/project/list.html'
    model = Project
    queryset = Project.objects.all()
    context_object_name = 'project_list'

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        self.request.breadcrumbs([(_("Projects"), url.reverse('project_list'))])
        return context


class SprintList(ListView):
    """
    список спринтов
    """
    model = Sprint
    template_name = 'projects/sprint/list.html'
    context_object_name = 'sprint_list'

    def get_queryset(self):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        self.project = project
        return self.model.objects.filter(project=project)

    def get_context_data(self, **kwargs):
        context = super(SprintList, self).get_context_data(**kwargs)
        self.request.breadcrumbs([(_("Projects"), url.reverse('project_list')),
                                  (self.project.name, url.reverse('project_detail', kwargs={'pk': self.project.pk})),
                                  (_("sprints"), url.reverse('sprint_list', kwargs={'project_pk': self.project.pk}))])
        return context


class SprintCreate(CreateView):
    template_name = "projects/sprint/create.html"
    model = Sprint

    def get_success_url(self):
        from pm_scrum.context_processors import project
        project_id = project(self.request)['project'].id
        return url.reverse("sprint_list", kwargs={'project_pk': project_id})

    success_url = lambda self: self.object.get_url()

class SprintTaskList(ListView):
    """
    список задач
    """
    model = SprintTask
    context_object_name = 'sprint_task_list'

    def get_queryset(self):
        from pm_scrum.context_processors import project as project_context, sprint
        extra_context = project_context(self.request)
        if extra_context:
            project = extra_context.get('project')
            self.project = project
            return self.model.objects.filter(sprint__in=Sprint.objects.filter(project=project))
        return self.model.objects.filter(sprint=sprint(self.request)['sprint'])

    def get_template_names(self):
        #path = self.request.path
        return 'projects/project/tasks.html'

    def get_context_data(self, **kwargs):
        context = super(SprintTaskList, self).get_context_data(**kwargs)
        if context['project']:
            self.request.breadcrumbs(
                [(_("Projects"), url.reverse('project_list')), (context['project'].name, '/%d/' % context['project'].pk),
                 (_("all tasks"), url.reverse('project_tasks', kwargs={'project_pk': context['project'].pk}))])
        return context


class SprintTaskDetail(DetailView):
    model = SprintTask
    template_name = 'projects/tasks/detail.html'
    queryset = SprintTask.objects.all()
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super(SprintTaskDetail, self).get_context_data(**kwargs)
        sprint = self.object.sprint
        project = sprint.project
        self.request.breadcrumbs([(_("Projects"), url.reverse('project_list')),
                                  (project.name, '/%d/' % project.id),
                                  (_('sprints'), url.reverse('sprint_list', kwargs={'project_pk': project.pk})),
                                  (sprint.title,
                                   url.reverse('sprint_detail', kwargs={'project_pk': project.pk, 'pk': sprint.pk})),
                                  (_('tasks'), url.reverse('sprint_task_list',
                                                           kwargs={'project_pk': project.pk, "sprint_pk": sprint.pk})),
                                  (self.object.title, url.reverse('sprint_task_detail',
                                                                  kwargs={'project_pk': project.pk,
                                                                          "sprint_pk": sprint.pk,
                                                                          'pk': self.object.pk})),
        ])
        return context


class SprintTaskCreate(CreateView):

    model = SprintTask
    template_name = 'projects/sprint/create.html'

    def get_success_url(self):
        from pm_scrum.context_processors import project, sprint
        project_id = project(self.request)['project'].id
        sprint_id = sprint(self.request)['sprint'].id
        return url.reverse("sprint_task_list", kwargs={'project_pk':project_id, "sprint_pk": sprint_id})


class SprintDetail(DetailView):
    model = Sprint
    template_name = 'projects/sprint/detail.html'
    context_object_name = 'sprint'

    def get_context_data(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        context = super(SprintDetail, self).get_context_data(**kwargs)
        project = context['sprint'].project
        self.request.breadcrumbs([(_("Projects"), url.reverse('project_list')), (project.name, '/%d/' % project.id),
                                  (_('sprints'), url.reverse('sprint_list', kwargs={'project_pk': project.pk})), (
                context['sprint'].title,
                url.reverse('sprint_detail', kwargs={'project_pk': project.pk, 'pk': context['sprint'].pk}))])
        return context
