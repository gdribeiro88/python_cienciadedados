
class Glicemia: 

    #é necessário de um método/serviço que crie ou instancie um objeto do tipo Glicemia
    def __init__(self, dia_semana, ano, valor_glicemia, valor_insulina, kcal, carb, qualidade_sono):
        self.dia_semana = dia_semana
        self.ano = ano
        self.valor_glicemia = int(valor_glicemia)
        self.valor_insulina = int(valor_insulina)
        self.kcal = int(kcal)
        self.carb = int(carb)
        self.qualidade_sono = int(qualidade_sono)


    #estamos reescrevendo o método que gera uma string do objeto Glicemia
    def __str__(self):
        return f"Glicemia[Dia:{self.dia_semana}, Ano:{self.ano}, Valor Glicemia:{self.valor_glicemia}, Insulina:{self.valor_insulina}, Kcal:{self.kcal}, Carb.:{self.carb}, Sono:{self.qualidade_sono}]"