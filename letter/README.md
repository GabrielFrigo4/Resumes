# ✉️ Cartas de Apresentação Oficiais (`letter/`)

Esta pasta contém as cartas de apresentação institucionais oficiais (modelo *Open Application* / candidatura geral), prontas para leitura e distribuição pública.

---

## 📑 Documentos Disponíveis

| Arquivo | Idioma | Finalidade | Download da Release |
| :--- | :---: | :--- | :---: |
| **[`letter-pt.tex`](./letter-pt.tex)** | 🇧🇷 PT-BR | Carta de apresentação institucional em português | [![Baixar](https://img.shields.io/badge/PDF-Baixar-darkred?style=flat-square&logo=adobeacrobatreader)](https://github.com/GabrielFrigo4/Resumes/releases/latest/download/letter-pt.pdf) |
| **[`letter-en.tex`](./letter-en.tex)** | 🇺🇸 EN-US | Cover letter institucional para oportunidades globais | [![Baixar](https://img.shields.io/badge/PDF-Baixar-darkblue?style=flat-square&logo=adobeacrobatreader)](https://github.com/GabrielFrigo4/Resumes/releases/latest/download/letter-en.pdf) |

---

## 🛠️ Compilação Local

Para compilar apenas as cartas oficiais:

```bash
make letters
```

---

## 💡 Cartas Específicas por Vaga

Se você deseja gerar uma carta personalizada para uma empresa específica:
1. Copie o template em [`template/letter-pt.tex`](../template/letter-pt.tex) ou [`template/letter-en.tex`](../template/letter-en.tex).
2. Crie uma pasta dentro de [`companies/`](../companies/) (ex: `companies/empresa/letter.tex`).
3. Ajuste as variáveis `\targetRole` e `\targetCompany` no topo do arquivo.
