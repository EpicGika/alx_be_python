weather = input("What's the weather like today? (sunny/rainy/cold):")

# If the weather is “sunny”, recommend: Wear a t-shirt and sunglasses.

if weather == "sunny":
    print("recommend: Wear a t-shirt and sunglasses.")

elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")

elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")

else:
    print("Sorry, I don't have recommendations for this weather.")
