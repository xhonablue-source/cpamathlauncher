# Deploying the daily lesson apps

The launcher (`app.py`) is one Streamlit deployment. Each **daily lesson** is a separate Streamlit deployment that lives in this same repo as its own file. That is why the launcher links out to `https://cpamath6dayNN.streamlit.app/` instead of using Streamlit multipage navigation — the day apps were built to open in a new tab, on a projector, without the launcher chrome around them.

## Files

| Day | File | Expected URL |
|-----|------|--------------|
| 5 | `day5_lesson_app.py` | https://cpamath6day5.streamlit.app/ |
| 13 | `day13_lesson_app.py` | https://cpamath6day13.streamlit.app/ |
| 14 | `day14_lesson_app.py` | https://cpamath6day14.streamlit.app/ |
| 15 | `day15_lesson_app.py` | https://cpamath6day15.streamlit.app/ |

## To deploy one day

1. share.streamlit.io → **New app** → **Deploy a public app from GitHub**
2. Repository: `xhonablue-source/cpamathlauncher`
3. Branch: `main`
4. **Main file path**: the day's file, e.g. `day13_lesson_app.py`
5. **Custom subdomain**: `cpamath6day13` — this is what makes the URL match the launcher link, so set it before you click Deploy.
6. Deploy. First build takes a couple of minutes while matplotlib installs.

Repeat for each day. All of them share this repo's `requirements.txt`.

## After deploying

Open the launcher, click the day's **Open Lesson** button, and confirm it lands on the lesson rather than a 404. The URLs are listed in the `DAYS` list near the top of `app.py` if a subdomain has to change.

## Classroom notes

- Every lesson app is standalone: no `_common.py`, no imports from `app.py`. A day can be deployed, rolled back, or edited without touching the launcher.
- Each app holds student input in `st.session_state` only. Nothing is written to disk and nothing leaves the browser session, so there is no student data to manage and no FERPA surface.
- The sidebar roadmap doubles as the pacing guide — the timestamps on each slide add up to a 55-minute period.
