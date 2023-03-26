"""message = input('>  ')
words = message.split(' ')

emoji = {
    ":)" : "👩🏿",
    ":(" : "😎"
}
output = ''
for item in words:
    output += emoji.get(item, item) + ' '
print(output)
"""


def emoji_converter(message):
    words = message.split(' ')

    emoji = {
        ":)": "😊",
        ":(": "☹"
    }
    output = " "
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input("> ")

print(emoji_converter(message))