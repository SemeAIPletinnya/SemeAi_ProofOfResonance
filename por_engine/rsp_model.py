
"""RSP Hypothesis module (skeleton). Generated 2025-10-21 22:57:30Z."""

def stability_point(series: list[float]) -> float:
    """Return a toy stability point metric for a series."""
    if not series:
        return 0.0
    return sum(series) / (len(series) + 1.0)
