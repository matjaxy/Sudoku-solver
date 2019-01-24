from Tkinter import *
from sudoku import sudoku, begin, debug, print_all
from unicodedata import numeric

frame_list = []


def fill():
    tmp_list = []
    counter = 0
    for y in range(9):
        #print y
        for x in range(9):
            #print sudoku[x][y]
            tmp_list.append(sudoku[x][y])

    for frame in frame_list:
        frame.insert(END, tmp_list[counter], 'normal')
        counter += 1


def clear():
    for frame in frame_list:
        frame.delete('1.0', END)


def grab_numbers():
    tmp_list = []
    n = 0
    ret = 0
    for frame in frame_list:
        try:
            #print frame.get("1.0", END), type(frame.get("1.0", END)) # unicode ...
            k = int(frame.get("1.0", END).encode('ascii'))
            #print k
            #print "kkk", type(k)
            if k:
                tmp_list.append((n, k))
            n += 1
        except:
            n += 1
            #print "Empty field"

   # print "List len:", len(tmp_list)
    for pair in tmp_list:
        x = pair[0] % 9
        y = pair[0] / 9
        if debug:
            print "Value", pair[1], "detected on coords[" + str(pair[0]) + "]", x, y
        sudoku[x][y] = pair[1]

    if debug:
        print_all(sudoku)
    return ret

def check_inputs():
    global label1

    if grab_numbers() != 0:
        print "Some input errors happened."
        return

    #solve
    time = begin()

    # clear fields
    clear()

    # enter numbers into fields
    fill()

    labelText.set(str(time))


root = Tk()
root.title('Sudoku solver 1.0')
root.wm_iconbitmap('ss.ico')
for y in range(9):
    for x in range(9):
        if x == 3:
            frame = Frame(root, borderwidth=3, relief='ridge')#, padx=10)
        else:
            frame = Frame(root, borderwidth=3, relief='ridge')
        frame.grid(column=x, row=y, sticky="nsew")
        T = Text(frame, height=1, width=3)
        T.insert(END, "", 'normal')
        T.pack(side=LEFT)
        frame_list.append(T)


frame10 = Frame(root, borderwidth=2, relief='ridge')
frame11 = Frame(root, borderwidth=2, relief='ridge')
frame12 = Frame(root, borderwidth=2, relief='ridge')

frame10.grid(column=0, row=10, sticky="nsew")
frame11.grid(column=1, row=10, sticky="nsew")
frame12.grid(column=2, row=10, columnspan=7, sticky="nsew")

labelText = StringVar()
labelText.set("Press Start to begin")
label1 = Label(frame12, textvariable=labelText)
start_btn = Button(frame10, text="Start", command=check_inputs)
clear_btn = Button(frame11, text="Clear", command=clear)

#button2 = Button(frame3, text="Apply and close", command=root.destroy)

label1.pack(fill=X)
start_btn.pack(fill=X)
clear_btn.pack(fill='x')
#button2.pack(fill='x')
#print sudoku

root.mainloop()