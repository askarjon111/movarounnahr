from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from main.views import customhandler404
from django.conf.urls.static import static
from django.conf import settings
from buyurtma.routers import router

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('goal/', include('goal.urls')),
    path('chat/', include('bot.urls')),
    path('board/', include('board.urls')),
    path('task/', include('board.task_urls')),
    path('buyurtma/', include('buyurtma.urls')),
    path('mobile/', include(router.urls)),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = customhandler404
