import math
from datetime import datetime, time

# Returns number of points awarded to a receipt
def calc_points(receipt):

    points = 0
    
    # One point for every alphanumeric character in the retailer name
    points += sum([char.isalnum() for char in receipt.retailer])

    # 50 points if the total is a round dollar amount with no cents.
    if int(float(receipt.total)) == float(receipt.total):
        points += 50
    
    # 25 points if the total is a multiple of 0.25.
    if float(receipt.total) % 0.25 == 0:
        points += 25

    # 5 points for every two items on the receipt.
    points += 5 * (len(receipt.items) // 2)

    # If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
    for item in receipt.items:
        if len(item.shortDescription.strip()) % 3 == 0:
            points += math.ceil(float(item.price) * 0.2)

    # 6 points if the day in the purchase date is odd.
    day = datetime.strptime(receipt.purchaseDate, "%Y-%m-%d").day
    if day % 2 != 0:
        points += 6
    
    # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    purchase_time = datetime.strptime(receipt.purchaseTime, "%H:%M").time()
    if time(14, 0) < purchase_time < time(16, 0):
        points += 10

    return points