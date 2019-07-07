from kivy.app import App
from kivy.properties import OptionProperty, NumericProperty, ListProperty, \
        BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition, FallOutTransition

from kivy.lang import Builder
from kivy.clock import Clock
from math import cos, sin


import plateau as plt

Builder.load_string('''
<GamePlateau>:
    size_hint: None, None
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  # red
        Rectangle:
            pos: self.pos
            size: self.size
            
            
    
    BoxLayout:
        canvas.before:
            #Color:
            #   rgba: 0, 0, 1, 1  # blue
            Rectangle:
                pos: self.pos
                size: self.size

        size: self.parent.size  # important!
        pos: self.parent.pos  # important!
        orientation: 'vertical'
        GridLayout:
            cols: 3
            id: tic_buttons
            Button:
                id: btn0
                text: ''
                font_size: 100
                #background_normal: ''
                background_color: 0.31, 0.5, 0.69, 1.0
                background_disabled_normal: ''
                on_release: root.testButtons(self,0)
            Button:
                id: btn1
                text: ''
                font_size: 100
                background_disabled_normal: ''
                background_color: 0.31, 0.5, 0.69, 1.0
                on_release: root.testButtons(self,1)
                
            Button:
                id: btn2
                text: ''
                font_size: 100
                background_color: 0.31, 0.5, 0.69, 1.0
                background_disabled_normal: ''
                on_release: root.testButtons(self,2)
            Button:
                id: btn3
                text: ''
                font_size: 100
                background_color: 0.31, 0.5, 0.69, 1.0
                background_disabled_normal: ''
                on_release: root.testButtons(self,3)
            Button:
                id: btn4
                text: ''
                font_size: 100
                background_color: 0.31, 0.5, 0.69, 1.0
                background_disabled_normal: ''
                on_release: root.testButtons(self,4)
            Button:
                id: btn5
                text: ''
                font_size: 100
                background_color: 0.31, 0.5, 0.69, 1.0
                background_disabled_normal: ''
                on_release: root.testButtons(self,5)
                
            Button:
                id: btn6
                text: ''
                font_size: 100
                background_color: 0.31, 0.5, 0.69, 1.0
                background_disabled_normal: ''
                on_release: root.testButtons(self,6)
            Button:
                id: btn7
                text: ''
                font_size: 100
                background_color: 0.31, 0.5, 0.69, 1.0
                background_disabled_normal: ''
                on_release: root.testButtons(self,7)
            Button:
                id: btn8
                text: ''
                font_size: 100
                background_color: 0.31, 0.5, 0.69, 1.0
                background_disabled_normal: ''
                on_release: root.testButtons(self,8)

<GameScreen>:
    
    PageLayout:
        id: page_layout
        canvas.before:
            Color:
                rgba: 0.14, 0.14, 0.14, 1
            Rectangle:
                pos: self.pos
                size: self.size
        size: self.parent.size
        anchor_x: 'center'
        anchor_y: 'center'
        GamePlateau:
            id: game_plateau
            size: 400, 300
        GridLayout:
            canvas.before:
                Color:
                    rgba: 0.14, 0.14, 0.14, 0.97
                Rectangle:
                    pos: self.pos
                    size: self.size
            rows: 2
            size: self.parent.size  # important!
            pos: self.parent.pos  # important!
            GridLayout:
                cols:2
                Button:
                    text: 'Recommencer'
                    size_hint: 1,None
                    on_release: root.resetGame()
                Button:
                    text: 'Revenir au menu'
                    size_hint: 1,None
                    on_release: root.manager.current='menu'
            GridLayout:
                rows: 3
                GridLayout:
                    cols: 2
                    Label:
                        id: gagne_label1
                        text: 'Partie gagnés par : '
                    Label:
                        id: gagne_val1
                        text: ''
                GridLayout:
                    cols: 2
                    Label:
                        id: gagne_label2
                        text: 'Partie gagnés par : '
                    Label:
                        id: gagne_val2
                        text: ''
                GridLayout:
                    cols: 2
                    Label:
                        id: gagne_label3
                        text: 'Partie nulles : '
                    Label:
                        id: gagne_val3
                        text: ''
<GameMenu>:
    canvas.before:
        Color:
            rgba: 0.14, 0.14, 0.14, 1
        Rectangle:
            pos: self.pos
            size: self.size
    GridLayout:
        cols: 2
        height: 44 * 5
        GridLayout:
            id: parent_layout
            cols: 2

            Label:
                text: 'Mode de jeu (contre)'
            GridLayout:
                cols: 4
                Label:
                    text: 'Ordinateur'
                CheckBox:
                    allow_no_selection: False
                    group: 'gamemode' 
                    active: True
                    on_state: root.AiActivated = True; root.stateChange();root.toogleAiInput(False)
                Label:
                    text: 'Joueur'
                CheckBox:
                    allow_no_selection: False
                    group: 'gamemode'
                    on_state: root.AiActivated = False; root.stateChange();root.toogleAiInput(True)
            
            Label:
                text: 'Pion joueur 1'
            GridLayout:
                cols: 4
                Label:
                    text: 'X'
                CheckBox:
                    allow_no_selection: False
                    group: 'pion' 
                    active: True
                    on_state: root.pion = 'X'
                Label:
                    text: 'O'
                CheckBox:
                    allow_no_selection: False
                    group: 'pion'
                    on_state: root.pion = 'O'
            
            Label:
                id: player_label
                text: 'Player Name'
            TextInput:
                id: player_input0
                text: 'Joueur'
                multiline: False
            Label:
                id: player_label
                text: 'Player 2 Name'
                disabled: True
            TextInput:
                id: player_input
                text: 'Colosse'
                multiline: False
                disabled: True
            Label:
                id: diff_label
                text: 'Difficulte'
            GridLayout:
                id: diff_layout
                cols: 4
                Label:
                    text: 'Normale'
                CheckBox:
                    allow_no_selection: False
                    group: 'difficulty' 
                    active: True
                    on_state: root.AiDifficult = False; root.stateChange()
                Label:
                    text: 'Imbattable'
                CheckBox:
                    allow_no_selection: False
                    group: 'difficulty'
                    on_state: root.AiDifficult = True; root.stateChange()

        AnchorLayout:
            GridLayout:
                cols: 1
                size_hint: None, None
                size: self.minimum_size
                ToggleButton:
                    size_hint: None, None
                    size: 100, 44
                    text: 'Jouer'
                    on_state: root.manager.current = 'game'
                Button:
                    size_hint: None, None
                    size: 100, 44
                    text: 'Quitter'
                    on_press: quit()
                    
<CustomPopUp@Popup>
    auto_dismiss: True
    size_hint: None,None
    size: 150,150
    on_dismiss: root.getOut();
    GridLayout:
        rows: 2 
        Label:
            id: who_won
            text: 'ABC Won'
        Button:
            text: 'Recommencer'
            on_release: root.resetGame();root.dismiss();
    
''')

class CustomPopUp(Popup):
    uiScreen = None
    restarted = False
    def resetGame(self):
        if(self.uiScreen!= None):
            self.uiScreen.resetGame()
            self.restarted = True
    def getOut(self):
        if(self.restarted==False):
            self.uiScreen.ids.page_layout.page = 1
        return False
    pass


class GamePlateau(Widget):
    AiActivated = True
    AiDifficult = False
    pion = 'X'
    gagne1 = 0
    gagne2 = 0
    nulles = 0
    Namep1 = ''
    Namep2 = ''
    currentPion ='X'
    plateau = None
    labelInterface = None
    def alternatePion(self):
        self.currentPion = 'O' if self.currentPion=='X' else 'X'
    def testButtons(self,button,num):
        print(str(button)+" "+str(num))
        self.playButton(button)
        case = plt.conversion_plateau_index[num]
        self.plateau.selectionner_case(case[0],case[1],self.currentPion)
        if self.plateau.est_gagnant(self.currentPion):
            if self.isPlayer1():
                self.player1Win()
                return
            else:
                self.player2Win()
                return
        if not self.plateau.non_plein():
            self.draw()
            return
        self.alternatePion()

        if self.AiActivated:
            case = self.plateau.choisir_prochaine_case(self.currentPion)
            self.plateau.selectionner_case(case[0], case[1], self.currentPion)
            case = plt.conversion_plateau_index2[case]
            self.playButton(self.ids['btn'+str(case)])

            if self.plateau.est_gagnant(self.currentPion):
                self.player2Win()
                return
            if not self.plateau.non_plein():
                self.draw()
                return

            self.alternatePion()
        else:
            return
    def isPlayer1(self):
        return self.currentPion == self.pion
    def player1Win(self):
        self.blockBtns()
        self.gagne1+=1
        self.updateScores()
        popup = CustomPopUp()
        popup.uiScreen = self.labelInterface
        popup.title = 'Vainqueur'
        popup.ids.who_won.text = str(self.Namep1) + ' a gagné'
        popup.open()
    def player2Win(self):
        self.blockBtns()
        self.gagne2 += 1
        self.updateScores()
        popup = CustomPopUp()
        popup.uiScreen = self.labelInterface
        popup.title = 'Vainqueur'
        popup.ids.who_won.text = str(self.Namep2) + ' a gagné'
        popup.open()
    def draw(self):
        self.blockBtns()
        self.nulles +=1
        self.updateScores()
        popup = CustomPopUp()
        popup.uiScreen = self.labelInterface
        popup.title = 'Partie Nulle'
        popup.ids.who_won.text = 'Partie nulle'
        popup.open()
    def blockBtns(self):
        btnStr = 'btn'
        for i in range(0,9):
            btn = self.ids[btnStr+str(i)]
            btn.disabled = True
    def updateScores(self):
        if(self.labelInterface!=None):
            self.labelInterface.updateScore()
            #self.labelInterface.ids.page_layout.page = 1


    def playButton(self,button):
        if self.currentPion=='O':
            self.oButton(button)
        else:
            self.xButton(button)
    def xButton(self,button):
        button.disabled= True
        button.text = 'X'
        button.background_color = ((0.6, 1, 0.4, 1))
    def oButton(self,button):
        button.disabled= True
        button.text = 'O'
        button.background_color = ((0.69,0.31,0.31,1))

class GameMenu(Screen):
    AiActivated = True
    AiDifficult = False
    pion = 'X'
    def toogleAiInput(self,state):
        self.ids.diff_layout.disabled = state
        self.ids.player_input.text = "Colosse"
        self.ids.player_label.disabled = not state
        self.ids.player_input.disabled = not state

    def stateChange(self):
        print('Ai activation : ' + str(self.AiActivated))
        print('Ai difficult : ' + str(self.AiDifficult))
        print('Pion: ' + str(self.pion))
    def toogleAI(self):
        self.AiActivated = True if not self.AiActivated else False
        print('Ai activation : '+str(self.AiActivated))
    def toogleAIDifficulty(self):
        self.AiDifficult = True if not self.AiDifficult else False
        print('Ai difficult : '+str(self.AiDifficult))

    def launchGame(self):
        pass

class GameScreen(Screen):
    AiActivated = True
    AiDifficult = False
    pion = 'X'

    def on_pre_enter(self, *args):
        plat = self.ids['game_plateau']
        menu = self.manager.get_screen('menu')
        plat.AiActivated = menu.AiActivated
        plat.AiDifficult = menu.AiDifficult
        plat.pion = menu.pion
        plat.currentPion = menu.pion

        plat.Namep1 = menu.ids.player_input0.text
        plat.Namep2 = menu.ids.player_input.text
        plat.gagne1 = 0
        plat.gagne2 = 0
        plat.gagne3 = 0
        if plat.Namep1=='':
            plat.Namep1 = 'Joueur1'
        if plat.Namep2=='':
            plat.Namep2 = 'Joueur2'
        print('Game Initialization')
        print('Ai activation : ' + str(plat.AiActivated))
        print('Ai difficult : ' + str(plat.AiDifficult))
        print('Pion: ' + str(plat.pion))
        aa = 'Partie gagnés par '
        self.ids.gagne_label1.text = aa+str(plat.Namep1)+' :'
        self.ids.gagne_label2.text = aa + str(plat.Namep2) + ' :'
        self.resetGame()
        plat.labelInterface = self

    def resetGame(self):
        btnStr = 'btn'
        test = self.ids.game_plateau
        for i in range(0,9):
            btn = test.ids[btnStr+str(i)]
            btn.disabled=False
            btn.text = ''
            btn.background_color  = 0.31, 0.5, 0.69, 1.0

        plat = self.ids['game_plateau']
        plat.plateau = plt.Plateau()
        plat.plateau.difficulte = 2 if plat.AiDifficult else 1

        menu = self.manager.get_screen('menu')
        plat.pion = menu.pion
        plat.currentPion = menu.pion

        self.updateScore()
        self.ids.page_layout.page = 0

    def updateScore(self):
        plat = self.ids['game_plateau']
        aa = 'Partie gagnés par '
        self.ids.gagne_val1.text = str(plat.gagne1)
        self.ids.gagne_val2.text = str(plat.gagne2)
        self.ids.gagne_val3.text = str(plat.nulles)


screen_manager = ScreenManager(transition=FallOutTransition())
screen_manager.add_widget(GameMenu(name='menu'))
screen_manager.add_widget(GameScreen(name='game'))




class TicTacGame(App):
    def build(self):
        return screen_manager


if __name__ == '__main__':
    TicTacGame().run()