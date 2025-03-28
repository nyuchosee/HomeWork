import csv
import json

def read_books_from_csv(csv_file):
    books = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            book = {
                "title": row['Title'],
                "author": row['Author'],
                "pages": int(row['Pages']),
                "genre": row['Genre'],
            }
            books.append(book)
    return books


def read_users_from_json(json_file):
    with open(json_file, mode='r', encoding='utf-8') as file:
        users = json.load(file)
    return users


def distribute_books(books, users):
    num_books = len(books)
    num_users = len(users)
    result = []

    for i, user in enumerate(users):
        user_books = {
            "name": user['name'],
            "gender": user['gender'],
            "address": user['address'],
            "age": user['age'],
            "books": []
        }

        for j in range(i, num_books, num_users):
            user_books['books'].append(books[j])
        result.append(user_books)
    return result


def write_result_to_json(result, output_file):
    with open(output_file, mode='w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def main():
    books = read_books_from_csv('books.csv')
    users = read_users_from_json('user.json')
    result = distribute_books(books, users)
    write_result_to_json(result, 'result.json')


if __name__ == "__main__":
    main()
