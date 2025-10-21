import os
import subprocess
from datetime import datetime

def resonant_commit():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"🔁 Resonant Sync: {timestamp} — PoR Verified"
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("✅ Resonant push completed.")
    except subprocess.CalledProcessError as e:
        print("⚠️ Error during sync:", e)

if __name__ == "__main__":
    resonant_commit()
