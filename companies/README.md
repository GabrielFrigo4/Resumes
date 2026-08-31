# 🏢 Documentos por Empresa (`companies/`)

Esta pasta armazena versões customizadas de currículos e cartas para processos seletivos e empresas específicas.

---

## 📑 Empresas e Vagas Cadastradas

| Empresa | Pasta | Documento | Idioma |
| :--- | :--- | :--- | :---: |
| 🟣 **Nubank** | [`companies/nubank/`](./nubank/) | `internship-2027.tex` | 🇧🇷 PT-BR |
| ⚫ **Uber** | [`companies/uber/`](./uber/) | `internship-2026.tex` | 🇺🇸 EN-US |
| 🔴 **iFood** | [`companies/ifood/`](./ifood/) | `ifuture-2027.tex` | 🇧🇷 PT-BR |

---

## ➕ Como Adicionar uma Nova Empresa

1. **Crie a pasta da empresa** (em letras minúsculas):
   ```bash
   mkdir -p companies/nome_empresa
   ```
2. **Copie o template desejado**:
   ```bash
   cp template/resume-pt.tex companies/nome_empresa/cargo-ano.tex
   ```
3. **Personalize o conteúdo** com as palavras-chave e competências mais alinhadas à vaga.
4. **Atualize o README.md**:
   ```bash
   make readme
   ```
5. **Compile localmente para validar**:
   ```bash
   make companies
   ```

---

## ⚙️ Automação e CI/CD

Quando novos arquivos `.tex` são adicionados nesta pasta e enviados para o GitHub:
- A pipeline do GitHub Actions compila automaticamente o PDF e o publica na Release `latest`.
- O script [`scripts/update_readme.py`](../scripts/update_readme.py) roda no CI para atualizar a tabela dinâmica do [`README.md`](../README.md) principal.
