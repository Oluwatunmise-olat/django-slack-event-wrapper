from functools import wraps
import hmac
import hashlib
import time
from django.conf import settings
from django.http import JsonResponse


try:
    settings.SIGNING_SECRET
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


def validate_request(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        request = args[0]
        headers = args[0].headers
        # This signature was created by slack by combining
        # the signing secret with the request body
        slack_signature = headers.get('X-Slack-Signature')
        slack_request_timestamp = headers.get('X-Slack-Request-Timestamp')
        if not slack_signature and not slack_request_timestamp:
            # to allow not dictinoary objects to be serialized we apply safe=False
            return JsonResponse("This endpoint is strictly for slack events.", safe=False)
        # staright from slack documantation
        if time.time() - int(slack_request_timestamp) > 60*5:
            # The request Timestamp is more than 5 miutes from local time,
            # It could be a replay attack , so lets ignore it
            # The above came straight from slack documantation
            return JsonResponse()
        basestring = f"v0:{slack_request_timestamp}:{request.body.decode('utf-8')}"
        # converts the basestring to bytes
        bytes_basestring = basestring.encode()
        key = settings.SIGNING_SECRET.encode()
        hashed = 'v0=' + hmac.new(key=key, msg=bytes_basestring,
                                  digestmod=hashlib.sha256).hexdigest()
        is_request_valid = hmac.compare_digest(hashed, slack_signature)
        if not is_request_valid:
            return JsonResponse("This event is not for our app.", safe=False)
        return function(*args, **kwargs)
    return wrapper
