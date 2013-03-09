from django.db import models
from django.contrib.auth.models import User as Django_User
from django.utils.translation import gettext as _

GENDERS = (
    ('m', _('male')),
    ('f', _('female'))
)

class Profile(models.Model):
    user            = models.ForeignKey(to=Django_User)
    first_name      = models.CharField(max_length=255)
    last_name       = models.CharField(max_length=255)
    gender          = models.CharField(max_length=100, default='male', choices=GENDERS)
    avatar          = models.FileField(upload_to='avatars', default=None)

    __unicode__ = lambda self: self.first_name

def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance, first_name="User %d" % instance.id, last_name="")

models.signals.post_save.connect(create_profile, Django_User)