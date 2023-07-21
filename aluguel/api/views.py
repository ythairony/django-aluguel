from django.shortcuts import render, redirect

from .daos import ItemDAO, TemaDAO, RentDAO, ClientDAO


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


class TemaViews:
    def __init__(self):
        self.tema_dao = TemaDAO()


    def list_tema(self, request):
        tema_list = TemaDAO.list_tema(request)
        context = {'tema_list': tema_list}
        return render(request, 'tema/listTema.html', context)
    
    
    def form_tema(self, request):
        list_item = ItemDAO.list_item(self)
        context = {'list_item' : list_item}
        return render(request, 'tema/formTema.html', context)
    
    
    def save_tema(self, request):
        nome = request.POST.get('name')
        valor_aluguel = request.POST.get('price')
        cor = request.POST.get('color')
        itens = request.POST.getlist('item')
        self.tema_dao.save_tema(nome, valor_aluguel, cor, itens)
        return redirect('/listTema')


    def delete_tema(self, request, id):
        self.tema_dao.delete_tema(id)
        return redirect('/listTema')
    
    
    def detail_tema(self, request, id):
        tema = TemaDAO.detail_tema(request, id)
        context = {'tema' : tema}
        return render(request, 'tema/formEditTema.html', context)
    
    
    def update_tema(self, request, id):
        nome = request.POST.get('name')
        valor_aluguel = request.POST.get('price')
        cor = request.POST.get('color')
        itens = request.POST.getlist('item')
        self.tema_dao.update_tema(request, id, nome, valor_aluguel, cor, itens)
        return redirect('/listTema')
    

class RentViews:
    def __init__(self):
        self.rent_dao = RentDAO()

    def list_rent(self, request): #listRent
        rent_list = RentDAO.list_rent(request)
        context = {'rent_list': rent_list}
        return render(request, 'rent/listRent.html', context) 
    
    #Redirecionador para o formulário de cadastro de aluguel
    def form_rent(self, request): #formRent
        client_list = ClientDAO.list_client(request)
        tema_list = TemaDAO.list_tema(request)
        context = {'client_list':client_list, 'tema_list': tema_list}
        return render(request, 'rent/formRent.html', context)
    
    #Salva o novo aluguel e volta para listagem de alugueis
    def save_rent(self, request): #saveRent       
        date=request.POST['date']
        start_hours = request.POST['start_hours']
        end_hours = request.POST['end_hours']
        client_id = request.POST['select_client']
        tema_id = request.POST['select_theme']

        client = ClientDAO.find_client(self, client_id)    

        self.rent_dao.save_rent(request, date, start_hours, end_hours, client, tema_id)

        return redirect('/listRent')

    #Deleta um aluguel e volta para listagem de alugueis
    def delete_rent(self, request, id): #deleteRent
        self.rent_dao.delete_rent(id)
        return redirect('/listRent')
    
    #Pega um aluguel pelo ID e enviar para o form de edição
    def detail_rent(self, request, id): #detailRent
        rent = RentDAO.detail_rent(request, id)
        context = {'rent': rent}
        return render(request, 'rent/formEditRent.html', context)
    
    #Atualiza um item e volta para listagem
    def update_rent(self, request, id): #updateRent
        date=request.POST['date']
        start_hours = request.POST['start_hours']
        end_hours = request.POST['end_hours']

        #começou a dar errado quando pediu o id do cliente
        # client = RentViews.detail_rent(self, request, id).client
        # client_id = ClientDAO.find_client(self, client)

        self.rent_dao.update_rent(request, id, date, start_hours, end_hours)

                
        return redirect('/listRent')


