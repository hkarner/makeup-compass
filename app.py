import streamlit as st
import sys
import os

# Make sure rules/ is importable
sys.path.insert(0, os.path.dirname(__file__))

from logic import build_profile
from seo import set_page_meta, inject_jsonld
from about_page import render_about
from welcome_page import render_welcome
from makeup_101 import render_makeup_101
from skill_page import build_skill_page

# ── MUST be first st. call ────────────────────────────────────────────────────
st.set_page_config(
    page_title="Makeup Compass",
    page_icon="🧭",
    layout="centered"
)

# ── SEO / GEO setup ───────────────────────────────────────────────────────────
set_page_meta()
inject_jsonld()  # injects JSON-LD structured data for AI tool indexing

# ── Navigation ────────────────────────────────────────────────────────────────
page = st.sidebar.radio(
    "Navigate",
    options=["💄 Quiz", "📚 Makeup 101", "📖 About & Methodology"],
    label_visibility="collapsed"
)

if page == "📚 Makeup 101":
    render_makeup_101()
    st.stop()

if page == "📖 About & Methodology":
    render_about()
    st.stop()  # don't render the quiz on the About page

# ── Welcome screen ────────────────────────────────────────────────────────────
if not st.session_state.get("started", False):
    render_welcome()
    st.stop()

# ── Quiz ─────────────────────────────────────────────────────────────────────
st.components.v1.html("""
<script>
    var el = window.parent.document.querySelector('.main');
    if (el) el.scrollTop = 0;
    window.parent.scrollTo(0, 0);
</script>
""", height=0)
st.title("🧭 Makeup Compass")
st.divider()

with st.form("quiz"):
    st.subheader("About You")
    st.caption("💡 Before you start: find a mirror near a window or step outside. Natural light gives you the most accurate read on your skin tone, vein color, and dark circles.")

    depth = st.radio(
        "1. Skin tone depth",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: {
            1: "1 — Fair — Very light skin; I burn easily and rarely tan",
            2: "2 — Light-medium — Light skin that may tan slightly in summer",
            3: "3 — Medium — Tan or olive tone; I tan fairly easily",
            4: "4 — Medium-deep — Brown skin tone",
            5: "5 — Deep — Deep brown or ebony skin tone"
        }[x],
        index=2
    )

    st.markdown(
        '<p style="font-size: 0.875rem; font-weight: 400; margin-bottom: 0.25rem;">2. Undertone</p>',
        unsafe_allow_html=True
    )
    st.caption("Check the inside of your wrist in natural light. Veins that look green = warm. Blue or purple = cool. Can't tell? You're probably neutral. Paper test: hold a white piece of paper next to your face, then a cream or off-white one. Whichever makes your skin look clearer and more defined points toward cool (white wins) or warm (cream wins). Use that direction to choose below.")
    undertone = st.radio(
        "2. Undertone",
        options=["warm", "neutral-warm", "neutral", "neutral-cool", "cool"],
        format_func=lambda x: {
            "warm":         "Warm — My wrist veins look green; gold jewelry looks more natural on my skin than silver",
            "neutral-warm": "Neutral-warm — Veins look blue-green; gold looks slightly more natural but silver works too",
            "neutral":      "Neutral — Can't tell if veins are blue or green; gold and silver look equally natural",
            "neutral-cool": "Neutral-cool — Veins look blue-green; silver looks slightly more natural but gold works too",
            "cool":         "Cool — My wrist veins look blue or purple; silver jewelry looks more natural on my skin than gold"
        }[x],
        label_visibility="collapsed",
    )

    coverage = st.radio(
        "3. Base coverage preference",
        options=["none", "skin-like", "light", "medium", "full"],
        format_func=lambda x: {
            "none":      "Skip base entirely — I prefer a bare-skin approach",
            "skin-like": "Skin-like / barely there — just a hint of evening out",
            "light":     "Light coverage",
            "medium":    "Medium coverage",
            "full":      "Full coverage",
        }[x],
        index=2
    )

    eye_shape = st.radio(
        "4. Eye shape",
        options=["deep-set", "hooded", "almond", "monolid", "downturned", "protruding"],
        format_func=lambda x: {
            "deep-set":   "Deep-set — my eyes sit back in the socket; the brow bone casts shadow on the lid",
            "hooded":     "Hooded — the brow bone partially covers the lid when my eyes are open",
            "almond":     "Almond — my eyes are roughly almond-shaped with visible lid crease",
            "monolid":    "Monolid — I have little or no visible lid crease",
            "downturned": "Downturned — the outer corners angle slightly downward",
            "protruding": "Protruding — my lids appear to project forward"
        }[x],
        help="Not sure? Look straight ahead in a mirror. If your brow bone overshadows your lid when your eyes are open: hooded. If you can see your whole lid and a clear crease: almond. No crease at all: monolid. Outer corners dip downward: downturned. If you're unsure, almond is the most common."
    )

    dark_circles = st.radio(
        "5. Dark circles?",
        options=["none", "mild", "blue-purple", "brown", "mixed"],
        format_func=lambda x: {
            "none":        "None",
            "mild":        "Mild — barely noticeable",
            "blue-purple": "Moderate — blue or purple tone",
            "brown":       "Moderate — brown tone",
            "mixed":       "Mixed — blue/purple at inner corner, brown underneath"
        }[x],
        help="Check in natural light. If the shadow under your eye looks bluish or purplish — especially near the inner corner — that's a clue toward blue-purple. If it looks more brown or tan-coloured, that's a clue toward brown. If you're seeing both in different spots, mixed is the right pick. Not sure at all? Mixed is a safe default."
    )

    st.markdown(
        '<p style="font-size: 0.875rem; font-weight: 400; margin-bottom: 0.25rem;">6. Overall contrast level</p>',
        unsafe_allow_html=True
    )
    st.caption(
        "Contrast = the gap between your skin depth and your feature depth — not just how dark your features are. "
        "Dark hair + dark eyes on medium skin = Medium or Medium-High, not High. "
        "Medium: a noticeable but soft difference. Medium-High: features read clearly against your skin, but it's not a stark jump. "
        "High: your skin and features are at opposite ends — e.g. fair skin + very dark hair and eyes, or deep skin + very light eyes."
    )
    contrast = st.radio(
        "6. Overall contrast level",
        options=["low", "medium", "medium-high", "high"],
        format_func=lambda x: {
            "low":         "Low — Hair, eyes, and skin are all close in depth (e.g., light skin + light hair + light eyes)",
            "medium":      "Medium — A noticeable but not stark difference. Medium skin + medium-dark features.",
            "medium-high": "Medium-high — Clear difference between skin and features, but skin is medium. Dark hair/eyes don't automatically mean high contrast.",
            "high":        "High — Stark light-dark opposition. Typically fair/light skin with very dark hair and eyes.",
        }[x],
        index=1,
        label_visibility="collapsed",
        help="💡 Look at a no-makeup photo in natural light. It's about the gap between how light your skin is and how dark your features are — not just whether your features are dark. Not sure? Medium is the most common starting point.",
    )

    lip_type = st.radio(
        "7. Lip type",
        options=["even", "two-toned", "thin", "full", "thin-two-toned", "full-two-toned"],
        format_func=lambda x: {
            "even":            "Even-toned — my lips are roughly one color",
            "two-toned":       "Two-toned — medium or full lips with darker edges, lighter or pinker center",
            "thin":            "Thin — I have thinner lips (even-toned)",
            "full":            "Full — I have fuller lips (even-toned)",
            "thin-two-toned":  "Thin and two-toned — thinner lips with darker edges",
            "full-two-toned":  "Full and two-toned — fuller lips with darker edges, lighter center"
        }[x]
    )

    lash_curl = st.radio(
        "8. Lash curl",
        options=["straight", "wavy", "curly"],
        format_func=lambda x: {
            "straight": "Straight — my lashes point outward or slightly downward with no natural curve",
            "wavy":     "Slightly wavy — some natural shape, but not dramatically curled",
            "curly":    "Curly — my lashes have a natural upward curl",
        }[x],
        index=1,
        help="Look at your lashes without mascara. Do they point straight out, or do they curve upward naturally?"
    )

    lash_color = st.radio(
        "9. Lash color",
        options=["dark", "light"],
        format_func=lambda x: {
            "dark":  "Dark — my lashes are naturally brown, black, or dark brown",
            "light": "Light — my lashes are naturally blonde, red, or light brown",
        }[x],
        help="Look at your lashes without mascara in natural light."
    )

    lash_density = st.radio(
        "10. Lash density",
        options=["sparse", "average", "full"],
        format_func=lambda x: {
            "sparse":  "Sparse — my lashes are fine or thin; I can see gaps",
            "average": "Average — moderate density, neither especially full nor sparse",
            "full":    "Full — my lashes are naturally thick or plentiful",
        }[x],
        index=1,
        help="Look at your lashes without mascara. How thick or full are they naturally?"
    )

    submitted = st.form_submit_button("Get My Guide →", use_container_width=True)

# ── Results ───────────────────────────────────────────────────────────────────
if submitted:
    # Fresh submission — save inputs and reset sub-question state
    st.session_state["quiz_inputs"] = dict(
        depth=depth, undertone=undertone, eye_shape=eye_shape,
        contrast=contrast, lip_type=lip_type, coverage=coverage,
        dark_circles=dark_circles,
        lash_curl=lash_curl, lash_color=lash_color, lash_density=lash_density
    )
    st.session_state["submitted"] = True
    st.session_state["subq_done"] = False
    st.session_state["profile"] = None  # clear any previous profile

if st.session_state.get("submitted"):
    inputs = st.session_state["quiz_inputs"]
    eye_shape_val = inputs["eye_shape"]
    dark_circles_val = inputs["dark_circles"]

    needs_subq = (
        eye_shape_val in ("deep-set", "hooded")
        or dark_circles_val not in ("none", "mild")
    )

    # ── Sub-questions (shown once, between form submit and results) ────────────
    if needs_subq and not st.session_state.get("subq_done"):
        st.components.v1.html("""
        <script>
            var el = window.parent.document.querySelector('.main');
            if (el) el.scrollTop = 0;
            window.parent.scrollTo(0, 0);
        </script>
        """, height=0)
        st.divider()
        st.subheader("One more thing...")
        st.caption(
            "These quick follow-ups help us give you more precise placement advice "
            "for your specific eye anatomy."
        )

        deep_set_subtype = "uniform"
        hooded_subtype = "outer"
        dark_circle_location = "everywhere"
        lid_discoloration = "none"

        if eye_shape_val == "deep-set":
            deep_set_subtype = st.radio(
                "Where does your eye feel deepest or most shadowed?",
                options=["uniform", "inner", "outer"],
                format_func=lambda x: {
                    "uniform": "Uniformly set back — the whole lid feels shadowed under the brow bone",
                    "inner":   "Inner corner — most cavernous near the nose (deepest shadow zone near the bridge)",
                    "outer":   "Outer corner — most covered by the lid fold at the outer edge",
                }[x],
                help="Look straight ahead in a mirror. Where does your eye feel most recessed or shadowed — evenly across the lid, or concentrated at one end?"
            )

        if eye_shape_val == "hooded":
            hooded_subtype = st.radio(
                "How much of your lid is covered by the fold?",
                options=["outer", "full"],
                format_func=lambda x: {
                    "outer": "Just the outer corner — my center and inner lid are still visible when eyes are open",
                    "full":  "Most or all of my lid — very little lid space shows when eyes are open",
                }[x],
                help="Look straight ahead with eyes open. If you can see your lid clearly in the center: outer hooding. If barely any lid is visible: full hooding."
            )

        if dark_circles_val not in ("none", "mild"):
            dark_circle_location = st.radio(
                "Where are your dark circles most noticeable?",
                options=["inner", "full", "outer", "everywhere"],
                format_func=lambda x: {
                    "inner":      "Inner corner — darkest near the nose",
                    "full":       "Full undereye — evenly spread across the whole area",
                    "outer":      "Outer corner — darkest toward the outside",
                    "everywhere": "Everywhere equally",
                }[x],
                help="Check in natural light. Does the shadow concentrate near your nose, sit evenly, or sit more toward the outer corner?"
            )

            lid_discoloration_answer = st.radio(
                "Does the discoloration extend onto your eyelids as well?",
                options=[
                    "No — just under the eye",
                    "Yes — partial (inner corner or center of lid only)",
                    "Yes — full lid (most or all of the lid surface is affected)"
                ],
                help=(
                    "This is often called 'really dark circles' but is actually thin skin "
                    "over blood vessels on the lid surface — a different condition with a different fix."
                )
            )
            lid_discoloration = (
                "none" if lid_discoloration_answer.startswith("No")
                else "partial" if "partial" in lid_discoloration_answer
                else "full"
            )

        if st.button("View My Results →", use_container_width=True):
            st.session_state["deep_set_subtype"] = deep_set_subtype
            st.session_state["hooded_subtype"] = hooded_subtype
            st.session_state["dark_circle_location"] = dark_circle_location
            st.session_state["lid_discoloration"] = lid_discoloration
            st.session_state["subq_done"] = True
            st.rerun()

        st.stop()

    # ── Build profile (once, then cached in session state) ────────────────────
    if st.session_state.get("profile") is None:
        profile = build_profile(
            depth=inputs["depth"],
            undertone=inputs["undertone"],
            eye_shape=inputs["eye_shape"],
            contrast=inputs["contrast"],
            lip_type=inputs["lip_type"],
            coverage=inputs["coverage"],
            dark_circles=inputs["dark_circles"],
            deep_set_subtype=st.session_state.get("deep_set_subtype", "uniform"),
            hooded_subtype=st.session_state.get("hooded_subtype", "outer"),
            dark_circle_location=st.session_state.get("dark_circle_location", "everywhere"),
            lid_discoloration=st.session_state.get("lid_discoloration", "none"),
            lash_curl=inputs.get("lash_curl", "wavy"),
            lash_color=inputs.get("lash_color", "dark"),
            lash_density=inputs.get("lash_density", "average"),
        )
        st.session_state["profile"] = profile
    else:
        profile = st.session_state["profile"]

    # Restore display variables from session state
    depth = inputs["depth"]
    undertone = inputs["undertone"]
    eye_shape = inputs["eye_shape"]
    contrast = inputs["contrast"]
    lip_type = inputs["lip_type"]
    coverage = inputs["coverage"]
    dark_circles = inputs["dark_circles"]
    lash_curl = inputs.get("lash_curl", "wavy")
    lash_color = inputs.get("lash_color", "dark")
    lash_density = inputs.get("lash_density", "average")

    st.components.v1.html("""
    <script>
        var el = window.parent.document.querySelector('.main');
        if (el) el.scrollTop = 0;
        window.parent.scrollTo(0, 0);
    </script>
    """, height=0)
    st.divider()
    st.header("Your Personalized Makeup Guide")
    st.markdown("""
    These are starting points, not rules. Each section describes *what tends to work* 
    for your feature combination — but you're the one who knows what you love, and 
    that always wins. Use this as a lens for shopping and experimenting, not a prescription.

    *Tip: When something in your results surprises you, that's worth exploring — sometimes 
    the unexpected thing is exactly right. Sometimes it isn't. That's what swatching is for.*
    """)

    # --- Your Profile summary ---
    contrast_labels = {
        "low":         ("Low contrast", "Your hair, eyes, and skin are close in depth. Soft, blended looks work best — heavy pigment can overwhelm your natural harmony."),
        "medium":      ("Medium contrast", "Moderate difference between your features. You have flexibility — you can do soft everyday looks or build up for events."),
        "medium-high": ("Medium-high contrast", "Your dark hair/eyes read noticeably against your skin. You can carry more definition than you think — in brows, liner, and eye shadow — without it looking overdone."),
        "high":        ("High contrast", "Very dark features against lighter skin (or vice versa). You can wear bold definition and rich color — high-contrast faces carry more makeup than lower-contrast ones."),
    }
    contrast_label, contrast_desc = contrast_labels.get(contrast, ("Unknown", ""))

    st.markdown("### ✨ Your Profile")
    st.markdown(f"""
    **Contrast:** {contrast_label}  
    {contrast_desc}

    **Undertone:** {undertone.replace("-", " ").title()} · **Skin depth:** {depth}/5 · **Eye shape:** {eye_shape.title()}
    """)
    st.divider()

    sections = [
        ("🫧 Base", profile["base"]),
        ("🌙 Undereye", profile["undereye"]),
        ("🪮 Brows", profile["brows"]),
        ("👁️ Eyes", profile["eyes"]),
        ("✨ Lashes & Mascara", profile["mascara"]),
        ("💋 Lips", profile["lips"]),
        ("🛍️ At the Store", profile["store"]),
    ]

    for title, content in sections:
        with st.expander(title, expanded=True):
            st.markdown(content)

    # Export
    st.divider()
    export_text = "\n\n".join(
        f"## {title}\n{content}" for title, content in sections
    )
    st.download_button(
        label="Download your guide as .txt",
        data=export_text,
        file_name="my_makeup_guide.txt",
        mime="text/plain"
    )

    # AI Skill Page
    with st.expander("💡 Use your profile with AI — get a downloadable skill page", expanded=False):
        st.markdown("""
**Take your profile further with AI**

Download your Makeup Compass Skill Page — a plain-text file you can paste into any AI assistant
(ChatGPT, Claude, Gemini, etc.) as context. The AI will understand your full makeup profile and
can help you screen products, interpret swatch images, and get a second opinion on anything makeup-related.

**How to use it:**
1. Download the file and open it
2. Copy all the text
3. Paste it at the start of a new chat with your AI assistant of choice
4. Ask your question — or upload a swatch image and ask: *"Based on my profile, would this work for me?"*

You only need to paste it once per conversation. Save the file somewhere easy to find.

**Want it permanent?** If you have a paid plan, save it so the AI always knows your profile:
- 🟣 **Claude Pro/Max/Team** → [Claude Projects](https://claude.ai/projects) — create a project and upload the .txt as project knowledge ([how-to video](https://www.youtube.com/watch?v=GJ5jTgcbRHA))
- 🟢 **ChatGPT Plus** → [ChatGPT Skills](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) — paste your profile as a custom instruction ([how-to video](https://www.youtube.com/watch?v=QqwNue_KL-4))
- 🔵 **Gemini Advanced** → [Gemini Gems](https://gemini.google.com/gems) — create a Gem and paste your profile as context
        """)

        st.markdown("---")
        st.markdown("**Optional: personalise further with your own products**")
        st.caption(
            "Adding products you’ve tried makes the AI’s recommendations much more specific to you. "
            "Leave blank if you’re not sure yet — you can always edit the downloaded file."
        )

        works_for_me = st.text_area(
            "Products that work for me",
            placeholder="e.g. NARS Sheer Glow in Syracuse, Charlotte Tilbury Pillow Talk lip liner, Rare Beauty Soft Pinch blush in Joy...",
            help="List any products — foundation, concealer, lip colour, brow pencil, anything — that you know look good on you. One per line or comma-separated."
        )

        doesnt_work_for_me = st.text_area(
            "Products that haven’t worked for me",
            placeholder="e.g. anything too pink-toned, full coverage foundations, matte lip formulas, cool-toned concealers...",
            help="List products, shades, or whole categories that haven’t worked — too grey, too pink, too heavy, wrong undertone, etc."
        )

        st.markdown("---")
        st.markdown("**Optional: get looks built from products you already own**")
        st.caption(
            "Paste the products you own by category. The AI will use this to suggest specific looks "
            "using only what's in your kit — no shopping required. Leave blank to skip."
        )

        owned_products = st.text_area(
            "Products I own",
            placeholder=(
                "Lips: NYX Lip IV Hydrating Gloss Stain in Blush Rush\n"
                "Eyes: NYX Jumbo Eye Pencil in Frosting, Maybelline Color Tattoo Stix in I Am Cozy\n"
                "Blush: NYX Butter Melt Blush in U Know Butta\n"
                "Base: L'Oréal True Match Tinted Serum in 4.5-5.5 Rich Medium\n"
                "Powder: L'Oréal True Match Powder in W7 Caramel Beige"
            ),
            help="List by category (Lips, Eyes, Blush, Base, Brows, Undereye, Powder). "
                 "The AI will generate daytime and night-out looks using only these products.",
            height=150
        )

        skill_text = build_skill_page(
            depth=depth,
            undertone=undertone,
            eye_shape=eye_shape,
            contrast=contrast,
            lip_type=lip_type,
            coverage=coverage,
            dark_circles=dark_circles,
            lash_curl=lash_curl,
            lash_color=lash_color,
            lash_density=lash_density,
            works_for_me=works_for_me,
            doesnt_work_for_me=doesnt_work_for_me,
            owned_products=owned_products
        )

        st.download_button(
            label="⬇️ Download my AI Skill Page",
            data=skill_text,
            file_name="my_makeup_skill_page.txt",
            mime="text/plain"
        )

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/creator_mark.png", use_container_width=True)