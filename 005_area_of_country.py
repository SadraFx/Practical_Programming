def truncate_float(float_number, decimal_places):
    multiplier = 10 ** decimal_places
    return int(float_number * multiplier) / multiplier

def area_of_country(name,area):
    world_landmass = 148940000 
    a = 100 * area / world_landmass
    ans = truncate_float(a,2)
    print(name,"is",str(ans)+'%',"of the total world's landmass")

area_of_country("Russia", 17098242)
area_of_country("USA", 9372610)
area_of_country("Iran", 1648195)

