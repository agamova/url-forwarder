from django.db import models
import string
import secrets



def create_token():
    alphabet = string.ascii_letters.upper() + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(10))


class ForwarderModel(models.Model):
    slug = models.SlugField()
    access_code = models.CharField(max_length=10, default=create_token)
    redirect_url = models.URLField()

    def __str__(self):
        return f'{self.slug} --> {self.redirect_url}'
