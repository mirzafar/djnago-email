from django.urls import path
from main.views import *


urlpatterns = [
    path('', indexHandler),
    path('user/', adminHandler),

    path('userlist', userlistpaginations),
    # path('userlist', UserlistpaginationsListViews.as_view()),
]
