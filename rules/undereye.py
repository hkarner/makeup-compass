def get_undereye(dark_circles, depth):
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

    base_protocol = (
        f"1. Apply eye cream and let it fully absorb (2–3 minutes). "
        f"This prevents cream products from migrating into fine lines.\n"
        f"2. Pat (do not rub) a **{corrector_shade} cream corrector** onto the dark area. "
        f"Patting keeps the product where you placed it.\n"
        f"3. Set immediately with a **matte eyeshadow that matches your skin tone exactly.** "
        f"This neutralizes without adding brightness — unlike concealer, which reads too pale.\n\n"
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
        return base_protocol + note

    return base_protocol