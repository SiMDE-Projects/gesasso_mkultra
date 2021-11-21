import getconf
from split_settings.tools import include

config = getconf.ConfigGetter("gesasso", ["./local_settings.ini"])

DISABLE_SYNC_ASSOS = config.getbool(
    "DISABLE_SYNC_ASSOS",
    False,
    "Disable calls to resources server for Asso's data sync",
)

include(
    "components/*.py",
)
