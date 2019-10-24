devices=[ "R1", "R2","R3","S1" ,"S2" ,"Moni" ]
for item in devices:
      if "1" in item:
          print(item)
    
switches=[]
for item in devices:
        if "i" in item:
            switches.append(item)
print(switches)
