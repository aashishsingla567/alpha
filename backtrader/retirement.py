import numpy as np
import matplotlib.pyplot as plt

# Function to calculate compound interest with monthly contributions
def calculate_investment_growth(principal, monthly_contribution, years, interest_rate, compounding_frequency=12, annual_increase=0):
    total_months = years * 12
    balances = []
    contributions = []

    for month in range(total_months + 1):
        # Calculate future value with compound interest and contributions
        future_value = principal * (1 + interest_rate / compounding_frequency) ** (compounding_frequency * (month / 12))
        future_value += monthly_contribution * (((1 + interest_rate / compounding_frequency) ** (compounding_frequency * (month / 12)) - 1) / (interest_rate / compounding_frequency))

        # Record the balance and contributions at each step
        balances.append(future_value)
        contributions.append(principal + monthly_contribution * month)

        # Increase the monthly contribution at the end of each year
        if month % 12 == 0 and month != 0:
            monthly_contribution *= (1 + annual_increase)

    return balances, contributions

# Investment parameters
principal = 240000          # Initial investment in dollars
monthly_contribution = -500  # Monthly contribution in dollars
years = 50                # Investment duration in years
interest_rate = 0.10      # Annual interest rate (10%)
compounding_frequency = 1  # Compounded annually
annual_increase = 0.10    # Annual increase in monthly contribution 

# Calculate investment growth
balances, contributions = calculate_investment_growth(principal, monthly_contribution, years, interest_rate, compounding_frequency, annual_increase)

# Plotting
plt.figure(figsize=(12, 6))
years_range = np.arange(0, years + 1, step=1)

# Plot Future Value
plt.plot(np.arange(0, years * 12 + 1) / 12, balances, 'o-', color='brown', label=f"Future Value ({interest_rate * 100:.2f}%)", markersize=2)

# Plot Total Contributions
plt.plot(np.arange(0, years * 12 + 1) / 12, contributions, 'D-', color='teal', label="Total Contributions", markersize=2)

# Add annotations for a generic year
def annotate_year(year):
    balance_year = balances[year * 12]
    contribution_year = contributions[year * 12]
    plt.annotate(f"Year {year}\nFuture Value: ${balance_year:,.2f}\nTotal Contributions: ${contribution_year:,.2f}",
                 xy=(year, balance_year), xytext=(year + 5, balance_year - 200000),
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor="brown", facecolor="white"),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2", color="brown"),
                 fontsize=10, color="brown")

# Example usage
annotate_year(40)

# Customize plot appearance
plt.title("Total Savings", fontsize=16, weight='bold')
plt.xlabel("Years", fontsize=12)
plt.ylabel("US Dollars ($)", fontsize=12)
plt.xticks(years_range)
plt.yticks(np.arange(0, max(balances) + 500000, step=392000), fontsize=10, weight='bold')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc="upper left", fontsize=12)
plt.show()
