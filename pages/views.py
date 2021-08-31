from django.http import JsonResponse
from django.shortcuts import redirect

from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from pages.models import UserInfo


def index(request):
    return render(request, 'pages/index.html')


def search(request):
    users_list = UserInfo.objects.all()
    search_dict = request.GET.copy()
    keyword = search_dict.get('keyword')

    if keyword is not None:
        keyword = search_dict['keyword']
        users_list = users_list.filter(details__icontains=keyword).distinct()  # django == Django Web development

    context = {
        'users_list': users_list,
    }
    return render(request, 'pages/search_result.html', context)


def filter_name(request):
    users_list = UserInfo.objects.all()
    users = request.GET.getlist('name[]')
    if len(users) > 0:
        users_list = users_list.filter(name__icontains=users).distinct()
    t = render_to_string('pages/filter_view.html', {'data': users_list})
    return JsonResponse({'data': t})
