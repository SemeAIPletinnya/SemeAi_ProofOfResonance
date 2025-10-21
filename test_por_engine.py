from por_engine.por_kernel import por

# Тестові дані
tests = [
    (0.9, 0.8, 1.0, 0.2),
    (0.7, 0.9, 0.95, 0.1),
    (1.0, 1.0, 1.0, 0.001),
    (0.5, 0.5, 0.5, 0.1),
]

print("🔬 Proof-of-Resonance Kernel Test Results:")
for i, (S, H, T, D) in enumerate(tests, 1):
    result = por(S, H, T, D)
    print(f"Test {i}: PoR({S}, {H}, {T}, {D}) = {result:.4f}")

