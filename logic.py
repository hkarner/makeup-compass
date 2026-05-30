from rules.brows import get_brows
from rules.eyes import get_eyes
from rules.lips import get_lips
from rules.base import get_base
from rules.undereye import get_undereye
from rules.store import get_store
from rules.mascara import get_mascara

def build_profile(
    depth, undertone, eye_shape, contrast, lip_type, coverage, dark_circles,
    deep_set_subtype="uniform", hooded_subtype="outer", dark_circle_location="everywhere", lid_discoloration="none",
    lash_curl="wavy", lash_color="dark", lash_density="average"
):
    """
    Takes raw quiz answers and returns a dict of personalized
    recommendation strings, one per category.

    Optional sub-type params (from follow-up questions):
      deep_set_subtype:     "uniform" | "inner" | "outer"
      hooded_subtype:       "outer" | "full"
      dark_circle_location: "inner" | "full" | "outer" | "everywhere"
      lid_discoloration: "none" | "partial" | "full"

    Lash params (from quiz Q8–Q10):
      lash_curl:    "straight" | "wavy" | "curly"
      lash_color:   "dark" | "light"
      lash_density: "sparse" | "average" | "full"
    """
    return {
        "brows": get_brows(contrast),
        "eyes": get_eyes(
            eye_shape, undertone, contrast,
            deep_set_subtype=deep_set_subtype,
            hooded_subtype=hooded_subtype,
            lid_discoloration=lid_discoloration,
        ),
        "mascara": get_mascara(
            eye_shape=eye_shape,
            lash_curl=lash_curl,
            lash_color=lash_color,
            lash_density=lash_density,
            dark_circles=dark_circles,
        ),
        "lips": get_lips(undertone, lip_type),
        "base": get_base(depth, undertone, coverage),
        "undereye": get_undereye(
            dark_circles, depth,
            dark_circle_location=dark_circle_location,
            deep_set_subtype=deep_set_subtype,
        ),
        "store": get_store(undertone),
    }