"""rateme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from core.views import  avaliacao_delete, avaliacao_update, pessoa_update, pessoa_delete, list_home, pessoa_create, pessoa_home, produto_home, produto_create, avaliacao_create, produto_update, produto_delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pessoa/', pessoa_home, name = 'url_pessoa_home'),
    path('produto/', produto_home, name = 'url_produto_home'),
    path('', list_home, name = 'url_home'),
    path('pessoa/create', pessoa_create, name = 'url_pessoa_create'),
    path('produto/create', produto_create, name = 'url_produto_create'),
    path('avaliacao/create', avaliacao_create, name = 'url_avaliacao_create'),
    path('produto/update/<int:pk>/', produto_update, name = 'url_produto_update'),
    path('produto/delete/<int:pk>/', produto_delete, name = 'url_produto_delete'),
    path('pessoa/update/<int:pk>/', pessoa_update, name = 'url_pessoa_update'),
    path('pessoa/delete/<int:pk>/', pessoa_delete, name = 'url_pessoa_delete'),
    path('avaliacao/update/<int:pk>/', avaliacao_update, name = 'url_avaliacao_update'),
    path('avaliacao/delete/<int:pk>/', avaliacao_delete, name = 'url_avaliacao_delete')
]
