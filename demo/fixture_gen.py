__author__ = 'djakson'

from fixture_generator import fixture_generator

from django.contrib.auth.models import User, Group

from projects.models import *

@fixture_generator(User)
def test_users():
    simon           = User.objects.create(pk=2,username="simon")
    adrian          = User.objects.create(pk=3, username="adrian")
    jacob           = User.objects.create(pk=4, username="jacob")

@fixture_generator(TaskStatus)
def task_statuses():
    new             = TaskStatus.objects.create(status="new", default=True)
    opened          = TaskStatus.objects.create(status="opened")
    in_progress     = TaskStatus.objects.create(status="in progress")
    closed          = TaskStatus.objects.create(status="closed")
    rejected        = TaskStatus.objects.create(status="rejected")

@fixture_generator(TaskTracker)
def task_tracker():
    error           = TaskTracker.objects.create(name='error')
    task            = TaskTracker.objects.create(name='task')

@fixture_generator(Project)
def projects():
    cubertin        = Project.objects.create(name="cubertin", description="")
    stroyprice      = Project.objects.create(name="stroyprice", description="")
    homlibre        = Project.objects.create(name="homlibre", description="")
    kibet           = Project.objects.create(name="kibet", description="")
    fotlim          = Project.objects.create(name="fotlim", description="")

@fixture_generator(Role)
def roles():
    admin           = Role.objects.create(name='admin')
    manager         = Role.objects.create(name='manager')
    developer       = Role.objects.create(name='developer')

@fixture_generator(ProjectMember,requires=['demo.test_users', 'demo.projects', 'demo.roles'])
def project_member():
    adrian          = Django_User.objects.get(username='adrian')
    jacob           = Django_User.objects.get(username='jacob')
    cubertin        = Project.objects.get(name="cubertin")
    role_manager    = Role.objects.get(name='manager')
    role_developer  = Role.objects.get(name='developer')

    manager         = ProjectMember.objects.create(user=adrian, project=cubertin)
    manager.role.add(role_manager)
    developer       = ProjectMember.objects.create(user=jacob, project=cubertin)
    developer.role.add(role_developer)

@fixture_generator(Sprint, requires=['demo.projects'])
def sprint():
    import datetime
    cubertin        = Project.objects.get(name='cubertin')
    sprint1         = Sprint.objects.create(title="sprint1", project=cubertin, deadline_at=datetime.datetime.now())

@fixture_generator(SprintTask, requires=['demo.sprint', 'demo.project_member', 'demo.task_tracker'])
def sprint_tasks():
    sprint          = Sprint.objects.get(title='sprint1')
    task_tracker    = TaskTracker.objects.get(name='task')
    assigner        = ProjectMember.objects.get(user=Django_User.objects.get(username='adrian'))
    author          = ProjectMember.objects.get(user=Django_User.objects.get(username='jacob'))
    task1           = SprintTask.objects.create(sprint=sprint, deadline_at=sprint.deadline_at, title='task1 in sprint1',
        description='tra-ta-ta', tracker=task_tracker, assigner=assigner, author=author)
