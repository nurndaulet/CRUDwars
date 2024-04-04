"""WarGame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from Soldiers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main_page'),
    path('AddArmy/', views.add_army, name='add_army'),
    path('fight_arm', views.fight_arm, name='fight_arm'),
    path('army/<int:army_id>/', views.army_detail_view, name='army_detail'),
    path('deleteArmy/<int:army_id>/', views.deleteArmy, name='deleteArmy'),
    path('fight/<str:cname1>/<str:cname2>/', views.fight, name="fight")
]
