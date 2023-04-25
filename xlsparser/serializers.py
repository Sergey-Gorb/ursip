from django.core import serializers
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from xlsparser.models import XlsRow


class BulkCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        result = [self.child.create(attrs) for attrs in validated_data]

        try:
            self.child.Meta.model.objects.bulk_create(result)
        except IntegrityError as e:
            raise ValidationError(e)

        update_project_last_modified(result)

        return result


class XslRowSerializer(serializers.ModelSerializer):
    # project = ModelObjectidField()

    def create(self, validated_data):
        instance = XlsRow(**validated_data)

        if isinstance(self._kwargs["data"], dict):
            instance.save()

        return instance

    class Meta:
        model = XlsRow
        fields = ("id", "name", "project", "description", "last_modified")
        read_only_fields = ("id", "last_modified")
        list_serializer_class = BulkCreateListSerializer
