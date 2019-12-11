from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('register', views.TowaryView)
router.register('logowanie', views.KuponyView)


urlpatterns = [
    path('', include(router.urls)),
]