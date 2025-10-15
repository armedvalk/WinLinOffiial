
#I do not know if I should compile this or what.
import platform
import pyautogui
import subprocess
OperatingS=platform.system()



  #only reason it is not working is becuase replit is headless, this needs a head.
  #Ignore  the pyautogui errors, they are not important. 
  #*The intent of thi is for the user of the script, to see the files scanned with malware.
  #I love comments. 
def HardeningScript():
  if OperatingS=="Windows":
    subprocess.run("wh.cmd")
  elif OperatingS=="Linux":
    subprocess.run("lh.sh")
  else:
    pyautogui.alert("Your opperating system is not supported yet.")
  return
                    
def main():
  pyautogui.alert("Please run this app as an administrator, otherwise the scripts do not run.")
  pyautogui.alert("This script is for windows and linux only. Not for cisco packt tracer.")
  #The only reason is it a paramter is that the SysAdmin will input his file path.
  HardeningScript()
  #this script works by detecting the operating system, from that variable,  there is a conditional statment that runs the apprpriate script according to thht variabe.
#its so simple yet so stupid.
  restat = pyautogui.confirm(text="Are you ok for us to restart your computer?",title="Restarting Computer Confirmation",buttons=['OK','No'])
  if(restat=="OK"):
    if(OperatingS=="Windows"):
        subprocess.run("shutdown /r /t 1")
    elif(OperatingS=="Linux"):
      subprocess.run("sudo reboot")
    else:
        pyautogui.alert("You have an operating system that is not supported by this script.")
        #Good Gosh, I wrote alot. and no chatgpt used!

#Thiis was made in possible by some scripts I found on github. I just compiled t into an automation.

  
    