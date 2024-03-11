from pathlib import Path

import pandas as pd

ROOT = Path().cwd()
DATA = ROOT.joinpath("data")
FORMATTED = DATA.joinpath("formatted")


def main():
    if not FORMATTED.exists():
        FORMATTED.mkdir()

    source = input("Please enter source file name: ")
    formatted = input("Please enter formatted file name: ")

    data = pd.read_csv(DATA.joinpath(source))
    data.columns = [c.strip() for c in data.columns]

    data["Withdrawals"] = data["Amount"].apply(lambda x: -x if x < 0 else 0)
    data["Deposits"] = data["Amount"].apply(lambda x: x if x > 0 else 0)
    data["Payee"] = data["Amount"].apply(lambda x: x if x > 0 else 0)
    data["Description"] = data["Narrative"]
    data["Reference Number"] = range(len(data))

    headers = [
        "Date",
        "Withdrawals",
        "Deposits",
        "Payee",
        "Description",
        "Reference Number",
    ]

    data = data[headers]

    data.to_csv(FORMATTED.joinpath(formatted), index=False)


if __name__ == "__main__":
    main()
