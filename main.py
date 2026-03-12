# Define o array de char do alfabeto para facilitar a manipulação
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print("Welcome to Caesar Cipher enconde and decode!")
    
while True:
    
    # Recebe a escolha do usuário para codificar, decodificar ou sair
    try:
        choice = int(input("Enter 1 to encode, 2 to decode, or 0 to exit: "))
    except ValueError:
        print("Error: choice must be an integer (0, 1, or 2).")
        continue

    # Valida a escolha do usuario    
    if choice == 0:
        print("Exiting the program. Goodbye!")
        break
    if choice not in (1, 2):
        print("Invalid choice. Please enter 1 to encode, 2 to decode, or 0 to exit.")
        continue

    # Recebe a string a ser codificada ou decodificada
    prase = str(input("Enter the string to encode/decode: "))

    # Recebe o valor do shift para a codificação ou decodificação (SALTOS)
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Error: shift value must be an integer.")
        continue

    # Processa cada caractere da string de entrada
    for ch in prase:
        if ch in ('ç', 'Ç'):
            ch = 'C' if ch.isupper() else 'c'

        upper = ch.upper()
        
        # Verifica se o caractere é uma letra do alfabeto e aplica a codificação ou decodificação
        if upper in ALPHABET:
            
            # Se escolha for 1, codifica (shift para a direita), se for 2, decodifica (shift para a esquerda)
            if choice == 1:
                # Calcula o índice do novo caractere após aplicar o shift, usando módulo para garantir que fique dentro do alfabeto
                index = (ALPHABET.index(upper) + shift) % 26
            else:
                # Calcula o índice do novo caractere após aplicar o shift, usando módulo para garantir que fique dentro do alfabeto
                index = (ALPHABET.index(upper) - shift) % 26
            result = ALPHABET[index]

            # Mantém a caixa original do caractere (maiúscula ou minúscula)
            if ch.islower():
                result = result.lower()
            
            # Imprime o resultado do caractere codificado ou decodificado
            print(result, end="")
        else:
            print(ch, end="")
    print("\n")