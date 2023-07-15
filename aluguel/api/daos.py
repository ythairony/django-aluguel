from django.shortcuts import redirect, render

from .models import Item, Tema


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
               


class TemaDAO:
    # Recuperar a lista de temas cadastrados
    def list_tema(self):
        tema_list = Tema.objects.all()
        return tema_list
    
    
    def save_tema(self, nome, valor_aluguel, cor, itens):
        tema_festa = Tema(nome=nome, valor_aluguel=valor_aluguel, cor=cor)
        tema_festa.save()
        tema_festa.tema.set(itens)


    def delete_tema(self, id):
        tema = Tema.objects.get(pk=id)
        tema.delete()


    def detail_tema(self, id):
        tema = Tema.objects.get(pk=id)
        return tema
    

    def update_tema(self, request, id):
        tema = Tema.objects.get(pk=id)
        tema.nome = request.POST['nome']
        tema.valor_aluguel = request.POST['valor_aluguel']
        tema.cor = request.POST['cor']
        tema.tema = request.POST['tema']
        tema.save()