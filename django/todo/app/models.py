from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, _user_has_perm
from django.utils import timezone


# Create your models here.
class Item(models.Model):
    content = models.TextField()


class UserManager(BaseUserManager):
    def create_user(self, request_data, **kwargs):
        user = self.model(
            username=request_data['username'],
            display_name=request_data['display'],
            created_at=timezone.now(),
        )

        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, username, display_name, password, **kwargs):
        request_data = {
            'username': username,
            'display': display_name,
            'password': password
        }
        user = self.create_user(request_data)
        user.superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=16, unique=True)
    display_name = models.CharField(max_length=32)
    created_at = models.DateTimeField(default=timezone.now())
    superuser = models.BooleanField(default=False)

    objects = UserManager()

    def user_has_perm(self, perm, obj):
        return _user_has_perm(self, perm, obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return self.superuser

    @property
    def is_superuser(self):
        return self.superuser

    class Meta:
        db_table = 'api_user'
        swappable = 'AUTH_USER_MODEL'
