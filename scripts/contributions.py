"""Generate the profile's contribution cards using only Python's standard library."""
import argparse
from collections import Counter
from datetime import datetime, timezone
from html import escape
import json
import os
from pathlib import Path
import re
import textwrap
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
START = "## Open-source contributions\n"
END = "## Highlighted projects"


def api(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "minh-profile-card",
               "X-GitHub-Api-Version": "2022-11-28"}
    if os.environ.get("GH_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GH_TOKEN"]
    with urlopen(Request("https://api.github.com/" + path, headers=headers), timeout=45) as response:
        return json.load(response)


def normalize(pr):
    return {"repo": pr["base"]["repo"]["full_name"], "number": pr["number"],
            "title": pr["title"], "url": pr["html_url"],
            "state": "merged" if pr.get("merged_at") else ("open" if pr["state"] == "open" else "closed"),
            "updated_at": pr["updated_at"], "merged_at": pr.get("merged_at")}


def fetch_contributions(config):
    query = "is:pr is:public author:" + config["username"]
    query += "".join(" -user:" + owner for owner in config["excluded_owners"])
    result = []
    for page in range(1, 11):
        data = api("search/issues?" + urlencode({"q": query, "per_page": 100, "page": page,
                                                "sort": "created", "order": "desc"}))
        if data.get("incomplete_results") or data["total_count"] > 1000:
            raise RuntimeError("Incomplete GitHub search; keeping the last successful card.")
        for item in data["items"]:
            result.append(normalize(api(item["pull_request"]["url"].removeprefix("https://api.github.com/"))))
        if len(result) >= data["total_count"]:
            break
    return {"updated_at": datetime.now(timezone.utc).date().isoformat(), "pull_requests": result}


def ordered(prs):
    return sorted(prs, key=lambda p: ({"merged": 0, "open": 1, "closed": 2}[p["state"]],
                                     -(datetime.fromisoformat((p.get("merged_at") or p["updated_at"]).replace("Z", "+00:00")).timestamp())))


def label(pr, config):
    return config["projects"].get(pr["repo"], pr["repo"].split("/")[-1])


def summary(pr, config):
    return config["summaries"].get(pr["url"], pr["title"])


def render_svg(data, config, theme="dark"):
    dark = theme == "dark"
    bg, panel, border = ("#0d111b", "#141c2b", "#263449") if dark else ("#f6f8fc", "#ffffff", "#d9e2ef")
    ink, muted, accent = ("#edf4ff", "#9aabc3", "#65dfcb") if dark else ("#18263c", "#586b85", "#087f73")
    purple = "#c0a0ff" if dark else "#7545c1"
    prs = data["pull_requests"]
    counts = Counter(p["state"] for p in prs)
    featured = [p for p in ordered(prs) if p["state"] != "closed"][:8]
    rows = max(1, (len(featured) + 1) // 2)
    height = 294 + rows * 150
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title desc">',
           '<title id="title">Minh Pham · Open-source contributions</title>',
           f'<desc id="desc">{counts["merged"]} merged PRs, {counts["open"]} open PRs, {counts["closed"]} closed without merge across {len(set(p["repo"] for p in prs))} projects. Full links and descriptions in the README.</desc>',
           f'<defs><linearGradient id="edge"><stop stop-color="{accent}"/><stop offset="1" stop-color="{purple}"/></linearGradient>',
           f'<radialGradient id="glow"><stop stop-color="{purple}" stop-opacity=".12"/><stop offset="1" stop-color="{bg}" stop-opacity="0"/></radialGradient></defs>',
           f'<rect x="1" y="1" width="958" height="{height-2}" rx="24" fill="{bg}" stroke="{border}"/>',
           '<rect x="28" y="26" width="4" height="39" rx="2" fill="url(#edge)"/>',
           '<ellipse cx="835" cy="80" rx="240" ry="180" fill="url(#glow)"/>',
           f'<g font-family="DejaVu Sans,Segoe UI,Arial,sans-serif" fill="{ink}">']

    def text(x, y, value, size=14, color=None, weight=None, extra=""):
        out.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color or ink}"'
                   + (f' font-weight="{weight}"' if weight else "") + f' {extra}>{escape(str(value))}</text>')

    text(46, 39, "BUILDING IN THE OPEN", 11, accent, 700, 'letter-spacing="2"')
    text(46, 68, "Open-source contributions", 26, weight=700)
    text(46, 97, "Geospatial computing · graphics · cloud infrastructure · scientific tools", 13, muted)
    text(914, 39, "@minhpham1810", 12, muted, extra='text-anchor="end"')
    metrics = [(counts["merged"], "MERGED PRs", purple), (counts["open"], "OPEN PRs", accent),
               (len(set(p["repo"] for p in prs)), "PROJECTS", ink), (len(prs), "TOTAL PRs", ink)]
    for i, (value, name, color) in enumerate(metrics):
        x = 28 + i * 230
        out.append(f'<rect x="{x}" y="120" width="214" height="79" rx="12" fill="{panel}" stroke="{border}"/>')
        text(x+18, 154, value, 29, color, 700)
        text(x+18, 181, name, 10, muted, 600, 'letter-spacing="1.2"')
    text(28, 230, "SELECTED CONTRIBUTIONS", 10, muted, 700, 'letter-spacing="1.8"')
    for i, pr in enumerate(featured):
        x, y = 28 + (i % 2) * 460, 248 + (i // 2) * 150
        color = purple if pr["state"] == "merged" else accent
        out.append(f'<rect x="{x}" y="{y}" width="444" height="134" rx="12" fill="{panel}" stroke="{border}"/>')
        out.append(f'<rect x="{x}" y="{y+17}" width="3" height="27" rx="1.5" fill="{color}"/>')
        text(x+18, y+28, textwrap.shorten(label(pr, config), width=28, placeholder="…"), 16, weight=700)
        out.append(f'<rect x="{x+354}" y="{y+13}" width="74" height="23" rx="11" fill="{color}" fill-opacity=".12"/>')
        text(x+391, y+29, pr["state"].upper(), 10, color, 700, 'text-anchor="middle"')
        lines = textwrap.wrap(summary(pr, config), width=51, max_lines=3, placeholder="…")
        for j, line in enumerate(lines):
            text(x+18, y+54+j*18, line, 12, muted)
        text(x+18, y+117, f'{pr["repo"]}  ·  #{pr["number"]}', 10, muted)
    if not featured:
        text(28, 285, "Upstream contributions will appear here automatically.", 16, muted)
    footer = height-24
    out.append(f'<path d="M28 {footer-22}H932" stroke="{border}"/>')
    text(28, footer, f'{counts["closed"]} closed without merge · full history linked below', 11, muted)
    text(932, footer, f'Updated {data["updated_at"]} UTC · refreshes daily', 11, muted, extra='text-anchor="end"')
    out.append("</g></svg>\n")
    return "".join(out)


def markdown_cell(value):
    return re.sub(r"\s+", " ", value).replace("|", "&#124;").replace("<", "&lt;").replace(">", "&gt;").replace("[", "&#91;").replace("]", "&#93;")


def section(data, config):
    lines = ['<!-- Generated by scripts/contributions.py. Edit scripts/contributions-config.json for display copy. -->',
             '<picture>',
             '  <source media="(prefers-color-scheme: dark)" srcset="assets/open-source-dark.svg">',
             '  <source media="(prefers-color-scheme: light)" srcset="assets/open-source-light.svg">',
             '  <img alt="Open-source contributions: merged and open pull requests across upstream projects" src="assets/open-source-dark.svg" width="960">',
             '</picture>', '', '<details>', '<summary>Explore contributions and pull requests</summary>', '']
    for state, heading in [("merged", "Merged"), ("open", "Open pull requests"), ("closed", "Closed proposals (not merged)")]:
        lines += [f"### {heading}", "", "| Project | Contribution | PR |", "| --- | --- | --- |"]
        for pr in ordered(data["pull_requests"]):
            if pr["state"] == state:
                lines.append(f'| **{markdown_cell(label(pr, config))}** | {markdown_cell(summary(pr, config))} | [#{pr["number"]}]({pr["url"]}) |')
        lines.append("")
    lines += ['</details>', '', f'*Updated {data["updated_at"]} UTC · refreshed daily with GitHub Actions. [All authored pull requests](https://github.com/pulls?q=is%3Apr+author%3A{config["username"]}).*', '']
    return "\n".join(lines)


def update_readme(readme, content):
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("Expected exactly one contributions section and projects section")
    start = readme.index(START) + len(START)
    end = readme.index(END, start)
    return readme[:start] + "\n" + content.rstrip() + "\n\n" + readme[end:]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="Render the last verified data without API access")
    args = parser.parse_args()
    config = json.loads((ROOT / "scripts/contributions-config.json").read_text())
    path = ROOT / "data/contributions.json"
    data = json.loads(path.read_text()) if args.offline else fetch_contributions(config)
    readme = ROOT / "README.md"
    new_readme = update_readme(readme.read_text(), section(data, config))
    cards = {theme: render_svg(data, config, theme) for theme in ("dark", "light")}
    # Finish all API requests and rendering before replacing a last-successful output.
    (ROOT / "assets").mkdir(exist_ok=True)
    for theme, svg in cards.items():
        (ROOT / f"assets/open-source-{theme}.svg").write_text(svg)
    path.write_text(json.dumps(data, indent=2) + "\n")
    readme.write_text(new_readme)
    print(f'Rendered {len(data["pull_requests"])} upstream PRs; updated {data["updated_at"]}')


if __name__ == "__main__":
    main()
