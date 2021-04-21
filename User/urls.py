from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', register, name='user-registration'),
    path('hospitalRegister/', register, name='hospital-registration'),
    path('ngoRegister/', register, name='ngo-registration'),
    path('login/', login, name='user-login'),
    path('hospitalLogin/', login, name='hospital-login'),
    path('ngoLogin/', login, name='ngo-login'),
    path('logout/', logout, name='user-logout'),
    path('admitPatient/', admitPatient, name='admit-patient'),
    path('showPatients/', showPatients, name='admitted-patients'),
    # path('showPatient/', showPatient, name='patient-details'),
    # path('showAdmissionHistory/', showAdmissionHistory, name='patient-admission'),
    path('dischargePatient/', dischargePatient, name='discharge-patient'),
    path('patientSearch/', patientSearch, name='patient-search'),
    path('profile/', profile, name='user-profile'),
    path('admissionHistory/', admissionHistory, name='admission-history'),
    path('hospitalProfile/', hospitalProfile, name='hospital-profile'),
    path('ngoProfile/', ngoProfile, name='ngo-Profile'),
    path('profileEdit/', profileEdit, name='user-profileEdit'),
    path('profilePicEdit/', profilePicEdit, name='user-profilePicEdit'),
    path('aadharPicEdit/', aadharPicEdit, name='user-aadharPicEdit'),
    path('findHelp/', findHelp, name='user-findHelp'),
    path('showHelpRequests/', showHelpRequests, name='user-showHelpRequests'),
    path('registerChoice/', register, name='user-registerChoice'),
    path('loginChoice/', login, name='user-loginChoice'),
    path('userProfileView/', userProfileView, name='user-profileView'),
    path('healthIDCardView/', healthIDCardView, name='user-healthIDCardView'),
    path('hospitalProfileView/', hospitalProfileView, name='hospital-profileView'),
    path('ngoProfileView/', ngoProfileView, name='ngo-profileView'),
    path('showPatient/<int:pk>/', showPatientHistory, name = 'show-patient'),
    path('admissionHistory/<int:pk>/', showUserHistory, name = 'show-user'),
    path('ngoHowMuchPay/', ngoHowMuchPay, name='ngo-howMuchPay'),
    path('showHospitalDetails/', showHospitalDetails, name='ngo-showHospitalDetails'),
    path('addNewBill/', addNewBill, name='hospital-addNewBill'),
    path('usersPastHistoryInHospital/<int:pk>/', usersPastHistoryInHospital, name='users-pastHistoryInHospital'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
