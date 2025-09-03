from pathlib import Path

workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)
file_path = workspace /"notes.txt"
print(file_path)

#creating or overwrite using 'w'
f = open(file_path, "w", encoding = "utf-8")
f.write("This is the first line in notes.txt\n")
f.close()