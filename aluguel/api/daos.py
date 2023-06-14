from django.shortcuts import redirect, render

from .models import Item


class ItemDAO:
    #Recupera a lista de itens cadastrados
    def listItem(self, request):
        item_list = Item.objects.all()
        context = {'item_list': item_list}
        return render(request, 'item/listItem.html', context)

    #Redirecionador para o formulário de cadastro de item
    def formItem(self, request):
        return render(request, 'item/formItem.html')

    #Salva o novo item e volta para listagem de itens
    def saveItem(self, request):
        i = Item(name=request.POST['name'], 
                 description=request.POST['description'])
        i.save()
        return redirect('/listItem')

    #Deleta um item e volta para listagem de itens
    def deleteItem(self, id):
        i = Item.objects.get(pk=id)
        i.delete()
        return redirect('/listItem')
    
    #Pega um item pelo ID e enviar para o form de edição
    def detailItem(self, request, id):
        item = Item.objects.get(pk=id)
        return render(request, 'item/formEditItem.html', {'item': item} )

    #Atualiza um item e volta para listagem
    def updateItem(self, request, id):
        i = Item.objects.get(pk=id)
        i.name = request.POST['name']
        i.description = request.POST['description']
        i.save()
        return redirect('/listItem')        