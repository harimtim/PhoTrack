import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier
import platform
import colorama
import art
import os

#https://github.com/harimtim/PhoTrack

output = 'Location'

def get_location():
    global output
    try:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

        print(f'{colorama.Fore.BLUE}{art.text2art("PhoTrack", font="sub-zero")}{colorama.Fore.YELLOW}')
        number = input(f"Phonenumber: {colorama.Fore.GREEN}")
        
        phoneNumber = phonenumbers.parse(number)

        timeZone = timezone.time_zones_for_geographical_number(phoneNumber)

        geolocation = geocoder.description_for_number(phoneNumber,"en")

        service = carrier.name_for_number(phoneNumber, "en")

        timeZone = timeZone[0]

        print(f"""{colorama.Fore.MAGENTA}
Location -------->: {colorama.Fore.WHITE}{geolocation}{colorama.Fore.MAGENTA}
Time Zone ------->: {colorama.Fore.WHITE}{timeZone}{colorama.Fore.MAGENTA}
Service Provider >: {colorama.Fore.WHITE}{service}{colorama.Fore.CYAN}

Programmer: {colorama.Fore.WHITE}https://github.com/{colorama.Fore.MAGENTA}harimtim{colorama.Fore.WHITE}/PhoTrack
""")



    except:
        print(f"{colorama.Fore.RED}Error{colorama.Fore.WHITE}")

if __name__ == "__main__":
    get_location()