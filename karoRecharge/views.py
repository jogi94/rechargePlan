from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
from .forms import *

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

#
def generateRechargePlan(request):
    customerPlan = request.POST.get('customerPlan')
    rechargeInst = rechargePlan.objects.filter(price = customerPlan)
    if request.method == 'POST':
        formObj = generateCustomerRechargeForm(request.POST)
        print(formObj)
        if formObj.is_valid():
            cd = formObj.save(commit=False)
            cd.save()
            return HttpResponse('Recharge Successful')
        else:
            return HttpResponse('opppssssss')
    else:
        return HttpResponse('Wrong Number')