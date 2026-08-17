file = open("access1.log", "w")
file.write("2026-04-27 10:15:32 192.168.1.1 /home \n")
file.write("2026-04-27 10:16:10 192.168.1.2 /login \n")
file.write("2026-04-27 10:17:45 192.168.1.1 /dashboard \n")
file.write("2026-04-27 10:18:20 192.168.1.3 /profile \n")
file.close()
file = open("access1.log", "r")
ip_list = []
for line in file:
    data = line.split()
    ip_list.append(data[2])
file.close()
print("UNIQUE IP ADDRESSES: ")
unique_ips = set(ip_list)
for ip in unique_ips:
    print(ip)
print("IP ADDRESSES OCCURENCE: ")
for ip in unique_ips:
    print(ip, ":", ip_list.count(ip))