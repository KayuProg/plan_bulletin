from controls import frame#実行場所が一階層上だからfrom controls

class calender_contents(frame.frame_class):#frame_class継承
    def __init__(self,title):
        super().__init__(title)#frame_classを継承してtitleを渡す．
        