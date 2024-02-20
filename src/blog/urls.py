from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog import settings
from posts.views import BlogHome

urlpatterns = [
                  path('', BlogHome.as_view(), name='home'),
                  path('admin/', admin.site.urls),
                  path('blog/', include('posts.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
