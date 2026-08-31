# 📝 Modelos Base e Esqueletos (`template/`)

Esta pasta contém os modelos de código-fonte reutilizáveis para currículos e cartas de apresentação. Os arquivos daqui são otimizados para ATS e estruturados com variáveis centralizadas no topo para facilitar a personalização.

> ℹ️ **Nota de CI/CD:** Os arquivos desta pasta são mantidos como modelos e **não são compilados nas releases públicas do GitHub**.

---

## 📑 Modelos Disponíveis

### 📄 Modelos de Currículo
- **[`resume-pt.tex`](./resume-pt.tex)**: Template de currículo em Português (PT-BR).
- **[`resume-en.tex`](./resume-en.tex)**: Template de currículo em Inglês (EN-US).

### ✉️ Modelos de Carta de Apresentação
- **[`letter-pt.tex`](./letter-pt.tex)**: Template de carta com variáveis parametrizáveis (`\targetRole`, `\targetCompany`).
- **[`letter-en.tex`](./letter-en.tex)**: Template de cover letter em inglês.

---

## 🎯 Como Usar os Templates

### 1. Bloco de Variáveis no Topo
Cada template possui um bloco inicial configurável. Basta editar os valores para atualizar o documento:

```latex
\newcommand{\candidateName}{Seu Nome}
\newcommand{\candidateLocation}{Sua Cidade, Estado}
\newcommand{\candidatePhone}{+55 11 90000-0000}
\newcommand{\candidateEmail}{seu.email@exemplo.com}
\newcommand{\candidateLinkedInUser}{seu-usuario}
\newcommand{\candidateLinkedInURL}{https://linkedin.com/in/seu-usuario}
\newcommand{\candidateGitHubUser}{seu-github}
\newcommand{\candidateGitHubURL}{https://github.com/seu-github}
\newcommand{\candidateWebsite}{seuportfolio.com}
\newcommand{\candidateWebsiteURL}{https://seuportfolio.com}

\newcommand{\targetRole}{Cargo Desejado}
\newcommand{\targetCompany}{Nome da Empresa}
```

### 2. Guias de Personalização
Procure pelos comentários `% PERSONALIZAR:` (ou `% CUSTOMIZE:`) ao longo do arquivo para orientações de adaptação de cada seção.

---

## 🛠️ Teste de Compilação Local

Para testar a compilação de todos os templates localmente:

```bash
make templates
```
