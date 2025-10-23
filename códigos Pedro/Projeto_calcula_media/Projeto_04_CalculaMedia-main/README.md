
# 📘 Calculadora de Média Escolar

Um mini-projeto em **Python** para calcular a média das **4 notas bimestrais** de um estudante. Foco em praticar **entrada de dados**, **operações matemáticas** e **exibição formatada**.

---

## 🎯 Objetivo Educacional
- Reforçar a lógica de **entrada → processamento → saída**.
- Trabalhar com **`input()`**, **conversão para `float`**, operações aritméticas e **f-strings**.
- Introduzir **boas práticas** (funções puras, validação, testes).

---

## 📝 Enunciado
Você foi convidado a criar uma **Calculadora de Média Escolar**. Seu programa deve:
1. Pedir as **4 notas bimestrais** do estudante (valores de 0 a 10).
2. Calcular a **média aritmética**.
3. Exibir a média **com 2 casas decimais**.
4. Mostrar um **feedback** com base na média:
   - **≥ 7.0** → **Aprovado(a)** ✅
   - **≥ 5.0 e < 7.0** → **Recuperação** ⚠️
   - **< 5.0** → **Reprovado(a)** ❌

> Exemplo:
```
Digite a 1ª nota: 7.0
Digite a 2ª nota: 8.5
Digite a 3ª nota: 6.0
Digite a 4ª nota: 9.0

Média: 7.63 — Situação: Aprovado(a) ✅
```

---

## 💻 Como executar

Pré-requisito: **Python 3.8+**

1) Clone este repositório ou baixe os arquivos.
```bash
git clone https://github.com/seu-usuario/projeto-fabrica-1.git
cd projeto-fabrica-1
```

2) Rode o programa:
```bash
python media.py
```

3) Digite as quatro notas quando solicitado. Pronto! 🎉

> Dica (Windows): se `python` não funcionar, tente `py media.py`.

---

## 🧪 (Opcional) Rodando testes
Sem dependências externas. Use o próprio `unittest` do Python:
```bash
python -m unittest
```

---

## 🧠 Conceitos trabalhados
- Entrada de dados com `input()`
- Conversão e validação de `float`
- Funções puras e testáveis (`calcular_media`, `classificar_media`)
- Formatação de saída com f-strings
- Organização de projeto e **README**

---

## 🚀 Extensões sugeridas
- Permitir **n** notas (não só 4).
- Salvar histórico de médias em um arquivo `.csv`.
- Criar uma GUI simples com **Tkinter**.
- Internacionalização (exibir mensagens em **pt**/**en**).

---

## 📂 Estrutura do projeto
```
projeto-fabrica-1/
├─ media.py
├─ README.md
├─ tests/
│  └─ test_media.py
├─ .gitignore
└─ LICENSE
```

---

## 📝 Licença
Este projeto está sob licença **MIT** — sinta-se à vontade para usar e adaptar em suas aulas. ✨

