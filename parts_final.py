import pandas as pd

# Original data in dictionary form, including the 'Remark' column
data = {
    "Part Name": ["key", "key", "lock", "lock", "key", "washer"],
    "Part Number": [1212, 1212, 3434, 3434, 1212, 3231],
    "RID": ["gg12", "hgj", "gyuu", "uioi", "lkrd", "tlet"],
    "Remark": ["avail", "avail", "canceled", "wrong", "avail", "canceled"],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Group by 'Part Name' and 'Part Number', get list of RIDs and remarks for each group
grouped = df.groupby(["Part Name", "Part Number"])[["RID", "Remark"]].apply(lambda x: x.values.tolist()).reset_index()

# Add a new column for the count of RIDs
grouped["RID Count"] = grouped[0].apply(len)

# Filter for parts that have more than one RID
more_than_one_rid = grouped[grouped[0].apply(len) > 1]

# Sort by number of RIDs in descending order, then by 'Part Number' in descending order
more_than_one_rid_sorted = more_than_one_rid.sort_values(by=["RID Count", "Part Number"], ascending=[False, False])

# Create an empty list to hold the restructured data
restructured_data = []

# Iterate through each part that has more than one RID and append the data
for _, row in more_than_one_rid_sorted.iterrows():
    part_name = row["Part Name"]
    part_number = row["Part Number"]
    rid_count = row["RID Count"]
    rids = [item[0] for item in row[0]]  # Extract RID values from the nested list
    remarks = [item[1] for item in row[0]]  # Extract Remark values from the nested list
    
    # Append the header row with 'Part Name', 'Part Number', and 'RID Count'
    restructured_data.append([part_name, part_number, rid_count, None, None])
    
    # Append each 'RID' value and its corresponding 'Remark' under the corresponding part
    for rid, remark in zip(rids, remarks):
        restructured_data.append([None, None, None, rid, remark])

# Convert the list to a DataFrame
df_restructured = pd.DataFrame(restructured_data, columns=["Part Name", "Part Number", "RID Count", "RID", "Remark"])

# Define the output path for the restructured data Excel file
output_file_restructured_excel = 'restructured_parts_data_with_remarks.xlsx'

# Save the restructured DataFrame to an Excel file
df_restructured.to_excel(output_file_restructured_excel, index=False)

output_file_restructured_excel
