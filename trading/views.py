# trading/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlertSerializer
from django.conf import settings
from . import ib
from pymongo import MongoClient
from datetime import datetime
import pytz

mongo = MongoClient(settings.MONGO_URI)
db = mongo["tradingview_ib"]
alerts_collection = db["alerts"]

@api_view(['POST'])
def tradingview_webhook(request):
    print("📩 Raw request data:", request.body.decode())
    serializer = AlertSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data
    action = data['action']
    symbol = data['symbol']
    exchange = data['exchange']
    currency = data['currency']
    qty = data['quantity']
    time_str = data['time']

    # Parse time
    try:
        formatted_time = datetime.fromisoformat(time_str.replace("Z", "+00:00")).astimezone(pytz.UTC).strftime("%Y-%m-%d %H:%M:%S")
    except:
        formatted_time = time_str

    # Get margin & positions before
    margin_before = ib.get_margin()
    positions_before = ib.get_positions()

    # Trade
    try:
        contract = ib.Stock(symbol, exchange, currency)
        ib.ib.qualifyContracts(contract)
        order = ib.MarketOrder(action, qty)
        trade = ib.ib.placeOrder(contract, order)
        ib.ib.sleep(2)
    except Exception as e:
        return Response({
        "error": "Failed to place order",
        "details": str(e)
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Get margin & positions after
    margin_after = ib.get_margin()
    positions_after = ib.get_positions()

    # Log to MongoDB
    alerts_collection.insert_one({
        "symbol": symbol,
        "exchange": exchange,
        "currency": currency,
        "action": action,
        "quantity": qty,
        "time": formatted_time,
        "order_status": trade.orderStatus.status,
        "margin_before": margin_before,
        "margin_after": margin_after,
        "positions_before": positions_before,
        "positions_after": positions_after,
        "created_at": datetime.utcnow()
    })

    return Response({
        "status": "success",
        "order_status": trade.orderStatus.status,
        "margin_before": margin_before,
        "margin_after": margin_after,
        "positions_before": positions_before,
        "positions_after": positions_after
    })
