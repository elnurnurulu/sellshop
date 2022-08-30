from rest_framework.generics import CreateAPIView
from core.api.serializers import SubscriberSerializer
from core.models import Subscriber
from rest_framework import status,permissions
from rest_framework.response import Response

class SubscriberAPIView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head','post']

    serializer_class = SubscriberSerializer
    queryset_class = Subscriber.objects.all()

    def get(self,request, *args, **kwargs):
        subscriber = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscriber, many = True)
        return Response(serializer.data)

        
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        email = request.data.get('email')
        if Subscriber.objects.filter(email=email).exists() == False:
            if serializer.is_valid():
                Subscriber.objects.create(email=email)
                message = {'success': True,
                           'message': 'Subscriber added.'}
                return Response(message, status=status.HTTP_201_CREATED)
            else:
                message = {'success': False,
                           'message': 'Invalid email address.'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        message = {'success': False,
                   'message': 'Subscriber already exists.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
