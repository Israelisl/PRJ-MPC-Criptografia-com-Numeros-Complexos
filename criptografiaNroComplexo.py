import matplotlib.pyplot as plt

class Complexo:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Multiplicação: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
    def multiplicar(self, outro):
        return Complexo(
            self.real * outro.real - self.imag * outro.imag,
            self.real * outro.imag + self.imag * outro.real
        )

    # Divisão: Necessária para a decriptografia
    def dividir(self, outro):
        denominador = outro.real**2 + outro.imag**2
        return Complexo(
            (self.real * outro.real + self.imag * outro.imag) / denominador,
            (self.imag * outro.real - self.real * outro.imag) / denominador
        )

    # Para facilitar a impressão no console
    def __repr__(self):
        return f"({self.real:.2f} + {self.imag:.2f}i)"

# --- CONFIGURAÇÃO ---
texto_original = "GUIVEN"
# A chave pode ser qualquer número complexo. 
# Experimente mudar para (1, 1) para ver uma rotação de 45 graus!
chave = Complexo(5, -2.8) 

print(f"--- INICIANDO CRIPTOGRAFIA ---")
print(f"Texto Original: {texto_original}")
print(f"Chave Utilizada: {chave}\n")

# 1. REPRESENTAÇÃO ORIGINAL (Cada letra vira um ponto no Eixo Real)
# Ex: 'A' -> 65 -> (65 + 0i)
pontos_originais = [Complexo(ord(char), 0) for char in texto_original]

print("Coordenadas Originais (no Eixo Real):")
for i, p in enumerate(pontos_originais):
    print(f" Letra '{texto_original[i]}': {p}")

# 2. CRIPTOGRAFIA (Multiplicação pela Chave)
pontos_cifrados = [p.multiplicar(chave) for p in pontos_originais]

print("\nCoordenadas Cifradas (Misturadas no Plano):")
for i, p in enumerate(pontos_cifrados):
    print(f" Letra '{texto_original[i]}' cifrada: {p}")

# 3. DECRIPTOGRAFIA (Divisão pela Chave)
pontos_recuperados = [p.dividir(chave) for p in pontos_cifrados]
texto_final = "".join([chr(round(p.real)) for p in pontos_recuperados])

print(f"\nTexto Decifrado: {texto_final}")
print("-" * 30)

# --- VISUALIZAÇÃO COM MATPLOTLIB ---
plt.figure(figsize=(12, 7))

# Extrair dados para o gráfico
orig_x = [p.real for p in pontos_originais]
orig_y = [p.imag for p in pontos_originais]
cif_x = [p.real for p in pontos_cifrados]
cif_y = [p.imag for p in pontos_cifrados]

# Plotar pontos originais
plt.scatter(orig_x, orig_y, color='blue', label='Original (Letras no Eixo X)', s=100, zorder=3)
for i, txt in enumerate(texto_original):
    plt.annotate(f" {txt}", (orig_x[i], orig_y[i]), color='blue', fontsize=12, weight='bold')

# Plotar pontos cifrados
plt.scatter(cif_x, cif_y, color='red', label='Cifrado (Rotacionado + Escalonado)', s=100, zorder=3)
for i, txt in enumerate(texto_original):
    plt.annotate(f" {txt}'", (cif_x[i], cif_y[i]), color='red', fontsize=12)

# Desenhar setas mostrando o "salto" de cada letra (opcional, mas visualmente incrível)
for i in range(len(pontos_originais)):
    plt.arrow(orig_x[i], orig_y[i], cif_x[i]-orig_x[i], cif_y[i]-orig_y[i], 
              color='gray', linestyle='--', alpha=0.3, head_width=2)

# Configurações do Plano Cartesiano
plt.axhline(0, color='black', linewidth=1.5) # Eixo Real
plt.axvline(0, color='black', linewidth=1.5) # Eixo Imaginário
plt.title(f"Transformação de Caracteres no Plano Complexo\nChave: {chave}", fontsize=14)
plt.xlabel("Parte Real (Re)")
plt.ylabel("Parte Imaginária (Im)")
plt.grid(True, which='both', linestyle=':', alpha=0.5)
plt.legend()
plt.tight_layout()

plt.show()