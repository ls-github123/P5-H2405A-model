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
    path("test/", Test.as_view()),
    path('ask/',Ask.as_view()),
    path('streamask/',StreamAsk.as_view()),
    path('sseview/',sse_view),
    path('toolsView/',ToolsView.as_view()),
    path('toolsCall/',ToolsCall.as_view()),
    # path('sse/',sse_views),
    path('echartssse/',echartssse),
    path('randromCount/',RandromCount.as_view()),
    path('cates/',CatesView.as_view()),
    path('questions/',QuestionsView.as_view()),
    path('catesall/',Catesall.as_view()),
    path('ddurl/',DDUrl.as_view()),
    path('ddcallback/',DDcallback.as_view()),
    path('testSMM/',TestSMM.as_view()),
    path("movieData/",MovieData.as_view()),
    path('testFasiss/',TestFasiss.as_view()),
    path('fileUpload/',FileUpload.as_view()),
    path('sse/',sse_notifications),
    path('memoryTest/',qustions_ask),
    path('askMessage/',AskMessage.as_view()),
    path('upload/',FUPload.as_view()),
    path('testFaiss/',TestFaiss.as_view()),
    path('testBd/',TestBd.as_view()),
    path('publishView/',PublishView.as_view()),
    path('crmManager/',CrmManager.as_view())
]
