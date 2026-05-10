import subprocess
import sys

p1 = subprocess.Popen([sys.executable, "smm_bot_Final.py"])
p2 = subprocess.Popen([sys.executable, "Claw_VIP_Final.py"])

print("SMM Bot চালু")
print("Claw VIP Bot চালু")

p1.wait()
p2.wait()
