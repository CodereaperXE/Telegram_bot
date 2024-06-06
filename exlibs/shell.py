import subprocess
import os

class Shell:
    def run_command(self,command):
        while True:
            # command=str(input("> "))
            if command.split()[0]=="cd":
                os.chdir(command.split(maxsplit=1)[1])
                return "Directory changed\n"
            return subprocess.check_output(command, shell=True).decode()

# c=Test()

# while True:
#     comm=str(input("> "))
#     print(c.run_command(comm))

