import wx

STA = "<!START>"
STOP = "<!STOP>"

matrix = None
reverse_matrix = None

def init():
    global matrix, reverse_matrix
    matrix = [
        [
            [STA, 'A', 'B', 'C'],
            ['D', 'E', 'F', 'G'],
            ['H', 'I', 'J', 'K'],
            ['L', 'M', 'N', 'O']
        ],
        [
            ['P', 'Q', 'R', 'S'],
            ['T', 'U', 'V', 'X'],
            ['Y', 'W', 'Z', '*'],
            [',', ';', ':', '-']
        ],
        [
            [' ', 'a', 'b', 'c'],
            ['d', 'e', 'f', 'g'],
            ['h', 'i', 'j', 'k'],
            ['l', 'm', 'n', 'o']
        ],
        [
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v', 'x'],
            ['y', 'w', 'z', '+'],
            ['.', '!', '?', STOP]
        ]
    ]

    reverse_matrix = {}
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                code = i*100 + j * 10 + k
                c = matrix[i][j][k]
                reverse_matrix[c] = code

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Character Code Finder")
        panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(panel, label="Enter a character:")
        sizer.Add(self.label, 0, wx.ALL | wx.CENTER, 10)

        self.entry = wx.TextCtrl(panel)
        sizer.Add(self.entry, 0, wx.ALL | wx.CENTER, 10)

        self.button = wx.Button(panel, label="Find Code")
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)
        sizer.Add(self.button, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)

    def on_button_click(self, event):
        char = self.entry.GetValue()
        if char in reverse_matrix:
            wx.MessageBox(f'Code for {char}: {reverse_matrix[char]:03d}', "Character Code", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox(f'Character {char} not found in matrix.', "Character Not Found", wx.OK | wx.ICON_WARNING)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == "__main__":
    init()
    app = MyApp()
    app.MainLoop()
