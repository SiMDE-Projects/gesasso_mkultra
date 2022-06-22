import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

env = environ.Env(
    GESASSO_SENTRY_DSN=(str, ""), GESASSO_SENTRY_ENV=(str, "developpement")
)

sentry_sdk.init(
    dsn=env("GESASSO_SENTRY_DSN"),
    environment=env("GESASSO_SENTRY_ENV"),
    integrations=[
        DjangoIntegration(),
    ],
    traces_sample_rate=1.0,
    send_default_pii=True,
)
