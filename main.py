import PySimpleGUI as sg


def analyseGesture(input_segment, graph_size):
    return getSegment(input_segment[0], graph_size), getSegment(input_segment[1], graph_size)


def getSegment(point_coordinate, graph_size):
    x, y = point_coordinate
    if x < graph_size[0]/3.0:
        # on the left side
        if y < graph_size[1]/3.0:
            return 0
        elif y < graph_size[1]/3.0*2.0:
            return 3
        else:
            return 6
    elif x < graph_size[0]/3.0*2.0:
        # in the middle
        if y < graph_size[1]/3.0:
            return 1
        elif y < graph_size[1]/3.0*2.0:
            return 4
        else:
            return 7
    else:
        if y < graph_size[1]/3.0:
            return 2
        elif y < graph_size[1]/3.0*2.0:
            return 5
        else:
            return 8


def main():
    # obj = tk.Tk() # Creates a tkinter object
    # label = tk.Label(obj, text="This is a text button")

    # print(sg.Window.get_screen_size())
    # w, h = sg.Window.get_screen_size()

    screen_size = (50, 50)
    graph_size = (100, 100)
    layout = [[sg.Graph(canvas_size=graph_size, graph_bottom_left=(0, 0), graph_top_right=graph_size,
                        enable_events=True, drag_submits=True, key="-GRAPH-", change_submits=True,
                        background_color='lightblue')]]

    window = sg.Window(title="User Input", layout=layout)
    graph = window["-GRAPH-"]

    # ---===--- Loop taking in user input --- #
    dragging = False
    start_point = end_point = prior_rect = None
    while True:
        # this block processes the motion
        event, values = window.read()
        if event is None:
            break
        if event == "-GRAPH-":
            x, y = values["-GRAPH-"]
            if not dragging:
                start_point = (x, y)
                dragging = True
                drag_figures = graph.get_figures_at_location((x, y))
                lastxy = x, y
            else:
                end_point = (x, y)
        elif event.endswith('+UP'):  # The drawing has ended because mouse up

            # info = window["info"]
            # info.update(value=f"grabbed rectangle from {start_point} to {end_point}")

            gesture_segment = (start_point, end_point)

            # clear all the buffer
            start_point, end_point = None, None  # enable grabbing a new rect
            dragging = False
            prior_rect = None

            # return the segments
            output_gesture = analyseGesture(gesture_segment, graph_size)
            print("start", output_gesture[0], "end", output_gesture[1])
    window.close()

main()