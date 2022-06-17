import environ

env = environ.Env(
    GESASSO_EMAIL_HOST=(str, "mailserver"),
)

EMAIL_HOST = env("GESASSO_EMAIL_HOST")
