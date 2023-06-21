from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filterset_class = AdvertisementFilter

    # А зачем вообще переопределять для методов? Через класс-наследник BasePermission вроде как хорошо
    # валидируются как изменение, так и удаление объявления

    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update"]:
    #         return [IsAuthenticated()]
    #     return []

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
