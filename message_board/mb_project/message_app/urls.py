from django.conf.urls import url

from .views import Home_Page_view

urlpatterns=[
url(r'^$',Home_Page_view.as_view()),
]