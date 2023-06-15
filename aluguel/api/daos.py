from django.shortcuts import redirect, render

from .models import Item


class ItemDAO:
    #Recupera a lista de itens cadastrados
    def list_item(self):
        item_list = Item.objects.all()
        return item_list

    #Salva o novo item e volta para listagem de itens
    def save_item(self, nome, descricao):
        i = Item(name=nome, description=descricao)
        i.save()
        

    #Deleta um item e volta para listagem de itens
    def delete_item(self, id):
        i = Item.objects.get(pk=id)
        i.delete()
        
    
    #Pega um item pelo ID e enviar para o form de edição
    def detail_item(self, id):
        item = Item.objects.get(pk=id)
        return item
        

    #Atualiza um item e volta para listagem
    def update_item(self, request, id):
        i = Item.objects.get(pk=id)
        i.name = request.POST['name']
        i.description = request.POST['description']
        i.save()
               