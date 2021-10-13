from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.conf import settings

from django_slack_event_wrapper.verify_signature import validate_request
from django_slack_event_wrapper.events import slack_event_trigger, slash_event_trigger


try:
    settings.VERIFICATION_TOKEN
    settings.SIGNING_SECRET
    settings.APP_ID

except Exception as e:
    raise Exception(
        """
        seems like your configurations aren't rightly done.
        Check to ensure that you have set your [
            VERIFICATION_TOKEN,
            APP_ID,
            SIGNING_SECRET
        ]
    """
    )


class SlackEventView(APIView):
    # validates all incomming request
    @method_decorator(validate_request)
    def dispatch(self, *args, **kwargs):
        return super(SlackEventView, self).dispatch(*args, **kwargs)

    def post(self, request):
        received_data = request.data
        if received_data['type'] and received_data['type'] == 'url_verification':
            return Response({'challenge': received_data['challenge']}, status="200")

        if received_data['type'] == 'app_rate_limited':
            return Response(None, status="200")

        token = received_data['token']
        app_id = received_data['api_app_id']

        # extra layer for verification of requests
        if not token == settings.VERIFICATION_TOKEN and app_id == settings.APP_ID:
            return Response(None, status="403")

        # work space event occured
        team_id = received_data['team_id']
        # Holds field data for occuring event
        event = received_data['event']
        # Event that occured
        event_type = event['type']

        return slack_event_trigger(team_id=team_id, event_type=event_type, event=event)


class SlashCommandView(APIView):

    # validates all incomming request
    @ method_decorator(validate_request)
    def dispatch(self, *args, **kwargs):
        return super(SlashCommandView, self).dispatch(*args, **kwargs)

    def post(self, request):
        received_data = request.data
        user_id = received_data.get('user_id')
        channel_id = received_data.get('channel_id')
        # dispatch event
        slash_event_trigger(user_id=user_id, channel_id=channel_id, slash_event_data=received_data)
        return Response(status="200")
