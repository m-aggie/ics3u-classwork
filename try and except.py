Exercise 82
def main():
    while True:
        try:
            distance = float(input("Enter the distance travelled (km). "))
            if distance < 1:
                raise IndexError
            break
        except (ValueError,IndexError):
            print("Please enter a number. ")

    calculate_the_taxi_fare(distance)

def calculate_the_taxi_fare(distance):
    base_fare = 4.00
    additional_fare = 0.25*(distance/.14)
    total_fare = base_fare + additional_fare
    total_fare = round(total_fare,2)
    print(total_fare)

if __name__ == "__main__":
    main()
    
Exercise 83
