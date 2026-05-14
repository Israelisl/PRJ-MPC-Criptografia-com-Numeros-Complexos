from dataclasses import dataclass


@dataclass(frozen=True)
class Complexo:
    real: float
    imag: float

    # Multiplicação: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
    def multiplicar(self, outro):
        return Complexo(
            self.real * outro.real - self.imag * outro.imag,
            self.real * outro.imag + self.imag * outro.real
        )

    # Divisão: Necessária para a decriptografia
    def dividir(self, outro):
        denominador = outro.real**2 + outro.imag**2
        if denominador == 0:
            raise ValueError("A chave 0 + 0i não pode ser usada para criptografar.")

        return Complexo(
            (self.real * outro.real + self.imag * outro.imag) / denominador,
            (self.imag * outro.real - self.real * outro.imag) / denominador
        )

    # Para facilitar a impressão no console
    def __repr__(self):
        sinal = "+" if self.imag >= 0 else "-"
        return f"({self.real:.2f} {sinal} {abs(self.imag):.2f}i)"


def ler_texto():
    while True:
        texto = input("Digite o texto a ser criptografado: ")
        if texto:
            return texto

        print("O texto não pode ficar vazio.")


def ler_float(mensagem):
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Digite um número válido. Exemplo: 5 ou -2,8")


def ler_chave():
    while True:
        real = ler_float("Parte real da chave: ")
        imag = ler_float("Parte imaginária da chave: ")
        chave = Complexo(real, imag)

        if chave.real != 0 or chave.imag != 0:
            return chave

        print("A chave 0 + 0i não pode ser usada. Escolha outra chave.")


def texto_para_pontos(texto):
    # Cada caractere vira um ponto no eixo real. Exemplo: 'A' -> 65 -> 65 + 0i.
    return [Complexo(ord(char), 0) for char in texto]


def criptografar(pontos, chave):
    return [ponto.multiplicar(chave) for ponto in pontos]


def descriptografar(pontos_cifrados, chave):
    pontos_recuperados = [ponto.dividir(chave) for ponto in pontos_cifrados]
    texto = "".join(chr(round(ponto.real)) for ponto in pontos_recuperados)
    return pontos_recuperados, texto


def imprimir_resultados(texto_original, chave, pontos_originais, pontos_cifrados, texto_decifrado):
    print("\n--- INICIANDO CRIPTOGRAFIA ---")
    print(f"Texto original: {texto_original}")
    print(f"Chave utilizada: {chave}\n")

    print("Coordenadas originais no eixo real:")
    for caractere, ponto in zip(texto_original, pontos_originais):
        print(f" Caractere {caractere!r}: {ponto}")

    print("\nCoordenadas cifradas no plano complexo:")
    for caractere, ponto in zip(texto_original, pontos_cifrados):
        print(f" Caractere {caractere!r} cifrado: {ponto}")

    print("\nTexto cifrado como pares ordenados:")
    print(" ".join(f"{ponto.real:.2f},{ponto.imag:.2f}" for ponto in pontos_cifrados))

    print(f"\nTexto decifrado: {texto_decifrado}")
    print("-" * 30)


def anotar_pontos(ax, texto_original, valores_x, valores_y, cor, sufixo="", peso="normal"):
    deslocamentos = [(0, 10), (0, 24), (0, 38), (0, 52), (0, 66), (0, 80)]

    for i, caractere in enumerate(texto_original):
        dx, dy = deslocamentos[i % len(deslocamentos)]
        ax.annotate(
            f"{i + 1}:{caractere}{sufixo}",
            (valores_x[i], valores_y[i]),
            textcoords="offset points",
            xytext=(dx, dy),
            ha="center",
            color=cor,
            fontsize=10,
            weight=peso,
            arrowprops={"arrowstyle": "-", "color": cor, "alpha": 0.4},
        )


def preparar_plano(ax):
    ax.axhline(0, color="black", linewidth=1.2)
    ax.axvline(0, color="black", linewidth=1.2)
    ax.set_xlabel("Parte real (Re)")
    ax.set_ylabel("Parte imaginária (Im)")
    ax.grid(True, which="both", linestyle=":", alpha=0.5)


def plotar_pontos(texto_original, chave, pontos_originais, pontos_cifrados):
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError:
        print("\nNão foi possível abrir o gráfico porque o matplotlib não está instalado.")
        print("Instale com: pip install -r requirements.txt")
        return

    orig_x = [ponto.real for ponto in pontos_originais]
    orig_y = [ponto.imag for ponto in pontos_originais]
    cif_x = [ponto.real for ponto in pontos_cifrados]
    cif_y = [ponto.imag for ponto in pontos_cifrados]

    figura, (ax_geral, ax_original) = plt.subplots(2, 1, figsize=(12, 9))
    figura.suptitle(f"Representação dos caracteres no plano complexo\nChave: {chave}", fontsize=14)

    ax_geral.scatter(orig_x, orig_y, color="blue", label="Original (eixo real)", s=90, zorder=3)
    ax_geral.scatter(cif_x, cif_y, color="red", label="Cifrado (multiplicado pela chave)", s=90, zorder=3)
    anotar_pontos(ax_geral, texto_original, orig_x, orig_y, "blue", peso="bold")
    anotar_pontos(ax_geral, texto_original, cif_x, cif_y, "red", sufixo="'")

    for i in range(len(pontos_originais)):
        ax_geral.arrow(
            orig_x[i],
            orig_y[i],
            cif_x[i] - orig_x[i],
            cif_y[i] - orig_y[i],
            color="gray",
            linestyle="--",
            alpha=0.3,
            head_width=2,
        )

    ax_geral.set_title("Visão geral: original e cifrado")
    preparar_plano(ax_geral)
    ax_geral.legend()

    ax_original.scatter(orig_x, orig_y, color="blue", label="Original ampliado", s=100, zorder=3)
    anotar_pontos(ax_original, texto_original, orig_x, orig_y, "blue", peso="bold")
    ax_original.set_title("Ampliação dos caracteres originais no eixo real")
    preparar_plano(ax_original)
    ax_original.set_ylim(-8, 14)
    ax_original.set_xlim(min(orig_x) - 3, max(orig_x) + 3)
    ax_original.legend()

    plt.tight_layout()
    plt.show()


def main():
    texto_original = ler_texto()
    chave = ler_chave()

    pontos_originais = texto_para_pontos(texto_original)
    pontos_cifrados = criptografar(pontos_originais, chave)
    _, texto_decifrado = descriptografar(pontos_cifrados, chave)

    imprimir_resultados(texto_original, chave, pontos_originais, pontos_cifrados, texto_decifrado)
    plotar_pontos(texto_original, chave, pontos_originais, pontos_cifrados)


if __name__ == "__main__":
    main()
