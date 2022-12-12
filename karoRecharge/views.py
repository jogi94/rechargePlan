from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *

# Create your views here.
def rechargePlanView(request):
    rechargePlanList = rechargePlan.objects.filter(status='published')
    print('hi ' + str(rechargePlanList))
    context ={
        'rechargePlanList':rechargePlanList,
    }
    return render(request, 'plans.html', context)


#
def rechargePlanDetailView(request,slug):
	pageInst = get_object_or_404(rechargePlan, slug=slug)
	context = {
		'pageInst':pageInst,
	}
	return render(request, 'planDetail.html', context)