from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации

    def create(self, request):
        Product.objects.create(title=request.data['title'], description=request.data['description'])

        return Response({'detail': 'Product is added.'})

    def retrieve(self, request, pk=None):
        pass

    # def list(self, request):
    #     pass

    def update(self, request, pk=None):
        pass

    # TODO: тут лажа, переделать
    def destroy(self, request, pk=None):
        product = Product.objects.filter(id=pk)

        if len(product._result_cache) == 0:
            return Response({'detail': f'There is no product №{pk}.'})

        product.delete()
        return Response({'detail': f'Product №{pk} is deleted.'})


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
