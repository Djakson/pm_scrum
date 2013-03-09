# coding=utf-8
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User as Django_User
from django.utils.translation import ugettext as _

class Role(models.Model):
    name            = models.CharField(max_length=100, unique=True)

    __unicode__     = lambda self: self.name

class TaskStatus(models.Model):
    status          = models.CharField(max_length=200)
    default         = models.BooleanField(default=False)

    __unicode__     = lambda self: self.status

class TaskTracker(models.Model):
    '''
    трекер задач. показывает к какому типу задача относится (задача,ошибка)
    '''
    name            = models.CharField(max_length=100)

    __unicode__     = lambda self: self.name


class ProductBacklog(models.Model):
    project         = models.ForeignKey("Project", related_name='project')
    name            = models.CharField(max_length=200)
    created_at      = models.DateTimeField(auto_now=True)
    updated_at      = models.DateTimeField(auto_now=True)

class ProductBacklogTask(models.Model):
    backlog         = models.ForeignKey(ProductBacklog, related_name="backlog")
    name            = models.CharField(max_length=200)
    priority        = models.IntegerField(max_length=1000)
    estimate        = models.FloatField(max_length=1000)  # estimate in story-point
    demo_test       = models.TextField(null=True, blank=True)
    description     = models.TextField(null=True, blank=True)
    created_at      = models.DateTimeField(auto_now=True)
    updated_at      = models.DateTimeField(auto_now=True)


class Project(models.Model):
    '''
    проект. больше сказать нечего
    '''
    name            = models.CharField(max_length=200)
    description     = models.TextField()
    created_at      = models.DateTimeField(auto_now=True)
    updated_at      = models.DateTimeField(auto_now=True)
    deadline        = models.DateField(auto_now=True)
    __unicode__     = lambda self: self.name

    get_absolute_url= lambda self: reverse('project_detail', kwargs={'pk':self.pk})

    def get_owner(self):
        return self.member.get(role__in=[Role.objects.get(name='owner')])

class Sprint(models.Model):
    '''
    спринт. короткий забег дабы сделать все пиздато с плюшками и блэкджеком
    '''
    project         = models.ForeignKey(Project, related_name='sprint_project')
    title           = models.CharField(max_length=200, blank=True)
    created_at      = models.DateTimeField(auto_now=True, blank=False)
    updated_at      = models.DateTimeField(auto_created=True, auto_now=True)
    deadline_at     = models.DateTimeField(auto_now=True, auto_created=True)

    __unicode__     = lambda self: self.title

class SprintBackLog(models.Model):
    '''
    бэклог. все, что налажали будет писаться сюда
    '''
    sprint          = models.ForeignKey(Sprint, related_name='backlog')
    project         = models.ForeignKey(Project, related_name='sprint_backlogs')
    title           = models.CharField(max_length=200, blank=True)
    created_at      = models.DateTimeField(auto_now=True, blank=False)
    updated_at      = models.DateTimeField(auto_created=True, auto_now=True)

    __unicode__     = lambda self: "backlog \"%s\"" % self.title

class Task(models.Model):
    '''
    общая задача без привязки к кому либо. Будет абстрактной. Вдруг понадобится еще где-то
    '''
    title           = models.CharField(max_length=200, blank=True)
    description     = models.TextField()
    tracker         = models.ForeignKey(TaskTracker, related_name='tracker_tasks')
    status          = models.ForeignKey(TaskStatus, default=1)
    progress        = models.FloatField(null=True, default=0, max_length=100)
    assigner        = models.ForeignKey("ProjectMember", related_name="tasks")
    author          = models.ForeignKey("ProjectMember", related_name="my_own_task")
    deadline_at     = models.DateTimeField(auto_now=True)
    created_at      = models.DateTimeField(auto_now=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        abstract    = True

    __unicode__     = lambda self: self.title if self.title else _('task %d') % self.pk

class SprintTask(Task):
    sprint          = models.ForeignKey(Sprint, related_name='sprint_tasks')

class ProjectMember(models.Model):
    '''
    Член проекта. Не просто член
    '''
    user            = models.ForeignKey(Django_User, related_name="member_in_projects")
    project         = models.ForeignKey(Project, related_name="member")
    role            = models.ManyToManyField(Role)
    created_at      = models.DateTimeField(auto_now=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def get_name(self):
        try:
            name    = "%s is %s in %s" % (self.user.username, ",".join(map(lambda r: r.name, self.role.all())), self.project.name)
        except:
            name    = "project manager %d" % self.pk
        return name

    __unicode__     = get_name