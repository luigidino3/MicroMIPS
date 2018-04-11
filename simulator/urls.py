from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.reset, name = 'reset'),
    url(r'^menu$', views.home, name = 'home'),
    url(r'^registerValuesChanged$', views.registeredReg, name = 'registeredReg'),
    url(r'^changeDataMemory$', views.changeDataMemory, name='changeDataMemory'),
	url(r'^inputRegisters/', views.inputReg, name = 'inputReg'),
    url(r'^gotoMemory/', views.gotoMemory, name = 'gotoMemory'),
    url(r'^programRegistered/', views.programRegistered, name='programRegistered'),
	url(r'^pipeline/', views.pipeline, name = 'pipeline'),
    url(r'^clearedPipeline/', views.purge, name = 'purge'),
]
