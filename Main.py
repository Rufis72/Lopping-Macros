import pyautogui, time, pynput, math
# Put your macro into the Text list on the line below this, put a 'd_' before the text to press that key down, you can also type a bunch of characters, and it will do that for all of them (for example: d_this is example text), 'u_' to press that key up, you can also put a bunch of characters to do it for all of those characters (ex: u_this is example text), and nothing to tap it for wait's value (the variable). You can also put in 'wait_' and then a number to have it wait that many milliseconds.
Text = ["e", "cheese", "wait_300"]
wait = 0 # this is how much it waits between each action is milliseconds
quick_key_press = 1 # this is how fast it will type a key when you just enter a key
activation_key = "F12"
is_looping = False
# checking for the press of the activation key
def key_pressed(key):
    global is_looping
    if key == pynput.keyboard.Key.f12:
        is_looping = not is_looping
Listener = pynput.keyboard.Listener(on_press=key_pressed)
Listener.start()
while True:
    if is_looping:
        for character in enumerate(Text):
            temp_characters = character[1].split("_")
            if len(temp_characters) == 1:
                pyautogui.typewrite(temp_characters[0], wait/1000)
            else:
                if temp_characters[0] == "d":
                    if len(temp_characters[1]) != 1:
                        for char in temp_characters[1]:
                            pyautogui.keyDown(char)
                    else:
                        pyautogui.keyDown(temp_characters[1])
                elif temp_characters[0] == "u":
                    if len(temp_characters[1]) != 1:
                        for char in temp_characters[1]:
                            pyautogui.keyUp(char)
                    else:
                        pyautogui.keyUp(temp_characters[1])
                elif temp_characters[0] == "wait":
                    for waiting in range(int(math.floor(float(temp_characters[1])))):
                        time.sleep(0.001)
                else:
                    raise Exception(f"'{temp_characters[1]}' is not valid, you can either do 'u_', 'd_', 'wait_', a character to press quickly, or a bunch of characters to press quickly.")