import psutil

THRESHOLD = 75.0

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

cpu_warning = cpu > THRESHOLD
mem_warning = memory > THRESHOLD
disk_warning = disk > THRESHOLD

cpu_status = f"WARNING (above {THRESHOLD}%)" if cpu_warning else "Healthy"
mem_status = f"WARNING (above {THRESHOLD}%)" if mem_warning else "Healthy"
disk_status = f"WARNING (above {THRESHOLD}%)" if disk_warning else "Healthy"

if cpu_warning or mem_warning or disk_warning:
    overall = "NEEDS ATTENTION"
else:
    overall = "HEALTHY"

print("=== System Health Report ===")
print(f"CPU    : {cpu}%  -> {cpu_status}")
print(f"Memory : {memory}%  -> {mem_status}")
print(f"Disk   : {disk}%  -> {disk_status}")
print(f"Overall: {overall}")