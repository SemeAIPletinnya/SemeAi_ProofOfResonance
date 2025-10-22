#!/bin/bash
echo "🔁 Starting Resonant Auto-Sync..."

timestamp=$(date +"%Y-%m-%d %H:%M:%S")
git add .
git commit -m "🔁 Resonant Auto-Sync — $timestamp"
git push origin main

echo "✅ Resonant push completed successfully at $timestamp"
