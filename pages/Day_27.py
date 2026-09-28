"""
Math 6 — Day 27: Refine Equivalent Ratios, Part 3 — Party Planner + i-Ready Online Lesson
Same structure as the Day 22–26 apps, by Xavier Honablue, M.Ed.

Aligned to i-Ready Classroom Mathematics, Grade 6, Unit 3 (Ratio Reasoning):
Lesson 13, Session 5 — Refine (Part 3 of an extended Refine). The second half of the
period is a second 30-minute teacher-assigned i-Ready online lesson that corroborates
Lesson 13 (solving problems with equivalent ratios, 6.RP.A.3 / 6.RP.A.3a).

Run locally with:  streamlit run app.py
"""
PAGE_TITLE = "Day 27 — Refine: Party Planner + i-Ready"
PAGE_ICON = "🎉"
DAY_LABEL = "Day 27"
ROADMAP_SUB = ("55-minute period — Lesson 13 Refine, Part 3 of 3 (25 min) + "
               "i-Ready online lesson (30 min)")
STEPS = [
    "1. Welcome Back",
    "2. Data Talk: Fix One Error",
    "3. Performance Task: Party Planner",
    "4. Engage / Explore / Enrich",
    "5. Closure: My Model, My Proof",
    "6. i-Ready Online Lesson (30 min)",
]
DEFAULT_NOTES = [{
    "date": "Day 26",
    "note": "Two-step problems exposed who can find a hidden multiplier and who still needs the "
            "multiplier handed to them. i-Ready pass rate on the equivalent-ratios lesson is the "
            "list for today's small group. Students who passed early moved into My Path.",
}]
STANDARDS_CAPTION = ("Standards in play: 6.RP.A.3 (use ratio reasoning to solve real-world "
                     "problems) · 6.RP.A.3a (tables of equivalent ratios; missing values; "
                     "plotting pairs) · SMP 1, 4 · i-Ready online lesson aligned to 6.RP.A.3a.")

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
NOTES_FILE = os.path.join(os.path.dirname(__file__), "observer_notes_day27.json")


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


if "observer_notes_d27" not in st.session_state:
    st.session_state.observer_notes_d27 = load_notes()


def observer_log():
    st.markdown("---")
    st.markdown("#### 🔎 Observer Notes (running log)")
    st.caption("A running teacher log carried day to day. Add what you noticed in class today, "
               "then Save — copy it into tomorrow's app to keep the thread going.")
    for n in st.session_state.observer_notes_d27:
        st.markdown(f"**{n['date']}:** {n['note']}")
    new_note = st.text_area("Add a new observation:", key="new_observer_note")
    if st.button("Save observation"):
        if new_note.strip():
            st.session_state.observer_notes_d27.append(
                {"date": f"{DAY_LABEL} — {datetime.now().strftime('%Y-%m-%d')}",
                 "note": new_note.strip()})
            save_notes(st.session_state.observer_notes_d27)
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
    if "step_d27" not in st.session_state:
        st.session_state.step_d27 = 0
    for i, label in enumerate(STEPS):
        marker = "▶ " if i == st.session_state.step_d27 else ""
        if st.button(marker + label, key=f"nav_{i}", width="stretch"):
            st.session_state.step_d27 = i
            st.rerun()

step = st.session_state.step_d27
name = st.session_state.get("student_name", "") or "class"
st.markdown(f"## {STEPS[step]}")
st.progress((step + 1) / len(STEPS))


if step == 0:
    box("observer", "🔎 OBSERVER NOTE — carried from Day 26",
        f"<p style='margin:0'>{st.session_state.observer_notes_d27[0]['note']}</p>")
    read_aloud(
        "Last day of Refine. Today you use everything at once. You are planning a party for the "
        "whole grade, and every part of the plan is an equivalent ratio. Then thirty more minutes "
        "on i-Ready. Tomorrow is the Lesson 13 Quiz — today is your dress rehearsal."
    )
    box("tools", "Today's tools",
        "Party Planner task card &middot; model menu card &middot; grid paper &middot; "
        "<b>Chromebook + headphones</b> for the i-Ready block.")
    box("literacy", "LEARNING TARGETS",
        "I can find and fix my own mistake in an equivalent-ratio problem.<br>"
        "I can use equivalent ratios to plan a real event and explain which model I chose.<br>"
        "I can pass my second assigned i-Ready lesson.")
    slides_ref("Grade 6 &rsaquo; Unit 3 &rsaquo; Lesson 13 &rsaquo; <b>Session 5 Refine</b>: "
               "Apply It problems. In i-Ready, assign the second Grade 6 online lesson on "
               "<b>solving problems with equivalent ratios</b> (ratio tables / double number "
               "lines) before class.")
    box("iready", "⏱ PACING", "Steps 1–5: <b>25 minutes</b> &nbsp;·&nbsp; Step 6 i-Ready: "
        "<b>30 minutes</b>. Start the i-Ready timer no later than minute 25.")

elif step == 1:
    st.write("**Purpose (3 min):** Every student gets back Wednesday's exit ticket with one "
             "error circled. Fix it in the margin.")
    box("existing", "THE MOST COMMON ERROR FROM WEDNESDAY",
        "“3 cups juice : 2 cups soda. For 7½ cups juice: 7½ − 3 = 4½, so 2 + 4½ = "
        "<b>6½ cups soda</b>.”")
    pick = st.radio("What went wrong?", ["They added instead of multiplying",
                                         "They flipped the order",
                                         "They multiplied only one quantity"],
                    index=None, key="d27_err")
    if pick:
        (st.success if pick.startswith("They added") else st.error)(
            "Added the same amount (4½) to both. The multiplier is 7½ ÷ 3 = 2½, "
            "so soda = 2 × 2½ = 5 cups.")
    st.markdown("##### Fix it on the double number line")
    st.pyplot(draw_double_number_line([(3, 2), (6, 4), (Fraction(15, 2), 5), (9, 6)],
                                      "juice", "soda", highlight=Fraction(15, 2)))

elif step == 2:
    read_aloud(
        "The sixth grade is throwing an end-of-unit party for 90 students. Your team is the "
        "planning committee. Every item comes with a ratio. Solve each one, name your model, and "
        "the app will total your order."
    )
    box("tools", "PARTY PLANNER — THE RATIOS",
        "🍕 <b>3 pizzas for every 20 students</b><br>"
        "🧃 <b>2 gallons of punch for every 15 students</b> — punch is 3 cups juice : 2 cups soda<br>"
        "🍪 <b>5 cookies for every 2 students</b><br>"
        "🪑 <b>1 table for every 6 students</b><br>"
        "💵 Pizza costs <b>$24 for 2 pizzas</b>")
    students = st.select_slider("Students coming", options=[30, 45, 60, 90, 120], value=90,
                                key="d27_n")
    items = [
        ("🍕 Pizzas", Fraction(3 * students, 20), "pizzas"),
        ("🧃 Gallons of punch", Fraction(2 * students, 15), "gallons"),
        ("🍪 Cookies", Fraction(5 * students, 2), "cookies"),
        ("🪑 Tables", Fraction(students, 6), "tables"),
    ]
    st.markdown(f"##### Plan for {students} students")
    results = []
    for i, (label, ans, unit) in enumerate(items):
        c1, c2 = st.columns([1.3, 1])
        with c1:
            ok = check_answer(f"{label} needed:", ans, f"d27_it{i}_{students}",
                              f"Multiplier = {students} ÷ the students in the ratio. "
                              "Use it on the other quantity.")
        with c2:
            st.selectbox("Model I used", ["Ratio table", "Double number line", "Graph"],
                         key=f"d27_md{i}_{students}")
        results.append((label, ans, unit, ok))
    pizzas = Fraction(3 * students, 20)
    whole_pizzas = -(-pizzas.numerator // pizzas.denominator)
    st.markdown("##### Stretch: the budget")
    check_answer(f"Cost of {whole_pizzas} pizzas (dollars) — round pizzas UP to whole pizzas first:",
                 whole_pizzas * 12, f"d27_cost_{students}",
                 "$24 : 2 pizzas → $12 : 1 pizza. Multiply by the number of pizzas.")
    if st.checkbox("Show the teacher key", key="d27_key"):
        st.table([{"Item": l, "Exact": mixed(a), "Order": f"{-(-a.numerator // a.denominator)} {u}"}
                  for l, a, u, _ in results])
        st.caption("Real orders round UP — you can't buy 13½ pizzas, and nobody goes without.")
    ask_the_class("Which item did your team solve with a graph? Why would anyone choose a graph "
                  "here?")

elif step == 3:
    st.markdown("#### Engage / Explore / Enrich (7 min)")
    tabs = st.tabs(["Engage (with teacher)", "Explore (on-level)", "Enrich (extend)"])
    with tabs[0]:
        st.write("With linking cubes at the teacher table: build 2 blue : 5 red. Copy it until "
                 "you have 20 red. Record every copy in a table.")
        check_answer("How many blue cubes go with 20 red?", 8, "d27_eng",
                     "Count your copies: 20 red is 4 copies of 5 red.")
    with tabs[1]:
        st.write("**Lesson 13 Refine Apply It.** A map scale is 2 cm : 15 km.")
        check_answer("Kilometers for 9 cm?", Fraction(135, 2), "d27_exp1",
                     "9 ÷ 2 = 4½. 15 × 4½ = ?")
        check_answer("Centimeters for 60 km?", 8, "d27_exp2", "60 ÷ 15 = 4. 2 × 4 = ?")
    with tabs[2]:
        st.write("**Two ratios, one answer.** A paint shop mixes blue : white = 3 : 5 for "
                 "Sky and 2 : 3 for Ocean. You need 16 quarts of each color. How much blue paint "
                 "is that in total? Which color is darker?")
        if st.button("Reveal", key="d27_enr"):
            st.success("Sky: 16 × ⅜ = 6 qt blue. Ocean: 16 × ⅖ = 6⅖ qt blue. Total 12⅖ qt. "
                       "Ocean is darker (⅖ > ⅜ — its line is steeper).")

elif step == 4:
    st.write("**Closure (3 min):** One sentence each in your journal.")
    box("literacy", "SENTENCE FRAMES",
        "“For ______ I chose a ______ because ______.”<br>"
        "“I know my answer is right because when I check it ______.”<br>"
        "“The error I will watch for on tomorrow's quiz is ______.”")
    st.text_area("Type your closure sentences (optional):", key="d27_close")
    box("observer", "👩🏾‍🏫 TEACHER MOVE",
        "Collect journals as students log in to i-Ready. Anyone who named 'adding' as their "
        "error to watch for joins the first small group.")

elif step == 5:
    iready_block(
        "d27",
        "Grade 6 · Ratios &amp; Proportional Relationships — <b>solving problems with equivalent "
        "ratios</b> (ratio tables and double number lines, 6.RP.A.3a).",
        "The online lesson sets up real-world ratio problems and asks for missing values in "
        "tables and on double number lines — the Party Planner moves. Look for students who "
        "write the multiplier above the table column before they calculate.",
        "First pull: students logged 'Not yet' on Wednesday's i-Ready lesson. Re-teach with the "
        "i-Ready <b>Tools for Instruction</b> equivalent-ratios activity: redo one Party Planner "
        "item with a ratio table, name the multiplier out loud, then let them retake the "
        "online lesson's quiz. Second pull (last 10 min): quiz-readiness check with two "
        "problems from tomorrow's review.")
    observer_log()


st.markdown("---")
c_back, c_next = st.columns([1, 1])
if c_back.button("⬅ Back", disabled=(step == 0)):
    st.session_state.step_d27 = max(0, step - 1)
    st.rerun()
if c_next.button("Next ➡", disabled=(step == len(STEPS) - 1)):
    st.session_state.step_d27 = min(len(STEPS) - 1, step + 1)
    st.rerun()

st.caption(STANDARDS_CAPTION)
st.markdown(
    "<div style='text-align:center;color:#8a939c;font-size:11px;margin-top:18px;'>"
    "www.cognitivecloud.ai &middot; Developed by Xavier Honablue, M.Ed"
    "</div>",
    unsafe_allow_html=True,
)
