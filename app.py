import os
import streamlit as st

st.set_page_config(
    page_title="MathCraft CPA — Lesson Launcher",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded",
)

NAVY = "#1F3864"
GOLD = "#B08D57"
CREAM = "#F2EFE9"
MUTED = "#9C9284"
GREEN = "#3C8B5D"

st.markdown(
    f"""
    <style>
    .stApp {{ background-color: #FFFFFF; }}
    .block-container {{ padding-top: 2rem; padding-bottom: 3rem; max-width: 1200px; }}
    .mc-banner {{
        background: linear-gradient(135deg, {NAVY} 0%, #142544 100%);
        color: white;
        padding: 2.2rem 2.4rem;
        border-radius: 14px;
        margin-bottom: 1.8rem;
        border-bottom: 6px solid {GOLD};
    }}
    .mc-banner h1 {{ margin: 0; font-size: 2.6rem; letter-spacing: 0.5px; }}
    .mc-banner p {{ margin: 0.4rem 0 0 0; opacity: 0.9; font-size: 1.15rem; }}
    .big-title {{ color: {NAVY}; font-size: 2rem; font-weight: 800; margin-bottom: 0.3rem; }}
    .sub-title {{ color: {GOLD}; font-size: 1.1rem; font-weight: 700; margin-bottom: 1rem; }}
    /* ---- Uniform day cards ---- */
    .day-card {{
        background-color: {CREAM};
        border: 2px solid {GOLD};
        border-radius: 12px;
        padding: 1.4rem 1.5rem;
        margin-bottom: 1rem;
        height: 560px;
        display: flex;
        flex-direction: column;
    }}
    .day-pill {{
        display: inline-block;
        background-color: {NAVY};
        color: white;
        font-size: 0.75rem;
        font-weight: 700;
        padding: 0.15rem 0.7rem;
        border-radius: 999px;
        margin-bottom: 0.6rem;
        width: fit-content;
    }}
    .day-card h3 {{
        color: {NAVY};
        margin: 0 0 0.5rem 0;
        font-size: 1.2rem;
        line-height: 1.3;
        min-height: 3.1rem;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }}
    .day-card p {{
        margin: 0;
        font-size: 0.95rem;
        color: #3a3a3a;
        line-height: 1.4;
        flex: 1 1 auto;
        display: -webkit-box;
        -webkit-line-clamp: 5;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }}
    .day-card .btn-stack {{
        margin-top: 1rem;
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }}
    .link-button, .pdf-button, .worksheet-button, .hmwk-button {{
        display: block;
        box-sizing: border-box;
        text-align: center;
        border-radius: 8px;
        padding: 0.5rem 0.8rem;
        font-weight: 700;
        font-size: 0.92rem;
        text-decoration: none !important;
        transition: background-color 0.15s ease, color 0.15s ease;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        cursor: pointer;
    }}
    .link-button {{
        background-color: {NAVY};
        color: white !important;
        border: 2px solid {NAVY};
    }}
    .link-button:hover {{ background-color: #142544; border-color: #142544; }}
    .pdf-button {{
        background-color: white;
        color: {NAVY} !important;
        border: 2px solid {NAVY};
    }}
    .pdf-button:hover {{ background-color: {NAVY}; color: white !important; }}
    .pdf-button.disabled {{
        background-color: #ECEAE5;
        color: {MUTED} !important;
        border: 2px dashed #C9C2B6;
        cursor: not-allowed;
        pointer-events: none;
    }}
    .worksheet-button {{
        background-color: white;
        color: {GREEN} !important;
        border: 2px solid {GREEN};
    }}
    .worksheet-button:hover {{ background-color: {GREEN}; color: white !important; }}
    .hmwk-button {{
        background-color: {GOLD};
        color: white !important;
        border: 2px solid {GOLD};
    }}
    .hmwk-button:hover {{ background-color: #96754A; border-color: #96754A; }}
    .hmwk-note {{
        display: block;
        font-size: 0.72rem;
        color: {MUTED};
        margin-top: 0.25rem;
        line-height: 1.3;
        white-space: normal;
    }}
    .calendar-note {{
        background-color: #FFF4E5;
        border-left: 6px solid {GOLD};
        border-radius: 8px;
        padding: 1rem 1.3rem;
        margin-bottom: 1rem;
        color: #7a5a1e;
        font-size: 0.95rem;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="mc-banner">
        <h1>🧮 MathCraft CPA</h1>
        <p>Chandler Park Academy · Grade 6 Mathematics · Daily Lesson Launcher</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="big-title">Welcome, Families and Students!</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Professor Xavier Honablue, M.Ed.</div>', unsafe_allow_html=True)
st.write(
    "Click any day below to open that day's full lesson, or open the Observer Guide PDF to view it "
    "right in your browser. Use the school calendar underneath to match each lesson day to its actual "
    "calendar date."
)

st.markdown("---")
st.markdown("### 📅 Lessons by Day")

DAYS = [
    dict(
        label="Day 1",
        title="What Is Math?",
        desc="Observe a real object, then simulate an imagined object using geometric shapes on graph paper.",
        page="https://cpa-math6-day1.streamlit.app/",
        guide_file="Day1_Observer_Guide.pdf",
    ),
    dict(
        label="Day 2",
        title="Getting to Know You: Data Reveal",
        desc="A real class-data opener (12 of 42), a confounding-variables talk, and five shape survey stations.",
        page="https://cpamathgrade6day2.streamlit.app/",
        guide_file="Day2_Observer_Guide.pdf",
    ),
    dict(
        label="Day 3",
        title="Hear From Us: Skits & Focus",
        desc="A Human Bar Graph, classroom-behavior skits, and a Keep-or-Rid vote — no drawing today.",
        page="https://cpamathgrade6day3.streamlit.app/",
        guide_file="Day3_Observer_Guide.pdf",
    ),
    dict(
        label="Day 4",
        title="Testing the Model",
        desc="First multi-board Engage/Explore/Enrich pilot with IXL.com, journaling, and 1-on-1 tutoring.",
        page="https://cpamathgrade6day4.streamlit.app/",
        guide_file="Day4_Observer_Guide.pdf",
    ),
    dict(
        label="Day 5",
        title="Area Is Multiplication",
        desc="First grade-level content day: rectangle area taught alongside two-digit multiplication, using a Nerf dart board to generate dimensions.",
        page="https://cpamath6day5.streamlit.app/",
        guide_file="Day5_Observer_Guide.pdf",
        worksheet_file="wksht.pdf",
        worksheet_label="Classwork Worksheet (wksht)",
        hmwk_url="https://www.ixl.com/math/grade-6/area-of-rectangles-and-squares",
        hmwk_label="HMWK: Earn 90% on GG.2 (IXL, 6th grade)",
    ),
    dict(
            label="Day 6",
            title="Area Unlocks the Missing Side",
            desc="Square vs. rectangle repair, then area runs in reverse: given the area and one side, find the missing side, and split an L-shaped floor into two rectangles.",
            page="https://cpamath6day6.streamlit.app/",
            guide_file="Day6_Observer_Guide.pdf",
            worksheet_file="Day6_wksht.pdf",
            worksheet_label="Classwork Worksheet (Day 6 wksht)",
            hmwk_url="https://www.ixl.com/math/grade-6/area-of-rectangles-and-squares",
            hmwk_label="HMWK: Earn 90% on GG.2 (IXL, 6th grade)",
    ),
    dict(
        label="Day 7",
        title="Area of Compound Rectangles",
        desc="Split an L-shaped floor into two rectangles and add, or enclose it in one rectangle and subtract the missing piece — then apply both moves to a trickier T-shape.",
        page="https://cpamath6day7.streamlit.app/",
        guide_file="Day7_Observer_Guide.pdf",
        worksheet_file="Day7_wksht.pdf",
        worksheet_label="Classwork Worksheet (Day 7 wksht)",
        hmwk_url="https://www.ixl.com/math/grade-6/area-of-compound-figures",
        hmwk_label="HMWK: Earn 90% on GG.11 (IXL, 6th grade)",
    ),
]

# Starting with Day 5 (the first grade-level content day), each lesson dict above
# should include an "hmwk_url" pointing to the matching IXL.com skill so a
# 📝 HMWK button appears on its card. Optionally add "hmwk_label" to state the
# target (e.g. "HMWK: Earn 90% on GG.2 (IXL, 6th grade)") instead of the
# generic "HMWK (IXL.com)" text. Days before Day 5 are intro/pilot days and
# intentionally have no homework link.
#
# A lesson dict may also include "worksheet_file" (a PDF in ./static/) to show
# a 📝 Classwork Worksheet button — it renders above the HMWK button on that
# day's card. Optionally add "worksheet_label" to customize its text.
#
# Shared family login for IXL — only needed if a parent doesn't have their own
# student's IXL account and must borrow the class account to complete homework.
IXL_PARENT_LOGIN_NOTE = "Parents borrowing the class login: Username bethuneacademy · Password BrightFuture2020"

# All homework, whether or not it's practiced on IXL, still has to be shown
# on paper — IXL is for practice/scoring, the notebook is the record of work.
HMWK_INSTRUCTIONS = "Show ALL work by hand — pencil and paper (graph paper is best), written out in your math notebook."

# PDFs live in ./static/ and are served directly by Streamlit at app/static/<file>
# (requires [server] enableStaticServing = true in .streamlit/config.toml).
# A plain <a href> to that URL is used instead of a base64/Blob "onclick" trick —
# the base64 approach breaks Streamlit's React click handling and silently fails.
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")

# Cards wrap onto new rows instead of squeezing every day into one row —
# with 7+ lesson days, one giant row of equal-width st.columns() made each
# card too narrow for its own button labels and the HMWK note to fit,
# forcing ugly text wrapping and ellipsis-truncated buttons. Chunking into
# fixed-size rows keeps each card a readable width no matter how many
# lesson days get added over the course of the year.
CARDS_PER_ROW = 4
for row_start in range(0, len(DAYS), CARDS_PER_ROW):
    row_days = DAYS[row_start:row_start + CARDS_PER_ROW]
    cols = st.columns(CARDS_PER_ROW)
    for col, day in zip(cols, row_days):
        with col:
            guide_path = os.path.join(STATIC_DIR, day["guide_file"])
            has_guide = os.path.exists(guide_path)
            if has_guide:
                guide_button_html = (
                    f'<a class="pdf-button" href="app/static/{day["guide_file"]}" '
                    f'target="_blank" rel="noopener noreferrer">📄 Observer Guide (PDF)</a>'
                )
            else:
                guide_button_html = (
                    '<span class="pdf-button disabled">📄 Guide — Coming Soon</span>'
                )

            worksheet_file = day.get("worksheet_file")
            if worksheet_file and os.path.exists(os.path.join(STATIC_DIR, worksheet_file)):
                worksheet_label = day.get("worksheet_label", "Classwork Worksheet")
                worksheet_button_html = (
                    f'<a class="worksheet-button" href="app/static/{worksheet_file}" '
                    f'target="_blank" rel="noopener noreferrer">📝 {worksheet_label}</a>'
                )
            else:
                worksheet_button_html = ""

            hmwk_url = day.get("hmwk_url")
            if hmwk_url:
                hmwk_label = day.get("hmwk_label", "HMWK (IXL.com)")
                hmwk_tooltip = f"{HMWK_INSTRUCTIONS}&#10;{IXL_PARENT_LOGIN_NOTE}"
                hmwk_button_html = (
                    f'<a class="hmwk-button" href="{hmwk_url}" target="_blank" '
                    f'rel="noopener noreferrer" title="{hmwk_tooltip}">📝 {hmwk_label}</a>'
                    f'<span class="hmwk-note">✏️ {HMWK_INSTRUCTIONS}</span>'
                    f'<span class="hmwk-note">{IXL_PARENT_LOGIN_NOTE}</span>'
                )
            else:
                hmwk_button_html = ""
            # NOTE: btn_stack_html is built as one joined string (no blank lines
            # between pieces). When a piece is "", leaving it on its own line
            # inside the triple-quoted block below creates a whitespace-only
            # line, which ends the raw-HTML block early (CommonMark's blank-line
            # rule) and leaks a literal "</div>" onto the page for every day
            # missing that piece. Joining on one line avoids that.
            link_button_html = (
                f'<a class="link-button" href="{day["page"]}" target="_blank">'
                f'🔗 Open {day["label"]} →</a>'
            )
            btn_stack_html = link_button_html + guide_button_html + worksheet_button_html + hmwk_button_html
            st.markdown(
                f"""
                <div class="day-card">
                    <span class="day-pill">{day['label']}</span>
                    <h3>{day['title']}</h3>
                    <p>{day['desc']}</p>
                    <div class="btn-stack">{btn_stack_html}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

st.markdown("---")
st.markdown("### 🗓️ School Calendar")

CALENDAR_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "assets", "school_calendar.png")
if os.path.exists(CALENDAR_IMAGE_PATH):
    st.image(CALENDAR_IMAGE_PATH, use_container_width=True, caption="Chandler Park Academy District Calendar")
else:
    st.markdown(
        """
        <div class="calendar-note">
        📌 The official school calendar will appear here once it's added to this project
        (<code>assets/school_calendar.png</code>).
        </div>
        """,
        unsafe_allow_html=True,
    )
