from rest_framework import routers

from fdm.apps.api.v1.viewsets import AccountViewSet


api_router = routers.SimpleRouter()
api_router.register('users', AccountViewSet)
