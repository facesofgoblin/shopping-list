#berkas ini bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main

# impor path dari django.urls untuk mendefinisikan pola URL
from django.urls import path

#fungsi show_main dr modul main.views sebagai tampilan jika URL diakses
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]