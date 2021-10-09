"""config URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from posts.views import new, create, list, detail, update
from account.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('', list, name='list'),
    path('<int:id>/', detail, name='detail'),
    path('<int:id>/update/', update, name='update'),
    # path('<int:id>/delete/', delete, name='delete'),
    path('account/signup/', signup, name='signup'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
