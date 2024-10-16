# print("hello world")
book_path="books/frankenstein.txt"

def read_file(path):
  with open(path) as f:
    return f.read()

def count_words(text):
  words = text.split()
  return len(words)

def sort_on(dict):
  return dict["num"]

def report(path):
  text = read_file(path)
  chars = count_chars(text)
  chars_list = []
  for k, v in chars.items():
    char_dict = {"char": k, "num": v}
    if k.isalpha():
      chars_list.append(char_dict)
  chars_list.sort(reverse=True, key=sort_on)
  print(f"--- Begin report of {path} ---")
  print(f"{count_words(text)} words found in the document\n")
  for char in chars_list:
    print(f"The '{char["char"]}' character was found {char["num"]} times")
  print("--- End report ---")

def count_chars(text):
  chars = {}
  for char in text:
      if not char.lower() in chars.keys():
        chars[char.lower()] = 0
      chars[char.lower()] += 1
  return chars

def ___main___():
#  text = read_file(book_path) 
  report(book_path)
#  print(text)
#  print(count_words(text))
#  print(count_chars(text)) 

___main___()  
