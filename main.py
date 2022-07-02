# with open("some_file.txt", "r") as myfile:
#     myfile.readlines()

# try:
#     some_file = open("some_file.txt")
#     my_dict={"color": "green"}
#     print(my_dict["color"])
# except FileNotFoundError:
#     # print("there was error")
#     some_file=open("some_file.txt", "w")
#     some_file.write("hello world")
# except KeyError as my_key:
#     print(f"That {my_key} key does not exist in dictionary")
#
# else:
#     some_file=open("some_file.txt")
#     content=some_file.read()
#     print(content)
# finally:
#     # raising error
#     raise SystemError("this is something error i created")
    # some_file.close()
    # print("your file is closed")

hight=float(input("Enter hight: "))
weight=int(input("Eniter weight: "))


if hight >3:
    raise KeyError(f"hight: {hight} should be less than 3 meters ")

bmi=weight/hight**2
print(bmi)