from models import Author, Quote
import connect
import json


def convert_json_to_list(json_path):
    with open(json_path) as f:
        objects = json.load(f)
    return objects


def insert_reference_field_to_objects(objects, field):
    for item in objects:
        item[field] = Author.objects(fullname=item[field]).first()
    return objects


def seed_models(model, seeds):
    for seed in seeds:
        model(**seed).save()


def main():
    seed_models(Author, convert_json_to_list('json/authors.json'))
    seed_models(Quote, insert_reference_field_to_objects(convert_json_to_list('json/quotes.json'), 'author'))


if __name__ == '__main__':
    main()
