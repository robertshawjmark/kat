from pathlib import Path

import pandas as pd

ROOT = Path().cwd()

data = pd.read_csv(
    ROOT.joinpath("data", "VISA GBP Transactions - Downloaded from Bank.csv")
)
data.columns = [c.strip() for c in data.columns]

data["Withdrawals"] = data["Amount"].apply(lambda x: -x if x < 0 else 0)
data["Deposits"] = data["Amount"].apply(lambda x: x if x > 0 else 0)
data["Payee"] = data["Amount"].apply(lambda x: x if x > 0 else 0)


headers = [
    "Date",
    "Withdrawals",
    "Deposits",
    "Payee",
    "Description",
    "Reference Number",
]


# data = data[headers]

print(data)
