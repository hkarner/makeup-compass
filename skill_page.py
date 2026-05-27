# skill_page.py
# Generates a plain-text LLM skill page from quiz inputs.
# Used by app.py — call build_skill_page() and pass to st.download_button().

def build_skill_page(depth, undertone, eye_shape, contrast, lip_type, coverage, dark_circles, lash_curl="wavy", lash_color="dark", lash_density="average", works_for_me="", doesnt_work_for_me="", owned_products=""):
    """Returns a plain-text skill page string for the given profile."""

    depth_labels = {
        1: "1 out of 5 (fair — very light skin)",
        2: "2 out of 5 (light-medium — light skin, may tan slightly)",
        3: "3 out of 5 (medium — tan or olive tone)",
        4: "4 out of 5 (medium-deep — brown skin tone)",
        5: "5 out of 5 (deep — deep brown or ebony skin tone)",
    }

    undertone_blocks = {
        "warm": (
            "I lean warm. Products with yellow, peach, golden, or olive undertones work best.\n"
            "Watch for: pink, rosy, cool, or ash undertones — these tend to clash or look grey on me.\n"
            "If a swatch pulls pink or lavender in the pan, it may not translate well on me.\n"
            "Product label clues — good: W, Y, Golden, Peach, Tan, Caramel.\n"
            "Product label clues — flag: C, P, Pink, Rose, Cool."
        ),
        "neutral-warm": (
            "I'm neutral-warm — I lean slightly warm but have good flexibility.\n"
            "Yellow, peach, and golden tones look natural; I can also pull off some neutral pinks.\n"
            "Products labeled W, N, or NW are usually a good starting point.\n"
            "Strongly cool or ashy products may pull slightly grey on me."
        ),
        "neutral": (
            "I'm neutral — I can wear both warm and cool products.\n"
            "Products labeled N or Neutral, or those in the middle of a brand's range, tend to work well.\n"
            "I have the most shade flexibility of any undertone."
        ),
        "neutral-cool": (
            "I'm neutral-cool — I lean slightly cool but have good flexibility.\n"
            "Pink, rose, and soft taupe tones look natural; I can also pull off some neutral warms.\n"
            "Products labeled C, N, or NC are usually a good starting point.\n"
            "Very warm or strongly golden products may pull slightly orange on me."
        ),
        "cool": (
            "I lean cool. Products with pink, rose, beige, or blue-based undertones work best.\n"
            "Watch for: orange, yellow, or strongly golden undertones — these can look muddy on me.\n"
            "Product label clues — good: C, P, Pink, Rose, Beige.\n"
            "Product label clues — flag: W, Y, Golden, Warm."
        ),
    }

    depth_notes = {
        1: "I need the lightest shades. Look for: porcelain, ivory, fair, or shade 10–20 in numbered ranges.",
        2: "I need light to light-medium shades. Look for: light, nude, sand, or shade 20–30.",
        3: "I need medium shades. Look for: medium, beige, tan, or shade 30–40.",
        4: "I need medium-deep shades. Look for: medium-deep, caramel, mocha, or shade 40–50.",
        5: "I need the deepest shades. Look for: deep, espresso, ebony, or shade 50–60+.",
    }

    contrast_blocks = {
        "low": (
            "My contrast is low — my hair, eyes, and skin are close in depth.\n"
            "Soft, blended looks suit me best. Heavy pigment can overwhelm my colouring.\n"
            "I look best in enhancing products rather than defining ones.\n"
            "Strong liner or a bold lip can look costume-y unless carefully balanced."
        ),
        "medium": (
            "My contrast is medium — some difference between features, but nothing stark.\n"
            "I have flexibility between soft everyday looks and slightly more defined ones.\n"
            "I can wear some definition in brows and eyes without it looking overdone."
        ),
        "medium-high": (
            "My contrast is medium-high — my features read noticeably against my skin.\n"
            "I can carry more definition than I might expect — bold brows, defined liner, richer pigments all work.\n"
            "Soft or barely-there products may disappear on me; I often need a slightly more pigmented hand."
        ),
        "high": (
            "My contrast is high — very dark features against lighter skin (or vice versa).\n"
            "I can wear bold definition and rich colour without it looking overdone.\n"
            "Strong brows, graphic liner, and opaque lip colours all suit me."
        ),
    }

    eye_blocks = {
        "deep-set": (
            "My eyes are deep-set — they sit back in the socket; the brow bone casts shadow on the lid.\n"
            "Lighter, brightening shades on the lid help counteract the natural shadow.\n"
            "Avoid heavy dark shades all over the lid — eyes can recede further.\n"
            "Upper lash liner works well; tight-lining the waterline can make eyes look smaller."
        ),
        "hooded": (
            "My eyes are hooded — the brow bone partially covers the lid when my eyes are open.\n"
            "Look for long-wearing shadow formulas; shadow tends to transfer to the brow bone.\n"
            "Matte or satin finishes on the lid look cleaner than heavy shimmer.\n"
            "Wing and liner work best placed slightly above the visible lid crease."
        ),
        "almond": (
            "My eyes are almond-shaped — classic proportions with a visible lid crease.\n"
            "Most techniques and formulas work well; I have the most flexibility of any eye shape.\n"
            "I can wear diffused or precise liner placement without it looking off."
        ),
        "monolid": (
            "I have a monolid — little or no visible lid crease.\n"
            "Graphic liner and bold lid colour show up well on my eye shape.\n"
            "Crease-focused techniques designed for a visible crease won't translate the same way.\n"
            "I may need to layer shadow more heavily, as the lid isn't visible when eyes are open."
        ),
        "downturned": (
            "My eyes are downturned — outer corners angle slightly downward.\n"
            "Upward-sweeping liner and shadow that flicks upward at the outer corner suit me best.\n"
            "Avoid heavy colour or liner that droops at the outer corner — it emphasises the droop."
        ),
        "protruding": (
            "My eyes are protruding — my lids appear to project forward.\n"
            "Matte or satin finishes are more flattering than high shimmer.\n"
            "Deeper shades in the socket help create depth; avoid frosty finishes all over the lid."
        ),
    }

    dark_circle_blocks = {
        "none": "I don't have significant dark circles. A standard concealer that matches my skin tone works fine.",
        "mild": (
            "I have mild dark circles. A light-coverage concealer one shade lighter than my skin tone is usually enough.\n"
            "Match the undertone of the concealer to my undertone — no colour corrector needed."
        ),
        "blue-purple": (
            "I have blue-purple dark circles.\n"
            "I need peachy or salmon-toned concealers — not pink, not pure yellow.\n"
            "A peach or salmon corrector underneath concealer neutralises the blue-purple tone.\n"
            "Flag: pink-leaning concealers will make my circles look more purple, not less."
        ),
        "brown": (
            "I have brown dark circles — pigmentation-based, not vascular.\n"
            "An orange or peach corrector neutralises brown pigment before concealer.\n"
            "Look for a concealer that matches my skin tone exactly, or one shade lighter.\n"
            "Very light concealers will look ashy or chalky under my eyes."
        ),
        "mixed": (
            "I have mixed dark circles — blue-purple at the inner corner, brown underneath.\n"
            "Spot-correct: peach/salmon at the inner corner, orange-peach underneath for the brown.\n"
            "A neutral-warm concealer over top tends to unify both.\n"
            "Avoid pink-leaning concealers — they worsen the inner-corner circles."
        ),
    }

    lip_blocks = {
        "even": (
            "My lips are even-toned throughout.\n"
            "I can wear sheer, buildable, or opaque formulas without worrying about uneven coverage.\n"
            "Heavy lip liner isn't necessary unless I want to define the shape."
        ),
        "two-toned": (
            "My lips are two-toned — darker edges, lighter or pinker centre.\n"
            "Sheer or glossy formulas may show unevenness; buildable or opaque are more forgiving.\n"
            "A lip liner in my lip shade or slightly deeper helps even out the border first."
        ),
        "thin": (
            "I have thinner lips.\n"
            "Glossy, sheer, or light-reflecting formulas help create the appearance of fullness.\n"
            "Very dark or fully matte formulas can make lips appear smaller — use intentionally."
        ),
        "full": (
            "I have fuller lips.\n"
            "I can wear any formula — matte, gloss, stain — without it looking too heavy.\n"
            "Deeper, bolder shades tend to look especially striking on me."
        ),
        "thin-two-toned": (
            "I have thinner lips that are also two-toned.\n"
            "A lip liner to define and even the border helps before applying colour.\n"
            "Light-reflecting or sheer formulas add volume; very dark mattes can make lips look smaller and uneven."
        ),
    }

    coverage_blocks = {
        "none": (
            "I skip base entirely — bare-skin approach.\n"
            "Base product recommendations are not relevant for me."
        ),
        "skin-like": (
            "I want skin-like or barely-there coverage — just a hint of evening out.\n"
            "Skin tints, tinted moisturisers, and skin-finish foundations are my zone.\n"
            "Avoid full-coverage or matte formulas."
        ),
        "light": (
            "I prefer light coverage — evened out without looking like makeup.\n"
            "Light-coverage foundations, tinted moisturisers, and BB creams work well.\n"
            "Dewy or natural finish preferred over matte."
        ),
        "medium": (
            "I prefer medium coverage — enough to cover minor unevenness without a full mask.\n"
            "Medium-coverage foundations with a natural or satin finish are my zone.\n"
            "I can blend down a full-coverage formula with a damp sponge when needed."
        ),
        "full": (
            "I prefer full coverage — thorough coverage of unevenness, redness, or discolouration.\n"
            "Full-coverage foundations and concealers are what I'm looking for.\n"
            "Setting with powder helps full coverage last longer and look less heavy."
        ),
    }

    mascara_curl_blocks = {
        "straight": (
            "My lashes are straight — curling before mascara is essential.\n"
            "Waterproof formula is strongly recommended: the only formula that reliably holds curl on straight lashes.\n"
            "Confirmed options: L'Oréal Voluminous Carbon Black Waterproof, Maybelline Sky High Waterproof.\n"
            "Tubing mascara (L'Oréal Double Extend Beauty Tubes) is a good everyday alternative — "
            "slides off cleanly with warm water, no rubbing."
        ),
        "wavy": (
            "My lashes have a slight natural curl — curling before application helps but isn't mandatory.\n"
            "Waterproof or tubing formula both work well.\n"
            "Tubing mascara (e.g. L'Oréal Double Extend Beauty Tubes) removes cleanly with warm water."
        ),
        "curly": (
            "My lashes are naturally curly — curl retention isn't a priority.\n"
            "Tubing mascara is ideal: coats each lash, removes with warm water, doesn't weigh down the curl.\n"
            "Waterproof is an option for long-wear events."
        ),
    }

    mascara_density_notes = {
        "sparse":  "Sparse lashes — a formula with some volumizing alongside lengthening helps build visible density.",
        "average": "Average lash density — lengthening or volumizing formulas both work.",
        "full":    "Full lashes — lengthening preferred; heavy volumizing can cause clumping.",
    }

    mascara_color_notes = {
        "light": "Light lashes — mascara shade is noticeable. Black for definition; brown-black for a softer natural look.",
        "dark":  "Dark lashes — formula matters more than shade. Black and brown-black are both fine.",
    }

    swatch_prompts = [
        '"Based on my profile, does this shade\'s undertone work for me?"',
        '"Would this concealer correct my dark circles or make them look worse?"',
        '"This product looks [warm/cool/pink] in the pan — is that likely to work for my undertone?"',
        '"I\'m between two shades — which is more likely to suit my depth and undertone?"',
        '"This is labeled [Cool/Warm/Neutral Beige] — is that a flag or a match for me?"',
        '"Is this lip shade likely to look natural or bold on my colouring?"',
    ]

    lines = [
        "# MY MAKEUP COMPASS SKILL PAGE",
        "# Generated by Makeup Compass · makeup-compass.streamlit.app",
        "# " + "\u2500" * 55,
        "# HOW TO USE THIS FILE",
        "# Paste this entire document into a new AI chat before asking makeup questions.",
        "# The AI will use this as your profile context for any question or product screen.",
        "#",
        "# To screen a product: paste this, upload a swatch image, and ask:",
        '#   "Based on my profile, would this shade work for me?"',
        "# " + "\u2500" * 55,
        "",
        "## MY PROFILE SUMMARY",
        "",
        f"Skin depth:          {depth_labels.get(depth, str(depth))}",
        f"Undertone:           {undertone.replace('-', ' ').title()}",
        f"Eye shape:           {eye_shape.replace('-', ' ').title()}",
        f"Contrast level:      {contrast.replace('-', ' ').title()}",
        f"Lip type:            {lip_type.replace('-', ' ').title()}",
        f"Coverage preference: {coverage.replace('-', ' ').title()}",
        f"Dark circles:        {dark_circles.replace('-', ' ').title()}",
        f"Lash curl:           {lash_curl.title()}",
        f"Lash color:          {lash_color.title()}",
        f"Lash density:        {lash_density.title()}",
        "",
        "## WHAT MY PROFILE MEANS FOR PRODUCT SCREENING",
        "",
        f"### Undertone \u2014 {undertone.replace('-', ' ').title()}",
        undertone_blocks.get(undertone, ""),
        "",
        f"### Skin Depth \u2014 {depth}/5",
        depth_notes.get(depth, ""),
        "",
        f"### Contrast \u2014 {contrast.replace('-', ' ').title()}",
        contrast_blocks.get(contrast, ""),
        "",
        f"### Eye Shape \u2014 {eye_shape.replace('-', ' ').title()}",
        eye_blocks.get(eye_shape, ""),
        "",
        f"### Dark Circles \u2014 {dark_circles.replace('-', ' ').title()}",
        dark_circle_blocks.get(dark_circles, ""),
        "",
        f"### Lip Type \u2014 {lip_type.replace('-', ' ').title()}",
        lip_blocks.get(lip_type, ""),
        "",
        f"### Coverage \u2014 {coverage.replace('-', ' ').title()}",
        coverage_blocks.get(coverage, ""),
        "",
        "### Lashes & Mascara",
        mascara_curl_blocks.get(lash_curl, ""),
        mascara_density_notes.get(lash_density, ""),
        mascara_color_notes.get(lash_color, ""),
        "",
        "## SUGGESTED QUESTIONS TO ASK",
        "",
    ]

    for p in swatch_prompts:
        lines.append(f"- {p}")

    lines += [
        "",
        "# " + "\u2500" * 55,
        "# END OF SKILL PAGE",
        "# " + "\u2500" * 55,
    ]

    # Optional: owned products + look suggestions
    if owned_products and owned_products.strip():
        lines += [
            "",
            "## LOOKS FROM MY KIT",
            "",
            "### My Owned / Confirmed Products",
            owned_products.strip(),
            "",
            "### Instructions for AI — Generating Looks From This Kit",
            "Using ONLY the products listed above, suggest specific looks for me.",
            "Rules:",
            "- Do not recommend products I don't own. If a category has no owned product, omit it or say 'nothing in kit'.",
            "- Follow all profile rules: deep-set eye technique (light on lid center, NOT in crease, NOT on brow bone), warm undertone only, sheer + buildable lip format, one feature elevated at a time.",
            "- Suggest at minimum: a daytime look and a night-out look, using only what's available.",
            "- For each look, list exactly: product name + placement instruction. No filler.",
            "- If the kit has gaps (e.g. no confirmed base), note the gap and suggest the closest substitute from what's available.",
            "",
            "### Suggested Prompts to Use With This Section",
            '- "Using only my kit products, build me a daytime look."',
            '- "Using only my kit products, what\'s the most polished night-out look I can do?"',
            '- "I only have 5 minutes — what\'s the minimum from my kit that still looks put together?"',
            '- "I want to feature my lips tonight using only what I own — what look does that build to?"',
        ]
    else:
        lines += [
            "",
            "## LOOKS FROM MY KIT",
            "",
            "### My Owned / Confirmed Products",
            "(Paste your owned products here by category, e.g.:",
            " Lips: NYX Lip IV Hydrating Gloss Stain in Blush Rush",
            " Eyes: NYX Jumbo Eye Pencil in Frosting, Maybelline Color Tattoo Stix in I Am Cozy",
            " Blush: NYX Butter Melt Blush in U Know Butta)",
            "",
            "### Instructions for AI — Generating Looks From This Kit",
            "Once the product list above is filled in: using ONLY those products, suggest specific looks.",
            "Rules:",
            "- Do not recommend products I don't own. If a category has no owned product, omit it or say 'nothing in kit'.",
            "- Follow all profile rules: deep-set eye technique (light on lid center, NOT in crease, NOT on brow bone), warm undertone only, sheer + buildable lip format, one feature elevated at a time.",
            "- Suggest at minimum: a daytime look and a night-out look, using only what's available.",
            "- For each look, list exactly: product name + placement instruction. No filler.",
        ]

    # Optional: user's own product references
    if works_for_me and works_for_me.strip():
        lines += [
            "",
            "## PRODUCTS I KNOW WORK FOR ME",
            works_for_me.strip(),
        ]
    else:
        lines += [
            "",
            "## PRODUCTS I KNOW WORK FOR ME",
            "(Add yours here: foundation shades, lip colours, concealers, etc. that you know look good on you.)",
        ]

    if doesnt_work_for_me and doesnt_work_for_me.strip():
        lines += [
            "",
            "## PRODUCTS THAT HAVEN'T WORKED FOR ME",
            doesnt_work_for_me.strip(),
        ]
    else:
        lines += [
            "",
            "## PRODUCTS THAT HAVEN'T WORKED FOR ME",
            "(Add yours here: products, shades, or categories that were the wrong undertone, too heavy, too grey, etc.)",
        ]

    return "\n".join(lines)