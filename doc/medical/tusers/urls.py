"""
URL configuration for medical project.

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

from django.urls import path
from .views import *

urlpatterns = [
    path("ddurl/", DingdingUrl.as_view()),
    path("user/dingtalkCallback/", DingdingCallback.as_view()),
    path('getQnToken/',QnToken.as_view()),
    path('idcode/',Idcard.as_view()),
    path('baiduUsermes/',BaiduUsermes.as_view()),
    path('search/',DockerSearch.as_view()),
    path('message/',MessageView.as_view()),
    path('testWebsocket/',TestWebsocket.as_view()),
    path('departments/',DeptManager.as_view()),
    path('aricleComment/',AricleComment.as_view()),
    path('patients/',Patients.as_view()),
    path('preorder/',Preorder.as_view()),
    path('orderskey/',Orderskey.as_view()),
    path('orders/',OrdersView.as_view()),
    path('pay/',Pay.as_view()),
    path('alipaycallback/',Alipaycallback.as_view()),
    path('upload/',FileUpload.as_view()),
    path('sse/',sse_notifications),
    path('patient/consult/order/list',Patients.as_view()),
    path('TestDoctor/',TestDoctor.as_view()),
    path('testDemo/',TestDemo.as_view()),
    path('testMongo/',TestMongo.as_view()),
    path('fileupload/',fileupload)
   
]
