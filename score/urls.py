from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'', views.table_list, name='table_list'),
]
