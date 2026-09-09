# Делал с AI

system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online"),
]
active_nodes = []
cpu_loads = []
ram_usages = []

for node_name, cpu_load, ram_usage, status in system_telemetry:
    if status == "offline":
        continue

    active_nodes.append(node_name)
    cpu_loads.append(cpu_load)
    ram_usages.append(ram_usage)

active_nodes_count = len(active_nodes)

average_cpu = round(
    sum(cpu_loads) / len(cpu_loads),
    2,
)

max_ram = max(ram_usages)

telemetry_report = {
    "active_nodes_count": active_nodes_count,
    "metrics": {
        "average_cpu": average_cpu,
        "max_ram": max_ram,
    },
}

print(f"Активные узлы в сети: {active_nodes}")
print("Итоговый отчет телеметрии:")
print(telemetry_report)
