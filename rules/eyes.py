def get_eyes(eye_shape, undertone, contrast, deep_set_subtype="uniform", hooded_subtype="outer", lid_discoloration="none"):

    # ── Deep-set sub-type branching ──────────────────────────────────────────
    if eye_shape == "deep-set":
        if deep_set_subtype == "inner":
            shape_text = (
                "Your eyes sit deep in the socket, with the **inner corner as the most recessed point** — "
                "creating a cavernous shadow pocket near the nose. This is your highest-impact zone.\n\n"
                "- **Inner corner (most critical):** A generous dab of warm champagne shimmer here is doing structural work — "
                "filling the deepest shadow pocket and counteracting the blue/purple dark circle zone. Never skip or underdo this step.\n"
                "- **Lid center:** Warm satin shimmer applied with a fingertip. Brings the lid forward against the natural socket shadow.\n"
                "- **Outer corner:** Your outer lid is covered by the fold from above, but not recessed into the face — "
                "shimmer placed on the visible lid surface near the outer corner *does* catch light. "
                "Place product on the lid surface itself, not tucked under the fold.\n"
                "- **Crease transition:** Warm taupe matte blended *upward above* the crease — never pressed into the socket.\n"
                "- **Liner:** Soft brown pencil on the upper lash line only, smudged soft. Skip the wing.\n"
                "- **Lower lash line:** Skip, or a soft warm brown smudge at outer third only.\n"
                "- **Avoid:** Color pressed into the crease, brow bone highlight, glitter, black liner all around."
            )
        elif deep_set_subtype == "outer":
            shape_text = (
                "Your eyes sit deep in the socket, with the **outer corner most covered by the lid fold**. "
                "Shimmer tucked into the outer corner will disappear under the fold.\n\n"
                "- **Lid center:** Warm satin shimmer applied with a fingertip. This is your primary light zone.\n"
                "- **Inner corner:** A dab of warm champagne shimmer brightens the eye and counteracts the dark circle zone.\n"
                "- **Outer corner:** Concentrate shimmer on the center and inner two-thirds of the lid only. "
                "Avoid shimmer at the outer corner — it sits under the fold and won't catch light.\n"
                "- **Crease transition:** Warm taupe matte blended *upward above* the crease — never pressed into the socket.\n"
                "- **Liner:** Soft brown pencil on the upper lash line only, smudged soft. Taper off before the outer corner.\n"
                "- **Lower lash line:** Skip, or a soft warm brown smudge at the inner two-thirds only.\n"
                "- **Avoid:** Shimmer tucked under the outer fold, brow bone highlight, glitter, black liner all around."
            )
        else:  # uniform (default)
            shape_text = (
                "Your eyes sit uniformly deep in the socket, with the brow bone casting shadow across the lid. "
                "The goal is to bring the lid forward, not add more depth.\n\n"
                "- **Lid center:** Warm satin shimmer applied with a fingertip to the center of the lid. "
                "Brings the lid forward against the natural socket shadow.\n"
                "- **Inner corner:** A dab of warm champagne shimmer brightens the eye and counteracts the dark circle zone.\n"
                "- **Crease transition:** Warm taupe matte blended *upward above* the crease — never pressed into the socket.\n"
                "- **Liner:** Soft brown pencil on the upper lash line only, smudged soft. Skip the wing.\n"
                "- **Lower lash line:** Skip, or a soft warm brown smudge at outer third only.\n"
                "- **Avoid:** Color pressed into the crease, brow bone highlight, glitter, black liner all around, saturated shadow."
            )

    # ── Hooded sub-type branching ─────────────────────────────────────────────
    elif eye_shape == "hooded":
        if hooded_subtype == "full":
            shape_text = (
                "Your lid fold covers most or all of the visible lid when your eyes are open. "
                "Most technique work happens **above the fold**, not in the traditional lid zone.\n\n"
                "- **Shimmer:** Place above the fold line so it stays visible when eyes are open. "
                "Traditional lid placement disappears under the fold.\n"
                "- **Crease:** This is your primary definition zone — blend a transition color above the fold. "
                "This is what reads as the eye's main feature from the front.\n"
                "- **Liner:** Very thin line on the upper lash line only, or skip entirely. "
                "Thick liner on a fully hooded lid is invisible and can make the eye look smaller.\n"
                "- **Lower lash line:** Skip — adds visual weight without adding definition.\n"
                "- **Avoid:** Heavy shimmer in the traditional lid position (disappears under the fold), "
                "thick liner, dramatic cut crease, anything that visually closes the eye."
            )
        else:  # outer (default)
            shape_text = (
                "The outer corner of your lid is covered by the brow bone fold, but your **center and inner lid are visible** "
                "when eyes are open. This is more common than full hooding — and often mistaken for almond eyes.\n\n"
                "- **Lid center and inner lid:** This is your workable shimmer zone. Apply warm satin shimmer here.\n"
                "- **Outer corner:** Keep shimmer away from the outer corner where the fold begins — "
                "product placed there gets hidden and can visually drag the eye down.\n"
                "- **Liner:** Apply on the visible upper lash line and taper off before the outer corner. "
                "Don't follow the lash line all the way to the corner — the fold will hide it and create a drooping effect.\n"
                "- **Crease:** Blend a transition color just above where the fold sits — this is visible from the front.\n"
                "- **Avoid:** Liner extending to the outer corner, shimmer at the outer corner, dramatic cut crease."
            )

    # ── All other shapes ──────────────────────────────────────────────────────
    else:
        shape_rules = {
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
        shape_text = shape_rules.get(eye_shape, shape_rules["almond"])

    undertone_modifier = {
        "warm":         "Shade family: warm browns, terracotta, peach, warm taupe.",
        "neutral-warm": "Shade family: warm browns, terracotta, peach, warm taupe.",
        "neutral":      "Shade family: taupe, nude browns, soft grey-brown.",
        "neutral-cool": "Shade family: rose-brown, mauve-taupe, cool grey. Avoid orange-browns.",
        "cool":         "Shade family: rose-brown, mauve-taupe, cool grey. Avoid orange-browns.",
    }

    contrast_modifier = {
        "low":         "Keep it simple: one shadow all over, skip liner.",
        "medium":      "Two-shadow look (lid + transition color); soft liner optional.",
        "medium-high": "Full technique as described above; liner recommended.",
        "high":        "Full technique; liner can be slightly more defined.",
    }

    undertone_text = undertone_modifier.get(undertone, undertone_modifier["neutral"])
    contrast_text = contrast_modifier.get(contrast, contrast_modifier["medium"])

    result = (
        f"{shape_text}\n\n"
        f"**Shade direction:** {undertone_text}\n\n"
        f"**Intensity:** {contrast_text}"
    )

    if lid_discoloration == "partial":
        result += (
            "\n\n**Lid discoloration (thin eyelid skin — often called dark circles):**\n"
            "The discoloration at your inner corner and/or lid center is caused by thin skin over "
            "blood vessels — not the same as undereye dark circles. "
            "Apply a light press of peach/orange corrector (same product as your undereye step) "
            "to the inner corner and lid center with your fingertip — one thin layer. "
            "Then place your warm satin shimmer directly over it. "
            "Skip matte powder on the lid — it deepens socket shadow on deep-set eyes."
        )
    elif lid_discoloration == "full":
        result += (
            "\n\n**Lid discoloration — full lid (thin eyelid skin, often called dark circles):**\n"
            "Your eyelid skin is thin enough that blood vessels show through across the entire lid — "
            "this reads as brownish or blue-gray discoloration and is consistently misidentified as dark circles. "
            "Apply a thin press of peach/orange corrector (same product as your undereye step) "
            "across your full upper lid with your fingertip before any other eye product. "
            "Then place your warm shimmer at the inner corner and lid center as usual — "
            "corrector and shimmer are two separate steps, using the same corrector across a larger zone. "
            "Skip matte powder on the lid entirely — it absorbs light and deepens the socket shadow."
        )

    return result