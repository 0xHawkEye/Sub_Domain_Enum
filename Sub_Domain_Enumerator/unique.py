import requests
import threading
import sys


# Global variables
found_subdomains = set()
progress = 0
total_domains = 0
print_lock = threading.Lock()
progress_lock = threading.Lock()



def request(url):
    global progress
    try:
        result = requests.get("https://" + url, timeout=5)  # Set timeout to avoid long waits
        if result:
            print_result("[+] Subdomain discovered ------->  '{}'".format(url))
            found_subdomains.add(url)  # Add the found subdomain to the set
    except:
        # Ignore all exceptions silently
        pass
    finally:
        # Update progress
        progress_lock.acquire()
        progress += 1
        progress_lock.release()

        # Update progress bar
        update_progress_bar()

def update_progress_bar():
    global progress
    global total_domains
    percent = progress / total_domains
    bar_length = 50
    filled_length = int(bar_length * percent)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    print_progress('\r[{}] {:.2f}%'.format(bar, percent * 100), end='', flush=True)

def print_result(message, end='\n', flush=False):
    with print_lock:
        if flush:
            sys.stdout.flush()
        sys.stdout.write(message + end)
        sys.stdout.flush()

def print_progress(message, end='\n', flush=False):
    with progress_lock:
        if flush:
            sys.stdout.flush()
        sys.stdout.write(message + end)
        sys.stdout.flush()

def main():
    global total_domains
    banner = """
   _____         _      _____                            _          ______
  / ____|       | |    |  __ \                          (_)        |  ____|
 | (___   _   _ | |__  | |  | |  ___   _ __ ___    __ _  _  _ __   | |__    _ __   _   _  _ __ ____
  \___ \ | | | || '_ \ | |  | | / _ \ | '_ ` _ \  / _` || || '_ \  |  __|  | '_ \ | | | || '_ ` _  |
  ____) || |_| || |_) || |__| || (_) || | | | | || (_| || || | | | | |____ | | | || |_| || | | | | |
 |_____/  \__,_||_.__/ |_____/  \___/ |_| |_| |_| \__,_||_||_| |_| |______||_| |_| \__,_||_| |_| |_|
                   ______                                      ______
                  |______|                                    |______|

"""
    print(banner)
    target_url = input("Enter the target URL: ")
    with open("test.txt", "r") as wordlist:
        domains = wordlist.readlines()
        total_domains = len(domains)
        threads = []
        for line in domains:
            word = line.strip()
            test_url = word + "." + target_url
            thread = threading.Thread(target=request, args=(test_url,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    # Print a new line after all threads finish
    file = "output/" + target_url + ".txt"

    print_result('')
    print("[+] Scanning completed")
    print("[+] Found Subdomains are stored at: output ")

    # Write found subdomains to a text file

    with open(file, "w") as outfile:
        for subdomain in found_subdomains:
            outfile.write(subdomain + '\n')

if __name__ == "__main__":
    main()
