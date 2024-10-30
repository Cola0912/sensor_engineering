# Makefile for XeLaTeX Compilation
TEXFILE = homework
LATEX = xelatex
FLAGS = -interaction=nonstopmode -halt-on-error
OUTPUT = HW1_21C1002_相田舟星_レポート1.pdf

.PHONY: all clean

all: $(OUTPUT)

$(OUTPUT): $(TEXFILE).tex
	$(LATEX) $(FLAGS) $(TEXFILE).tex
	$(LATEX) $(FLAGS) $(TEXFILE).tex  # for cross-references and TOC
	mv $(TEXFILE).pdf $(OUTPUT)

clean:
	rm -f $(TEXFILE).aux $(TEXFILE).log $(TEXFILE).out $(OUTPUT)
