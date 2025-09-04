import os

# Declare directory name
directory = "new"

#  Create a directory
os.mkdir("MyFolder")
print("Created: MyFolder")


#  List all components in current working directory
print("\nContents in current directory:")
print(os.listdir())


#  Get current working directory
print("Current Working Directory:", os.getcwd())

# . Change working directory
os.chdir(directory)
print("Changed Directory To:", os.getcwd())

#  Rename a directory
os.rename("MyFolder", "RenamedFolder")
print("Renamed Directory to 'RenamedFolder'")

#  Remove empty directory
os.rmdir("NewFolder")   # works only if empty
print("Removed NewFolder (empty)")

#  Create a file inside NewFolder
with open("NewFolder/test.txt", "w") as f:
    f.write("Hello!")
    
# . Remove the directory
if os.path.exists(directory):
    os.rmdir(directory)
    print(f"\nDirectory '{directory}' removed successfully!")