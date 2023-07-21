from .models import Rent, Tema, Client
from datetime import datetime
from decimal import Decimal
# from .daos import RentDAO

def obter_dia_da_semana(data_str):
        try:
            # Converte a string para o objeto datetime
            data = datetime.strptime(data_str, '%Y-%m-%d')
            # Obtém o dia da semana (0 = segunda-feira, 1 = terça-feira, ..., 6 = domingo)
            dia_da_semana = data.weekday()
            
            # Mapeia o número do dia da semana para o nome do dia
            dias_da_semana = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
            nome_do_dia = dias_da_semana[dia_da_semana]
            
            return nome_do_dia
        except ValueError:
            return "Formato de data inválido. Utilize o formato 'YYYY-MM-DD'."

class Util:
    
    

    def CalcDesc(self, request):
        data = request.POST['date']
        cliente_id = request.POST['select_client']
        dia_semana = obter_dia_da_semana(data)
        desc_40 = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira']
        desc_10 = ['sexta-feira', 'sábado', 'domingo']
        cliente = Client.objects.get(pk=cliente_id)
        tema_escolhido = request.POST['select_theme']
        tema = Tema.objects.get(pk=tema_escolhido)
        if cliente:
            rent = Rent.objects.filter(client=cliente)
            if dia_semana in desc_40 and rent:
                 valor_aluguel = tema.valor_aluguel * Decimal(0.6)
            elif dia_semana in desc_10 and rent:
                 valor_aluguel = tema.valor_aluguel * Decimal(0.9)
        
        return valor_aluguel