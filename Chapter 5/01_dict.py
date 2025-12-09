# Dictionary & sets

# Dictionary is a collection of keys-value pairs.

d = {} # empty dictionary

a = {
    "key": "value",
    "harry": "code",
    "marks": "100",
    "0" : "Harry", # you can write here numbers as keys too but they will be treated as strings
    "list": [1, 2, 9]
}
print(a, type(a)) # Output: <class 'dict'>
print(a["key"]) # Output: "value"
print(a["list"]) # Output: [1, 2, 9]

# PROPERTIES OF PYTHON DICTIONARIES
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys.
