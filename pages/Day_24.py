"""
Math 6 — Day 24: Equivalent Ratios on the Coordinate Plane
Same structure as the Day 22 and Day 23 apps, by Xavier Honablue, M.Ed.

Aligned to i-Ready Classroom Mathematics, Grade 6, Unit 3 (Ratio Reasoning):
Lesson 13, Session 3 — Develop: Equivalent Ratios as Points in the Coordinate Plane.
Every pair in a ratio table is an ordered pair. Equivalent ratios land on one straight
line through (0, 0); a pair made by ADDING lands off the line.

Run locally with:  streamlit run app.py
"""
PAGE_TITLE = "Day 24 — Equivalent Ratios on the Coordinate Plane"
PAGE_ICON = "📈"
DAY_LABEL = "Day 24"
ROADMAP_SUB = ("55-minute period — Find Equivalent Ratios, Session 3 "
               "(Develop: Equivalent Ratios on the Coordinate Plane)")
STEPS = [
    "1. Welcome Back",
    "2. Warm-Up: Which One Doesn't Belong?",
    "3. Try It: Maya's Smoothies",
    "4. Model It: Table → Ordered Pairs",
    "5. Model It: Read the Graph",
    "6. Error Alert: Off the Line",
    "7. Real Life: Two Lines, One Graph",
    "8. Project: Graph Lab",
    "9. Practice, Stations & Exit Ticket",
]
DEFAULT_NOTES = [{
    "date": "Day 23",
    "note": "Mixed-number multipliers landed once students saw 2½ groups as 2 groups plus half a "
            "group. Devon's 8½ error came up on its own in two classes. Graphs were only "
            "previewed in the Explore station — today makes the coordinate plane the main event.",
}]
STANDARDS_CAPTION = ("Standards in play: 6.RP.A.3 (use ratio reasoning to solve problems) · "
                     "6.RP.A.3a (tables of equivalent ratios; plot the pairs on the coordinate "
                     "plane) · 6.NS.C.8 (graph points in the coordinate plane).")

import json
import os
from datetime import datetime
from fractions import Fraction

import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

NAVY = "#1b3a5c"
NAVY_LIGHT = "#eef4fa"
NAVY_BORDER = "#2c4a6e"
GREEN = "#3f7d55"
GREEN_LIGHT = "#eef7f0"
GOLD = "#8a5a20"
GOLD_LIGHT = "#f6ecd9"
RED = "#b03a2e"
RED_LIGHT = "#fdf1ef"
PLUM = "#6b3fa0"
PLUM_LIGHT = "#f4effa"
TEAL = "#1f6f78"
TEAL_LIGHT = "#e8f5f6"

CUSTOM_CSS = f"""
<style>
.box {{
    border: 2px solid {NAVY};
    border-radius: 8px;
    padding: 14px 18px;
    margin: 10px 0;
    background: white;
}}
.pill {{
    display: inline-block;
    color: white;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.4px;
    padding: 4px 12px;
    border-radius: 12px;
    margin-bottom: 8px;
}}
.box-readaloud {{ border-color: {NAVY}; }}
.box-readaloud .pill {{ background: {NAVY}; }}
.box-readaloud p {{ font-style: italic; margin: 4px 0 0 0; }}
.box-literacy {{ border-color: {NAVY_BORDER}; background: {NAVY_LIGHT}; }}
.box-literacy .pill {{ background: {NAVY_BORDER}; }}
.box-existing {{ border-color: {GREEN}; background: {GREEN_LIGHT}; }}
.box-existing .pill {{ background: {GREEN}; }}
.box-tools {{ border-color: {GOLD}; background: {GOLD_LIGHT}; }}
.box-tools .pill {{ background: {GOLD}; }}
.box-observer {{ border: 2px dashed {RED}; background: {RED_LIGHT}; }}
.box-observer .pill {{ background: {RED}; }}
.box-slides {{ border-color: {PLUM}; background: {PLUM_LIGHT}; }}
.box-slides .pill {{ background: {PLUM}; }}
.box-iready {{ border-color: {TEAL}; background: {TEAL_LIGHT}; }}
.box-iready .pill {{ background: {TEAL}; }}
.ask {{ color: {RED}; font-weight: 700; margin-top: 8px; }}
.roadmap-title {{ color: {NAVY}; font-weight: 700; font-size: 15px; margin-bottom: 0; }}
.roadmap-sub {{ color: #5a6672; font-size: 11.5px; margin-top: -4px; }}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def html_widget(html, height):
    """Interactive HTML (timers). st.iframe on current Streamlit; components.html on older."""
    if hasattr(st, "iframe"):
        st.iframe(html, height=height)
    else:
        import streamlit.components.v1 as components
        components.html(html, height=height)


def box(kind, pill, body_html):
    st.markdown(
        f'<div class="box box-{kind}"><span class="pill">{pill}</span>{body_html}</div>',
        unsafe_allow_html=True,
    )


def read_aloud(text):
    box("readaloud", "🔊 READ ALOUD", f"<p>&ldquo;{text}&rdquo;</p>")


def ask_the_class(text):
    st.markdown(f'<p class="ask">❓ Ask the class: {text}</p>', unsafe_allow_html=True)


def slides_ref(text):
    box("slides", "📊 i-READY TEACHER TOOLBOX", text)


# ----------------------------------------------------------------------
# Observer notes — a running teacher log, persisted to a local JSON file
# ----------------------------------------------------------------------
NOTES_FILE = os.path.join(os.path.dirname(__file__), "observer_notes_day24.json")


def load_notes():
    if os.path.exists(NOTES_FILE):
        try:
            with open(NOTES_FILE) as f:
                return json.load(f)
        except Exception:
            return list(DEFAULT_NOTES)
    return list(DEFAULT_NOTES)


def save_notes(notes):
    try:
        with open(NOTES_FILE, "w") as f:
            json.dump(notes, f, indent=2)
    except Exception:
        pass  # read-only filesystem — notes still live for this session


if "observer_notes_d24" not in st.session_state:
    st.session_state.observer_notes_d24 = load_notes()


def observer_log():
    st.markdown("---")
    st.markdown("#### 🔎 Observer Notes (running log)")
    st.caption("A running teacher log carried day to day. Add what you noticed in class today, "
               "then Save — copy it into tomorrow's app to keep the thread going.")
    for n in st.session_state.observer_notes_d24:
        st.markdown(f"**{n['date']}:** {n['note']}")
    new_note = st.text_area("Add a new observation:", key="new_observer_note")
    if st.button("Save observation"):
        if new_note.strip():
            st.session_state.observer_notes_d24.append(
                {"date": f"{DAY_LABEL} — {datetime.now().strftime('%Y-%m-%d')}",
                 "note": new_note.strip()})
            save_notes(st.session_state.observer_notes_d24)
            st.success("Saved to the observer log.")
            st.rerun()
        else:
            st.warning("Write a note first.")


# ----------------------------------------------------------------------
# Fraction / ratio helpers
# ----------------------------------------------------------------------
def mixed(x):
    """Plain-text mixed number: Fraction(5, 2) -> '2 1/2'."""
    x = Fraction(x)
    if x.denominator == 1:
        return str(x.numerator)
    sign = "-" if x < 0 else ""
    x = abs(x)
    whole, rem = divmod(x.numerator, x.denominator)
    if whole == 0:
        return f"{sign}{rem}/{x.denominator}"
    return f"{sign}{whole} {rem}/{x.denominator}"


def tex(x):
    x = Fraction(x)
    if x.denominator == 1:
        return str(x.numerator)
    whole, rem = divmod(abs(x.numerator), x.denominator)
    sign = "-" if x < 0 else ""
    frac = rf"\tfrac{{{rem}}}{{{x.denominator}}}"
    return f"{sign}{whole}{frac}" if whole else f"{sign}{frac}"


def m(x):
    return f"${tex(x)}$"


def parse_mixed(text):
    """Parse '2 1/4', '9/4', '2.25', or '3' into a Fraction. Returns None if unreadable."""
    t = (text or "").strip().replace("½", " 1/2").replace("¼", " 1/4").replace("¾", " 3/4")
    t = t.replace("$", "").replace(",", "")
    if not t:
        return None
    try:
        parts = t.split()
        if len(parts) == 2:
            whole = Fraction(parts[0])
            frac = Fraction(parts[1])
            return whole + frac if whole >= 0 else whole - frac
        return Fraction(parts[0])
    except (ValueError, ZeroDivisionError):
        return None


def equivalent(r1, r2):
    return Fraction(r1[0]) * Fraction(r2[1]) == Fraction(r1[1]) * Fraction(r2[0])


def check_answer(label, answer, key, hint, success=None):
    """Text box + instant feedback for a numeric answer (accepts fractions / mixed numbers)."""
    r = st.text_input(label, key=key, placeholder="Type a whole number, fraction, or mixed number")
    if r:
        v = parse_mixed(r)
        if v is not None and v == Fraction(answer):
            st.success(success or f"Correct — {m(answer)}.")
            return True
        st.error(hint)
    return False


def draw_double_number_line(pairs, label_a, label_b, highlight=None, figsize=(8.6, 2.4)):
    pairs = sorted({(Fraction(a), Fraction(b)) for a, b in pairs})
    top = max(a for a, _ in pairs)
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot([0, 1], [1.35, 1.35], color=NAVY, linewidth=2)
    ax.plot([0, 1], [0.45, 0.45], color=GOLD, linewidth=2)
    for a, b in [(Fraction(0), Fraction(0))] + pairs:
        x = float(a / top)
        hot = highlight is not None and a == Fraction(highlight)
        col_a = RED if hot else NAVY
        col_b = RED if hot else GOLD
        ax.plot([x, x], [1.25, 1.45], color=col_a, linewidth=2.6 if hot else 2)
        ax.plot([x, x], [0.35, 0.55], color=col_b, linewidth=2.6 if hot else 2)
        ax.text(x, 1.62, mixed(a), ha="center", va="bottom", fontsize=10, color=col_a,
                fontweight="bold" if hot else "normal")
        ax.text(x, 0.22, mixed(b), ha="center", va="top", fontsize=10, color=col_b,
                fontweight="bold" if hot else "normal")
    ax.text(-0.03, 1.35, label_a, ha="right", va="center", fontsize=10, color=NAVY, fontweight="bold")
    ax.text(-0.03, 0.45, label_b, ha="right", va="center", fontsize=10, color=GOLD, fontweight="bold")
    ax.set_xlim(-0.32, 1.04)
    ax.set_ylim(-0.1, 1.95)
    ax.axis("off")
    return fig


def draw_ratio_graph(series, x_label, y_label, xmax=None, ymax=None, line=True,
                     highlight=None, figsize=(6.2, 4.6)):
    """series: list of (name, color, [(x, y), ...]). Plots points (and a ray through the
    origin when line=True and the points are proportional)."""
    fig, ax = plt.subplots(figsize=figsize)
    all_x = [float(x) for _, _, pts in series for x, _ in pts]
    all_y = [float(y) for _, _, pts in series for _, y in pts]
    xmax = xmax or (max(all_x) * 1.15 if all_x else 10)
    ymax = ymax or (max(all_y) * 1.15 if all_y else 10)
    for name, color, pts in series:
        xs = [float(x) for x, _ in pts]
        ys = [float(y) for _, y in pts]
        ax.scatter(xs, ys, s=55, color=color, zorder=3, label=name)
        if line and pts:
            x0, y0 = pts[0]
            if all(equivalent((x0, y0), p) for p in pts) and float(x0) != 0:
                slope = float(Fraction(y0) / Fraction(x0))
                ax.plot([0, xmax], [0, slope * xmax], color=color, linewidth=1.4,
                        linestyle="--", alpha=0.8)
            else:
                ax.plot(xs, ys, color=color, linewidth=1.2, alpha=0.6)
        for x, y in pts:
            ax.annotate(f"({mixed(x)}, {mixed(y)})", (float(x), float(y)),
                        textcoords="offset points", xytext=(6, -12), fontsize=8, color=color)
    if highlight is not None:
        ax.scatter([float(highlight[0])], [float(highlight[1])], s=160, facecolors="none",
                   edgecolors=RED, linewidths=2.2, zorder=4)
    ax.scatter([0], [0], s=40, color="black", zorder=3)
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, ymax)
    ax.set_xlabel(x_label, fontsize=10, color=NAVY, fontweight="bold")
    ax.set_ylabel(y_label, fontsize=10, color=GOLD, fontweight="bold")
    ax.grid(True, alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    if len(series) > 1:
        ax.legend(fontsize=9, loc="upper left")
    fig.tight_layout()
    return fig


def ratio_table(rows, headers):
    st.table([dict(zip(headers, r)) for r in rows])


# ----------------------------------------------------------------------
# i-Ready online lesson block (Wed / Thu corroborating lessons)
# ----------------------------------------------------------------------
def countdown(minutes, key):
    html_widget(
        f"""
        <div style="font-family:Arial;text-align:center;padding:10px;border:3px solid {TEAL};
                    border-radius:12px;background:{TEAL_LIGHT}">
          <div style="font-size:13px;color:{TEAL};font-weight:700;letter-spacing:1px">
            i-READY ONLINE LESSON TIMER</div>
          <div id="t_{key}" style="font-size:58px;font-weight:800;color:{NAVY}">{minutes:02d}:00</div>
          <button id="s_{key}" style="font-size:16px;padding:6px 18px;margin:4px;border-radius:8px;
                  border:none;background:{TEAL};color:white;cursor:pointer">▶ Start</button>
          <button id="p_{key}" style="font-size:16px;padding:6px 18px;margin:4px;border-radius:8px;
                  border:none;background:{GOLD};color:white;cursor:pointer">⏸ Pause</button>
          <button id="r_{key}" style="font-size:16px;padding:6px 18px;margin:4px;border-radius:8px;
                  border:none;background:#777;color:white;cursor:pointer">↺ Reset</button>
        </div>
        <script>
          let left = {minutes} * 60, timer = null;
          const el = document.getElementById("t_{key}");
          const show = () => {{
            const mm = String(Math.floor(left / 60)).padStart(2, "0");
            const ss = String(left % 60).padStart(2, "0");
            el.textContent = mm + ":" + ss;
            el.style.color = left <= 300 ? "{RED}" : "{NAVY}";
            if (left === 0) el.textContent = "TIME — log your score!";
          }};
          document.getElementById("s_{key}").onclick = () => {{
            if (timer) return;
            timer = setInterval(() => {{ if (left > 0) {{ left--; show(); }}
                                         else {{ clearInterval(timer); timer = null; }} }}, 1000);
          }};
          document.getElementById("p_{key}").onclick = () => {{ clearInterval(timer); timer = null; }};
          document.getElementById("r_{key}").onclick = () => {{
            clearInterval(timer); timer = null; left = {minutes} * 60; show(); }};
        </script>
        """,
        height=190,
    )


def iready_block(key, lesson_focus, look_fors, small_group):
    """The 30-minute i-Ready corroborating-lesson block built into the Wed/Thu lessons."""
    box("iready", "💻 i-READY ONLINE LESSON · 30 MIN",
        f"<b>Today's assigned lesson focus:</b> {lesson_focus}<br>"
        "<b>Goal:</b> finish the lesson and <b>pass</b> the quiz at the end "
        "(i-Ready shows the score). Pass early? Keep going in <b>My Path</b>.")
    c1, c2 = st.columns([1.1, 1])
    with c1:
        countdown(30, key)
        st.link_button("🔗 Open i-Ready (sign in with Clever)", "https://login.i-ready.com/",
                       width="stretch")
    with c2:
        box("tools", "STUDENT CHECKLIST",
            "1. Headphones on. Sign in to i-Ready through Clever.<br>"
            "2. Open <b>My Assignments</b> first — the teacher-assigned lesson is on top.<br>"
            "3. Notebook out: copy every ratio table or double number line the lesson shows.<br>"
            "4. When the quiz ends, write your score in the log below.<br>"
            "5. Passed? Continue in <b>My Path</b> until the timer ends.")
    box("existing", "LOOK-FORS — HOW THE ONLINE LESSON MATCHES TODAY", look_fors)
    box("observer", "👩🏾‍🏫 TEACHER DURING THE BLOCK — SMALL GROUP", small_group)

    st.markdown("##### 📋 i-Ready score log (this browser session only)")
    log_key = f"{key}_log"
    if log_key not in st.session_state:
        st.session_state[log_key] = []
    with st.form(f"{key}_form", clear_on_submit=True):
        c1, c2, c3 = st.columns([1.3, 1, 1])
        who = c1.text_input("Student (first name + last initial)")
        score = c2.number_input("Quiz score (%)", min_value=0, max_value=100, step=5, value=0)
        passed = c3.selectbox("Passed?", ["Yes", "Not yet"])
        if st.form_submit_button("Log it"):
            if who.strip():
                st.session_state[log_key].append(
                    {"Student": who.strip(), "Score": f"{score}%", "Passed": passed})
            else:
                st.warning("Type a name first.")
    if st.session_state[log_key]:
        st.table(st.session_state[log_key])
        n_pass = sum(1 for r in st.session_state[log_key] if r["Passed"] == "Yes")
        st.caption(f"{n_pass} of {len(st.session_state[log_key])} logged students passed. "
                   "Students marked 'Not yet' are tomorrow's first small group.")
    else:
        st.caption("No scores logged yet. Nothing is saved after the tab closes — copy the "
                   "list into your gradebook before you leave.")


# ----------------------------------------------------------------------
# Sidebar — Sign In + Roadmap
# ----------------------------------------------------------------------
with st.sidebar:
    st.subheader("Sign In")
    st.text_input("Your name:", key="student_name")
    st.selectbox("Choose your shape avatar:",
                 ["Rectangle", "Square", "Triangle", "Circle", "Hexagon"], key="avatar")
    st.selectbox("Pick your learning mode:",
                 ["Focus Champ", "Growth Mode", "Problem Solver", "Data Boss", "Brain Builder"],
                 key="learning_mode")
    st.markdown("---")
    st.markdown(f'<p class="roadmap-title">{DAY_LABEL} Roadmap</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="roadmap-sub">{ROADMAP_SUB}</p>', unsafe_allow_html=True)
    if "step_d24" not in st.session_state:
        st.session_state.step_d24 = 0
    for i, label in enumerate(STEPS):
        marker = "▶ " if i == st.session_state.step_d24 else ""
        if st.button(marker + label, key=f"nav_{i}", width="stretch"):
            st.session_state.step_d24 = i
            st.rerun()

step = st.session_state.step_d24
name = st.session_state.get("student_name", "") or "class"
st.markdown(f"## {STEPS[step]}")
st.progress((step + 1) / len(STEPS))


if step == 0:
    box("observer", "🔎 OBSERVER NOTE — carried from Day 23",
        f"<p style='margin:0'>{st.session_state.observer_notes_d24[0]['note']}</p>")
    read_aloud(
        "So far you have shown equivalent ratios three ways: equal groups, a double number line, "
        "and a ratio table. Today is the fourth way, and it is the one scientists and business "
        "owners use most — a graph. Every row of a ratio table is secretly a point. When the "
        "ratios are equivalent, the points do something beautiful: they line up perfectly, and "
        "the line runs straight back to zero."
    )
    box("tools", "Today's tools",
        "Grid paper (first quadrant, 0–20) &middot; two colored pencils &middot; rulers &middot; "
        "yesterday's ratio tables &middot; journal &middot; exit ticket.")
    box("literacy", "LEARNING TARGETS",
        "I can write the pairs in a ratio table as ordered pairs <b>(x, y)</b>.<br>"
        "I can plot equivalent ratios and explain why they fall on a straight line through "
        "<b>(0, 0)</b>.<br>"
        "I can use a graph to find a missing value and to test whether two ratios are equivalent.")
    slides_ref("Grade 6 &rsaquo; Unit 3 &rsaquo; Lesson 13 &rsaquo; <b>Session 3</b> slides: "
               "Try It, Model It (plotting a ratio table), Discuss It. Project them next to "
               "this app during steps 3–5.")
    ask_the_class("If you plotted 0 cups of strawberries and 0 cups of yogurt, where would that "
                  "point be? Does it belong with the others?")

elif step == 1:
    st.write("**Purpose:** Retrieve equivalence from Days 21–23 before it goes on a graph.")
    st.markdown("##### Which one doesn't belong?")
    tables = {
        "A": [(2, 3), (4, 6), (6, 9)],
        "B": [(1, 5), (2, 10), (5, 25)],
        "C": [(3, 4), (5, 6), (7, 8)],
        "D": [(4, 1), (8, 2), (20, 5)],
    }
    cols = st.columns(4)
    for col, (k, rows) in zip(cols, tables.items()):
        with col:
            st.markdown(f"**Table {k}**")
            st.table([{"x": a, "y": b} for a, b in rows])
    pick = st.radio("Which table doesn't belong?", list(tables), index=None, horizontal=True,
                    key="d24_wodb")
    if st.button("Check", key="d24_wodb_chk"):
        if pick == "C":
            st.success("Table C. 3 : 4 → 5 : 6 → 7 : 8 adds 2 each time. The others multiply "
                       "both quantities by the same number, so every row is equivalent.")
        elif pick:
            st.error(f"Look again at Table {pick}: what number multiplies the first row into the "
                     "second? Now try Table C.")
        else:
            st.warning("Pick a table first.")
    ask_the_class("Could someone argue a different table doesn't belong? (Table D is the only one "
                  "where y is smaller than x.)")

elif step == 2:
    box("literacy", "CONNECT TO CULTURE",
        "Smoothie shops, juice bars, and corner stores all sell drinks made from a fixed recipe. "
        "<i>What is your go-to drink, and what two ingredients would you mix?</i>")
    read_aloud(
        "Maya's smoothie uses 2 cups of strawberries for every 3 cups of yogurt. She makes 1, 2, "
        "3, and 4 batches. Build the ratio table, then turn each row into a point: strawberries "
        "go across on x, yogurt goes up on y."
    )
    batches = st.slider("Number of batches shown", 1, 6, 4, key="d24_batches")
    rows = [(2 * k, 3 * k) for k in range(1, batches + 1)]
    c1, c2 = st.columns([1, 1.4])
    with c1:
        st.table([{"Batches": k, "Strawberries (x)": a, "Yogurt (y)": b, "Point": f"({a}, {b})"}
                  for k, (a, b) in enumerate(rows, 1)])
    with c2:
        st.pyplot(draw_ratio_graph([("strawberries : yogurt", NAVY, rows)],
                                   "cups of strawberries (x)", "cups of yogurt (y)",
                                   xmax=14, ymax=20))
    box("existing", "WHAT DO YOU NOTICE?",
        "The points line up. The dashed line passes through <b>(0, 0)</b> — zero strawberries "
        "means zero yogurt. Every step right 2 goes up 3.")
    ask_the_class("Where would the point for half a batch go? Is (1, 1½) on the line?")

elif step == 3:
    box("literacy", "MATH LITERACY: ORDERED PAIR",
        "An <b>ordered pair (x, y)</b> names a point: move <b>x</b> across, then <b>y</b> up. "
        "In a ratio graph, x is the first quantity and y is the second. <b>Order matters</b> — "
        "(2, 3) and (3, 2) are different points, just like 2 : 3 and 3 : 2 are different ratios.")
    read_aloud(
        "Pick any ratio. The app builds the table and plots every row. Watch the line. Change the "
        "ratio — the line gets steeper or flatter, but it always starts at zero."
    )
    c1, c2, c3 = st.columns(3)
    a = c1.number_input("First quantity (x)", 1, 12, 3, key="d24_a")
    b = c2.number_input("Second quantity (y)", 1, 12, 2, key="d24_b")
    n = c3.slider("Rows", 2, 6, 4, key="d24_n")
    rows = [(a * k, b * k) for k in range(1, n + 1)]
    cA, cB = st.columns([1, 1.4])
    with cA:
        st.table([{"× k": f"× {k}", "x": x, "y": y, "(x, y)": f"({x}, {y})"}
                  for k, (x, y) in enumerate(rows, 1)])
        st.markdown(f"Every step: **right {a}, up {b}**.")
    with cB:
        st.pyplot(draw_ratio_graph([(f"{a} : {b}", NAVY, rows)], "x", "y"))
    st.markdown("##### Plot a point yourself")
    px = st.number_input("x-coordinate", 0, 60, 0, key="d24_px")
    py = st.number_input("y-coordinate", 0, 60, 0, key="d24_py")
    if st.button("Is my point on the line?", key="d24_pt"):
        if px == 0 and py == 0:
            st.info("(0, 0) is always on a ratio line — zero of one means zero of the other.")
        elif px * b == py * a:
            st.success(f"Yes — ({px}, {py}) is equivalent to {a} : {b}. "
                       f"Check: {px} × {b} = {px * b} and {py} × {a} = {py * a}.")
        else:
            st.error(f"No — ({px}, {py}) is off the line. {px} × {b} = {px * b} but "
                     f"{py} × {a} = {py * a}.")
    ask_the_class("Which ratio made the steepest line? What is true about its numbers?")

elif step == 4:
    box("literacy", "MATH LITERACY: READ THE GRAPH",
        "To find a missing value, go to the known value on its axis, move to the line, then read "
        "the other axis. The line fills in every equivalent ratio — even ones between the table "
        "rows.")
    read_aloud(
        "A school printer prints 15 pages every 2 minutes. How many pages in 5 minutes? The "
        "table jumps from 4 minutes to 6 minutes. The line does not skip anything."
    )
    rows = [(2, 15), (4, 30), (6, 45), (8, 60)]
    target = st.select_slider("Minutes", options=[Fraction(k, 2) for k in range(1, 21)],
                              value=Fraction(5), format_func=mixed, key="d24_read")
    ty = target * Fraction(15, 2)
    st.pyplot(draw_ratio_graph([("minutes : pages", NAVY, rows)], "minutes (x)", "pages (y)",
                               xmax=11, ymax=80, highlight=(target, ty)))
    st.markdown(f"**{mixed(target)} minutes → {mixed(ty)} pages.**")
    st.markdown("##### Your turn")
    check_answer("How many minutes to print 75 pages?", 10, "d24_rd1",
                 "Find 75 on the y-axis, go across to the line, then down.")
    check_answer("How many pages in 1 minute? (the unit rate)", Fraction(15, 2), "d24_rd2",
                 "Halve the first row: 2 min → 1 min, so halve 15 pages too.",
                 success="Correct — 7½ pages per minute. That's the point (1, 7½).")
    ask_the_class("The table never had 5 minutes. How did the graph still know?")

elif step == 5:
    box("existing", "THE CLAIM",
        "Jordan says: <i>&ldquo;3 : 2 is equivalent to 5 : 4 because I added 2 to both.&rdquo;</i> "
        "Jordan plotted (3, 2) and (5, 4) and connected them. <b>Is Jordan correct?</b>")
    base = [(3, 2), (6, 4), (9, 6)]
    wrong = [(3, 2), (5, 4), (7, 6)]
    show = st.checkbox("Show Jordan's 'add 2' points next to the real equivalent ratios",
                       value=True, key="d24_err")
    series = [("× (equivalent)", NAVY, base)]
    if show:
        series.append(("+ 2 (Jordan)", RED, wrong))
    st.pyplot(draw_ratio_graph(series, "x", "y", xmax=11, ymax=8))
    c1, c2 = st.columns(2)
    with c1:
        st.error("Adding 2 each time makes a line that does **not** go through (0, 0). "
                 "Extend it back: at x = 1 it would hit y = 0 — one of something for zero of the "
                 "other. That isn't the same recipe.")
    with c2:
        st.success("Multiplying keeps every point on the ray from (0, 0). "
                   "Cross-product check: 3 × 4 = 12 but 2 × 5 = 10 — not equivalent.")
    box("literacy", "THE GRAPH TEST",
        "Two ratios are equivalent when their points sit on the <b>same straight line through "
        "(0, 0)</b>.")
    pick = st.radio("Which pair is equivalent to 4 : 6?",
                    ["(6, 8)", "(10, 15)", "(5, 7)", "(8, 10)"], index=None, key="d24_ea")
    if st.button("Check", key="d24_ea_chk"):
        if pick == "(10, 15)":
            st.success("Correct — 4 : 6 = 2 : 3 and 10 : 15 = 2 : 3. Both land on the same line.")
        elif pick:
            st.error("That one adds instead of multiplying. Divide 4 : 6 down to 2 : 3 first.")
    ask_the_class("If a line of ratio points doesn't pass through (0, 0), what does that tell you?")

elif step == 6:
    box("literacy", "MATH LITERACY: COMPARE STEEPNESS",
        "When two ratios are graphed on the same axes, the <b>steeper</b> line has more y for "
        "every 1 of x.")
    read_aloud(
        "Two runners on the track. Aaliyah runs 3 laps every 4 minutes. Brandon runs 2 laps every "
        "3 minutes. Put minutes on x and laps on y. The steeper line is the faster runner — no "
        "division required, you can see it."
    )
    A = [(4, 3), (8, 6), (12, 9)]
    B = [(3, 2), (6, 4), (9, 6), (12, 8)]
    st.pyplot(draw_ratio_graph([("Aaliyah 3 laps : 4 min", NAVY, A),
                                ("Brandon 2 laps : 3 min", GOLD, B)],
                               "minutes (x)", "laps (y)", xmax=14, ymax=11))
    pick = st.radio("Who is faster?", ["Aaliyah", "Brandon", "Same speed"], index=None,
                    horizontal=True, key="d24_run")
    if st.button("Check", key="d24_run_chk"):
        if pick == "Aaliyah":
            st.success("Aaliyah. At 12 minutes she has 9 laps; Brandon has 8. Her line is steeper.")
        elif pick:
            st.error("Look at x = 12 minutes. Who has more laps?")
    box("tools", "CAREER CONNECTION",
        "Coaches, delivery dispatchers, and nurses reading an IV drip rate all compare "
        "lines like these every day.")
    ask_the_class("Where on the graph do the two runners have the same number of laps? "
                  "(Only at 0, 0.)")

elif step == 7:
    read_aloud(
        "Graph Lab. Each team gets a ratio card. Build a four-row table, plot it on grid paper, "
        "and draw the ray from zero. Then you get a mystery point. Decide, with proof, whether it "
        "belongs on your line."
    )
    box("tools", "The rules",
        "1) Reader, Table-builder, Plotter, Checker. "
        "2) Label both axes with the quantity names. "
        "3) Your proof must use the table <b>and</b> the graph. "
        "4) Checker confirms with cross products before submitting.")
    cards = {
        "Card 1 — 2 cups rice : 3 cups water": ((2, 3), (7, Fraction(21, 2))),
        "Card 2 — 5 pages : 2 minutes": ((5, 2), (12, 5)),
        "Card 3 — 4 blue : 1 yellow": ((4, 1), (18, Fraction(9, 2))),
        "Card 4 — 3 dogs : 5 cats": ((3, 5), (8, 13)),
        "Card 5 — 6 miles : 1 hour": ((6, 1), (15, Fraction(5, 2))),
    }
    card = st.selectbox("Draw a card:", list(cards), key="d24_card")
    (ra, rb), mystery = cards[card]
    st.markdown(f"**Mystery point:** ({mixed(mystery[0])}, {mixed(mystery[1])})")
    if st.checkbox("Show the teacher key for this card", key="d24_key"):
        ok = equivalent((ra, rb), mystery)
        st.pyplot(draw_ratio_graph([(f"{ra} : {rb}", NAVY, [(ra * k, rb * k) for k in range(1, 5)])],
                                   "x", "y", highlight=mystery))
        st.markdown(("✅ **On the line.** " if ok else "❌ **Off the line.** ") +
                    f"{mixed(mystery[0])} × {rb} = {mixed(mystery[0] * rb)} and "
                    f"{mixed(mystery[1])} × {ra} = {mixed(mystery[1] * ra)}.")
    st.markdown("##### 🏆 Team submissions")
    if "d24_lab" not in st.session_state:
        st.session_state.d24_lab = []
    with st.form("d24_form", clear_on_submit=True):
        c1, c2, c3 = st.columns(3)
        team = c1.text_input("Team")
        which = c2.selectbox("Card", list(cards))
        verdict = c3.selectbox("Mystery point is…", ["On the line", "Off the line"])
        proof = st.text_input("Proof in one sentence")
        if st.form_submit_button("Submit"):
            if not team.strip() or not proof.strip():
                st.warning("Team name and proof are both required.")
            else:
                r, mp = cards[which]
                truth = "On the line" if equivalent(r, mp) else "Off the line"
                st.session_state.d24_lab.append({
                    "Team": team.strip(), "Card": which.split(" — ")[0], "Said": verdict,
                    "Proof": proof.strip(), "Result": "✅" if verdict == truth else "❌"})
    if st.session_state.d24_lab:
        st.table(st.session_state.d24_lab)
    else:
        st.caption("No teams have submitted yet.")
    ask_the_class("Card 4's mystery point was close to the line but not on it. How did your team "
                  "know for sure?")

elif step == 8:
    st.markdown("#### Engage / Explore / Enrich stations")
    tabs = st.tabs(["Engage (all)", "Explore (on-level)", "Enrich (extend)"])
    with tabs[0]:
        st.write("Independent practice — **Lesson 13 Session 3 practice** in the Student "
                 "Bookshelf. Use the graph of **5 : 2** (5 pages every 2 minutes).")
        rows = [(2, 5), (4, 10), (6, 15)]
        st.pyplot(draw_ratio_graph([("minutes : pages", NAVY, rows)], "minutes (x)", "pages (y)",
                                   xmax=11, ymax=28, figsize=(5.2, 3.6)))
        check_answer("1. How many pages in 8 minutes?", 20, "d24_p1",
                     "Each 2 minutes adds 5 pages. Or multiply 2 : 5 by 4.")
        check_answer("2. How many minutes for 25 pages?", 10, "d24_p2",
                     "25 is 5 × 5, so the minutes are 2 × 5.")
        check_answer("3. How many pages in 3 minutes?", Fraction(15, 2), "d24_p3",
                     "Halfway between 2 and 4 minutes on the line.")
    with tabs[1]:
        st.write("Partner check: Partner A plots 4 : 3, Partner B plots 8 : 6 and 12 : 9 on the "
                 "same axes. Do you get one line or two? Then plot 5 : 4 in a new color and "
                 "explain in writing why it is on a different line.")
    with tabs[2]:
        st.write("**Unit rate on the graph.** On the line for 5 pages : 2 minutes, find the point "
                 "where x = 1. What does its y-value mean? Then find the point where y = 1. What "
                 "does its x-value mean?")
        if st.button("Reveal", key="d24_enrich"):
            st.success("(1, 2½): 2½ pages per minute. (⅖, 1): ⅖ of a minute per page "
                       "(24 seconds).")
    box("existing", "EXIT TICKET",
        "A recipe uses <b>3 cups of flour for every 2 eggs</b>. (a) List three points on its "
        "graph. (b) Is the point <b>(12, 8)</b> on the line? (c) Is <b>(5, 4)</b>? Explain one "
        "with the graph and one with numbers.")
    et = st.radio("(b) Is (12, 8) on the line?", ["Yes", "No"], index=None, horizontal=True,
                  key="d24_et1")
    et2 = st.radio("(c) Is (5, 4) on the line?", ["Yes", "No"], index=None, horizontal=True,
                   key="d24_et2")
    if st.button("Check exit ticket", key="d24_et_chk"):
        good = et == "Yes" and et2 == "No"
        (st.success if good else st.error)(
            "(12, 8) = 3 : 2 × 4 — on the line. (5, 4) adds 2 to each — off the line "
            "(5 × 2 = 10, 4 × 3 = 12).")
    observer_log()


st.markdown("---")
c_back, c_next = st.columns([1, 1])
if c_back.button("⬅ Back", disabled=(step == 0)):
    st.session_state.step_d24 = max(0, step - 1)
    st.rerun()
if c_next.button("Next ➡", disabled=(step == len(STEPS) - 1)):
    st.session_state.step_d24 = min(len(STEPS) - 1, step + 1)
    st.rerun()

st.caption(STANDARDS_CAPTION)
st.markdown(
    "<div style='text-align:center;color:#8a939c;font-size:11px;margin-top:18px;'>"
    "www.cognitivecloud.ai &middot; Developed by Xavier Honablue, M.Ed"
    "</div>",
    unsafe_allow_html=True,
)
