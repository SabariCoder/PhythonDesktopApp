# Examples of all standard data types in Python

# Numeric Types
integer_num = 10                # int
float_num = 3.14                # float
complex_num = 2 + 3j            # complex
#print("Numeric Types:"+complex_num)

# Sequence Types
string_val = "Hello, World!"    # str
list_val = [1, 2, 3, 4]         # list
tuple_val = (5, 6, 7, 8)        # tuple
range_val = range(5)            # range

# Mapping Type
dict_val = {'a': 1, 'b': 2}     # dict

# Set Types
set_val = {1, 2, 3}             # set
frozenset_val = frozenset([4, 5, 6])  # frozenset

# Boolean Type
bool_val = True                 # bool

# Binary Types
bytes_val = b'abc'              # bytes
bytearray_val = bytearray(5)    # bytearray
memoryview_val = memoryview(bytes_val) # memoryview

# None Type
none_val = None                 # NoneType

# Print all types and their values
print("int:", integer_num)
print("float:", float_num)
print("complex:", complex_num)
print("str:", string_val)
print("list:", list_val)
print("tuple:", tuple_val)
print("range:", list(range_val))
print("dict:", dict_val)
print("set:", set_val)
print("frozenset:", frozenset_val)
print("bool:", bool_val)
print("bytes:", bytes_val)
print("bytearray:", bytearray_val)
print("memoryview:", memoryview_val)
print("NoneType:", none_val)

for i in range(0, 101, 2):
    print(i)

# Example usage
if __name__ == "__main__":
    print("All data types have been defined and printed.")
    # You can add more operations or functions to manipulate these data types as needed.