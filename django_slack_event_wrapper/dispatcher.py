from functools import wraps
from django_slack_event_wrapper.custom_signal import slash_event_data_received, slack_event_data_received


def slack_event_emitter(client_event_type):
    """
        Handles slack events
    """
    def decorator(func):
        @wraps(func)
        def wrapped_func(sender, event_type, event, team_id, **kwargs):
            if event_type == client_event_type:
                return func(event, **kwargs)
        # calls the decorated client func when a signal is received
        slack_event_data_received.connect(wrapped_func, weak=False)

    return decorator


def slash_command_emitter(command):
    """
        Handles Slash commands
    """
    def decorator(func):
        @wraps(func)
        def wrapped_func(sender, user_id, channel_id, slash_event_data, **kwargs):
            if slash_event_data['command'] == command:
                return func(user_id, channel_id, slash_event_data, **kwargs)
        slash_event_data_received.connect(wrapped_func, weak=False)
    return decorator
