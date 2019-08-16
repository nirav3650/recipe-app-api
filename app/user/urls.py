from django.urls import path
from user.views import CreateUserAPi
app_name = 'user'
urlpatterns = [
    path("create", CreateUserAPi.as_view(), name="create")
]
