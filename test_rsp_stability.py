from por_engine.por_kernel import por

S, H, T = 0.9, 0.85, 1.0
alphas = [0.8, 1.0, 1.2, 1.5, 2.0]
distances = [1.0, 0.5, 0.2, 0.1, 0.01, 0.001]

print("🔬 Resonant Stability (RSP) Sensitivity Map\n")
for alpha in alphas:
    print(f"α = {alpha}")
    for D in distances:
        val = por(S, H, T, D, alpha)
        print(f"  D={D:<6} → PoR={val:.4f}")
    print()
