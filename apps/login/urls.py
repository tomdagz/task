from django.conf.urls import url
from .views import userloguin

urlpatterns = [
	url(r'^$', userloguin, name="userloguin"),
]