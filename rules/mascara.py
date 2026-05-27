def get_mascara(eye_shape, lash_curl, lash_color, lash_density, dark_circles="none"):
    """
    Returns personalized mascara guidance.

    eye_shape:    "deep-set" | "hooded" | "almond" | "monolid" | "downturned" | "protruding"
    lash_curl:    "straight" | "wavy" | "curly"
    lash_color:   "dark" | "light"
    lash_density: "sparse" | "average" | "full"
    dark_circles: "none" | "mild" | "blue-purple" | "brown" | "mixed"
    """

    lines = []

    # ── Curl + formula recommendation ─────────────────────────────────────────
    if lash_curl == "straight":
        curl_note = (
            "**Always curl before applying mascara** — straight lashes recede easily, especially on deep-set eyes. "
            "A curler lifts them into visibility before any product goes on.\n\n"
            "**Formula: Waterproof is strongly recommended.** Waterproof is the only formula that reliably locks "
            "curl on straight lashes — regular mascara will not hold it. "
            "Confirmed options: L'Oréal Voluminous Carbon Black Waterproof, Maybelline Sky High Waterproof.\n\n"
            "**Alternative: Tubing mascara** (e.g. L'Oréal Double Extend Beauty Tubes) coats each lash individually "
            "and slides off cleanly with warm water, no rubbing required. A gentler everyday option "
            "if curl hold is less critical."
        )
    elif lash_curl == "wavy":
        curl_note = (
            "Curling before applying helps open the eye and set the shape, even with some natural curl. "
            "Not mandatory, but recommended.\n\n"
            "**Formula:** Waterproof or tubing both work well. "
            "Tubing mascara (e.g. L'Oréal Double Extend Beauty Tubes) is a solid everyday choice — "
            "removes easily with warm water, no rubbing."
        )
    else:  # curly
        curl_note = (
            "You have naturally curly lashes — curl retention isn't your primary concern.\n\n"
            "**Formula: Tubing mascara is ideal** (e.g. L'Oréal Double Extend Beauty Tubes). "
            "Tubes coat each lash individually and slide off cleanly with warm water — "
            "no formula weight to pull down the natural curl. "
            "Waterproof is an option for long-wear days or events."
        )

    lines.append(curl_note)
    lines.append("")

    # ── Lengthening vs. volumizing ────────────────────────────────────────────
    if eye_shape in ("deep-set", "hooded"):
        if lash_density == "sparse":
            formula_note = (
                "**Formula type: Lengthening with a light volumizing boost.** "
                "Sparse lashes can use some density, but heavy volumizing on "
                f"{'deep-set' if eye_shape == 'deep-set' else 'hooded'} eyes can read as clumpy "
                "in the shadowed socket area. A lengthening formula with mild volume is the right balance."
            )
        else:
            formula_note = (
                "**Formula type: Lengthening over volumizing.** "
                f"{'Deep-set' if eye_shape == 'deep-set' else 'Hooded'} eyes already have natural shadow — "
                "heavy volumizing adds bulk that can read as spider-y. "
                "Lengthening extends lashes upward and outward, which opens the eye without adding visual weight."
            )
    elif eye_shape == "downturned":
        formula_note = (
            "**Formula type: Lengthening + curl hold.** "
            "Curling and lengthening both help counteract the downward angle of the lash line. "
            "A waterproof formula is useful here to maintain the lifted shape throughout the day."
        )
    else:
        if lash_density == "sparse":
            formula_note = (
                "**Formula type: Volumizing or lengthening — your call.** "
                "Sparse lashes benefit from volumizing to build density. "
                "Lengthening also works well to extend what's there."
            )
        elif lash_density == "full":
            formula_note = (
                "**Formula type: Lengthening preferred.** "
                "Full lashes don't need more volume — a lengthening formula extends and separates "
                "without overloading. Heavy volumizing on full lashes can clump."
            )
        else:  # average
            formula_note = (
                "**Formula type: Lengthening or volumizing both work.** "
                "Average density gives you flexibility — choose based on the look you want."
            )

    lines.append(formula_note)
    lines.append("")

    # ── Color guidance ────────────────────────────────────────────────────────
    if lash_color == "light":
        color_note = (
            "**Shade:** Your lashes are naturally light, so mascara color makes a visible difference. "
            "**Black** creates defined, high-contrast lashes. **Brown-black** reads softer and more natural — "
            "a good everyday option if you want definition without the full contrast of pure black."
        )
    else:
        color_note = (
            "**Shade:** With naturally dark lashes, color matters less than formula. "
            "Black and brown-black are both fine — focus on formula type and application."
        )

    lines.append(color_note)
    lines.append("")

    # ── Placement ─────────────────────────────────────────────────────────────
    if eye_shape in ("deep-set", "hooded"):
        placement_note = (
            "**Placement: Upper lashes only as your default.** "
            "Lower lash mascara on deep-set or hooded eyes tends to draw attention to the undereye shadow zone "
            "rather than frame the eye. Skip lower lashes, or use a very light hand at the outer third only."
        )
    elif eye_shape == "downturned":
        placement_note = (
            "**Placement:** Focus on upper lashes and angle the wand slightly upward at the outer corner "
            "to counteract the natural downward direction. "
            "Lower lash mascara can pull the eye down further — skip or limit to the inner two-thirds only."
        )
    else:
        placement_note = (
            "**Placement:** Upper and lower lashes both work well. "
            "Wiggle the wand at the root and sweep upward for maximum lift."
        )

    lines.append(placement_note)

    # ── Dark circles interaction ──────────────────────────────────────────────
    if dark_circles in ("blue-purple", "brown", "mixed"):
        lines.append("")
        lines.append(
            "**Undereye note:** You have dark circles — use a **waterproof or tubing formula** "
            "to prevent smudging into the corrected undereye zone. A non-waterproof formula can migrate "
            "by midday and undo the color correction work underneath."
        )

    # ── Universal tip ─────────────────────────────────────────────────────────
    lines.append("")
    lines.append(
        "*Application tip: Wiggle the wand at the root and sweep upward. "
        "Never pump the wand in and out of the tube — it pushes air in, dries the formula faster, "
        "and introduces bacteria.*"
    )

    return "\n".join(lines)