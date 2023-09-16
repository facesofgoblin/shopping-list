# PERUBAHAN: 13 SEP 2023, TUTORIAL 2
from django.forms import ModelForm
from main.models import Product

#Membuat form sederhana
class ProductForm(ModelForm):
    class Meta:
        model = Product     #Menjalankan model yang digunakan untuk form. 
                            # Ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek Product

        fields = ["name", "price", "description"]
        # menunjukkan field dr model Product yang digunakan untuk form
        # date_added gaada di list krn tanggal ditambahkan secara otomatis
