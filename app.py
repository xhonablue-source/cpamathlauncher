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

    .day-card {{
        background-color: {CREAM};
        border: 2px solid {GOLD};
        border-radius: 12px;
        padding: 1.5rem 1.6rem 0.7rem 1.6rem;
        margin-bottom: 1rem;
        height: 100%;
    }}
    .day-card h3 {{ color: {NAVY}; margin: 0 0 0.4rem 0; }}
    .day-card p {{ min-height: 3.6rem; font-size: 0.98rem; }}
    .day-pill {{
        display: inline-block;
        background-color: {NAVY};
        color: white;
        font-size: 0.75rem;
        font-weight: 700;
        padding: 0.15rem 0.7rem;
        border-radius: 999px;
        margin-bottom: 0.6rem;
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
    "Click any day below to open that day's full lesson. Use the school calendar underneath to "
    "match each lesson day to its actual calendar date."
)

st.markdown("---")
st.markdown("### 📅 Lessons by Day")

DAYS = [
    dict(
        label="Day 1",
        title="What Is Math?",
        desc="Observe a real object, then simulate an imagined object using geometric shapes on graph paper.",
        page="https://cpa-math6-day1.streamlit.app/",
    ),
    dict(
        label="Day 2",
        title="Getting to Know You: Data Reveal",
        desc="A real class-data opener (12 of 42), a confounding-variables talk, and five shape survey stations.",
        page="https://cpamathgrade6day2.streamlit.app/",
    ),
    dict(
        label="Day 3",
        title="Hear From Us: Skits & Focus",
        desc="A Human Bar Graph, classroom-behavior skits, and a Keep-or-Rid vote — no drawing today.",
        page="https://cpamathgrade6day3.streamlit.app/",
    ),
    dict(
        label="Day 4",
        title="Testing the Model",
        desc="First multi-board Engage/Explore/Enrich pilot with IXL.com, journaling, and 1-on-1 tutoring.",
        page="https://cpamathgrade6day4.streamlit.app/",
    ),
]

cols = st.columns(4)
for col, day in zip(cols, DAYS):
    with col:
        st.markdown(
            f"""
            <div class="day-card">
                <span class="day-pill">{day['label']}</span>
                <h3>{day['title']}</h3>
                <p>{day['desc']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.page_link(day["page"], label=f"Open {day['label']} →", icon="🔗", use_container_width=True)

st.markdown("---")
st.markdown("### 🗓️ School Calendar — Match a Lesson Day to a Real Date")

CALENDAR_IMAGE_PATH = os.path.join(os.path.dirname(__file__), "assets", "school_calendar.png")

if os.path.exists(CALENDAR_IMAGE_PATH):
    st.image(CALENDAR_IMAGE_PATH, use_container_width=True, caption="Chandler Park Academy District Calendar")
else:
    st.markdown(
        """
        <div class="calendar-note">
        📌 The official school calendar will appear here once it's added to this project
        (<code>assets/school_calendar.png</code>). Once it's in place, families will be able to scroll
        down to see the real calendar directly under the lesson-day buttons above.
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("#### Day → Calendar Date Reference")
st.caption("Fill in or update the dates below to match this year's actual teaching calendar.")

ref_cols = st.columns(4)
placeholder_dates = ["[date]", "[date]", "[date]", "[date]"]
for col, day, date in zip(ref_cols, DAYS, placeholder_dates):
    with col:
        st.markdown(
            f"""
            <div class="day-card" style="text-align:center;">
                <span class="day-pill">{day['label']}</span>
                <h3 style="font-size:1.3rem;">{date}</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.caption(
    "Tell Professor Xavier's assistant the actual date for each lesson day, and this reference "
    "row will be updated to match — or upload the school calendar and both sections can be filled "
    "in together."
)
