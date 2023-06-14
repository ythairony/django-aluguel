from django.shortcuts import render

from .daos import ItemDAO


# Create your views here.
def index(request):
    return render(request, 'index.html')

class ItemViews:
    def __init__(self):
        self.itemDAO = ItemDAO()

    def listItem(self, request):
        return self.itemDAO.listItem(request)

    def formItem(self, request):
        return self.itemDAO.formItem(request)

    def saveItem(self, request):
        return self.itemDAO.saveItem(request)

    def deleteItem(self, request, id):
        return self.itemDAO.deleteItem(id)

    def detailItem(self, request, id):
        return self.itemDAO.detailItem(request, id)
        
    def updateItem(self, request, id):
        return self.itemDAO.updateItem(request, id)
