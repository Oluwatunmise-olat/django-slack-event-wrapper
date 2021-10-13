## DJANGO SLACK EVENT WRAPPER


This is a django wrapper to handle slack events and slash commands.
It also verifies incoming events using x-slack-signature and x-slack-timestamp.
It receives slack events, slash commands and delivers gracefully with the events.  

### CONFIGURATION AND SETUP

```
>settings.py
INSTALLED_APPS = [
    'django_slack_event_wrapper',
    ...
]

CONFIGURATIONS
=============

VERIFICATION_TOKEN = XXXXXXXXXXXXXXXXXXXXX
SIGNING_SECRET = XXXXXXXXXXXXXXXXXXXXX
APP_ID = XXXXXXXXXXXXXXXXXXXXX
OAUTH_TOKEN = XXXXXXXXXXXXXXXXXXXXX
BOT_ID = XXXXXXXXXXXXXXXXXXXXX

```

```
>urls.py
    open your projects urls.py file and add the following
    urlpatterns = [
        path('slack-app/', include('django_slack_event_wrapper.urls')),
        ....
    ]
    Note: you can change the name from slack-app to whatever you like.

```

### When registering your webhook urls to slack, you use the following:
```
    1. For Events: http[s]://yourdomain.name/slack-app/events [If you changed the root url name, use that instead of slack-app]

    2. For Slash Commands: http[s]://yourdomain.name/slack-app/slash-commands [If you changed the root url name, use that instead of slack-app]
```

### EXAMPLE

```
    NOTE: Create A slack.py file
    from django_slack_event_wrapper.dispatcher import slack_event_emitter, slash_command_emitter
    from rest_framework.response import Response

```

### EVENT
```
    @slack_event_emitter("message")
    def on_message(event, **kwargs):
        print(event)
        # have fun


```

### SLASH COMMAND
```

    @slash_command_emitter('/message-count')
    def message_count(user_id, channel_id, slash_event_data, **kwargs):
        print(user_id, channel_id)
        # have fun

```
