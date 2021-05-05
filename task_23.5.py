def same_by(characteristic, objects):
    if not objects:
        return True
    etalon = characteristic(objects[0])
    for obj in objects:
        if characteristic(obj) != etalon:
            return False
    return True
