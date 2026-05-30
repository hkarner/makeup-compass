import streamlit as st

def render_welcome():
    st.image("assets/logo.png", width=280)
    st.image("assets/welcome_banner.png", use_container_width=True)
    st.title("🧭 Makeup Compass")

    st.markdown("""
    If you've ever felt lost in the makeup aisle — overwhelmed by options,
    unsure what actually works *for your specific features* — this is for you.

    Makeup Compass asks 10 questions about your features — plus a couple of short
    follow-ups depending on your answers — and gives you a personalized guide:
    what formats, finishes, and shade directions tend to work for you — and why.
    No specific products, no brand pressure, no rules. Just a clearer map.

    *Takes about 3–4 minutes. Your answers stay in your browser and are never stored.*
    """)

    # ── Start Button — top position so no scroll offset on transition ─────────
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Find My Direction →", use_container_width=True, type="primary"):
            st.session_state.started = True
            st.rerun()

    st.divider()

    # ── What You'll Get ───────────────────────────────────────────────────────
    st.subheader("What you'll get")
    st.markdown("""
    After answering 7 questions about your features, you'll receive a personalized guide covering:

    - 🪮 **Brows** — format, shade, and what to avoid
    - 👁️ **Eyes** — technique and finish for your eye shape
    - ✨ **Lashes & Mascara** — formula and technique for your lash type
    - 💋 **Lips** — format and shade family that works with your lip type
    - 🫧 **Base** — coverage approach and undertone guidance
    - 🌙 **Undereye** — correction technique based on your dark circle type
    - 🛍️ **At the Store** — words to look for and words to skip

    *Example: "Your two-toned lips do best with sheer, buildable formulas — avoid anything opaque or matte,
    which will flatten your natural lip gradient."*
    """)

    st.divider()

    # ── Before You Start ──────────────────────────────────────────────────────
    st.subheader("Before you start")
    st.markdown("""
    The quiz asks you to observe your own features. For the most accurate results:

    - 🪟 **Find natural light** — sit near a window or step outside. Overhead indoor lighting distorts skin tone.
    - 🪞 **Grab a mirror** — you'll need to look at your wrist veins and under-eye area.
    - 📄 **Grab two pieces of paper** — one white, one off-white or cream (for the undertone test).
    - 💧 **Remove makeup if possible** — or keep it minimal.
    """)

    st.caption("Not sure what undertone or contrast means? Open the 📚 Makeup 101 tab in the sidebar before you start.")