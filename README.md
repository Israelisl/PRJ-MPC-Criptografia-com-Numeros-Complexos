# Criptografia com Números Complexos

Este projeto foi desenvolvido por Israel da Silva Lemes e Rainan de Oliveira Reis para a disciplina de Estrutura de Dados, do curso Desenvolvimento de Software Multiplataforma - 2° Semestre.

O programa demonstra como números complexos podem ser usados em um algoritmo criptográfico simples de mistura de caracteres. Cada caractere do texto original é representado como um ponto no plano cartesiano, usando seu código numérico como parte real. Em seguida, esse ponto é multiplicado por uma chave complexa, gerando a versão cifrada. Para decifrar, o programa divide os pontos cifrados pela mesma chave.

## Objetivo

Atender ao enunciado PRJ.5:

> Números complexos podem ser utilizados como algoritmos criptográficos simples de mistura de caracteres. Desenvolva um programa que receba como entrada um texto e que efetue a criptografia desse texto utilizando mistura através da multiplicação por um número complexo que representa uma chave. Um programa que conheça a chave, ou seja, o número complexo original, deve ser capaz de decifrar o texto cifrado. Na solução desse problema, ilustre como ficam as representações dos caracteres do texto original e cifrado no plano cartesiano.

## Como funciona

1. O usuário digita um texto.
2. O usuário informa a parte real e a parte imaginária da chave complexa.
3. Cada caractere é convertido para seu código numérico com `ord()`.
4. Cada código vira um ponto complexo no formato `código + 0i`.
5. O ponto é multiplicado pela chave complexa.
6. Para recuperar o texto, o programa divide o ponto cifrado pela mesma chave.
7. O resultado é exibido no terminal e representado em um gráfico no plano cartesiano.

## Requisitos

- Python 3
- matplotlib

Instale as dependências com:

```powershell
pip install -r requirements.txt
```

## Como executar

Na pasta do projeto, execute:

```powershell
python criptografiaNroComplexo.py
```

Depois informe o texto e a chave complexa quando o programa solicitar.

Exemplo:

```text
Digite o texto a ser criptografado: GUIVEN
Parte real da chave: 5
Parte imaginária da chave: -2.8
```

O programa exibirá:

- As coordenadas originais dos caracteres.
- As coordenadas cifradas.
- O texto cifrado como pares ordenados.
- O texto decifrado.
- Um gráfico comparando os pontos originais e cifrados no plano cartesiano.

## Observação

A chave `0 + 0i` não pode ser usada, pois a descriptografia depende da divisão pela chave, e não existe divisão por zero.
