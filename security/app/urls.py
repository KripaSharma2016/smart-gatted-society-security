from django.conf.urls import url
from . import views

urlpatterns = [
    url('^internal/v1/security/sg/register$', views.sg_register)
]