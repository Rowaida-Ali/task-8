list=(input("enter a list ")).split(",")
print(list)
cond=""
def is_sorted(list):
    for i in range(0,len(list)):
        if list[i]>=list[i-1] :
            cond="true"
        else:
            cond="false"    
    print(cond)                               
is_sorted(list)     
user=float(input("how bread did you pay "))
def price(user) :
    bread_price=3.49
    discount=0.06
    price=bread_price*user
    discount=price*discount
    total_price=price-discount
    print(f"your price before price {price}$")
    print(f"the total price equal {total_price}$")
price(user)