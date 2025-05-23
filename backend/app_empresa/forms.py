from django import forms

class ExcelUploadFormArea(forms.Form):
    file = forms.FileField()

class ExcelUploadFormAmbiente(forms.Form):
    file = forms.FileField()

class ExcelUploadFormPatrimonio(forms.Form):
    file = forms.FileField()

class ExcelUploadFormFuncionario(forms.Form):
    file = forms.FileField()
