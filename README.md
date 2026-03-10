# 📄 Gabriel Frigo | Currículos (Resumes)
 [![Baixar CV em Português][download_pt_icon]][download_pt]
 [![Baixar Resume em Inglês][download_en_icon]][download_en]

---

## 📌 Sobre o Repositório
 Este repositório armazena o código-fonte estruturado em LaTeX dos meus currículos profissionais. O foco principal destes documentos é destacar minha experiência como Engenheiro de Software, com ênfase em **programação de baixo nível, alta performance (GPGPU) e desenvolvimento de sistemas**.

 A escolha de utilizar LaTeX reflete a busca por um controle tipográfico absoluto, versionamento de texto e a filosofia de tratar documentação como código (*Docs as Code*).

## ⚙️ Automação (CI/CD)
 Para manter o fluxo de atualização rápido e eficiente, este repositório conta com uma esteira de Integração e Entrega Contínuas (CI/CD) via **GitHub Actions**. 

 Sempre que uma alteração é submetida na branch principal:
 1. Um *runner* do GitHub inicializa um ambiente com uma distribuição TeX.
 2. Os arquivos `.tex` são compilados nativamente.
 3. Os PDFs gerados (`resume-pt.pdf` e `resume-en.pdf`) são automaticamente atualizados e disponibilizados para download na aba de *Releases*.

---

## 📖 Estrutura dos Arquivos
 Os currículos estão divididos em dois idiomas principais, mantendo a mesma base de layout e informações adaptadas para seus respectivos mercados:

 * 🇧🇷 **`resume-pt.tex`:** Versão em Português (PT-BR), ideal para vagas no Brasil, com foco no ecossistema de tecnologia e mercado nacional.
 * 🇺🇸 **`resume-en.tex`:** Versão em Inglês (EN-US), direcionada para oportunidades internacionais e empresas que adotam o inglês como idioma primário.

---

## 🛠️ Como Compilar Localmente
 Caso você queira clonar este repositório para inspecionar o código, utilizar o layout ou fazer testes locais sem depender do CI/CD:

 1. Certifique-se de ter uma distribuição LaTeX instalada em seu sistema (como TeX Live no Linux/FreeBSD, ou MiKTeX/TeX Live no Windows via MSYS2).
 2. Clone este repositório em sua máquina:
 ```bash
 git clone [https://github.com/GabrielFrigo4/Resumes.git](https://github.com/GabrielFrigo4/Resumes.git)
 ```

 3. Compile o arquivo `.tex` desejado utilizando o compilador `pdflatex`:
 ```bash
 pdflatex resume-pt.tex
 pdflatex resume-en.tex
 ```

 4. O arquivo `.pdf` correspondente será gerado no mesmo diretório.

---

## 🔗 Links Úteis
 * **Meu Perfil do GitHub:** [GabrielFrigo4](https://github.com/GabrielFrigo4)
 * **LinkedIn:** [gabriel-frigo](https://www.linkedin.com/in/gabriel-frigo-b6727b275/)

[download_pt]: https://github.com/GabrielFrigo4/Resumes/releases/latest/download/resume-pt.pdf
[download_pt_icon]: https://img.shields.io/badge/PT--BR-Baixar_PDF-red?style=for-the-badge&logo=adobeacrobatreader

[download_en]: https://github.com/GabrielFrigo4/Resumes/releases/latest/download/resume-en.pdf
[download_en_icon]: https://img.shields.io/badge/EN--US-Baixar_PDF-blue?style=for-the-badge&logo=adobeacrobatreader