from rest_framework import serializers
from api.models import Reviews,Books
from django.contrib.auth.models import User

class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    author=serializers.CharField()
    price=serializers.IntegerField()
    publisher=serializers.CharField()
    qty=serializers.IntegerField()

    def create(self, validated_data):
        return Books.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get("name")
        instance.author = validated_data.get("author")
        instance.publisher= validated_data.get("publisher")
        instance.qty= validated_data.get("qty")
        instance.save()
        return instance


    # FIELD LEVEL VALIDATION
    # def validate_price(self,value):
    #     if value not in range(50,1000):
    #         raise serializers.ValidationError("invalid price")
    #     return value
    #
    #
    # def validate_qty(self,value):
    #     if value not in range(1,500):
    #         raise serializers.ValidationError("invalid quantity")
    #     return value


    # OBJECT LEVEL VALIDATION BY OVERRIDING VALIDATE METHOD
    def validate(self,data):
        price=data.get("price")
        qty=data.get("qty")
        if qty not in range(1,500):
            raise serializers.ValidationError("invalid quantity")
        if price not in range(50,1000):
            raise serializers.ValidationError("invalid price")
        return data



class ReviewSerializer(serializers.ModelSerializer):
    created_date=serializers.CharField(read_only=True)

    class Meta:
        model=Reviews
        fields="__all__"
        # exclude=("created_date",)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)