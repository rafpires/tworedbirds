"""two_red_birds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from rest_framework.authtoken import views


from employees.views import DepartmentViewSet, EmployeeViewSet, RoleViewSet


router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='departments')
router.register(r'employees', EmployeeViewSet, basename='employess')
router.register(r'roles', RoleViewSet, basename='roles')


schema_view = get_schema_view(
   openapi.Info(
      title="Two Red Birds APIs",
      default_version='v1',
      description="A django demo",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="rafael.andreis.pires@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
