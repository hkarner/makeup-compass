import streamlit as st

def render_welcome():
    st.title("🧭 Makeup Compass")

    st.markdown("""
    If you've ever felt lost in the makeup aisle — overwhelmed by options,
    unsure what actually works *for your specific features* — this is for you.

    Makeup Compass asks 7 short questions about your features and gives you a
    personalized guide: what formats, finishes, and shade directions tend to work
    for you — and why. No specific products, no brand pressure, no rules.
    Just a clearer map.

    *Takes about 2 minutes. Your answers stay in your browser and are never stored.*
    """)

    st.divider()

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Find My Direction →", use_container_width=True, type="primary"):
            st.session_state.started = True
            st.rerun()