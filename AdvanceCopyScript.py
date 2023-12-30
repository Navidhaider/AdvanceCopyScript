import time
import pyperclip
import keyboard

def read_notepad(file_path):
    with open(file_path, 'r') as file:
        content = file.read().splitlines()
        return content

# Replace 'F:/Folder/test.txt' with the path to your Notepad file
notepad_path = 'F:/Folder/test.txt'

lines = read_notepad(notepad_path)
current_line = 0

while True:
    if keyboard.read_key() == 'insert':  # Check for the 'Insert' key press
        if current_line < len(lines):
            line = lines[current_line]
            current_line += 1
            print(f"Pasting: {line}")

            pyperclip.copy(line)  # Copy the line to clipboard

            # Simulate key presses to perform cut and paste (Ctrl + X for cut, Ctrl + V for paste)
            keyboard.press_and_release('ctrl+x')  # Cut
            time.sleep(0.1)  # Delay for the cut operation to complete
            keyboard.press_and_release('ctrl+v')  # Paste
            keyboard.press_and_release('enter')  # Simulate pressing 'Enter' after pasting the line
            time.sleep(0.5)  # Adjust this delay as needed
        else:
            print("No more lines to paste.")

    if keyboard.is_pressed('q'):
        break

print("Program terminated.")
