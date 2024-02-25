import requests


def request(url):
    try:
        result = requests.get("https://" + url)
        if result:
            print("[+] Subdomain discovered ------->  " + "'"+url+"'")

    except:
        pass


def main():
    print(" hello")
    target_url = input("Enter the target url : ")
    with open("subdmainwordlist.txt", "r") as wordlist:
        for line in wordlist:
            word = line.strip()
            test_url = word + "." + target_url
            request(test_url)


main()
