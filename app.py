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

# The Summative Test Sessions button is the launcher for ALL summative tests
# this school year. Clicking it opens a list of every test below. To post a new
# test, drop its PDF in ./static/ and add one dict to the end of this list.
SUMMATIVE_TESTS = [
    dict(
        label="Test 1",
        title="Days 5–10",
        desc="25 questions (4 pts each): rectangle area, missing sides, compound rectangles, "
             "parallelograms, and multiplying decimals &amp; fractions.",
        file="Summative_Assessment_Days5-10.pdf",
    ),
]

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
    .link-button, .pdf-button, .worksheet-button, .hmwk-button, .enrich-button, .anchor-button {{
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
    /* ---- Native download button, styled to match .pdf-button ---- */
    div[data-testid="stDownloadButton"] {{
        margin-top: -0.9rem;
        margin-bottom: 1rem;
    }}
    div[data-testid="stDownloadButton"] button {{
        width: 100%;
        background-color: white;
        color: {NAVY};
        border: 2px solid {NAVY};
        border-radius: 8px;
        font-weight: 700;
        font-size: 0.92rem;
        padding: 0.5rem 0.8rem;
        transition: background-color 0.15s ease, color 0.15s ease;
    }}
    div[data-testid="stDownloadButton"] button:hover {{
        background-color: {NAVY};
        color: white;
        border-color: {NAVY};
    }}
    div[data-testid="stDownloadButton"] button:focus:not(:active) {{
        color: {NAVY};
        border-color: {NAVY};
    }}
    .worksheet-button {{
        background-color: white;
        color: {GREEN} !important;
        border: 2px solid {GREEN};
    }}
    .worksheet-button:hover {{ background-color: {GREEN}; color: white !important; }}
    .anchor-button {{
        background-color: #EAF3FF;
        color: #1F5FA8 !important;
        border: 2px solid #1F5FA8;
        white-space: normal;
        line-height: 1.25;
    }}
    .anchor-button:hover {{ background-color: #1F5FA8; color: white !important; }}
    .enrich-button {{
        background-color: #F1ECF8;
        color: #5B3F8C !important;
        border: 2px dashed #5B3F8C;
        white-space: normal;
        line-height: 1.25;
    }}
    .enrich-button:hover {{ background-color: #5B3F8C; color: white !important; }}
    .enrich-note {{
        display: block;
        font-size: 0.72rem;
        color: #5B3F8C;
        margin-top: 0.25rem;
        line-height: 1.3;
        white-space: normal;
    }}
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
    "right in your browser."
)

st.markdown("---")

# Built as one joined string with no blank lines so Streamlit's markdown
# parser keeps the whole raw-HTML block together.
test_items_html = "".join(
    f'<a class="test-item" href="app/static/{t["file"]}" target="_blank" rel="noopener noreferrer">'
    f'<span class="test-pill">{t["label"]}</span>'
    f'<span class="test-text"><b>{t["title"]}</b><br><span class="test-desc">{t["desc"]}</span></span>'
    f'<span class="test-open">Open PDF →</span></a>'
    for t in SUMMATIVE_TESTS
    if os.path.exists(os.path.join(os.path.dirname(__file__), "static", t["file"]))
) or '<p class="test-desc">No summative tests posted yet.</p>'
st.markdown(
    f"""
    <style>
    details.summative > summary {{
        list-style: none; cursor: pointer; display: block; text-align: center;
        background-color: {GOLD}; color: white; font-weight: 800; font-size: 1.15rem;
        padding: 1rem 1.5rem; border-radius: 12px; border: 2px solid {GOLD};
    }}
    details.summative > summary::-webkit-details-marker {{ display: none; }}
    details.summative > summary:hover {{ background-color: #96754A; border-color: #96754A; }}
    details.summative[open] > summary {{ border-radius: 12px 12px 0 0; }}
    .test-list {{ border: 2px solid {GOLD}; border-top: none; border-radius: 0 0 12px 12px; padding: 0.6rem; }}
    a.test-item {{
        display: flex; align-items: center; gap: 0.9rem; padding: 0.7rem 0.9rem; margin: 0.3rem 0;
        border-radius: 10px; background: {CREAM}; text-decoration: none !important; color: {NAVY} !important;
    }}
    a.test-item:hover {{ background: #E8E1D3; }}
    .test-pill {{ background: {NAVY}; color: white; font-weight: 700; font-size: 0.8rem;
                  padding: 0.25rem 0.7rem; border-radius: 999px; white-space: nowrap; }}
    .test-text {{ flex: 1; line-height: 1.35; }}
    .test-desc {{ color: {MUTED}; font-size: 0.82rem; }}
    .test-open {{ font-weight: 700; color: {GOLD}; white-space: nowrap; }}
    </style>
    <details class="summative"><summary>📝 Open Summative Test Sessions →</summary><div class="test-list">{test_items_html}</div></details>
    <p style="text-align:center;color:{MUTED};font-size:0.85rem;margin-top:0.4rem;margin-bottom:1.5rem;">
        Every summative test for the school year, in order. Click to see the list, then open a test. Show all work.
    </p>
    """,
    unsafe_allow_html=True,
)

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
        desc="First multi-board Engage/Explore/Enrich pilot with online practice, journaling, and 1-on-1 tutoring.",
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
        hmwk_url="https://www.khanacademy.org/math/cc-fourth-grade-math/area-perimeter/imp-area-and-perimeter/e/area-and-perimeter-of-rectangles-word-problems",
        hmwk_label="HMWK: Earn 90% on Area & Perimeter of Rectangles: Word Problems (Khan Academy)",
    ),
    dict(
            label="Day 6",
            title="Area Unlocks the Missing Side",
            desc="Square vs. rectangle repair, then area runs in reverse: given the area and one side, find the missing side, and split an L-shaped floor into two rectangles.",
            page="https://cpamath6day6.streamlit.app/",
            guide_file="Day6_Observer_Guide.pdf",
            anchor_charts=[
                dict(file="Anchor_Chart_Area_of_a_Square.pdf", label="Anchor Chart: Area of a Square"),
            ],
            worksheet_file="Day6_wksht.pdf",
            worksheet_label="Classwork Worksheet (Day 6 wksht)",
            hmwk_url="https://www.khanacademy.org/math/cc-third-grade-math/imp-geometry/imp-multiply-to-find-area/e/find-a-missing-side-length-when-given-area-of-a-rectangle",
            hmwk_label="HMWK: Earn 90% on Find a Missing Side Length When Given Area (Khan Academy)",
    ),
    dict(
        label="Day 7",
        title="Area of Compound Rectangles",
        desc="Split an L-shaped floor into two rectangles and add, or enclose it in one rectangle and subtract the missing piece — then apply both moves to a trickier T-shape.",
        page="https://cpamath6day7.streamlit.app/",
        guide_file="Day7_Observer_Guide.pdf",
        worksheet_file="Day7_wksht.pdf",
        worksheet_label="Classwork Worksheet (Day 7 wksht)",
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/x0267d782:cc-6th-plane-figures/cc-6th-area/e/area-of-quadrilaterals-and-polygons",
        hmwk_label="HMWK: Earn 90% on Area of Composite Shapes (Khan Academy)",
    ),
    dict(
        label="Day 8",
        title="Area of a Parallelogram",
        desc="Cut a triangle off one end of a leaning parallelogram and slide it to the other end — it becomes a rectangle with the exact same base and height, so Area = base × height.",
        page="https://cpamath6day8.streamlit.app/",
        guide_file="Day8_Observer_Guide.pdf",
        anchor_charts=[
            dict(file="Anchor_Chart_Area_of_a_Parallelogram.pdf", label="Anchor Chart: Area of a Parallelogram"),
        ],
        worksheet_file="Day8_wksht.pdf",
        worksheet_label="Classwork Worksheet (Day 8 wksht)",
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/x0267d782:cc-6th-plane-figures/cc-6th-parallelogram-area/e/area_of_parallelograms",
        hmwk_label="HMWK: Earn 90% on Area of Parallelograms (Khan Academy)",
    ),
    dict(
        label="Day 9",
        title="Area of a Parallelogram — Refine, Practice & Quiz",
        desc="Finish Apply It, work through Refine (including a student's real base-times-slant mistake), Additional Practice, and the full Lesson 1 Quiz.",
        page="https://cpamath6day9.streamlit.app/",
        guide_file="Day9_Observer_Guide.pdf",
        anchor_charts=[
            dict(file="Anchor_Chart_Area_of_a_Parallelogram.pdf", label="Anchor Chart: Area of a Parallelogram"),
        ],
        worksheet_file="Day9_wksht.pdf",
        worksheet_label="Classwork Worksheet (Day 9 wksht)",
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/x0267d782:cc-6th-plane-figures/cc-6th-parallelogram-area/e/find-missing-side-when-given-area-of-a-parallelogram",
        hmwk_label="HMWK: Earn 90% on Find Missing Length When Given Area of a Parallelogram (Khan Academy)",
    ),
    dict(
        label="Day 10",
        title="Skill Breakout — Multiplying Decimals & Fractions",
        desc="Two prerequisite-skill reviews before Percent of a Quantity: multiplying decimals and multiplying fractions, proving both are the same function wearing different notation, plus percent-flavored practice and two common-mistake traps.",
        page="https://cpamath6day10.streamlit.app/",
        guide_file="Day10_Observer_Guide.pdf",
        worksheet_file="Day10_wksht.pdf",
        worksheet_label="Classwork Worksheet (Day 10 wksht)",
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-arithmetic-operations/cc-6th-multiplying-decimals/e/multiplying_decimals",
        hmwk_label="HMWK: Earn 90% on Multiplying Decimals (Standard Algorithm) (Khan Academy)",
    ),
    dict(
        label="Day 11",
        title="Review Day — Days 5–10",
        desc="No new lesson today: a 50-question review of rectangle area, missing sides, compound rectangles, parallelograms, and multiplying decimals & fractions, with in-depth worked solutions.",
        worksheet_file="Day11_Review_Sheet.pdf",
        worksheet_label="Review Sheet (50 Qs + Solutions)",
        enrichment=[
            dict(file="Day11_Enrichment_Stretching_Machine.pdf",
                 label="Enrichment: The Stretching Machine (Advanced Outlook)"),
            dict(file="Day11_Enrichment_Videos.pdf",
                 label="Enrichment Videos (MIT · Stanford · CMU)"),
        ],
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/x0267d782:cc-6th-plane-figures/cc-6th-area/e/area-of-quadrilaterals-and-polygons",
        hmwk_label="HMWK: Earn 90% on Area of Composite Shapes (Khan Academy)",
    ),
    dict(
        label="Day 12",
        title="Review Day 2 — Days 5–10",
        desc="A second review with all-new numbers: 56 questions on rectangle area, missing sides, compound rectangles, parallelograms (with extra practice spotting distractor slanted sides and diagonals), and multiplying decimals & fractions, with in-depth worked solutions.",
        worksheet_file="Day12_Review_Sheet.pdf",
        worksheet_label="Review Sheet (56 Qs + Solutions)",
        enrichment=[
            dict(file="Day12_Enrichment_Project.pdf",
                 label="Enrichment Project: Build It in Detroit"),
        ],
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/x0267d782:cc-6th-plane-figures/cc-6th-parallelogram-area/e/find-missing-side-when-given-area-of-a-parallelogram",
        hmwk_label="HMWK: Earn 90% on Find Missing Length When Given Area of a Parallelogram (Khan Academy)",
    ),
    dict(
        label="Day 13",
        title="Area of a Triangle",
        desc="Two copies of any triangle lock together into a parallelogram, so Area = ½ × base × height — including obtuse triangles whose height falls outside the shape, and problems that run the formula backwards to a missing base or height.",
        guide_file="Day13_Observer_Guide.pdf",
        worksheet_file="Day13_Lesson_Packet.pdf",
        worksheet_label="Lesson & Practice (12 Qs + Solutions)",
        anchor_charts=[
            dict(file="Anchor_Chart_Area_of_a_Parallelogram.pdf", label="Anchor Chart: Area of a Parallelogram"),
        ],
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/x0267d782:cc-6th-plane-figures/cc-6th-area-triangle/e/area_of_triangles_1",
        hmwk_label="HMWK: Earn 90% on Area of Triangles (Khan Academy)",
    ),
    dict(
        label="Day 14",
        title="Nets & Surface Area",
        desc="Cut a real box apart and flatten it: every face is a rectangle or triangle you can already measure. Surface area of cubes, rectangular prisms, and triangular prisms, plus wrapping-paper, fish-tank, and paint problems.",
        guide_file="Day14_Observer_Guide.pdf",
        worksheet_file="Day14_Lesson_Packet.pdf",
        worksheet_label="Lesson & Practice (12 Qs + Solutions)",
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-geometry-topic/x0267d782:cc-6th-nets-of-3d-figures/e/surface-area",
        hmwk_label="HMWK: Earn 90% on Surface Area Using Nets (Khan Academy)",
    ),
    dict(
        label="Day 15",
        title="Area of a Trapezoid",
        desc="One pair of parallel sides, two ways to find the area: decompose into a rectangle and two triangles, or compose two copies into a parallelogram with base b₁ + b₂ — both give A = ½(b₁ + b₂)h.",
        guide_file="Day15_Observer_Guide.pdf",
        worksheet_file="Day15_Lesson_Packet.pdf",
        worksheet_label="Lesson & Practice (12 Qs + Solutions)",
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/x0267d782:cc-6th-plane-figures/cc-6th-area/e/decompose-area-with-triangles",
        hmwk_label="HMWK: Earn 90% on Decompose Area With Triangles (Khan Academy)",
    ),
    dict(
        label="Day 16",
        title="Review Day — Days 13–15",
        desc="No new lesson today: a 42-question review of triangle area, nets & surface area, and trapezoid area, with distractor slanted sides, missing-measure problems, error analysis, and in-depth worked solutions.",
        worksheet_file="Day16_Review_Sheet.pdf",
        worksheet_label="Review Sheet (42 Qs + Solutions)",
        anchor_charts=[
            dict(file="Anchor_Chart_Area_of_a_Triangle.pdf", label="Anchor Chart: Area of a Triangle"),
            dict(file="Anchor_Chart_Nets_and_Surface_Area.pdf", label="Anchor Chart: Nets & Surface Area"),
            dict(file="Anchor_Chart_Area_of_a_Trapezoid.pdf", label="Anchor Chart: Area of a Trapezoid"),
        ],
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/x0267d782:cc-6th-plane-figures/cc-6th-area-triangle/e/find-base-and-height-on-a-triangle",
        hmwk_label="HMWK: Earn 90% on Find Base and Height on a Triangle (Khan Academy)",
    ),
    dict(
        label="Day 17",
        title="Enrichment Day — Three Big Ideas",
        desc="Optional Advanced Outlook day built on Days 13–15: Pick's Theorem (count dots, get area), Euler's Formula (V − E + F = 2 for every solid you built from a net), and why surface area grows slower than volume — plus a hands-on Polyhedron Zoo build.",
        enrichment=[
            dict(file="Day17_Enrichment_Big_Ideas.pdf",
                 label="Enrichment: Pick's Theorem, Euler's Formula & SA:V"),
            dict(file="Day17_Enrichment_Project_Polyhedron_Zoo.pdf",
                 label="Enrichment Project: The Polyhedron Zoo"),
        ],
    ),
    dict(
        label="Day 18",
        title="Ratio Language — For Every",
        desc="Ratios start out loud: 4 test tubes for every 1 student, 6 tacos for every 3 guests. Equal-groups models built from counters, the order-matters trap, and a For-Every Museum build where every exhibit card has to name both quantities being compared.",
        page="https://cpamath6day18.streamlit.app/",
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-ratios-prop-topic/intro-to-ratios/e/representing-ratios",
        hmwk_label="HMWK: Earn 90% on Basic Ratios (Khan Academy)",
        worksheet_file="Day18_wksht.pdf",
        worksheet_label="Classwork Worksheet (Day 18 wksht)",
    ),
    dict(
        label="Day 19",
        title="Writing Ratios — Part to Part, Part to Whole",
        desc="Two ways to write a ratio — the word to and a colon — then the split that trips everyone: 8 mallards to 5 ruddy ducks is part-to-part, but 8 to 13 is part-to-whole. Ends with the Ratio Card Challenge, scored on whether the class can tell what you compared.",
        page="https://cpamath6day19.streamlit.app/",
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-ratios-prop-topic/cc-6th-ratio-word-problems/e/part-part-whole-ratios",
        hmwk_label="HMWK: Earn 90% on Part-Part-Whole Ratios (Khan Academy)",
        worksheet_file="Day19_wksht.pdf",
        worksheet_label="Classwork Worksheet (Day 19 wksht)",
    ),
    dict(
        label="Day 20",
        title="Refine — Say What It Compares",
        desc="No new idea today, just precision: a ratio with no sentence attached scores nothing. Akiko's bike ride, Mason's granola-bar error, Bridget's welcome bags — where the difference keeps moving but the multiple never does — and a team ratio hunt on the bear-tagging data.",
        page="https://cpamath6day20.streamlit.app/",
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-ratios-prop-topic/visualize-ratios/e/ratios-with-tape-diagrams",
        hmwk_label="HMWK: Earn 90% on Ratios With Tape Diagrams (Khan Academy)",
        worksheet_file="Day20_wksht.pdf",
        worksheet_label="Classwork Worksheet (Day 20 wksht)",
    ),
    dict(
        label="Day 21",
        title="Explore Equivalent Ratios",
        desc="Equivalent ratios express the same comparison. Build one by combining equal groups, which turns out to be the same as multiplying both quantities by the same number — and see exactly why 3 : 2 and 9 : 8 are not equivalent even though 6 was added to each.",
        page="https://cpamath6day21.streamlit.app/",
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-ratios-prop-topic/visualize-ratios/e/equivalent-ratio-word-problems--basic-",
        hmwk_label="HMWK: Earn 90% on Equivalent Ratios With Equal Groups (Khan Academy)",
        worksheet_file="Day21_wksht.pdf",
        worksheet_label="Classwork Worksheet (Day 21 wksht)",
    ),
    dict(
        label="Day 22",
        title="Equivalent Ratios at Scale",
        desc="Equal groups run out of paper at 120 picnic tables. The double number line shows every equivalent ratio at once; the ratio table multiplies or divides straight to the one you need. Heartbeat Lab, Kareem's 4 : 1 error, and a review of the whole ratio week.",
        page="https://cpamath6day22.streamlit.app/",
        hmwk_url="https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-ratios-prop-topic/cc-6th-equivalent-ratios/e/solving-ratio-problems-with-tables",
        hmwk_label="HMWK: Earn 90% on Ratio Tables (Khan Academy)",
        worksheet_file="Day22_wksht.pdf",
        worksheet_label="Classwork Worksheet (Day 22 wksht)",
    ),
]

# Starting with Day 5 (the first grade-level content day), each lesson dict above
# should include an "hmwk_url" pointing to the matching Khan Academy exercise so a
# 📝 HMWK button appears on its card. Optionally add "hmwk_label" to state the
# target (e.g. "HMWK: Earn 90% on Area of Triangles (Khan Academy)") instead
# of the generic "HMWK (Khan Academy)" text. Students reach Khan Academy
# through Clever SSO, so these links land them straight in the exercise
# already signed in. Days before Day 5 are intro/pilot days and
# intentionally have no homework link.
#
# A lesson dict may also include "worksheet_file" (a PDF in ./static/) to show
# a 📝 Classwork Worksheet button — it renders above the HMWK button on that
# day's card. Optionally add "worksheet_label" to customize its text.
#
# A lesson dict may also include "anchor_charts": a list of dict(file=..., label=...)
# PDFs in ./static/. Each shows as a light-blue 📌 button under the Observer Guide.
#
# A lesson dict may also include "enrichment": a list of dict(file=..., label=...)
# PDFs in ./static/. Each shows as a dashed purple 🚀 button at the bottom of the
# card. Enrichment is optional, "Advanced Outlook" material that can go beyond
# 6th-grade standards — it is never required or tested.
#
# All homework, whether or not it's practiced on Khan Academy, still has to be
# shown on paper — Khan Academy is for practice/scoring, the notebook is the
# record of work.
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
            # Review days have no lesson page or observer guide, so both
            # "page" and "guide_file" are optional.
            guide_file = day.get("guide_file")
            if not guide_file:
                guide_button_html = ""
            elif os.path.exists(os.path.join(STATIC_DIR, guide_file)):
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
                hmwk_label = day.get("hmwk_label", "HMWK (Khan Academy)")
                hmwk_tooltip = HMWK_INSTRUCTIONS
                hmwk_button_html = (
                    f'<a class="hmwk-button" href="{hmwk_url}" target="_blank" '
                    f'rel="noopener noreferrer" title="{hmwk_tooltip}">📝 {hmwk_label}</a>'
                    f'<span class="hmwk-note">✏️ {HMWK_INSTRUCTIONS}</span>'
                )
            else:
                hmwk_button_html = ""
            # NOTE: btn_stack_html is built as one joined string (no blank lines
            # between pieces). When a piece is "", leaving it on its own line
            # inside the triple-quoted block below creates a whitespace-only
            # line, which ends the raw-HTML block early (CommonMark's blank-line
            # rule) and leaks a literal "</div>" onto the page for every day
            # missing that piece. Joining on one line avoids that.
            if day.get("page"):
                link_button_html = (
                    f'<a class="link-button" href="{day["page"]}" target="_blank">'
                    f'🔗 Open {day["label"]} →</a>'
                )
            else:
                link_button_html = ""
            enrich_button_html = "".join(
                f'<a class="enrich-button" href="app/static/{e["file"]}" target="_blank" '
                f'rel="noopener noreferrer">🚀 {e["label"]}</a>'
                for e in day.get("enrichment", [])
                if os.path.exists(os.path.join(STATIC_DIR, e["file"]))
            )
            if enrich_button_html:
                enrich_button_html += (
                    '<span class="enrich-note">🚀 Optional enrichment · Advanced Outlook — '
                    'may go beyond 6th-grade standards; not tested.</span>'
                )
            anchor_button_html = "".join(
                f'<a class="anchor-button" href="app/static/{c["file"]}" target="_blank" '
                f'rel="noopener noreferrer">📌 {c["label"]}</a>'
                for c in day.get("anchor_charts", [])
                if os.path.exists(os.path.join(STATIC_DIR, c["file"]))
            )
            btn_stack_html = (link_button_html + guide_button_html + anchor_button_html + worksheet_button_html
                              + hmwk_button_html + enrich_button_html)
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
