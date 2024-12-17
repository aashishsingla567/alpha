import random
import matplotlib.pyplot as plt

def manage_risk(initial_balance, trades, risk_per_trade=0.02, reward_per_trader=0.03):
    balance = initial_balance
    balances = [balance]
    for trade in trades:
        if trade == 'W':
            balance *= 1 + reward_per_trader
        elif trade == 'L':
            balance *= 1 - risk_per_trade
        else:
            print("Invalid trade entry. Use 'W' for win and 'L' for lose.")
        balances.append(balance)
    return {'balance': balance, 'balances': balances}

def generate_trades(num_trades):
    num_wins = int(num_trades * winRate)
    num_losses = num_trades - num_wins
    trades = ['W'] * num_wins + ['L'] * num_losses
    random.shuffle(trades)
    return trades

def plot_balance_over_time(balances, final_balance, initial_balance, noOfTrades):
    # Plotting the balance over time
    plt.plot(balances, label='Balance Over Time')
    plt.xlabel('Trade Number')
    plt.ylabel('Balance')
    plt.title(f'Balance Over Time\nFinal Balance: {final_balance}, Net Profit: {final_balance - initial_balance}, Total Trades: {noOfTrades}')
    plt.legend()
    plt.show()



INITIAL_BALANCE =2000
NO_OF_TRADES = 200
RISK_PERCENTAGE = 0.025

winRate = 0.5
riskToRewardRatio = 1.5

rewardPercentage = RISK_PERCENTAGE * riskToRewardRatio
trades = generate_trades(NO_OF_TRADES)


if __name__ == "__main__":
    result = manage_risk(INITIAL_BALANCE, trades, risk_per_trade=RISK_PERCENTAGE, reward_per_trader=rewardPercentage)
    final_balance = round(result['balance'])
    print(f"Balance : {final_balance}")
    print(f"Profit : {final_balance - INITIAL_BALANCE}")
    plot_balance_over_time(result['balances'], final_balance, INITIAL_BALANCE, NO_OF_TRADES)