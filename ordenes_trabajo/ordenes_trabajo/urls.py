"""
URL configuration for ordenes_trabajo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from ordenes_trabajo.gestion_ordenes  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('estado/', views.estado, name='estado'),
    path('odts/', views.odts, name='odts'),
    path('odts/crear/', views.crear_odt, name='crear_odt'),
    path('odts/<int:odt_id>/', views.detalle_odt, name='detalle_odt'),
    path('odts/<int:odt_id>/editar/', views.editar_odt, name='editar_odt'),
    path('odts/<int:odt_id>/eliminar/', views.eliminar_odt, name='eliminar_odt'),
    path('odts/<int:odt_id>/estado/', views.actualizar_estado_odt, name='actualizar_estado_odt'),
]
