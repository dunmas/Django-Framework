from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (['title', 'description'])


class ProductPositionSerializer(serializers.ModelSerializer):
    stock = serializers.StringRelatedField()

    class Meta:
        model = StockProduct
        fields = (['stock', 'product', 'quantity', 'price'])


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = (['address', 'positions'])

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        for product in positions:
            StockProduct.objects.create(stock=stock, product=product['product'],
                                        quantity=product['quantity'], price=product['price'])

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        for product in positions:
            StockProduct.objects.update_or_create(stock=instance, product=product['product'],
                                                  defaults={'price': product['price'],
                                                            'quantity': product['quantity']})

        return stock
