def get_undereye(dark_circles, depth, dark_circle_location="everywhere", deep_set_subtype="uniform"):
    if dark_circles in ("none", "mild"):
        return (
            "No targeted correction needed. Eye cream as a hydrating base before any "
            "eye product is sufficient. Skip undereye concealer entirely."
        )

    # Corrector shade based on depth
    if depth <= 2:
        corrector_shade = "peach"
    elif depth <= 4:
        corrector_shade = "peach-to-orange (test which neutralizes better on your skin)"
    else:
        corrector_shade = "orange"

    # Location-specific application instructions
    if dark_circle_location == "inner":
        application_note = (
            "**Application zone:** Your dark circles are concentrated at the inner corner near the nose. "
            "Apply corrector as a targeted dab at the inner corner only — do not sweep across the full undereye. "
            "Set with a matte eyeshadow that matches your skin tone, blending outward to meet bare skin naturally. "
            "Note: inner corner dark circles often have a blue/purple cast regardless of overall type — "
            "peach corrector is typically right here even if you selected 'brown' overall."
        )
    elif dark_circle_location == "outer":
        application_note = (
            "**Application zone:** Your dark circles are concentrated at the outer corner. "
            "Apply corrector to the outer third of the undereye only. "
            "Blend inward toward center to avoid a visible edge at the outer corner."
        )
    else:  # full or everywhere
        application_note = (
            "**Application zone:** Apply corrector across the full undereye in a soft half-moon shape. "
            "Set with a matte eyeshadow that matches your skin tone exactly across the full zone."
        )

    base_protocol = (
        f"1. Apply eye cream and let it fully absorb (2–3 minutes). "
        f"This prevents cream products from migrating into fine lines.\n"
        f"2. Pat (do not rub) a **{corrector_shade} cream corrector** onto the dark area. "
        f"Patting keeps the product where you placed it.\n"
        f"3. Set immediately with a **matte eyeshadow that matches your skin tone exactly.** "
        f"This neutralizes without adding brightness — unlike concealer, which reads too pale.\n\n"
        f"{application_note}\n\n"
        f"**Why not concealer?** Concealers are formulated 1–2 shades lighter than skin to 'brighten,' "
        f"but on medium-to-deep warm skin tones this reads dramatically pale and obvious. "
        f"The corrector + skin-tone-matched powder approach is technically more accurate.\n\n"
        f"**Avoid:** Liquid or serum base products under the eye — they migrate into fine lines by evening. "
        f"Always set the corrector with powder before it can move."
    )

    if dark_circles == "mixed":
        note = (
            "\n\n**Mixed circles tip:** Apply corrector selectively — "
            "heavier at the inner corner (blue/purple zone), lighter hand under the outer area (brown zone)."
        )
        base_protocol = base_protocol + note

    # Cross-variable flag: deep-set inner corner + dark circles at inner corner = highest priority step
    if deep_set_subtype == "inner" and dark_circle_location == "inner":
        priority_note = (
            "\n\n**⭐ Priority note for your eye shape:** Because both your deepest socket point AND "
            "your dark circles are concentrated at the inner corner, this is your single highest-impact step. "
            "Inner corner work — corrector + a warm champagne shimmer pencil (like NYX Frosting) — does double duty: "
            "it corrects the dark circle AND fills the deepest shadow pocket. "
            "If you only do one thing in your eye routine, do this."
        )
        base_protocol = base_protocol + priority_note

    return base_protocol