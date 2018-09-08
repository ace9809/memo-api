"""memo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from api import views


"""
urlpatterns = [
    #path('', views.api_root),
    path('memo-list/create/', views.MemoCreate.as_view(), name="memo-create"),
]
"""

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    #url(r'^api-auth/', include('rest_framework.urls')),
    path('memo-list/', views.MemoList.as_view(), name="memo-list"),
    path('memo-list/<int:pk>/', views.MemoDetail.as_view(), name="memo-detail"),
    path('memo-list/create/', views.MemoCreate.as_view(), name="memo-create"),
    path('memo-list/update/', views.MemoUpdate.as_view(), name="memo-update"),
    path('memo-list/destroy/', views.MemoDestroy.as_view(), name="memo-destroy"),
])
