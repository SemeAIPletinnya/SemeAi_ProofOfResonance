"""Minimal Proof-of-Resonance kernel.

This is a lightweight, readable baseline that exposes the core signals:
- coherence
- drift
- phase locking
- silence gate
"""

from dataclasses import dataclass


def clamp(value: float, min_value: float = 0.0, max_value: float = 1.0) -> float:
    return max(min_value, min(max_value, value))


@dataclass(frozen=True)
class ResonanceInputs:
    signal: float
    harmony: float
    timing: float
    baseline: float
    energy: float


@dataclass(frozen=True)
class ResonanceOutputs:
    coherence: float
    drift: float
    phase_lock: float
    silence_gate: float
    resonance: float


def compute_coherence(signal: float, harmony: float, timing: float) -> float:
    return clamp(signal * harmony * timing)


def compute_drift(signal: float, baseline: float) -> float:
    return clamp(abs(signal - baseline))


def compute_silence_gate(energy: float, threshold: float = 0.2) -> float:
    return 0.0 if energy < threshold else 1.0


def compute_phase_lock(coherence: float, drift: float) -> float:
    return clamp(coherence - drift)


def por_kernel(inputs: ResonanceInputs) -> ResonanceOutputs:
    coherence = compute_coherence(inputs.signal, inputs.harmony, inputs.timing)
    drift = compute_drift(inputs.signal, inputs.baseline)
    silence_gate = compute_silence_gate(inputs.energy)
    phase_lock = compute_phase_lock(coherence, drift)
    resonance = clamp(phase_lock * silence_gate)
    return ResonanceOutputs(
        coherence=coherence,
        drift=drift,
        phase_lock=phase_lock,
        silence_gate=silence_gate,
        resonance=resonance,
    )


if __name__ == "__main__":
    default_inputs = ResonanceInputs(
        signal=0.85,
        harmony=0.9,
        timing=0.95,
        baseline=0.8,
        energy=0.4,
    )
    result = por_kernel(default_inputs)
    print(result)
