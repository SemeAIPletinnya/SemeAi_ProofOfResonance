import pandas as pd
from por_core import ProofOfResonance

# Очікує файл misc/semeai_resonance_cores.csv (у тебе він є)
cores = pd.read_csv("misc/semeai_resonance_cores.csv")

por = ProofOfResonance(alpha=1.1)
rows = []
for _, r in cores.iterrows():
    # Просте моделювання значень (можна замінити реальними вимірами)
    S, H, T, D = 0.80, 0.85, 0.90, 0.10
    score = por.compute(S, H, T, D)
    rows.append((r.Core_Name, round(score, 3), por.interpret(score)))

df = pd.DataFrame(rows, columns=["Core", "PoR Index", "Interpretation"])
print("\n🜂 Resonance Simulation Results")
print(df.to_string(index=False))
