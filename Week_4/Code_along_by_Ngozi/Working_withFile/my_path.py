# # This is how it works
# # Using os.getcwd()

# # import os

# # # Get the current working directory

# # print("Current working directory:", os.getcwd())

# # # Ensure to check the output

# # Absolute path example
# absolute_path = r"C:\Users\ncc73\Desktop\GEN_AI\Week_4\Code_along_by_Ngozi\Working_withFile\my_path.py"

# # Relative path example
# relative_path = "Week_4\Code_along_by_Ngozi\Working_withFile\my_path.py"

# print("Absolute Path:", absolute_path)
# print("Relative Path:", relative_path)

# import os

# folder = "Week_4\Code_along_by_Ngozi\Working_withFile"
# filename = "my_path.py"

# # path = os.join(folder, filename)
# path = os.path.join(folder, filename)
# print("Full path:", path)

# # #This way, Python handles slashes (/ vs \) automatically.

# import os

# path = "my_path.py"
# if os.path.exists(path):
#     print("Yes, the file exists!")
# else:
#     print("File not found.")


from pathlib import Path
print("current directory:", Path.cwd()) 

file = Path("my_path.py")

print("File exits:", file.exists())

folder = Path("C:/Users/ncc73/Desktop/GEN_AI")
full_path = folder / "my_path.py"
print("Full path:", full_path)

from pathlib import Path 

print("Parent folder:", Path.cwd().parent)

for file in Path.cwd().iterdir():
    print(file)

