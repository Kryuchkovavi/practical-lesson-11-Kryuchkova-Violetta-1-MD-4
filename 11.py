def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"название ресторана: {self.restaurant_name}")
            print(f"тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print("Ресотран открыт")

    newRest = Restaurant("MamaMia", "Italian")

    print("название ресторана:", newRest.restaurant_name)
    print("тип кухни:", newRest.cuisine_type)

    newRest.describe_restaurant()
    newRest.open_restaurant()

def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"название ресторана: {self.restaurant_name}")
            print(f"тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print("Ресторан открыт")


    restaurant1 = Restaurant("Burger Palace", "American")
    restaurant2 = Restaurant("Sushi Heaven", "Japanese")
    restaurant3 = Restaurant("Taco Fiesta", "Mexican")

    restaurant1.describe_restaurant()
    restaurant1.open_restaurant()
    restaurant2.describe_restaurant()
    restaurant2.open_restaurant()
    restaurant3.describe_restaurant()
    restaurant3.open_restaurant()

def z3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, initial_rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = initial_rating

        def describe_restaurant(self):
            print(f"Restaurant name: {self.restaurant_name}")
            print(f"Cuisine type: {self.cuisine_type}")
            print(f"Rating: {self.rating}")
            print()

        def update_rating(self, new_rating):
            previous_rating = self.rating
            self.rating = new_rating
            print(f"Rating updated to: {self.rating}")
            average_rating = (previous_rating + new_rating) / 2
            print(f"Средний рейтинг: {average_rating}")
            print()


    restaurant1 = Restaurant("Burger Palace", "American", 3)
    restaurant2 = Restaurant("Pasta Paradise", "Italian", 4.1)
    restaurant3 = Restaurant("Sushi Heaven", "Japanese", 2.5)

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

    restaurant_choice = input("Введите название ресторана для обновления рейтинга: ")

    if restaurant_choice == restaurant1.restaurant_name:
        new_rating = float(input("Введите новую оценку для ресторана: "))
        restaurant1.update_rating(new_rating)
    elif restaurant_choice == restaurant2.restaurant_name:
        new_rating = float(input("Введите новую оценку для ресторана: "))
        restaurant2.update_rating(new_rating)
    elif restaurant_choice == restaurant3.restaurant_name:
        new_rating = float(input("Введите новую оценку для ресторана: "))
        restaurant3.update_rating(new_rating)
    else:
        print("Ресторан не найден.")


z3()