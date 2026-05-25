import streamlit as st
import sys
import os

# Make sure rules/ is importable
sys.path.insert(0, os.path.dirname(__file__))

from logic import build_profile
from seo import set_page_meta, inject_jsonld
from about_page import render_about
from welcome_page import render_welcome

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
    options=["💄 Quiz", "📖 About & Methodology"],
    label_visibility="collapsed"
)

if page == "📖 About & Methodology":
    render_about()
    st.stop()  # don't render the quiz on the About page

# ── Welcome screen ────────────────────────────────────────────────────────────
if not st.session_state.get("started", False):
    render_welcome()
    st.stop()

# ── Quiz ─────────────────────────────────────────────────────────────────────
st.title("🧭 Makeup Compass")
st.divider()

with st.form("quiz"):
    st.subheader("About You")

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

    undertone = st.radio(
        "2. Undertone",
        options=["warm", "neutral-warm", "neutral", "neutral-cool", "cool"],
        format_func=lambda x: {
            "warm":         "Warm — My wrist veins look green; gold jewelry flatters me more than silver",
            "neutral-warm": "Neutral-warm — Veins look blue-green; I lean toward gold but silver works too",
            "neutral":      "Neutral — Can't tell if veins are blue or green; gold and silver both look good",
            "neutral-cool": "Neutral-cool — Veins look blue-green; I lean toward silver but gold works too",
            "cool":         "Cool — My wrist veins look blue or purple; silver jewelry flatters me more than gold"
        }[x],
        help="Check the inside of your wrist in natural light for the vein test."
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
        }[x]
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
        }[x]
    )

    st.markdown(
        '<p style="font-size: 0.875rem; font-weight: 400; margin-bottom: 0.25rem;">6. Overall contrast level</p>',
        unsafe_allow_html=True
    )
    st.caption(
        "Contrast = how different your hair and eye color are from your skin in terms of depth (light vs. dark). "
        "Not about color — purely about how light or dark your features are compared to your skin."
    )
    contrast = st.radio(
        "6. Overall contrast level",
        options=["low", "medium", "medium-high", "high"],
        format_func=lambda x: {
            "low":         "Low — My hair, eyes, and skin are all similar in depth",
            "medium":      "Medium — Some difference between features, but nothing stark. Dark eyes or hair, but medium skin.",
            "medium-high": "Medium-high — Noticeably darker hair/eyes against my skin. My features read clearly from across a room.",
            "high":        "High — Very dark hair and eyes against light or very fair skin",
        }[x],
        index=1,
        label_visibility="collapsed",
        help="💡 Look at a no-makeup photo in natural light. Does your face have a stark light/dark pattern? High. Features blend together? Low. Something in between? Medium.",
    )

    lip_type = st.radio(
        "7. Lip type",
        options=["even", "two-toned", "thin", "full", "thin-two-toned"],
        format_func=lambda x: {
            "even":           "Even-toned — my lips are roughly one color",
            "two-toned":      "Two-toned — darker edges, lighter or pinker center",
            "thin":           "Thin — I have thinner lips (even-toned)",
            "full":           "Full — I have fuller lips (even-toned)",
            "thin-two-toned": "Thin and two-toned"
        }[x]
    )

    submitted = st.form_submit_button("Get My Guide →", use_container_width=True)

# ── Results ───────────────────────────────────────────────────────────────────
if submitted:
    profile = build_profile(
        depth=depth,
        undertone=undertone,
        eye_shape=eye_shape,
        contrast=contrast,
        lip_type=lip_type,
        coverage=coverage,
        dark_circles=dark_circles
    )

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