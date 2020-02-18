import subprocess

myfile = open("network_data/scannedIP.txt", "rt")
contents = myfile.read()
myfile.close()
ls = contents.split()
macs = []
lab1 = ['94:65:2D:F2:DC:93', '08:D4:0C:70:A2:FA', 'AA:BB:CC:DD:EE:FG']
lab2 = ['08:D4:0C:70:A2:FB', '94:65:2D:F2:DC:94', 'AA:BB:CC:DD:EE:FU']
lab3 = ['08:D4:0C:70:A2:FC', 'AA:BB:CC:DD:EE:FF', '94:65:2D:F2:DC:95']
for x in ls:
    output = subprocess.run(f"sudo nmap -sP {x} | grep MAC", shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    macs.append(str(output.stdout)[13:30])
zipped = list(zip(ls, macs))
# print(zipped)
# OnePlus -- 94:65:2D:F2:DC:93
# Dell Gaming -- 08:D4:0C:70:A2:FB
lab_one = open("lab_data/lab1", "w")
lab_two = open("lab_data/lab2", "w")
lab_three = open("lab_data/lab3", "w")
for x, y in zipped:
    if y in lab1:
        lab_one.write(f"{x}\n")
    elif y in lab2:
        lab_two.write(f"{x}\n")
    elif y in lab3:
        lab_three.write(f"{x}\n")
lab_one.close()
lab_two.close()
lab_three.close()
