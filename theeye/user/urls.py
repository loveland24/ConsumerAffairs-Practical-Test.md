from django.urls import path
from user.views import (
    UserView, UserRudView
)


urlpatterns = [
    path('', UserView.as_view(), name='user-create'),
    path('<int:id>/', UserRudView.as_view(), name='user-rud'),
]

