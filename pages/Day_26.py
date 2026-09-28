"""
Math 6 — Day 26: Refine Equivalent Ratios, Part 2 — Word Problems + i-Ready Online Lesson
Same structure as the Day 22–25 apps, by Xavier Honablue, M.Ed.

Aligned to i-Ready Classroom Mathematics, Grade 6, Unit 3 (Ratio Reasoning):
Lesson 13, Session 5 — Refine (Part 2 of an extended Refine). The second half of the
period is a 30-minute teacher-assigned i-Ready online lesson that corroborates the
Lesson 13 work (equivalent ratios, 6.RP.A.3a).

Run locally with:  streamlit run app.py
"""
PAGE_TITLE = "Day 26 — Refine: Word Problems + i-Ready"
PAGE_ICON = "💻"
DAY_LABEL = "Day 26"
ROADMAP_SUB = ("55-minute period — Lesson 13 Refine, Part 2 of 3 (25 min) + "
               "i-Ready online lesson (30 min)")
STEPS = [
    "1. Welcome Back",
    "2. Do-Now: Double Number Line",
    "3. Refine: Two-Step Word Problems",
    "4. Refine: Prove It Is (or Isn't) Equivalent",
    "5. Check-In Exit Ticket",
    "6. i-Ready Online Lesson (30 min)",
]
DEFAULT_NOTES = [{
    "date": "Day 25",
    "note": "Most students defaulted to the ratio table even when a double number line was "
            "faster. The Error Analysis step worked: 'multiplied only one quantity' was the "
            "error students recognized in their own work most. Today: word problems where the "
            "multiplier is hidden, then 30 minutes of i-Ready to corroborate.",
}]
STANDARDS_CAPTION = ("Standards in play: 6.RP.A.3 (use ratio reasoning to solve real-world "
                     "problems) · 6.RP.A.3a (tables of equivalent ratios; missing values) · "
                     "i-Ready online lesson aligned to 6.RP.A.3a.")

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
NOTES_FILE = os.path.join(os.path.dirname(__file__), "observer_notes_day26.json")


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


if "observer_notes_d26" not in st.session_state:
    st.session_state.observer_notes_d26 = load_notes()


def observer_log():
    st.markdown("---")
    st.markdown("#### 🔎 Observer Notes (running log)")
    st.caption("A running teacher log carried day to day. Add what you noticed in class today, "
               "then Save — copy it into tomorrow's app to keep the thread going.")
    for n in st.session_state.observer_notes_d26:
        st.markdown(f"**{n['date']}:** {n['note']}")
    new_note = st.text_area("Add a new observation:", key="new_observer_note")
    if st.button("Save observation"):
        if new_note.strip():
            st.session_state.observer_notes_d26.append(
                {"date": f"{DAY_LABEL} — {datetime.now().strftime('%Y-%m-%d')}",
                 "note": new_note.strip()})
            save_notes(st.session_state.observer_notes_d26)
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
    if "step_d26" not in st.session_state:
        st.session_state.step_d26 = 0
    for i, label in enumerate(STEPS):
        marker = "▶ " if i == st.session_state.step_d26 else ""
        if st.button(marker + label, key=f"nav_{i}", width="stretch"):
            st.session_state.step_d26 = i
            st.rerun()

step = st.session_state.step_d26
name = st.session_state.get("student_name", "") or "class"
st.markdown(f"## {STEPS[step]}")
st.progress((step + 1) / len(STEPS))


if step == 0:
    box("observer", "🔎 OBSERVER NOTE — carried from Day 25",
        f"<p style='margin:0'>{st.session_state.observer_notes_d26[0]['note']}</p>")
    read_aloud(
        "Two halves today. First half, with me: word problems where the multiplier is hiding and "
        "you have to dig it out. Second half, thirty minutes on i-Ready. The i-Ready lesson "
        "assigned to you covers the same thing we are doing right now — equivalent ratios. "
        "What you practice with me, you will see again on the screen."
    )
    box("tools", "Today's tools",
        "Model menu card &middot; notebook &middot; exit ticket half-sheet &middot; "
        "<b>Chromebook charged + headphones</b> for the i-Ready block.")
    box("literacy", "LEARNING TARGETS",
        "I can solve two-step equivalent-ratio word problems and show the multiplier.<br>"
        "I can prove whether two ratios are equivalent two different ways.<br>"
        "I can pass my assigned i-Ready lesson on equivalent ratios.")
    slides_ref("Grade 6 &rsaquo; Unit 3 &rsaquo; Lesson 13 &rsaquo; <b>Session 5 Refine</b>: "
               "Refine problems 4–6 today. In i-Ready, assign the Grade 6 online lesson on "
               "<b>equivalent ratios</b> (Ratios &amp; Proportional Relationships domain) "
               "before class so it is on top of every student's <i>My Assignments</i>.")
    box("iready", "⏱ PACING", "Steps 1–5: <b>25 minutes</b> &nbsp;·&nbsp; Step 6 i-Ready: "
        "<b>30 minutes</b>. Start the i-Ready timer no later than minute 25.")

elif step == 1:
    st.write("**Purpose (3 min):** Warm up the double number line from Day 22.")
    box("tools", "DO-NOW", "Fill a double number line for <b>4 : 5</b> up to 20 on the top line. "
        "Then: what goes with <b>14</b> on the top line?")
    pts = [(4 * k, 5 * k) for k in range(1, 6)]
    reveal = st.checkbox("Reveal the double number line", key="d26_dn")
    if reveal:
        st.pyplot(draw_double_number_line(pts + [(14, Fraction(35, 2))], "top", "bottom",
                                          highlight=14))
    check_answer("What goes with 14?", Fraction(35, 2), "d26_do",
                 "14 is halfway between 12 and 16. Halfway between 15 and 20 is…",
                 success="Correct — 17½. 14 ÷ 4 = 3½ and 5 × 3½ = 17½.")

elif step == 2:
    st.write("**Refine (8 min):** The multiplier is hiding. Find it first, then scale.")
    read_aloud("Read the question twice. Circle the two quantities in the ratio. Box the number "
               "you are scaling to. That boxed number, divided by its partner in the ratio, is "
               "your multiplier.")
    probs = [
        ("A school orders <b>3 buses for every 120 students</b>. 280 students are going on the "
         "trip. How many buses? (Buses come whole.)", Fraction(7),
         "280 ÷ 120 = 2⅓. 3 × 2⅓ = 7 buses. Or go through 1 bus : 40 students."),
        ("A trail mix uses <b>2 cups nuts : 3 cups pretzels</b>. Jada planned for <b>12 cups of pretzels</b>, "
         "then switched to <b>15 cups of pretzels</b>. How many <i>more</i> cups of nuts does she need?",
         Fraction(2), "12 cups pretzels → 8 nuts; 15 cups pretzels → 10 nuts. 10 − 8 = 2 cups more."),
        ("A runner runs <b>5 miles in 40 minutes</b>. At the same rate, how many minutes for "
         "<b>8 miles</b>?", Fraction(64),
         "Go through 1 mile : 8 minutes, then × 8 = 64 minutes."),
    ]
    for i, (q, ans, fix) in enumerate(probs):
        box("existing", f"PROBLEM {i + 1}", q)
        check_answer("Answer:", ans, f"d26_wp{i}", "Find the multiplier first. " + fix.split(".")[0] + ".",
                     success="Correct. " + fix)
    ask_the_class("In Problem 2, what was the SECOND step after you scaled the ratio?")

elif step == 3:
    st.write("**Refine (7 min):** Prove it two ways — one with a model, one with numbers.")
    pairs = [
        ("6 : 10", (6, 10), "9 : 15", (9, 15)),
        ("4 : 3", (4, 3), "10 : 9", (10, 9)),
        ("2½ : 1", (Fraction(5, 2), 1), "15 : 6", (15, 6)),
    ]
    for i, (l1, r1, l2, r2) in enumerate(pairs):
        c1, c2 = st.columns([1.2, 1])
        with c1:
            pick = st.radio(f"**{i + 1}.** Is {l1} equivalent to {l2}?", ["Yes", "No"],
                            index=None, horizontal=True, key=f"d26_eq{i}")
        with c2:
            if pick:
                truth = equivalent(r1, r2)
                if (pick == "Yes") == truth:
                    st.success(f"{'Yes' if truth else 'No'}. "
                               f"{mixed(r1[0])} × {mixed(r2[1])} = {mixed(r1[0] * r2[1])}; "
                               f"{mixed(r1[1])} × {mixed(r2[0])} = {mixed(r1[1] * r2[0])}.")
                else:
                    st.error("Test it: divide each ratio down to its simplest form, or plot both.")
    series = [("6 : 10", NAVY, [(6, 10), (9, 15)]), ("4 : 3 vs 10 : 9", RED, [(4, 3), (10, 9)])]
    if st.checkbox("Show pairs 1 and 2 on a graph", key="d26_g"):
        st.pyplot(draw_ratio_graph(series, "x", "y", xmax=12, ymax=17, figsize=(5.6, 3.8)))
        st.caption("Pair 1 lands on one line through (0, 0). Pair 2 does not — the red segment "
                   "misses the origin.")
    ask_the_class("Which proof would convince a skeptic faster: the graph or the numbers?")

elif step == 4:
    st.write("**Check-In (5 min):** This tells me who I pull into my small group during i-Ready.")
    box("existing", "EXIT TICKET",
        "A punch recipe uses <b>3 cups juice for every 2 cups soda</b>. (a) How much soda for "
        "<b>7½ cups juice</b>? (b) Is <b>9 cups juice : 5 cups soda</b> the same recipe? "
        "Prove it.")
    ok1 = check_answer("(a) Cups of soda:", 5, "d26_x1", "7½ ÷ 3 = 2½. 2 × 2½ = ?")
    p = st.radio("(b) Same recipe?", ["Yes", "No"], index=None, horizontal=True, key="d26_x2")
    if p:
        (st.success if p == "No" else st.error)(
            "No — 3 : 2 × 3 = 9 : 6, not 9 : 5. Cross products 3 × 5 = 15, 2 × 9 = 18.")
    box("observer", "👩🏾‍🏫 TEACHER MOVE",
        "Sort the half-sheets while students log in. Anyone who missed (a) or said 'Yes' on (b) "
        "is in the first small group during the i-Ready block.")

elif step == 5:
    iready_block(
        "d26",
        "Grade 6 · Ratios &amp; Proportional Relationships — <b>equivalent ratios</b> "
        "(ratio tables and double number lines, 6.RP.A.3a).",
        "The online lesson asks students to complete ratio tables, find missing values, and "
        "decide which ratios are equivalent — the same moves as today's Refine. Listen for "
        "students saying the multiplier out loud. Expect the 'add instead of multiply' error "
        "on the first missing-value item.",
        "Pull 4–6 students from the exit-ticket sort. Use the i-Ready <b>Tools for Instruction</b> "
        "activity for equivalent ratios: build 3 : 2 with two-color counters, copy it 2 and 3 "
        "times, record each copy in a ratio table, then redo exit-ticket (a) together. Release "
        "them to their i-Ready lesson with 15 minutes left.")
    observer_log()


st.markdown("---")
c_back, c_next = st.columns([1, 1])
if c_back.button("⬅ Back", disabled=(step == 0)):
    st.session_state.step_d26 = max(0, step - 1)
    st.rerun()
if c_next.button("Next ➡", disabled=(step == len(STEPS) - 1)):
    st.session_state.step_d26 = min(len(STEPS) - 1, step + 1)
    st.rerun()

st.caption(STANDARDS_CAPTION)
st.markdown(
    "<div style='text-align:center;color:#8a939c;font-size:11px;margin-top:18px;'>"
    "www.cognitivecloud.ai &middot; Developed by Xavier Honablue, M.Ed"
    "</div>",
    unsafe_allow_html=True,
)
