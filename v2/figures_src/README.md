# figures_src/

One Python script per figure. Each script:

- accepts `--paper-dir <path>` (the v2/ directory),
- writes its figure to `generated/figures/<name>.pdf` (and `.png`),
- writes a `generated/figures/<name>.numbers.csv` **sidecar** with `label,value`
  rows for every number it draws, so those numbers are reachable from prose via
  `\result{fig.<name>}{<label>}`.

`make figures` runs every `*.py` here. See `../README.md` for the full contract
and `hyang0129/onlycodes/paper/figures_src/` for worked examples.
