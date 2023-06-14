
from api.views import ItemViews, index
from django.contrib import admin
from django.urls import path

itemview = ItemViews()
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

]
