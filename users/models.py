
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email,last_name, first_name,gender, phone, **kwargs):
        user = self.model(email=email,gender=gender, first_name=first_name, last_name=last_name, phone=phone, **kwargs)
        user.set_password(None)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, gender,phone, **kwargs):
        user = self.create_user(email, name, gender,phone, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    gender=models.CharField(max_length=10)
    phone = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'phone']

    objects = CustomUserManager()

# class CUser(models.Model):
#     email= models.EmailField(primary_key=True)
#     first_name= models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     gender  =models.CharField(max_length=10)    
#     phone = models.CharField(max_length=15)

