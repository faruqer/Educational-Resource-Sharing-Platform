from rest_framework import serializers

from resources.models import Category, Resource


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class ResourceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source='category',
        queryset=Category.objects.all(),
        write_only=True,
    )
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Resource
        fields = (
            'id',
            'title',
            'description',
            'category',
            'category_id',
            'resource_type',
            'file',
            'external_url',
            'created_by',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, attrs):
        file_data = attrs.get('file') or getattr(self.instance, 'file', None)
        external_url = attrs.get('external_url') or getattr(self.instance, 'external_url', '')
        if not file_data and not external_url:
            raise serializers.ValidationError('Provide either a file or an external URL.')
        return attrs
