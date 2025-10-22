import sys
import subprocess
import platform
#Just those three as its such a simple script, This fork is literally just me weaving a bunch of scripts together :)
#For the 25-26 year, I decided to keep a CLI as opposed ot py-auto-gui, I wanna mke this cross platform.
#I found the best thign to do, is to keep all windows files on the same directory as the linux files.
#please note, these scripts do require intervention from the user, as they are not fully automated.
OS=platform.system()
batch_file_path="Windows.bat"
def ScriptRun():
    if OS == "Windows":
       subprocess.run(batch_file_path, shell=True, check=False, capture_output=False, text=False)
    elif OS == "Linux":
      Distro=input("Which Linux Distribution are you using? [1]Ubuntu [2]Mint? Enter the number: ")
      if Distro == "1" or "[1]":
         subprocess.run("Ubuntu.sh")
      elif Distro == "2" or "[2]":
          subprocess.run("Mint.sh")

def  main():
    ScriptRun()
         