from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^', include('simulator.urls')),
	url(r'^home/', include('simulator.urls')),
    url(r'^admin/', admin.site.urls),
]
