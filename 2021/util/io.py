def get_lines(day, cast=str):
    with open(get_filename(day)) as file:
        for line in file:
            yield cast(line)


def get_filename(day):
    return f'data/{day}'
