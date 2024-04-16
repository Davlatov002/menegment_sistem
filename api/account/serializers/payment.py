from rest_framework import serializers

from apps.account.models.payment import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [
            'id',
            'price_sum',
            'student',
            'paid_time',
            'mothly',
        ]
