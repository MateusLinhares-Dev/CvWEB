from django.urls import path
from curriculum.views import InfoMateusView

urlpatterns = [
    path("", InfoMateusView.as_view(), name="curriculum")
]