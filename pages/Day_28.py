"""
Math 6 — Day 28: Lesson 13 Review & Quiz — Find Equivalent Ratios
Same structure as the Day 22–27 apps, by Xavier Honablue, M.Ed.

Aligned to i-Ready Classroom Mathematics, Grade 6, Unit 3 (Ratio Reasoning):
Lesson 13 Quiz (i-Ready Teacher Toolbox, Lesson 13 assessment), with a review warm-up,
quiz corrections, and a preview of Lesson 14 (part-to-part and part-to-whole ratios).

Run locally with:  streamlit run app.py
"""
PAGE_TITLE = "Day 28 — Lesson 13 Review & Quiz"
PAGE_ICON = "📝"
DAY_LABEL = "Day 28"
ROADMAP_SUB = "55-minute period — Lesson 13 Quiz day (review · quiz · corrections · preview)"
STEPS = [
    "1. Welcome Back",
    "2. Review: Four Models, Four Minutes",
    "3. Quiz Checklist",
    "4. Lesson 13 Quiz (25 min)",
    "5. Corrections: Fix-It Practice",
    "6. Reflection & Lesson 14 Preview",
]
DEFAULT_NOTES = [{
    "date": "Day 27",
    "note": "Party Planner showed most teams can find a hidden multiplier; rounding UP for real "
            "orders was the new wrinkle. Second i-Ready lesson pass rate was higher than "
            "Wednesday's. Watch for the 'add instead of multiply' error on the quiz.",
}]
STANDARDS_CAPTION = ("Standards assessed: 6.RP.A.1 · 6.RP.A.3 · 6.RP.A.3a (equivalent ratios "
                     "in tables, double number lines, and the coordinate plane).")

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
NOTES_FILE = os.path.join(os.path.dirname(__file__), "observer_notes_day28.json")


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


if "observer_notes_d28" not in st.session_state:
    st.session_state.observer_notes_d28 = load_notes()


def observer_log():
    st.markdown("---")
    st.markdown("#### 🔎 Observer Notes (running log)")
    st.caption("A running teacher log carried day to day. Add what you noticed in class today, "
               "then Save — copy it into tomorrow's app to keep the thread going.")
    for n in st.session_state.observer_notes_d28:
        st.markdown(f"**{n['date']}:** {n['note']}")
    new_note = st.text_area("Add a new observation:", key="new_observer_note")
    if st.button("Save observation"):
        if new_note.strip():
            st.session_state.observer_notes_d28.append(
                {"date": f"{DAY_LABEL} — {datetime.now().strftime('%Y-%m-%d')}",
                 "note": new_note.strip()})
            save_notes(st.session_state.observer_notes_d28)
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
    if "step_d28" not in st.session_state:
        st.session_state.step_d28 = 0
    for i, label in enumerate(STEPS):
        marker = "▶ " if i == st.session_state.step_d28 else ""
        if st.button(marker + label, key=f"nav_{i}", width="stretch"):
            st.session_state.step_d28 = i
            st.rerun()

step = st.session_state.step_d28
name = st.session_state.get("student_name", "") or "class"
st.markdown(f"## {STEPS[step]}")
st.progress((step + 1) / len(STEPS))


if step == 0:
    box("observer", "🔎 OBSERVER NOTE — carried from Day 27",
        f"<p style='margin:0'>{st.session_state.observer_notes_d28[0]['note']}</p>")
    read_aloud(
        "Quiz day. You have spent a full week and a half with equivalent ratios — equal groups, "
        "double number lines, tables, graphs, mixed-number multipliers, and two i-Ready lessons. "
        "Nothing on today's quiz is new. Warm up with me, check the list, then show what you know."
    )
    box("tools", "Today's tools",
        "Pencil &middot; eraser &middot; model menu card (face down during the quiz) &middot; "
        "i-Ready Lesson 13 Quiz &middot; correction sheet.")
    box("literacy", "LEARNING TARGETS",
        "I can show mastery of equivalent ratios on the Lesson 13 Quiz.<br>"
        "I can correct my errors and explain each correction with a multiplier.")
    slides_ref("Grade 6 &rsaquo; Unit 3 &rsaquo; Lesson 13 &rsaquo; <b>Lesson Quiz</b> "
               "(print from the Teacher Toolbox assessments, or assign it digitally in i-Ready). "
               "Accommodations per IEP/504.")

elif step == 1:
    st.write("**Review (5 min):** One ratio, four ways. Call on four students — one per model.")
    ra, rb = 3, 4
    rows = [(ra * k, rb * k) for k in range(1, 5)]
    t0, t1, t2, t3 = st.tabs(["Equal groups", "Ratio table", "Double number line", "Graph"])
    with t0:
        st.markdown("🟦🟦🟦 🟨🟨🟨🟨 &nbsp;|&nbsp; 🟦🟦🟦 🟨🟨🟨🟨 &nbsp;|&nbsp; 🟦🟦🟦 🟨🟨🟨🟨")
        st.caption("Three groups of 3 : 4 make 9 : 12.")
    with t1:
        st.table([{"× k": f"× {k}", "blue": x, "yellow": y} for k, (x, y) in enumerate(rows, 1)])
    with t2:
        st.pyplot(draw_double_number_line(rows, "blue", "yellow"))
    with t3:
        st.pyplot(draw_ratio_graph([("3 : 4", NAVY, rows)], "blue (x)", "yellow (y)",
                                   figsize=(5.4, 3.6)))
    check_answer("Quick check — how many yellow go with 7½ blue?", 10, "d28_rev",
                 "7½ ÷ 3 = 2½. 4 × 2½ = ?")

elif step == 2:
    st.write("**Quiz checklist (3 min):** Read it together, then flip the model card face down.")
    checks = [
        "I circle the two quantities and keep them in the SAME order the problem uses.",
        "I find the multiplier: new amount ÷ original amount of the SAME quantity.",
        "I multiply BOTH quantities by the same number — never add.",
        "If the multiplier isn't whole, I go through a smaller ratio or use a mixed number.",
        "I check with a second model or with cross products.",
        "I label my answer with units.",
    ]
    for i, c in enumerate(checks):
        st.checkbox(c, key=f"d28_chk{i}")
    box("existing", "REMEMBER", "Equivalent ratios sit on one straight line through (0, 0). "
        "If your answer came from adding, it is off the line.")

elif step == 3:
    box("iready", "📝 LESSON 13 QUIZ · 25 MIN",
        "Work silently and independently. Show your multiplier on every problem. "
        "When you finish, check every answer a second way, then turn it in and start Step 5 "
        "quietly.")
    html_widget(
        f"""
        <div style="font-family:Arial;text-align:center;padding:10px;border:3px solid {NAVY};
                    border-radius:12px;background:{NAVY_LIGHT}">
          <div style="font-size:13px;color:{NAVY};font-weight:700;letter-spacing:1px">QUIZ TIMER</div>
          <div id="qt" style="font-size:64px;font-weight:800;color:{NAVY}">25:00</div>
          <button id="qs" style="font-size:16px;padding:6px 18px;border-radius:8px;border:none;
                  background:{NAVY};color:white;cursor:pointer">▶ Start</button>
          <button id="qp" style="font-size:16px;padding:6px 18px;border-radius:8px;border:none;
                  background:{GOLD};color:white;cursor:pointer">⏸ Pause</button>
        </div>
        <script>
          let left = 25 * 60, t = null; const el = document.getElementById("qt");
          const show = () => {{ el.textContent = String(Math.floor(left/60)).padStart(2,"0") + ":" +
                                String(left%60).padStart(2,"0");
                                el.style.color = left <= 300 ? "{RED}" : "{NAVY}";
                                if (left === 0) el.textContent = "Pencils down"; }};
          document.getElementById("qs").onclick = () => {{ if (t) return;
            t = setInterval(() => {{ if (left > 0) {{ left--; show(); }} else {{ clearInterval(t); }} }}, 1000); }};
          document.getElementById("qp").onclick = () => {{ clearInterval(t); t = null; }};
        </script>
        """,
        height=180,
    )
    box("observer", "👩🏾‍🏫 TEACHER DURING THE QUIZ",
        "Circulate with a clipboard. Tally who shows a multiplier and who adds. Do not re-teach "
        "during the quiz — the tally decides Monday's small groups and who takes the retake after "
        "matching practice (per syllabus: highest score counts).")

elif step == 4:
    st.write("**Corrections (15 min):** Early finishers start here; everyone works here after "
             "the quiz. Each item matches a quiz skill.")
    items = [
        ("A. Ratio table", "5 notebooks cost $15. What do 8 notebooks cost (dollars)?", 24,
         "Go through 1 notebook : $3."),
        ("B. Double number line", "4 laps in 6 minutes. Minutes for 10 laps?", 15,
         "Mark 2 laps : 3 minutes, then count to 10 laps."),
        ("C. Mixed-number multiplier", "6 cups flour for 4 loaves. Flour for 10 loaves (cups)?", 15,
         "10 ÷ 4 = 2½. 6 × 2½ = ?"),
        ("D. Scale down", "36 red : 24 blue. Red for 6 blue?", 9,
         "24 ÷ 4 = 6, so divide 36 by 4 too."),
    ]
    score = 0
    for i, (tag, q, ans, hint) in enumerate(items):
        box("existing", tag, q)
        if check_answer("Answer:", ans, f"d28_fx{i}", hint):
            score += 1
    st.markdown("##### E. Graph")
    st.pyplot(draw_ratio_graph([("2 : 5", NAVY, [(2, 5), (4, 10), (6, 15)])], "x", "y",
                               xmax=9, ymax=22, figsize=(5.2, 3.4)))
    g = st.radio("Which point is on this line?", ["(5, 8)", "(8, 20)", "(3, 6)", "(7, 10)"],
                 index=None, key="d28_g")
    if g:
        ok = g == "(8, 20)"
        score += ok
        (st.success if ok else st.error)("(8, 20) = 2 : 5 × 4. The others add or mix the order.")
    st.progress(score / 5, text=f"Fix-It score: {score} / 5")

elif step == 5:
    box("literacy", "REFLECTION (JOURNAL)",
        "1. The model I trust most for equivalent ratios is ______ because ______.<br>"
        "2. One quiz problem I want to redo is # ___. Here is my fix: ______.<br>"
        "3. On a scale of 1–4, my confidence with equivalent ratios is ___.")
    conf = st.select_slider("My confidence (1–4)", options=[1, 2, 3, 4], value=3, key="d28_conf")
    if conf <= 2:
        st.info("Thanks for being honest. Keep going in i-Ready My Path this weekend and ask for a "
                "retake after the matching practice.")
    else:
        st.success("Nice. Lesson 14 builds right on top of this.")
    read_aloud(
        "Next week: Lesson 14. Part-to-part and part-to-whole ratios. If a class has 12 girls and "
        "15 boys, 12 to 15 compares a part to a part. 12 to 27 compares a part to the whole "
        "class. Same class, two different ratios — and both of them can be scaled exactly the "
        "way you did all week."
    )
    box("tools", "PREVIEW QUESTION",
        "A fruit bowl has <b>4 apples and 6 oranges</b>. Write the apples-to-oranges ratio and "
        "the apples-to-all-fruit ratio.")
    if st.button("Reveal", key="d28_prev"):
        st.success("Apples : oranges = 4 : 6 (part-to-part). Apples : all fruit = 4 : 10 "
                   "(part-to-whole).")
    observer_log()


st.markdown("---")
c_back, c_next = st.columns([1, 1])
if c_back.button("⬅ Back", disabled=(step == 0)):
    st.session_state.step_d28 = max(0, step - 1)
    st.rerun()
if c_next.button("Next ➡", disabled=(step == len(STEPS) - 1)):
    st.session_state.step_d28 = min(len(STEPS) - 1, step + 1)
    st.rerun()

st.caption(STANDARDS_CAPTION)
st.markdown(
    "<div style='text-align:center;color:#8a939c;font-size:11px;margin-top:18px;'>"
    "www.cognitivecloud.ai &middot; Developed by Xavier Honablue, M.Ed"
    "</div>",
    unsafe_allow_html=True,
)
