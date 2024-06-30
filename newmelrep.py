import pandas as pd


def record_aircraft_data(data, inop_ac, passenger, cargo):
  """
  This function records aircraft data including inoperational, passenger, and cargo aircraft.

  Args:
      data (dict): Dictionary containing aircraft data with keys 'TN', 'Cat', 'FID', and 'Skill'.
      inop_ac (list): List of tail numbers for inoperational aircraft.
      passenger (list): List of tail numbers for passenger aircraft.
      cargo (list): List of tail numbers for cargo aircraft.

  Returns:
      pandas.DataFrame: Dataframe containing information on AMT and CBN technicians by category.
  """
  dataframe = pd.DataFrame(data, columns=['TN', 'Cat', 'FID', 'Skill'])

  # Filter out inoperational aircraft
  dataframe = dataframe[~dataframe['TN'].isin(inop_ac)]

  # Filter dataframes for passenger and cargo aircraft
  passenger_df = dataframe[dataframe['TN'].isin(passenger)]
  cargo_df = dataframe[dataframe['TN'].isin(cargo)]

  # Filter and count AMT technicians by category
  amt_df = passenger_df[passenger_df['Skill'] == 'AMT']
  amt_df = amt_df.drop_duplicates('FID')
  amt_cat_a = amt_df[amt_df['Cat'] == 'A']['Cat'].count()
  amt_cat_b = amt_df[amt_df['Cat'] == 'B']['Cat'].count()
  amt_cat_c = amt_df[amt_df['Cat'] == 'C']['Cat'].count()
  amt_cat_d = amt_df[amt_df['Cat'] == 'D']['Cat'].count()

  # Filter and count CBN technicians by category
  cbn_df = passenger_df[passenger_df['Skill'] == 'CBN']
  cbn_df = cbn_df.drop_duplicates('FID')
  cbn_cat_a = cbn_df[cbn_df['Cat'] == 'A']['Cat'].count()
  cbn_cat_b = cbn_df[cbn_df['Cat'] == 'B']['Cat'].count()
  cbn_cat_c = cbn_df[cbn_df['Cat'] == 'C']['Cat'].count()
  cbn_cat_d = cbn_df[cbn_df['Cat'] == 'D']['Cat'].count()

  # Return dataframe containing technician counts by category
  return pd.DataFrame({
      'AMT_Cat_A': [amt_cat_a],
      'AMT_Cat_B': [amt_cat_b],
      'AMT_Cat_C': [amt_cat_c],
      'AMT_Cat_D': [amt_cat_d],
      'CBN_Cat_A': [cbn_cat_a],
      'CBN_Cat_B': [cbn_cat_b],
      'CBN_Cat_C': [cbn_cat_c],
      'CBN_Cat_D': [cbn_cat_d],
  })


# Example usage for B737 data
B737_data = record_aircraft_data(record_B737, B737_inop_ac, B737_passenger, B737_cargo)
print(B737_data)

# Example usage for B777 data (assuming record_B777 and B777_inop_ac, etc. are defined similarly)
B777_data = record_aircraft_data(record_B777, B777_inop_ac, B777_passenger, B777_cargo)
print(B777_data)
