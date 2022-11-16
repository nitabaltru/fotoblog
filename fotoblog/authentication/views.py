from authentication.forms import SignupForm
from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import View


class SignupPage(View):
    template_name = "authentication/signup.html"
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            context={"form": form},
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(
            request,
            self.template_name,
            context={"form": form},
        )
