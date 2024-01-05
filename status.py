import time
import psutil


#System information
print("=" * 25, "System Information", "=" * 25)
print("MY PC Name:", psutil.users()[0].name) 

#CPU information
print("=" * 25, "CPU Information", "=" * 25)
print("CPU Physical Cores:", psutil.cpu_count(logical=False))
print("Total CPU Usage:", psutil.cpu_percent())

#Memory information
print("=" * 25, "Memory Information", "=" * 25)
virtual_memory = psutil.virtual_memory()
print("Total Memory:", virtual_memory.total / (1024 * 1024 * 1024), "GB")
print("Available Memory:", virtual_memory.available / (1024 * 1024 * 1024), "GB")
print("Memory Usage:", virtual_memory.percent, "%")

#Network information
print("=" * 25, "Network Information", "=" * 25)
net_io_counters = psutil.net_io_counters()
print("Total Bytes Sent:", net_io_counters.bytes_sent)
print("Total Bytes Received:", net_io_counters.bytes_recv)

#Disk information
print("=" * 25, "Disk Information", "=" * 25)
print("Disk Usage:")
for disk_usage in psutil.disk_usage('/'), psutil.disk_usage('/Users/mdmijanurrahman'): 
    print(disk_usage)

#CPU and RAM Live information
print("=" * 25, "Live CPU and Memory Usages", "=" * 25)

def display_use(cpu_usage, mem_usage, bars = 50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '▌' * int(cpu_percent * bars) + '_' * (bars - int(cpu_percent * bars))
    mem_percent = (mem_usage / 100.0)
    mem_bar = '▌' * int(mem_percent * bars) + '_' * (bars - int(mem_percent * bars))

    print(f"\rCPU Usage: | {cpu_bar} | {cpu_usage:.2f}% \n\n", end="")
    print(f"MEM Usage: | {mem_bar} | {mem_usage:.2f}% \n\n", end="\r")


while True:
    display_use(psutil.cpu_percent(), psutil.virtual_memory().percent, 25)
    time.sleep(2)


