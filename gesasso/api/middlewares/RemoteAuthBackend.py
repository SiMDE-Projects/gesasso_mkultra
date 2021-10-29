from django.contrib.auth.backends import RemoteUserBackend


class RemoteAuthBackend(RemoteUserBackend):
    def authenticate(self, request, remote_user):
        user = super(RemoteAuthBackend, self).authenticate(request, remote_user['id'])
        user.first_name = remote_user['firstname']
        user.last_name = remote_user['lastname']
        user.email = remote_user['email']
        user.save()
        return user
