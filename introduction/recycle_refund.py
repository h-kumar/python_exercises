
def recycle_refund():
    deposit_ml = 0.10
    deposit_l = 0.25

    recycle_ml = int(input("How many containers less than or equal to a litre?: "))
    recycle_l = int(input("How many containers more than a litre?: "))

    refund = (recycle_ml*deposit_ml)+(recycle_l*deposit_l)
    print("Your total refund will be $%.2f."%refund)

# refund = recycle_refund()

if __name__ == '__main__':
    recycle_refund()



