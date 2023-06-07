import shutil
import subprocess
import sys

def pip_install(package, output_folder):
    subprocess.check_call([sys.executable, "-m", "pip", "download", package, "--platform", "manylinux1_x86_64", "--platform", "win_amd64", "--platform", "win32", "--python-version", "3.10.8", "--only-binary=:all:", "-d", output_folder])
    subprocess.check_call([sys.executable, "-m", "pip", "download", package, "--platform", "manylinux1_x86_64", "--platform", "win_amd64", "--platform", "win32", "--python-version", "3.11", "--only-binary=:all:", "-d", output_folder])
    
print("Packaging Dependencies")
sdk_url = 'azure-ai-ml'
output_folder = "deps"
pip_install(sys.argv[1], output_folder)
subprocess.check_call(["piprepo", "build", output_folder])
shutil.make_archive(output_folder, "zip", output_folder)