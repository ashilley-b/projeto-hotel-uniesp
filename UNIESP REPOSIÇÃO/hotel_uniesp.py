def criar_hotel(inicio=101, quantidade=10):
    """Cria a matriz do hotel com quartos sequenciais."""
    if quantidade < 10 or quantidade > 20:
        raise ValueError("Quantidade deve ser entre 10 e 20.")
    return [[inicio + i, 'Livre', ''] for i in range(quantidade)]

def listar_quartos(hotel):
    """Mostra status de todos os quartos."""
    print("\n=== Lista de Quartos ===")
    for quarto in hotel:
        numero, status, nome = quarto
        if status.lower() == 'livre':
            print(f"Quarto {numero}: [Livre]")
        else:
            print(f"Quarto {numero}: [OCUPADO - {nome}]")
    print("========================\n")

def encontrar_quarto(hotel, numero):
    """Retorna o índice do quarto na matriz ou None se não existir."""
    for idx, quarto in enumerate(hotel):
        if quarto[0] == numero:
            return idx
    return None

def check_in(hotel):
    """Realiza o check-in: pede número do quarto e nome do hóspede."""
    try:
        numero = int(input("Número do quarto para check-in: ").strip())
    except ValueError:
        print("Entrada inválida. Digite um número de quarto.")
        return

    idx = encontrar_quarto(hotel, numero)
    if idx is None:
        print("Quarto inexistente.")
        return

    if hotel[idx][1].lower() != 'livre':
        print("Quarto indisponível.")
        return

    nome = input("Nome do hóspede: ").strip()
    if not nome:
        print("Nome vazio. Check-in cancelado.")
        return

    hotel[idx][1] = 'Ocupado'
    hotel[idx][2] = nome
    print(f"Check-in realizado: Quarto {numero} - {nome}")

def check_out(hotel):
    """Realiza o check-out: pede número do quarto e libera-o."""
    try:
        numero = int(input("Número do quarto para check-out: ").strip())
    except ValueError:
        print("Entrada inválida. Digite um número de quarto.")
        return

    idx = encontrar_quarto(hotel, numero)
    if idx is None:
        print("Quarto inexistente.")
        return

    if hotel[idx][1].lower() == 'livre':
        print("Esse quarto já está livre.")
        return

    nome = hotel[idx][2]
    hotel[idx][1] = 'Livre'
    hotel[idx][2] = ''
    print(f"Check-out realizado: Quarto {numero} - {nome} liberado.")

def buscar_hospede(hotel):
    """Busca por um hóspede pelo nome e informa o quarto ou não encontrado."""
    termo = input("Nome do hóspede a buscar: ").strip().lower()
    if not termo:
        print("Nome vazio.")
        return

    encontrados = []
    for quarto in hotel:
        numero, status, nome = quarto
        if nome.lower() == termo and status.lower() != 'livre':
            encontrados.append(numero)

    if encontrados:
        quartos_str = ', '.join(str(n) for n in encontrados)
        print(f"Hóspede encontrado no(s) quarto(s): {quartos_str}")
    else:
        print("Hóspede não encontrado.")

def main():
    hotel = criar_hotel(inicio=101, quantidade=10)

    while True:
        print("=== Hotel UNIESP - Sistema de Recepção ===")
        print("[1] Listar Quartos")
        print("[2] Realizar Check-in")
        print("[3] Realizar Check-out")
        print("[4] Buscar Hóspede")
        print("[5] Sair")
        opc = input("Escolha uma opção: ").strip()

        if opc == '1':
            listar_quartos(hotel)
        elif opc == '2':
            check_in(hotel)
        elif opc == '3':
            check_out(hotel)
        elif opc == '4':
            buscar_hospede(hotel)
        elif opc == '5':
            print("Obrigado por usar o sistema do Hotel UNIESP. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
