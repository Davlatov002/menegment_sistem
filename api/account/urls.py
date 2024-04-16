from django.urls import path

from api.account.views.user import (
    CustomTokenObtainPairView,
    UserUpdateAPIView,
    UserRetrieveAPIView,
    UserCreateAPIView,
    UserDestroyAPIView,
    UserListAPIView,
)
from api.account.views.student_profile import (
    StudentProfileListAPIView,
    StudentProfileDestroyAPIView,
    StudentProfileCreateAPIView,
    StudentProfileUpdateAPIView,
    StudentProfileRetrieveAPIView,
)
from api.account.views.staff_profile import (
    StaffProfileListAPIView,
    StaffProfileCreateAPIView,
    StaffProfileRetrieveAPIView,
    StaffProfileUpdateAPIView,
    StaffProfileDestroyAPIView,
)
from api.account.views.payment import (
    PaymentListAPIView,
    PaymentCreateAPIView,
    PaymenDestroyAPIView,
    PaymentUpdateAPIView,
    PaymentRetrieveAPIView,
)
from rest_framework_simplejwt.views import TokenRefreshView




urlpatterns = [

    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('users/', UserListAPIView.as_view(), name='user_all'),
    path('user-create/', UserCreateAPIView.as_view(), name='user_create'),
    path('user-update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user-delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),

    path('student-profiles/', StudentProfileListAPIView.as_view(), name='student_profile_all'),
    path('student-profile/<int:pk>/', StudentProfileRetrieveAPIView.as_view(), name='student_profile_retrieve'),
    path('student-profile-create/', StudentProfileCreateAPIView.as_view(), name='student_profile_create'),
    path('student-profile-update/<int:pk>/', StudentProfileUpdateAPIView.as_view(), name='student_profile_update'),
    path('student-profile-delete/<int:pk>/', StudentProfileDestroyAPIView.as_view(), name='student_profile_delete'),

    path('staff-profiles/', StaffProfileListAPIView.as_view(), name='staff_profile_all'),
    path('staff-profile/<int:pk>/', StaffProfileRetrieveAPIView.as_view(), name='staff_profile_retrieve'),
    path('staff-profile-create/', StaffProfileCreateAPIView.as_view(), name='staff_profile_create'),
    path('stafft-profile-update/<int:pk>/', StaffProfileUpdateAPIView.as_view(), name='staff_profile_update'),
    path('staff-profile-delete/<int:pk>/', StaffProfileDestroyAPIView.as_view(), name='staff_profile_delete'),

    path('payments/', PaymentListAPIView.as_view(), name='payment_all'),
    path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_retrieve'),
    path('payment-create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment-update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment_update'),
    path('payment-delete/<int:pk>/', PaymenDestroyAPIView.as_view(), name='payment_delete'),

]

