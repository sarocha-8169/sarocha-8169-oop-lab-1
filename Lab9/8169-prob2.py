import re
txt = input("Enter text: ")
pattern_search = input("Enter pattern: ")
str_search = re.search(pattern_search,txt)

if str_search:
    print(f"Found {pattern_search} in {txt} at {str_search.start()}")
else:
    print(f"Cannot find {pattern_search} in {txt}")

