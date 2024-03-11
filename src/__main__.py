from pathlib import Path

import pandas as pd

ROOT = Path().cwd()


# headers = [
#     'Date',
#     'Withdrawals',
#     'Deposits',
#     'Payee',
#     'Description',
#     'Reference Number',
# ]

data = pd.read_csv(
    ROOT.joinpath("data", "VISA GBP Transactions - Downloaded from Bank.csv")
)
data.columns = [c.strip() for c in data.columns]

drop = [
    "Account Number",
    "Sort Code",
    "Card",
    "Ledger Balance",
]

data = data.drop(columns=drop)

data["Withdrawals"] = data["Amount"].apply(lambda x: -x if x < 0 else 0)
data["Deposits"] = data["Amount"].apply(lambda x: x if x > 0 else 0)
data["Payee"] = data["Amount"].apply(lambda x: x if x > 0 else 0)


headers = [
    "Date",
    "Account Number",  # b
    "Sort Code",  # c
    "Card",  # d
    "Narrative",
    "Amount",
    "Ledger Balance",  # g
]

filter = [
    "Account Number",
    "Sort Code",
    "Card",
    "Ledger Balance",
]
