from django.urls import path
from django_slack_event_wrapper import views

app_name = 'django_slack_event_wrapper'

urlpatterns = [
    path('events', views.SlackEventView.as_view()),
    path('slash-commands', views.SlashCommandView.as_view()),
]
