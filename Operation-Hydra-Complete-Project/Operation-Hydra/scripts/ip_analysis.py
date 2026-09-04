from pathlib import Path
import csv
import ipaddress

root = Path(__file__).resolve().parents[1]
ioc_file = root / "iocs" / "indicators_of_compromise.csv"

print("=== Operation Hydra: Safe IP Indicator Analysis ===")
with ioc_file.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row["type"] == "IP":
            ip = ipaddress.ip_address(row["value"])
            print(f"IP: {ip}")
            print(f"Private: {ip.is_private}")
            print(f"Reserved: {ip.is_reserved}")
            print("Note: Documentation/test addresses are not traced as real targets.")
