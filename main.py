# with open("some_file.txt", "r") as myfile:
#     myfile.readlines()

try:
    some_file = open("some_file.txt")
    my_dict={"color": "green"}
    print(my_dict["car"])
except FileNotFoundError:
    # print("there was error")
    some_file=open("some_file.txt", "w")
    some_file.write("hello world")
except KeyError as my_key:
    print(f"That {my_key} key does not exist in dictionary")