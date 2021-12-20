import requests as rq
import sys
import subprocess
from prettytable import PrettyTable

banner = r"""
 ██▓███   ██▀███   ██▓ ██▒   █▓ ▄▄▄     ▄▄▄█████▓▓█████ ▓█████  ██▀███  
▓██░  ██▒▓██ ▒ ██▒▓██▒▓██░   █▒▒████▄   ▓  ██▒ ▓▒▓█   ▀ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▓██ ░▄█ ▒▒██▒ ▓██  █▒░▒██  ▀█▄ ▒ ▓██░ ▒░▒███   ▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██▀▀█▄  ░██░  ▒██ █░░░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░██▓ ▒██▒░██░   ▒▀█░   ▓█   ▓██▒ ▒██▒ ░ ░▒████▒░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▓     ░ ▐░   ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ░▒ ░ ▒░ ▒ ░   ░ ░░    ▒   ▒▒ ░   ░     ░ ░  ░ ░ ░  ░  ░▒ ░ ▒░
░░         ░░   ░  ▒ ░     ░░    ░   ▒    ░         ░      ░     ░░   ░ 
            ░      ░        ░        ░  ░           ░  ░   ░  ░   ░     
                           ░                                            
"""
print(banner+'\n')

def webtorrent_stream(magnet_href: str, download: bool, stream_choice:int):
    cmd = []
    cmd.append("webtorrent")
    cmd.append(magnet_href)
    if stream_choice == 1:
        if not download:
            cmd.append('--vlc')
    else:
        if not download:
            cmd.append('--chromecast')

    if sys.platform.startswith('linux'):
        subprocess.call(cmd)
    elif sys.platform.startswith('win32'):
        subprocess.call(cmd, shell=True)

def webtorrent_info(magnet_href:str):
    cmd=[]
    cmd.append("webtorrent")
    cmd.append("info")
    cmd.append(magnet_href)
    if sys.platform.startswith('linux'):
        subprocess.call(cmd)
    elif sys.platform.startswith('win32'):
        subprocess.call(cmd, shell=True)

        

def main():
    ans=True
    while ans:
        print ("""
        1. Stream/ Download Movies
        2. Other than movie
        3. Exit
        """)
        ans=input("What would you like to do? ") 
        if ans=="1":
            Movie()
        elif ans=="2":
            Other()    
        elif ans=="3":
            sys.exit()
        elif ans !="":
            print("\n Not Valid Choice Try again") 
        


def Movie():
    x = PrettyTable()
    movie_name = input("Enter the movie name:\n")
    print(f"Searching for {movie_name}")
    base_url = f"https://api.sumanjay.cf/torrent/?query={movie_name}"
    torrent_results = rq.get(url=base_url).json()
    index = 1
    magnets_links = []
    for results in torrent_results:
        if 'movie' in results['type'].lower():
            x.field_names = ["index", "Name", "size"]
            x.add_row([index, results['name'], results['size']])
            index += 1
            magnets_links.append(results['magnet'])
    print(x)        

    if magnets_links:
            print("\n")
            print("Default output location:\n* when streaming: Temp folder\n* when downloading: Current directory")
            choice = int(
                input("\nEnter the index of the movie which you want to stream or Download\n"))
            try:
                magnet_href = magnets_links[choice-1]
                
                download = False
                stream_choice = int(
                    input("\nPress 1 to stream with VLC\n Press 2 to download the movie\n Press 3 to Stream with ChromCast\n"))
                if stream_choice == 2:
                    download = True

                webtorrent_stream(magnet_href, download, stream_choice)
               
            except IndexError:
                print("Incorrect Index entered")
    else:
            print(f"No results found for {movie_name}")

def Other():
        file_name = input("Enter the file name:\n")
        print(f"Searching for {file_name}")
        base_url = f"https://api.sumanjay.cf/torrent/?query={file_name}"
        torrent_results = rq.get(url=base_url).json()
        index = 1
        magnets_links = []
        for results in torrent_results:
            if 'other' in results['type'].lower():
                print(index, ") ", results['name'], "-->", results['size'])
                index += 1
                magnets_links.append(results['magnet'])

        if magnets_links:
            choice = int(
                input("\nEnter the index of the file which you want to Download\n"))
            try:
                magnet_href = magnets_links[choice-1]
                download = True

                webtorrent_stream(magnet_href, download, stream_choice=1)
               
            except IndexError:
                print("Incorrect Index entered")
        else:
            print(f"No results found for {file_name}")

            


main()
input("any key")
sys.exit()


