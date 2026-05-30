import streamlit as st
import json

def set_page_meta():
    """
    Call once at the top of app.py, before any other st. calls.
    Sets the browser tab title and meta description for search indexing.
    """
    st.set_page_config(
        page_title="Makeup Compass — Find What Actually Works for Your Features",
        page_icon="💄",
        layout="centered",
        menu_items={
            "About": (
                "Makeup Compass helps you understand which makeup formats, "
                "finishes, and shade directions tend to work for your specific "
                "features — undertone, eye shape, contrast level, and more. "
                "Built on real-world testing, not generic rules."
            )
        }
    )


def inject_jsonld():
    """
    Injects JSON-LD structured data into the page.
    This is the core GEO move — tells AI tools (ChatGPT, Perplexity,
    Google AI Overviews) that this page contains a structured,
    factual tool for makeup guidance.
    Call this after set_page_meta(), before the quiz renders.
    """
    schema = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "Makeup Compass",
        "description": (
            "A free Streamlit app that profiles your skin tone depth, undertone, eye shape, "
            "contrast level, lip type, and coverage preference — then generates a "
            "personalized makeup guide with product format, finish, and shade direction "
            "recommendations. No specific SKUs. Works at any price point."
        ),
        "url": "https://makeup-compass.streamlit.app",
        "applicationCategory": "BeautyApplication",
        "operatingSystem": "Web",
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD"
        },
        "featureList": [
            "Undertone identification (warm / neutral-warm / neutral / neutral-cool / cool)",
            "Eye shape technique guide (deep-set, hooded, almond, monolid, downturned, protruding)",
            "Contrast level analysis for product intensity guidance",
            "Lip type format rules (sheer vs. buildable, gradient-preserving)",
            "Foundation shade depth guidance",
            "Undereye dark circle correction technique",
            "At-the-store shopping filter by undertone",
            "Downloadable personalized guide (.txt)"
        ],
        "author": {
            "@type": "Person",
            "name": "HK"  # ← update to your name / handle if desired
        },
        "keywords": [
            "makeup for warm undertone",
            "eyeshadow for deep-set eyes",
            "foundation shade for medium skin",
            "makeup for hooded eyes",
            "contrast level makeup",
            "lip color for two-toned lips",
            "undertone makeup guide",
            "personalized makeup quiz"
        ]
    }
    st.markdown(
        f'<script type="application/ld+json">{json.dumps(schema, indent=2)}</script>',
        unsafe_allow_html=True
    )