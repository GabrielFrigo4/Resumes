# 📄 Gabriel Frigo | Currículos e Cartas de Apresentação (Resumes & Cover Letters)
 | 🇧🇷 Português (PT-BR) | 🇺🇸 English (EN-US) |
 | :---: | :---: |
 | [![Baixar CV em Português][download_resume_pt_icon]][download_resume_pt] | [![Baixar Resume em Inglês][download_resume_en_icon]][download_resume_en] |
 | [![Baixar Carta em Português][download_letter_pt_icon]][download_letter_pt] | [![Baixar Cover Letter em Inglês][download_letter_en_icon]][download_letter_en] |

---

## 📌 Sobre o Repositório
 Este repositório armazena o código-fonte estruturado em LaTeX dos meus currículos profissionais e cartas de apresentação. O foco principal destes documentos é destacar a minha experiência como Engenheiro de Software, com ênfase em **programação de baixo nível, alta performance (GPGPU) e desenvolvimento de sistemas**.

 A escolha de utilizar LaTeX reflete a procura por um controlo tipográfico absoluto, versionamento de texto e a filosofia de tratar a documentação como código (*Docs as Code*).

## ⚙️ Automação (CI/CD)
 Para manter o fluxo de atualização rápido e eficiente, este repositório conta com uma esteira de Integração e Entrega Contínuas (CI/CD) via **GitHub Actions**. 

 Sempre que uma alteração é submetida na branch principal:
 1. Um *runner* do GitHub inicializa um ambiente com uma distribuição TeX.
 2. Os ficheiros `.tex` são compilados nativamente.
 3. Os PDFs gerados ([`resume-pt.pdf`][download_resume_pt], [`resume-en.pdf`][download_resume_en], [`letter-pt.pdf`][download_letter_pt] e [`letter-en.pdf`][download_letter_en]) são automaticamente atualizados e disponibilizados para download na aba de *Releases*.

---

## 📖 Estrutura dos Ficheiros
 Os documentos estão divididos em dois idiomas principais, mantendo a mesma base de layout e informações adaptadas para os seus respetivos mercados:

### 📄 [Currículos](./Resume)
 * 🇧🇷 **[`resume-pt.tex`](./Resume/resume-pt.tex):** Currículo em Português (PT-BR), ideal para vagas no Brasil, com foco no ecossistema de tecnologia e mercado nacional.
 * 🇺🇸 **[`resume-en.tex`](./Resume/resume-en.tex):** Resume em Inglês (EN-US), direcionado para oportunidades internacionais e empresas que adotam o inglês como idioma primário.

### ✉️ [Cartas de Apresentação](./Letter)
 * 🇧🇷 **[`letter-pt.tex`](./Letter/letter-pt.tex):** Carta de Apresentação em Português, destacando a ligação entre a minha lógica matemática e implementação técnica.
 * 🇺🇸 **[`letter-en.tex`](./Letter/letter-en.tex):** Cover Letter em Inglês, estruturada para candidaturas globais e comunicação com equipas internacionais.

### 📝 [Templates Base (Boilerplates)](./Template)
 Disponibilizei versões "limpas" e padronizadas do meu layout, otimizadas para ATS e livres de inconsistências (como o uso misto de `\section` e `\section*`), para quem quiser clonar a estrutura:
 * 🇧🇷 **[`template-pt.tex`](./Template/template-pt.tex):** Template genérico em Português.
 * 🇺🇸 **[`template-en.tex`](./Template/template-en.tex):** Template genérico em Inglês.

---

## 🛠️ Como Compilar Localmente
 Caso queira clonar este repositório para inspecionar o código, utilizar o layout ou fazer testes locais sem depender do CI/CD:

 1. Certifique-se de ter uma distribuição LaTeX instalada no seu sistema (como TeX Live no Linux/FreeBSD, ou MiKTeX/TeX Live no Windows via MSYS2).

 2. Clone este repositório na sua máquina:
 ```bash
 git clone "https://github.com/GabrielFrigo4/Resumes.git"
 ```

 3. Compile o ficheiro `.tex` desejado utilizando o compilador `pdflatex`:
 ```bash
 pdflatex resume-pt.tex
 pdflatex resume-en.tex
 pdflatex letter-pt.tex
 pdflatex letter-en.tex
 ```

 4. O ficheiro `.pdf` correspondente será gerado no mesmo diretório.

---

## 🔗 Links Úteis
 * **Meu Perfil do GitHub:** [GabrielFrigo4](https://github.com/GabrielFrigo4)
 * **LinkedIn:** [gabriel-frigo](https://www.linkedin.com/in/gabriel-frigo-b6727b275/)

[download_resume_pt]: https://github.com/GabrielFrigo4/Resumes/releases/latest/download/resume-pt.pdf
[download_resume_pt_icon]: https://img.shields.io/badge/CURRÍCULO_PT--BR-Baixar_PDF-red?style=for-the-badge&logo=adobeacrobatreader

[download_resume_en]: https://github.com/GabrielFrigo4/Resumes/releases/latest/download/resume-en.pdf
[download_resume_en_icon]: https://img.shields.io/badge/RESUME_EN--US-Baixar_PDF-blue?style=for-the-badge&logo=adobeacrobatreader

[download_letter_pt]: https://github.com/GabrielFrigo4/Resumes/releases/latest/download/letter-pt.pdf
[download_letter_pt_icon]: https://img.shields.io/badge/CARTA_PT--BR-Baixar_PDF-darkred?style=for-the-badge&logo=adobeacrobatreader

[download_letter_en]: https://github.com/GabrielFrigo4/Resumes/releases/latest/download/letter-en.pdf
[download_letter_en_icon]: https://img.shields.io/badge/LETTER_EN--US-Baixar_PDF-darkblue?style=for-the-badge&logo=adobeacrobatreader
