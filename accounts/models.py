from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db.models.fields import DateTimeField

# Manager of the custom user model
# Uses email as the unique identifier instead of username
class MyAccountManager(BaseUserManager):
    # creates a user and saves his/her credentials
    def create_user(self,email,username,first_name, last_name, password = None):
        if not email:
            raise ValueError("A user must have an email address")
        if not username:
            raise ValueError("A user must have a username")
        user = self.model(
            email = self.normalize_email(email), # converts email address to lowercase while entering in database
            username  = username,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,username,first_name,last_name,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name= last_name

        )
        # set all permissions True for superuser
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using = self._db)
        return user


class Account(AbstractBaseUser):
    # Fields for the user model
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name ='email', max_length = 60,unique = True)
    username = models.CharField(max_length= 30, unique = True)
    date_joined = models.DateTimeField(verbose_name='Date Joined',auto_now_add = True)
    last_login  = DateTimeField(verbose_name = 'last login', auto_now = True )
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    # setting email to uniquely identify a user 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    # specifying the class that drives operations 
    objects = MyAccountManager()

    # methods

    # display name for objects of user model will be email
    def __str__(self):
        return self.email

    # if a user is admin then he/she will have all permissions   
    def has_perm(self,perm,obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True




