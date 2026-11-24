def compute_pr(generation_kwh,irradiance_kwh_m2,capacity_kwp):
    '''Performance Ratio: actual vs theoretical yield.
     generation_kwh: measured AC output
    irradiance_kwh_m2: POA irradiance at panel surface
    capacity_kwp : plant DC capacity
    Returns PR as a float(0 to 1).'''
    theoretical= irradiance_kwh_m2*capacity_kwp
    if theoretical ==0:
       return None
    return generation_kwh/theoretical

def compute_cuf(generation_kwh,capacity_kwp,hours_in_periods):
    ''' Capacity Utilization Factor(CUF)- also called PLF in India.
    =Actual generation/Maximum possible generation

    generation_kwh: actual AC generation in the period(kWh)
    capacity_kwp: plant DC capacity(kWp)
    hours_in_period: number of hours in period (e.g. 8760 for annual)
    Returns CUF as a float. Rajasthan benchmark: 0.21-0.25 annually.'''

    max_possible= capacity_kwp*hours_in_periods
    if max_possible ==0:
        return None
    return generation_kwh/max_possible

def compute_availability(total_hours,downtime_hours):
    ''' Plant Availability=uptime/schedulded hours.
    total_hours: total scheduled operating hours in period
    downtime_hours: hours the plant was unavailable (any cause)
    Returns availability as float. Target:>0.98(98%).'''
    if total_hours==0:
       return None
    if downtime_hours>total_hours:
        raise ValueError('Down Time cannot be greater than Total Hours')
    uptime=total_hours-downtime_hours
    return uptime/total_hours

avail=compute_availability(8760,120)
print(f'Availability:{avail:.3f}')

cuf=compute_cuf(210000000,100000,8760)
print(f'CUF:{cuf:.3f}')

pr=compute_pr(850000,1050,1000)
print(f'Performance ratio:{pr:.3f}')

import csv
with open(r'C:\Users\RaviShankar\Python Projects/Plant_1_Generation_Data.csv') as f:
    reader=csv.DictReader(f)
    rows=list(reader)

    print(rows[0].keys())
    print(rows[0])
    
