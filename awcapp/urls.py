from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'awcapp'


urlpatterns = [
    path('api/login/', views.UserLoginView.as_view(), name="login_api"),
    path('api/sec_entry/', views.SectorEntryView.as_view(), name="sec_entry_api"),
    path('api/awc_entry/', views.AwcEntryView.as_view(), name="awc_entry_api"),
    path('api/staff_entry/', views.StaffInfoView.as_view(), name="staff_info_api"),
    path('api/child_entry/', views.ChildInfoView.as_view(), name="child_info_api"),
    path('api/gravid_women_entry/', views.GravidWomenInfoView.as_view(), name="gravid_women_api"),
    path('api/postpartum_mother_entry/', views.PostpartumMotherView.as_view(), name="postpartum_mother_api"),
    path('api/girl_entry/', views.TeenAgeGirlView.as_view(), name="girl_entry_api"),
    path('api/death_info_entry/', views.DeathInfoView.as_view(), name="death_entry_api"),
    path('api/fetch/sec_entry/', views.FetchSectorEntry.as_view(), name="fetch_sec_entry_api"),
    path('api/fetch/awc_entry/', views.FetchAwcEntry.as_view(), name="fetch_awc_entry_api"),
    path('api/fetch/staff_entry/', views.StaffInfoFetchView.as_view(), name="fetch_awc_staff_api"),
    path('api/fetch/child_entry/', views.ChildInfoFetchView.as_view(), name="fetch_child_info_api"),
    path('api/fetch/gravid_women_entry/', views.GravidWomenInfoFetchView.as_view(), name="fetch_gravid_women_api"),
    path('api/fetch/postpartum_mother_entry/', views.PostpartumMotherFetchView.as_view(), name="fetch_postpartum_mother_api"),
    path('api/fetch/girl_entry/', views.TeenAgeGirlFetchView.as_view(), name="fetch_girl_entry_api"),
    path('api/fetch/death_info_entry/', views.DeathInfoFetchView.as_view(), name="fetch_death_entry_api"),
    path('api/download/awc_report/', views.DownloadAWCReportView.as_view(), name="download_awc_report_view"),

]

