"""caunus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import urls

"""
 Add the i18n_patterns to all the other patterns but not the admin
"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('excavation/', include('excavation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='excavation/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

'''
 - Specify the url path for the media where all the image uploads reside
 - Appending it to the already existing urlpatterns
'''
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
urlpatterns += i18n_patterns(
 # Django Admin
 url(r’^{}/’.format(settings.DJANGO_ADMIN_URL), admin.site.urls),
)
"""