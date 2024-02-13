import re
import subprocess
import multiprocessing     # garder multiprocess < 8


file_name = "output.txt"

# command = "ls -lh -a --color"
command = "sim-profile -iclass dijkstra/dijkstra_small.ss input.dat"

arg = command.split()

with open(file_name, "w") as file:
    process = subprocess.run(arg, stdout=file, stderr=file)

if process.returncode != 0:
    print("Erreur dans le sous-processus")
    print(f"Commande entrée : '{command}'")
    print(f"returncode = {process.returncode}")
    exit(1)


with open(file_name, "r") as file:
    output = "".join(file.readlines())

instr = "load"
pattern = instr + r" +(\d+) +([.\d]+)"
match  = re.search(pattern, output) 

# les valeurs qui nous interessent sont capturées par les parenthèses du pattern 

count = match.group(1)
pdf = match.group(2)

print(f"{instr}: count = {count}, pdf = {pdf}")




# "/usr/ensta/pack/simplescalar-3v0d/simplesim-3.0/sim-profile"
