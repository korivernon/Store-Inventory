import mysql.connector
import datetime, pypng
from qrtools import QR
from pillow import Image

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "R0bin54!",
    database = "storeInventory",
    auth_plugin = "mysql_native_password"
)
cursor = mydb.cursor()

class CHECKIN:
    def __init__(self,item_png):
        # Decoding QR Code using QR Tools Module
        # myQRcode takes in the image

        # Using Relative Path
        # Convert to bitmap using .tobitmap()
        # QR Code will be linked to the site link where the item is.
        url = self.url
        myQRcode =

        '''
        img = Image.open(item_png)
        myQRcode = QR(img)
        '''
        # Stored as a code instead of a string for relocation
        self.qr_code = myQRcode.data_to_string() # we expect the decoded qr_code
        self.img = img

    def time_in(self):
        #Returns the Timestamped Date
        # ISO Formatting
        return datetime.now().isoformat()

    def item_checked_out(self):
        return False

    def image(self):
        return self.img

    def qr_code(self):
        return self.qr_code

def checkIn(check_in_bool = True, png):
    item = CHECKIN(png)
    price = input("What is the price of the item? \n")
    store_check_in_em = "korivernon@nyu.edu"
    # Database Columns we want to effect

    checkItemIn = "INSERT INTO store_inventory (image, qr_code, time_in, item_checked_out, store_check_in_em, price, description) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    # Seven Fields in Check In
    # Commit to database
    store_inventory = (item.image(),item.qr_code(),item.time_in(), item.item_checked_out(), store_check_in_em, price)
    # We are finished with the check in.
    # Return a check to ensure row was added.
    cursor.execute(store_inventory,checkItemIn)
    print("Done")
    return checkIn = False

class CHECKOUT:
    def __init__(self, item_qr_code):
        # QR of Item
        self.item_qr = QR(item_qr_code)

    def decode(self, item_qr):
        # Return Decoded String
        return qr_code_str = self.item_qr.data_to_string()

    def date_checked_out(self):
        #Returns the Timestamped Date
        # ISO Formatting
        return datetime.now().isoformat()

    def price(self):
        store_inventory = "SELECT * FROM price WHERE qr_code = %s"
        # Return the price of the item.
        return cursor.execute(store_inventory,self.item_qr.decode())

    def item_checked_out(self):
        return True

def checkOut(check_out_bool = True, qr_code):
    item = CHECKOUT(qr_code)
    item_price = int(item.price())
    # Insert email so that store will be notified upon purchase of item
    store_check_in_em = "korivernon@nyu.edu"

    print("Item price: " + "$" + item_price + .045*item_price)


    promo = input("Special codes or promotions? Y (Yes) N (NO)")
    if promo == "y" or promo == "Y":
        code = input("Code here: ")
        PROMO(code)
        if PROMO.valid() == True:
            new_total = PROMO.discount()*item_price
            new_total = new_total*1.045
            print("New total is:",new_total")

    cont = input("Continue with purchase? Y (Yes), N (No)")
    if cont == False:
        pass

    client_em = input("What is the email of the client? \n")

    checkOut = "INSERT INTO store_inventory (item_checked_out, date_checked_out, client_em, store_sold_em, price) VALUES(%s,%s,%s,%s,%s) WHERE qr_code = %s"
    store_inventory = (item.item_checked_out(),item.date_checked_out(),client_em, item.item_checked_out(), store_check_in_em, price, item.decode())

    cursor.execute(store_inventory,checkOut)
    print("Done")
    return checkItemOut = False

def main():
    print("============ Store Inventory ============\n")
    optionMenu = input("Do you want to check an item in or do you want to check an item out? h (help) \n")
    if optionMenu.lower() == 'h':
        optionMenu = input("I (for check item in), O (for check item out): \n")
    elif optionMenu.lower() == 'o':
        # PNG of item will be
        qr_code_png = input()
        checkOut(True,qr_code_png)
    elif optionMenu.lower() == 'i':
        item_png = input()
        checkIN(True,item_png)
    else:
        raise Exception("That command is not accepted.")
main()
