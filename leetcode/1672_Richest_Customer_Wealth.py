def maximumWealth(accounts):
    return max([sum(account) for account in accounts])


print(maximumWealth([[0, 0]]))