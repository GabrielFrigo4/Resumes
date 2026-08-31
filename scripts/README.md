# 🛠️ Scripts e Utilitários (`scripts/`)

Esta pasta contém scripts de automação e utilitários auxiliares do repositório, desenvolvidos em Python sem dependências externas e seguindo os princípios de Clean Code.

---

## 📜 Scripts Disponíveis

### 1. `update_readme.py` (Tabela Dinâmica de Empresas)
Varre a pasta [`companies/`](../companies/) para detectar automaticamente novas candidaturas/documentos e injeta a tabela Markdown formatada (com badges do Shields.io e links diretos para o download da release) dentro do [`README.md`](../README.md) principal.

```bash
make readme
```

---

### 2. `check_links.py` (Validador de Links Externos)
Varre todos os arquivos `.tex` do repositório, extrai URLs (`https://...`), realiza requisições HTTP e valida se todos os links (LinkedIn, GitHub, portfólio, projetos e certificados) continuam ativos e funcionais.

```bash
make check-links
```

---

### 3. `export_text.py` (Exportador para ATS / Texto Puro)
Converte os currículos oficiais ([`resume/resume-pt.tex`](../resume/resume-pt.tex) e [`resume/resume-en.tex`](../resume/resume-en.tex)) em versões limpas em texto puro ([`resume/resume-pt.txt`](../resume/resume-pt.txt) e [`resume/resume-en.txt`](../resume/resume-en.txt)), ideais para copiar e colar em plataformas de recrutamento (Gupy, Greenhouse, Lever, Workday).

```bash
make export
```
