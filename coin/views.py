from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Space

def index(request):
    latest_space_list = Space.objects.order_by('-create_date')[:10]
    context = {
        'latest_space_list': latest_space_list,
    }
    return render(request, 'index.html', context)


def title(request, space_id):
    space = get_object_or_404(Space, pk=space_id)
    return render(request, 'title.html', {'space': space})
    # try:
    #     space = Space.objects.get(pk=space_id)
    # except Space.DoesNotExist:
    #     raise Http404("Space does not exist")
    # return render(request, 'title.html', {'space': space})


def content(request, space_id):
    response = "You're looking at the content of space %s."
    return HttpResponse(response % space_id)

