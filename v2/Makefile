# v2/Makefile — dissertation build system (ported from onlycodes/paper).
#
# Targets:
#   make deps     — install Python dependencies from requirements.txt
#   make figures  — render all figures_src/*.py scripts → generated/figures/
#   make values   — build_numbers.py: CSVs + sidecars → generated/values.tex
#   make lint     — BIB GATE: bare-digit-not-in-citation check on prose .tex
#   make paper    — figures + values + lint + latexmk -pdf main.tex
#   make clean    — remove generated/ and latexmk byproducts
#
# First-time setup:
#   make deps     (installs pandas, numpy, scipy, matplotlib)
#   make paper
#
# Use a non-system Python (recommended; keeps the repo venv-isolated):
#   make PYTHON=../.venv/bin/python paper
#
# LaTeX (latexmk) is required for 'make paper'; all other targets work without it.

PYTHON   ?= python3
PAPER_DIR = $(CURDIR)
MAIN      = main

# All figure renderer scripts (none yet — drop *.py into figures_src/)
FIGURE_SCRIPTS := $(wildcard figures_src/*.py)
# Sentinel file: figures are up to date when this exists
FIGURES_STAMP  := generated/.figures_stamp

.PHONY: deps check-deps figures values lint paper clean

# ---------------------------------------------------------------------------
# deps: install Python dependencies declared in requirements.txt
# ---------------------------------------------------------------------------
deps:
	$(PYTHON) -m pip install -r requirements.txt

# ---------------------------------------------------------------------------
# check-deps: fail fast with a helpful pointer if pandas/matplotlib missing
# ---------------------------------------------------------------------------
check-deps:
	@$(PYTHON) -c "import pandas, numpy" 2>/dev/null || { \
	    echo "ERROR: missing Python deps (pandas / numpy)." 1>&2; \
	    echo "       Run: make deps    (or: $(PYTHON) -m pip install -r requirements.txt)" 1>&2; \
	    exit 1; \
	}

# ---------------------------------------------------------------------------
# figures: run every figures_src/*.py → generated/figures/*.pdf + *.numbers.csv
# ---------------------------------------------------------------------------
figures: check-deps $(FIGURES_STAMP)

$(FIGURES_STAMP): $(FIGURE_SCRIPTS) $(wildcard data/*.csv)
	@mkdir -p generated/figures
	@for script in $(FIGURE_SCRIPTS); do \
	    echo "  Rendering $$script ..."; \
	    $(PYTHON) $$script --paper-dir $(PAPER_DIR) || exit 1; \
	done
	@touch $(FIGURES_STAMP)

# ---------------------------------------------------------------------------
# values: build_numbers.py → generated/values.tex + generated/provenance.txt
# ---------------------------------------------------------------------------
values: figures
	$(PYTHON) build_numbers.py --paper-dir $(PAPER_DIR)

# ---------------------------------------------------------------------------
# lint: the BIB GATE — bare-digit-not-in-citation check
# ---------------------------------------------------------------------------
lint:
	$(PYTHON) lint.py --paper-dir $(PAPER_DIR)

# ---------------------------------------------------------------------------
# paper: end-to-end build (requires latexmk)
# ---------------------------------------------------------------------------
paper: figures values lint
	latexmk -pdf -interaction=nonstopmode $(MAIN).tex

# ---------------------------------------------------------------------------
# clean: remove generated/ and latexmk byproducts
# ---------------------------------------------------------------------------
clean:
	rm -rf generated/
	latexmk -C $(MAIN).tex 2>/dev/null || true
	rm -f $(MAIN).bbl $(MAIN).run.xml
