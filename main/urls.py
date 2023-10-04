#berkas ini bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main

# impor path dari django.urls untuk mendefinisikan pola URL
from django.urls import path

#fungsi show_main dr modul main.views sebagai tampilan jika URL di
from main.views import add_product_ajax, get_product_json, show_main

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

# TUTORIAL 3 IMPOR FUNGSI REGISTER DAN LOG IN
from main.views import register #sesuaikan dengan nama fungsi yang dibuat
from main.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from main.views import logout_user 

# TUTORIAL 4
from main.views import edit_product
from main.views import delete_product

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

    # PATH FUNGSI REGISTER : TUTORIAL 3
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    # TUTORIAL 4
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete/<int:id>', delete_product, name='delete_product'), # sesuaikan dengan nama fungsi yang dibuat

    # TUTORIAL 5
    
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
]