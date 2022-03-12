from rest_framework import serializers
from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['driver_name', 'init_load', 'init_amount', 'init_km', 'fin_load', 'fin_amount',
                  'fin_km', 'status', 'cause']
