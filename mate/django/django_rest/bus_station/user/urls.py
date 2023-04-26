from django.urls import path
from rest_framework.authtoken import views

from user.views import CreateUserView, CreateTokenView, ManageUserView

urlpatterns = [
    path("token/", CreateTokenView.as_view(), name="token"),
    path("create/", CreateUserView.as_view(), name="create"),
    path("me/", ManageUserView.as_view(), name="manage")

]

app_name = "user"
