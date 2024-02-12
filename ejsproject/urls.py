
from django.contrib import admin
from django.urls import path, include, re_path
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter
from ejsapp.views import MarkViewSet, SubjectViewSet, StudentViewSet, DateViewSet

router = DefaultRouter()
router.register('marks', MarkViewSet)
router.register('subjects', SubjectViewSet)
router.register('students', StudentViewSet)
router.register('dates', DateViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path(r'api/auth/', include('djoser.urls')),
    re_path(r'api/auth/', include('djoser.urls.authtoken')),
]
