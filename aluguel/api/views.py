from django.shortcuts import render
from .models import Item

# Create your views here.
def index(request):
    return render(request, 'index.html')

class ItemViews:
    #Recupera a lista de itens cadastrados
    def listItem(request):
        item_list = Item.objects.all()
        context = {'item_list': item_list}
        return render(request, 'item/listItem.html', context)