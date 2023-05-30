import math

def num(a, m, b):
    E = (a + 4*m + b) / 6
    SD = (b - a) / 6
    return E, SD

tasks = []
while True:
    a = float(input("Enter the 'a' number (or enter '0' to finish): "))
    if a == 0:
        break
    m = float(input("Enter the 'm' number: "))
    b = float(input("Enter the 'b' number: "))
    tasks.append((a, m, b))

E_tasks, SD_tasks = zip(*[num(*task) for task in tasks])

E_project = sum(E_tasks)
SD_project = math.sqrt(sum(sd**2 for sd in SD_tasks))

CI_min = E_project - 2*SD_project
CI_max = E_project + 2*SD_project

print(f"Project's 95% confidence interval: {CI_min:.2f} ... {CI_max:.2f} points")
