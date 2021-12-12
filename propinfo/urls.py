from django.urls import path

from . import views

app_name = 'propinfo' # not needed but allows us to namespace the urls

urlpatterns = [
    # eg: .../propinfo/
    path('', views.index, name='index'),

    # eg: .../propinfo/detail/
    path('detail/', views.detail, name='detail'),
]
