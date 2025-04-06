import datetime

class Carro:
    def __init__(self, marca, modelo, quilometragem, ano_fabricacao, ultima_revisao, quilometragem_revisao):
        self.marca = marca
        self.modelo = modelo
        self.quilometragem = quilometragem
        self.ano_fabricacao = ano_fabricacao
        self.ultima_revisao = ultima_revisao
        self.quilometragem_revisao = quilometragem_revisao

    def precisa_revisao(self):
        # Verifica se a quilometragem atual é maior ou igual a 10.000 km
        # ou se já passou 1 ano desde a última revisão
        if (self.quilometragem - self.quilometragem_revisao) >= 10000:
            print(f"O carro {self.marca} {self.modelo} precisa de revisão devido à quilometragem.")
        elif (datetime.date.today() - self.ultima_revisao).days >= 365:
            print(f"O carro {self.marca} {self.modelo} precisa de revisão devido ao tempo desde a última revisão.")
        else:
            print(f"O carro {self.marca} {self.modelo} não precisa de revisão.")

def cadastrar_carro():
    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo do carro: ")
    quilometragem = float(input("Digite a quilometragem atual do carro: "))
    ano_fabricacao = int(input("Digite o ano de fabricação do carro: "))
    
    ano = int(input("Digite o ano da última revisão: "))
    mes = int(input("Digite o mês da última revisão: "))
    dia = int(input("Digite o dia da última revisão: "))
    ultima_revisao = datetime.date(ano, mes, dia)
    
    quilometragem_revisao = float(input("Digite a quilometragem na época da última revisão: "))
    
    return Carro(marca, modelo, quilometragem, ano_fabricacao, ultima_revisao, quilometragem_revisao)

def listar_carros(carros):
    print("\n")
    print("Lista de Carros:")
    print("\n")
    for i, carro in enumerate(carros, 1):
        print(f"{i}. {carro.marca} {carro.modelo} - Quilometragem: {carro.quilometragem}")

def main():
    carros = []
    while True:
        print("Bem vindo ao Checkup Car!")
        print("\n1. Cadastrar carro")
        print("2. Listar carros")
        print("3. Verificar próximas revisões")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            carros.append(cadastrar_carro())
        elif opcao == "2":
            listar_carros(carros)
        elif opcao == "3":
            for carro in carros:
                carro.precisa_revisao()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
