from django.urls import path
from .views import BotUsersApiView, FeedbacksApiView

urlpatterns = [
               path('bot-users', BotUsersApiView.as_view(), name='bot-users'),
               path('feedbacks', FeedbacksApiView.as_view(), name='feedbacks'),
               ]