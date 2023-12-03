import subprocess

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "update"])
subprocess.run(["git", "push", "origin", "main"])