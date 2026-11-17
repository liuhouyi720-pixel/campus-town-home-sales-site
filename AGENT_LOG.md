# Agent log

Add a dated entry each time you work with your AI coding agent, with the newest entry at the bottom. Each entry records what you asked the agent, what it produced, and what you checked or changed. Paste your key prompts in exactly as you typed them. Include at least one time the agent got something wrong, and how you caught it.

Copy this outline for each entry:

```markdown
## YYYY-MM-DD: What you worked on

- **Asked:** "Paste your prompt here."
- **Agent produced:** What it made or changed.
- **Checked or changed:** How you checked it, and what you fixed.
```

## 2026-11-17: Show all city median sale prices

- **Asked:** " read `AGENTS.md` and `docs/data_description_sheet.md` first.  Then show every median sales price on index.html, rounded to whole dollar, in both chart and table"
- **Agent produced:** Replaced the placeholder with a responsive bar chart and table for all 18 cities. Every median displays as whole US dollars with comma separators. Added eligible sale counts, the $1,000 minimum rule, rounding notes, and a reproducible Python script in `scripts/`.
- **Checked or changed:** Every chart price, table price, and count matched an independent query of the read-only SQLite dataset. Confirmed 35,438 eligible sales and 4 exclusions, including Pittsboro's $876,985.50 median rounding up to $876,986. Checked Chromium layouts at 320, 375, 768, 1100, and 1440 pixels, relative links, browser errors, and repeatable generation. The first browser check incorrectly assumed file URLs were allowed; Chromium blocked them, so the check was corrected to use a temporary local HTTP server. Dataset files and the publishing workflow were unchanged.

## 2026-11-17: Publish the chart update

- **Asked:** "push the chart update to `main`  "
- **Agent produced:** Pulled remote `main`, confirmed it still contained the initial placeholder, and restored the saved chart-and-table update for publication. Placed the chart above the table on all screen sizes. Both views show whole-dollar median prices.
- **Checked or changed:** Rechecked all 18 medians and eligible counts against the read-only SQLite dataset, confirmed chart/table order and whole-dollar formatting in Chromium, and checked that only the site, its generation script, and documentation changed. The earlier assumption that remote `main` already contained another chart was disproved by pulling and inspecting its initial commit. The original dataset files and publishing workflow were preserved.
