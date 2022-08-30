from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from user.api.serializers import UserSerializer

User = get_user_model()


class UserProfileAPIView(RetrieveAPIView):
    # permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user