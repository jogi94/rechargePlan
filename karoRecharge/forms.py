from django import forms
from .models import *

#
class generateCustomerRechargeForm(forms.ModelForm):
	class Meta:
		model = generateCustomerRecharge
		fields = ('customerNumber','customerPlan',)

