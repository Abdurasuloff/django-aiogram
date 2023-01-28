from .models import BotUser, Feedback
from .serializers import BotUserSerializer, FeedbackSerializer
from rest_framework.generics import ListCreateAPIView

class BotUsersApiView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class  = BotUserSerializer

class FeedbacksApiView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class  = FeedbackSerializer
