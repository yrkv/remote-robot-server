import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import database
from .models import RobotState

#if len(RobotState.objects.all()) != 1:
RobotState.objects.all().delete()
RobotState.objects.create(state='{}')

def get_state(request):
    state = RobotState.objects.all()[0].state
    print(state)
    return HttpResponse(state)

@csrf_exempt
def set_state(request):

    if request.method == 'POST':
        state = json.loads(RobotState.objects.all()[0].state)
        RobotState.objects.all().delete()
        parsed_json = json.loads(request.body)
        state = {**state, **parsed_json}
        RobotState.objects.create(state=json.dumps(state))

    return HttpResponse('')



