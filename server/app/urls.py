from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	url(r'^$', views.Home.as_view(), name='home'),
	url(r'^partners/', views.Partners.as_view(), name= 'partners'),
	url(r'^aade_tamuk/', views.AadeTamuk.as_view(), name= 'aade_tamuk'),
	url(r'^aade_central_texas/', views.AadeCentralTexas.as_view(), name= 'aade_central_texas'),
	url(r'^donations/', views.Donations.as_view(), name= 'donations'),
	url(r'^officers/', views.Officers.as_view(), name= 'officers'),
	url(r'^contact_us/', views.ContactUs.as_view(), name= 'contact_us')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
