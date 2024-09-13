hash_set = set()

hash_set.add("John")
hash_set.add("Willy")
hash_set.add("Jack")
hash_set.add("Alfie")
hash_set.add("Jim")
hash_set.add("Tom")

hash_set.remove("Jack")

print(hash_set.__contains__("Jack"))


dict = {}

dict['Alfie'] = 23
age = dict['Alfie']
