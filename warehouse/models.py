from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
#from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

hold = "Hold"
transit = "Transit"
shifted = "Shifted"

waiting = "Waiting"
received = "Received"

TRANSPORT_CHOICES = (
    (hold,'Hold'),
    (transit, 'Transit'),
    (shifted,'Shifted'),
)

CUSTOMER_CHOICES = (
    (waiting,'Waiting'),
    (received, 'Received'),
)



class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_aw_manager = models.BooleanField('Assembly Warehouse', default=False)
    is_cw_manager = models.BooleanField('City Warehouse', default=False)
    is_sw_manager = models.BooleanField('Sub Warehouse', default=False)
    is_aw_executive = models.BooleanField('Assembly Warehouse Executive', default=False)
    is_cw_executive = models.BooleanField('City Warehouse Executive', default=False)
    is_sw_executive = models.BooleanField('Sub Warehouse Executive', default=False)
    is_aw_transport = models.BooleanField('Assembly Warehouse Transport', default=False)
    is_cw_transport = models.BooleanField('City Warehouse Transport', default=False)
    is_sw_transport = models.BooleanField('Sub Warehouse Transport', default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...

    def __str__(self):
        return str(self.id) + ' - ' + str(self.user_id) + ' - ' + str(self.email_confirmed)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class AssemblyWarehouse(models.Model):
    user = models.ForeignKey(User,on_delete=None)
    purifierid = models.CharField(max_length=10, unique=True)
    aw_manager = models.CharField(max_length=250,blank=True)
    aw_executive = models.CharField(max_length=250,blank=True)
    location = models.CharField(max_length=500,blank=True)
    address = models.CharField(max_length=500,blank=True)
    is_in_transport = models.CharField(max_length=25,choices=TRANSPORT_CHOICES,default=hold)
    is_in_citywarehouse = models.BooleanField(default=False)
    cw_name = models.CharField(max_length=250,blank=True)
    transport_person_name = models.CharField(max_length=250,blank=True)
    is_returned = models.BooleanField(default=False)
    returned_from = models.CharField(max_length=250,blank=True)
    is_device_ok = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    start_transport = models.DateTimeField(blank=True,null=True)
    end_transport = models.DateTimeField(blank=True,null=True)
    return_time = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.purifierid + ' - ' + self.aw_manager


class CityWarehouse(models.Model):
    user = models.ForeignKey(User,on_delete=None)
    aw = models.ForeignKey(AssemblyWarehouse,on_delete=None,blank=True, null=True)
    purifierid = models.CharField(max_length=10,unique=True)
    cw_manager = models.CharField(max_length=250,blank=True)
    cw_executive = models.CharField(max_length=250,blank=True)
    location = models.CharField(max_length=250,blank=True)
    address = models.CharField(max_length=500,blank=True)
    is_in_transport = models.CharField(max_length=25,choices=TRANSPORT_CHOICES,default=hold)
    is_in_subwarehouse = models.BooleanField(default=False)
    sw_name = models.CharField(max_length=250,blank=True)
    transport_person_name = models.CharField(max_length=250,blank=True)
    is_returned = models.BooleanField(default=False)
    returned_from = models.CharField(max_length=250,blank=True)
    is_device_ok = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    start_transport = models.DateTimeField(blank=True,null=True)
    end_transport = models.DateTimeField(blank=True,null=True)
    return_time = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.purifierid + ' - ' + self.cw_manager

class SubWarehouse(models.Model):
    user = models.ForeignKey(User,on_delete=None)
    cw = models.ForeignKey(CityWarehouse,on_delete=None,blank=True, null=True)
    purifierid = models.CharField(max_length=10,unique=True)
    sw_manager = models.CharField(max_length=250,blank=True)
    sw_executive = models.CharField(max_length=250,blank=True)
    location = models.CharField(max_length=250,blank=True)
    address = models.CharField(max_length=500,blank=True)
    is_in_transport = models.CharField(max_length=25,choices=TRANSPORT_CHOICES,default=hold)
    customer_transport = models.CharField(max_length=50,choices=CUSTOMER_CHOICES,default=waiting)
    is_with_customer = models.BooleanField(default=False)
    transport_person_name = models.CharField(max_length=250,blank=True)
    is_returned = models.BooleanField(default=False)
    returned_from = models.CharField(max_length=250,blank=True)
    is_device_ok = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    cust_name = models.CharField(max_length=250,blank=True)
    cust_phoneno = models.CharField(max_length=15,blank=True)
    start_transport = models.DateTimeField(blank=True,null=True)
    end_transport = models.DateTimeField(blank=True,null=True)
    return_time = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.purifierid + ' - ' + self.sw_manager

class TotalCityWarehouse(models.Model):
    user = models.ForeignKey(User,on_delete=None)
    cw_name = models.CharField(max_length=500,blank=True)
    cw_manager = models.CharField(max_length=500,blank=True)
    cw_executive = models.CharField(max_length=500,blank=True)
    cw_manager_active = models.BooleanField(default=True)
    cw_executive_active = models.BooleanField(default=True)

    def __str__(self):
        return self.cw_name + ' - ' + self.cw_manager

class TotalSubWarehouse(models.Model):
    user = models.ForeignKey(User,on_delete=None)
    sw_name = models.CharField(max_length=500,blank=True)
    sw_manager = models.CharField(max_length=500,blank=True)
    sw_executive = models.CharField(max_length=500,blank=True)
    sw_manager_active = models.BooleanField(default=True)
    sw_executive_active = models.BooleanField(default=True)

    def __str__(self):
        return self.sw_name + ' - ' + self.sw_manager


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)