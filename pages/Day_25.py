"""
Math 6 — Day 25: Refine Equivalent Ratios, Part 1 — Choose Your Model
Same structure as the Day 22–24 apps, by Xavier Honablue, M.Ed.

Aligned to i-Ready Classroom Mathematics, Grade 6, Unit 3 (Ratio Reasoning):
Lesson 13, Session 5 — Refine: Finding Equivalent Ratios (Part 1 of an extended Refine,
continued Day 26 and Day 27, Lesson 13 Quiz on Day 28).

Run locally with:  streamlit run app.py
"""
PAGE_TITLE = "Day 25 — Refine: Choose Your Model"
PAGE_ICON = "🧰"
DAY_LABEL = "Day 25"
ROADMAP_SUB = "55-minute period — Find Equivalent Ratios, Session 5 (Refine), Part 1 of 3"
STEPS = [
    "1. Welcome Back",
    "2. Warm-Up: One Ratio, Four Models",
    "3. Refine Example A: Ratio Table",
    "4. Refine Example B: Double Number Line",
    "5. Refine Example C: Graph",
    "6. Choose Your Model",
    "7. Error Analysis: Three Wrong Answers",
    "8. Project: Model Match-Up Relay",
    "9. Refine Practice & Exit Ticket",
]
DEFAULT_NOTES = [{
    "date": "Day 24",
    "note": "The graph made the add-vs-multiply error visible: students could SEE Jordan's points "
            "leave the line. Several students still reach for adding when the multiplier is not "
            "obvious. Refine starts by making them choose a model on purpose.",
}]
STANDARDS_CAPTION = ("Standards in play: 6.RP.A.1 · 6.RP.A.3 (use ratio reasoning to solve "
                     "real-world problems) · 6.RP.A.3a (tables of equivalent ratios, missing "
                     "values, plotting pairs) · SMP 1, 3, 5.")

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
NOTES_FILE = os.path.join(os.path.dirname(__file__), "observer_notes_day25.json")


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


if "observer_notes_d25" not in st.session_state:
    st.session_state.observer_notes_d25 = load_notes()


def observer_log():
    st.markdown("---")
    st.markdown("#### 🔎 Observer Notes (running log)")
    st.caption("A running teacher log carried day to day. Add what you noticed in class today, "
               "then Save — copy it into tomorrow's app to keep the thread going.")
    for n in st.session_state.observer_notes_d25:
        st.markdown(f"**{n['date']}:** {n['note']}")
    new_note = st.text_area("Add a new observation:", key="new_observer_note")
    if st.button("Save observation"):
        if new_note.strip():
            st.session_state.observer_notes_d25.append(
                {"date": f"{DAY_LABEL} — {datetime.now().strftime('%Y-%m-%d')}",
                 "note": new_note.strip()})
            save_notes(st.session_state.observer_notes_d25)
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
    if "step_d25" not in st.session_state:
        st.session_state.step_d25 = 0
    for i, label in enumerate(STEPS):
        marker = "▶ " if i == st.session_state.step_d25 else ""
        if st.button(marker + label, key=f"nav_{i}", width="stretch"):
            st.session_state.step_d25 = i
            st.rerun()

step = st.session_state.step_d25
name = st.session_state.get("student_name", "") or "class"
st.markdown(f"## {STEPS[step]}")
st.progress((step + 1) / len(STEPS))


if step == 0:
    box("observer", "🔎 OBSERVER NOTE — carried from Day 24",
        f"<p style='margin:0'>{st.session_state.observer_notes_d25[0]['note']}</p>")
    read_aloud(
        "You now own four tools for equivalent ratios: equal groups, the double number line, the "
        "ratio table, and the graph. This week is Refine week. No new idea — just getting sharp. "
        "Today the question is not only 'what is the answer' but 'which tool gets me there "
        "fastest, and how do I prove it?'"
    )
    box("tools", "Today's tools",
        "Model menu card (table · double number line · graph · tape diagram) &middot; grid paper "
        "&middot; relay answer sheets &middot; journal &middot; exit ticket.")
    box("literacy", "LEARNING TARGETS",
        "I can choose a model — table, double number line, or graph — to find equivalent ratios.<br>"
        "I can explain why my model works and check my answer a second way.<br>"
        "I can find and fix the three most common equivalent-ratio errors.")
    slides_ref("Grade 6 &rsaquo; Unit 3 &rsaquo; Lesson 13 &rsaquo; <b>Session 5 Refine</b> "
               "slides: Example A, B, C and the Refine problems. Project Examples A–C next to "
               "steps 3–5.")
    ask_the_class("Which of the four models do you trust most right now? Why?")

elif step == 1:
    st.write("**Purpose:** See one ratio in every model before choosing between them.")
    a, b = st.columns(2)
    ra = a.number_input("Part 1", 1, 9, 5, key="d25_ra")
    rb = b.number_input("Part 2", 1, 9, 3, key="d25_rb")
    rows = [(ra * k, rb * k) for k in range(1, 5)]
    t1, t2, t3 = st.tabs(["Ratio table", "Double number line", "Graph"])
    with t1:
        st.table([{"× k": f"× {k}", "first": x, "second": y} for k, (x, y) in enumerate(rows, 1)])
    with t2:
        st.pyplot(draw_double_number_line(rows, "first", "second"))
    with t3:
        st.pyplot(draw_ratio_graph([(f"{ra} : {rb}", NAVY, rows)], "first (x)", "second (y)",
                                   figsize=(5.6, 3.8)))
    box("existing", "SAME RATIO, THREE PICTURES",
        "The table lists the pairs. The double number line lines them up. The graph turns them "
        "into points on one line through (0, 0). All three are built by <b>multiplying both "
        "quantities by the same number</b>.")
    ask_the_class("Which model would you use if the question asked about 1½ batches?")

elif step == 2:
    box("tools", "REFINE EXAMPLE A — RATIO TABLE",
        "A florist puts <b>4 roses with every 6 daisies</b>. She has <b>30 daisies</b>. "
        "How many roses does she need?")
    read_aloud("A ratio table is fastest when you can see the multiplier. Six to thirty — "
               "times five. Do the same to four.")
    ratio_table([("given", 4, 6), ("÷ 2", 2, 3), ("× 5 (from 4 : 6)", 20, 30)],
                ["Move", "Roses", "Daisies"])
    box("existing", "WHY IT WORKS",
        "30 ÷ 6 = 5, so both quantities are multiplied by 5: 4 × 5 = <b>20 roses</b>. "
        "Check: 20 : 30 = 2 : 3 = 4 : 6.")
    st.markdown("##### Try one like it")
    check_answer("The florist has 45 daisies. How many roses?", 30, "d25_a1",
                 "45 ÷ 6 is not whole — go through 2 : 3 first. 45 ÷ 3 = 15.",
                 success="Correct — 30 roses. 2 : 3 × 15 = 30 : 45.")
    ask_the_class("Why did going through 2 : 3 help with 45 daisies?")

elif step == 3:
    box("tools", "REFINE EXAMPLE B — DOUBLE NUMBER LINE",
        "A car uses <b>3 gallons of gas every 90 miles</b>. How many gallons for <b>150 miles</b>?")
    read_aloud("A double number line is best when the answer lands between the easy tick marks. "
               "Mark 30 miles for every 1 gallon, then count up to 150.")
    pts = [(30 * k, k) for k in range(1, 7)]
    st.pyplot(draw_double_number_line(pts, "miles", "gallons", highlight=150))
    box("existing", "WHY IT WORKS",
        "90 : 3 → ÷ 3 → 30 : 1 → × 5 → <b>150 : 5</b>. The car needs <b>5 gallons</b>.")
    st.markdown("##### Try one like it")
    check_answer("How many gallons for 105 miles?", Fraction(7, 2), "d25_b1",
                 "105 is halfway between 90 and 120 on the line.",
                 success="Correct — 3½ gallons. 105 ÷ 30 = 3½.")
    ask_the_class("Where would 105 miles sit on the line? How did that tell you the answer?")

elif step == 4:
    box("tools", "REFINE EXAMPLE C — GRAPH",
        "Two lemonade recipes: <b>Recipe 1 uses 2 scoops for every 5 cups water</b>. "
        "<b>Recipe 2 uses 3 scoops for every 8 cups water</b>. Are they the same flavor?")
    read_aloud("A graph is best when you are comparing. Same flavor means same line.")
    r1 = [(5, 2), (10, 4), (15, 6)]
    r2 = [(8, 3), (16, 6)]
    st.pyplot(draw_ratio_graph([("Recipe 1: 2 scoops : 5 cups", NAVY, r1),
                                ("Recipe 2: 3 scoops : 8 cups", GOLD, r2)],
                               "cups of water (x)", "scoops (y)", xmax=18, ymax=8))
    pick = st.radio("Which recipe is stronger (more lemon)?", ["Recipe 1", "Recipe 2", "Same"],
                    index=None, horizontal=True, key="d25_c")
    if st.button("Check", key="d25_c_chk"):
        if pick == "Recipe 1":
            st.success("Recipe 1 — its line is steeper: more scoops for the same water. "
                       "Numbers: 2 × 8 = 16 but 5 × 3 = 15, so they are not equivalent.")
        elif pick:
            st.error("Compare at 40 cups of water: Recipe 1 has 16 scoops, Recipe 2 has 15.")
    ask_the_class("Could you have answered this without the graph? What would you do instead?")

elif step == 5:
    box("literacy", "MATH LITERACY: CHOOSE YOUR MODEL",
        "<b>Ratio table</b> — the multiplier is easy to see or you need several answers. "
        "<b>Double number line</b> — the answer lands between friendly marks. "
        "<b>Graph</b> — you are comparing two ratios or testing if a point belongs.")
    problems = [
        ("A printer prints 12 pages in 3 min. How many pages in 10 min?", "Double number line",
         Fraction(40), "pages"),
        ("Paint: 2 cans cover 350 sq ft. How many cans for 1,400 sq ft?", "Ratio table",
         Fraction(8), "cans"),
        ("Is 6 : 9 the same ratio as 10 : 15 and 14 : 20?", "Graph", None, None),
        ("A recipe uses 3 eggs for 4 cups flour. Eggs for 10 cups flour?", "Double number line",
         Fraction(15, 2), "eggs"),
    ]
    for i, (q, best, ans, unit) in enumerate(problems):
        st.markdown(f"**{i + 1}.** {q}")
        c1, c2 = st.columns([1, 1])
        choice = c1.selectbox("Model I'd choose", ["—", "Ratio table", "Double number line",
                                                   "Graph"], key=f"d25_m{i}")
        if choice != "—":
            if choice == best:
                c1.success(f"Good choice — {best}.")
            else:
                c1.info(f"That can work. Many students choose **{best}** here. Explain yours.")
        with c2:
            if ans is not None:
                check_answer(f"Answer ({unit})", ans, f"d25_ans{i}",
                             "Find the multiplier on the quantity you know, then use it on the other.")
            else:
                g = st.radio("Which is NOT equivalent?", ["6 : 9", "10 : 15", "14 : 20"],
                             index=None, key="d25_g")
                if g:
                    (st.success if g == "14 : 20" else st.error)(
                        "14 : 20 is off the line: 14 × 3 = 42 but 20 × 2 = 40.")
    ask_the_class("Did two people pick different models for the same problem and still get the "
                  "same answer?")

elif step == 6:
    read_aloud("Three students answered the same problem and all three are wrong in a different "
               "way. Name each error and fix it. The problem: 4 blue beads for every 7 red beads. "
               "How many blue beads go with 28 red beads?")
    errors = [
        ("Kiara: “28 − 7 = 21, so 4 + 21 = 25 blue.”", "Adding",
         "She added the same amount instead of multiplying. 28 ÷ 7 = 4, so 4 × 4 = 16."),
        ("Marcus: “7 × 4 = 28, so the answer is 7 blue.”", "Flipped the order",
         "He used 7 from the red side. The blue side is 4, so 4 × 4 = 16."),
        ("Tae: “28 ÷ 7 = 4, so 28 blue.”", "Multiplied only one quantity",
         "He found the multiplier but never used it on the blue beads: 4 × 4 = 16."),
    ]
    for i, (claim, label, fix) in enumerate(errors):
        box("existing", f"STUDENT {i + 1}", claim)
        pick = st.selectbox("Name the error", ["—", "Adding", "Flipped the order",
                                               "Multiplied only one quantity"], key=f"d25_e{i}")
        if pick != "—":
            (st.success if pick == label else st.error)(fix if pick == label else
                                                        "Not quite — test it with the ratio table.")
    check_answer("The correct number of blue beads:", 16, "d25_eans",
                 "28 ÷ 7 = 4. Multiply the blue beads by 4 too.")
    ask_the_class("Which of the three errors have you made this week? How will you catch it?")

elif step == 7:
    read_aloud(
        "Relay. Teams of four. Each card has one ratio problem. Runner one solves with a table, "
        "runner two checks with a double number line, runner three checks on the graph, runner "
        "four writes the proof sentence. First team with four matching answers wins."
    )
    cards = {
        "Card A — 5 laps in 8 min. Laps in 20 min?": Fraction(25, 2),
        "Card B — 9 apples cost $6. Cost of 15 apples?": Fraction(10),
        "Card C — 4 in. on the map is 50 mi. Miles for 10 in.?": Fraction(125),
        "Card D — 6 teachers for 90 students. Teachers for 135 students?": Fraction(9),
    }
    card = st.selectbox("Draw a card:", list(cards), key="d25_card")
    if st.checkbox("Show the teacher key", key="d25_key"):
        st.markdown(f"**Answer: {mixed(cards[card])}**")
    if "d25_relay" not in st.session_state:
        st.session_state.d25_relay = []
    with st.form("d25_form", clear_on_submit=True):
        c1, c2, c3 = st.columns(3)
        team = c1.text_input("Team")
        which = c2.selectbox("Card", list(cards))
        ans = c3.text_input("Answer")
        proof = st.text_input("Proof sentence (\"We multiplied both by ___ because ___\")")
        if st.form_submit_button("Submit"):
            v = parse_mixed(ans)
            if not team.strip() or v is None:
                st.warning("Team and a numeric answer are required.")
            else:
                st.session_state.d25_relay.append({
                    "Team": team.strip(), "Card": which[:6], "Answer": mixed(v),
                    "Proof": proof.strip(), "Result": "✅" if v == cards[which] else "❌"})
    if st.session_state.d25_relay:
        st.table(st.session_state.d25_relay)
    else:
        st.caption("No teams have submitted yet.")

elif step == 8:
    st.markdown("#### Refine practice — Engage / Explore / Enrich")
    tabs = st.tabs(["Engage (all)", "Explore (on-level)", "Enrich (extend)"])
    with tabs[0]:
        st.write("**Lesson 13 Session 5 Refine**, problems 1–3 in the Student Bookshelf, plus:")
        check_answer("1. 3 cups rice : 5 cups water. Water for 12 cups rice?", 20, "d25_p1",
                     "12 ÷ 3 = 4. Multiply the water by 4.")
        check_answer("2. 8 pencils cost $2. Cost of 20 pencils (dollars)?", 5, "d25_p2",
                     "Go through 4 pencils : $1.")
        check_answer("3. 2 in. of rain every 3 hr. Rain in 7½ hr (inches)?", 5, "d25_p3",
                     "7½ ÷ 3 = 2½. Multiply 2 by 2½.")
    with tabs[1]:
        st.write("Solve problem 3 two ways — ratio table and double number line — and write one "
                 "sentence about which was faster for you.")
    with tabs[2]:
        st.write("**Three-way mix.** A granola uses oats : nuts : raisins = 4 : 2 : 1. You have "
                 "10 cups of oats. How many cups of each other ingredient, and how many cups in all?")
        if st.button("Reveal", key="d25_enrich"):
            st.success("Multiplier 10 ÷ 4 = 2½ → nuts 5 cups, raisins 2½ cups, total 17½ cups.")
    box("existing", "EXIT TICKET",
        "A bakery sells <b>6 muffins for $9</b>. (a) Choose a model and find the cost of "
        "<b>10 muffins</b>. (b) Name the model you chose and why.")
    check_answer("Cost of 10 muffins (dollars):", 15, "d25_exit",
                 "Go through 2 muffins : $3, then × 5.", success="Correct — $15.")
    observer_log()


st.markdown("---")
c_back, c_next = st.columns([1, 1])
if c_back.button("⬅ Back", disabled=(step == 0)):
    st.session_state.step_d25 = max(0, step - 1)
    st.rerun()
if c_next.button("Next ➡", disabled=(step == len(STEPS) - 1)):
    st.session_state.step_d25 = min(len(STEPS) - 1, step + 1)
    st.rerun()

st.caption(STANDARDS_CAPTION)
st.markdown(
    "<div style='text-align:center;color:#8a939c;font-size:11px;margin-top:18px;'>"
    "www.cognitivecloud.ai &middot; Developed by Xavier Honablue, M.Ed"
    "</div>",
    unsafe_allow_html=True,
)
