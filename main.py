from energy_utlis import compute_pr,compute_cuf,compute_availability
pr= compute_pr(850000,1050,1000)
cuf= compute_cuf(2100000,1000,8760)
avail= compute_availability(8760,87)

print('===Plant KPI Report===')
print(f'Performance Ration:{pr:.1%}')
print(f'CUF(annual est.:{cuf:.1%})')
print(f'Availability:{avail:.1%}')