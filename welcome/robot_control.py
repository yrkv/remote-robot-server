import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


state = {}

def get_state(request):
    return HttpResponse(json.dumps(state))

@csrf_exempt
def set_state(request):
    global state

    if request.method == 'POST':
        parsed_json = json.loads(request.body)
        state = {**state, **parsed_json}

    return HttpResponse('')



