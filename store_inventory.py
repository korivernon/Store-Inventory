import mysql.connector
import datetime, pyqrcode

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "R0bin54!",
    database = "storeInventory",
    auth_plugin = "mysql_native_password"
)

mycursor = mydb.cursor()
mycursor.execute()

sqlFormula = "INSERT INTO store_inventory (qr_code, time_in, time_qr_exp, item_checked_out, date_checked_out, client_em, store_sold_em, store_check_in_em, price) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

class CHECKOUT:
    def __init__(self,qr_code):
        if
        self.qr_code = self.item

    def date(self):
        if self.item is None:
            raise Exception("Item is")

def main():
    print(mydb)

main()
