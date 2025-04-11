from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import ExcelUploadForm
from .models import ExcelDocument

class ExcelUploadView(View):
    def get(self, request):
        form = ExcelUploadForm()
        context = {'form': form}
        return render(request, 'app/upload_excel.html', context)

    def post(self, request):
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_doc = form.save()
            messages.success(request, 'Excel file uploaded successfully!')
            return redirect('excel_list')
        return render(request, 'app/upload_excel.html', {'form': form})

class ExcelListView(View):
    def get(self, request):
        documents = ExcelDocument.objects.all().order_by('-uploaded_at')
        context = {'documents': documents}
        return render(request, 'app/excel_list.html', context)