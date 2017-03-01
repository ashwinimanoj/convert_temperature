"""temperature URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from temperature.views import display_root, \
	convert_fahrenheit,convert_celsius, convert_kelvin, \
	convert_rankine

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', display_root),
    url(r'^convert/fahrenheit/(\d+)', convert_fahrenheit),
    url(r'^convert/celsius/(\d+)', convert_celsius),
    url(r'^convert/kelvin/(\d+)', convert_kelvin),
    url(r'^convert/rankine/(\d+)', convert_rankine),
    
]
