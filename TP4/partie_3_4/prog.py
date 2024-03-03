import re
import subprocess
import matplotlib.pyplot as plt
import multiprocessing 


file_name = "output.txt"
output_file = "cacti_out.txt"
temp_file_name = "temp.cfg"

pattern_float = r"(\d+(?:\.\d*)?(?:e[-+]?\d+)?)"

def run(command, output_file):
    arg = command.split()
    with open(output_file, "w") as file:
        process = subprocess.run(arg, stdout=file, stderr=file)
        pass

    # if process.returncode != 0:
    #     print("Erreur dans le sous-processus")
    #     print(f"Commande entrée : '{command}'")
    #     print(f"returncode = {process.returncode}")
    return process.returncode


def cacti_stats(config_file, output_file="cacti_out.txt"):
    command = f"cacti6.5 -infile {config_file}"
    code = run(command, output_file)
    if code != 0:
        return float("nan"), float("nan")

    # Area extraction
    pattern = r"\(mm2\): " + pattern_float
    with open(output_file, "r") as file:
        text = "".join(file.readlines())

    areas = re.findall(pattern, text) 
    assert len(areas) == 2

    area_cache = sum(map(float, areas)) # résultat en mm²

    # Power extraction
    pattern = r"(?:Data|Tag) array: +Total dynamic read energy/access +\(nJ\): " + pattern_float
    energies = re.findall(pattern, text)
    assert len(energies) == 2

    pattern = r"(?:Data|Tag) side \(with Output driver\) \(ns\): " + pattern_float
    durations = re.findall(pattern, text)
    assert len(durations) == 2


    power_cache = sum(map((lambda e, d: float(e)/float(d)), energies, durations)) * 1000 # résultat en watts

    return area_cache, power_cache

def write_file(proc, n_kibibytes, temp_file_name):
    with open(f"{proc}_L1.cfg", "r") as src, open(temp_file_name, "w") as dest:
        src.readline()
        src.readline()

        dest.write("# Cache size\n")
        dest.write(f"-size (bytes) {n_kibibytes * 1<<10}\n")

        for line in src:
            dest.write(line)


for proc in ("A7", "A15"):
    print(proc)
    area_L1 = []
    power_L1 = []
    area_L2, power_L2 = cacti_stats(f"{proc}_L2.cfg")

    for n_kibibytes in (1, 2, 4, 8, 16, 32):
        write_file(proc, n_kibibytes, temp_file_name)
        a, p = cacti_stats(temp_file_name)
        area_L1.append(a)
        power_L1.append(p)


    # area_L1[i] contient la surface d'un cache L1 de taille 2^i kibioctets


    if proc == "A7" :
        area_proc_plus_L1s = 0.45
        power_proc = 100.
    elif proc == "A15":
        area_proc_plus_L1s = 2. 
        power_proc = 500.

    proportion = 2 * area_L1[5] / area_proc_plus_L1s
    area_proc = area_proc_plus_L1s - 2 * area_L1[5]

    area_total = [area_proc + 2*area_L1[i] + area_L2 for i in range(6)]

    power_proc_plus_L1 = [power_proc + 2*power_L1[i] for i in range(6)]



    print(f" --- Processeur Cortex {proc} --- ")

    print(f"Surface processeur sans caches : {area_proc:.4}mm²")
    print(f"Surface de chaque cache L1 : {area_L1[5]:.4}mm²")
    print(f"Surface du cache L2 : {area_L2:.4}mm²")
    print(f"Les caches L1 occupent : {proportion:.2%} de l'ensemble coeur + caches L1")
    print(f"Surface totale : {area_total[5]:.4}mm²")
    print()

    print(f"Puissance processeur sans caches : {power_proc:.4}mW")
    print(f"Puissance de chaque cache L1 : {power_L1[5]:.4}mW")
    print(f"Puissance du cache L2 : {power_L2:.4}mW")
    print(f"Puissance totale (hors L2): {power_proc_plus_L1[5]:.4}mW")
    print()

    print("Valeurs en fonction de la taille des L1")
    print("Surface proc + deux L1 + L2 : ", area_total)
    print("Puissance L1 : ", power_L1)
    print()





