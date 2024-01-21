import serial
import time
import re

massa_list = [0] # massa_list cannot start empty
beep_list = []
space_list = []


def morse_to_english(morse_str):

    if len(morse_str) == 0:
        return ""
    print(morse_str)
    morse_str = morse_str.replace("*", "")
    print(morse_str)
    morse_str += '////'
    pointer = 0
    final = ""
    current_word = ""
    while pointer < len(morse_str):
        if morse_str[pointer] == "/":
            pointer += 1
            continue

        try:
            current_morse = morse_str[pointer:morse_str.find("/", pointer)]
            pointer = morse_str.find("/", pointer)
            current_word += morse_dic_reverse[current_morse]

            if pointer + 3 < len(morse_str) and morse_str[pointer + 3] == "/":
                final += current_word + " "
                current_word = ""
                pointer += 7
            else:
                pointer += 3
        except KeyError:
            print("Illegal word at index " + str(pointer))
            pointer += 1
    return final

morse_dic_reverse = {'.-': 'a',
                     '-...': 'b',
                     '-.-.': 'c',
                     '-..': 'd',
                     '.': 'e',
                     '..-.': 'f',
                     '--.': 'g',
                     '....': 'h',
                     '..': 'i',
                     '.---': 'j',
                     '-.-': 'k',
                     '.-..': 'l',
                     '--': 'm',
                     '-.': 'n',
                     '---': 'o',
                     '.--.': 'p',
                     '--.-': 'q',
                     '.-.': 'r',
                     '...': 's',
                     '-': 't',
                     '..-': 'u',
                     '...-': 'v',
                     '.--': 'w',
                     '-..-': 'x',
                     '-.--': 'y',
                     '--..': 'z',
                     '.----': '1',
                     '..---': '2',
                     '...--': '3',
                     '....-': '4',
                     '.....': '5',
                     '-....': '6',
                     '--...': '7',
                     '---..': '8',
                     '----.': '9',
                     '-----': '0',
                     '.-.-.-': '.',
                     '--..--': ',',
                     '..--..': '?',
                     '-.-.--': '!',
                     '.----.': "'",
                     '-..-.': '/'}

arduino = serial.Serial(port='/dev/tty.usbserial-10',  baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x,  'utf-8'))
    time.sleep(0.009)
    data = arduino.readline()
    return str(data)

empty_list = True
while True:
    value = write_read(str(2))
    if "space" in value:
        if massa_list[len(massa_list)-1] < 0:
            # Adds spaces together if the last one was a space
            massa_list[len(massa_list)-1] += int(re.findall("(\d+)", value)[0]) * -1
            space_list[len(space_list)-1] += int(re.findall("(\d+)", value)[0]) * -1
        else:
            massa_list.append(int(re.findall("(\d+)", value)[0]) * -1)
            space_list.append(int(re.findall("(\d+)", value)[0]) * -1)
    elif "beep" in value:
        # Adds beeps together if the last one was a beep
        if massa_list[len(massa_list)-1] > 0:
            massa_list[len(massa_list)-1] += int(re.findall("(\d+)", value)[0])
            space_list[len(space_list)-1] += int(re.findall("(\d+)", value)[0])
        else:
            massa_list.append(int(re.findall("(\d+)", value)[0]))
            beep_list.append(int(re.findall("(\d+)", value)[0]))
    elif "OFF" in value:
        break

beep_list.sort()

# To be on the safe side, call "t" the second-smallest beep
t = float(beep_list[2]) # Conversion necessary for arithmetic

# Now, use a for loop to approximate the multiplicity
for i in range(len(massa_list)):
    massa_list[i] = float(float(massa_list[i]) / float(t))

massa_list.remove(0)

for i in range(len(massa_list)):
    # Space case
    if massa_list[i] < 0:
        # spaces can either be multiples of 3 or 7, so
        if abs(massa_list[i]) > 120:
            massa_list[i] = "*"
        # Long pause case 7t
        elif 120 >= abs(massa_list[i]) >= 6:
            massa_list[i] = "///////"
        # Short pause case 3t
        elif 6 > abs(massa_list[i]) >= 2.5:
            massa_list[i] = "///"
        elif 2.5 > abs(massa_list[i]) >= 0.1:
            massa_list[i] = ""
        else:
            massa_list[i] = "*"

    # Beep case
    elif massa_list[i] > 0:
        if 0 < massa_list[i] < 2:
            massa_list[i] = "."
        elif 2 <= massa_list[i] <= 7:
            massa_list[i] = "-"
        else:
            massa_list[i] = "*"
    else:
        print("Oopsies, why is it zero?")
massa_list = "".join(massa_list)
print(morse_to_english(massa_list))
