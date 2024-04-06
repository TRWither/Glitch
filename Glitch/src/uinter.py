import os
import sys

def clear_screen():
    # Clearing screen for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

def home():
    clear_screen()
    hometext = """

                    _____ _ _ _       _     
                    |  __ \ (_) |     | |    
                    | |  \/ |_| |_ ___| |__  
                    | | __| | | __/ __| '_ \ 
                    | |_\ \ | | || (__| | | |
                     \____/_|_|\__\___|_| |_|

    ==============================================================
    Glitch is a Linux CLI text editor.
    Version : 1.0.0                 License : BSD-3 Clause
    >>> Some commands :
    F : find file                   D : find directory
    O+F : open file                 H : help
    E : exit file                   Q : quit                      
    """

    print(hometext)
    while True:
        cmd = input("Command : ")
                
        if cmd.lower() == "f":
            filename = input("Find file : ")
            if os.path.isfile(filename):
                print(f"{filename} found.")
            else:
                print(f"\033[31m{filename} not found because it doesn't exist or it is not a file.\033[0m")

        elif cmd.lower() == "d":
            foldername = input("Find directory : ")
            if os.path.isdir(foldername):
                print(f"{foldername} found.")
            else:
                print(f"\033[31m{foldername} not found because it doesn't exist or it is not a folder.\033[0m")
                
        elif cmd.lower() == "of":
            while True:
                file_to_open = input("Open file : ")
                if os.path.isfile(file_to_open):
                    with open(file_to_open, 'r') as file:
                        os.system('clear')
                        content = file.read()
                        print(content)
                        while True:
                            fcmd = input("Command : ")
                            if fcmd.lower() == "e":
                                os.system('clear')
                                home()
                                break
                            elif fcmd.lower() == "s":
                                search_in_file = input("Search : ")
                                if search_in_file in content:
                                    lines = content.split('\n')
                                    for i, line in enumerate(lines, start=1):
                                        if search_in_file in line:
                                            print(f"Word '{search_in_file}' found at line {i}: {line}")
                                else:
                                    print(f"Word '{search_in_file}' not found in the file.")
                                # paste copied texte at the indicated position
                                position = int(input("Insertion position : "))
                                content = content[:position] + clipboard + content[position+len(clipboard):]
                                print("Pasted from clipboard.")
                            elif fcmd.lower() == "ap":
                                absolute_path = os.path.abspath(file_to_open)
                                print(f"Absolute path : {absolute_path}")
                            elif fcmd.lower() == "rp":
                                rel_path = os.path.relpath(file_to_open)
                                print(f"Relative path : {rel_path}")
                            elif fcmd.lower() == "fp-r":
                                os.chmod(file_to_open, 0x444)
                                print(f"{file_to_open} : read.")
                            elif fcmd.lower() == "fp-w":
                                os.chmod(file_to_open, 0x200)
                                print(f"{file_to_open} : write.")
                            elif fcmd.lower() == "fp-x":
                                os.chmod(file_to_open, 0o100)
                                print(f"{file_to_open} : execute.")
                            elif fcmd.lower() == "ef":
                                if os.access(file_to_open, os.W_OK):
                                    with open(file_to_open, 'r+') as file:
                                        os.system('clear')
                                        content = file.read()
                                        print(content)
                                        print("Type your edits below. Press Ctrl+D when finished.")
                                        new_content = sys.stdin.read()
                                        file.seek(0)
                                        file.write(new_content)
                                        file.truncate()
                                        print("File content updated successfully.")
                                else:
                                    print("\033[31mPermission denied: You don't have write permission for this file.\033[0m")
                            else:
                                print(f"\033[31mFile '{file_to_open}' not found.\033[0m")
                        else:
                            print("\033[31mInvalid command.\033[0m")
                    break
                else:
                    print(f"\033[31m{file_to_open} not found because it doesn't exist or it is not a file.\033[0m")
                
        elif cmd.lower() == "h":
            os.system('clear')
            help()
            hcmd = input("Command : ")
            if hcmd.lower() == "eh":
                    os.system('clear')
                    home()
            else:
                print("Invalid command in help page.")
                
        elif cmd.lower() == "q":
            print("Exiting Glitch...")
            clear_screen()
            break
        
        elif cmd.lower() == "cl":
            os.system('clear')
            home()

        elif cmd.lower() == "cd":
            godir = input("Enter the path of the directory : ")
            if os.path.isdir(godir):
                os.chdir(godir)
            else:
                print("Unknow directory.")
                
        elif cmd.lower() == "cd-o":
            os.chdir("..")
            print("Returned to the previous folder.")          
        
        elif cmd.lower() == "nf":
            newfile = input("Enter the name of the new file : ")
            os.mknod(newfile)
            print("Created.")

        elif cmd.lower() == "nd":
            newfolder = input("Enter the name of the folder : ")
            os.mkdir(newfolder)
            print("Created.")
            
        elif cmd.lower() == "rf":
            rmfile = input("Remove file : ")
            os.remove(rmfile)
            print("Removed.")
        
        elif cmd.lower() == "rd":
            rmdir = input("Folder to remove : ")
            os.rmdir(rmdir)
            print("Removed.")
        
        else:
            print("\033[31mInvalid command.\033[0m")
            
# HELP
def help():
    print("""
          
          \033[1;34m-------------------- GLITCH - HELP PAGE --------------------\033[0m
         ============================================================\033[0m
          Glitch is a text editor for Linux created in Python by Withe
          r. It has been released under BSD-3 Clause license.\033[0m
          
         1. Check if files or folders exist\033[0m
         -------------------------------------------\033[0m
          To check if a file or a folder exists, you must use 'f' for
          a file, and 'd' for a folder.
          If the file/folder exists, you'll see a message like this :
          
          '<file/folder> found.\033[0m'\033[0m
          
         2. Open files and folders\033[0m
         -------------------------------------------\033[0m
          Now, how to open a file ?
          You must use the command 'of'. It will print the file content
          in the console.
          
          To open a folder, use 'od'. It will list all the files in the
          folder.\033[0m
          
         3. Create new files\033[0m
         -------------------------------------------\033[0m
          You can also create new files in Glitch. To do that, use the
          command 'nf'. It will create a new file, and you can open it
          next.\033[0m
          
         4. Create new folders
         -------------------------------------------
          To make a new folder in Glitch, use the command 'nd'. It will
          make a new directory, and you can open it next.\033[0m
          
         5. Show help page
         -------------------------------------------
          Use 'h' to print this message.\033[0m
          
         6. Quit Glitch
         -------------------------------------------
          Use 'q' to exit Glitch.\033[0m
          
         7. Exit a file
         -------------------------------------------
          Use 'e' when you are in a file to exit the file and return to
          the home. You can also use it to exit a directory.\033[0m
          
         8. Remove a file
         -------------------------------------------
          Yes, you can remove files you created in Glitch. To do that, 
          use 'rf'. It will remove the file you want.\033[0m
          
         9. Remove a folder
         -------------------------------------------
          You can also remove folders you created in Glitch. To do that, 
          use 'rd'. It will remove the folder you want.\033[0m
          
         10. Change file permissions
         -------------------------------------------
          When you are editing a file, you can change the file permission
          s. Read, Write and Execute. To do that, open a file. Next, choo
          se the permission you want to change :
          
          - 'fp-r\033[0m' : you can read the file or not
          - 'fp-w\033[0m' : you can write in the file or not
          - 'fp-x\033[0m' : you can execute the file or not\033[0m
          
         11. Edit files
         -------------------------------------------
          There are a lot of tools for you when you want to edit the conte
          nt of a file.
          - 's\033[0m' : use it to search something in the file. The number of li
          ne will be indicated.
          - 'ap\033[0m' : print the absolute path of the file.
          - 'rp\033[0m' : print the relative path of the file.
          - 'ef\033[0m' : modify the content of a file. When finished, type Ctrl+
          D.\033[0m
          
         12. Homepage
         -------------------------------------------
          Here are some commands for the homepage :
          - 'cl\033[0m' : clear the entire commands history.\033[0m
          
         13. Go in a directory
         -------------------------------------------
          To use commands in a specified directory, use 'cd'. If you want t
          o exit the directory, use 'cd-o'.\033[0m
          
          -------------------------------------------
         14. To exit this page : 'eh'.\033[0m
          """)
