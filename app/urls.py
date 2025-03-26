"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from avarias.views import AvariasListView, NewAvariasView, AvariaDetailView, AvariaUpdateView, AvariaDeleteView
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout'),
    path('avarias/<int:pk>/', AvariaDetailView.as_view(), name= 'avarias_detail'),
    path('avarias/<int:pk>/update/', AvariaUpdateView.as_view(), name= 'avarias_update'),
    path('avarias/', AvariasListView.as_view(), name = 'avarias_list'),
    path('new_avarias/', NewAvariasView.as_view(), name = 'new_avarias'),
    path('avarias/<int:pk>/delete/', AvariaDeleteView.as_view(), name= 'avarias_delete'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


