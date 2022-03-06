
from django.urls import include, path
from users.views import dashboard, register

urlpatterns = [
    path(r"^accounts/", include("django.contrib.auth.urls")),
    path(r"^dashboard/", dashboard, name="dashboard"),
    path(r"^register/", register, name="register"),
]