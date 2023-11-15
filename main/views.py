# PENAMBAHAN IMPOR UNTUK KEPERLUAN TUTORIAL 3
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  

# TUTORIAL 5
# AJAX
from django.views.decorators.csrf import csrf_exempt

# IMPOR UNTUK KEPERLUAN FUNGSI LOG IN
from django.contrib.auth import authenticate, login
# IMPOR UNTUK KEPERLUAN FUNGSI LOG OUT
from django.contrib.auth import logout
# IMPOR FUNGSI UNTUK MERESTRIKSI AKSES HALAMAN MAIN
# kode ini digunakan untuk mewajibkan pengguna login sebelum mengakses suatu web
from django.contrib.auth.decorators import login_required 

# impor untuk keperluan menggunakan data dari cookies
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponseRedirect, JsonResponse
from main.forms import ProductForm
from django.urls import reverse
from django.shortcuts import render #berguna untuk mengimpor fungsi render
#django.shortcuts Fungsi render digunakan untuk me-render tampilan HTML dengan menggunakan data yang diberikan.
# Create your views here.

# PERUBAHAN: 13 SEP 2023, TUTORIAL 2
# Membuat Form Input Data dan Menampilkan Data Produk Pada HTML
#ditambahkan beberapa import berikut:

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
# PENAMBAHAN KODE AGAR HALAMAN MAIN HANYA BISA DIAKSES OLEH PENGGUNA YG TERAUTENTIKASI
@login_required(login_url='/login')
# def show_main(request):
#     # Fungsi Product.objects.all() digunakan untuk mengambil seluruh object Product yang tersimpan pada database.
#     products = Product.objects.all()

#     context = {
#         'name': 'Pak Bepe', # Nama kamu
#         'class': 'PBP A', # Kelas PBP kamu
#         'products': products,

#         # menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web
#         'last_login': request.COOKIES['last_login']   # PENAMBAHAN VARIABEL
#     }

#     return render(request, "main.html", context)

# PERUBAHAN FUNGSI SHOW_MAIN UNTUK KEPERLUAN PENGHUBUNGAN PRODUCT DAN USER
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP A', # Kelas PBP kamu
        'products': products,

        # menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web
        'last_login': request.COOKIES['last_login']   # PENAMBAHAN VARIABEL
    }
    return render(request, "main.html", context)

# TUTORIAL 5
# MEMBUAT FUNGSI UNTUK MENGEMBALIKAN DATA JSON
def get_product_json(request):
    product_item = Product.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

#Membuat Fungsi untuk Menambahkan Produk dengan AJAX

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        #name = request.POST.get("name") berfungsi untuk mengambil value name pada request.
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        user = request.user

    # new_product membuat objek Product baru dengan parameter sesuai values dari request.
        new_product = Product(name=name, price=price, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

#Membuat fungsi baru dengan nama create_product yg menerima parameter request
# def create_product(request):
#     form = ProductForm(request.POST or None)        #Membuat ProductForm baru dengan memasukkan QueryDict berdasarkan input dari user pada request.POST.

# #form.is_valid() digunakan untuk memvalidasi isi input dari form tersebut.
# #form.save() digunakan untuk membuat dan menyimpan data dari form tersebut.
# #return HttpResponseRedirect(reverse('main:show_main')) digunakan untuk melakukan redirect setelah data form berhasil disimpan.
#     if form.is_valid() and request.method == "POST":
#         form.save()
#         return HttpResponseRedirect(reverse('main:show_main'))

#     context = {'form': form}
#     return render(request, "create_product.html", context)

# MERUBAH FUNGSI CREATE PRODUCT PD LANGKAH MENGHUBUNGKAN PRODUCT DGN USER
def create_product(request):
    form = ProductForm(request.POST or None)

# Parameter commit=False yang digunakan pada potongan kode diatas berguna 
# untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database.
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
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

# DI BAWAH INI PENAMBAHAN FUNGSI UNTUK TUTORIAL 3
# FUNGSI UNTUK HALAMAN REGISTER
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

# FUNGSI UNTUK HALAMAN LOG IN 
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password) #AKAN DILAKUKAN AUTENTIKASI

        # MENGGANTI FUNGSI IF UNTUK KEPERLUAN COOKIES
        if user is not None:
            login(request, user)    # LOG IN DULU
            response = HttpResponseRedirect(reverse("main:show_main"))  # MEMBUAT RESPONSE
            response.set_cookie('last_login', str(datetime.datetime.now())) # untuk membuat _cookie last_login dan menambahkannya ke dalam response
            return response
        
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

# FUNGSI LOG OUT
# def logout_user(request):
#     logout(request) # menghapus sesi pengguna yang masuk
#     return redirect('main:login') # mengarahkan pengguna ke halaman login dalam aplikasi django

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')    # menghapus cookie last_login saat pengguna melakukan logout.
    return response


# TUTORIAL 4 - MENAMBAHKAN FUNGSI EDIT
def edit_product(request, id):
    # Get product berdasarkan ID
    product = Product.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get data berdasarkan ID
    product = Product.objects.get(pk = id)
    # Hapus data
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))


# KEPERLUAN TUTORIAL 8
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Product.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)