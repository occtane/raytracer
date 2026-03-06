from pathlib import Path
import platform
import subprocess

build_dir = Path("build")

exe_name = "raytracer.exe" if platform.system() == "Windows" else "raytracer"

executable = list(build_dir.rglob(exe_name))

if not executable:
	print("No raytracer executable found.")
	exit()

# choose the newest build
executable.sort(key=lambda p: p.stat().st_mtime, reverse=True)

exe_path = executable[0]

print("Using executable:")
print(exe_path)

name = input("Enter image name: ")

output_dir = Path("Images")
output_dir.mkdir(exist_ok=True)

output_file = output_dir / f"{name}.ppm"

with open(output_file, "w") as f:
	subprocess.run([exe_path], stdout=f)

print("Image saved to: ", output_dir / name)
