from rest_framework import serializers

class AlertSerializer(serializers.Serializer):
    symbol = serializers.CharField()
    exchange = serializers.CharField()
    currency = serializers.CharField()
    action = serializers.CharField()
    quantity = serializers.CharField()
    time = serializers.CharField()
