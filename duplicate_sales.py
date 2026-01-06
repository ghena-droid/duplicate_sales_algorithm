sales_records = ["A001", "A002", "A002", "A003", "A001", "A004"]

unique_sales = []

for record in sales_records:
    is_duplicate = False

    for item in unique_sales:
        if record == item:
            is_duplicate = True
            break

if not is_duplicate:
    unique_sales.append(record)
else:
    print("Duplicate skipped:", record)


print("Original Records:", sales_records)
print("Unique Records:", unique_sales)
