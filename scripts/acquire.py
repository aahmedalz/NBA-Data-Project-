import hashlib
import shutil
import os

def sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

files = {
    "team_stats_traditional_rs.csv": "data/raw/team_stats_traditional_rs.csv",
    "team_stats_advanced_rs.csv": "data/raw/team_stats_advanced_rs.csv",
}

os.makedirs("data/raw", exist_ok=True)

checksums = {}
for src, dst in files.items():
    shutil.copy(src, dst)
    checksums[dst] = sha256(dst)
    print(f"Copied {src} -> {dst}")
    print(f"  SHA-256: {checksums[dst]}")

with open("data/raw/checksums.txt", "w") as f:
    for path, checksum in checksums.items():
        f.write(f"{checksum}  {path}\n")

print("\nChecksums saved to data/raw/checksums.txt")
