"""Regenerate the city price summary, chart, and table in index.html.

Run from any directory: python scripts/update_city_medians.py
Only sale_price is converted to a number; identifiers stay as text.
The original dataset is read, never modified.
"""

import csv
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from html import escape
from pathlib import Path
import re
from statistics import median


ROOT = Path(__file__).resolve().parents[1]
MIN_SALE_PRICE = 1000


def main():
    prices_by_city = defaultdict(list)
    excluded = 0
    with (ROOT / "data/college_town_home_sales.csv").open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            price = int(row["sale_price"])
            if price < MIN_SALE_PRICE:
                excluded += 1
                continue
            prices_by_city[(row["city"], row["state"])].append(price)

    # Integer prices yield integer or half-dollar medians, both exactly representable.
    cities = [
        (city, state, Decimal(str(median(prices))), len(prices))
        for (city, state), prices in prices_by_city.items()
    ]
    cities.sort(key=lambda item: (-item[2], item[0], item[1]))
    maximum = max(item[2] for item in cities)

    def dollars(value):
        rounded = value.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        return f"${rounded:,.0f}"

    included = sum(item[3] for item in cities)
    summary = (
        f'      <p class="intro">Compare all {len(cities):,} cities in the dataset, '
        f'using {included:,} sales of ${MIN_SALE_PRICE:,} or more. '
        f'The chart and table show every city’s median, rounded to whole dollars.</p>\n'
        f'      <p class="note">{excluded:,} sales below ${MIN_SALE_PRICE:,} are excluded. '
        'Data collected March 2026.</p>'
    )
    chart = ['          <ol class="price-chart">']
    table = ["          <tbody>"]
    for city, state, value, count in cities:
        label = escape(f"{city}, {state}")
        formatted = dollars(value)
        width = value / maximum * 100
        chart.extend([
            '            <li class="chart-row">',
            f'              <span class="chart-label">{label}</span>',
            f'              <span class="bar-track" aria-hidden="true"><span class="bar" style="width: {width:.4f}%"></span></span>',
            f'              <span class="chart-value">{formatted}</span>',
            '            </li>',
        ])
        table.extend([
            "            <tr>",
            f'              <th scope="row">{label}</th>',
            f'              <td class="numeric">{formatted}</td>',
            f'              <td class="numeric">{count:,}</td>',
            "            </tr>",
        ])
    chart.extend([
        '          </ol>',
        f'          <div class="chart-axis" aria-hidden="true"><span>$0</span><span>{dollars(maximum)}</span></div>',
    ])
    table.append("          </tbody>")

    page_path = ROOT / "index.html"
    page = page_path.read_text(encoding="utf-8")
    for name, content in [("summary", summary), ("chart", "\n".join(chart)), ("table", "\n".join(table))]:
        pattern = rf"(<!-- BEGIN GENERATED {name} -->)\n.*?([ \t]*<!-- END GENERATED {name} -->)"
        page, replacements = re.subn(pattern, lambda match: f"{match[1]}\n{content}\n{match[2]}", page, flags=re.DOTALL)
        if replacements != 1:
            raise ValueError(f"Expected exactly one generated {name} section; found {replacements}")
    page_path.write_text(page, encoding="utf-8")
    print(f"Updated index.html: {len(cities)} cities, {included:,} eligible sales, {excluded} excluded.")


if __name__ == "__main__":
    main()
