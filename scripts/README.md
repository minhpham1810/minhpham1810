# Contribution cards

The daily workflow discovers public pull requests authored by minhpham1810,
fetches authoritative merge states, and generates light/dark SVGs plus the
collapsible contribution history. No personal access token or external hosting
is needed: the workflow uses its built-in GitHub token.

Run locally with Python 3.12:

```sh
python -m unittest discover -s scripts -v
GH_TOKEN=your-token python scripts/contributions.py
# Re-render a verified snapshot without network access:
python scripts/contributions.py --offline
```

Edit contributions-config.json to adjust project labels, contribution summaries,
or excluded owners. Campus work already covered under Highlighted projects is
excluded from this upstream card. New projects are included automatically, with
their PR titles used until a custom summary is added.

The card features up to eight merged/open contributions, ordered by status and
recency; all matching public PRs remain in the counts and expandable history.
Closed PRs are never counted as merged. Failed or incomplete API responses fail
the workflow and leave the last successfully committed card in place.

GitHub caches README images, so updates may take a little time to appear.
Public repositories may have scheduled workflows disabled by GitHub after
60 days without repository activity; a manual workflow run can re-enable them.
