import os
import math


#Determine lot size tier
def determine_lot_size(lot_size):

    tier1 = "Lot Size Tier 1"
    tier2 = "Lot Size Tier 2" 
    tier3 = "Lot Size Tier 3"
    tier4 = "Lot Size Tier 4" 
    tier5 = "Lot Size Tier 5"

    if lot_size < 7500: 
        print(lot_size)
        return tier1
    elif lot_size in range(7500, 10999):
        print(lot_size)
        return tier2
    elif lot_size in range(11000, 17499): 
        print(lot_size)
        return tier3
    elif lot_size in range(17500, 43559): 
        print(lot_size) 
        return tier4
    elif lot_size > 43560: 
        print(lot_size)
        return tier5
    else: 
        print("waiting for other shit")


def determine_tier_lot(HCF, tier2_range, tier3_range, tier4_range):
    if HCF == 8:
        print("Tier 1 water usage")
    elif HCF in tier2_range:
        print("Tier 2 water Usage")
    elif HCF in tier3_range:
        print("Tier 3 water Usage")
    elif HCF in tier4_range: 
        print("Tier 4 Water usuage")
    else:
        print("Need HCF")

    print(lot_tier)


def determine_HCF(lot_tier, HCF):

    #Default tier ranges
    tier2_range = range(9, 17)
    tier3_range = range(15, 35)
    tier4_range = range(26, 44)

    if lot_tier == "Lot Size Tier 1":
        determine_tier_lot(HCF, )

    elif lot_tier == "Lot Size Tier 2":
        tier2_range = range(9, 20)
        tier3_range = range(18, 44)
        tier4_range = range(35, 44)
        determine_tier_lot(HCF, tier2_range, tier3_range, tier4_range) 

    elif lot_tier == "Lot Size Tier 3":
        tier2_range = range(9, 33)
        tier3_range = range(26, 83)
        tier4_range = range(59, 83)
        determine_tier_lot(HCF, tier2_range, tier3_range, tier4_range)

    elif lot_tier == "Lot Size Tier 4":
        tier2_range = range(9, 39)
        tier3_range = range(30, 101)
        tier4_range = range(71, 101)
        determine_tier_lot(HCF, tier2_range, tier3_range, tier4_range)

    elif lot_tier == "Lot Size Tier 5":
        tier2_range = range(9, 39)
        tier3_range = range(30, 101)
        tier4_range = range(71, 101)
        determine_tier_lot(HCF, tier2_range, tier3_range, tier4_range)
    else:
        print("NO Lot tier inputted")

lot_size = input("Enter lot size:")
my_HCF = input("Enter HCF:") 
lot_size = int(lot_size) 
my_HCF = int(my_HCF) 
lot_tier = determine_lot_size(lot_size) 
determine_HCF(lot_tier, my_HCF)





