import pandas as pd

# Load the cleaned CSV file
file_path = '/Users/hitabratanath/work/Personal/backtrader/cleaned_tcs.csv'
df = pd.read_csv(file_path)

# Keep only the required columns
df = df[['Date', 'OPEN', 'HIGH', 'LOW', 'close', 'VOLUME']]

# Rename columns to match Backtrader's expected names
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

# Save the updated CSV file
final_file_path = '/Users/hitabratanath/work/Personal/backtrader/final_tcs.csv'
df.to_csv(final_file_path, index=False)
