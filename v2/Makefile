# v2/Makefile — dissertation build system (ported from onlycodes/paper).
#
# Targets:
#   make deps     — install Python dependencies from requirements.txt
#   make figures  — render all figures_src/*.py scripts → generated/figures/
#   make values   — build_numbers.py: CSVs + sidecars → generated/values.tex
#   make lint      — BIB GATE (numbers): bare-digit-not-in-citation check on prose
#   make check-refs— BIB GATE (citations): undefined/duplicate/orphan reference check
#                    (add ONLINE=1 to also resolve arXiv/DOI titles; needs network)
#   make voice     — VOICE METER: prose-texture report vs Ch.4 (warning-only)
#   make voice-profile — (re)build the Ch.4 target profile (data/voice_profile_ch4.json)
#   make paper     — figures + values + lint + check-refs + latexmk -pdf main.tex
#   make clean     — remove generated/ and latexmk byproducts
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
SLIDES    = defense_slides
SLIDES_MACBOOK = defense_slides_macbook

# All figure renderer scripts (none yet — drop *.py into figures_src/)
FIGURE_SCRIPTS := $(wildcard figures_src/*.py)
# Sentinel file: figures are up to date when this exists
FIGURES_STAMP  := generated/.figures_stamp

.PHONY: deps check-deps figures values lint check-refs voice voice-profile paper slides slides-macbook clean

# ONLINE=1 makes check-refs resolve arXiv/DOI titles (needs network)
CHECKREFS_FLAGS := $(if $(ONLINE),--online,)

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
# check-refs: the CITATION half of the bib gate — undefined / duplicate /
# orphaned references (ONLINE=1 also resolves arXiv/DOI titles). stdlib only.
# ---------------------------------------------------------------------------
check-refs:
	$(PYTHON) check_refs.py --paper-dir $(PAPER_DIR) $(CHECKREFS_FLAGS)

# ---------------------------------------------------------------------------
# voice: the VOICE METER — prose-texture report (burstiness, tricolons,
# cross-chapter n-gram repetition) vs the Ch.4 human exemplar. Warning-only by
# default; deliberately NOT in `paper` until the framing chapters pass. Run
# `make voice-profile` once to (re)build data/voice_profile_ch4.json, then
# `make voice` to report, or `$(PYTHON) voice_meter.py --gate` to fail on a
# gateable issue. See outlines/style_guide.md §6.
# ---------------------------------------------------------------------------
voice:
	$(PYTHON) voice_meter.py --paper-dir $(PAPER_DIR)

voice-profile:
	$(PYTHON) voice_meter.py --paper-dir $(PAPER_DIR) --profile chapters/04_label_blindness.tex

# ---------------------------------------------------------------------------
# paper: end-to-end build (requires latexmk)
# ---------------------------------------------------------------------------
paper: figures values lint check-refs
	latexmk -pdf -interaction=nonstopmode $(MAIN).tex

# ---------------------------------------------------------------------------
# slides: dissertation-defense Beamer deck. Reuses generated figures/values but
# is intentionally outside the dissertation prose lint gate.
# ---------------------------------------------------------------------------
slides: figures values
	latexmk -pdf -interaction=nonstopmode $(SLIDES).tex

# 16:10 rendering for MacBook displays. The wrapper inputs the same slide source.
slides-macbook: figures values
	latexmk -pdf -interaction=nonstopmode $(SLIDES_MACBOOK).tex

# ---------------------------------------------------------------------------
# clean: remove generated/ and latexmk byproducts
# ---------------------------------------------------------------------------
clean:
	rm -rf generated/
	latexmk -C $(MAIN).tex 2>/dev/null || true
	latexmk -C $(SLIDES).tex 2>/dev/null || true
	latexmk -C $(SLIDES_MACBOOK).tex 2>/dev/null || true
	rm -f $(MAIN).bbl $(MAIN).run.xml
	rm -f $(SLIDES).bbl $(SLIDES).run.xml
	rm -f $(SLIDES_MACBOOK).bbl $(SLIDES_MACBOOK).run.xml
