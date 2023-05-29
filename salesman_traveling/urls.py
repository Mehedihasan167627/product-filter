from django.urls import path 
from .views import*

app_name="salesman_traveling"
urlpatterns=[
    path("best-route-generate/",CreateBestRouteView.as_view(),name='generate'),
    path("best-route/",ShowBestRouteView.as_view(),name='show_route'),
 
]