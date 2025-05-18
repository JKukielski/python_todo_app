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

files = ['a.txt', 'b.txt', 'c.txt']
for file in files:
    file = open(file, 'r')
    content = file.read()
    print(content)
    file.close()