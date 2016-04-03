# Using URL patterns to match a URL to view logic
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from restapi.bubbletea import views

# Use of routers to return class viewsets (endpoints), making use of "api/v1/" API URL-setting conventions
router = routers.DefaultRouter()
router.register(r'franchises', views.FranchiseViewSet, 'franchise')
router.register(r'locations', views.LocationViewSet, 'location')
router.register(r'drinks', views.DrinkViewSet)
router.register(r'reviews', views.ReviewViewSet)

# Add login oppurtunity for use through browserable API
# Add URL for API docs
urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
