import pygame
import pygame_gui

import tkinter as tk
from tkinter import simpledialog
import mbox
import math

from shapely.geometry import Point, Polygon

class Gui():

    def drawRegularPolygon(self, surface, color, numSides, tiltAngle, x, y, radius):

        pts = []

        for i in range(numSides):

            x = x + radius * math.cos(tiltAngle + math.pi * 2 * i / numSides)
            y = y + radius * math.sin(tiltAngle + math.pi * 2 * i / numSides)

            pts.append([int(x), int(y)])

        pygame.draw.polygon(surface, color, pts)

    #--------------------------------------------

    def isInsideOfPolygon(self, x, y, x2, y2, radius):

        tiltAngle = math.pi / 2
        shift = 5
        numSides = 6
        p = Point(x, y)

        coords = []

        for i in range(numSides):

            newX = x2 + radius * 2 / 3 * math.cos(tiltAngle + math.pi * 2 * i / numSides)
            newY = y2 + radius * 2 / 3 * math.sin(tiltAngle + math.pi * 2 * i / numSides)

            newX -= shift

            coords.append((newX, newY))

        poly = Polygon(coords)

        return p.within(poly)

    #--------------------------------------------

    def wrapText(self, surface, text, color, rect, font, margin):

        isWrapped = False

        rect = pygame.Rect(rect)
        top = rect.top

        fontHeight = font.size("Tg")[1]

        while text:

            i = 1

            if top + fontHeight > rect.bottom:
                break

            while font.size(text[:i])[0] < rect.width and i < len(text):

                i += 1

            if i < len(text):

                isWrapped = True
                i = text.rfind(" ", 0, i) + 1

            line = font.render(text[:i], True, color)

            surface.blit(line, (rect.left, top))

            top += fontHeight + margin / 4

            text = text[i:]

        return isWrapped

    #--------------------------------------------

    def __init__(self):

        #------ KOLORY

        self.__WHITE = (255, 255, 255)

        self.__ORANGE = (255, 128, 0) #Antylopa

        self.__RED = (204, 0, 0) #Barszcz

        self.__PINK = (255, 204, 204) #Czlowiek

        self.__GRAY = (96, 96, 96) #Guarana

        self.__VIOLET = (153, 51, 255) #Jagody

        self.__BLUE = (0, 0, 204) #Lis

        self.__YELLOW = (255, 255, 51) #Mlecz

        self.__WEIRD_BLUE = (0, 102, 102) #Owca

        self.__GREEN = (0, 204, 0) #Trawa

        self.__BROWN = (102, 51, 0) #Wilk

        self.__CYAN = (51, 255, 255) #Zolw #light blue...

        self.__LIGHT_GRAY = (224, 224, 224) #Cyberowca

        self.__BLACK = (0, 0, 0)

    #--------------------------------------------

    def startDialogue(self):

        pygame.init()

        pygame.display.set_caption("Początek gry")

        FPS = 60

        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        MARGIN = 50

        ACCEPT_WIDTH = 200
        INPUT_WIDTH = 100
        TYP_PLANSZY_WIDTH = 200

        TYP_PLANSZY_HEIGHT = 46

        FONT_S_SIZE = 20 / 8 * 5
        FONT_SIZE = 20 * 6 / 5

        ELEMENTS_HEIGHT = 30
        TITLE_OFF_SET = 80
        
        TEXTMARGIN_X = 2
        TEXTMARGIN_Y = 15

        window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

        manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

        accept = pygame_gui.elements.UIButton(
            
            relative_rect=pygame.Rect(SCREEN_WIDTH/2 - ACCEPT_WIDTH/2, SCREEN_HEIGHT/5 + 3 * MARGIN + TYP_PLANSZY_HEIGHT / 2, ACCEPT_WIDTH, ELEMENTS_HEIGHT),
            text="Zacznij grę!",
            manager=manager
            
            )

        xInput = pygame_gui.elements.UITextEntryLine(
            
            relative_rect=pygame.Rect(SCREEN_WIDTH/2 - INPUT_WIDTH/2, SCREEN_HEIGHT/5, INPUT_WIDTH, ELEMENTS_HEIGHT),
            manager=manager
            
            )

        xInput.set_allowed_characters(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])

        yInput = pygame_gui.elements.UITextEntryLine(
            
            relative_rect=pygame.Rect(SCREEN_WIDTH/2 - INPUT_WIDTH/2, SCREEN_HEIGHT/5 +  MARGIN, INPUT_WIDTH, ELEMENTS_HEIGHT),
            manager=manager
            
            )

        yInput.set_allowed_characters(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])

        typPlanszy = pygame_gui.elements.UISelectionList(
            
            relative_rect = pygame.Rect(SCREEN_WIDTH/2 - TYP_PLANSZY_WIDTH/2, SCREEN_HEIGHT/5 + 2 * MARGIN, TYP_PLANSZY_WIDTH, TYP_PLANSZY_HEIGHT),
            item_list = ["Plansza prostokątna", "Plansza hexowa"],
            manager=manager,
            default_selection = "Plansza prostokątna"

            )

        font = pygame.font.Font('Lato.ttf', int(FONT_SIZE))
        fontS = pygame.font.Font('Lato.ttf', int(FONT_S_SIZE))

        title = font.render("Dostosuj planszę", True, self.__WHITE)

        xText = fontS.render("Rozmiar X", True, self.__WHITE)

        yText = fontS.render("Rozmiar Y", True, self.__WHITE)

        isRunning = True
        clock = pygame.time.Clock()

        wybor = 0
        x = 0
        y = 0

        while isRunning:

            time_delta = clock.tick(FPS)/1000.0
            window_surface.blit(background, (0, 0))

            window_surface.blit(title, (SCREEN_WIDTH/2 - INPUT_WIDTH/2 - TITLE_OFF_SET/2, SCREEN_HEIGHT/10))

            window_surface.blit(xText, (SCREEN_WIDTH/2 - INPUT_WIDTH/2 + TEXTMARGIN_X, SCREEN_HEIGHT/5 - TEXTMARGIN_Y))
            window_surface.blit(yText, (SCREEN_WIDTH/2 - INPUT_WIDTH/2 + TEXTMARGIN_X, SCREEN_HEIGHT/5 + MARGIN - TEXTMARGIN_Y))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    isRunning = False

                if event.type == pygame.USEREVENT:

                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                        if event.ui_element == accept:

                            isRunning = False

                if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:

                    if event.text != '':

                        if event.ui_element == xInput:

                            x = int (event.text)

                        if event.ui_element == yInput:

                            y = int (event.text)

                if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:

                    if event.ui_element == typPlanszy:

                        wybor = 0 if event.text == "Plansza prostokątna" else 1

                manager.process_events(event)

            manager.update(time_delta)

            manager.draw_ui(window_surface)

            pygame.display.update()

        return [wybor, x, y]
    
    #--------------------------------------------

    def pickColor(self, char):

        if char == 'A':
            return self.__ORANGE

        if char == 'B':
            return self.__RED

        if char == 'C':
            return self.__PINK

        if char == 'G':
            return self.__GRAY

        if char == 'J':
            return self.__VIOLET

        if char == 'L':
            return self.__BLUE

        if char == 'M':
            return self.__YELLOW

        if char == 'O':
            return self.__WEIRD_BLUE

        if char == 'T':
            return self.__GREEN

        if char == 'W':
            return self.__BROWN

        if char == 'Z':
            return self.__CYAN

        if char == 'o':
            return self.__LIGHT_GRAY

        return (0, 0, 0)

    #--------------------------------------------

    def setUpGui(self, flag, czyCzlowiekIstnieje, swiat, organizmy, plansza):

        FPS = 60

        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600

        BOARD_HEIGHT = 400
        BOARD_WIDTH = SCREEN_WIDTH/2

        BUTTON_MARGIN = 10
        BUTTON_AREA_HEIGHT = SCREEN_HEIGHT - BOARD_HEIGHT
        BUTTON_AREA_WIDTH = SCREEN_WIDTH/2

        BUTTON_UP_ROW_N = 4
        BUTTON_UP_HEIGHT = 30

        BUTTON_UP_WIDTH = (BUTTON_AREA_WIDTH - (BUTTON_UP_ROW_N + 1) * BUTTON_MARGIN)/BUTTON_UP_ROW_N

        OBECNA_TURA_FONT_SIZE = 20

        EVENTS_PAGE_SIZE = 8
        starting_page_index = 0
        starting_page = 1

        TITLE_HEIGHT = 20

        MARGIN_LEGEND = 20

        HEIGHT_OF_ROW = ((BUTTON_AREA_HEIGHT - TITLE_HEIGHT) / 4) - MARGIN_LEGEND

        POSITION_Y_ROW =  SCREEN_HEIGHT - (BUTTON_AREA_HEIGHT * (3/4)) + TITLE_HEIGHT 

        MARGIN_LEGEND = 20

        WIDTH_DISTRIBUTE = BOARD_WIDTH - 2 * MARGIN_LEGEND

        WIDTH_OF_TILE = (WIDTH_DISTRIBUTE / 4) / 4

        WIDTH_OF_TEXT = ( (WIDTH_DISTRIBUTE / 4) * 3) / 4

        TITLE_HEIGHT = 20

        HEIGHT_OF_ROW = ((BUTTON_AREA_HEIGHT - TITLE_HEIGHT) / 4) - MARGIN_LEGEND

        POSITION_Y_ROW =  SCREEN_HEIGHT - (BUTTON_AREA_HEIGHT * (3/4)) + TITLE_HEIGHT 

        TEXT_SPACE_X = 25
        TEXT_SPACE_Y = 5
        TITLE_MARGIN = 120

        LOG_SPACE_Y = 20
        DZIENNIK_MARGIN = 125

        pygame.init()
        
        pygame.display.set_caption("Wirtualny Świat")

        font = pygame.font.Font('Lato.ttf', OBECNA_TURA_FONT_SIZE)
        fontS = pygame.font.Font('Lato.ttf', int(OBECNA_TURA_FONT_SIZE/6 * 5))
        fontSS = pygame.font.Font('Lato.ttf', int(OBECNA_TURA_FONT_SIZE/8 * 5))

        window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

        manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
      
        #------ TWORZENIE PLANSZY

        BOARD_MARGIN = 20
        BOARD_MARGIN_HEX = 60

        REAL_BOARD_HEIGHT = BOARD_HEIGHT - 2 * BOARD_MARGIN
        REAL_BOARD_WIDTH = BOARD_WIDTH - 2 * BOARD_MARGIN

        TILE_HEIGHT = int ( REAL_BOARD_HEIGHT / swiat.getRozmiarY() )
        TILE_WIDTH = int ( REAL_BOARD_WIDTH / swiat.getRozmiarX() )

        TILE_WIDTH_HEX = ( TILE_WIDTH / 3 ) * 2

        #------ TEKSTY

        obecnaTura = font.render("Obecna tura: " + str(swiat.getObecnaTura()), True, self.__WHITE)

        czlowiekNieZyje = font.render("Czlowiek nie żyje!", True, self.__WHITE)

        podajKierunek = fontS.render("Wybierz kierunek ruchu człowieka", True, self.__WHITE)

        dziennik = fontS.render("Dziennik zdarzeń", True, self.__WHITE)

        tarcza = ""

        if czyCzlowiekIstnieje[0]:
            tarcza = swiat.findOrganizmByChar('C', organizmy).podajInfoTarcza(swiat.getTuraUmiejetnosc())

        tarczaRender = fontS.render(tarcza, True, self.__WHITE)

        if "Tarcza musi się odnowić!" in tarcza:
            
            tarczaRender = fontSS.render(tarcza, True, self.__WHITE)

        kierunek = 0

        kierunekTxt = ""

        if czyCzlowiekIstnieje[0]:
            kierunek = swiat.findOrganizmByChar('C', organizmy).getKierunekRuchu()

            if kierunek == 1: kierunekTxt = "Górę"
            if kierunek == 2: kierunekTxt = "Dół"
            if kierunek == 3: kierunekTxt = "Lewo"
            if kierunek == 4: kierunekTxt = "Prawo"

        ruchCzlowieka = fontS.render("Czlowiek będzie poruszał się w: " + kierunekTxt, True, self.__WHITE)

        #------ PRZYCISKI

        nastTura = pygame_gui.elements.UIButton(

            relative_rect = pygame.Rect(BUTTON_MARGIN, BOARD_HEIGHT + BUTTON_MARGIN, BUTTON_UP_WIDTH , BUTTON_UP_HEIGHT),
            text = 'Zacznij',
            manager = manager

            )

        wyjscie = pygame_gui.elements.UIButton(

            relative_rect = pygame.Rect(2 * BUTTON_MARGIN + BUTTON_UP_WIDTH, BOARD_HEIGHT + BUTTON_MARGIN, BUTTON_UP_WIDTH, BUTTON_UP_HEIGHT),
            text = 'Wyjście',
            manager = manager

            )

        zaladuj = pygame_gui.elements.UIButton(

            relative_rect = pygame.Rect(3 * BUTTON_MARGIN + 2 * BUTTON_UP_WIDTH, BOARD_HEIGHT + BUTTON_MARGIN, BUTTON_UP_WIDTH, BUTTON_UP_HEIGHT),
            text = 'Załaduj',
            manager = manager

            )

        zapisz = pygame_gui.elements.UIButton(

            relative_rect = pygame.Rect(4 * BUTTON_MARGIN + 3 * BUTTON_UP_WIDTH, BOARD_HEIGHT + BUTTON_MARGIN, BUTTON_UP_WIDTH, BUTTON_UP_HEIGHT),
            text = 'Zapisz',
            manager = manager

            )

        gora = pygame_gui.elements.UIButton(

            relative_rect = pygame.Rect(4 * BUTTON_MARGIN + 3 * BUTTON_UP_WIDTH, BOARD_HEIGHT + BUTTON_MARGIN * 3 + BUTTON_UP_HEIGHT, BUTTON_UP_WIDTH, BUTTON_UP_HEIGHT),
            text = 'W górę',
            manager = manager

            )

        dol = pygame_gui.elements.UIButton(

            relative_rect = pygame.Rect(4 * BUTTON_MARGIN + 3 * BUTTON_UP_WIDTH, BOARD_HEIGHT + BUTTON_MARGIN * 3 + BUTTON_UP_HEIGHT * 2, BUTTON_UP_WIDTH, BUTTON_UP_HEIGHT),
            text = 'W dół',
            manager = manager

            )

        lewo = pygame_gui.elements.UIButton(

            relative_rect = pygame.Rect(4 * BUTTON_MARGIN + 3 * BUTTON_UP_WIDTH, BOARD_HEIGHT + BUTTON_MARGIN * 3  + BUTTON_UP_HEIGHT * 3, BUTTON_UP_WIDTH, BUTTON_UP_HEIGHT),
            text = 'W lewo',
            manager = manager

            )

        prawo = pygame_gui.elements.UIButton(

            relative_rect = pygame.Rect(4 * BUTTON_MARGIN + 3 * BUTTON_UP_WIDTH, BOARD_HEIGHT + BUTTON_MARGIN * 3 + BUTTON_UP_HEIGHT * 4, BUTTON_UP_WIDTH, BUTTON_UP_HEIGHT),
            text = 'W prawo',
            manager = manager

            )

        next = pygame_gui.elements.UIButton(

            relative_rect = pygame.Rect(BOARD_WIDTH + BUTTON_MARGIN, POSITION_Y_ROW - HEIGHT_OF_ROW - BOARD_MARGIN - BUTTON_UP_HEIGHT, BUTTON_UP_WIDTH, BUTTON_UP_HEIGHT),
            text = '->',
            manager = manager

            )

        prev = pygame_gui.elements.UIButton(

            relative_rect = pygame.Rect(BOARD_WIDTH + 2 * BUTTON_MARGIN + BUTTON_UP_WIDTH, POSITION_Y_ROW - HEIGHT_OF_ROW - BOARD_MARGIN - BUTTON_UP_HEIGHT, BUTTON_UP_WIDTH, BUTTON_UP_HEIGHT),
            text = '<-',
            manager = manager

            )

        tarczaAktywuj = pygame_gui.elements.UIButton(

            relative_rect = pygame.Rect(BUTTON_MARGIN, BOARD_HEIGHT + BUTTON_MARGIN + 7 * OBECNA_TURA_FONT_SIZE, 0 , 0),
            text = 'Aktywuj tarczę',
            manager = manager

            )

        if tarcza == "Można aktywować tarczę!":
            
            tarczaAktywuj = pygame_gui.elements.UIButton(

                relative_rect = pygame.Rect(BUTTON_MARGIN, BOARD_HEIGHT + BUTTON_MARGIN + 7 * OBECNA_TURA_FONT_SIZE, BUTTON_UP_WIDTH , BUTTON_UP_HEIGHT),
                text = 'Aktywuj tarczę',
                manager = manager

                )
      
        isButtonClicked = False
        clock = pygame.time.Clock()
        ch = ""

        x = y = 0

        highlightText = ''

        countEndL = 0

        while not isButtonClicked:

            time_delta = clock.tick(FPS)/1000.0
            window_surface.blit(background, (0, 0))

            if swiat.getIsHex() == False:

                for i in range(0, swiat.getRozmiarY()):

                    for j in range(0, swiat.getRozmiarX()):

                        pygame.draw.rect(window_surface, self.pickColor(plansza[i][j]), (BOARD_MARGIN + j * TILE_WIDTH, BOARD_MARGIN + i * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT) )

            else:

                for i in range(0, swiat.getRozmiarY()):

                    for j in range(0, swiat.getRozmiarX()):

                        self.drawRegularPolygon(window_surface, self.pickColor(plansza[i][j]), 6, math.pi / 2, BOARD_MARGIN_HEX + j * TILE_WIDTH_HEX + TILE_WIDTH_HEX/2 * i, BOARD_MARGIN_HEX * 4 / 3 + i * TILE_WIDTH_HEX, TILE_WIDTH_HEX/2) 

            listOfChars = [['A', 'B', 'C', 'G'], ['J', 'L', 'M', 'O'], ['T', 'W', 'Z', 'o']]
            listOfNames = [['Antylopa', 'Barszcz', 'Czlowiek', 'Guarana'], ['Jagody', 'Lis', 'Mlecz', 'Owca'], ['Trawa', 'Wilk', 'Zolw', 'Cyberowca']]

            legendCoordinates = []

            legendaTitle = fontS.render("Legenda organizmów", True, self.__WHITE)
            window_surface.blit(legendaTitle, (BOARD_WIDTH + TITLE_MARGIN, POSITION_Y_ROW - HEIGHT_OF_ROW - TEXT_SPACE_Y))

            for i in range(0, 3):

                for j in range(0, 4):

                    pygame.draw.rect(window_surface, self.pickColor(listOfChars[i][j]), (BOARD_WIDTH + BOARD_MARGIN + j * (WIDTH_OF_TILE + WIDTH_OF_TEXT), POSITION_Y_ROW + i * HEIGHT_OF_ROW + MARGIN_LEGEND * i, WIDTH_OF_TILE, HEIGHT_OF_ROW) )

                    znak = listOfChars[i][j]

                    znakTxt = fontSS.render(znak, True, self.__BLACK)

                    window_surface.blit(znakTxt, (BOARD_WIDTH + BOARD_MARGIN + j * (WIDTH_OF_TILE + WIDTH_OF_TEXT) + WIDTH_OF_TILE / (3 if znak != 'M' and znak != 'W' else 4), POSITION_Y_ROW + i * HEIGHT_OF_ROW + MARGIN_LEGEND * i + HEIGHT_OF_ROW / 5))

                    legendCoordinates.append([BOARD_WIDTH + BOARD_MARGIN + j * (WIDTH_OF_TILE + WIDTH_OF_TEXT), POSITION_Y_ROW + i * HEIGHT_OF_ROW + MARGIN_LEGEND * i, WIDTH_OF_TILE, HEIGHT_OF_ROW, WIDTH_OF_TILE, HEIGHT_OF_ROW])

                    if listOfChars[i][j] == highlightText:
                        nazwaOrganizmu = fontSS.render("- " + listOfNames[i][j], True, self.__RED)

                    else:
                        nazwaOrganizmu = fontSS.render("- " + listOfNames[i][j], True, self.__WHITE)

                    window_surface.blit(nazwaOrganizmu, (BOARD_WIDTH + BOARD_MARGIN + j * (WIDTH_OF_TILE + WIDTH_OF_TEXT) + TEXT_SPACE_X, POSITION_Y_ROW + i * HEIGHT_OF_ROW + MARGIN_LEGEND * i + TEXT_SPACE_Y))

            starting_page_index = (starting_page - 1) * (EVENTS_PAGE_SIZE)

            strona = fontS.render("Strona " + str(starting_page), True, self.__WHITE)
            window_surface.blit(strona, (BOARD_WIDTH + 3 * BUTTON_MARGIN + 2 * BUTTON_UP_WIDTH, POSITION_Y_ROW - 3 * HEIGHT_OF_ROW + TEXT_SPACE_Y))

            window_surface.blit(dziennik, (BOARD_WIDTH + DZIENNIK_MARGIN, TEXT_SPACE_Y * 3))
            j = 0

            pageIncrease = False

            countEndL = 0
            countWrapped = 0

            for i in range(starting_page_index, len(swiat.getLogOutOfEndl())):

                
               if not 'Kolejnosc' in swiat.getLogOutOfEndl()[i]:

                    wrap = self.wrapText(window_surface, swiat.getLogOutOfEndl()[i], self.__WHITE, (BOARD_WIDTH + TEXT_SPACE_X, LOG_SPACE_Y * (i + 3 + countWrapped - ( (EVENTS_PAGE_SIZE ) * (starting_page - 1) ) ), SCREEN_WIDTH - BOARD_WIDTH - 2*TEXT_SPACE_X, BOARD_HEIGHT - LOG_SPACE_Y * (i + 3 - ( (EVENTS_PAGE_SIZE ) * (starting_page - 1) ) )), fontSS, LOG_SPACE_Y)

                    if wrap: countWrapped += 1

                    j += 1
                    if j == EVENTS_PAGE_SIZE and not 'Kolejnosc' in swiat.getLogOutOfEndl()[i + 1 if i + 1 < len(swiat.getLogOutOfEndl()) else 0]:
                        pageIncrease = True
                        break

               else: break             


            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    flag[0] = False
                    isButtonClicked = True

                if event.type == pygame.MOUSEMOTION:

                    x, y = event.pos

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and x >= BOARD_MARGIN and x <= BOARD_WIDTH - BOARD_MARGIN and y >= BOARD_MARGIN and y <= BOARD_HEIGHT - BOARD_MARGIN:
                    
                    for i in range(0, swiat.getRozmiarY()):

                        for j in range(0, swiat.getRozmiarX()):

                            a = ( x >= BOARD_MARGIN + TILE_WIDTH * j and x <= BOARD_MARGIN + (TILE_WIDTH) * (j + 1) and y >= BOARD_MARGIN + TILE_HEIGHT * i and y <= BOARD_MARGIN + (TILE_HEIGHT) * (i + 1) )

                            if swiat.getIsHex():

                                a = self.isInsideOfPolygon(x, y, BOARD_MARGIN_HEX + j * TILE_WIDTH_HEX + TILE_WIDTH_HEX/2 * i, BOARD_MARGIN_HEX * 4 / 3 + i * TILE_WIDTH_HEX, TILE_WIDTH_HEX)

                            if a:

                                b = False

                                if swiat.findOrganizmByXY(j, i, organizmy) != organizmy[0]:
                                    
                                        if swiat.findOrganizmByXY(j, i, organizmy).getZnak() == 'C' and highlightText != 'C':

                                            czyCzlowiekIstnieje[0] = False
                                            swiat.changeTuraUmiejetnosc(-5)
                                            b = True
                              
                                if highlightText != '':

                                    swiat.addOrganizmByXY(j, i, organizmy, highlightText)

                                if highlightText == '':

                                    swiat.edytujPlansze(j, i, " ")
                                    swiat.deleteOrganizmByXY(j, i, organizmy)

                                if highlightText == 'C' and not czyCzlowiekIstnieje[0]:

                                    swiat.changeTuraUmiejetnosc(-5)
                                    czyCzlowiekIstnieje[0] = True
                                    return ''

                                if b: return ''


                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and x >= BOARD_WIDTH + MARGIN_LEGEND and x <= SCREEN_WIDTH - MARGIN_LEGEND and y >= POSITION_Y_ROW and y <= SCREEN_HEIGHT - MARGIN_LEGEND:

                    for i in range(0, len(legendCoordinates)):

                        if x >= legendCoordinates[i][0] and x <= legendCoordinates[i][0] + legendCoordinates[i][2] and y >= legendCoordinates[i][1] and y <= legendCoordinates[i][1] + legendCoordinates[i][3]:

                            highlightText = listOfChars[int(i/4)][i % 4]
               

                if event.type == pygame.USEREVENT:

                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                        changeButtonClicked = True

                        if event.ui_element == nastTura:

                            ch = 'T'            

                        if event.ui_element == wyjscie:

                            ch = 'E'

                        if event.ui_element == zaladuj:

                            ch = 'L'            

                        if event.ui_element == zapisz:

                            ch = 'Z'

                        if event.ui_element == gora:

                            ch = "UP"           

                        if event.ui_element == dol:

                            ch = "DOWN"

                        if event.ui_element == lewo:

                            ch = "LEFT"        

                        if event.ui_element == prawo:

                            ch = "RIGHT"

                        if event.ui_element == tarczaAktywuj:

                            ch = 'U'

                        if event.ui_element == next:

                            if pageIncrease:

                                starting_page += 1

                            changeButtonClicked = False


                        if event.ui_element == prev:

                            if starting_page != 1:

                                starting_page -= 1

                            changeButtonClicked = False

                        if changeButtonClicked:
                            
                            isButtonClicked = True


                if event.type == pygame.KEYDOWN:

                    isButtonClicked = True

                    if event.key == pygame.K_UP:

                        ch = "UP"

                    if event.key == pygame.K_LEFT:

                        ch = "LEFT"

                    if event.key == pygame.K_RIGHT:

                        ch = "RIGHT"

                    if event.key == pygame.K_UP:

                        ch = "UP"

                    if event.key == pygame.K_DOWN:

                        ch = "DOWN"
                        

                manager.process_events(event)


            manager.update(time_delta)
            manager.draw_ui(window_surface)

            window_surface.blit(obecnaTura, (BUTTON_MARGIN, BOARD_HEIGHT + 2 * BUTTON_MARGIN + BUTTON_UP_HEIGHT))

            if not czyCzlowiekIstnieje[0]:

                window_surface.blit(czlowiekNieZyje, (BUTTON_MARGIN, BOARD_HEIGHT + 2 * BUTTON_MARGIN + BUTTON_UP_HEIGHT + OBECNA_TURA_FONT_SIZE * 2))

            else:

                if kierunek == 0:
                    window_surface.blit(podajKierunek, (BUTTON_MARGIN, BOARD_HEIGHT + 2 * BUTTON_MARGIN + BUTTON_UP_HEIGHT + OBECNA_TURA_FONT_SIZE * 2))

                else:
                    window_surface.blit(ruchCzlowieka, (BUTTON_MARGIN, BOARD_HEIGHT + 2 * BUTTON_MARGIN + BUTTON_UP_HEIGHT + OBECNA_TURA_FONT_SIZE * 2))

                window_surface.blit(tarczaRender, (BUTTON_MARGIN, BOARD_HEIGHT + 2 * BUTTON_MARGIN + BUTTON_UP_HEIGHT + OBECNA_TURA_FONT_SIZE * 3))


            pygame.display.update()

        return ch