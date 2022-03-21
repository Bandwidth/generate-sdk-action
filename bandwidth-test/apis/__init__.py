
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.calls_api import CallsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from bandwidth-test.api.calls_api import CallsApi
from bandwidth-test.api.conferences_api import ConferencesApi
from bandwidth-test.api.media_api import MediaApi
from bandwidth-test.api.messages_api import MessagesApi
from bandwidth-test.api.recordings_api import RecordingsApi
