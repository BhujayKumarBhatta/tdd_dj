
# from django.conf.urls import url
# from django.contrib import admin
# 
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]


"""tdd_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
    
'''
from django.urls import path
https://docs.djangoproject.com/en/2.1/topics/http/urls/

from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
'''    
    
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
from django.conf.urls import path
#from django.urls import include, url
#from django.conf.urls import url, include may be older way of doing
from lists.views import home_page
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name = 'home_page')  
     #path(r'^$', home_page, name = 'home_page')  , doesn't work  
     #url(r'^$', home_page, name = 'home_page'), i think it is older way of doing 

]

