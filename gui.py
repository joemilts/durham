import wx
import wx.grid as gridlib
import numpy as np
import random as rn

bets = np.zeros(5)
########################################################################
class PanelOne(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(self)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        self.rb1 = wx.RadioBox(self, style = wx.RA_SPECIFY_COLS, label = "Game 1", pos = (5, 50), choices = ["3", "3", "3"])
        self.rb1.Bind(wx.EVT_RADIOBOX, self.onRadioBox1)
        my_sizer.Add(self.rb1, 0, wx.ALL | wx.CENTER, 5)

        self.rb2 = wx.RadioBox(self, style = wx.RA_SPECIFY_COLS, label = "Game 2", pos = (5, 50), choices = ["2", "4", "4"])
        self.rb2.Bind(wx.EVT_RADIOBOX, self.onRadioBox2)
        my_sizer.Add(self.rb2, 0, wx.ALL | wx.CENTER, 5)

        self.rb3 = wx.RadioBox(self, style = wx.RA_SPECIFY_COLS, label = "Game 3", pos = (5, 50), choices = ["10", "1", "1.11"])
        self.rb3.Bind(wx.EVT_RADIOBOX, self.onRadioBox3)
        my_sizer.Add(self.rb3, 0, wx.ALL | wx.CENTER, 5)

        self.rb4 = wx.RadioBox(self, style = wx.RA_SPECIFY_COLS, label = "Game 4", pos = (5, 50), choices = ["5", "2.5", "2.5"])
        self.rb4.Bind(wx.EVT_RADIOBOX, self.onRadioBox4)
        my_sizer.Add(self.rb4, 0, wx.ALL | wx.CENTER, 5)

        self.rb5 = wx.RadioBox(self, style = wx.RA_SPECIFY_COLS, label = "Game 5", pos = (5, 50), choices = ["2.5", "3.33", "3.33"])
        self.rb5.Bind(wx.EVT_RADIOBOX, self.onRadioBox5)
        my_sizer.Add(self.rb5, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(my_sizer)

        my_btn = wx.Button(self, label = 'Confirm Choices')
        my_btn.Bind(wx.EVT_BUTTON, parent.gtpage2)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)


    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything")
        else:
            print(f'You typed: "{value}"')

    def onRadioBox1(self,e):
        bets[0] = self.rb1.GetStringSelection()

    def onRadioBox2(self,e):
        bets[1] = self.rb2.GetStringSelection()

    def onRadioBox3(self,e):
        bets[2] = self.rb3.GetStringSelection()

    def onRadioBox4(self,e):
        bets[3] = self.rb4.GetStringSelection()

    def onRadioBox5(self,e):
        bets[4] = self.rb5.GetStringSelection()


########################################################################
class PanelTwo(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        grid = gridlib.Grid(self)
        grid.CreateGrid(6, 4)

        my_sizer = wx.BoxSizer(wx.VERTICAL)
        my_sizer.Add(grid, 0 , wx.EXPAND)
        self.SetSizer(my_sizer)
        grid.SetColLabelValue(0, 'Name')
        grid.SetColLabelValue(1, 'AI 1')
        grid.SetColLabelValue(2, 'AI 2')
        grid.SetColLabelValue(3, 'AI 3')
        grid.SetRowLabelValue(5, 'Total Odds')

        print(bets)

        grid.SetCellValue(0, 0, str(bets[0]))
        grid.SetCellValue(1, 0, str(bets[1]))
        grid.SetCellValue(2, 0, str(bets[2]))
        grid.SetCellValue(3, 0, str(bets[3]))
        grid.SetCellValue(4, 0, str(bets[4]))

        choices_1 = [3, 3, 3]
        choices_2 = [2, 4, 4]
        choices_3 = [10, 1, 1.11]
        choices_4 = [5, 2.5, 2.5]
        choices_5 = [2.5, 3.33, 3.33]

        AI_1 = [rn.choice(choices_1), rn.choice(choices_2), rn.choice(choices_3), rn.choice(choices_4), rn.choice(choices_5)]
        AI_2 = [rn.choice(choices_1), rn.choice(choices_2), rn.choice(choices_3), rn.choice(choices_4), rn.choice(choices_5)]
        AI_3 = [rn.choice(choices_1), rn.choice(choices_2), rn.choice(choices_3), rn.choice(choices_4), rn.choice(choices_5)]
        AI_4 = [rn.choice(choices_1), rn.choice(choices_2), rn.choice(choices_3), rn.choice(choices_4), rn.choice(choices_5)]
        AI_5 = [rn.choice(choices_1), rn.choice(choices_2), rn.choice(choices_3), rn.choice(choices_4), rn.choice(choices_5)]

        grid.SetCellValue(0, 1, str(AI_1[0]))
        grid.SetCellValue(1, 1, str(AI_1[1]))
        grid.SetCellValue(2, 1, str(AI_1[2]))
        grid.SetCellValue(3, 1, str(AI_1[3]))
        grid.SetCellValue(4, 1, str(AI_1[4]))
        grid.SetCellValue(5, 1, str(AI_1[0] * AI_1[1] * AI_1[2] * AI_1[3] * AI_1[4]))

        grid.SetCellValue(0, 2, str(AI_2[0]))
        grid.SetCellValue(1, 2, str(AI_2[1]))
        grid.SetCellValue(2, 2, str(AI_2[2]))
        grid.SetCellValue(3, 2, str(AI_2[3]))
        grid.SetCellValue(4, 2, str(AI_2[4]))
        grid.SetCellValue(5, 2, str(AI_2[0] * AI_2[1] * AI_2[2] * AI_2[3] * AI_2[4]))

        grid.SetCellValue(0, 3, str(AI_3[0]))
        grid.SetCellValue(1, 3, str(AI_3[1]))
        grid.SetCellValue(2, 3, str(AI_3[2]))
        grid.SetCellValue(3, 3, str(AI_3[3]))
        grid.SetCellValue(4, 3, str(AI_3[4]))
        grid.SetCellValue(5, 3, str(AI_3[0] * AI_3[1] * AI_3[2] * AI_3[3] * AI_3[4]))


        #txt = wx.TextCtrl(self)
        #my_sizer.Add(txt, 0, wx.ALL | wx.EXPAND, 5)
        button =wx.Button(self, label="Go to results", pos=(200, 325))
        button.Bind(wx.EVT_BUTTON, parent.gtpage3)
        my_sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)

########################################################################

class PanelThree(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        txt = wx.TextCtrl(self)
        my_sizer.Add(txt, 0, wx.ALL | wx.CENTER, 5)
        

########################################################################
class MyForm(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "5 fold acca",
                          size=(800,600))

        self.panel_one = PanelOne(self)
        self.panel_two = PanelTwo(self)
        self.panel_three = PanelThree(self)
        self.panel_two.Hide()
        self.panel_three.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.sizer.Add(self.panel_three, 1, wx.EXPAND)
        self.SetSizer(self.sizer)


    #----------------------------------------------------------------------

    def gtpage2(self, event):
        self.panel_one.Hide()
        self.panel_two.Show()
        self.Layout()
        self.Update()

    def gtpage3(self, event):
        self.panel_two.Hide()
        self.panel_three.Show()
        self.Layout()
        self.Update()

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()