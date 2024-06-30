import pandas as pd

data = {'item': ['apple', 'banana', 'orange', 'apple', 'pear', 'apple', "pear"]}
df = pd.DataFrame(data)

# Get value counts
repetitions = df['item'].value_counts()

# Filter values based on threshold
filtered_repetitions = repetitions[repetitions >= 2]

# Create DataFrame with repeated items and counts
repeated_df = pd.DataFrame({'item': filtered_repetitions.index, 'count': filtered_repetitions.values})

print(repeated_df)
