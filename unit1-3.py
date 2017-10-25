#


import ui

def calculate (sender) :
    #
    
    # input
    length = int(view['input_lenth'].text)
    width = int(view['input_with'].text) 
    
    area = length * width
    pirmitor = (length + width) * 2
    view['area_lable'].text = str(area)
    view['pirimitor_lable'].text = str(pirmitor)

view = ui.load_view()
view.present('sheet')
