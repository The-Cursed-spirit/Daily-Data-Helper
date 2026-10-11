
class DailyDataHelper:
    def __init__(self, data):
        self.data = data
        print("Daily Data Helper started!")

    def show_data(self):
        print("\nDaily Data:")
        for index, value in enumerate(self.data):
            print(index, ":", value)

    def search_data(self, target):
        print("\nSearching for:", target)
        for index, value in enumerate(self.data):
            if value == target:
                print("Found at index:", index)
                return
        print("Data not found!")

    def __del__(self):
        print("Daily Data Helper ended!")


# Create an object
daily = DailyDataHelper([10, 20, 30, 40, 50])

# Display all data
daily.show_data()

# Search for a value
daily.search_data(30)

# Search for a missing value
daily.search_data(100)

# Delete the object
del daily
