
import virustotal3
import os 
import platform
import pyautogui
import subprocess
API_KEY=os.getenv("VIRUSTOTAL_API_KEY")
FilePath =pyautogui.prompt("Enter the file path")
OperatingS=platform.system()

def FileScan(FilePath):

  scanres=virustotal3.scan_file(FilePath,API_KEY)
  
  pyautogui.alert("Files Scanned Successfully"+scanres)
  #only reason it is not working is becuase replit is headless, this needs a head.
  #Ignore  the pyautogui errors, they are not important. 
  #*The intent of thi is for the user of the script, to see the files scanned with malware.
  #I love comments. 
def HardeningScript():
  if OperatingS=="Windows":
    subprocess.run("wh.cmd")
  elif OperatingS=="Linux":
    subprocess.run("lh.sh")

def main():
  pyautogui.alert("Please run this app as an administrator, otherwise the scripts do not run.")
  pyautogui.alert("This script is for windows and linux only. Not for cisco packt tracer.")
  FileScan(FilePath)
  #The only reason is it a paramter is that the SysAdmin will input his file path.
  HardeningScript()
  #this script works by detecting the operating system, from that variable,  there is a conditional statment that runs the apprpriate script according to thht variabe.
#its so simple yet so stupid.
  restat = pyautogui.confirm(text="Are you ok for us to restart your computer?",title=="Restarting Computer Confirmation",buttons=["OK","No"])
  if(restat=="OK"):
    if(OperatingS=="Windows"):
        subprocess.run("shutdown /r /t 1")
    elif(OperatingS=="Linux"):
      subprocess.run("sudo reboot")
    else:
        pyautogui.alert("You have an operating system that is not supported by this script.")
        #Good Gosh, I wrote alot. and no chatgpt used!

#Thiis was made in possible by some scripts I found on github. I just compiled t into an automation.

  
    
