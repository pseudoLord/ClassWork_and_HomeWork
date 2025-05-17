class BuildingError(Exception):
    def __str__(self):
        return f"With so much materials the house can not be built"


def check_materials(amount, limit):
    if amount > limit:
        return "We have enough materials"
    else:
        raise BuildingError(amount)


materials = 234
limit = 300
print(check_materials(materials, limit))

