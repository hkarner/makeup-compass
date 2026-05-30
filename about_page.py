import streamlit as st

def render_about():
    st.image("assets/about_makeup_compass_banner.png", use_container_width=True)
    st.title("🧭 About Makeup Compass")

    st.markdown("""
    ## What this quiz does

    Makeup Compass asks 7 questions about your features and generates a 
    personalized guide covering:

    - **Brows** — format, shade rule, what to avoid
    - **Eyes** — technique for your eye shape, shade direction, liner guidance
    - **Lips** — format (sheer vs. buildable) and shade family for your undertone
    - **Base** — coverage approach, undertone coding key, shade depth note
    - **Undereye** — dark circle correction technique based on circle type and skin depth
    - **At the Store** — words to look for and avoid by undertone

    No specific products are recommended. Descriptions focus on format, finish, and 
    shade direction — so the guide works at any price point and stays useful even 
    as specific products come and go.

    ---

    ## The framework: why these 7 questions

    Most makeup advice fails because it's generic. The questions in this quiz target 
    the specific variables that actually determine whether a product looks right on your face:

    ### Undertone
    Your skin's underlying color temperature — warm (yellow/peach/golden), neutral, or cool 
    (pink/blue). This is the single most important filter for every product category. 
    A warm-undertone person wearing cool-toned products will look "off" or drained regardless 
    of how beautiful the color looks in the pan.

    **How to identify yours:** Hold a peach/coral blush near your face, then a pink/mauve one. 
    The one that makes your face look more alive is your undertone direction.

    ### Skin tone depth
    How light or deep your skin is on a 1–5 scale. Depth affects which shade range to shop 
    within, and also determines undereye corrector color (peach vs. orange).

    **Key insight:** For depths 3–5, medium shades frequently read too light and drain warmth. 
    Always test one step deeper than the obvious choice.

    ### Eye shape
    Deep-set, hooded, almond, monolid, downturned, or protruding eyes each have different 
    placement rules. The same technique that works beautifully on almond eyes can completely 
    disappear on a deep-set eye, or close up a hooded eye.

    **Example:** Deep-set eyes sit back in the socket, so the lid is already in natural shadow. 
    Shimmer on the lid center brings it forward. Pressing color into the crease adds more 
    darkness where there's already too much. The fix is counterintuitive until you understand 
    the geometry.

    ### Contrast level
    The relative difference between your hair/eye depth and your skin tone. High-contrast 
    coloring can carry more defined makeup. Low-contrast coloring is overwhelmed by it. 
    This is why makeup that looks stunning on one person looks harsh on another with similar features.

    ### Lip type
    Even-toned vs. two-toned (darker at the edges, lighter at the center) determines format 
    rules more than shade does. Two-toned lips have a natural gradient that opaque or matte 
    products flatten and erase. Sheer and buildable formats enhance the gradient instead.

    ### Coverage preference
    Affects which base product category to shop. Includes the option to skip base entirely — 
    which, for medium-to-deep skin tones especially, is often the most natural-looking approach.

    ### Dark circles
    Type (blue/purple vs. brown vs. mixed) determines corrector color. Depth determines 
    whether peach or orange is the right corrector shade. Standard concealer (formulated 
    1–2 shades lighter than skin) reads obviously pale on medium-to-deep skin — this quiz 
    recommends a corrector + skin-tone-matched powder technique instead.

    ---

    ## How the recommendations are generated

    All logic is static — a set of if/then rules derived from real-world testing and 
    established makeup artistry principles. There is no AI model making predictions. 
    Your answers map directly to pre-written guidance for each feature combination.

    No data is collected or stored. Your quiz answers never leave your browser session.

    ---

    ## Why "no specific products"?

    Products get discontinued. Formulas change. What's available varies by location and 
    price point. Describing *what to look for* ("sheer, buildable, warm peachy-pink gloss 
    stain") rather than naming a specific SKU means the guide stays useful for years — 
    and works whether you're shopping at a drugstore or a department counter.

    When a specific product is mentioned as an example, it's labeled as a reference point, 
    not a prescription.

    ---

    ## Quick reference: undertone shopping filters

    | Undertone | Look for | Avoid |
    |---|---|---|
    | Warm | W-coded, golden, peachy, coral | C-coded, cool, rosy, pink-based |
    | Neutral-warm | W or N (test), golden lean | C-coded, cool |
    | Neutral | N-coded, balanced | Strong warm or cool extremes |
    | Neutral-cool | N or C, pink-neutral | W-coded, warm golden |
    | Cool | C-coded, pink, rosy | W-coded, golden, peach |

    ---

    ## Quick reference: eye shapes

    | Shape | Key rule | What to avoid |
    |---|---|---|
    | Deep-set | Satin shimmer on lid center; blend crease color *upward above* socket | Color in the crease; brow bone highlight; glitter |
    | Hooded | Place color above the natural crease so it's visible when eyes are open | Shimmer on lid (reflects off the hood); cut crease |
    | Almond | Most techniques work; let undertone guide shades | Nothing shape-specific |
    | Monolid | Color across full lid in layers; blend transition above where crease would be | Standard Western crease technique |
    | Downturned | Wing liner upward; avoid outer lower liner | Heavy outer lower liner; anything that pulls the corner down |
    | Protruding | Matte finishes recede the lid; deeper matte in crease | Shimmer on lid center; white liner on waterline |
    """)