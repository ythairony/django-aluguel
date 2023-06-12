
from django.contrib import admin
from django.urls import path
from api.views import ItemViews, index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    #urls itens
    path('listItem/', ItemViews.listItem),
    path('formItem/', ItemViews.formItem),
    # path('saveItem/', ItemViews.saveItem),
    # path('deleteItem/<int:id>', ItemViews.deleteItem),
    # path('detailItem/<int:id>', ItemViews.detailItem),
    # path('updateItem/<int:id>', ItemViews.updateItem),

]
