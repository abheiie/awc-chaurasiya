from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.views.generic.edit import CreateView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
#from exampmapp.backend CaseInsensitiveModelBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
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
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.core import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import (
	DistrictSerializer,
	SectorSerializer,
	UserLoginSerializer,
	SectorEntrySerializer,
	FetchSectorEntrySerializer,
	FetchAwcEntrySerializer,
	AwcEntrySerializer,
	StaffInfoSerializer,
	ChildInfoSerializer,
	GravidWomenInfoSerializer,
	PostpartumMotherSerializer,
	TeenAgeGirlSerializer,
	DeathInfoSerializer
	)
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status


class UserLoginView(RetrieveAPIView):

	permission_classes = (AllowAny,)
	serializer_class = UserLoginSerializer


	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		district_id = serializer.data['district']['id']
		district_name = serializer.data['district']['name']
		response = {
			'success' : 'True',
			'status code' : status.HTTP_200_OK,
			'message': 'User logged in  successfully',
			'token' : serializer.data['token'],
			'role' : serializer.data['role'],
			'username' : serializer.data['username'],
			'district_id':district_id,
			'district_name':district_name,
			}
		status_code = status.HTTP_200_OK

		return Response(response, status=status_code)



class SectorEntryView(RetrieveAPIView):
	serializer_class = SectorEntrySerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)


	def post(self, request):
		request.data.update({'user_id':request.user.id})
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid(raise_exception=True):
			status_code = status.HTTP_200_OK
			return Response({"info":"Data Saved Sucessfully!"}, status=status_code)
		else:
			return Response({"info":"Please provide all valid feilds."}, status=status_code)






class FetchAwcEntry(APIView):
	serializer_class = AwcEntrySerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request):
		data = AwcEntry.objects.all()
		serializer = AwcEntrySerializer(data, many=True)
		return Response({"awc_entries": serializer.data})



class FetchSectorEntry(APIView):
	serializer_class = SectorEntrySerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request):
		data = SectorEntry.objects.all()
		serializer = SectorEntrySerializer(data, many=True)
		return Response({"sector_entries": serializer.data})






class AwcEntryView(RetrieveAPIView):
	serializer_class = AwcEntrySerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)


	def post(self, request):
		request.data.update({'user_id':request.user.id})
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid(raise_exception=True):
			status_code = status.HTTP_200_OK
			return Response({"info":"Data Saved Sucessfully!"}, status=status_code)
		else:
			return Response({"info":"Please provide all valid feilds."}, status=status_code)



class StaffInfoFetchView(APIView):
	serializer_class = StaffInfoSerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request):
		data = StaffInfo.objects.all()
		serializer = StaffInfoSerializer(data, many=True)
		return Response({"staff_entries": serializer.data})



class StaffInfoView(RetrieveAPIView):
	serializer_class = StaffInfoSerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)


	def post(self, request):
		request.data.update({'user_id':request.user.id})
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid(raise_exception=True):
			status_code = status.HTTP_200_OK
			return Response({"info":"Data Saved Sucessfully!"}, status=status_code)
		else:
			return Response({"info":"Please provide all valid feilds."}, status=status_code)






class ChildInfoFetchView(APIView):
	serializer_class = ChildInfoSerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request):
		data = ChildInfo.objects.all()
		serializer = ChildInfoSerializer(data, many=True)
		return Response({"childs_entries": serializer.data})



class ChildInfoView(RetrieveAPIView):
	serializer_class = ChildInfoSerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)


	def post(self, request):
		request.data.update({'user_id':request.user.id})
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid(raise_exception=True):
			status_code = status.HTTP_200_OK
			return Response({"info":"Data Saved Sucessfully!"}, status=status_code)
		else:
			return Response({"info":"Please provide all valid feilds."}, status=status_code)




class GravidWomenInfoFetchView(APIView):
	serializer_class = GravidWomenInfoSerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request):
		data = GravidWomenInfo.objects.all()
		serializer = GravidWomenInfoSerializer(data, many=True)
		return Response({"gravid_women_entries": serializer.data})



class GravidWomenInfoView(RetrieveAPIView):
	serializer_class = GravidWomenInfoSerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)


	def post(self, request):
		request.data.update({'user_id':request.user.id})
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid(raise_exception=True):
			status_code = status.HTTP_200_OK
			return Response({"info":"Data Saved Sucessfully!"}, status=status_code)
		else:
			return Response({"info":"Please provide all valid feilds."}, status=status_code)






class PostpartumMotherFetchView(APIView):
	serializer_class = PostpartumMotherSerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request):
		data = PostpartumMother.objects.all()
		serializer = PostpartumMotherSerializer(data, many=True)
		return Response({"mothers_entries": serializer.data})



class PostpartumMotherView(RetrieveAPIView):
	serializer_class = PostpartumMotherSerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)


	def post(self, request):
		request.data.update({'user_id':request.user.id})
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid(raise_exception=True):
			status_code = status.HTTP_200_OK
			return Response({"info":"Data Saved Sucessfully!"}, status=status_code)
		else:
			return Response({"info":"Please provide all valid feilds."}, status=status_code)





class TeenAgeGirlFetchView(APIView):
	serializer_class = TeenAgeGirlSerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request):
		data = TeenAgeGirl.objects.all()
		serializer = TeenAgeGirlSerializer(data, many=True)
		return Response({"girl_entries": serializer.data})



class TeenAgeGirlView(RetrieveAPIView):
	serializer_class = TeenAgeGirlSerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)


	def post(self, request):
		request.data.update({'user_id':request.user.id})
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid(raise_exception=True):
			status_code = status.HTTP_200_OK
			return Response({"info":"Data Saved Sucessfully!"}, status=status_code)
		else:
			return Response({"info":"Please provide all valid feilds."}, status=status_code)






class DeathInfoFetchView(APIView):
	serializer_class = DeathInfoSerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)
	def get(self, request):
		data = DeathInfo.objects.all()
		serializer = DeathInfoSerializer(data, many=True)
		return Response({"death_entries": serializer.data})



class DeathInfoView(RetrieveAPIView):
	serializer_class = DeathInfoSerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)


	def post(self, request):
		request.data.update({'user_id':request.user.id})
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid(raise_exception=True):
			status_code = status.HTTP_200_OK
			return Response({"info":"Data Saved Sucessfully!"}, status=status_code)
		else:
			return Response({"info":"Please provide all valid feilds."}, status=status_code)


class DownloadAWCReportView(APIView):
	permission_classes = (AllowAny,)
	# authentication_classes = (JSONWebTokenAuthentication,)
	
	def get(self, request):
		import csv
		header = ["AWC Name", "Child Name", "Mother", "Mother's AAdhar", "Father", "Fathers' AAdhar", "child's DOB ", "Sex", "Cast", "viklang"]
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = f"attachment; filename=spare_orders_list.csv"
		writer = csv.writer(response)
		writer.writerow(header)


		child_info_object = ChildInfo.objects.all()

		for i in child_info_object:
			current_row = []
			current_row.append(i.awc_name)
			current_row.append(i.child_name)
			current_row.append(i.mothers_name)
			current_row.append(i.mothers_aadhar)
			current_row.append(i.fathers_name)
			current_row.append(i.fathers_aadhar)
			current_row.append(i.dob)
			current_row.append(i.gender)
			current_row.append(i.cast)
			current_row.append(i.is_handicapped)
			writer.writerow(current_row)
		return response
