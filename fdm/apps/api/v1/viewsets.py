from rest_framework import mixins, viewsets

from fdm.apps.accounts.models import User
from fdm.apps.api.v1.serializers import UserSerializer


class AccountViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
