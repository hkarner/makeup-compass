def get_eyes(eye_shape, undertone, contrast):
    shape_rules = {
        "deep-set": (
            "Your eyes sit deep in the socket, which creates natural shadow on the lid. "
            "The goal is to bring the lid forward, not add more depth.\n\n"
            "- **Lid center:** Warm satin shimmer applied with a fingertip to the center of the lid only. "
            "This brings the lid forward against the natural socket shadow.\n"
            "- **Crease transition:** Warm taupe matte blended *upward above* the crease — never pressed into the socket.\n"
            "- **Inner corner:** A dab of warm champagne shimmer brightens the eye and counteracts the dark circle zone.\n"
            "- **Liner:** Soft brown pencil on the upper lash line only, smudged soft. Skip the wing — it curves downward on deep-set eyes.\n"
            "- **Lower lash line:** Skip entirely, or a soft warm brown smudge at the outer third only.\n"
            "- **Avoid:** Color pressed into the crease, brow bone highlight, glitter, black liner all around, saturated shadow."
        ),
        "hooded": (
            "Your lid is partially covered by the brow bone when eyes are open. "
            "Placement above the natural crease is everything.\n\n"
            "- **Lid:** Matte or satin mid-tone on the visible strip of lid. Avoid shimmer — it reflects off the hood.\n"
            "- **Crease:** Bring color *above* the natural crease line so it stays visible with eyes open.\n"
            "- **Liner:** Tight-line the upper waterline or apply a very thin line. Skip lower liner.\n"
            "- **Avoid:** Shimmer on the lid, dramatic cut crease, anything that visually closes the eye."
        ),
        "almond": (
            "Almond eyes are the most versatile shape — most techniques work well. "
            "Let undertone and contrast guide your shade choices.\n\n"
            "- **Lid:** Shimmer or matte, your preference.\n"
            "- **Crease:** Standard blending at the natural socket.\n"
            "- **Liner:** Upper only for a natural look; upper + lower outer third for more definition.\n"
            "- **Avoid:** Nothing shape-specific — focus on undertone-correct shades."
        ),
        "monolid": (
            "With no natural crease, color placement across the full lid is key.\n\n"
            "- **Lid:** Apply color across the entire lid in buildable layers. Shimmer at the center adds dimension.\n"
            "- **Transition:** Blend a slightly deeper shade above where a crease would be (high toward the brow bone).\n"
            "- **Liner:** Tight-line the upper lash line; graphic or floating liner also works well. Lower outer third optional.\n"
            "- **Avoid:** Standard Western crease blending technique — it won't show on your eye shape."
        ),
        "downturned": (
            "The outer corners angle downward. The goal is to visually lift them.\n\n"
            "- **Lid:** Shimmer or mid-tone across the lid.\n"
            "- **Outer corner:** Wing or flick liner upward, not following the natural downward direction.\n"
            "- **Lower lash line:** Skip, or a very light smudge at the inner two-thirds only. Outer lower liner pulls the eye down further.\n"
            "- **Avoid:** Heavy outer lower liner, anything that emphasizes the downward direction."
        ),
        "protruding": (
            "Your lids naturally project forward. Matte finishes recede the lid; shimmer brings it forward more.\n\n"
            "- **Lid:** Matte mid-tone in a warm or neutral family.\n"
            "- **Crease:** A slightly deeper matte shade creates shadow and adds depth.\n"
            "- **Liner:** Upper only; lower can be skipped.\n"
            "- **Avoid:** Shimmer on the lid center, very light or white liner on the waterline."
        ),
    }

    undertone_modifier = {
        "warm": "Shade family: warm browns, terracotta, peach, warm taupe.",
        "neutral-warm": "Shade family: warm browns, terracotta, peach, warm taupe.",
        "neutral": "Shade family: taupe, nude browns, soft grey-brown.",
        "neutral-cool": "Shade family: rose-brown, mauve-taupe, cool grey. Avoid orange-browns.",
        "cool": "Shade family: rose-brown, mauve-taupe, cool grey. Avoid orange-browns.",
    }

    contrast_modifier = {
        "low": "Keep it simple: one shadow all over, skip liner.",
        "medium": "Two-shadow look (lid + transition color); soft liner optional.",
        "medium-high": "Full technique as described above; liner recommended.",
        "high": "Full technique; liner can be slightly more defined.",
    }

    shape_text = shape_rules.get(eye_shape, shape_rules["almond"])
    undertone_text = undertone_modifier.get(undertone, undertone_modifier["neutral"])
    contrast_text = contrast_modifier.get(contrast, contrast_modifier["medium"])

    return (
        f"{shape_text}\n\n"
        f"**Shade direction:** {undertone_text}\n\n"
        f"**Intensity:** {contrast_text}"
    )