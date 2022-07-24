from django.core.paginator import Paginator
from django.shortcuts import render
from .task import *
from main.models import *
import validators
from django.http.response import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView


def indexHandler(request):
    if request.POST:
        action = request.POST.get('action', '')
        errors = []
        if action == 'send_email':
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')

            ch = Email()
            if email:
                if validators.email(email):
                    ch.email = email
                else:
                    errors.append("не правильный email")
            else:
                errors.append('Не заполнена')
            if password:
                ch.password = password
            else:
                errors.append('Не заполнена')
            ch.status = 0
            if not errors:
                ch.save()
                # send_message.delay(email, ch.id)
                response = JsonResponse({'status': True}, status=200)
            else:
                response = JsonResponse({'status': False, 'errors': errors}, status=200)
            return response

    return render(request, 'index.html', {})


def adminHandler(request):
    action = request.POST.get('add_user')
    errors = []
    if request.POST:
        last_name = request.POST.get('last_name', '')
        first_name = request.POST.get('first_name', '')
        email = request.POST.get('email', '')
        login = request.POST.get('login', '')
        password = request.POST.get('password', '')
        logo = request.FILES['logo']

        user = User()
        if last_name:
            user.last_name = last_name
        else:
            errors.append('не заполнена имя')
        if first_name:
            user.first_name = first_name
        else:
            errors.append('не заполнена фамиля')
        if email:
            user.email = email
        else:
            errors.append('не заполнена почта')
        if login:
            user.login = login
        else:
            errors.append('не заполнена логин')
        if password:
            user.password = password
        else:
            errors.append('не заполнена пароль')

        fs = FileSystemStorage()
        name = fs.save("upload/" + logo.name, logo)


        user.logo = name
        if not errors:
            user.save()
            response = JsonResponse({'status': True}, status=200)
        else:
            response = JsonResponse({'status': False, 'errors': errors})
        return response
    return render(request, 'user.html', {})


# pagination in function
# def userlistpaginations(request):
#     users = User.objects.all()
#     paginator = Paginator(users, 3)
#     page_number = request.GET.get('page', 1)
#     users_obj = paginator.get_page(page_number)
#
#     context = {
#         'users_obj': users_obj,
#         'users': users
#     }
#
#     return render(request, 'userlistpaginations.html', context)


def userlistpaginations(request):
    users_list = User.objects.all()
    paginator = Paginator(users_list, 3)
    page_number = request.GET.get('page', 1)
    users = paginator.get_page(page_number)

    context = {
        'users': users
    }

    return render(request, 'userlistpaginations.html', context)


# pagination in class-based
class UserlistpaginationsListViews(ListView):
    model = User
    context_object_name = 'users'
    paginate_by = 3
    template_name = 'pagination.html'


