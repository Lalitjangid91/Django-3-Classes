from django.urls import path
from . import views
urlpatterns=[
    path('',views.BoyHome,name='lalit'),
    path('addboy/',views.AddBoy,name='addboy'),
]
