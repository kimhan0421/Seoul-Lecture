from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from posts.views import new, create, list, detail, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('', list, name='list'),
    path('<int:id>/', detail, name='detail'),
    path('<int:id>/update/', update, name='update'),
    # path('<int:id>/delete/', delete, name='delete'),

    path('account/', include('account.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
