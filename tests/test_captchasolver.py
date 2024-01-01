from captchasolver.captchasolver import CAPTCHASolver

from .utils import encoded_image

captchasolver = CAPTCHASolver()


def test_captchasolver() -> None:
    """
    Test that CAPTCHASolver solves the CAPTCHA correctly.
    """
    assert captchasolver.solve(encoded_image) == "2ag2h"
