
"""Proof-of-Resonance kernel (skeleton)

- RSP (Resonant Stability Point)
- non-linear alpha weighting
- stabilizer epsilon

Generated 2025-10-21 22:57:30Z
"""

from math import pow

def por(S: float, H: float, T: float, D: float, alpha: float = 1.2, eps: float = 1e-6) -> float:
    """PoR = (S * H * T)**alpha / (D + eps)"""
    return pow(S * H * T, alpha) / (D + eps)
