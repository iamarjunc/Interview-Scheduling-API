from django.urls import path
from .views import RegisterUserView, RegisterAvailabilityView, GetSchedulableSlotsView

urlpatterns = [
    path('users/', RegisterUserView.as_view(), name='register-user'),
    path('availability/', RegisterAvailabilityView.as_view(), name='register-availability'),
    path('schedule/', GetSchedulableSlotsView.as_view(), name='get-schedulable-slots'),
]
