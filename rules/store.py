def get_store(undertone):
    rules = {
        "warm": {
            "look_for": "warm, golden, peachy, coral, terracotta, honey, W-coded",
            "avoid": "cool, rosy, pink-based, ashy, C-coded",
            "philosophy": "Skip the cool half of the swatch wall entirely — it cuts your decision fatigue in half."
        },
        "neutral-warm": {
            "look_for": "warm, golden, peachy, W-coded or neutral-leaning warm",
            "avoid": "cool, C-coded, overtly pink or rosy",
            "philosophy": "When in doubt between warm and neutral, test warm first."
        },
        "neutral": {
            "look_for": "neutral, N-coded, natural, balanced",
            "avoid": "strongly warm OR strongly cool — test both extremes before committing",
            "philosophy": "You have the most flexibility but also the most decisions. Test on your face, not your hand."
        },
        "neutral-cool": {
            "look_for": "cool, N or C-coded, pink-neutral, rosy",
            "avoid": "warm, golden, peachy, W-coded",
            "philosophy": "When in doubt between cool and neutral, test cool first."
        },
        "cool": {
            "look_for": "cool, C-coded, pink, rosy, blue-based",
            "avoid": "warm, golden, peachy, W-coded, orange-adjacent",
            "philosophy": "Skip the warm side of the swatch wall entirely — orange tones will fight your undertone."
        },
    }

    r = rules.get(undertone, rules["neutral"])
    return (
        f"**Look for:** *{r['look_for']}*\n\n"
        f"**Avoid:** *{r['avoid']}*\n\n"
        f"**One rule:** {r['philosophy']}\n\n"
        "**Universal tip:** Always swatch finalists on your face or jawline in natural light — "
        "never on the back of your hand. The two-tone difference is large enough to be misleading."
    )