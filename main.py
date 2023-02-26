import requests
import re


def get_steam_storage(id):
    response = requests.get("https://store.steampowered.com/api/appdetails?appids=" + id + "&cc=us&l=en&v=1")
    result = re.search('Storage:</strong> (.*) available space', str(response.json()[id]['data']['pc_requirements']['minimum']))
    if result:
        return result.group(1)
    else:
        return "No storage info found"


def main():
    print()


if __name__ == '__main__':
    main()
