ZONES = {
    "Master room": (7, 16, 218, 448),
    "Bedroom1": (220, 16, 349, 165),
    "Bedroom2": (350, 14, 613, 165),
    "Bath": (222, 232, 345, 449),
    "Bedroom3": (352, 236, 526, 449),
    "Hall_Part1": (223, 169, 627, 229),
    "Hall_Part2": (526, 232, 616, 450)
}


def active_zone(x, y):
    for zone_name, (x1, y1, x2, y2) in ZONES.items():
        if x1 < x < x2 and y1 < y < y2:
            if "Hall" in zone_name:
                return "Hall"
            return zone_name
    return None