import pandas as pd
import json

def get_inventory():
    # Read the data from the Excel spreadsheet
    df = pd.read_excel('inventory.xlsx')

    # Initialize an empty inventory
    inventory = {}

    print(inventory)

    # Iterate through the rows of the dataframe
    for index, row in df.iterrows():
        # Get the group name and hostname from the dataframe
        group = row['group']
        host = row['host']
        
        # Create the group if it doesn't already exist
        if group not in inventory:
            inventory[group] = {'hosts': []}
        
        # Add the host to the group
        inventory[group]['hosts'].append(host)
    
    # Print the inventory data in JSON format
    print(json.dumps(inventory))

if __name__ == '__main__':
    get_inventory()
