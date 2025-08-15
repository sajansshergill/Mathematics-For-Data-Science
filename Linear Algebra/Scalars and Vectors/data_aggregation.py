import numpy as np

# Sales data (in $1000s)
team_A = np.array([10, 12, 14, 15])  # Jan–Apr
team_B = np.array([8, 11, 13, 16])

# Total sales (aggregate)
total_sales = team_A + team_B
print("Total Sales:", total_sales)
