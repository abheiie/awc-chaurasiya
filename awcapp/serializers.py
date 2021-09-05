from rest_framework import serializers
from collections import OrderedDict 
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from .jwt_payload import jwt_payload_handler
from .models import (
    User,
    District,
    Sector,
    SectorEntry,
    AwcEntry,
    EditReport,
    StaffInfo,
    ChildInfo,
    ChildStatus,
    GravidWomenInfo,
    GravidWomenStatus,
    PostpartumMother,
    PostpartumStatus,
    TeenAgeGirl,
    TeenAgeGirlStatus,
    DeathInfo
)
from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError
from uuid import uuid4
import base64
from django.core.files.base import ContentFile
from django.contrib.auth import authenticate

JWT_PAYLOAD_HANDLER = jwt_payload_handler
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')


class SectorSerializer(serializers.ModelSerializer):
    district = serializers.SerializerMethodField()
    class Meta:
        model = Sector
        fields = "__all__"

    def get_district(self,obj):
        data = District.objects.filter(pk=obj.district.pk)
        res_data = DistrictSerializer(data,many=True)

        return res_data.data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=120, write_only=True)
    district = DistrictSerializer(required=False)
    token = serializers.CharField(max_length=255, read_only=True)
    role = serializers.CharField(max_length=120, read_only=True)


    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        user = authenticate(self,username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'username':user.username,
            'role':user.user_roll,
            'token': jwt_token,
            'district':user.district,
        }


class FetchSectorEntrySerializer(serializers.ModelSerializer):
    sector = serializers.SerializerMethodField()

    class Meta:
        model = SectorEntry
        fields = ('id','user','sector','superviser_name','mobile_no','created_on')

    def get_sector(self,obj):
        data = Sector.objects.filter(pk=obj.sector.pk)
        res_data = SectorSerializer(data,many=True)

        return res_data.data



class FetchAwcEntrySerializer(serializers.ModelSerializer):
    sector = serializers.SerializerMethodField()

    class Meta:
        model = AwcEntry
        fields = '__all__'

    def get_sector(self,obj):
        data = Sector.objects.filter(pk=obj.sector.pk)
        res_data = SectorSerializer(data,many=True)

        return res_data.data




class SectorEntrySerializer(serializers.ModelSerializer):
    sector = serializers.SerializerMethodField()
    user = UserSerializer(required=False)
    sector_id = serializers.IntegerField(default=20)
    user_id = serializers.IntegerField(default=20)

    class Meta:
        model = SectorEntry
        fields = ('id','user','user_id','sector_id','sector','superviser_name','mobile_no','created_on')


    def validate(self, data):
        sector_id = data.pop("sector_id", None)
        user_id = data.pop("user_id", None)
        sector_obj_id = Sector.objects.get(pk=sector_id)
        user_obj_id = User.objects.get(pk=user_id)
        data.update({'sector':sector_obj_id,'user':user_obj_id})

        SectorEntry.objects.create(**data)

        return {"info":"Data Saved Sucessfully!"}

    def get_sector(self,obj):
        data = Sector.objects.filter(pk=obj.sector.pk)
        res_data = SectorSerializer(data,many=True)

        return res_data.data



class AwcEntrySerializer(serializers.ModelSerializer):
    sector = serializers.SerializerMethodField()
    user = UserSerializer(required=False)
    sector_id = serializers.IntegerField(default=20)
    user_id = serializers.IntegerField(default=20)


    class Meta:
        model = AwcEntry
        fields = ('id','user','user_id','sector_id','sector','awc_center_name','awc_center_code',\
            'village_council','village','worker_name','worker_aadhar','worker_mobile_no',\
            'supporter_name','supporter_aadhar','supporter_mobile_no','created_on')


    def validate(self, data):
        sector_id = data.pop("sector_id", None)
        user_id = data.pop("user_id", None)
        sector_obj_id = Sector.objects.get(pk=sector_id)
        user_obj_id = User.objects.get(pk=user_id)
        data.update({'sector':sector_obj_id,'user':user_obj_id})

        AwcEntry.objects.create(**data)

        return {"info":"Data Saved Sucessfully!"}

    def get_sector(self,obj):
        data = Sector.objects.filter(pk=obj.sector.pk)
        res_data = SectorSerializer(data,many=True)

        return res_data.data




class StaffInfoSerializer(serializers.ModelSerializer):
    sector = serializers.SerializerMethodField()
    user = UserSerializer(required=False)
    sector_id = serializers.IntegerField(default=20)
    user_id = serializers.IntegerField(default=20)


    class Meta:
        model = StaffInfo
        fields = ('id','user','user_id','sector_id','sector','superviser_name','project_name','awc_center_name','awc_center_code',\
            'village_council','village','worker_name','worker_aadhar','worker_mobile_no',\
            'supporter_name','supporter_aadhar','supporter_mobile_no','created_on')


    def validate(self, data):
        sector_id = data.pop("sector_id", None)
        user_id = data.pop("user_id", None)
        sector_obj_id = Sector.objects.get(pk=sector_id)
        user_obj_id = User.objects.get(pk=user_id)
        data.update({'sector':sector_obj_id,'user':user_obj_id})

        StaffInfo.objects.create(**data)

        return {"info":"Data Saved Sucessfully!"}

    def get_sector(self,obj):
        data = Sector.objects.filter(pk=obj.sector.pk)
        res_data = SectorSerializer(data,many=True)

        return res_data.data



class ChildInfoSerializer(serializers.ModelSerializer):
    sector = serializers.SerializerMethodField()
    user = UserSerializer(required=False)
    sector_id = serializers.IntegerField(default=20)
    user_id = serializers.IntegerField(default=20)


    class Meta:
        model = ChildInfo
        fields = ('id','user','user_id','sector_id','sector','awc_name','child_name',\
            'fathers_name','fathers_aadhar','mothers_name','mothers_aadhar','dob',\
            'mobile_no','gender','cast','is_handicapped','condition','created_on')


    def validate(self, data):
        sector_id = data.pop("sector_id", None)
        user_id = data.pop("user_id", None)
        sector_obj_id = Sector.objects.get(pk=sector_id)
        user_obj_id = User.objects.get(pk=user_id)
        data.update({'sector':sector_obj_id,'user':user_obj_id})

        ChildInfo.objects.create(**data)

        return {"info":"Data Saved Sucessfully!"}

    def get_sector(self,obj):
        data = Sector.objects.filter(pk=obj.sector.pk)
        res_data = SectorSerializer(data,many=True)

        return res_data.data





class GravidWomenInfoSerializer(serializers.ModelSerializer):
    sector = serializers.SerializerMethodField()
    user = UserSerializer(required=False)
    sector_id = serializers.IntegerField(default=20)
    user_id = serializers.IntegerField(default=20)


    class Meta:
        model = GravidWomenInfo
        fields = ('id','user','user_id','sector_id','sector','project_name','awc_center_name',\
            'gravid_women_name','gravid_women_aadhar','husband_name','mobile_no','dob','created_on')


    def validate(self, data):
        sector_id = data.pop("sector_id", None)
        user_id = data.pop("user_id", None)
        sector_obj_id = Sector.objects.get(pk=sector_id)
        user_obj_id = User.objects.get(pk=user_id)
        data.update({'sector':sector_obj_id,'user':user_obj_id})

        GravidWomenInfo.objects.create(**data)

        return {"info":"Data Saved Sucessfully!"}

    def get_sector(self,obj):
        data = Sector.objects.filter(pk=obj.sector.pk)
        res_data = SectorSerializer(data,many=True)

        return res_data.data




class PostpartumMotherSerializer(serializers.ModelSerializer):
    sector = serializers.SerializerMethodField()
    user = UserSerializer(required=False)
    sector_id = serializers.IntegerField(default=20)
    user_id = serializers.IntegerField(default=20)


    class Meta:
        model = PostpartumMother
        fields = ('id','user','user_id','sector_id','sector','awc_center_name','name',\
            'aadhar','husband_name','delivery_date','mobile_no','created_on')


    def validate(self, data):
        sector_id = data.pop("sector_id", None)
        user_id = data.pop("user_id", None)
        sector_obj_id = Sector.objects.get(pk=sector_id)
        user_obj_id = User.objects.get(pk=user_id)
        data.update({'sector':sector_obj_id,'user':user_obj_id})

        PostpartumMother.objects.create(**data)

        return {"info":"Data Saved Sucessfully!"}

    def get_sector(self,obj):
        data = Sector.objects.filter(pk=obj.sector.pk)
        res_data = SectorSerializer(data,many=True)

        return res_data.data



class TeenAgeGirlSerializer(serializers.ModelSerializer):
    sector = serializers.SerializerMethodField()
    user = UserSerializer(required=False)
    sector_id = serializers.IntegerField(default=20)
    user_id = serializers.IntegerField(default=20)


    class Meta:
        model = TeenAgeGirl
        fields = ('id','user','user_id','sector_id','sector','awc_center_name','girl_name',\
            'girl_aadhar','dob','mobile_no','created_on')


    def validate(self, data):
        sector_id = data.pop("sector_id", None)
        user_id = data.pop("user_id", None)
        sector_obj_id = Sector.objects.get(pk=sector_id)
        user_obj_id = User.objects.get(pk=user_id)
        data.update({'sector':sector_obj_id,'user':user_obj_id})

        TeenAgeGirl.objects.create(**data)

        return {"info":"Data Saved Sucessfully!"}

    def get_sector(self,obj):
        data = Sector.objects.filter(pk=obj.sector.pk)
        res_data = SectorSerializer(data,many=True)

        return res_data.data




class DeathInfoSerializer(serializers.ModelSerializer):
    sector = serializers.SerializerMethodField()
    user = UserSerializer(required=False)
    sector_id = serializers.IntegerField(default=20)
    user_id = serializers.IntegerField(default=20)


    class Meta:
        model = DeathInfo
        fields = ('id','user','user_id','sector_id','sector','awc_center_name','benificiary_name',\
            'day_of_death','death_reason','created_on')


    def validate(self, data):
        sector_id = data.pop("sector_id", None)
        user_id = data.pop("user_id", None)
        sector_obj_id = Sector.objects.get(pk=sector_id)
        user_obj_id = User.objects.get(pk=user_id)
        data.update({'sector':sector_obj_id,'user':user_obj_id})

        DeathInfo.objects.create(**data)

        return {"info":"Data Saved Sucessfully!"}

    def get_sector(self,obj):
        data = Sector.objects.filter(pk=obj.sector.pk)
        res_data = SectorSerializer(data,many=True)

        return res_data.data