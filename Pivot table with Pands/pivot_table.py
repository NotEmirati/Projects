import pandas as pd

data = {'person': ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E'],
        'sales': [1000, 300, 400, 500, 800, 1000, 500, 700, 50, 60, 1000, 900, 750, 200, 300, 1000, 900, 250, 750, 50],
        'quarter': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],
        'country': ['US', 'Japan', 'Brazil', 'UK', 'US', 'Brazil', 'Japan', 'Brazil', 'US', 'US', 'US', 'Japan',
                    'Brazil', 'UK', 'Brazil', 'Japan', 'Japan', 'Brazil', 'UK', 'US']
        }

df = pd.DataFrame(data)

print(df)

pivot = df.pivot_table(index=['country'], values=['sales'], aggfunc='sum')
print(pivot)
