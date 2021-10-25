from django.urls import path

from session.views import SessionView, SessionRudView

urlpatterns = [
    path('', SessionView.as_view()),
    path('<str:id>/', SessionRudView.as_view()),
]