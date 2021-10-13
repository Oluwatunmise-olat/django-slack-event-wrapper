from django import dispatch
from django.dispatch import receiver

# events
event_type: str = ''
event: dict = {}
team_id: str = ''

# slash commands
slash_event_data: dict = {}
user_id: str = ''
channel_id: str = ''


slack_event_data_received = dispatch.Signal(providing_args=[event_type, event, team_id])
slash_event_data_received = dispatch.Signal(providing_args=[user_id, channel_id, slash_event_data])
