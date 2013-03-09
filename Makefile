sql:
	../pm_scrum_venv/bin/python ./manage.py sqlall projects
test:
	../pm_scrum_venv/bin/python ./manage.py runtest
demo:
	../pm_scrum_venv/bin/python ./manage.py loaddata users role projects task_statuses task_tracker project_member sprint sprint_tasks
