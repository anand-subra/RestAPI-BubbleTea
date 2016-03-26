"""filmlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
"""
from django.conf.urls import url, include
#
from rest_framework import routers
from filmlist.quickstart import views

router = routers.DefaultRouter()
router.register(r'api/v1/franchises', views.FranchiseViewSet)
router.register(r'api/v1/locations', views.LocationViewSet)
router.register(r'api/v1/drinks', views.DrinkViewSet)
router.register(r'api/v1/reviews', views.ReviewViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
