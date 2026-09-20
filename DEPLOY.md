# Deploying the daily lesson apps

One repo per day. This repo holds **only the launcher** (`app.py`) — the thing
that runs at cpamath.org. Every daily lesson is its own GitHub repo, its own
Streamlit deployment, and its own subdomain.

```
xhonablue-source/cpamathlauncher   → cpamath.org            (this repo, launcher only)
xhonablue-source/cpamath6day5      → cpamath6day5.streamlit.app
xhonablue-source/cpamath6day6      → cpamath6day6.streamlit.app
xhonablue-source/cpamath6day13     → cpamath6day13.streamlit.app
...
```

The launcher links out to `https://cpamath6dayNN.streamlit.app/` rather than
using Streamlit multipage navigation, because the day apps are built to open in
a new tab, on a projector, without the launcher chrome around them.

> **If you see a `dayNN_lesson_app.py` file sitting in this repo, it is a stray
> copy, not the deployed app.** `day5_lesson_app.py` and `day13_lesson_app.py`
> were both checked in here by mistake. The live Day 5 lesson is the repo
> `cpamath6day5`. Deleting the stray files from this repo breaks nothing.

## The naming rule

The repo name, the Streamlit subdomain, and the URL in the launcher's `DAYS`
list are **the same string**: `cpamath6dayNN`. Nothing reconciles them
automatically — if they don't match by hand, the card 404s.

A repo named off-pattern will never appear on cpamath.org. The repos `ratios`
and `percents` are examples: they exist, they may even deploy, but no launcher
card can point at them until they are rehomed as `cpamath6dayNN`.

## Each day's repo contains exactly four files

| File | Contents |
|---|---|
| `app.py` | The whole lesson. Standalone — no `_common.py`, no imports from the launcher. |
| `requirements.txt` | `streamlit>=1.32` and `matplotlib>=3.7` |
| `README.md` | Day number, title, and the deployed URL |
| `LICENSE` | MIT |

`cpamath6day10` is the reference shape. Match it.

## The three steps

### 1. Make the repo

github.com/new → Owner `xhonablue-source` → Repository name **`cpamath6dayNN`**
→ Public → *no* README/.gitignore/license (the four files supply them) → Create.

On the empty repo, **uploading an existing file** → drag in all four files →
Commit directly to `main`. Do not paste `app.py` into the web editor. It is a
1,000+ line file and the browser editor silently drops keystrokes at that size;
the upload path does not.

### 2. Deploy it

share.streamlit.io → **New app** → **Deploy a public app from GitHub**

- Repository: `xhonablue-source/cpamath6dayNN`
- Branch: `main`
- Main file path: `app.py`
- **Custom subdomain: `cpamath6dayNN`** — set this *before* clicking Deploy.
  It is what makes the URL match the launcher link, and changing it afterwards
  means redeploying.

First build takes a couple of minutes while matplotlib installs.

Open the app once before moving on. A lesson that builds but throws on slide 1
looks identical to a working one from the launcher.

### 3. Add the card to the launcher

Only now edit `app.py` in *this* repo. Find the day's entry in the `DAYS` list
and add the `page` key:

```python
dict(
    label="Day 13",
    title="Area of a Triangle",
    desc="...",
    page="https://cpamath6day13.streamlit.app/",   # ← this line
    guide_file="Day13_Observer_Guide.pdf",
    ...
),
```

A card with no `page` key still renders — it just shows no **Open Lesson**
button. That is the intended state for a day whose app isn't deployed yet, and
it is why review days (11, 12, 16) and enrichment days (17) have no `page`:
they are worksheet-only by design, not missing.

For a brand-new day, append a new `dict(...)` to the end of `DAYS`. Cards render
in list order, so the list stays in day order.

Commit, and Streamlit redeploys the launcher within a minute.

## Verifying

From cpamath.org, click the day's **Open Lesson** button and confirm it lands on
the lesson rather than a 404. If it 404s, the subdomain and the `page` URL
disagree — the Streamlit app's settings are the thing to fix, not the launcher.

## Classroom notes

- Every lesson app is standalone. A day can be deployed, rolled back, or edited
  without touching the launcher or any other day.
- Each app holds student input in `st.session_state` only. Nothing is written to
  disk and nothing leaves the browser session, so there is no student data to
  manage and no FERPA surface.
- The sidebar roadmap doubles as the pacing guide — the timestamps on each slide
  add up to a 55-minute period.
