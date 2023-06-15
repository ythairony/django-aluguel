from django.shortcuts import render, redirect

from .daos import ItemDAO


# Create your views here.
def index(request):
    return render(request, 'index.html')

class ItemViews:
    def __init__(self):
        self.item_dao = ItemDAO()

    def list_item(self, request):
        item_list = ItemDAO.list_item(request)
        context = {'item_list': item_list}
        return render(request, 'item/listItem.html', context)
    

    def form_item(self, request):
        # return self.item_dao.form_item(request)
        return render(request, 'item/formItem.html')

    def save_item(self, request):
        name=request.POST['name']
        description=request.POST['description']
        self.item_dao.save_item(name, description)
        return redirect('/listItem')

    def delete_item(self, request, id):
        self.item_dao.delete_item(id)
        return redirect('/listItem')

    def detail_item(self, request, id):
        item = ItemDAO.detail_item(request, id)
        context = {'item': item}
        return render(request, 'item/formEditItem.html', context)
        
    def update_item(self, request, id):
        self.item_dao.update_item(request, id)
        return redirect('/listItem') 
