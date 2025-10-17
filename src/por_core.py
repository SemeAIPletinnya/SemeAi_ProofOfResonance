import numpy as np

class ProofOfResonance:
    """((S × H × T) ^ α) / (D + ε)"""
    def __init__(self, alpha: float = 1.0, epsilon: float = 1e-6):
        self.alpha = alpha
        self.epsilon = epsilon
    def compute(self, S: float, H: float, T: float, D: float) -> float:
        from numpy import clip
        return float(clip(((S * H * T) ** self.alpha) / (D + self.epsilon), 0, 1))
    def interpret(self, v: float) -> str:
        return ("Perfect Resonance — Coherent Harmony" if v >= 0.9 else
                "Stable Resonance — Aligned Frequencies" if v >= 0.7 else
                "Partial Resonance — Needs Recalibration" if v >= 0.4 else
                "Low Resonance — Dissonant Field")

if __name__ == "__main__":
    por = ProofOfResonance(alpha=1.2)
    idx = por.compute(S=0.85, H=0.90, T=0.80, D=0.10)
    print(f"PoR Index: {idx:.3f} → {por.interpret(idx)}")
