import os
#import django models

def get_property_tier_usage(self, pk):
        user_profile = self.get_profile(pk=pk)
        prop = user_profile.user_property
        hcf_water = prop.hcf_usage
        lot_size = int(prop.lot_size)
        county_lot_ranges = LotSize.objects.filter(county=user_profile.county)
        for lot in county_lot_ranges:
            if lot_size in range(lot.lot_size_low, lot.lot_size_high):
                hcf_tiers = Tier.objects.filter(lot_size=lot)
                for tier in hcf_tiers:
                    if hcf_water in range(tier.tier_range_low, tier.tier_range_high):
                        return tier

def charge_tier_usage(self, pk):
        profile = Profile.objects.get(pk=pk)
        prop = profile.user_property
        hcf_water = prop.hcf_usage
        lot_size = prop.lot_size
        county_lot_ranges = LotSize.objects.filter(county=profile.county)
        tier_usage = self.get_property_tier_usage(profile.pk)
        print("HCF Water usage {}".format(hcf_water))
        charge_sum = 0
        final_charge = 0
        for lot in county_lot_ranges:
            if lot_size in range(lot.lot_size_low, lot.lot_size_high):
                hcf_tiers = Tier.objects.filter(lot_size=lot)
                subtract = hcf_water
                for tier in hcf_tiers:
                    if(subtract > 0):
                        print("{} - {} ".format(subtract, tier.tier_range_high - 1)) 
                        subtract -= tier.tier_range_high - 1
                        print("Subtract value: {}".format(subtract))
                        if(subtract < 0):
                            print("Value {}".format(subtract + tier.tier_range_high - 1))
                            remainder = subtract + tier.tier_range_high - 1 
                            charge = float(tier.billing_amount) * (remainder) 
                            charge_sum += charge
                            print("Final Charge {}".format(charge_sum))
                        else:
                            charge = float(tier.billing_amount) * (tier.tier_range_high - 1)
                            print("{} x {}".format(tier.billing_amount, tier.tier_range_high - 1))
                            print("Charge {} Dollars: ".format(charge))
                            charge_sum += charge
                            print("This the total: {}".format(charge_sum))
                    else:
                        print("Not subtracting any more")

        charge_without_county = charge_sum
        county_charges = Charge.objects.filter(county=profile.county)
        service_charge = 0
        float(service_charge)
        for charge in county_charges: 
            service_charge += charge.charge_amount
            print("Apply {} charge for {}".format(charge.title, charge.charge_amount))

        print("Service charge total: {}".format(service_charge)) 
        print("{} + {} = {} ".format(service_charge, charge_sum, float(service_charge) + charge_sum)) 

        final_charge = float(service_charge) + charge_sum
        final_charge = round(final_charge, 2)

        return "Total Charge {} ".format(final_charge) 
