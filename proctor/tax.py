""" Calculating tax """
def calculate_tax(taxinfo):
    """
    A function calculate_tax that takes an argument as dictionary
    """
    if isinstance(taxinfo, int):
        raise ValueError('Invalid input of type int not allowed')
    people = taxinfo.keys()
    for peo in people:
        if isinstance(taxinfo[peo], str):
            raise ValueError('Allow only numeric input')
        earning = taxinfo[peo]
        if earning <= 1000:
            taxinfo[peo] = (earning * 0)
        elif earning in range(1001, 10001):
            taxinfo[peo] = (earning - 10000) * 0.1
        elif earning in range(10001, 20201):
            tax1 = 1000 * 0
            tax2 = 9000 * 0.1
            tax3 = (earning - 10000) * 0.15
            taxinfo[peo] = (tax1 + tax2 + tax3)
        elif earning in range(20201, 30750):
            tax1 = 1000 * 0
            tax2 = 9000 * 0.1
            tax3 = 10200 * 0.15
            tax4 = (earning - 20200) * 0.20
            taxinfo[peo] = (tax1 + tax2 + tax3 + tax4)
        elif earning in range(30751, 50001):
            tax1 = 1000 * 0
            tax2 = 9000 * 0.1
            tax3 = 10200 * 0.15
            tax4 = (30750 - 20200) * 0.20
            tax5 = (earning - 30750) * 0.25
            taxinfo[peo] = (tax1 + tax2 + tax3 + tax4 + tax5)
        elif earning >= 50001:
            tax1 = 1000 * 0
            tax2 = 9000 * 0.1
            tax3 = 10200 * 0.15
            tax4 = (30750 - 20200) * 0.20
            tax5 = (50000 - 30750) * 0.25
            tax6 = (earning - 50000) * 0.30
            taxinfo[peo] = (tax1 + tax2 + tax3 + tax4 + tax5 + tax6)
    return taxinfo
