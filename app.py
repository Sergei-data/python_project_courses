purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(purchases):
    return sum(p["price"] * p["quantity"] for p in purchases)

def product_by_category(purchases): 
    result = {}
    for p in purchases:
        cat = p["category"]
        item = p["item"]
        if cat not in result:
            result[cat] = set()
        result[cat].add(item)
    return {k: list(v) for k, v in result.items()}

def shoping_filter(purchases, min_price):
    return [p for p in purchases if p["price"] >= min_price]

def avg_price_by_category(purchases):
    totals = {}
    counts = {}
    for p in purchases:
        cat = p["category"]
        totals[cat] = totals.get(cat, 0) + p["price"]
        counts[cat] = counts.get(cat, 0) + 1
    return {cat: round(totals[cat] / counts[cat], 2) for cat in totals}

def most_popylar_category(purchases):
    category_quantities = {}
    for p in purchases:
        cat = p["category"]
        category_quantities[cat] = category_quantities.get(cat, 0) + p["quantity"]
    return max(category_quantities, key=category_quantities.get)


print("Общая выручка:", total_revenue(purchases))
print("Товары по категориям:", product_by_category(purchases))
print("Покупки дороже 1.0:", shoping_filter(purchases, 1.0))
print("Средняя цена по категориям:", avg_price_by_category(purchases))
print("Категория с наибольшим количеством проданных товаров:", most_popylar_category(purchases))
