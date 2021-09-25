from rest_framework import serializers

from EnvergaDB.models import Records


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Records
        fields = ('id', 'author', 'description', 'date_modified',
                  'date_created', 'status')
