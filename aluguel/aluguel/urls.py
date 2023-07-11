
from api.views import ItemViews, index, TemaViews
from django.contrib import admin
from django.urls import path

itemview = ItemViews()
temaview = TemaViews()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    #urls itens
    path('listItem/', itemview.list_item),
    path('formItem/', itemview.form_item),
    path('saveItem/', itemview.save_item),
    path('deleteItem/<int:id>', itemview.delete_item),
    path('detailItem/<int:id>', itemview.detail_item),
    path('updateItem/<int:id>', itemview.update_item),
    #urls temas
    path('listTema/', temaview.list_tema),
    path('formTema/', temaview.form_tema),
    path('saveTema/', temaview.save_tema),
    path('deleteTema/<int:id>', temaview.delete_tema),
    path('detailTema/<int:id>', temaview.detail_tema),
    path('updateTema/<int:id>', temaview.update_tema),

]
