import urllib.request


def get_lines(day, cast=str):
    for line in get_input(day):
        yield cast(line)


def get_filename(day):
    return f'data/{day}'


def get_input(day):
    cookie = read_cookie()
    url = f'https://adventofcode.com/2021/day/{day}/input'
    request = urllib.request.Request(url)
    request.add_header('Cookie', f'session={cookie}')
    with urllib.request.urlopen(request) as response:
        return response.readlines()


def read_cookie():
    try:
        with open('.config/cookie') as file:
            return file.readline()
    except OSError:
        print('Are you missing .config/cookie?')
        return None
