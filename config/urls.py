from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    
    # this url also add log in logout button in right top corner of the api output
    path('api-auth/', include('rest_framework.urls')), # for including urls of rest_frameworks
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), # add path for login logout passwrod reset in api
]
