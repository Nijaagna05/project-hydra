from pathlib import Path
import csv
from collections import defaultdict

root = Path(__file__).resolve().parents[1]
file_path = root / "evidence" / "transaction_logs" / "transactions.csv"

flows = defaultdict(list)
incoming = defaultdict(list)

with file_path.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        flows[row["source_account"]].append(row)
        incoming[row["destination_account"]].append(row)

print("=== Operation Hydra: Simulated Transaction Trace ===")
for account, rows in incoming.items():
    sources = {r["source_account"] for r in rows}
    if len(sources) > 1:
        print(f"Convergence point: {account}")
        print(f"Incoming sources: {', '.join(sorted(sources))}")
        print(f"Transactions: {len(rows)}")

print("\nTransaction chain:")
with file_path.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(f'{row["transaction_id"]}: {row["source_account"]} -> {row["destination_account"]} | INR {row["amount_inr"]}')
