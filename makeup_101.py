import streamlit as st

def render_makeup_101():
    st.title("📚 Makeup 101")
    st.caption("A plain-language reference for anyone new to makeup terms. Read this before taking the quiz if you're not sure how to answer a question.")

    # ── Before You Start ──────────────────────────────────────────────────────
    st.subheader("Before You Start: How to Prepare")
    st.markdown("""
    The quiz asks you to observe your own features. Getting this right matters —
    the better your answers, the more accurate your guide.

    **What you'll need:**
    - A mirror
    - Natural light — sit near a window or step outside. Avoid overhead indoor lighting;
      it distorts skin tone and shadow.
    - A white piece of paper *and* an off-white or cream piece (for the undertone test)
    - No makeup on, or as little as possible

    **The two most important tests:**
    """)

    with st.expander("🔍 The Vein Test (for undertone)"):
        st.markdown("""
        Look at the inside of your wrist in natural light.

        - Veins look **green or olive** → you're likely **warm**
        - Veins look **blue or purple** → you're likely **cool**
        - Can't tell — looks blue-green or both → you're likely **neutral**

        *Tip: Don't overthink it. If you're genuinely unsure, neutral-warm is the most common starting point for medium skin tones.*
        """)

    with st.expander("🔍 The Paper Test (for undertone)"):
        st.markdown("""
        Hold a **white** piece of paper next to your bare face. Then swap it for an **off-white or cream** piece.

        - If your skin looks clearer and more defined against the **white** paper → you likely lean **cool**
        - If your skin looks more alive and natural against the **cream** paper → you likely lean **warm**
        - If there's no noticeable difference → you're likely **neutral**

        *This test works best in natural light. Store lighting will give you a false read.*
        """)

    st.divider()

    # ── Glossary ──────────────────────────────────────────────────────────────
    st.subheader("Key Terms Explained")

    with st.expander("🎨 Undertone — warm, neutral, cool"):
        st.markdown("""
        Undertone is the subtle hue *beneath* your skin's surface. It doesn't change with a tan or in different lighting — it's permanent.

        - **Warm** — yellow, peachy, or golden undertones. Coral blushes tend to look more natural than pink ones.
        - **Cool** — pink, rosy, or bluish undertones. Silver jewelry tends to look more natural than gold.
        - **Neutral** — a mix of both. Most products work well.
        - **Neutral-warm / Neutral-cool** — a slight lean in one direction, but with flexibility.

        **Why it matters:** A product with the wrong undertone can make your skin look grey, washed out, or slightly off — even if the depth (lightness/darkness) is exactly right.
        """)

    with st.expander("💡 Skin Depth — the 1–5 scale"):
        st.markdown("""
        Skin depth is simply how light or dark your skin is, on a scale of 1 (fair) to 5 (deep).

        - **1 — Fair:** Very light skin, burns easily, rarely tans
        - **2 — Light-medium:** Light skin that may tan slightly in summer
        - **3 — Medium:** Tan or olive tone, tans fairly easily
        - **4 — Medium-deep:** Brown skin tone
        - **5 — Deep:** Deep brown or ebony skin tone

        **Why it matters:** It determines which shade range to shop in for base products, concealer, and depth of lip color.
        """)

    with st.expander("⚡ Contrast Level"):
        st.markdown("""
        Contrast is how different your hair and eye color are from your skin tone — purely in terms of light vs. dark depth, not about color.

        - **Low contrast:** Hair, eyes, and skin are all similar in depth (e.g., light hair, light eyes, light skin — or all deep tones)
        - **Medium contrast:** Some difference between features, but nothing stark
        - **Medium-high contrast:** Noticeably darker hair/eyes against your skin
        - **High contrast:** Very dark hair and eyes against light or very fair skin

        **Tip:** Look at a no-makeup photo in natural light. Do your hair and eyes jump out sharply against your skin? That's higher contrast. Do they blend softly in? That's lower contrast.

        **Why it matters:** Higher contrast faces can carry more definition (bolder brows, more liner) without looking overdone. Lower contrast faces look best with softer, more blended approaches.
        """)

    with st.expander("💧 Coverage"):
        st.markdown("""
        Coverage refers to how much a base product (foundation, tinted moisturizer, skin tint) evens out your skin.

        - **Skin-like / Barely there:** Just a hint of evening out — your skin still looks like skin
        - **Light coverage:** Smooths minor unevenness without looking like you're wearing much
        - **Medium coverage:** Covers discoloration and unevenness while still looking natural
        - **Full coverage:** Thorough coverage of redness, hyperpigmentation, or significant unevenness
        - **Skip base:** No base product at all — bare skin or targeted correction only

        **Why it matters:** Using too much coverage can look heavy or mask-like. Using too little may not address what you want to address. Neither is wrong — it's personal preference.
        """)

    with st.expander("👁️ Eye Shapes"):
        st.markdown("""
        - **Deep-set:** Eyes sit back in the socket; the brow bone naturally casts shadow on the lid. *The most common shape people misidentify.*
        - **Hooded:** The brow bone partially covers the lid when eyes are open. The lid seems to disappear.
        - **Almond:** Classic shape with a visible lid and clear crease. The most common shape overall.
        - **Monolid:** Little or no visible crease. Common in East Asian features.
        - **Downturned:** Outer corners angle slightly downward.
        - **Protruding:** Lids appear to project forward from the face.

        **Not sure?** Look straight ahead in a mirror. If you can see your full lid and a clear crease line: almond. If your brow bone covers part of your lid when your eyes are open: hooded. If you have no crease at all: monolid. If you're genuinely unsure, almond is the most common and a reasonable default.
        """)

    with st.expander("🌙 Dark Circles"):
        st.markdown("""
        Dark circles come in different types, and the correction technique depends on the type:

        - **Blue/purple:** Caused by blood vessels showing through thin under-eye skin. Needs a **peach or salmon** color corrector to neutralize.
        - **Brown:** Caused by pigmentation (melanin). Needs an **orange or peach** corrector.
        - **Mixed:** Blue/purple at the inner corner, brown underneath. Needs spot correction with both.
        - **Mild:** Light shadowing. A concealer close to your skin tone is usually enough.
        - **None:** Lucky you — a standard foundation or nothing works fine.

        **Tip:** Check in natural light. The inner corner is usually where blue/purple shows up first.
        """)

    with st.expander("💋 Lip Types"):
        st.markdown("""
        - **Even-toned:** Your lips are roughly one consistent color all over.
        - **Two-toned:** Darker edges, lighter or pinker center. Very common — this is the natural lip gradient many people have.
        - **Thin:** Naturally thinner lips.
        - **Full:** Naturally fuller lips.

        **Why it matters:** Two-toned lips interact differently with lip products. Opaque or heavily pigmented products flatten the natural gradient and can look off. Sheer and buildable formulas work with it instead of against it.
        """)

    with st.expander("🏷️ How to Read Product Labels"):
        st.markdown("""
        Brands use letter codes and descriptor words to signal undertone. Once you know these, shopping gets much faster.

        **Undertone codes:**
        - **W or Warm** → warm undertone (yellow/golden/peachy)
        - **C or Cool** → cool undertone (pink/rosy/blue-based)
        - **N or Neutral** → neutral undertone
        - **NW** → neutral-warm | **NC** → neutral-cool

        **Words that signal warm:**
        Golden, Peach, Caramel, Honey, Sand, Tan, Beige (warm beige), Bronze

        **Words that signal cool:**
        Rose, Pink, Porcelain, Ivory (sometimes), Ashy, Nude (often cool-leaning)

        **Words that signal neutral:**
        Natural, Buff, Bisque, Medium Beige

        **General rule:** If a shade looks orange-toned or golden in the pan, it's likely warm. If it looks pink, rosy, or dull/grey in the pan, it's likely cool or neutral. This pan-color signal is often more reliable than the label.
        """)

    with st.expander("✨ Mascara — formulas, curl, and application"):
        st.markdown("""
        **Always curl before applying mascara** — never after. Curling after mascara can cause the curler to stick to the lashes and pull them out.

        **Formula types:**
        - **Waterproof:** Locks curl and resists smudging. The only formula that reliably holds curl on straight lashes. Needs an oil-based or micellar remover — pat, don't rub.
        - **Tubing mascara:** Coats each lash in tiny polymer tubes rather than pigment. Slides off cleanly with warm water — no rubbing, no lash loss. Best everyday option for anyone who struggles with removal. *(Confirmed example: L'Oréal Double Extend Beauty Tubes)*
        - **Regular (non-waterproof):** Easiest removal, least curl hold. Fine if your lashes have natural curl or longevity isn't a concern.

        **Lengthening vs. volumizing:**
        - **Lengthening:** Extends lashes outward and upward. Best for deep-set and hooded eyes — heavy volumizing can look clumpy in a shadowed socket.
        - **Volumizing:** Adds thickness and density. Best for sparse lashes. Avoid on full lashes — can overload them and clump.

        **Application tip:** Wiggle the wand at the root and sweep upward. Never pump the wand in and out of the tube — it pushes air in, dries the formula faster, and introduces bacteria.

        **Lower lashes:** On deep-set or hooded eyes, lower lash mascara tends to emphasize undereye shadow rather than frame the eye. When in doubt, skip it or apply a very light hand at the outer third only.
        """)

    st.divider()
    st.caption("These are general guidelines, not absolute rules. Individual products vary, and swatching on your face in natural light is always the final test.")