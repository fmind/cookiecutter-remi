#!/usr/bin/env python3

"""Documentation of the app."""

import remi.gui as gui

from remi import start, App


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=120, height=100)
        self.lbl = gui.Label("Hello world!")
        self.bt = gui.Button("Press me!")

        self.bt.onclick.do(self.on_button_pressed)

        container.append(self.lbl)
        container.append(self.bt)

        return container

    def on_button_pressed(self, widget):
        self.lbl.set_text("Button pressed!")
        self.bt.set_text("Hi!")


if __name__ == "__main__":
    start(MyApp)
