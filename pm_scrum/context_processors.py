from projects.models import Project, Sprint

__author__ = 'djakson'

import re

def project(request):
    parse = re.search('^/(\d+).*/$', request.path)
    if parse is None:
        return {}
    project_id = parse.group(1)
    if project_id:
        return {'project': Project.objects.get(pk=int(project_id))}
    return {}

def sprint(request):
    try:
        parse = re.search('^/\d+/sprint/(\d+)/', request.path)
        if parse is None:
            return {}
        sprint_id = parse.group(1)
        if sprint_id:
            return {'sprint': Sprint.objects.get(pk=int(sprint_id))}
        return {}
    except:
        return {}