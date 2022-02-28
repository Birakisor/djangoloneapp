from django.urls import path
from loanapp import views


urlpatterns = [
    path('',views.loancal,name='loancal'),
    #path('loancheck',views.loancheck,name='loancal')
]
