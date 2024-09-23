# Car Rental System

## Main menu
def main_menu():
    print("Welcome to The Car Rental")
    print("Choose menu list:")
    print("1. Car Databases")
    print("2. Add New Car")
    print("3. Car Undermaintenance")
    print("4. Customer Information")
    print("5. Book a Car")
    print("6. Delete Car")
    print("7. Exit the menu")

# 1. Car Databases

# Database dummy
car_data = {
    "1": {
        "car_id": "1",
        "name": "calya",
        "transmission": "matic",
        "year": 2018,
        "seats": 6,
        "price_per_day": 250000,
        "availability": False,
        "broke_stat": False,
    },
    "2": {
        "car_id": "2",
        "name": "raize",
        "transmission": "matic",
        "year": 2019,
        "seats": 4,
        "price_per_day": 300000,
        "availability": False,
        "broke_stat": True,
    },
    "3": {
        "car_id": "3",
        "name": "livina",
        "transmission": "matic",
        "year": 2020,
        "seats": 6,
        "price_per_day": 500000,
        "availability": True,
        "broke_stat": False,
    },
    "4": {
        "car_id": "4",
        "name": "sigra",
        "transmission": "manual",
        "year": 2022,
        "seats": 6,
        "price_per_day": 410000,
        "availability": True,
        "broke_stat": False,
    },
    "5": {
        "car_id": "5",
        "name": "avanza",
        "transmission": "manual",
        "year": 2023,
        "seats": 6,
        "price_per_day": 450000,
        "availability": True,
        "broke_stat": False,
    },
}

def database():
    print(
        "car_id\tName\tTransmission\tYear\t\tSeats\tPrice per Day\tAvailability\tMaintenance Status")  # make a header
    for (car_id,car_details,) in (car_data.items()):  # loop to iterates car_data dict with car_id is the unique key and car_details takes car's details
        print("{}\t\t{}\t{}\t\t{}\t{}\t\t{}\t\t{}\t\t{}".format(
                car_details["car_id"],
                car_details["name"],
                car_details["transmission"],
                car_details["year"],
                car_details["seats"],
                car_details["price_per_day"],
                "Available" if car_details["availability"] else "Not Available",
                "Yes" if car_details["broke_stat"] else "No",
            )
        )

# filtering car database
# available cars
def avail_cars():
    def get_available_cars(car_data):
        available_cars = []
        for car_id, car_info in car_data.items():
            if car_info["availability"]:
                available_cars.append(car_info)
        return available_cars
    # new available car data
    available_cars = get_available_cars(car_data)
    # print the data
    print("car_id\tName\tTransmission\tYear\t\tSeats\tPrice per Day\tAvailability\tMaintenance Status")  # make a header
    for data in available_cars:
        print(
            "{}\t\t{}\t{}\t\t{}\t{}\t\t{}\t\t{}\t\t{}".format(
                data["car_id"],
                data["name"],
                data["transmission"],
                data["year"],
                data["seats"],
                data["price_per_day"],
                "Available" if data["availability"] else "Not Available",
                "Yes" if data["broke_stat"] else "No",
            )
        )

# car rented
def rented_cars():
    def get_rented_cars(car_data):
        rented_cars = []
        for car_id, car_info in car_data.items():
            if car_info["availability"] == False and car_info["broke_stat"] == False:
                rented_cars.append(car_info)
        return rented_cars
    # new rented car data
    rented_cars = get_rented_cars(car_data)
    # print the data
    print("car_id\tName\tTransmission\tYear\t\tSeats\tPrice per Day\tAvailability\tMaintenance Status")  # make a header
    for data in rented_cars:
        print(
            "{}\t\t{}\t{}\t\t{}\t{}\t\t{}\t\t{}\t\t{}".format(
                data["car_id"],
                data["name"],
                data["transmission"],
                data["year"],
                data["seats"],
                data["price_per_day"],
                "Available" if data["availability"] else "Not Available",
                "Yes" if data["broke_stat"] else "No",
            )
        )

# car undermaintenance
def maintenance_cars():
    def get_maintenance_cars(car_data):
        maintenance_cars = []
        for car_id, car_info in car_data.items():
            if car_info["availability"] == False and car_info["broke_stat"] == True:
                maintenance_cars.append(car_info)
        return maintenance_cars
    # new under maintenance car data
    maintenance_cars = get_maintenance_cars(car_data)
    # print the data
    print("car_id\tName\tTransmission\tYear\t\tSeats\tPrice per Day\tAvailability\tMaintenance Status")  # make a header
    for data in maintenance_cars:
        print(
            "{}\t\t{}\t{}\t\t{}\t{}\t\t{}\t\t{}\t\t{}".format(
                data["car_id"],
                data["name"],
                data["transmission"],
                data["year"],
                data["seats"],
                data["price_per_day"],
                "Available" if data["availability"] else "Not Available",
                "Yes" if data["broke_stat"] else "No",
            )
        )

# car database system
def cardata_sys():
    print("Car Database Menu")
    print("1. All cars database\n2. Available cars database\n3. Rented cars database\n4. Car under maintenance")
    option = int(input("Enter the number of the menu: "))
    if option == 1:
        database()
    elif option == 2:
        avail_cars()
    elif option == 3:
        rented_cars()
    elif option == 4:
        maintenance_cars()
    else:
        print("Your input is not valid")

# 2. Add New Car
# Check the car_id in the car database
def is_car_id_used(car_id):
    return car_id in car_data

# add car function
def add_car():
    car_id_check = input("Enter new car id: ")
    if is_car_id_used(car_id_check):
        print(f"Car_id {car_id_check} is not available")
    else:
        newcar_id = car_id_check
        name = input("Enter new car name: ")
        transmission = input("Enter new car transmission: ")
        year = int(input("Enter the year of the car: "))
        seats = int(input("Enter number of seats: "))
        price = int(input("Enter rent price per day: "))
        newdata = {
            "car_id": car_id_check,
            "name": name,
            "transmission": transmission,
            "year": year,
            "seats": seats,
            "price_per_day": price,
            "availability": True,
            "broke_stat": False,
        }
        car_data[newcar_id] = newdata
        database()

# 3. Car Under Maintenance

def update_broken_car():
    car_id = input("Enter car_id that you want to update: ")
    if is_car_id_used(car_id):
        status = input("Is the car undermaintanance or not? (yes/no)")
        if status == "yes" or status == "Yes" or status == "YES":
            # updating car_data data
            car_data[car_id]["availability"] = False
            car_data[car_id]["broke_stat"] = True
        elif status == "no" or status == "No" or status == "NO":
            # updating car_data data
            car_data[car_id]["availability"] = True
            car_data[car_id]["broke_stat"] = False
        else:
            print("Input is not valid")
    else:
        print("car_id doesn't exist")
    database()


# 4. Customer information
# customer dummy data
cust_data = {
    "cust_id": ["C1", "C2"],
    "name": ["Andi", "Budi"],
    "telp_num": ["08123456789", "08987654321"],
    "car_booked": [False, True],
    "bookcar_id": [None, "1"],
}

# customer database
def cust_database():
    print("Customer Database Menu")
    print("1. Get Customer Data")
    print("2. Delete Customer Data")

# read customer database
def get_cust():
    print("Index\tCust_ID\tName\t Telephone Number\tRent Car\t\tcar_id")
    for i in range(len(cust_data["name"])):
        print(f"{i+1}", end="\t\t")
        for key, value in cust_data.items():
            print(f"{value[i]}", end="\t\t")
        print()

# delete customer from database
def del_cust():
    get_cust()
    del_index = int(input("Enter the index of the customer you want to delete: "))
    index = del_index - 1
    if 0 < del_index <= len(cust_data["name"]):
        cust_data["cust_id"].pop(index)
        cust_data["name"].pop(index)
        cust_data["telp_num"].pop(index)
        cust_data["car_booked"].pop(index)
        cust_data["bookcar_id"].pop(index)
    else:
        print("The index you input is not valid")

# Customer Information System
def cust_sys():
    cust_database()
    menu_index = int(input("Enter the index of the menu: "))
    if menu_index == 1:
        get_cust()
    elif menu_index == 2:
        del_cust()
    else:
        print("Invalid index")


# 5. Car Booking System

def book_car():
    book = input("Enter car_id the customer want to rent: ")
    if is_car_id_used(book) and car_data[book]["availability"] == True:
        day = int(input("How many days the customer want to rent the car: "))
        price = car_data[book]["price_per_day"] * day
        print("Your total price is Rp{}".format(price))
        cust = input("have the customer ever rented here? (yes/no)")
        if cust == "yes" or cust == "Yes" or cust == "YES":
            cust_info = input("Enter customer id: ")
            info = cust_info.upper()
            cust_index = cust_data["cust_id"].index(info)
            # update customer data
            cust_data["car_booked"][cust_index] = True
            cust_data["bookcar_id"][cust_index] = book
            # update car database
            car_data[book]["availability"] = False
        elif cust == "no" or cust == "No" or cust == "NO":
            cust_id = input("Enter new customer id: ")
            name = input("Enter customer name: ")
            num = input("Enter customer telephone number: ")
            cust_data["cust_id"].append(cust_id)
            cust_data["name"].append(name)
            cust_data["telp_num"].append(num)
            cust_data["car_booked"].append(True)
            cust_data["bookcar_id"].append(book)
            # update car database
            car_data[book]["availability"] = False
        else:
            print("Your input is not valid")
    else:
        print("car_id doesn't exist")

    database()
    get_cust()

    # Payment system

    money = int(input("Enter the amount of money: "))
    if money < price:
        while money < price:
            less = price - money
            print(f"Your money is less than {less}")
            money = int(input("Enter the amount of money: "))
    elif money > price:
        change = money - price
        print(f"Your money back: {change}")
    elif money == price:
        print("Thank You!")
    else:
        print("Your input is not valid")


# 6. Delete existing car in the car database

def del_car():
    database()
    del_index = input("Enter car_id you want to delete: ")
    if is_car_id_used(del_index):
        car_data.pop(del_index)
    else:
        print("car_id doesn't exist")
    database()


## Main system

while True:
    main_menu()
    option = int(input("Enter the number of the menu: "))
    if option == 1:
        database()
    elif option == 2:
        add_car()
    elif option == 3:
        update_broken_car()
    elif option == 4:
        cust_sys()
    elif option == 5:
        book_car()
    elif option == 6:
        del_car()
    elif option == 7:
        print("Exiting the program...")
        break
    else:
        print("Your input is not valid")
