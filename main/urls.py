#berkas ini bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main

# impor path dari django.urls untuk mendefinisikan pola URL
from django.urls import path

#fungsi show_main dr modul main.views sebagai tampilan jika URL di
from main.views import show_main

#13 September 2023
# impor fungsi create_product yg tadi dibuat di views.py
from main.views import show_main, create_product

# Tutorial Mengembalikan Data dalam Bentuk XML
# Mengimpor fungsi yang tadi dibuat di views.py
from main.views import show_main, create_product, show_xml 

# TUTORIAL: MENGEMBALIKAN DATA DALAM BENTUK JSON 
from main.views import show_main, create_product, show_xml, show_json

# TUTORIAL: MENGEMBALIKAN DATA BERDASARKAN ID DLM BENTUK XML DAN JSON
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),

    # Tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
    path('xml/', show_xml, name='show_xml'), 

    # PATH URL JSON
    path('json/', show_json, name='show_json'), 

    # PATH URL XML DAN JSON
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 

]