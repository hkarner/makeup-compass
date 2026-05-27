def get_lips(undertone, lip_type):
    format_rules = {
        "even": (
            "Good news: you have the most flexibility. Lip oil, tinted balm, gloss stain, "
            "or a sheer lipstick all work well. You can experiment with slightly more buildable coverage."
        ),
        "two-toned": (
            "Your lips have a natural two-tone gradient (darker at the edges, lighter at the center) — "
            "this is beautiful and worth enhancing, not covering. "
            "**Format is non-negotiable: sheer and buildable only.**\n\n"
            "Best formats: lip oil, gloss stain, tinted balm.\n\n"
            "Avoid: opaque lipstick (flattens your gradient), matte formula, full-coverage lip products."
        ),
        "thin": (
            "Avoid very dark shades — they visually shrink the lips. "
            "Gloss or shimmer finishes add optical volume. "
            "You can slightly overdraw the center cupid's bow if desired, but skip harsh lip liner all around."
        ),
        "full": (
            "You have latitude with shade depth — most formats work. "
            "If you don't want to emphasize volume further, avoid very dark + opaque combinations."
        ),
        "thin-two-toned": (
            "The most restrictive combination: sheer, warm-toned, and buildable is non-negotiable. "
            "Any matte, dark, or opaque product will flatten your natural gradient and make lips look smaller simultaneously. "
            "Best formats: tinted lip oil, sheer gloss stain."
        ),
        "full-two-toned": (
            "You have the volume to carry a range of formats, but the gradient still needs breathing room. "
            "Avoid fully opaque formulas that erase the natural variation — the two-tone is part of your look. "
            "Best formats: gloss stain, buildable sheer lipstick, tinted lip oil. "
            "You can go slightly deeper in shade than thin lips allow."
        ),
    }

    shade_rules = {
        "warm": {
            "yes": "warm peachy-pink, coral, warm nude-pink, warm rose, sheer warm berry",
            "avoid": "cool mauve, blue-pink, cool nude, blue-red"
        },
        "neutral-warm": {
            "yes": "MLBB nudes, peachy rose, warm pink, sheer warm berry",
            "avoid": "cool mauve, anything with a blue or grey base"
        },
        "neutral": {
            "yes": "true MLBB, soft rose, dusty pink (warm side), medium nude",
            "avoid": "strong cool tones; test soft mauves carefully"
        },
        "neutral-cool": {
            "yes": "soft mauve, cool rose, sheer berry, cool pink",
            "avoid": "orange-based nudes, warm peach"
        },
        "cool": {
            "yes": "cool pink, soft mauve, sheer berry, sheer plum, blue-red",
            "avoid": "warm peachy nudes, coral, orange-adjacent shades"
        },
    }

    fmt = format_rules.get(lip_type, format_rules["even"])
    shade = shade_rules.get(undertone, shade_rules["neutral"])

    return (
        f"**Format:** {fmt}\n\n"
        f"**Shade family to look for:** {shade['yes']}\n\n"
        f"**Shade family to avoid:** {shade['avoid']}"
    )