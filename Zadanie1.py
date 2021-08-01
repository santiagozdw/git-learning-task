print("Zadanie1")
shopping_list = ["chleb","bułki","pączek","marchew","seler","rukola"]
shopping_dict = {
    "piekarnia": ["chleb","bułki","pączek"],
    "warzywniak": ["marchew","seler","rukola"]
}
for shops, product in shopping_dict.items():
    print(f"ide do {shops.capitalize()} po {[name.capitalize()for name in product]}")
print (f"W sumie kupiłem {len(shopping_list)} produktów")
for shops, product in shopping_dict.items():
    print(f"W {shops} kupuje {len(product)} produktów")
print ("Pozdrowienia z Niderlandów dla Radała Korzeniowskiego")