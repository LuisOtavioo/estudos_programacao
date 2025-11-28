def contar_consoantes(texto):

    VOGAIS = "aeiouáéíóúãõ"
    consoantes_encontradas = []
    
    for caractere in texto:
        caractere_lower = caractere.lower()
        
        # O método isalpha() é mais robusto para isso.
        if caractere_lower.isalpha():
            if caractere_lower not in VOGAIS:
                consoantes_encontradas.append(caractere)
    
    print(f"String original: '{texto}'")
    print(f"Consoantes lidas ({len(consoantes_encontradas)}): {' '.join(consoantes_encontradas)}")
    print(f"Total de consoantes lidas: {len(consoantes_encontradas)}")

print("\n--- Solução Idiomática ---\n")
string_lida_2 = input("Digite outra string: ")
contar_consoantes(string_lida_2)