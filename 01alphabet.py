
lern_alphabet = {
"a":["APPLE","ANT","AEROPLANE","ALMIRAH","ALPHABET","ALMOND","APRICOT","APARTMENT","AQUARIUM","ARROW"],
"b":["BALL","BAT","BAG","BANANA","BASKET","BELL","BICYCLE","BOOK","BOTTLE","BOX"],
"c":["CAR","CAT","COW","CUP","CLOCK","CANDLE","CANDY","CAKE","CARTOON","CROCODILE"],
"d":["DOG","DOLL","DRESS","DRUM","DINOSAUR","DISH","DIAMOND","DOLPHIN","DUCK","DONKEY"],
"e":["ELEPHANT","EGG","EYE","EARTH","EAGLE","EARRING","ELEPHANT","ENGINE","ELEPHANT","ELEPHANT"],
"f":["FAN","FISH","FROG","FLOWER","FLAG","FORK","FINGER","FARM","FIRE","FIREWORK"],
"g":["GOAT","GUN","GIRAFFE","GLOVES","GLOBE","GARAGE","GARDEN","GATE","GHOST","GIFT"],
"h":["HORSE","HEN","HAT","HOUSE","HAMMER","HAND","HEART","HELICOPTER","HELLO","HONEY"],
"i":["ICECREAM","IGLOO","IGUANA","INK","IRON","ICE","INDIA","INSTRUMENT","INSECT","INTERNET"],
"j":["JUG","JAM","JEEP","JACKET","JELLY","JEWELLERY","JOKER","JUICE","JUNGLE","JUMP"],
"k":["KITE","KEY","KANGAROO","KING","KITCHEN","KID","KITE","KITTEN","KITE","KITE"],
"l":["LION","LAMP","LEMON","LEAF","LADDER","LADYBUG","LADYFINGER","LAPTOP","LION","LUNCH"],
"m":["MONKEY","MANGO","MOON","MOTORCYCLE","MIRROR","MILK","MOUNTAIN","MICROWAVE","MOSQUITO","MUSHROOM"],
"n":["NEST","NECKLACE","NUT","NAIL","NEEDLE","NEWSPAPER","NIGHT","NOTEBOOK","NOSE","NURSE"],
"o":["ORANGE","OWL","OCTOPUS","OIL","ONION","OCTAGON","OVAL","OCEAN","OFFICE","ORCHID"],
"p":["PENCIL","PEN","PUMPKIN","POT","PARROT","PINEAPPLE","PIG","PIANO","POLICE","POTATO"],
"q":["QUEEN","QUILT","QUARTER","QUESTION","QUICK","QUIET","QUICK","QUICK","QUICK","QUICK"],
"r":["RABBIT","ROSE","RAT","RADIO","RAINBOW","RACKET","RIVER","ROCKET","RABBIT","RICE"],
"s":["SUN","STAR","SNAKE","SHIP","SCHOOL","SAND","SQUARE","SUNFLOWER","SUNGLASSES","SUGAR"],
"t":["TIGER","TOMATO","TRAIN","TELEVISION","TABLE","TURTLE","TIGER","TIGER","TIGER","TIGER"],
"u":["UMBRELLA","UNIFORM","UNICORN","UNIVERSE","UNION","UNICORN","UNICORN","UNICORN","UNICORN","UNICORN"],
"v":["VOLCANO","VASE","VAN","VIOLIN","VILLAGE","VOLLEYBALL","VOLLEYBALL","VOLLEYBALL","VOLLEYBALL","VOLLEYBALL"],
"w":["WATERMELON","WATCH","WATER","WHEEL","WINDOW","WHALE","WATERFALL","WATERFALL","WATERFALL","WATERFALL"],
"x":["XYLOPHONE","XMAS","XRAY","XMAS","XMAS","XMAS","XMAS","XMAS","XMAS","XMAS"],
"y":["YAK","YARD","YOGA","YOGURT","YOGA","YOGA","YOGA","YOGA","YOGA","YOGA"],
"z":["ZEBRA","ZOO","ZEBRA","ZEBRA","ZEBRA","ZEBRA","ZEBRA","ZEBRA","ZEBRA","ZEBRA"]
}
user_input = input("enter a letter:")
if user_input in lern_alphabet:
    print(f"words{lern_alphabet[user_input]}")
else:
    print("please enter a valid leter")










