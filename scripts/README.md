# Scripts

`update_city_medians.py` reads the original CSV and regenerates the summary,
bar chart, and table in `index.html`. Run `python scripts/update_city_medians.py`
from the repository root. It uses only Python's standard library. All 18 city/state
groups are included; sales below $1,000 are excluded, and half-dollar medians
round up. Commit the regenerated `index.html` with the script. The published page
is plain HTML and needs no build step or JavaScript.

Scripts that make data files for the site go here. An example is a script that writes a small JSON summary from `data/college_town_home_sales.csv`, so the site doesn't have to load the full 9 MB file.

If the site reads a file that a script made, commit both the script and the file it makes. Say in the main README how to run the script, so anyone can rerun it and get the same file.

Unless you switch to a framework that needs a build step (and update `.github/workflows/pages.yml` to match), the site must work as committed: GitHub Pages publishes the files as they are.
