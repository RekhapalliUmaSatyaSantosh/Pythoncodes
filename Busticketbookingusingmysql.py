import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="santosh@1503",
    database="santosh"
)
cursor=conn.cursor()
def showbuses(From,To):
    print('\n Available Buses are=')
    query="""SELECT busno, Price, Seats 
    FROM buses 
    WHERE LOWER(`From`)=LOWER(%s) 
    AND LOWER(`To`)=LOWER(%s)
    """
    cursor.execute(query, (From,To))
    result = cursor.fetchall()
    for bus in result:
            print('Bus No=',bus[0],
                  '|Price=',bus[1],
                  '|Available seats=',bus[2])

def booking(bus_no,seats_required):
    cursor.execute("SELECT Seats, Price FROM buses WHERE busno=%s", (bus_no,))
    result = cursor.fetchone()
    if result:
        available,price=result
        if available>=seats_required:
            total=seats_required*price
            cursor.execute(
                "UPDATE buses SET Seats=Seats-%s WHERE busno=%s",
                (seats_required, bus_no)
            )
            conn.commit()
            print("\nSeats booked successfully")
            print("Total amount=", total)
        else:
            print("\nNot enough seats")
    else:
        print("\nBus Not Found")


source = input("Enter Source: ")
destination = input("Enter Destination: ")

showbuses(source, destination)

busno = input("\nEnter Bus Number to book: ")
seats = int(input("Enter number of seats: "))

booking(busno, seats)

cursor.close()
conn.close()
