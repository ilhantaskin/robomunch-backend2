import sys

version = sys.argv[1]
with open("VERSION", "w") as f:
    f.write(version + "\n")
print(f"Version bumped to {version}")
