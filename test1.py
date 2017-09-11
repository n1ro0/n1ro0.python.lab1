import argparse


def test():

    a = 1
    def hello_world():
        print(a)
        print("Hello world!")

    print(hello_world.__code__, hello_world.__closure__,
          hello_world.__defaults__, hello_world.__kwdefaults__,
          hello_world.__name__, hello_world.__qualname__, dir(hello_world))



def draw_pieplot():
    print("|||pieplot||||")

def draw_lineplot():
    print("|||lineplot|||")

def draw(method):
    draw_methods = {"pieplot":draw_pieplot,
                    "lineplot":draw_lineplot}
    draw_methods[method]()



parser = argparse.ArgumentParser(description='Sample argparse py')
parser.add_argument('--method', type=str, choices=("pieplot", "lineplot"))
output = parser.parse_args()

draw(output.method)