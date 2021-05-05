def find_farthest_orbit(orb):
    sp = []
    for i in orb:
        sp.append(i[0] * i[1])
    ind = sp.index(max(sp))
    return orb[ind]
     
