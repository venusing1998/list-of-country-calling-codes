from db import CODE


def print_country_or_region(code):
    country_or_region = CODE.get(code)
    if country_or_region:
        print("The country or region is:", country_or_region)
    else:
        print("There is no this calling code. Please check the calling code.")


if __name__ == "__main__":
    code = input("Please input the calling code for search:\n")
    print_country_or_region(code)
