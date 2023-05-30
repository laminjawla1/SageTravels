from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib import messages
from flights.models import Flight

# Create your views here.
class MyLoginView(auth_views.LoginView):
    template_name="accounts/login.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_flights'] = Flight.objects.all().order_by("-date")
        return context
    
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            messages.success(self.request, "Logged in successfully")
        else:
            messages.error(self.request, "Incorrect Credentials")
        return super().get_redirect_url(*args, **kwargs)

class MyLogoutView(auth_views.LogoutView):
    template_name="accounts/logout.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MyLogoutView, self).get_context_data(*args, *kwargs)
        context['recent_flights'] = Flight.objects.all().order_by("-date")
        return context

    def get_success_url(self):
        messages.success(self.request, "Logged out successfully")
        return self.get_redirect_url() or self.get_default_redirect_url()