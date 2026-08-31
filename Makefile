.POSIX:
.PHONY: all resumes letters templates companies readme hooks check-links export clean

# ######################################
# COMPILADOR
# ######################################
PDFLATEX      = pdflatex
PDFLATEXFLAGS = -interaction=nonstopmode -halt-on-error

# ######################################
# MACROS E FONTES
# ######################################
RESUMES_SRC = \
	resume/resume-en.tex \
	resume/resume-pt.tex
RESUMES_PDF = $(RESUMES_SRC:.tex=.pdf)

LETTERS_SRC = \
	letter/letter-en.tex \
	letter/letter-pt.tex
LETTERS_PDF = $(LETTERS_SRC:.tex=.pdf)

COMPANIES_SRC = \
	companies/ifood/ifuture-2027.tex \
	companies/nubank/internship-2027.tex \
	companies/uber/internship-2026.tex
COMPANIES_PDF = $(COMPANIES_SRC:.tex=.pdf)

TEMPLATES_SRC = \
	template/letter-en.tex \
	template/letter-pt.tex \
	template/resume-en.tex \
	template/resume-pt.tex
TEMPLATES_PDF = $(TEMPLATES_SRC:.tex=.pdf)

ALL_PDF = $(RESUMES_PDF) $(LETTERS_PDF) $(COMPANIES_PDF)

# ######################################
# ALVOS PRINCIPAIS
# ######################################
all: $(ALL_PDF)

resumes: $(RESUMES_PDF)

letters: $(LETTERS_PDF)

companies: $(COMPANIES_PDF)

templates: $(TEMPLATES_PDF)

# ######################################
# UTILITÁRIOS
# ######################################
readme:
	python3 scripts/update_readme.py

hooks:
	git config core.hooksPath .githooks
	chmod +x .githooks/*
	@echo "Git hooks ativados com sucesso!"

check-links:
	python3 scripts/check_links.py

export:
	python3 scripts/export_text.py

# ######################################
# REGRAS DE INFERÊNCIA
# ######################################
.SUFFIXES:
.SUFFIXES: .tex .pdf

.tex.pdf:
	$(PDFLATEX) $(PDFLATEXFLAGS) -output-directory="$(@D)" "$<"

# ######################################
# LIMPEZA
# ######################################
clean:
	rm -f resume/*.aux resume/*.log resume/*.out resume/*.pdf
	rm -f letter/*.aux letter/*.log letter/*.out letter/*.pdf
	rm -f template/*.aux template/*.log template/*.out template/*.pdf
	rm -f companies/*/*.aux companies/*/*.log companies/*/*.out companies/*/*.pdf
