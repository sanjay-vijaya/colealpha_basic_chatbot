# import the csv for store a data in csv file .
import csv

# create dictionary to store stock data
stock_data = {
    "APPLE": {
        'symbol': 'AAPL',
        'price': 150,
        'volume': 10000
    },
    "TESLA": {
        'symbol': 'TSLA',
        'price': 700,
        'volume': 50000
    },
    "MICROSOFT": {
        'symbol': 'MSFT',
        'price': 300,
        'volume': 20000
    },
    "AMAZON": {
        'symbol': 'AMZN',
        'price': 185,
        'volume': 15000
    }
}
#create a function for Equalto Symbol
def double_qoute():
    print("="*100)
#create a function for Minus Symbol:
def single_qoute():
    print("-"*100)

def space():
    print()

# create function to get stock data


def main():
    single_qoute()
    print("                  Welcome to Stock Tracker")
    single_qoute()
    print("✅ Available Stocks")
    for stock_name, details in stock_data.items():
        print(
            f"Stock Name: {stock_name} | "
            f"Symbol: {details['symbol']} | "
            f"Price: ₹{details['price']:.2f} | "
            f"Volume: {details['volume']}"
        )
    single_qoute()
# get the Stock  name from User :
    stock_name = input("Enter the Stock Name : ").upper().strip()

# check the stock name in the Stock data :
    if stock_name in stock_data:
        space()
#print the Stock name is select by user
        print(f"\"{stock_name}\" is Available ")
        space()
#print the certain Stock price , select by user
        print(f"Single Stock Price is :\" {stock_data[stock_name]['price']}\"")
        space()
        quantity = int(input("Enter the Quantity of Stock:"))
# convert the Dictionary "Volume " into available Stock 
        available_volume = stock_data[stock_name]["volume"]
#Check the Quantity is correct valuee
        if quantity <= 0:
            print(f"❌ Invalid quantity: {quantity}. Quantity must be greater than 0.")
            return
        
# If the Qyantity is Greater than Dictionary Value is not Accept 
        elif quantity > available_volume:
            print(f"❌ Invalid quantity: {quantity}. Not enough shares available.")
            return
        space()
##print the Quantity and the price of single product and multiple the quatity and price for total amount

        print(f"Single Quantity Price is {quantity} x {stock_data[stock_name]["price"]} = {quantity*stock_data[stock_name]["price"]}")
        single_qoute()
        
# If the Quatityt is correct , the data will be acceptable
        print(f"✅  {quantity} shares of {stock_name} added Successfully !")
        
        total_amount = stock_data[stock_name]["price"]*quantity
        single_qoute()
    else:
        print(f"No information available for \"{stock_name}\" not found in the Stock Data ❌")
        double_qoute()
        return
     # CSV section MUST be inside main()
    print("Do you want to save the file as CSV - Type \"Yes\"")
    save_choice = input("yes/no : ").lower().strip()

    if save_choice == "yes" or save_choice == "y":

        with open("portfolio.csv", mode="w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Stock Name",
                "Symbol",
                "Price",
                "Volume",
                "Quantity",
                "Total Amount"
            ])

            writer.writerow([
                stock_name,
                stock_data[stock_name]["symbol"],
                stock_data[stock_name]["price"],
                stock_data[stock_name]["volume"],
                quantity,
                total_amount
            ])

    single_qoute()
# print the Details :
    double_qoute()
    print(
        f"\nStock Name: {stock_name}"
        f"\nStock Price: ₹{stock_data[stock_name]['price']:.2f}"
        f"\nStock Volume:{stock_data[stock_name]['volume']}"
        f"\nStock Symbol:{stock_data[stock_name]['symbol']}"
        f"\nSelect Quantity: {quantity}"
        f"\nTotal Amount: ₹ {stock_data[stock_name]['price']} x {quantity} = ₹{total_amount:.2f}"
    )
    double_qoute()
    if save_choice == "yes" or save_choice == "y":
        print(f"\n✅ Portfolio saved as portfolio.csv")
    else:
        print(f"\nPortfolio not saved ❌.")
    single_qoute()
    print(f"\nThank you for using Stock Tracker!")
    single_qoute()


# call the function to execute

main()
