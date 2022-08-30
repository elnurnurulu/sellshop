
from django.urls import path
from core.api.views import SubscriberAPIView

urlpatterns = [
    path('subscribers/', SubscriberAPIView.as_view(),),
]
