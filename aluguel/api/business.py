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
    def __init__(self):
        self.desc_40 = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira']
        self.desc_10 = ['sexta-feira', 'sábado', 'domingo']
        


    def calc_desc(self, request):
        cliente_tem_aluguel = Rent.objects.filter(client_id=request.POST['select_client']).exists()
        tema = Tema.objects.get(pk=request.POST['select_theme'])

        valor_aluguel = tema.valor_aluguel
        if cliente_tem_aluguel:
            dia_semana = obter_dia_da_semana(request.POST['date'])

            if dia_semana in self.desc_40:
                valor_aluguel = tema.valor_aluguel * Decimal(0.6)
            elif dia_semana in self.desc_10:
                valor_aluguel = tema.valor_aluguel * Decimal(0.9)
        
        
        return valor_aluguel