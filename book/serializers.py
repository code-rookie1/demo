from rest_framework import serializers

from book import models
from book.models import BookInfo


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookInfo
        fields = '__all__'
        extra_kwargs = {'bread': {'min_value': 30}}

    # def validate(self, attrs):
    #     bread = attrs['bread']
    #     pub_date = attrs['pub_date']
    #     if bread < pub_date:
    #         raise serializers.ValidationError('阅读量是小于评论量的')
    #     return attrs

    # def create(self, validated_data):
    #     name = validated_data['name']
    #     bread = validated_data['bread']
    #     return BookInfo.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.pub_date = validated_data.get('pub_date', instance.pub_date)
    #     # instance.bread = validated_data.get('bread', instance.bread)
    #     # instance.bcomment = validated_data.get('bcomment', instance.bcomment)
    #     instance.save()
    #     return instance
