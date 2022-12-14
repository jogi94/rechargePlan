from django.urls import path
from . import views

app_name = 'karoRecharge'

urlpatterns = [
	# path('', views.homeView, name="homeURL"),
	path('recharge-plan', views.rechargePlanView, name='rechargePlanUrl'),
	path('recharge-plan/<slug>/',views.rechargePlanDetailView, name='rechargePlanDetailUrl'),
	
	#submit
	path('generate-recharge-plan', views.generateRechargePlan, name='generateRechargePlanUrl')


]