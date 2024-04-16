from models import Quote, Author
import connect


def print_quotes_decorator(func):
    def wrapper(*args):
        quotes = func(*args)
        for quote in quotes:
            print(quote.author.fullname)
            print(quote.quote)

    return wrapper


@print_quotes_decorator
def find_quotes_by_tags(tags):
    return Quote.objects(tags__in=tags)

@print_quotes_decorator
def find_quotes_by_tag(tag):
    return Quote.objects(tags__startswith=tag[0])


@print_quotes_decorator
def find_quotes_by_author(author):
    return Quote.objects(author=Author.objects(fullname__startswith=author[0]).first())


if __name__ == '__main__':
    find_quotes_by_tags(['life', 'world', 'simile'])
    find_quotes_by_author(['Steve Martin'])
