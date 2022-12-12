from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
# from django.contrib.auth.models import User
from django.urls import reverse

STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
)

# Create your models here.
class rechargePlan(models.Model):
	#about servicex
    price = models.BigIntegerField(null=True, blank=True)
    slug = models.SlugField(null=True,blank=True)
    combo = models.TextField(null=True, blank=True)
    data_with_rollover = models.CharField(max_length=255, null=True, blank=True)
    sms_per_day = models.CharField(max_length=255, null=True, blank=True)
    local_std_and_roaming_calls = models.CharField(max_length=255, null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    def get_absolute_url(self):
        return reverse('karoRecharge:rechargePlanDetailUrl', args=[self.slug])
    
    def __str__(self):
        return f"Plan -- {self.price}" or '--Name not provided--'


class Images(models.Model):
	file = models.FileField('File', upload_to='images/', null=True, blank=True)
	title = models.CharField(max_length=100, null=True, blank=True)
	description = models.CharField(max_length=250, null=True, blank=True)
	rechargePlan = models.ForeignKey(rechargePlan, related_name='imagesRP', on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return self.filename

	@property
	def filename(self):
		return self.file.name.rsplit('/', 1)[-1]