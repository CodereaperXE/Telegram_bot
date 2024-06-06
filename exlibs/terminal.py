import subprocess
import os
import threading

class SimpleShell:
    def __init__(self):
        self.data = ""
        self.command = ""
        self.command_lock = threading.Lock()

    def give_command(self, command):
        with self.command_lock:
            self.command = command

    def get_data(self):
        with self.command_lock:
            self.temp=self.data
            print(self.temp)
            self.data=""
            return self.temp

    def run_shell(self):
        while True:
            # with self.command_lock:
            #     command = self.command
            #     self.command = ""
            if not self.command:
                print("on hold")
                
            if self.command.lower() == "exit":
                self.data += "\nExiting...\n"
                self.command=""
                break

            elif self.command.startswith("cd "):
                directory = self.command.split(maxsplit=1)[1]
                try:
                    os.chdir(directory)
                except FileNotFoundError:
                    self.data += f"\nDirectory not found: {directory}\n"
                self.command=""
                continue

            try:
                result = subprocess.run(self.command, shell=True, capture_output=True, text=True)
                self.data += f"\n{result.stdout}\n"
            except Exception as e:
                self.data += f"\nError: {e}\n"
            self.command=""

    def run(self):
        print("before ")
        active_thread = threading.Thread(target=self.run_shell)
        active_thread.start()
        print("starting ")

def test():
    shell = SimpleShell()
    shell.run()
    while True:
        temp_command = str(input("> "))
        shell.give_command(temp_command)
        temp = shell.get_data()
        if temp:
            print(temp)

test()
