from django.contrib import admin
from django.urls import path, include
# from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title='Blog api',
        default_version="v1",
        description="A sample API for learning DRF",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hello@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    
    # this url also add log in logout button in right top corner of the api output
    path('api-auth/', include('rest_framework.urls')), # for including urls of rest_frameworks
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), # add path for login logout passwrod reset in api
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), #for registration in api
    # path('openapi', get_schema_view(
    #     title='Blog Api',
    #     description='The very basic web api which is not up to the point',
    #     version='1.0.0'
    # ), name='openapi-schema'),

    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),


]
