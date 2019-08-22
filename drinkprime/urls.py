"""drinkprime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from warehouse import views,apiviews
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^login/', views.LoginView),
    url(r'^api/v1/rest-auth/', include('rest_auth.urls')),
    url(r'^api/v1/rest-auth/awarehouselist/(?P<pk>[0-9]+)/$', views.AssemblyWarehouseDetails.as_view()),
    url(r'^api/v1/rest-auth/awarehousecreate/', views.AssemblyWarehouseList.as_view()),
    url(r'^api/v1/rest-auth/awreadyfortransport/(?P<purifierid>[\w\-]+)/$', views.ReadyForTransportCityWarehouse.as_view()),
    url(r'^api/v1/rest-auth/awpurifierretured/(?P<purifierid>[\w\-]+)/$', views.PurifierReturned.as_view()),

    url(r'^api/v1/rest-auth/userdetail/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.UserDetail.as_view()),

    url(r'^api/v1/rest-auth/cwpurifiershifted/(?P<purifierid>[\w\-]+)/$', views.PurifierShiftedCityWarehouse.as_view()),
    url(r'^api/v1/rest-auth/cwarehousecreate/', views.CityWarehouseList.as_view()),
    url(r'^api/v1/rest-auth/cwreadyfortransport/(?P<purifierid>[\w\-]+)/$', views.ReadyForTransportSubWarehouse.as_view()),
    url(r'^api/v1/rest-auth/cwpurifierretured/(?P<purifierid>[\w\-]+)/$', views.CWPurifierReturned.as_view()),

    url(r'^api/v1/rest-auth/swpurifiershifted/(?P<purifierid>[\w\-]+)/$', views.PurifierShiftedSubWarehouse.as_view()),
    url(r'^api/v1/rest-auth/swarehousecreate/', views.SubWarehouseList.as_view()),
    url(r'^api/v1/rest-auth/swreadyfortransport/(?P<purifierid>[\w\-]+)/$', views.ReadyForTransportCustomer.as_view()),
    url(r'^api/v1/rest-auth/swpurifierreturned/(?P<purifierid>[\w\-]+)/$', views.SWPurifierReturned.as_view()),

    url(r'^api/v1/rest-auth/customerreceived/(?P<purifierid>[\w\-]+)/$', views.PurifierReceivedByCustomer.as_view()),

    url(r'^api/v1/rest-auth/totalcitywarehouselist/', views.TotalCityWarehouseDetails.as_view()),
    url(r'^api/v1/rest-auth/totalsubwarehouselist/', views.TotalSubWarehouseDetails.as_view()),

    #admin panel urls api's
    url(r'^api/v1/rest-auth/totalawpurifier/', apiviews.AssemblyWarehousePurifierCount.as_view()),
    url(r'^api/v1/rest-auth/totalawpurifierhold/', apiviews.AssemblyWarehousePurifierHoldCount.as_view()),
    url(r'^api/v1/rest-auth/totalawpurifiertransit/', apiviews.AssemblyWarehousePurifierTransitCount.as_view()),
    url(r'^api/v1/rest-auth/totalawpurifiershifted/', apiviews.AssemblyWarehousePurifierShiftedCount.as_view()),
    url(r'^api/v1/rest-auth/awpurifierhold/', apiviews.AssemblyWarehousePurifierHold.as_view()),
    url(r'^api/v1/rest-auth/awpurifiertransit/', apiviews.AssemblyWarehousePurifierTransit.as_view()),
    url(r'^api/v1/rest-auth/awpurifiershifted/', apiviews.AssemblyWarehousePurifierShifted.as_view()),

    url(r'^api/v1/rest-auth/totalcwpurifier/', apiviews.CityWarehousePurifierCount.as_view()),
    url(r'^api/v1/rest-auth/totalcwwisepurifier/', apiviews.CityWarehouseWisePurifierCount.as_view()),
    url(r'^api/v1/rest-auth/totalcwpurifierhold/', apiviews.CityWarehousePurifierHoldCount.as_view()),
    url(r'^api/v1/rest-auth/totalcwpurifiertransit/', apiviews.CityWarehousePurifierTransitCount.as_view()),
    url(r'^api/v1/rest-auth/totalcwpurifiershifted/', apiviews.CityWarehousePurifierShiftedCount.as_view()),
    url(r'^api/v1/rest-auth/cwpurifierhold/', apiviews.CityWarehousePurifierHold.as_view()),
    url(r'^api/v1/rest-auth/cwpurifiertransit/', apiviews.CityWarehousePurifierTransit.as_view()),
    url(r'^api/v1/rest-auth/cwpurifiershifted/', apiviews.CityWarehousePurifierShifted.as_view()),

    url(r'^api/v1/rest-auth/totalswpurifier/', apiviews.SubWarehousePurifierCount.as_view()),
    url(r'^api/v1/rest-auth/totalswwisepurifier/', apiviews.SubWarehouseWisePurifierCount.as_view()),
    url(r'^api/v1/rest-auth/totalswpurifierhold/', apiviews.SubWarehousePurifierHoldCount.as_view()),
    url(r'^api/v1/rest-auth/totalswpurifiertransit/', apiviews.SubWarehousePurifierTransitCount.as_view()),
    url(r'^api/v1/rest-auth/totalswpurifiershifted/', apiviews.SubWarehousePurifierShiftedCount.as_view()),
    url(r'^api/v1/rest-auth/swpurifierhold/', apiviews.SubWarehousePurifierHold.as_view()),
    url(r'^api/v1/rest-auth/swpurifiertransit/', apiviews.SubWarehousePurifierTransit.as_view()),
    url(r'^api/v1/rest-auth/swpurifiershifted/', apiviews.SubWarehousePurifierShifted.as_view()),

    url(r'^api/v1/rest-auth/custdetails/', apiviews.CustomerDetails.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)