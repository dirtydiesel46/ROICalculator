years = int(input("How many years are you investing for: "))
initial_investment = float(input("Enter your initial investment amount: "))
total_profit = 0

for year in range(years):
    print("Please enter the amount profited for year " + str(year + 1) + ": ")
    total_profit += float(input("Amount:"))
    print("Cummulative cashflow for year " +str(year+1) +"=" + str(total_profit))


def ROI(init_invest, net_profit, time):
    print("ROI: " + str(round((net_profit / time) / (init_invest) * 100,2)))
    return round(net_profit / time / init_invest * 100, 2)


def net_profit(init_invest, profit):
    print("Net profit: " + str(profit - init_invest))
    return profit - init_invest


net = net_profit(initial_investment, total_profit)
return_on_investment = ROI(initial_investment, net, years)
