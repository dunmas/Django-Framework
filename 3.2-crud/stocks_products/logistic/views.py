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

    def list(self, request):
        arg = request.GET.get('search')
        found_products = []
        queryset = self.get_queryset()

        if not arg:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        for product in queryset:
            if arg.casefold() in product.title.casefold() or arg.casefold() in product.description.casefold():
                found_products.append(product)

        if len(found_products) == 0:
            return Response({'detail': f'There is no such products.'})

        serializer = self.get_serializer(found_products, many=True)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        if not pk:
            return Response({'detail': f'Request error.'})

        product = Product.objects.filter(id=pk)
        if len(product) == 0:
            return Response({'detail': f'There is no product №{pk}.'})

        product.update(description=request.data['description'])
        return Response({'detail': f'Product №{pk} is updated.'})

    def destroy(self, request, pk=None):
        if not pk:
            return Response({'detail': f'Request error.'})

        product = Product.objects.filter(id=pk)
        if len(product) == 0:
            return Response({'detail': f'There is no product №{pk}.'})

        product.delete()
        return Response({'detail': f'Product №{pk} is deleted.'})


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
