"""
URL configuration for fleetproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from fleet.views import ListTaxis
from fleet.views import ListTrajectories
from fleet.views import ListTrajectoriesByID
from fleet.views import ListTrajectoriesPlate




urlpatterns = [
    path('admin/', admin.site.urls),
    path('taxis/', ListTaxis.as_view(), name='taxi_list'),
    #path('taxi/id', views.detaalle de los taxis individuales)
    # endpoint tiene que ser id de taxi y la fecha  y paginacio
    path('trajectories/', ListTrajectories.as_view(), name='trajectories_list' ),
    path('trajectories/taxi_id/', ListTrajectoriesByID.as_view(), name='trajectories_id'),
    path('plate/', ListTrajectoriesPlate.as_view(), name='plate'),
    ]
