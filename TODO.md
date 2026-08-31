# 📋 Roadmap & Backlog de Tarefas (TODO)

Este documento centraliza as tarefas planejadas, melhorias contínuas e ideias práticas para o repositório.

---

## 📌 Tarefas Concluídas

Lista de tarefas e melhorias técnicas implementadas e integradas com sucesso ao repositório:

- [x] **Configuração de Git Hooks / Pré-Commit Local:**
    - Hook de pre-commit nativo criado em `.githooks/pre-commit` e ativável via `make hooks`.
    - Executa `make readme` automaticamente antes do commit para sincronizar a tabela de empresas no `README.md`.
    - Executa verificação de formatação nos arquivos `.tex` em *staged*.

- [x] **Validação de Links Externos no CI:**
    - Script `scripts/check_links.py` criado e integrado ao `make check-links` e ao workflow do GitHub Actions.
    - Valida o status HTTP de todos os links externos.

- [x] **Exportação em Texto Puro para Plataformas de Vagas (ATS):**
    - Script `scripts/export_text.py` com parser LaTeX integrado ao comando `make export`.
    - Gera versões limpas em `resume/resume-pt.txt` e `resume/resume-en.txt`.
