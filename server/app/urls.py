from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.Home.as_view(), name='home'),
	url(r'^partners/', views.Partners.as_view(), name= 'partners'),
	url(r'^about_us/', views.AboutUs.as_view(), name= 'about_us'),
	url(r'^donate/', views.Donations.as_view(), name= 'donate'),
	url(r'^leadership/', views.Leadership.as_view(), name= 'leadership'),
	url(r'^contact_us/', views.ContactUs.as_view(), name= 'contact_us'),
	url(r'^admin_login/', views.AdminLogin.as_view(), name= 'admin_login'),
	url(r'^events/', views.Events.as_view(), name= 'events'),
	url(r'^news/', views.News.as_view(), name= 'news'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
