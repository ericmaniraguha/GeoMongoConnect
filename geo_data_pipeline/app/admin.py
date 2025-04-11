from django.contrib import admin
from .models import ExcelDocument

@admin.register(ExcelDocument)
class ExcelDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'processed')
    list_filter = ('processed', 'uploaded_at')
    search_fields = ('title', 'description')