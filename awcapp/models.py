import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save
import os
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
	PermissionsMixin


def image_file_path(instance, filename):
	"""Generate file path for new recipe image"""
	ext = filename.split('.')[-1]
	filename = f'{uuid.uuid4()}.{ext}'

	return os.path.join('uploads/', filename)


class UserManager(BaseUserManager):

	def create_user(self, email, username, password=None, **extra_fields):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')
		user = self.model(email=self.normalize_email(email),
						  username=username.lower(),
						  **extra_fields)
		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(email, username, password)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)

		return user


class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=180, unique=True)
	email = models.EmailField(max_length=180, unique=True)
	fullname = models.CharField(max_length=180, blank=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	date_joined = models.DateTimeField(auto_now_add=True)
	user_roll = models.CharField(verbose_name="user roll", max_length=60)
	district = models.ForeignKey("District", on_delete=models.SET_NULL, null=True)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def __str__(self):
		return self.username


class District(models.Model):
	name = models.CharField(max_length=60)

class Sector(models.Model):
	name = models.CharField(max_length=20)
	district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)	   





class SectorEntry(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
	superviser_name = models.CharField(max_length=180,blank=True,null=True)
	mobile_no = models.CharField(max_length=180,blank=True,null=True)
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.sector.name







class AwcEntry(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
	awc_center_name = models.CharField(verbose_name="Awc Center name",max_length=180,blank=True,null=True)
	awc_center_code = models.IntegerField(verbose_name="Awc Center Code",default=20)
	village_council = models.CharField(verbose_name="Village Council",max_length=180,blank=True,null=True)
	village = models.CharField(verbose_name="Village",max_length=180,blank=True,null=True)
	worker_name = models.CharField(verbose_name="Worker Name",max_length=180,blank=True,null=True)
	worker_aadhar = models.IntegerField(verbose_name="Worker Aadhar No",default=20)
	worker_mobile_no = models.CharField(verbose_name="Worker Name",max_length=180,blank=True,null=True)
	supporter_name = models.CharField(verbose_name="Supporter Name",max_length=180,blank=True,null=True)
	supporter_aadhar = models.IntegerField(verbose_name="Supporter Aadhar No",default=20)
	supporter_mobile_no = models.CharField(verbose_name="Supporter Mobile No",max_length=180,blank=True,null=True)
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.sector.name



class EditReport(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	serial_no = models.IntegerField(verbose_name="Serial Number",default=20)
	sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
	sector_incharge_name = models.CharField(verbose_name="Sector Incharge Name",max_length=180,blank=True,null=True)
	mobile_no = models.CharField(verbose_name="Worker Name",max_length=180,blank=True,null=True)
	awc_center_name = models.CharField(verbose_name="Awc Center name",max_length=180,blank=True,null=True)
	awc_center_code = models.IntegerField(verbose_name="Awc Center Code",default=20)
	village_council = models.CharField(verbose_name="Village Council",max_length=180,blank=True,null=True)
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.sector.name


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)


CONDITION_CHOICES = (
    ('General', 'General'),
    ('Medium', 'Medium'),
    ('Lower', 'Lower')
)



class StaffInfo(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
	superviser_name = models.CharField(verbose_name="Superviser Name",max_length=180,blank=True,null=True)
	project_name = models.CharField(verbose_name="Project Name",max_length=180,blank=True,null=True)
	awc_center_name = models.CharField(verbose_name="Awc Center name",max_length=180,blank=True,null=True)
	awc_center_code = models.IntegerField(verbose_name="Awc Center Code",default=20)
	village_council = models.CharField(verbose_name="Village Council",max_length=180,blank=True,null=True)
	village = models.CharField(verbose_name="Village",max_length=180,blank=True,null=True)
	worker_name = models.CharField(verbose_name="Worker Name",max_length=180,blank=True,null=True)
	worker_aadhar = models.IntegerField(verbose_name="Worker Aadhar No",default=20)
	worker_mobile_no = models.CharField(verbose_name="Worker Name",max_length=180,blank=True,null=True)
	supporter_name = models.CharField(verbose_name="Supporter Name",max_length=180,blank=True,null=True)
	supporter_aadhar = models.IntegerField(verbose_name="Supporter Aadhar No",default=20)
	supporter_mobile_no = models.CharField(verbose_name="Supporter Mobile No",max_length=180,blank=True,null=True)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.project_name




class ChildInfo(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
	awc_name = models.CharField(verbose_name="Awc Name",max_length=180,blank=True,null=True)
	child_name = models.CharField(verbose_name="Child Name",max_length=180,blank=True,null=True)
	fathers_name = models.CharField(verbose_name="Father's Name",max_length=180,blank=True,null=True)
	fathers_aadhar = models.CharField(verbose_name="Father's Aadhar",max_length=180,blank=True,null=True)
	mothers_name = models.CharField(verbose_name="Mother's Name",max_length=180,blank=True,null=True)
	mothers_aadhar = models.CharField(verbose_name="Mother's Aadhar",max_length=180,blank=True,null=True)
	dob = models.DateField(verbose_name="Date of Birth",max_length=8,blank=True,null=True)
	mobile_no = models.CharField(verbose_name="Mobile No",max_length=180,blank=True,null=True)
	gender = models.CharField(choices=GENDER_CHOICES, max_length=60,blank=True,null=True)
	cast = models.CharField(choices=CONDITION_CHOICES, max_length=60,blank=True,null=True)
	is_handicapped = models.BooleanField(default=False)
	condition = models.CharField(verbose_name="Condition",max_length=220,blank=True,null=True)
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.child_name



class ChildStatus(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	child_user = models.ForeignKey(ChildInfo, on_delete=models.SET_NULL, null=True, related_name='child_status')
	weight = models.CharField(verbose_name="Weight",max_length=180,blank=True,null=True)
	height = models.CharField(verbose_name="Height",max_length=180,blank=True,null=True)
	amusc = models.CharField(verbose_name="Amusc",max_length=180,blank=True,null=True)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.child_user.child_name



class GravidWomenInfo(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
	project_name = models.CharField(verbose_name="Project Name",max_length=180,blank=True,null=True)
	awc_center_name = models.CharField(verbose_name="Awc Center Name",max_length=180,blank=True,null=True)
	gravid_women_name = models.CharField(verbose_name="Gravid Women Name",max_length=180,blank=True,null=True)
	gravid_women_aadhar = models.CharField(verbose_name="Gravid Women Aadhar",max_length=180,blank=True,null=True)
	husband_name = models.CharField(verbose_name="Husband Name",max_length=180,blank=True,null=True)
	dob = models.DateField(verbose_name="Date of Birth",max_length=8,blank=True,null=True)
	mobile_no = models.CharField(max_length=180,blank=True,null=True)
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.gravid_women_name






class GravidWomenStatus(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	gravid_women = models.ForeignKey(GravidWomenInfo, on_delete=models.SET_NULL, null=True, related_name='gravid_women_status')
	condition = models.CharField(max_length=180,blank=True,null=True)
	probable_delivery_date = models.DateField(verbose_name="Probable Delivery Date",max_length=8,blank=True,null=True)
	hemoglobin_level = models.CharField(max_length=180,blank=True,null=True)
	weight = models.CharField(max_length=180,blank=True,null=True)
	anc_checkup = models.BooleanField(default=False)
	ifa_tablet = models.BooleanField(default=False)
	nutritious_food = models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.child_user.child_name




class PostpartumMother(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
	awc_center_name = models.CharField(verbose_name="Awc Center Name",max_length=180,blank=True,null=True)
	name = models.CharField(verbose_name="Gravid Women Name",max_length=180,blank=True,null=True)
	aadhar = models.CharField(verbose_name="Gravid Women Aadhar",max_length=180,blank=True,null=True)
	husband_name = models.CharField(verbose_name="Husband Name",max_length=180,blank=True,null=True)
	delivery_date = models.DateField(verbose_name="Probable Delivery Date",max_length=8,blank=True,null=True)
	mobile_no = models.CharField(max_length=180,blank=True,null=True)
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name



class PostpartumStatus(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	postpartum_mother = models.ForeignKey(PostpartumMother, on_delete=models.SET_NULL, null=True, related_name='postpartum_mother_status')
	hemoglobin_level = models.CharField(max_length=180,blank=True,null=True)
	anc_checkup = models.BooleanField(default=False)
	plasmodium_inf_test = models.BooleanField(default=False)
	nutritious_food = models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name


class TeenAgeGirl(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
	awc_center_name = models.CharField(verbose_name="Awc Center Name",max_length=180,blank=True,null=True)
	girl_name = models.CharField(verbose_name="Teen Age Girl Name",max_length=180,blank=True,null=True)
	fathers_name = models.CharField(verbose_name="Father's Name",max_length=180,blank=True,null=True)
	dob = models.DateField(verbose_name="Date of Birth",max_length=8,blank=True,null=True)
	girl_aadhar = models.CharField(verbose_name="Teen Age Girl Aadhar",max_length=180,blank=True,null=True)
	mobile_no = models.CharField(max_length=180,blank=True,null=True)
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.girl_name




class TeenAgeGirlStatus(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	girl = models.ForeignKey(TeenAgeGirl, on_delete=models.SET_NULL, null=True, related_name='teenage_girl_status')
	weight = models.CharField(max_length=180,blank=True,null=True)
	hemoglobin_level = models.CharField(max_length=180,blank=True,null=True)
	plasmodium_inf_test = models.BooleanField(default=False)
	nutritious_food = models.BooleanField(default=False)
	ifa_tablet = models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.girl_name




class DeathInfo(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
	awc_center_name = models.CharField(verbose_name="Awc Center Name",max_length=180,blank=True,null=True)
	benificiary_name = models.CharField(verbose_name="Benificiary Name",max_length=180,blank=True,null=True)
	day_of_death = models.DateField(verbose_name="Day of Death",max_length=8,blank=True,null=True)
	death_reason = models.CharField(verbose_name="Death Reason",max_length=180,blank=True,null=True)
	created_on = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.benificiary_name



###ANM Entry



