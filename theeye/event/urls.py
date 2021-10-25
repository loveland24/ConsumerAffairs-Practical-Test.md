from django.urls import path

from event.views import EventView, EventRudView

urlpatterns = [
    path('', EventView.as_view()),
    path('<int:id>/', EventRudView.as_view()),
]