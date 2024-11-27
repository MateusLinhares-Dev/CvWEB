from django.shortcuts import render, HttpResponse
from curriculum.models import Profile
from django.views import View

class InfoMateusView(View):
    template_name = "curriculum.html"

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.all()
        
        return render(request, self.template_name, {"profile":profile})
    