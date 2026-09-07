import os 
import time
import pandas as pd
class cafe:
    def __init__(self,id,name,order,price):
         self.id=id
         self.name=name
         self.order=order
         self.price=price 
    def bill(self):
        gst = self.price * 5/ 100
        total_bill = gst + self.price 
        print("Please wait........")
        time.sleep(3)
        print("-*-"*40)
        print("   Your Bill   ")
        print("-*-"*40)
        print("ID : ", self.id)
        print("Name : ", self.name)
        print("Order  : ", ", ".join(self.order))
        print("Gst : ", gst)
        return f"Total Bill : ₹{total_bill}"      
    def id_store(self,id):
          id_str=id
          return f"Last ID :{id_str}"            
store="my_cafe.xlsx"
if os.path.exists(store):
    df_old = pd.read_excel(store)
    booking_database = df_old.to_dict(orient="records")
else:
    booking_database = []
while True:
 print("=="*40)
 print("Welcome To My Cafe")
 print("=="*40)
 
 try:
        id=int(input("Enter The ID : "))
        if any(row["ID"] ==id  for row in booking_database ):
         print(f" INvalide ")
         continue
 except ValueError:
     pass
     continue
  
 name=input("Enter The Name : ").title()
 n=int(input("Enter The Order No : "))
 lst=[]
 t_price=0
 for i in range(n):
    order=input("Enter The order : ").title()
    
    try: 
        price=int(input("Enter The Price :₹"))
        lst.append(order)
        t_price+=price
    except ValueError:
        pass
        continue
 print("\n\n\n")     
 obj=cafe(id,name,lst,t_price)
 print(obj.bill())  
 print(obj.id_store(id)) 
 new_bill_record = {
        "ID": obj.id,
        "Name": obj.name,
        "Orders": ", ".join(obj.order), # Saves items list cleanly in Excel cell
        "Total_Amount": obj.price
    }
 booking_database.append(new_bill_record)
    
    
 pd.DataFrame(booking_database).to_excel(store, index=False)
    
 ans = input("\nDo you want to process another customer? (Y/N) : ").strip().title()
 if ans == "N":
        print("🔒 Secure logout triggered. System state closed.")
        break
