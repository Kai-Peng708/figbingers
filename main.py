import PySimpleGUI as sg



# obj = tk.Tk() # Creates a tkinter object
# label = tk.Label(obj, text="This is a text button")

# print(sg.Window.get_screen_size())
# w, h = sg.Window.get_screen_size()

screen_size = (50,50)
layout = [[sg.Graph(canvas_size=screen_size, graph_bottom_left= (0,0), graph_top_right=screen_size ,
                   enable_events=True, drag_submits=True ,key="-GRAPH-",change_submits=True,
                   background_color='lightblue')]]

window = sg.Window(title="User Input", layout=layout, margins=screen_size )
graph = window["-GRAPH-"]

# ---===--- Loop taking in user input --- #
dragging = False
start_point = end_point = prior_rect = None
while True:
    event, values = window.read()

    if event is None:
        break

    if  event == "-GRAPH-":
        x, y = values["-GRAPH-"]
        if not dragging:
            start_point = (x, y)
            dragging = True
            drag_figures = graph.get_figures_at_location((x, y))
            lastxy = x, y
        else:
            end_point = (x, y)
            print("start", start_point,"end",end_point)
    elif event.endswith('+UP'):  # The drawing has ended because mouse up
        # info = window["info"]
        # info.update(value=f"grabbed rectangle from {start_point} to {end_point}")
        start_point, end_point = None, None  # enable grabbing a new rect
        dragging = False
        prior_rect = None