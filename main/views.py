from django.shortcuts import render #berguna untuk mengimpor fungsi render
#django.shortcuts Fungsi render digunakan untuk me-render tampilan HTML dengan menggunakan data yang diberikan.
# Create your views here.

def show_main(request): # mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.

    context = { #dictionary yang berisi data yang akan dikirimkan ke tampilan.
        'nama': 'Rana Koesumastuti',
        'class': 'PBP A',
    }
    # me-render tampilan main.html dengan menggunakan fungsi render
    # di dalam render ada sebuah request untuk 
    return render(request, "main.html", context) 


