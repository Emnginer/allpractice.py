print("hell0 wofgggrld")
print("hell0 df")
message = input("> ")
words = message.split(" ")
emoji = {
    ":)": "☺",
    ":(": "☹"
}
output = ""
for word in words:
  output += emoji.get(word, word) + " "
print(output)
def user(firstname, lastname):
    print(f"{firstname} {lastname}")
user(lastname="emon", firstname="das")

