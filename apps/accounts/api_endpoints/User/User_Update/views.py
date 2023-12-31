from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserUpdateSerializer


class UserUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user


__all__ = ['UserUpdateAPIView']
