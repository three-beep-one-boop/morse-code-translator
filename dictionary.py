from morsetobeep import beeps

morse_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
              "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
              "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
              "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
              "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
              "z": "--..", "1": ".----", "2": "..---", "3": "...--",
              "4": "....-", "5": ".....", "6": "-....", "7": "--...",
              "8": "---..", "9": "----.", "0": "-----", ".": ".-.-.-",
              ",": "--..--", "?": "..--..", "!": "-.-.--", "'": ".----.",
              "/": "-..-."}


def rep_morse(input: str) -> list[str]:
    if input == "SOS":
        return ["...---..."]
    final = []
    split_input = input.split()
    word_count = 0
    for word in split_input:
        buffer = ""
        for ch in range(len(word)):
            buffer += morse_dict[word[ch]]
            if ch != len(word) - 1:
                buffer += "///"
        final.append(buffer)
        word_count += 1
    return final


my_str = input("Input the string to convert to Morse Code\n").lower()

beeps("my_beeep.mp3", 0.2, rep_morse(my_str))
