def Liter100km_ke_mpg(liter):
    # 100 km dalam mil = 100000 meter / 1609.344 meter
    mil = 100 / 1.609344
    # Liter ke galon
    galon = liter / 3.785411784
    return mil / galon

def mpg_ke_Liter100km(mpg):
    # 1 galon dalam liter
    liter = 3.785411784
    # mpg (mil per galon) dikonversi ke km per galon
    km100 = (mpg * 1.609344) / 100
    return liter / km100


print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.0))
print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))