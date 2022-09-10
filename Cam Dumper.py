import requests, re
from colorama import Fore, Back, Style
print(Fore.LIGHTGREEN_EX +"""

██████╗░░█████╗░██████╗░██╗░░██╗  ██████╗░██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗
██║░░██║███████║██████╔╝█████═╝░  ██║░░██║██║░░░██║██╔████╔██║██████╔╝█████╗░░██████╔╝
██║░░██║██╔══██║██╔══██╗██╔═██╗░  ██║░░██║██║░░░██║██║╚██╔╝██║██╔═══╝░██╔══╝░░██╔══██╗
██████╔╝██║░░██║██║░░██║██║░╚██╗  ██████╔╝╚██████╔╝██║░╚═╝░██║██║░░░░░███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝

""")
print("""\033[1;37m

|==============================================================================================|
| \033[1;31m[#] \033[1;37mDEVELOPER : Under_DarK                    \033[1;31m[#] \033[1;37mDiscord : Under_DarK#8078                    |
| \033[1;31m[#] \033[1;37mDiscord Tag : 8078                      \033[1;31m[#] \033[1;37mWEBSITE : https://offical-of-dark-team.glitch.me             |                                                                                
|==============================================================================================|
| \033[1;32m[1] \033[1;37mAmerika                            | \033[1;32m[11] \033[1;37mCin                                   |
| \033[1;32m[2] \033[1;37mIngiltere                            | \033[1;32m[12] \033[1;37mIstail                                  |
| \033[1;32m[3] \033[1;37mHollanda                              | \033[1;32m[13] \033[1;37mSoudi Arabistan                            |
| \033[1;32m[4] \033[1;37mJaponya                                     | \033[1;32m[14] \033[1;37mTayland                                |
| \033[1;32m[5] \033[1;37mBrezilya                                    | \033[1;32m[15] \033[1;37mUkrayna                                |
| \033[1;32m[6] \033[1;37mTURKIYE                                  | \033[1;32m[16] \033[1;37mSırbisan                           |
| \033[1;32m[7] \033[1;37mIran                                     | \033[1;32m[17] \033[1;37mAlmanya                               |
| \033[1;32m[8] \033[1;37mIspanya                                     | \033[1;32m[18] \033[1;37mPortekiz                                |
| \033[1;32m[9] \033[1;37mKanada                                   | \033[1;32m[19] \033[1;37mMalezya                                |
| \033[1;32m[10] \033[1;37mFinlandiya                                  | \033[1;32m[20] \033[1;37mFransa                                  |
|==============================================================================================|

""")

try:
    print()
    countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL","CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR","NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR","MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH","UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO","TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA","MD", "NI", "MT", "IT", "SA", "HR", "CY", "PK", "AE", "KZ","KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY","AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY","-"]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

# google dorks
  
    link =[
    "https://www.google.com/search?q=intitle:%22webcamxp%22%20%22Flash%20JPEG%20Stream%22"
    "https://www.google.com/search?q=inurl:mobile.html%20intitle:webcamXP"
    "https://www.google.com/search?q=intitle:%22Web%20Client%22%20inurl:%22webcamera.html%22"
    "https://www.google.com/search?q=intitle:%22HD%20IP%20Camera%22%20%22Remember%20me%22%20%22User%20name%22%20-.com%20-pdf"
    "https://www.google.com/search?q=intitle:%22IP%20Webcam%22%20inurl:%22/greet.html%22"
    "https://www.google.com/search?q=intitle:%22NetCamSC*%22"
    "https://www.google.com/search?q=intitle:%22NetCamXL*%22"
    "https://www.google.com/search?q=inurl:%22live/cam.html%22"
    ]

    num = int(input("Enter the country number >>> "))
    print("""
    \033[1;31m
    [ KAMERALAR HACKLENIYOR BEKLEYIN... ]
    
    """)
    if num not in range(1, 20+1):
        raise IndexError

    country = countries[num-1]
    res = requests.get(
        f"https://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"https://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("\033[1;37m[+] online camera :",ip)
except:
    pass
finally:
    print("\033[1;37m")
    exit()
