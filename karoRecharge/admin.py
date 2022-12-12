from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from django.urls import reverse
from .models import *

admin.site.site_header = "Recharge App"
admin.site.site_title = "Recharge App"
admin.site.index_title = "Recharge App"

# Register your models here.
def approvePost(modeladmin, request, queryset):
	for post in queryset:
		post.status = 'Published'
		post.save()
approvePost.short_description = 'Approve Selected'


def draftPost(modeladmin, request, queryset):
	for post in queryset:
		post.status = 'Draft'
		post.save()
draftPost.short_description = 'Draft Selected'

#gallery
class imagesAdmin(admin.StackedInline):
    model = Images

@admin.register(rechargePlan)
class rechargePlanAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ('price',)
    list_filter = ('price',)
    prepopulated_fields = {'slug': ('price',)}
    inlines = [imagesAdmin]
    actions = [approvePost, draftPost,] 

@admin.register(Images)
class ImagesAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'file','description', 'rechargePlan',)
    list_filter = ('file',)
    actions = [approvePost, draftPost,] 
