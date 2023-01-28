from .models import BotUser, Feedback
from rest_framework.serializers import ModelSerializer

class BotUserSerializer(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ("name", "username", "user_id", "created_at")
       
class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("user_id",  "created_at", "body")
