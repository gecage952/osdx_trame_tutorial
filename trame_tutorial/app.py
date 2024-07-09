from trame.decorators import TrameApp
from trame.widgets import html, router, vuetify3 as vuetify
from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout


@TrameApp()
class App:


    def __init__(self):
        self.server = get_server(client_type="vue3")

        self.create_ui()

    def create_ui(self):
        with SinglePageLayout(self.server) as layout:
            with layout.content:
                with vuetify.VCol():
                    vuetify.VTextField("Hello, World!")
                    vuetify.VBtn("Click Me!")
            return layout
