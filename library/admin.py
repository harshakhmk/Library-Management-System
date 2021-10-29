from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Books)
class ViewAdmin(ImportExportModelAdmin):
     exclude = ('id','category_id')
     pass

@admin.register(Category)
class ViewAdmin(ImportExportModelAdmin):
     exclude = ('id',)
     pass

