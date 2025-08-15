import pymysql

# Database connection function (to avoid repetition)
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="new_user",
        password="new_password",
        database="hotel_db"
    )

# View available rooms
def view_available_rooms():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT RoomID, RoomType, Price FROM rooms WHERE Availability = 'Available'")
        rooms = cursor.fetchall()

        if rooms:
            print("\nAvailable Rooms:")
            for room in rooms:
                print(f"Room ID: {room[0]}, Type: {room[1]}, Price: {room[2]}")
        else:
            print("\nNo rooms available right now.")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

# Book a room
def book_room():
    try:
        customer_name = input("Enter customer name: ")
        room_id = input("Enter room ID: ")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT Availability FROM rooms WHERE RoomID = %s", (room_id,))
        result = cursor.fetchone()

        if result and result[0] == 'Available':
            cursor.execute("UPDATE rooms SET Availability = 'Booked' WHERE RoomID = %s", (room_id,))
            cursor.execute("INSERT INTO customers (CustomerName, RoomID) VALUES (%s, %s)", (customer_name, room_id))
            conn.commit()
            print("\n✅ Room booked successfully!")
        else:
            print("\n❌ Room is not available.")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

# Generate bill
def generate_bill():
    try:
        customer_id = input("Enter customer ID: ")
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT rooms.Price 
            FROM rooms 
            JOIN customers ON rooms.RoomID = customers.RoomID 
            WHERE customers.CustomerID = %s
        """, (customer_id,))
        result = cursor.fetchone()

        if result:
            total_bill = result[0]
            cursor.execute("INSERT INTO billing (CustomerID, Amount) VALUES (%s, %s)", (customer_id, total_bill))
            conn.commit()
            print(f"\n💰 Bill generated: {total_bill}")
        else:
            print("\n❌ Customer not found.")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

# View customers
def view_customers():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT CustomerID, CustomerName, RoomID FROM customers")
        customers = cursor.fetchall()

        if customers:
            print("\nCustomer List:")
            for cust in customers:
                print(f"ID: {cust[0]}, Name: {cust[1]}, Room: {cust[2]}")
        else:
            print("\nNo customers found.")
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

# Main menu
def main():
    while True:
        print("\n==== Hotel Management System ====")
        print("1. View Available Rooms")
        print("2. Book Room")
        print("3. Generate Bill")
        print("4. View Customers")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_available_rooms()
        elif choice == '2':
            book_room()
        elif choice == '3':
            generate_bill()
        elif choice == '4':
            view_customers()
        elif choice == '5':
            print("\nExiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
