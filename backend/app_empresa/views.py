import openpyxl
from django.shortcuts import render
from django.http import HttpResponse
from .forms import (
    ExcelUploadFormArea, ExcelUploadFormAmbiente, ExcelUploadFormGestor,
    ExcelUploadFormManutentor, ExcelUploadFormPatrimonio
)
from .models import Area, Ambiente, Gestor, Manutentor, Patrimonio

def upload_area(request):
    if request.method == 'POST':
        form = ExcelUploadFormArea(request.POST, request.FILES)
        if form.is_valid():
            wb = openpyxl.load_workbook(request.FILES['file'])
            ws = wb.active
            for row in ws.iter_rows(min_row=2, values_only=True):
                Area.objects.create(area=row[0])
    else:
        form = ExcelUploadFormArea()
    return render(request, 'upload_excel.html', {'form': form, 'titulo': 'Upload de Área'})

def upload_ambiente(request):
    if request.method == 'POST':
        form = ExcelUploadFormAmbiente(request.POST, request.FILES)
        if form.is_valid():
            wb = openpyxl.load_workbook(request.FILES['file'])
            ws = wb.active
            for row in ws.iter_rows(min_row=2, values_only=True):
                Ambiente.objects.create(sig=row[0], descricao=row[1], sn=row[2], responsavel=row[3])
    else:
        form = ExcelUploadFormAmbiente()
    return render(request, 'upload_excel.html', {'form': form, 'titulo': 'Upload de Ambiente'})


def upload_gestor(request):
    if request.method == 'POST':
        form = ExcelUploadFormGestor(request.POST, request.FILES)
        if form.is_valid():
            wb = openpyxl.load_workbook(request.FILES['file'])
            ws = wb.active
            for row in ws.iter_rows(min_row=2, values_only=True):
                Gestor.objects.create(sn=row[0], nome=row[1], cargo=row[2])
    else:
        form = ExcelUploadFormGestor()
    return render(request, 'upload_excel.html', {'form': form, 'titulo': 'Upload de Gestor'})



def upload_manutentor(request):
    if request.method == 'POST':
        form = ExcelUploadFormManutentor(request.POST, request.FILES)
        if form.is_valid():
            wb = openpyxl.load_workbook(request.FILES['file'])
            ws = wb.active
            for row in ws.iter_rows(min_row=2, values_only=True):
                try:
                    gestor_id = row[4]
                    gestor = Gestor.objects.get(id=gestor_id)
                    Manutentor.objects.create(
                        sn=row[0],
                        nome=row[1],
                        email=row[2],
                        area=row[3],
                        gestor=gestor
                    )
                except Gestor.DoesNotExist:
                    print(f"Gestor com ID {row[4]} não encontrado.")
    else:
        form = ExcelUploadFormManutentor()

    return render(request, 'upload_excel.html', {'form': form, 'titulo': 'Upload de Manutentor'})



def upload_patrimonio(request):
    if request.method == 'POST':
        form = ExcelUploadFormPatrimonio(request.POST, request.FILES)
        if form.is_valid():
            wb = openpyxl.load_workbook(request.FILES['file'])
            ws = wb.active
            for row in ws.iter_rows(min_row=2, values_only=True):
                Patrimonio.objects.create(ni=row[1], descricao=row[2], localizacao=row[0])
    else:
        form = ExcelUploadFormPatrimonio()
    return render(request, 'upload_excel.html', {'form': form, 'titulo': 'Upload de Patrimônio'})

