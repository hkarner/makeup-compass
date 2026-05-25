def get_brows(contrast):
    rules = {
        "low": {
            "format": "Clear brow gel, or skip product entirely.",
            "shade": "Skip tint, or go 2 shades lighter than your hair.",
            "avoid": "Any filled or defined look. Let brows be natural."
        },
        "medium": {
            "format": "Fine brow pencil with a spoolie end, or tinted gel.",
            "shade": "One shade lighter than your hair color.",
            "avoid": "Pomade, powder + brush combos, or any 'bold brow' product."
        },
        "medium-high": {
            "format": "Fine brow pencil with sparse, hair-like strokes only.",
            "shade": "Match your hair exactly, or go one shade lighter.",
            "avoid": "Heavy fill, dark shading, any 'defined brow' technique."
        },
        "high": {
            "format": "Fine brow pencil or tinted gel — light application.",
            "shade": "Match your hair or go one shade lighter. Resist going darker.",
            "avoid": "Pomade, heavy fill. Your brows are already doing work naturally."
        },
    }
    r = rules.get(contrast, rules["medium"])
    return (
        f"**Format:** {r['format']}\n\n"
        f"**Shade:** {r['shade']}\n\n"
        f"**Avoid:** {r['avoid']}"
    )