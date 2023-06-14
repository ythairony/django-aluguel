
from api.views import ItemViews, index
from django.contrib import admin
from django.urls import path

itemview = ItemViews()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    #urls itens
    path('listItem/', itemview.listItem),
    path('formItem/', itemview.formItem),
    path('saveItem/', itemview.saveItem),
    path('deleteItem/<int:id>', itemview.deleteItem),
    path('detailItem/<int:id>', itemview.detailItem),
    path('updateItem/<int:id>', itemview.updateItem),

]
