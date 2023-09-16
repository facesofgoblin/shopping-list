from django.shortcuts import render #berguna untuk mengimpor fungsi render
#django.shortcuts Fungsi render digunakan untuk me-render tampilan HTML dengan menggunakan data yang diberikan.
# Create your views here.

# PERUBAHAN: 13 SEP 2023, TUTORIAL 2
# Membuat Form Input Data dan Menampilkan Data Produk Pada HTML
#ditambahkan beberapa import berikut:
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product

# Tutorial Mengembalikan Data dalam Bentuk XML
from django.http import HttpResponse
from django.core import serializers


# def show_main(request): # mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.

#     context = { #dictionary yang berisi data yang akan dikirimkan ke tampilan.
#         'name': 'Rana Koesumastuti',
#         'class': 'PBP A',
#     }
#     # me-render tampilan main.html dengan menggunakan fungsi render
#     # di dalam render ada sebuah request untuk 
#     return render(request, "main.html", context) 

# PERUBAHAN: 13 SEP 2023, TUTORIAL 2
# Membuat Form Input Data dan Menampilkan Data Produk Pada HTML

#Mengubah fungsi main mnenjadi seperti ini:
def show_main(request):
    # Fungsi Product.objects.all() digunakan untuk mengambil seluruh object Product yang tersimpan pada database.
    products = Product.objects.all()

    context = {
        'name': 'Pak Bepe', # Nama kamu
        'class': 'PBP A', # Kelas PBP kamu
        'products': products
    }

    return render(request, "main.html", context)

#Membuat fungsi baru dengan nama create_product yg menerima parameter request
def create_product(request):
    form = ProductForm(request.POST or None)        #Membuat ProductForm baru dengan memasukkan QueryDict berdasarkan input dari user pada request.POST.

#form.is_valid() digunakan untuk memvalidasi isi input dari form tersebut.
#form.save() digunakan untuk membuat dan menyimpan data dari form tersebut.
#return HttpResponseRedirect(reverse('main:show_main')) digunakan untuk melakukan redirect setelah data form berhasil disimpan.
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

# Tutorial Mengembalikan Data dalam Bentuk XML
# 
# def show_xml(request): # fungsi dengan parameter request
#     data = Product.objects.all() #menyimpan hasil query dari seluruh data yg ada pada Product

# Menambahkan return function
def show_xml(request):
    data = Product.objects.all()
    # content_type="application/xml"
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    # serializers digunakan untuk translate objek model menjadi format lain seperti dalam fungsi ini adalah XML.


# TUTORIAL: MENGEMBALIKAN DATA DALAM BENTUK JSON 
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


# TUTORIAL: MENGEMBALIKAN DATA BERDASARKAN ID DLM BENTUK XML DAN JSON
# Buat variabel dalam fungsi yg nyimpen hasil query dari data dengan id tertntu yg ada pd Product
# data = Product.objects.filter(pk=id)

#XML
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

#JSON
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")