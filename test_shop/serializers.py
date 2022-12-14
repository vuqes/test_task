from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    status = serializers.CharField(source='status.status_value')
    
    class Meta:
        model = Product
        fields = '__all__'


class DetailProductSerializer(serializers.ModelSerializer):
    image = SerializerMethodField()

    def get_image(self, obj):
        image_path, file_extension = obj.image.url.split('.')
        return {
                'path': image_path,
                'formats': [file_extension]
        }

    class Meta:
        model = Product
        fields = '__all__'
