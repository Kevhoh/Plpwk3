def calculate_discount(price, discount_percent):
    if discount_percent <= 20: #discount percentage cannot go beyond 20
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else: return price


original_price = int(input("Enter The Price Of The Item: "))
discount_percent = int(input("Enter The Discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

if final_price == original_price:
    print(f"No discount was applied. The Final price is : {final_price}")

else:
    print(f"The final price after applying {discount_percent}% discount is : {final_price}")