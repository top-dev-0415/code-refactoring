import locale


def statement(invoice: dict, plays: dict):
    totalAmount = 0
    volumeCredits = 0
    result = f"Statement for {invoice['customer']}\n"

    def format(amount):
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        return locale.currency(amount, grouping=True)

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        thisAmount = 0

        match play["type"]:
            case "tragedy":
                thisAmount = 40000
                if perf["audience"] > 30:
                    thisAmount += 1000 * (perf["audience"] - 30)
            case "comedy":
                thisAmount = 30000
                if perf["audience"] > 20:
                    thisAmount += 10000 + 500 * (perf["audience"] - 20)
                thisAmount += 300 * perf["audience"]
            case _:
                raise Exception(f"unknown type: ${play['type']}")

        # add volume credits
        volumeCredits += max(perf["audience"] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volumeCredits += perf["audience"] // 5

        # print line for this order
        result += (
            f"  {play['name']}: {format(thisAmount/100)} ({perf['audience']} seats)\n"
        )
        totalAmount += thisAmount

    result += f"Amount owed is {format(totalAmount/100)}\n"
    result += f"You earned {volumeCredits} credits\n"
    return result
