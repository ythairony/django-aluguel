from django.shortcuts import redirect, render

from .models import Client, Item, Rent, Tema
from .business import Util


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

        for item in itens:
            item_id = Item.objects.get(id=item)
            tema_festa.tema.add(item_id)

        tema_festa.save()
        # tema_festa.tema.set(itens)


    def delete_tema(self, id):
        tema = Tema.objects.get(pk=id)
        tema.delete()


    def detail_tema(self, id):
        tema = Tema.objects.get(pk=id)
        return tema
    

    def update_tema(self, request, id, nome, valor_aluguel, cor, itens):
        tema_festa = Tema(id=id, nome=nome, valor_aluguel=valor_aluguel, cor=cor)
        tema_festa.save()
        tema_festa.tema.set(itens)


class ClientDAO:
    def list_client(self):
        client_list = Client.objects.all()
        return client_list
    
    def find_client(self, cliente):
        client_id = Client.objects.get(id=cliente)
        return client_id


class RentDAO:
    def list_rent(self):
        rent_list = Rent.objects.all()
        return rent_list


    def save_rent(self, request, date, start_hours, end_hours, client_id, tema_id):
        # tema = Tema.objects.get(id=tema_id)
        # tema.valor_aluguel = Util().calc_desc(request)
        # print(tema.valor_aluguel)
        aluguel = Rent(date=date, start_hours=start_hours, end_hours=end_hours, client=client_id, theme_id=tema_id, valor_aluguel=Util().calc_desc(request))
        # desconto = Util.CalcDesc(self, request)

        # se ligar no tema, pode dar errado ainda
        aluguel.save()


    def delete_rent(self, id):
        rent = Rent.objects.get(pk=id)
        rent.delete()


    def detail_rent(self, id):
        rent = Rent.objects.get(pk=id)
        return rent

    def update_rent(self, request, id, date, start_hours, end_hours):
        rent = Rent.objects.get(id=id)
        rent.date=date
        rent.start_hours=start_hours
        rent.end_hours=end_hours
        rent.save()