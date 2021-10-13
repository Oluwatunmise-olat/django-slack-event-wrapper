from rest_framework.response import Response

from django_slack_event_wrapper.custom_signal import slack_event_data_received, slash_event_data_received


def slack_event_trigger(event_type: str, team_id: str, event: dict):
    slack_event_data_received.send(
        sender=slack_event_trigger, event_type=event_type, event=event, team_id=team_id)
    return Response(None)


def slash_event_trigger(user_id: str, channel_id: str, slash_event_data: dict):
    slash_event_data_received.send(sender=slash_event_trigger, user_id=user_id,
                                   channel_id=channel_id, slash_event_data=slash_event_data)
    return Response(None)
