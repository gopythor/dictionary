def add_to_dict(dic, *words):
  if (type(dic) is not dict):
    print("You need to send a dictionary. You sent:",type(dic))
  elif len(words) !=2 :
    print("You need to send a word and a definition.")
  elif words[0] in dic:
    print(words[0],"is already on the dictionary. Won't add.")
  else : 
    dic[words[0]] = words[1]
    print(words[0],"has been added.")
 

def get_from_dict(dic, *words):
  if (type(dic) is not dict):
    print("You need to send a dictionary. You sent:",type(dic))
  elif len(words) == 0 or len(words) >2 :
    print("You need to send a word to search for.")
  elif words[0] in dic:
    print(f"{words[0]}:", dic[words[0]])
  else:
    print(f"{words[0]} was not found in this dict.")

def update_word(dic, *words):
  if (type(dic) is not dict):
    print("You need to send a dictionary. You sent:",type(dic))
  elif len(words) == 1  or len(words) >3 :
    print("You need to send a word and a definition to update.")
  elif words[0] in dic:
    dic[words[0]] = words[1]
    print(words[0], "has been updated to:", dic[words[0]])
  else:
    print(f"{words[0]} is not on the dict. Can't update non-existing word.")

def delete_from_dict(dic, *words):
  if (type(dic) is not dict):
    print("You need to send a dictionary. You sent:",type(dic))
  elif len(words) == 0 or len(words) >2 :
    print("You need to specify a word to delete.")
  elif words[0] in dic:
    del dic[words[0]]
    print(words[0],"has been deleted.")
  else:
    print(f"{words[0]} is not in this dict. Won't delete.")

import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")