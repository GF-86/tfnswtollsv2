# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:32:23 2023
@author: giles.field
"""

class tolldict:
    def __init__(self, data, key='match'):
        if key not in data:
            raise ValueError(f"The key '{key}' is not present in the data.")
        self.data = data[key]

    def hastolls(self):
        if len(self.data.get('tollsCharged')) == 0:
            return False
        else:
            return True

    def confidence(self):
        return self.data.get('confidence')

    def distance(self):
        return self.data.get('distance')

    def duration(self):
        return self.data.get('duration')

    def geometry(self):
        return self.data.get('geometry')

    def is_cheapest(self):
        return self.data.get('isCheapest')

    def is_quickest(self):
        return self.data.get('isQuickest')

    def is_shortest(self):
        return self.data.get('isShortest')

    def max_charge_in_cents(self):
        return self.data.get('maxChargeInCents')

    def min_charge_in_cents(self):
        return self.data.get('minChargeInCents')

    def summary(self):
        return self.data.get('summary')
    
    def tollcostsummary(self):
        templist = []
        if self.hastolls():
            for tollscharged in self.data.get('tollsCharged'):
                for charges in tollscharged.get('charges'):
                    if 'startTime' in charges:
                        templist.append(charges.get('startTime'))
                        templist.append(charges.get('endTime'))
                        templist.append(charges.get('dayOfWeek'))
                    templist.append('$' + str(charges.get('chargeInCents')/100))
                for gantryvisits in tollscharged.get('gantryVisits'):
                    templist.append(gantryvisits.get('gantry').get('motorwayName'))
            return ' '.join(templist)
        else:
            return 'No tolls'
            