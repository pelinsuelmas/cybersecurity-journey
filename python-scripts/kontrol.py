# Blocklist: known malicious IPs
blocklist = ["10.0.0.5", "192.168.1.100", "172.16.0.9"]

# Incoming IPs (to check)
incoming_ips = ["10.0.0.5", "8.8.8.8", "172.16.0.9", "1.1.1.1"]

suspicious_count = 0

for ip in incoming_ips:
    if ip in blocklist:
        print(ip + " --> SUSPICIOUS! On the blocklist.")
        suspicious_count = suspicious_count + 1
    else:
        print(ip + " --> clean.")

print("---")
print(str(len(incoming_ips)) + " IPs scanned, " + str(suspicious_count) + " suspicious found.")
