<div align="center">
    <h1>Gabriel Frigo — Resumes & Letters</h1>
    <p>Repositório central de currículos, cartas de apresentação e modelos customizados em <b>LaTeX</b>.</p>
</div>

<p align="center">
    <a href="https://github.com/GabrielFrigo4/Resumes/actions/workflows/LaTeX.yml"><img src="https://github.com/GabrielFrigo4/Resumes/actions/workflows/LaTeX.yml/badge.svg" alt="Compilação LaTeX"></a>
    <a href="https://github.com/GabrielFrigo4/Resumes/releases/latest"><img src="https://img.shields.io/github/v/release/GabrielFrigo4/Resumes?label=Release&color=blue" alt="Última Release"></a>
    <a href="https://github.com/GabrielFrigo4/Resumes/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="Licença"></a>
</p>

---

## ⚡ Download Rápido (Última Release)

| Documento | Idioma | Formato | Link de Download |
| :--- | :---: | :---: | :---: |
| **Currículo Oficial (PT-BR)** | 🇧🇷 Português | PDF | [![Baixar PDF](https://img.shields.io/badge/PDF-Baixar-red?style=flat-square&logo=adobeacrobatreader)](https://github.com/GabrielFrigo4/Resumes/releases/latest/download/resume-pt.pdf) |
| **Resume Oficial (EN-US)** | 🇺🇸 Inglês | PDF | [![Baixar PDF](https://img.shields.io/badge/PDF-Baixar-blue?style=flat-square&logo=adobeacrobatreader)](https://github.com/GabrielFrigo4/Resumes/releases/latest/download/resume-en.pdf) |
| **Carta de Apresentação (PT-BR)** | 🇧🇷 Português | PDF | [![Baixar PDF](https://img.shields.io/badge/PDF-Baixar-darkred?style=flat-square&logo=adobeacrobatreader)](https://github.com/GabrielFrigo4/Resumes/releases/latest/download/letter-pt.pdf) |
| **Cover Letter (EN-US)** | 🇺🇸 Inglês | PDF | [![Baixar PDF](https://img.shields.io/badge/PDF-Baixar-darkblue?style=flat-square&logo=adobeacrobatreader)](https://github.com/GabrielFrigo4/Resumes/releases/latest/download/letter-en.pdf) |

---

## 📖 Estrutura do Repositório

Os documentos estão divididos em dois idiomas, mantendo a mesma base de layout com informações adaptadas para os respectivos mercados:

```
resumes/
├── resume/
│   ├── resume-pt.tex
│   ├── resume-en.tex
│   ├── resume-pt.txt
│   └── resume-en.txt
├── letter/
│   ├── letter-pt.tex
│   └── letter-en.tex
├── template/
│   ├── resume-pt.tex
│   ├── resume-en.tex
│   ├── letter-pt.tex
│   └── letter-en.tex
├── companies/
│   ├── ifood/
│   ├── nubank/
│   └── uber/
├── scripts/
│   ├── check_links.py
│   ├── export_text.py
│   └── update_readme.py
├── .githooks/
│   └── pre-commit
├── .github/workflows/
│   └── LaTeX.yml
├── Makefile
└── README.md
```

### 📄 [Currículos](./resume)

- 🇧🇷 **[`resume-pt.tex`](./resume/resume-pt.tex):** Currículo em Português (PT-BR), ideal para vagas no Brasil, com foco no ecossistema de tecnologia nacional.
- 🇺🇸 **[`resume-en.tex`](./resume/resume-en.tex):** Resume em Inglês (EN-US), direcionado para oportunidades internacionais.

### ✉️ [Cartas de Apresentação](./letter)

- 🇧🇷 **[`letter-pt.tex`](./letter/letter-pt.tex):** Carta de Apresentação oficial pronta para envio (Open Application / Apresentação Geral).
- 🇺🇸 **[`letter-en.tex`](./letter/letter-en.tex):** Cover Letter oficial em inglês pronta para envio global.

### 📝 [Templates Base](./template)

Modelos do layout otimizados para ATS e preparados para customização por vaga:

- 🇧🇷 **[`resume-pt.tex`](./template/resume-pt.tex) & 🇺🇸 [`resume-en.tex`](./template/resume-en.tex):** Modelos base de currículo.
- 🇧🇷 **[`letter-pt.tex`](./template/letter-pt.tex) & 🇺🇸 [`letter-en.tex`](./template/letter-en.tex):** Modelos base de carta com `\targetRole` e `\targetCompany`.

---

## 🎯 Como Personalizar para uma Vaga

1. Copie o template da sua língua e tipo de documento preferido em `template/` (ex: `template/resume-pt.tex` ou `template/letter-pt.tex`).
2. Defina as variáveis no início do arquivo:
    ```latex
    \newcommand{\targetRole}{Estágio em Desenvolvimento}
    \newcommand{\targetCompany}{Nome da Empresa}
    ```
3. Compile com `make` e envie!

---

## 🛠️ Como Compilar Localmente

```bash
git clone "https://github.com/GabrielFrigo4/Resumes.git"
```

Comandos de automação disponíveis via `Makefile`:

```bash
make all
make resumes
make letters
make companies
make templates
make readme
make hooks
make check-links
make export
make clean
```

---

## 🏢 Documentos por Empresa (companies)

Documentos customizados para processos seletivos específicos:

<!-- COMPANIES_TABLE_START -->
| Empresa | Documento / Vaga | Idioma | Download |
| :--- | :--- | :---: | :---: |
| **iFood** | iFuture 2027 (`ifuture-2027.pdf`) | 🇧🇷 PT-BR | [![Baixar](https://img.shields.io/badge/PDF-Baixar-EA1D2C?style=flat-square&logo=adobeacrobatreader)](https://github.com/GabrielFrigo4/Resumes/releases/latest/download/ifuture-2027.pdf) |
| **Nubank** | Estágio 2027 (`internship-2027.pdf`) | 🇧🇷 PT-BR | [![Baixar](https://img.shields.io/badge/PDF-Baixar-8A05BE?style=flat-square&logo=adobeacrobatreader)](https://github.com/GabrielFrigo4/Resumes/releases/latest/download/internship-2027.pdf) |
| **Uber** | Internship 2026 (`internship-2026.pdf`) | 🇺🇸 EN-US | [![Baixar](https://img.shields.io/badge/PDF-Baixar-000000?style=flat-square&logo=adobeacrobatreader)](https://github.com/GabrielFrigo4/Resumes/releases/latest/download/internship-2026.pdf) |
<!-- COMPANIES_TABLE_END -->

---

## 🔗 Links Úteis

- **Portfólio:** [gabrielfrigo.dev.br](https://gabrielfrigo.dev.br)
- **LinkedIn:** [linkedin.com/in/gabriel-frigo](https://linkedin.com/in/gabriel-frigo-b6727b275/)
- **GitHub:** [github.com/GabrielFrigo4](https://github.com/GabrielFrigo4)
