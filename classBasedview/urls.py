"""
URL configuration for classBasedview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.views.generic import TemplateView
from mainApp import views


urlpatterns = [
    path('admin/', admin.site.urls),

    #template based url passing 
    # path("", TemplateView.as_view(template_name="index.html"),name="home"), 
    
    # function based url    
    # path("",views.homepage,name="home"),

    #class based url
    path("", views.EmployeeClassView.as_view(), name="home"),

    #function based addPage
    # path("addPage/",views.addPage,name='add'),

    #class based url passing
    path("addPage/", views.EmployeePostclassView.as_view(), name="add"),

    #function based deletPage
    # path("delete/<int:id>/",views.deletePage, name='delete'),

    #class based deletePage
    path('delete/<int:id>/', views.EmployeeDeletePage.as_view(),name="delete"),


    #function basedUpdatepage
    #path("update/<int:id>/",views.updatePage,name="update"),
    path("update/<int:id>/", views.EmployeeUpdateView.as_view(),name="update"),








]
