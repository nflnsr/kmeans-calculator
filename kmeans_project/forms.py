from django import forms

class InputForm(forms.Form):
    data1 = forms.CharField(label='Masukkan input Anda', max_length=100)
    data2 = forms.CharField(label='Masukkan input Anda', max_length=100)
    k = forms.CharField(label='Masukkan input Anda', max_length=100)
    # tambahkan bidang lain yang Anda perlukan untuk logika Anda
