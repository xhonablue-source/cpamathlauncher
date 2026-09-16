import random

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import streamlit as st

# ============================================================
# CHANDLER PARK ACADEMY — DAY FIVE (55 MINUTES)
# "Area Is Multiplication"
# i-Ready Classroom Mathematics Unit 1 · Lesson 1 · Session 1
# Standalone version (no _common.py / launcher dependency)
# ============================================================

NAVY = "#1F3864"
GOLD = "#B08D57"
CREAM = "#F5F1E8"
TENS = "#D6E2F3"
ONES = "#F6E3C6"
BOTH = "#FFF0B3"


def inject_css():
    st.markdown(
        f"""
        <style>
        .stApp {{ background-color: {CREAM}; }}
        .big-title {{ font-size: 2.6rem; font-weight: 800; color: {NAVY}; line-height: 1.1; margin: 0.2rem 0 0.4rem 0; }}
        .sub-title {{ font-size: 1.4rem; color: #444; margin-bottom: 1rem; }}
        .banner {{ background-color: {NAVY}; color: white; padding: 0.7rem 1.3rem; border-radius: 10px;
                   font-weight: 700; font-size: 1.15rem; margin-bottom: 1rem; }}
        div[data-testid="stMarkdownContainer"] p {{ font-size: 1.15rem; line-height: 1.6; }}
        .readaloud-box {{ background-color: #FFFFFF; border: 3px solid {NAVY}; border-radius: 10px;
                          padding: 1.2rem 1.5rem; margin: 0.8rem 0 1.2rem 0; font-size: 1.25rem; line-height: 1.6; }}
        .readaloud-label {{ display: inline-block; background-color: {NAVY}; color: white; font-weight: 800;
                            font-size: 0.95rem; padding: 0.25rem 0.8rem; border-radius: 999px; margin-bottom: 0.6rem; }}
        .station-card {{ background-color: #FFFFFF; border: 2px solid {GOLD}; border-radius: 12px;
                         padding: 1rem 1.2rem; margin-bottom: 0.8rem; font-size: 1.1rem; }}
        .shape-tag {{ display: inline-block; background-color: {GOLD}; color: white; font-weight: 800;
                      font-size: 1rem; padding: 0.2rem 0.9rem; border-radius: 999px; margin-bottom: 0.5rem; }}
        .ican-box {{ background-color: #FFFFFF; border-left: 6px solid {GOLD}; padding: 0.7rem 1rem;
                     margin: 0.5rem 0; font-size: 1.1rem; border-radius: 0 8px 8px 0; }}
        .ican-tag {{ display: inline-block; background-color: {NAVY}; color: white; font-weight: 800;
                     font-size: 0.85rem; padding: 0.15rem 0.6rem; border-radius: 999px; margin-right: 0.6rem; }}
        .reflect-box {{ background-color: #FFF8E6; border: 2px dashed {GOLD}; border-radius: 10px;
                        padding: 1rem 1.3rem; font-size: 1.15rem; margin-top: 0.8rem; }}
        .timer {{ font-size: 1rem; color: {GOLD}; font-weight: 700; }}
        .credit {{ text-align: center; color: #666; font-size: 0.95rem; margin-top: 2rem; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def banner(text):
    st.markdown(f'<div class="banner">{text}</div>', unsafe_allow_html=True)


def read_aloud(text):
    st.markdown(
        f"""
        <div class="readaloud-box">
        <span class="readaloud-label">🔊 READ ALOUD</span><br>
        "{text}"
        </div>
        """,
        unsafe_allow_html=True,
    )


def attempt(key):
    """Count attempts on a check button; returns the new attempt number."""
    k = f"attempts_{key}"
    st.session_state[k] = st.session_state.get(k, 0) + 1
    return st.session_state[k]


def explain(title, lines):
    body = "<br>".join(lines)
    st.markdown(
        f'''<div class="reflect-box"><b>💡 {title}</b><br>{body}</div>''',
        unsafe_allow_html=True,
    )


def timer(text):
    st.markdown(f'<div class="timer">⏱ {text}</div>', unsafe_allow_html=True)


def split_at(n):
    """Return (tens_part, ones_part) for the split used on graph paper."""
    if n > 20:
        return 20, n - 20
    if n > 10:
        return 10, n - 10
    return n, 0


def draw_rectangle(base, height, show_pieces=True, show_labels=True):
    """Draw a base x height rectangle on a grid, split at the tens."""
    fig, ax = plt.subplots(figsize=(7, 4.4), dpi=110)
    fig.patch.set_facecolor("white")
    bt, bo = split_at(base)
    ht, ho = split_at(height)
    if show_pieces and bo and ho:
        ax.add_patch(Rectangle((0, 0), bt, ht, color=TENS))
        ax.add_patch(Rectangle((bt, 0), bo, ht, color=ONES))
        ax.add_patch(Rectangle((0, ht), bt, ho, color=ONES))
        ax.add_patch(Rectangle((bt, ht), bo, ho, color=BOTH))
        ax.plot([bt, bt], [0, height], color=NAVY, ls="--", lw=1.6)
        ax.plot([0, base], [ht, ht], color=NAVY, ls="--", lw=1.6)
        if show_labels:
            ax.text(bt / 2, ht / 2, f"{ht} × {bt}\n= {ht * bt}", ha="center", va="center", fontsize=13, weight="bold", color=NAVY)
            ax.text(bt + bo / 2, ht / 2, f"{ht}×{bo}\n={ht * bo}", ha="center", va="center", fontsize=10, weight="bold", color=NAVY)
            ax.text(bt / 2, ht + ho / 2, f"{ho}×{bt}={ho * bt}", ha="center", va="center", fontsize=11, weight="bold", color=NAVY)
            ax.text(bt + bo / 2, ht + ho / 2, f"{ho * bo}", ha="center", va="center", fontsize=10, weight="bold", color=NAVY)
    elif show_pieces and (bo or ho):
        # only one side needs a split
        if bo:
            ax.add_patch(Rectangle((0, 0), bt, height, color=TENS))
            ax.add_patch(Rectangle((bt, 0), bo, height, color=ONES))
            ax.plot([bt, bt], [0, height], color=NAVY, ls="--", lw=1.6)
            if show_labels:
                ax.text(bt / 2, height / 2, f"{height} × {bt} = {height * bt}", ha="center", va="center", fontsize=12, weight="bold", color=NAVY)
                ax.text(bt + bo / 2, height / 2, f"{height}×{bo}\n={height * bo}", ha="center", va="center", fontsize=10, weight="bold", color=NAVY)
        else:
            ax.add_patch(Rectangle((0, 0), base, ht, color=TENS))
            ax.add_patch(Rectangle((0, ht), base, ho, color=ONES))
            ax.plot([0, base], [ht, ht], color=NAVY, ls="--", lw=1.6)
            if show_labels:
                ax.text(base / 2, ht / 2, f"{ht} × {base} = {ht * base}", ha="center", va="center", fontsize=12, weight="bold", color=NAVY)
                ax.text(base / 2, ht + ho / 2, f"{ho}×{base}={ho * base}", ha="center", va="center", fontsize=10, weight="bold", color=NAVY)
    else:
        ax.add_patch(Rectangle((0, 0), base, height, color=TENS))
    # grid
    for x in range(base + 1):
        ax.plot([x, x], [0, height], color="#BBB", lw=0.5, zorder=1)
    for y in range(height + 1):
        ax.plot([0, base], [y, y], color="#BBB", lw=0.5, zorder=1)
    ax.add_patch(Rectangle((0, 0), base, height, fill=False, lw=2.2, color="#222"))
    ax.text(base / 2, -0.9, f"base = {base}", ha="center", va="top", fontsize=12, color="#333")
    ax.text(-0.5, height / 2, f"height = {height}", ha="right", va="center", fontsize=12, color="#333", rotation=90)
    ax.set_xlim(-2.5, base + 0.5)
    ax.set_ylim(-2, height + 0.5)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.tight_layout()
    return fig


# ------------------------------------------------------------
# Page setup
# ------------------------------------------------------------
st.set_page_config(page_title="Day 5 — Area Is Multiplication", page_icon="📐", layout="wide")
inject_css()
banner("Grade 6 Mathematics | Day Five | 55-Minute Period")

SLIDES = [
    "Welcome Back",
    "Facts Sprint",
    "Try It: Count It Fast",
    "Explore: Target Dimensions",
    "Discuss It & Connect It",
    "Engage / Explore / Enrich Boards",
    "Apply It: Exit Ticket",
    "Journal & Keep-or-Rid",
    "What You Just Did",
]

if "day5_slide" not in st.session_state:
    st.session_state.day5_slide = 0
if "sprint" not in st.session_state:
    random.seed()
    st.session_state.sprint = [(random.choice([3, 4, 6, 7]), random.randint(3, 9)) for _ in range(10)]
if "throws" not in st.session_state:
    st.session_state.throws = []
if "keep_votes" not in st.session_state:
    st.session_state.keep_votes = {"Keep": 0, "Rid": 0}


def go_to(i):
    st.session_state.day5_slide = i


def go_next():
    st.session_state.day5_slide = min(st.session_state.day5_slide + 1, len(SLIDES) - 1)


def go_prev():
    st.session_state.day5_slide = max(st.session_state.day5_slide - 1, 0)


# ------------------------------------------------------------
# Sidebar: student sign-in (Panther-style) + roadmap
# ------------------------------------------------------------
with st.sidebar:
    st.markdown(f"<h3 style='color:{NAVY};'>Sign In</h3>", unsafe_allow_html=True)
    name = st.text_input("Your name:", key="student_name")
    avatar = st.selectbox(
        "Choose your shape avatar:",
        ["🟦 Rectangle", "🔷 Parallelogram", "🔺 Triangle", "⬡ Hexagon", "🛑 Octagon"],
        key="avatar",
    )
    mode = st.selectbox(
        "Pick your learning mode:",
        ["🎯 Focus Champ", "🚀 Growth Mode", "🛠️ Problem Solver", "📊 Data Boss", "🧠 Brain Builder"],
        key="mode",
    )
    st.markdown("---")
    st.markdown(f"<h3 style='color:{NAVY};'>Day 5 Roadmap</h3>", unsafe_allow_html=True)
    st.caption("55-minute period — Area Is Multiplication")
    for i, label in enumerate(SLIDES):
        prefix = "▶ " if i == st.session_state.day5_slide else "　"
        st.button(f"{prefix}{i + 1}. {label}", key=f"d5nav_{i}", on_click=go_to, args=(i,), use_container_width=True)
    st.markdown("---")
    st.caption("i-Ready Classroom Mathematics · Unit 1 · Lesson 1 · Session 1")
    st.caption("Standards: 6.G.A.1 · 6.EE.A.2c · 4.NBT.B.5 · 3.MD.C.7 · 3.OA.C.7")

slide = st.session_state.day5_slide
st.markdown(f'<div class="big-title">{SLIDES[slide]}</div>', unsafe_allow_html=True)
st.progress((slide + 1) / len(SLIDES))

# ============================================================
# SLIDE 0 — WELCOME BACK
# ============================================================
if slide == 0:
    st.markdown('<div class="sub-title">Day 5 · Area Is Multiplication</div>', unsafe_allow_html=True)
    timer("0:00 – 0:03")
    if name:
        st.success(f"Welcome back, {name} the {avatar}! You're in {mode} today. Let's begin Day 5.")
    else:
        st.info("Type your name in the sidebar and pick a shape avatar to sign in.")
    read_aloud(
        "On Day 1 you drew shapes on graph paper. On Day 4 you tested the Engage / Explore / Enrich boards. "
        "Today those two things meet. You are going to find the area of rectangles — and you are going to "
        "discover that area IS multiplication. By the end of class you will multiply numbers like 14 times 23 "
        "without a calculator, just by drawing."
    )
    st.markdown(
        """
        <div class="station-card">
        <span class="shape-tag">Today's tools</span><br>
        Graph paper and colored pencils · the Nerf dart board · your journal · Chromebook for the boards (IXL) · exit ticket.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="station-card">
        <span class="shape-tag">Dart board rules</span><br>
        Darts move only teacher → thrower → teacher. One thrower per team at the line. A miss gets one re-throw,
        then your team draws a number card. If the rules break, the card deck replaces the board for the rest of class.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# SLIDE 1 — FACTS SPRINT
# ============================================================
elif slide == 1:
    timer("0:03 – 0:08 · Journal + Human Bar Graph")
    read_aloud(
        "Ten facts. Answer them in your journal, then type them here to check. When you have your score, "
        "stand behind that number on the Human Bar Graph line at the front. This is a 5-minute routine "
        "we will do every day from now on."
    )
    cols = st.columns(5)
    answers = []
    for i, (a, b) in enumerate(st.session_state.sprint):
        with cols[i % 5]:
            answers.append(st.number_input(f"{a} × {b} =", min_value=0, max_value=200, step=1, key=f"sprint_{i}"))
    c1, c2 = st.columns([1, 3])
    with c1:
        check = st.button("Check my sprint", key="sprint_check", use_container_width=True)
    with c2:
        if st.button("New set of 10", key="sprint_new", use_container_width=True):
            st.session_state.sprint = [(random.choice([3, 4, 6, 7]), random.randint(3, 9)) for _ in range(10)]
            for i in range(10):
                st.session_state.pop(f"sprint_{i}", None)
            st.rerun()
    if check:
        score = sum(1 for (a, b), ans in zip(st.session_state.sprint, answers) if a * b == ans)
        st.session_state.sprint_score = score
        n = attempt("sprint")
        if score == 10:
            st.balloons()
        if score >= 9:
            st.success(f"{score}/10 — facts are solid. Stand behind {score} on the bar graph.")
        elif score >= 6:
            st.warning(f"{score}/10 — almost there. Stand behind {score} on the bar graph.")
        else:
            st.error(f"{score}/10 — no problem, that's what the Engage board is for today. Stand behind {score}.")
        missed = [(a, b) for (a, b), ans in zip(st.session_state.sprint, answers) if a * b != ans]
        if missed:
            st.markdown("**Sketch one you missed as a dot array on graph paper:** " + ", ".join(f"{a} × {b}" for a, b in missed[:3]))
            if n >= 2:
                explain(
                    "Redo help — count by rows",
                    [f"{a} × {b}: draw {a} rows of {b} dots. Skip-count {b}, {2*b}, {3*b}… {a} times → <b>{a*b}</b>" for a, b in missed[:4]],
                )
            else:
                st.info("Fix the ones you missed and check again — the second check shows a worked explanation.")

# ============================================================
# SLIDE 2 — TRY IT
# ============================================================
elif slide == 2:
    timer("0:08 – 0:13 · Engage · i-Ready Try It")
    read_aloud(
        "How many squares are inside this rectangle? Find it a slow way AND a fast way. "
        "Two minutes silent. Then one minute with your partner."
    )
    left, right = st.columns([3, 2])
    with left:
        st.pyplot(draw_rectangle(8, 6, show_pieces=False), use_container_width=True)
    with right:
        guess = st.number_input("How many squares are inside?", min_value=0, max_value=200, step=1, key="tryit")
        if st.button("Check", key="tryit_check"):
            n = attempt("tryit")
            if guess == 48:
                st.balloons()
                st.success("48 square units. 6 rows of 8 — that's 6 × 8.")
            else:
                st.error("Not yet. Count one row, then count how many rows.")
                if n >= 2:
                    explain(
                        "Redo help",
                        ["One row across the bottom has <b>8</b> squares.",
                         "Stack <b>6</b> of those rows going up.",
                         "6 rows × 8 squares = <b>48 square units</b>. That's why area = rows × columns."],
                    )
        st.markdown(
            """
            <div class="reflect-box">
            <b>The big idea:</b> Area is the number of unit squares inside. Rows × columns counts them for you.<br><br>
            <b>A = b × h</b> &nbsp;— <i>b</i> and <i>h</i> are just the two side lengths.
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.caption("Standards in play: 3.MD.C.7 (relate area to multiplication) · 6.EE.A.2c (a formula is an expression you evaluate).")

# ============================================================
# SLIDE 3 — EXPLORE: TARGET DIMENSIONS
# ============================================================
elif slide == 3:
    timer("0:13 – 0:28 · Explore · teams of 5–6 · goal: 3 rectangles per team")
    read_aloud(
        "One thrower per team. First dart is your BASE, second dart is your HEIGHT. Bullseye counts as 25. "
        "Draw that rectangle on graph paper. Split each side at 10. Color the four pieces. Find each piece, add them up, "
        "and write the total inside your rectangle with the words 'square units'."
    )
    st.markdown(
        """
        <div class="station-card">
        <span class="shape-tag">Teacher model round</span>
        Base 23, height 14. Watch the split, then your team runs its own.
        </div>
        """,
        unsafe_allow_html=True,
    )
    c1, c2, c3 = st.columns([1, 1, 2])
    with c1:
        base = st.number_input("Base (dart 1)", min_value=1, max_value=25, value=23, step=1, key="base")
    with c2:
        height = st.number_input("Height (dart 2)", min_value=1, max_value=25, value=14, step=1, key="height")
    with c3:
        st.write("")
        if st.button("🎯 Simulate two throws (no board today)", key="throw", use_container_width=True):
            b = random.choice(list(range(1, 21)) + [25])
            h = random.choice(list(range(1, 21)) + [25])
            st.session_state.base = b
            st.session_state.height = h
            st.rerun()
    show = st.toggle("Show the pieces (teacher reveal)", value=False, key="reveal_pieces")
    st.pyplot(draw_rectangle(int(base), int(height), show_pieces=show, show_labels=show), use_container_width=True)

    st.markdown("**Your team's four pieces** (type what your drawing shows):")
    bt, bo = split_at(int(base))
    ht, ho = split_at(int(height))
    pieces = []
    labels = [(ht, bt), (ht, bo), (ho, bt), (ho, bo)]
    pc = st.columns(4)
    for i, (r, c) in enumerate(labels):
        with pc[i]:
            if r and c:
                pieces.append(st.number_input(f"{r} × {c} =", min_value=0, max_value=700, step=1, key=f"piece_{i}"))
            else:
                pieces.append(0)
                st.caption("no piece here")
    total = st.number_input("Total area (square units) =", min_value=0, max_value=700, step=1, key="total")
    if st.button("Check our rectangle", key="check_rect", use_container_width=True):
        expected = [r * c for r, c in labels]
        ok_pieces = all(p == e for p, e in zip(pieces, expected) if e)
        n = attempt("rect")
        if ok_pieces and total == int(base) * int(height):
            st.balloons()
            st.success(f"Correct! {base} × {height} = {' + '.join(str(e) for e in expected if e)} = {int(base) * int(height)} square units.")
            st.session_state.throws.append((int(base), int(height), int(base) * int(height)))
        elif ok_pieces:
            st.warning("Pieces are right — check your addition for the total.")
            if n >= 2:
                explain("Redo help — the addition", [f"{' + '.join(str(e) for e in expected if e)} = <b>{int(base) * int(height)}</b>. Add the two big pieces first, then the small ones."])
        else:
            st.error("One or more pieces is off. Point to that piece on your drawing and count its rows.")
            if n >= 2:
                wrong = [(r, c, p) for (r, c), p in zip(labels, pieces) if r and c and p != r * c]
                explain(
                    "Redo help — one piece at a time",
                    [f"The {r} × {c} piece: {r} rows of {c}. Skip-count by {c} → <b>{r*c}</b> (you wrote {p})." for r, c, p in wrong]
                    + [f"Then add every piece: {' + '.join(str(e) for e in expected if e)} = <b>{int(base) * int(height)}</b>."],
                )
            else:
                st.info("Fix it and check again — the second check walks through each piece.")
    if st.session_state.throws:
        st.markdown("**Team record**")
        st.table([{"Base": b, "Height": h, "Area (sq units)": a} for b, h, a in st.session_state.throws])
    st.caption("Teacher question while circulating: “Show me where 10 × 3 is on your picture.” Students who can't point to it → Engage board.")

# ============================================================
# SLIDE 4 — DISCUSS IT & CONNECT IT
# ============================================================
elif slide == 4:
    timer("0:28 – 0:38 · Discuss It · Connect It · i-Ready Session 1")
    read_aloud(
        "Two teams put a rectangle under the camera. Class — not the presenters — answer: "
        "Where is each number in the expression on the picture? Which piece was hardest? Why did splitting at 10 help?"
    )
    left, right = st.columns([3, 2])
    with left:
        st.pyplot(draw_rectangle(23, 14, show_pieces=True), use_container_width=True)
    with right:
        st.markdown(
            f"""
            <div class="station-card">
            <span class="shape-tag">Connect It</span><br>
            (10 + 4) × (20 + 3)<br>
            = 10×20 + 10×3 + 4×20 + 4×3<br>
            = 200 + 30 + 80 + 12<br>
            = <b>322 square units</b><br><br>
            <b>A = b × h</b> → A = 23 × 14 = 322
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("**Build the expression yourself:**")
        b = st.number_input("base", 1, 25, 23, key="ci_b")
        h = st.number_input("height", 1, 25, 14, key="ci_h")
        bt, bo = split_at(int(b))
        ht, ho = split_at(int(h))
        terms = [f"{r}×{c}" for r, c in [(ht, bt), (ht, bo), (ho, bt), (ho, bo)] if r and c]
        vals = [r * c for r, c in [(ht, bt), (ht, bo), (ho, bt), (ho, bo)] if r and c]
        st.code(f"{b} × {h} = {' + '.join(terms)}\n      = {' + '.join(str(v) for v in vals)}\n      = {int(b) * int(h)}")
    st.markdown(
        """
        <div class="reflect-box">
        <b>Skit (90 seconds, Day 3 style):</b> the <i>Counter</i> tries to count 322 squares one at a time.
        The <i>Splitter</i> finishes in four steps. Then the class votes which method to KEEP.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption("Don't name the distributive property unless a student does — call it 'the split'. It gets its name in i-Ready Lesson 19.")

# ============================================================
# SLIDE 5 — BOARDS
# ============================================================
elif slide == 5:
    timer("0:38 – 0:48 · Engage / Explore / Enrich rotation · Day 4 model")
    read_aloud(
        "Your board is based on what I saw during Target Dimensions, not on anything from before today. "
        "Engage sits with me. Explore and Enrich work independently on paper first, then IXL."
    )
    e1, e2, e3 = st.columns(3)
    with e1:
        st.markdown(
            """
            <div class="station-card">
            <span class="shape-tag">Engage · with teacher</span><br>
            <i>Couldn't point to 10 × 3, or sprint under 6/10.</i><br><br>
            1. Build 3 × 7, 4 × 6, 6 × 8 as arrays. Count by rows out loud.<br>
            2. Together: 12 × 6, split at 10 only (two pieces).<br>
            3. IXL <b>CQZ</b> — Tile a rectangle and find the area.<br>
            4. Names go on this week's 1-on-1 tutoring list.
            </div>
            """,
            unsafe_allow_html=True,
        )
    with e2:
        st.markdown(
            """
            <div class="station-card">
            <span class="shape-tag">Explore · independent</span><br>
            <i>Got the split with help; facts mostly there.</i><br><br>
            1. Three rectangles from the card deck, four-piece split.<br>
            2. Backwards problem: area 96, base 8 — find the height.<br>
            3. IXL <b>8PN</b> — Area of rectangles and squares.
            </div>
            """,
            unsafe_allow_html=True,
        )
    with e3:
        st.markdown(
            """
            <div class="station-card">
            <span class="shape-tag">Enrich · previews Day 6</span><br>
            <i>Fluent on the split, finished early.</i><br><br>
            1. Cut a 6 × 4 parallelogram from graph paper. Slice a right triangle off one end and slide it to the other. What rectangle appears?<br>
            2. Two more parallelograms, then write the rule in your own words.<br>
            3. IXL <b>ND5</b> Identify parallelograms → <b>QMU</b> Understanding area of a parallelogram.
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("[Open the IXL skill plan for i-Ready Grade 6 (all codes above are on page 1)](https://www.ixl.com/math/skill-plans/i-ready-classroom-mathematics-2024-grade-6)")
    st.markdown("**Board self-check** — which board are you on?")
    board = st.radio("", ["Engage", "Explore", "Enrich"], horizontal=True, key="board_pick", label_visibility="collapsed")
    st.info(f"{name or 'You'} → **{board}** board. Grab your materials and go.")

# ============================================================
# SLIDE 6 — APPLY IT / EXIT TICKET
# ============================================================
elif slide == 6:
    timer("0:48 – 0:53 · Apply It · silent · draw your own rectangle if you need one")
    read_aloud("Exit ticket. Silent. You may draw a rectangle on graph paper for any problem. Hand in the paper copy before journaling.")
    q1 = st.number_input("1. A rectangle is 7 units by 9 units. Area = ?", 0, 500, step=1, key="et1")
    q2 = st.number_input("2. Base 24, height 13. Split at the tens and find the total area = ?", 0, 500, step=1, key="et2")
    q3 = st.number_input("3. Area is 96 square units and the base is 8. Height = ?", 0, 500, step=1, key="et3")
    enrich = st.checkbox("I'm on the Enrich board — show problem 4", key="et_enrich")
    q4 = None
    if enrich:
        q4 = st.number_input("4. A parallelogram has base 6 and height 4. Area = ?", 0, 500, step=1, key="et4")
    if st.button("Submit exit ticket", key="et_submit", use_container_width=True):
        n = attempt("exit")
        results = [
            (q1 == 63, "63", ["7 rows of 9 squares.", "Skip-count 9, 18, 27, 36, 45, 54, <b>63</b>."]),
            (q2 == 312, "312", ["Split 24 → 20 + 4 and 13 → 10 + 3.", "10×20 = 200, 10×4 = 40, 3×20 = 60, 3×4 = 12.", "200 + 40 + 60 + 12 = <b>312</b>."]),
            (q3 == 12, "12", ["Area = base × height, so 96 = 8 × ?", "8 × 10 = 80, 8 × 12 = 96 → height = <b>12</b>."]),
        ]
        if enrich:
            results.append((q4 == 24, "24", ["Slice the triangle off one end and slide it over.", "It becomes a 6 × 4 rectangle = <b>24</b>."]))
        score = sum(1 for ok, _, _ in results if ok)
        for i, (ok, ans, why) in enumerate(results, start=1):
            if ok:
                st.success(f"Problem {i}: ✔ {ans}")
            else:
                st.error(f"Problem {i}: ✘")
                if n >= 2:
                    explain(f"Problem {i} — how to get it", why)
        if score == len(results):
            st.balloons()
        elif n == 1:
            st.info("Fix any ✘ and submit again — the second submit shows how each one works.")
        st.markdown(f"**{name or 'Student'}: {score} / {len(results)}**")
        if q2 != 312:
            st.warning("Problem 2 is the one that matters for tomorrow. Draw 24 × 13, split it, and try again in your journal.")

# ============================================================
# SLIDE 7 — JOURNAL & KEEP-OR-RID
# ============================================================
elif slide == 7:
    timer("0:53 – 0:55 · Close")
    read_aloud("Journal: draw a rectangle that shows 12 × 15. Where would you cut it? Then vote: keep the dart board for Day 6, or rid it?")
    j = st.text_area("Journal (optional — write it on paper too):", height=120, key="journal")
    if j.strip():
        st.success("Journaled. Hand-drawn version goes in your notebook.")
    st.markdown("**Keep-or-Rid vote — the dart board**")
    v1, v2 = st.columns(2)
    with v1:
        if st.button("👍 Keep it", key="vote_keep", use_container_width=True):
            st.session_state.keep_votes["Keep"] += 1
    with v2:
        if st.button("👎 Rid it", key="vote_rid", use_container_width=True):
            st.session_state.keep_votes["Rid"] += 1
    k, r = st.session_state.keep_votes["Keep"], st.session_state.keep_votes["Rid"]
    if k + r:
        fig, ax = plt.subplots(figsize=(4.5, 2.6), dpi=110)
        bars = ax.bar(["Keep", "Rid"], [k, r], color=[GOLD, NAVY], width=0.5)
        for bar, v in zip(bars, [k, r]):
            ax.text(bar.get_x() + bar.get_width() / 2, v + 0.1, str(v), ha="center", fontsize=12, weight="bold")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_ylim(0, max(k, r) + 2)
        ax.set_title("Class vote — record this on the Day 2 data wall", fontsize=10, color=NAVY)
        plt.tight_layout()
        st.pyplot(fig, use_container_width=False)

# ============================================================
# SLIDE 8 — WHAT YOU JUST DID
# ============================================================
elif slide == 8:
    read_aloud(
        "Here is what you actually did today, in the words the State of Michigan uses. "
        "Copy the I-can statements into your journal and write one sentence of evidence for each."
    )
    icans = [
        ("AREA", "I can find the area of a rectangle by decomposing it into pieces and adding them. (6.G.A.1)"),
        ("FORMULA", "I can substitute numbers into A = b × h and evaluate it. (6.EE.A.2c)"),
        ("MULTIPLY", "I can multiply two two-digit numbers using an area model. (4.NBT.B.5)"),
        ("STRUCTURE", "I can split a rectangle at the tens on purpose because it makes the math easier. (MP.7)"),
        ("ARGUE", "I can explain where each number in an expression lives on a picture. (MP.3)"),
    ]
    for tag, text in icans:
        st.markdown(f'<div class="ican-box"><span class="ican-tag">{tag}</span>{text}</div>', unsafe_allow_html=True)
    st.caption(
        "Michigan K-12 Standards for Mathematics use the Common Core codes verbatim: "
        "6.G.A.1, 6.EE.A.2c (grade-level); 4.NBT.B.5, 3.MD.C.7, 3.OA.C.7 (repair); MP.3, MP.4, MP.7. "
        "i-Ready Classroom Mathematics Unit 1, Lesson 1, Session 1."
    )
    st.markdown(
        f"""
        <div class="reflect-box">
        You walked in unable to multiply 14 × 23. You walked out having done it by drawing a rectangle.
        <br><br><b>{name or 'Mathematician'}, that is what area is for.</b>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ------------------------------------------------------------
# Navigation
# ------------------------------------------------------------
st.write("")
st.write("")
nav1, nav2, nav3 = st.columns([1, 3, 1])
with nav1:
    st.button("⬅ Back", on_click=go_prev, disabled=(slide == 0), use_container_width=True, key="d5_back")
with nav3:
    st.button("Next ➡", on_click=go_next, disabled=(slide == len(SLIDES) - 1), use_container_width=True, key="d5_next")

st.markdown(
    '<div class="credit"><a href="https://www.cognitivecloud.ai">www.cognitivecloud.ai</a> · Developed by Xavier Honablue, M.Ed · Chandler Park Academy</div>',
    unsafe_allow_html=True,
)
