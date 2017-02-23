from django.conf.urls import include, url
from .views import ListPlan, CreatePlan

urlpatterns = [
	url(r'^plans/$', ListPlan.as_view(), name='plans'),
	url(r'^create-plan/$', CreatePlan.as_view(), name='create_plan')
]