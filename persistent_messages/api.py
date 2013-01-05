from persistent_messages import notify
from persistent_messages import constants 

def add_message(request, level, message, extra_tags='', fail_silently=False, subject='', user=None, email=False, from_user=None, expires=None, close_timeout=None):
    """
    """
    if email:
        notify.email(level, message, extra_tags, subject, user, from_user)
    return request._messages.add(level, message, extra_tags, subject, user, from_user, expires, close_timeout)

def add_async_message(level, message, extra_tags='',
                      fail_silently=False, subject='', user=None, email=False,
                      from_user=None, expires=None, close_timeout=None):
    from persistent_messages.models import Message
    if not user:
        raise Exception("User must be supplied to async message")
    if email:
        notify.email(level, message, extra_tags, subject, user, from_user)
    message = Message(user=user, level=level, message=message,
                      extra_tags=extra_tags, subject=subject,
                      from_user=from_user, expires=expires,
                      close_timeout=close_timeout)
    message.save()
    return message

def info(request, message, extra_tags='', fail_silently=False, subject='', user=None, email=False, from_user=None, expires=None, close_timeout=None):
    """
    """
    level = constants.INFO
    return add_message(request, level, message, extra_tags, fail_silently, subject, user, email, from_user, expires, close_timeout)

def warning(request, message, extra_tags='', fail_silently=False, subject='', user=None, email=False, from_user=None, expires=None, close_timeout=None):
    """
    """
    level = constants.WARNING
    return add_message(request, level, message, extra_tags, fail_silently, subject, user, email, from_user, expires, close_timeout)

def debug(request, message, extra_tags='', fail_silently=False, subject='', user=None, email=False, from_user=None, expires=None, close_timeout=None):
    """
    """
    level = constants.DEBUG
    return add_message(request, level, message, extra_tags, fail_silently, subject, user, email, from_user, expires, close_timeout)
