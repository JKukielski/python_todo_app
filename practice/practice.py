# contents = ["I am creating some dummy content",
#             "This is the second part of dummy content",
#             "The last part of dummy content is this"]
# filenames = ["doc.txt",
#              "report.txt",
#              "presentation.txt"]
#
# for content, filename in zip(contents, filenames):
#     file = open(f"files/{filename}", 'w')
#     file.write(content)
#     file.close()

# while True:
#     prompt = input("Enter a new member: ") + "\n"
#     file = open("members.txt", 'r')
#     contents = file.readlines()
#     file.close()
#     contents.append(prompt)
#
#     file = open('members.txt', 'w')
#     file.writelines(contents)
#     file.close()

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for filename in filenames:
#     file = open(filename, 'w')
#     file.write("Hello")
#     file.close()

# files = ['a.txt', 'b.txt', 'c.txt']
# for file in files:
#     file = open(file, 'r')
#     content = file.read()
#     print(content)
#     file.close()

# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#     print(f"That is {(total_value / value) * 100}%")
# except ValueError:
#     print("You need to enter a number. Run the program again")

def get_average():
    with open('practice/data.txt', 'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)