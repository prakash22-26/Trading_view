from django.urls import path
from .views import tradingview_webhook

urlpatterns = [
    path("", tradingview_webhook),  # POST /webhook/
]
