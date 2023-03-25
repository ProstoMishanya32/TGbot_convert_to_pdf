import os, csv

def read_order_number():
    with open('data/order_number.txt', 'r', encoding="utf-8") as f:
        return int(f.read())

def write_order_number(order_number):
    with open('data/order_number.txt', 'w', encoding="utf-8") as f:
        f.write(str(order_number))

def read_used_order_numbers():
    if not os.path.exists('data/used_order_numbers.csv'):
        return []
    with open('data/used_order_numbers.csv', 'r', newline='',  encoding="utf-8") as f:
        reader = csv.reader(f)
        return [int(row[0]) for row in reader]

def write_used_order_number(order_number):
    with open('data/used_order_numbers.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([order_number])

def log_order(order_number, text_lines):
    order_number_formatted = f"{order_number // 1000000:03} {order_number // 1000 % 1000:03} {order_number % 1000:03}"

    with open('data/orders_log.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        if os.stat('data/orders_log.csv').st_size == 0:
            writer.writerow(["Order Number", "Text Line 1", "Text Line 2", "Text Line 3", "Text Line 4", "Text Line 5"])
        writer.writerow([order_number_formatted] + text_lines + [''] * (5 - len(text_lines)))