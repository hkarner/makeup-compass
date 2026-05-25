def get_base(depth, undertone, coverage):
    coverage_text = {
        "skip": (
            "Skipping base is a completely legitimate strategy, not a compromise. "
            "Instead: targeted undereye correction (if needed) + a touch of warm blush. "
            "This approach often reads more natural than foundation on medium-to-deep skin tones."
        ),
        "skin-like": (
            "Look for: skin tint, tinted moisturizer, or serum foundation. "
            "Key descriptors to find on the label: *warm, golden, peachy, satin, skin-like, natural finish.* "
            "Avoid labels that say: *rosy, pink-based, cool, full coverage, matte.*"
        ),
        "light": (
            "Look for: lightweight foundation, buildable tinted serum, or a layered skin tint. "
            "Depth tip: test one shade deeper than the obvious choice — "
            "medium shades frequently read too light and drain warmth once applied."
        ),
        "medium": (
            "Look for: foundation with a natural or satin finish. Avoid full matte formulas — "
            "they flatten the skin and amplify undertone mismatch. "
            "Depth tip: go warm-coded within your shade range. "
            "In L'Oréal True Match, W = warm (correct direction); N = neutral (will likely drain warmth)."
        ),
        "full": (
            "Look for: full-coverage foundation or high-coverage serum foundation. "
            "Key descriptors: *full coverage, buildable, long-wear, warm, golden*. "
            "Avoid labels that say: *rosy, pink-based, cool, dewy* — undertone rules still apply at full coverage. "
            "Application tip: use a damp beauty sponge for a more skin-like finish even at full coverage."
        ),
    }

    undertone_key = {
        "warm": ("W, golden, peach, olive", "C, cool, rosy, pink-based"),
        "neutral-warm": ("W or N (test both), lean toward golden", "C, cool"),
        "neutral": ("N, neutral, balanced", "strong C (cool) or strong W (warm) — test both ends"),
        "neutral-cool": ("N or C, pink-neutral", "W, warm golden, orange-toned"),
        "cool": ("C, pink, rose", "W, golden, warm, orange-toned"),
    }

    depth_note = ""
    if depth >= 3:
        depth_note = (
            "\n\n**Depth tip:** At your skin tone depth, medium shades frequently read too light "
            "and drain warmth after application. Always test one step deeper than the obvious choice "
            "before committing."
        )

    cov = coverage_text.get(coverage, coverage_text["skin-like"])
    codes = undertone_key.get(undertone, undertone_key["neutral"])

    return (
        f"**Approach:** {cov}\n\n"
        f"**Undertone coding key** — Look for: *{codes[0]}* · Avoid: *{codes[1]}*"
        f"{depth_note}"
    )