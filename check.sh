#!/usr/bin/env bash
# run the whole thing top to bottom so i can check nothing broke after edits.
set -e

cd "$(dirname "$0")/src"
for step in harmonize calibrate index validate robustness make_table plot; do
  echo "### $step"
  python3 "$step.py"
  echo
done

cd ..
echo "### tests"
python3 tests/test_parse.py
python3 tests/test_grain.py

echo "### paper"
cd paper/icdm
python3 make_fig.py
python3 to_tex.py
python3 to_docx.py
echo "all good"
