import urllib.request


def get_input(day):
    cookie = read_cookie()
    url = f'https://adventofcode.com/2023/day/{day}/input'
    request = urllib.request.Request(url)
    request.add_header('Cookie', f'session={cookie}')
    with urllib.request.urlopen(request) as response:
        return [line.decode('utf-8') for line in response.readlines()]


def read_cookie():
    try:
        with open('.config/cookie') as file:
            return file.readline()
    except OSError:
        print('Are you missing .config/cookie?')
        return None
