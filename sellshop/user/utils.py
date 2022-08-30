import os
import six
import requests
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator

def download_image(url):
    response = requests.get(url)
    file_name = 'profile_images/'  + url.split('/')[-1]  + '.png'
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    with open(file_path, 'wb') as f:
        f.write(response.content)
    return file_name


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


account_activation_token = AccountActivationTokenGenerator()