from curses import initscr,curs_set,init_pair,color_pair,start_color,A_STANDOUT,newwin,endwin,KEY_RIGHT,KEY_LEFT,KEY_DOWN,KEY_UP,COLOR_GREEN,COLOR_RED,COLOR_BLACK,COLOR_YELLOW
from random import randrange
initscr()
start_color()
curs_set(0)
init_pair(1, COLOR_GREEN, COLOR_BLACK)
init_pair(2, COLOR_RED, COLOR_BLACK)
init_pair(3, COLOR_YELLOW, COLOR_BLACK)
win = newwin(16,60,0,0)
win.keypad(1)
win.nodelay(1)
win.border('|','|','-','-','+','+','+','+')
win.addch(4,44,'$',color_pair(1))
snake = [ [30,7],[29,8],[28,7],[27,7],[26,7],[25,7] ]
key = KEY_RIGHT
while key != 27:
    win.addstr(0,2,' Amount: $'+str((len(snake)-6)*10)+' ', color_pair(3))
    win.addstr(0,20, ' First Hand Foundation ', A_STANDOUT)
    win.addstr(15,22, '20 Year Anniversary', A_STANDOUT)
    win.timeout(180+ ( (len(snake)-6) % 10- (len(snake)-6) ) * 3 )
    getkey = win.getch()
    key = key if getkey==-1 else getkey
    snake.insert(0,[snake[0][0]+(key==KEY_RIGHT and 1 or key==KEY_LEFT and -1), snake[0][1]+(key==KEY_DOWN and 1 or key==KEY_UP and -1)])
    win.addch(snake[len(snake)-1][1],snake[len(snake)-1][0],' ')
    if win.inch(snake[0][1],snake[0][0]) & 255 == 32: snake.pop()
    elif win.inch(snake[0][1],snake[0][0]) & 255 == ord('$'):  
        c = [n for n in [[randrange(1,58,1),randrange(1,14,1)] for x in range(len(snake))] if n not in snake]
        win.addch(c == [] and 4 or c[0][1],c == [] and 44 or c[0][0],'$',color_pair(1))
    else: break
    win.addch(snake[0][1],snake[0][0],'O',color_pair(2))
endwin()
print 'Your donation amount: '+str((len(snake)-7)*10)+' dollars\n'
