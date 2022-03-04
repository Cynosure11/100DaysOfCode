# EXCEPTIONS = ИСКЛЮЧЕНИЯ

# TRY: something that might cause an exception
# EXCEPT: do this if there was an exception
# ELSE: do this if there were no exceptions
# FINALLY: do this no matter what happened


# FileNotFound
# with open("a_file.txt") as file:
#    file.read()
# try:
#    file = open("a_file.txt")
#    a_dictionary = {"key": "value"}
#    print(a_dictionary["Your code is work ✅"])
# except FileNotFoundError:
#    file = open("a_file.txt", "w")
#    # If you use "w" - write and automatically create new file
#    file.write("something")
# except KeyError as error_message:
#    print(f"The key {error_message} does not exist")
# else:
#    content = file.read()
#    print(content)
# version 1 with finally:
# finally:
#    file.close()
#    print("File was closed")
# version 2 with finally:
# finally:
#    raise TypeError("This is message an error that I made up.")


# ----------------- Make your own error message code ----------------- #
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight/height ** 2
print(bmi)

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# Type
# text = "abc"
# print(text + 5)

