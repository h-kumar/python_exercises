def meal_tip_tax():
    gst = 0.05
    tip = 0.18

    meal_amt = float(input("Enter meal amount: ",))

    gst_amt = meal_amt * gst
    tip_amt = meal_amt * tip
    total_amt = meal_amt+gst_amt+tip_amt

    print("Your meal amount is $%.2f."%meal_amt)
    print("Tax amount is $%.2f."%gst_amt)
    print("Tip amount is $%.2f."%tip_amt)
    print("Your final bill amount is $%.2f."%total_amt)

if __name__ == '__main__':
    meal_tip_tax()



