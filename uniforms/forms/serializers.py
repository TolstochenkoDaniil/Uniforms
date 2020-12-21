from rest_framework import serializers
from .models import Form


class FormListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['name', 'url', 'creation_date']
        read_only_fields = ['creation_date']


class FormParametersSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    url = serializers.URLField()
    edit_url = serializers.URLField()
    university = serializers.CharField()
    discipline = serializers.CharField()
    is_valid = serializers.BooleanField()


class FormSerializer(serializers.HyperlinkedModelSerializer):
    form_params = FormParametersSerializer(source='*')

    def create(self, validated_data, user_id=None):
        params = validated_data.get('form_params')

        form, created = Form.objects.update_or_create(
            user_id=user_id.replace('-',''),
            defaults=params
        )

        return form, created

    class Meta:
        model = Form
        fields = ['form_params']