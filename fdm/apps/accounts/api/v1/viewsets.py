from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from fdm.apps.accounts.api.v1.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from fdm.apps.accounts.models import User
from fdm.apps.accounts.api.v1.serializers import UserSerializer


class AccountViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
