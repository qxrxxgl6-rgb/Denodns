with open(r"C:\Users\Administrator\.gemini\antigravity\scratch\rethinkdns-deploy\fly.tls.toml", "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace('app = ""', 'app = "rethink-dns-glxu"\nprimary_region = "nrt"')
c = c.replace('auto_stop_machines = "suspend"', 'auto_stop_machines = false')
with open(r"C:\Users\Administrator\.gemini\antigravity\scratch\rethinkdns-deploy\fly.toml", "w", encoding="utf-8") as f:
    f.write(c)
print("Updated successfully")
