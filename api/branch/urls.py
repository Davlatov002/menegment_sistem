from django.urls import path
from api.branch.views.branches import (
    BranchesCreateAPIView,
    BranchesListAPIView,
    BranchesUpdateAPIView,
    BranchesRetrieveAPIView, 
    BranchesDestroyAPIView,
)
from api.branch.views.room import (
    RoomCreateAPIView,
    RoomDestroyAPIView,
    RoomListAPIView,
    RoomUpdateAPIView,
    RoomRetrieveAPIView,
)

urlpatterns = [

    path('branches/', BranchesListAPIView.as_view(), name='branches_all'),
    path('branch/<int:pk>/', BranchesRetrieveAPIView.as_view(), name='branches_retrieve'),
    path('branch-create/', BranchesCreateAPIView.as_view(), name='branch_create'),
    path('branch-update/<int:pk>/', BranchesUpdateAPIView.as_view(), name='branch_update'),
    path('branch-delete/<int:pk>/', BranchesDestroyAPIView.as_view(), name='branch_delete' ),

    path('rooms/', RoomListAPIView.as_view(), name='room_all'),
    path('room/<int:pk>/', RoomRetrieveAPIView.as_view(), name='room_retrieve'),
    path('room-create/', RoomCreateAPIView.as_view(), name='room_create'),
    path('room-update/<int:pk>/', RoomUpdateAPIView.as_view(), name='room_update'),
    path('room-delete/<int:pk>/', RoomDestroyAPIView.as_view(), name='room_delete'),
]