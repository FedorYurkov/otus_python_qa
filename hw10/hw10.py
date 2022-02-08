import os
from datetime import datetime
from subprocess import (run, PIPE)
import re


result = run(["ps", "aux"], stderr=PIPE, stdout=PIPE)

process_list = re.sub(" +", " ", result.stdout.decode("utf-8")).split("\n")

system_users = []
users_process_count = {}
total_mem = 0
total_cpu = 0
most_mem_process = {"process_name": "", "mem": 0}
most_cpu_process = {"process_name": "", "cpu": 0}

for item in process_list[1:]:
    if item == "":
        continue

    parts = item.split(" ")

    user_name = parts[0]
    cpu_value = float(parts[2])
    mem_value = float(parts[3])
    process_name_match = re.search(".+ \d{1,2}:\d\d \d{1,2}:\d\d (.+)", item)
    process_name = process_name_match.group(1)

    if user_name not in system_users:
        system_users.append(user_name)

    if user_name not in users_process_count:
        users_process_count[user_name] = 1
    else:
        users_process_count[user_name] += 1

    total_cpu += cpu_value
    total_mem += mem_value

    if most_cpu_process["cpu"] < cpu_value:
        most_cpu_process = {"process_name": process_name[:20], "cpu": cpu_value}

    if most_mem_process["mem"] < mem_value:
        most_mem_process = {"process_name": process_name[:20], "mem": mem_value}

formatted_user = ""
for i in range(len(system_users)):
    formatted_user += f"'{system_users[i]}'"
    if i != len(system_users) - 1:
        formatted_user += ", "

formatted_user_process_count = ""
for key in users_process_count:
    formatted_user_process_count += key + ": " + str(users_process_count[key]) + "\n"


formatted_out = f"System state report:\n\n" \
                f"System users: {formatted_user}\n\n" \
                f"Total process running: {len(process_list) - 1}\n\n" \
                f"Users process:\n{formatted_user_process_count}" \
                f"\nTotal CPU used: {round(total_cpu, 2)}%\n" \
                f"Total MEM used: {round(total_mem, 2)}%\n\n" \
                f"The most CPU used process: {most_cpu_process['process_name']}: {most_cpu_process['cpu']}%\n" \
                f"The most MEM used process: {most_mem_process['process_name']}: {most_mem_process['mem']}%\n"

print(formatted_out)

with open(
        f"results/{os.path.basename('system_scan')}_{datetime.now().strftime('%d-%m-%Y_%H.%M.%S')}.txt",
        "w") as f:
    f.write(formatted_out)
