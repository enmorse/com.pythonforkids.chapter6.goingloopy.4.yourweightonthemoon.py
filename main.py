current_weight = 210
weight_on_moon = current_weight * 0.165

for year in range(1, 16):
    weight_on_moon += 1
    # print("Year {0} = {1}".format(year, weight_on_moon))
    # print("Year %s =  %s" % (year, weight_on_moon))
    print(f"Year {year} = {weight_on_moon}")
