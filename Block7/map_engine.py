ZONES = {
    "Master Bedroom": (0, 0, 215, 480),
    "Bedroom 1":      (220, 0, 345, 160),
    "Bedroom 2":      (350, 0, 640, 160),
    "Bathroom":       (220, 235, 345, 480),
    "Bedroom 3":      (350, 235, 520, 480),
    "Hall":           (215, 160, 640, 235),
    "Stairs":         (520, 235, 640, 480)
}

def active_zone(x, y):
    for zone_name, (x1, y1, x2, y2) in ZONES.items():
        if x1 < x < x2 and y1 < y < y2:
            return zone_name
    return None