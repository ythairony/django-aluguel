from django.shortcuts import render

from .daos import ItemDAO


# Create your views here.
def index(request):
    return render(request, 'index.html')

class ItemViews:
    def __init__(self):
        self.item_dao = ItemDAO()

    def list_item(self, request):
        return self.item_dao.list_item(request)

    def form_item(self, request):
        return self.item_dao.form_item(request)

    def save_item(self, request):
        return self.item_dao.save_item(request)

    def delete_item(self, request, id):
        return self.item_dao.delete_item(id)

    def detail_item(self, request, id):
        return self.item_dao.detail_item(request, id)
        
    def update_item(self, request, id):
        return self.item_dao.update_item(request, id)
