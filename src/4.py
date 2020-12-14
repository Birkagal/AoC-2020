''' 
Part One - how many passports are valid? those that have all required fields. Treat cid as optional
Part Two - how many passports are valid? those that have all required fields and valid values
'''


def partOne(content):
    credentials = []
    single_credential = ""
    valid_passports = 0
    for line in content:
        if line:
            single_credential += line + " "
        else:
            credintial_dict = dict(
                map(lambda x: x.split(':'), single_credential.split()))
            credentials.append(credintial_dict)
            single_credential = ""
    credintial_dict = dict(
        map(lambda x: x.split(':'), single_credential.split()))
    credentials.append(credintial_dict)
    for data in credentials:
        if len(data.keys()) == 8:
            valid_passports += 1
        elif len(data.keys()) == 7:
            if "cid" not in data:
                valid_passports += 1
    return valid_passports


def partTwo(content):
    credentials = []
    single_credential = ""
    valid_passports = 0
    for line in content:
        if line:
            single_credential += line + " "
        else:
            credintial_dict = dict(
                map(lambda x: x.split(':'), single_credential.split()))
            credentials.append(credintial_dict)
            single_credential = ""
    credintial_dict = dict(
        map(lambda x: x.split(':'), single_credential.split()))
    credentials.append(credintial_dict)
    for data in credentials:
        if len(data.keys()) == 8:
            if validate_passport(data):
                valid_passports += 1
        elif len(data.keys()) == 7:
            if "cid" not in data:
                if validate_passport(data):
                    valid_passports += 1
    return valid_passports


def validate_passport(data):
    byr = data["byr"]
    iyr = data["iyr"]
    eyr = data["eyr"]
    hgt = data["hgt"]
    hcl = data["hcl"]
    ecl = data["ecl"]
    pid = data["pid"]
    if byr.isnumeric() and (1920 <= int(byr) <= 2002):
        if iyr.isnumeric() and (2010 <= int(iyr) <= 2020):
            if eyr.isnumeric() and (2020 <= int(eyr) <= 2030):
                if hgt[0:-2].isnumeric():
                    if (hgt[-2:] in 'cm' and (150 <= int(hgt[0:-2]) <= 193)) or (hgt[-2:] in 'in' and (59 <= int(hgt[0:-2]) <= 76)):
                        if hcl[0] == '#' and len(hcl) == 7 and hcl[1:].isalnum():
                            if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                if pid.isnumeric() and len(pid) == 9:
                                    return True

    return False
