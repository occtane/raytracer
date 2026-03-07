from pathlib import Path
import platform
import subprocess

script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent

exe_name = "raytracer.exe" if platform.system() == "Windows" else "raytracer"

search_dirs = [
	project_root / "build",
	project_root / "cmake-build-debug",
]

executable = []
for d in search_dirs:
	if d.exists():
		executable.extend(d.rglob(exe_name))

if not executable:
	print("No raytracer executable found.")
	print("Searched in:")
	for d in search_dirs:
		print(f" - {d}")
	exit()

# choose the newest build
executable.sort(key=lambda p: p.stat().st_mtime, reverse=True)

exe_path = executable[0]

print("Using executable:")
print(exe_path)

name = input("Enter image name: ")

output_dir = project_root / "Images"
output_dir.mkdir(exist_ok=True)

output_file = output_dir / f"{name}.ppm"

with open(output_file, "wb") as f:
	subprocess.run([str(exe_path)], stdout=f, check=True)

# On Windows, some workflows can produce UTF-16 encoded PPM files.
if platform.system() == "Windows":
	with open(output_file, "rb") as f:
		head = f.read(2)

	if head == b"\xff\xfe" or head == b"\xfe\xff":
		raw = output_file.read_bytes()
		text = raw.decode("utf-16")
		output_file.write_bytes(text.encode("ascii"))
		print("Detected UTF-16 PPM output and converted it to ASCII PPM.")

print("Image saved to:", output_file)
