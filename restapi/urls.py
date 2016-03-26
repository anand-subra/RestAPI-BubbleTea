# Using URL patterns to match a URL to view logic
from django.conf.urls import url, include
from rest_framework import routers
from restapi.bubbletea import views


# Use of routers to return class viewsets (endpoints), making use of "api/v1/" API URL-setting conventions
router = routers.DefaultRouter()
router.register(r'api/v1/franchises', views.FranchiseViewSet)
router.register(r'api/v1/locations', views.LocationViewSet)
router.register(r'api/v1/drinks', views.DrinkViewSet)
router.register(r'api/v1/reviews', views.ReviewViewSet)


# Add login oppurtunity for use through browserable API
# Add URL for API docs
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
