from importlib import import_module

from django.conf import settings
from django.test import RequestFactory


def _attach_session(request):
    engine = import_module(settings.SESSION_ENGINE)
    request.session = engine.SessionStore(None)


class SessionRequestFactory(RequestFactory):
    def request(self, **request):
        request = super(SessionRequestFactory, self).request(**request)
        _attach_session(request)
        return request
