from rules.brows import get_brows
from rules.eyes import get_eyes
from rules.lips import get_lips
from rules.base import get_base
from rules.undereye import get_undereye
from rules.store import get_store

def build_profile(depth, undertone, eye_shape, contrast, lip_type, coverage, dark_circles):
    """
    Takes raw quiz answers and returns a dict of personalized
    recommendation strings, one per category.
    """
    return {
        "brows": get_brows(contrast),
        "eyes": get_eyes(eye_shape, undertone, contrast),
        "lips": get_lips(undertone, lip_type),
        "base": get_base(depth, undertone, coverage),
        "undereye": get_undereye(dark_circles, depth),
        "store": get_store(undertone),
    }