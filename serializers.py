from rest_framework import serializers

from transfer_record.models import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class DeleteRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

