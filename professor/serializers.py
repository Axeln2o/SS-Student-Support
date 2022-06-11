from rest_framework import serializers

from professor.models import Professor


class ProfessorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professor
        fields = ['first_name', 'last_name', 'department', 'time']