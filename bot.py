from queries import find_quotes_by_author, find_quotes_by_tags, find_quotes_by_tag

action_map = {
    'name': find_quotes_by_author,
    'tags': find_quotes_by_tags,
    'tag': find_quotes_by_tag,
}


def parse_command(user_line):
    (command, key) = user_line.split(':')
    keys = key.strip().split(',')
    return command.strip(), keys


def main():
    while True:
        user_line = input('Enter command: ')
        if user_line == 'exit':
            break
        (command, keys) = parse_command(user_line)
        action_map[command](keys)


if __name__ == '__main__':
    main()
