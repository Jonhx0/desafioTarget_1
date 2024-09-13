# Captura o valor 'string' na variável 'texto'.
texto = input("\nDigite uma frase ou palavra.\n")

# Conversão dos 'a' para minúsculo e verificação se eles estão nas strings.
if 'a' in texto.lower():
    print("Tem a letra 'a' na frase/palavra.")
    
    # Contagem dos 'a'.
    contador = texto.lower().count('a')
    print(f"A letra 'a' apareceu {contador} vezes na palavra/frase.")
else:
    print("Não tem a letra 'a' na frase/palavra.")
