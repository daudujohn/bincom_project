from django.urls import path
from . import views as polls_views

urlpatterns = [
    path('', polls_views.index, name='index'),
    path('puresult/', polls_views.puResult),
    path('lgaresult/', polls_views.lgaResult),
    path('newresult/', polls_views.newResult),
]
