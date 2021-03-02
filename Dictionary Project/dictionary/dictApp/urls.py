from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import HeadwordViewSet
    # , POSViewSet, MeaningViewSet
from . import form_views 
router = routers.DefaultRouter()

router.register('headword', HeadwordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("dict", form_views.head_word_view)
]