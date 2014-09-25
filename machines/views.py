from django.shortcuts import render_to_response
from django.template.context import RequestContext

from machines.models import Machine

# Create your views here.

def mainpage(request):
    machines = Machine.objects.all()
    user = request.user
    return render_to_response('machines/mainpage.html', \
        RequestContext(request, {'user':user, 'machines': machines, }))
