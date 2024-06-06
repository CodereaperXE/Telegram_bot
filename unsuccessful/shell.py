import subprocess
import threading
import os

class Shell:
    def __init__(self):
        self.command = ""
        self.data = ""
        self.kill_flag=0
        self.event = threading.Event()
        self.thread = threading.Thread(target=self._run_shell)
        self.thread.start()
        

    def run_command(self, command):
        if(self.kill_flag):
            return
        
        self.command = command
        self.event.clear()
        self.event.wait()  # Wait for the command to complete
        
        output = self.data
        self.data = ""
        return output
    
    def kill(self):
        self.kill_flag=1

    def _run_shell(self):
        while (not self.kill_flag):
            
            if self.command:
                if self.command.startswith("cd "):
                    directory = self.command.split(maxsplit=1)[1]
                    try:
                        os.chdir(directory)
                    except FileNotFoundError:
                        self.data += f"\nDirectory not found: {directory}\n"
                    self.event.set()
                    self.command=""
                    continue

                try:
                    output = subprocess.check_output(self.command, shell=True, text=True)
                    self.data = output
                except subprocess.CalledProcessError as e:
                    self.data = f"Error: {e.returncode}\n{e.output}"
                finally:
                    self.event.set()  # Signal that the command has completed
                    self.command = ""
        

# Usage
# Exit function should be described

# shell = Shell()

# while True:
#     temp = input("> ")
#     if temp=="exit_shell":
#         shell.kill()
#         break
#     if temp.strip() == "":
#         continue
#     data = shell.run_command(temp)
#     print(data)


