class Telhado:
    def __init__(self, area_horizontal, inclinacoes, rendimentos):
        self.area_horizontal = area_horizontal
        self.inclinacoes = inclinacoes
        self.rendimentos = rendimentos

    def obter_fator_correcao(self, inclinacao_percentual):
        fatores_correcao = {
            0: 1.000,
            5: 1.001,
            10: 1.005,
            15: 1.011,
            20: 1.020,
            25: 1.031,
            30: 1.044,
            35: 1.059,
            40: 1.077,
            45: 1.097,
            50: 1.118,
            55: 1.141,
            60: 1.166,
            65: 1.193,
            70: 1.221,
            75: 1.250,
            80: 1.281,
            85: 1.312,
            90: 1.345,
            95: 1.379,
            100: 1.414
        }
        return fatores_correcao.get(inclinacao_percentual, 1.000)

    def calcular_area_real(self, inclinacao_percentual):
        fator_correcao = self.obter_fator_correcao(inclinacao_percentual)
        area_real = self.area_horizontal * fator_correcao
        return area_real

    def calcular_quantidade_telhas(self):
        quantidades = {}
        for tipo, rendimento in self.rendimentos.items():
            inclinacao = self.inclinacoes[tipo]
            area_real = self.calcular_area_real(inclinacao)
            quantidade_telhas = area_real * rendimento
            quantidade_com_adicional = quantidade_telhas * 1.05  # Adicional de 5%
            quantidades[tipo] = (area_real, quantidade_telhas, quantidade_com_adicional)
        return quantidades

# Exemplo de uso
area_horizontal = 150  # Área em projeção horizontal em m²

# Inclinação do telhado em percentual para cada tipo de telha
inclinacoes = {
    'plana': 45,
    'colonial': 25,
    'paulista': 25,
    'plan': 25,
    'francesa': 30,
    'romana': 30,
    'portuguesa': 30,
    'americana': 30,
    'italiana': 30,
    'fibrocimento': 9
}

# Rendimento das telhas informado pelo fabricante (telhas por m²)
rendimentos = {
    'plana': 35,
    'colonial': 25,
    'paulista': 25,
    'plan': 24,
    'francesa': 16,
    'romana': 16,
    'portuguesa': 16,
    'americana': 12,
    'italiana': 14,
    'fibrocimento':1.5
}

telhado = Telhado(area_horizontal, inclinacoes, rendimentos)

quantidades_telhas = telhado.calcular_quantidade_telhas()

print("\n --------------- Cálculo número de telhas por tipo ---------------\n")
print(f"Área horizontal do telhado: {area_horizontal:.2f} m²")
for tipo, (area_real, quantidade, quantidade_com_adicional) in quantidades_telhas.items():
    print(f"\nTipo de telha: {tipo}")
    print(f"Área real do telhado: {area_real:.2f} m²")
    print(f"Quantidade de telhas {tipo} necessárias: {quantidade:.0f}")
    print(f"Quantidade de telhas {tipo} necessárias com adicional de 5%: {quantidade_com_adicional:.0f}")
