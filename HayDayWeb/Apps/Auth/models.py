from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE = (('business', 'business'), ('agent', 'agent'), ('owner', 'owner'))
    GENDER = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, max_length=250)
    phone = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    user_type = models.CharField(max_length=100, default=USER_TYPE[0][0], choices=USER_TYPE)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=100, choices=GENDER, null=True, default=None, blank=True)
    head_image = models.ImageField(upload_to='avatar/', null=True, blank=True)
    cover_image = models.ImageField(upload_to='coverPicture/', null=True, blank=True)
    referral_code = models.CharField(max_length=500, null=True, blank=True)
    how_did_you_hear = models.CharField(max_length=500, null=True, blank=True)
    is_on_boarding = models.BooleanField(default=False, null=True, blank=True)
    is_verified = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.email

    def __int__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Users'
        db_table = 'User'
