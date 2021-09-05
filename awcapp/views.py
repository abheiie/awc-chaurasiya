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
	authentication_classes = (JSONWebTokenAuthentication,)

	def common_method(self, header, filename):
		import csv
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
		writer = csv.writer(response)
		writer.writerow(header)
		return writer, response

	
	def get(self, request, type):

		if type == "child_under_6":
			header = ["क्र.","आंगनवाड़ी केंद्र का नाम", "बच्चे का नाम", "माता", "माता का आधार", "पिता", "पिता का आधार", "बच्चे की जन्मतिथि", "लिंग", "जाति", "विकलांग", "मो.न.", "वजन", "उन्चाई", "एमएयूसी", "कुपोशन की स्थिति"]
			writer, response = self.common_method(header, "child_under_6.csv")
			child_info_object = ChildInfo.objects.all()
			count = 0
			for i in child_info_object:
				print(i.child_status.filter().last().weight)
				count+=1
				current_row = []
				current_row.append(count)
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
				current_row.append(i.mobile_no) 
				child_status = i.child_status.filter().last()
				if child_status:
					current_row.append(child_status.weight) if child_status.weight else current_row.append("")
					current_row.append(child_status.height) if child_status.height else current_row.append("")
					current_row.append(child_status.height) if child_status.amusc else current_row.append("")
				#TODO need to be changed
					try:
						current_row.append(child_status.someting) 
					except:
						current_row.append("kuposhan ki sthiti")
				writer.writerow(current_row)

		elif type == "pregnant_woman":
			header = ["क्र.","सेक्टर का नाम", "आंगनबाडी केन्द्र का नाम","गर्भवती महिला का नाम","पति का नाम","गर्भवती का आधार","मो0न0","जन्मतिथि","गर्भधारण की स्थिति","संभावित प्रसव की तिथि","महिला का वजन","हिमोग्लोबिन स्तर","ए.एन.सी चेकअप (हां/नही)","आई.एफ.ए. टेबलेट (हां/नही)", "प्रदायित पोषण आहार (हां/नही)"]                                              
			writer, response = self.common_method(header, "pregnant_woman.csv")
			gravid_women_info = GravidWomenInfo.objects.all()
			count = 0
			for i in gravid_women_info:
				print(i.sector.name)
				current_row = []
				current_row.append(count)
				current_row.append(i.sector.name)
				current_row.append(i.awc_center_name) 
				current_row.append(i.gravid_women_name) 
				current_row.append(i.husband_name) 
				current_row.append(i.gravid_women_aadhar) 
				current_row.append(i.mobile_no) 
				current_row.append(i.dob) 
				gravid_women_status = i.gravid_women_status.filter().last()
				if gravid_women_status:
					current_row.append(gravid_women_status.condition) 
					current_row.append(gravid_women_status.probable_delivery_date) 
					current_row.append(gravid_women_status.weight) 
					current_row.append(gravid_women_status.hemoglobin_level) 
					current_row.append(gravid_women_status.anc_checkup) 
					current_row.append(gravid_women_status.ifa_tablet) 
					current_row.append(gravid_women_status.nutritious_food) 
				writer.writerow(current_row)
			return response

		elif type == "postpartum_mother":
			header = ["क्र","सेक्टर का नाम","आंगनबाड़ी केन्द्र का नाम","शिशुवती माता का नाम","पति का नाम","आधार क्रमांक","प्रसव तिथि","हिमोग्लोबिन स्तर","प्रदायित पोषण आहार","मलेरिया जांच"]
			writer, response = self.common_method(header, "postpartum_mother.csv")
			postpartum_mother_info = PostpartumMother.objects.all()
			count = 0

			for i in postpartum_mother_info:
				current_row = []
				current_row.append(count)
				current_row.append(i.sector.name)
				current_row.append(i.awc_center_name) 
				current_row.append(i.name) 
				current_row.append(i.husband_name) 
				current_row.append(i.aadhar) 
				current_row.append(i.delivery_date) 
				postpartum_mother_status = i.postpartum_mother_status.filter().last()

				if postpartum_mother_status:
					current_row.append(gravid_women_status.hemoglobin_level)
					current_row.append(gravid_women_status.nutritious_food) 
					current_row.append(gravid_women_status.plasmodium_inf_test) 
				writer.writerow(current_row)
			return response
		
		elif type == "teen_age_girl":
			header = ["आंगनबाड़ी का नाम","किशोरी बालिका का नाम","पिता का नाम","आधार क्रमांक","जन्मतिथि","वजन","हिमोग्लोबिन स्तर","प्रदायित पोषण आहार (हां/नही)","मलेरिया जांच (हां/नही)","आई.एफ.ए. (हां/नही)"]
			writer, response = self.common_method(header, "postpartum_mother.csv")
			postpartum_mother_info = TeenAgeGirl.objects.all()
			count = 0

			for i in postpartum_mother_info:
				current_row = []
				current_row.append(count)
				current_row.append(i.awc_center_name) 
				current_row.append(i.girl_name) 
				current_row.append(i.fathers_name) 
				current_row.append(i.girl_aadhar) 
				current_row.append(i.dob) 
				teenage_girl_status = i.teenage_girl_status.filter().last()
				if teenage_girl_status:
					current_row.append(teenage_girl_status.weight)
					current_row.append(teenage_girl_status.hemoglobin_level) 
					current_row.append(teenage_girl_status.nutritious_food) 
					current_row.append(teenage_girl_status.plasmodium_inf_test) 
					current_row.append(teenage_girl_status.ifa_tablet) 
				writer.writerow(current_row)
			return response

		elif type == "death_info":
			header = ["क्र.","आंगनबाड़ी केन्द्र का नाम","हितग्राही का नाम","हितग्राही का प्रकार","मृत्यु दिनांक","मृत्यु का कारण"]
			writer, response = self.common_method(header, "postpartum_mother.csv")
			death_info = DeathInfo.objects.all()
			count = 0
			for i in death_info:
				current_row = []
				current_row.append(count)
				current_row.append(i.awc_center_name) 
				current_row.append(i.benificiary_name) 
				#TODO: one column is blank and 
				current_row.append("हितग्राही का प्रकार") 
				current_row.append(i.day_of_death) 
				current_row.append(i.death_reason) 
				writer.writerow(current_row)
			return response