.PHONY: all clean resumes letters templates companies

# ##############################################################################
# DESCOBERTA DINÂMICA DE ARQUIVOS
# ##############################################################################
RESUMES_SRC := $(wildcard Resume/*.tex)
RESUMES_PDF := $(RESUMES_SRC:.tex=.pdf)

LETTERS_SRC := $(wildcard Letter/*.tex)
LETTERS_PDF := $(LETTERS_SRC:.tex=.pdf)

TEMPLATES_SRC := $(wildcard Template/*.tex)
TEMPLATES_PDF := $(TEMPLATES_SRC:.tex=.pdf)

COMPANIES_SRC := $(wildcard Companies/*/*.tex)
COMPANIES_PDF := $(COMPANIES_SRC:.tex=.pdf)

ALL_PDF := $(RESUMES_PDF) $(LETTERS_PDF) $(TEMPLATES_PDF) $(COMPANIES_PDF)

# ##############################################################################
# COMPILAÇÃO GERAL (TODOS OS ARQUIVOS)
# ##############################################################################
all: $(ALL_PDF)

# ##############################################################################
# COMPILAÇÃO ESPECÍFICA POR PASTA
# ##############################################################################
resumes: $(RESUMES_PDF)

letters: $(LETTERS_PDF)

templates: $(TEMPLATES_PDF)

companies: $(COMPANIES_PDF)

# ##############################################################################
# REGRA DE COMPILAÇÃO (.tex -> .pdf)
# ##############################################################################
%.pdf: %.tex
	pdflatex -output-directory=$(dir $<) $<

# ##############################################################################
# LIMPEZA DOS ARQUIVOS GERADOS
# ##############################################################################
clean:
	rm -f Resume/*.aux Resume/*.log Resume/*.out Resume/*.pdf
	rm -f Letter/*.aux Letter/*.log Letter/*.out Letter/*.pdf
	rm -f Template/*.aux Template/*.log Template/*.out Template/*.pdf
	rm -f Companies/*/*.aux Companies/*/*.log Companies/*/*.out Companies/*/*.pdf
