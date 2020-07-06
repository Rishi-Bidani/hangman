import pygame
import pygame_textinput

pygame.font.init()

win_width = 700
win_height = 700

screen = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption("Client")

temp_given_word = ""
hang_img = 0

# colors
green = (0, 220, 0)
# ---------- end colors -----------

images = [
    pygame.image.load("hangman0.png"),
    pygame.image.load("hangman1.png"),
    pygame.image.load("hangman2.png"),
    pygame.image.load("hangman3.png"),
    pygame.image.load("hangman4.png"),
    pygame.image.load("hangman5.png"),
    pygame.image.load("hangman6.png"),
]

new_list = []
blits = []

pygame.time.set_timer(pygame.USEREVENT, 4000)


class Blanks:
    def __init__(self, length, win, word, color=(255, 255, 255), top=500):
        self.length = length
        self.win = win
        self.color = color
        self.top = top
        self.word = word

    # def draw(self):
    #     num = [(50, 500), (80, 500), (110, 500), (140, 500), (170, 500), (200, 500)]
    #     for i in range(self.length + 1):
    #         pygame.draw.rect(self.win, self.color, (num[i][0], num[i][1], 20, 20))

    def draw(self):
        global new_list
        lis = []
        for i in range(self.length):
            x = 50 + i * 30
            a = x
            lis.append(a)
            y = 500
            pygame.draw.rect(self.win, self.color, (x, y, 20, 20))
        new_list = lis

    def findOccurrences(self, char):
        return [i for i, letter in enumerate(self.word) if letter == f'{char}']

        # findOccurrences(yourString, '|')


class Button:
    def __init__(self, text, x, y, color, width=40, height=40, textSize=20):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.textSize = textSize

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", self.textSize)
        text = font.render(self.text, 1, (0, 0, 0))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


choose = [Button("Give Word", round(screen.get_width() / 2 - 100), 320, green, 190, 70, 40)]


# Button("Guess", 100, 320, green, 190, 70, 40),


def redrawWindow(win, btn):
    font = pygame.font.SysFont('comicsans', 30)
    large_font = pygame.font.SysFont('comicsans', 100)
    text_win = large_font.render("You Win!!", True, (0, 0, 220))
    text_lose = large_font.render("You Lose :(", True, (220, 0, 0))
    a = Blanks(len(temp_given_word), screen, temp_given_word)
    white = (255, 255, 255)
    grey = (128, 128, 128)
    win.fill(grey)
    for b in btn:
        b.draw(win)
    if hang_img <= 6:
        win.blit(images[hang_img], (20, 170))
    else:
        win.blit(images[-1], (20, 170))
    a.draw()
    for k in range(len(blits)):
        screen.blit(font.render(f'{blits[k][0]}', True, (0, 0, 0)), (new_list[blits[k][1]], 500))
    if len(blits) == len(temp_given_word):
        screen.blit(text_win, (screen.get_width() / 2 - text_win.get_width() / 2,
                               screen.get_height() / 2 - text_win.get_height() / 2))
    if hang_img >= 7:
        screen.blit(text_lose, (round(screen.get_width() / 2 - text_win.get_width() / 2),
                                round(screen.get_height() / 2 - text_win.get_height() / 2)))
    pygame.display.update()


btns = [
    Button("A", 10, 10, green),
    Button("B", 60, 10, green),
    Button("C", 110, 10, green),
    Button("D", 160, 10, green),
    Button("E", 210, 10, green),
    Button("F", 260, 10, green),
    Button("G", 310, 10, green),
    Button("H", 360, 10, green),
    Button("I", 410, 10, green),
    Button("J", 460, 10, green),
    Button("K", 510, 10, green),
    Button("L", 560, 10, green),
    Button("M", 610, 10, green),
    Button("N", 660, 10, green),  # ----------
    Button("O", 10, 60, green),
    Button("P", 60, 60, green),
    Button("Q", 110, 60, green),
    Button("R", 160, 60, green),
    Button("S", 210, 60, green),
    Button("T", 260, 60, green),
    Button("U", 310, 60, green),
    Button("V", 360, 60, green),
    Button("W", 410, 60, green),
    Button("X", 460, 60, green),
    Button("Y", 510, 60, green),
    Button("Z", 560, 60, green)
]

bttns = btns

letter_check = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def main(bns):
    run = True
    global letter_check
    global temp_given_word
    global blits
    global hang_img

    temp_given_word = temp_given_word.upper()
    a = Blanks(len(temp_given_word), screen, temp_given_word)
    while run:
        redrawWindow(screen, bns)
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.USEREVENT and hang_img >= 7:
                resetEverything()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for b in bns:
                    if b.click(mouse):
                        # print(new_list)
                        check = letter_check.index(b.text)
                        find = (a.findOccurrences(b.text))
                        # print(find)
                        if b.text not in temp_given_word:
                            hang_img += 1
                            # print(hang_img)
                        if str(a.findOccurrences(b.text)):
                            for j in find:
                                blits.append((b.text, j))
                            # print(blits)
                        else:
                            pass

                        bttns.pop(check)
                        letter_check.pop(check)
        pygame.display.update()


def give_word(bns):
    global temp_given_word
    textinput = pygame_textinput.TextInput()
    clock = pygame.time.Clock()

    while True:
        screen.fill((225, 225, 225))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        if textinput.update(events):
            word = textinput.get_text()
            temp_given_word = word
            main(bns)

        screen.blit(textinput.get_surface(), (10, 10))

        pygame.display.update()
        clock.tick(30)


def main_menu(win, chose, bns):
    run = True

    while run:
        mouse = pygame.mouse.get_pos()
        white = (255, 255, 255)
        screen.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in chose:
                    if i.click(mouse):
                        if i.text == "Give Word":
                            give_word(bns)

        for i in chose:
            i.draw(win)
        pygame.display.update()


def resetEverything():
    global temp_given_word
    global new_list
    global blits
    global hang_img
    global bttns
    global letter_check
    global btns

    hang_img = 0
    temp_given_word = ""
    new_list = []
    blits = []
    btns = [
        Button("A", 10, 10, green),
        Button("B", 60, 10, green),
        Button("C", 110, 10, green),
        Button("D", 160, 10, green),
        Button("E", 210, 10, green),
        Button("F", 260, 10, green),
        Button("G", 310, 10, green),
        Button("H", 360, 10, green),
        Button("I", 410, 10, green),
        Button("J", 460, 10, green),
        Button("K", 510, 10, green),
        Button("L", 560, 10, green),
        Button("M", 610, 10, green),
        Button("N", 660, 10, green),  # ----------
        Button("O", 10, 60, green),
        Button("P", 60, 60, green),
        Button("Q", 110, 60, green),
        Button("R", 160, 60, green),
        Button("S", 210, 60, green),
        Button("T", 260, 60, green),
        Button("U", 310, 60, green),
        Button("V", 360, 60, green),
        Button("W", 410, 60, green),
        Button("X", 460, 60, green),
        Button("Y", 510, 60, green),
        Button("Z", 560, 60, green),
    ]
    bttns = btns
    letter_check = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    main_menu(screen, choose, bttns)


main_menu(screen, choose, bttns)
