# 📄 Currículos Oficiais (`resume/`)

Esta pasta armazena o código-fonte em LaTeX dos currículos oficiais completos, mantidos sempre atualizados e sem placeholders.

---

## 📑 Documentos Disponíveis

| Arquivo | Idioma | Mercado / Foco | Download da Release |
| :--- | :---: | :--- | :---: |
| **[`resume-pt.tex`](./resume-pt.tex)** | 🇧🇷 PT-BR | Vagas nacionais, ecossistema tech brasileiro | [![Baixar](https://img.shields.io/badge/PDF-Baixar-red?style=flat-square&logo=adobeacrobatreader)](https://github.com/GabrielFrigo4/Resumes/releases/latest/download/resume-pt.pdf) |
| **[`resume-en.tex`](./resume-en.tex)** | 🇺🇸 EN-US | Oportunidades internacionais e remotas globais | [![Baixar](https://img.shields.io/badge/PDF-Baixar-blue?style=flat-square&logo=adobeacrobatreader)](https://github.com/GabrielFrigo4/Resumes/releases/latest/download/resume-en.pdf) |

---

## 🛠️ Compilação Local

Para compilar apenas os currículos oficiais:

```bash
make resumes
```

Para compilar um arquivo específico manualmente:

```bash
pdflatex -output-directory=resume resume/resume-pt.tex
pdflatex -output-directory=resume resume/resume-en.tex
```

---

## ⚙️ Integração com CI/CD

Os arquivos desta pasta são compilados automaticamente pela pipeline do GitHub Actions a cada *push* nas branches principais, atualizando os PDFs na release `latest`.
