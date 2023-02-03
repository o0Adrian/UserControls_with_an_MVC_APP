from flet_mvc import FletController, alert, FletView, data
from user_controls.navbar import ModernNavBar
import flet as ft

# Controller
class MainController(FletController):
    def on_icon_click(self, e):
        """
        NOTE: This is the method that we want to be called
        whenever we click a button of the ModernNavBar User Control.
        
        But how is it called?
        Take a look at /user_controls/navbar.py > on_icon_click
        """
        value = e.control.content.controls[1].value
        self.model.text.current.value = f"You clicked: {value}"
        self.alert("clicked a tab", alert.INFO)
        self.update()

# Model
class MainModel():
    def __init__(self):
        self.text = ft.Ref[ft.Text]()

# View
class MainView(FletView):
    def __init__(self, controller, model):
        content = [
            ft.Row(
                controls= [
                    # NOTE: See how below we are using the ModernNavBar as if it were any other flet control.
                    # but in this case we send the apps controller (you can send anything: the page/model/anything.)
                    ModernNavBar(controller),
                    ft.Text(
                        ref=model.text,
                        value="You clicked: None",
                        text_align="center"
                    )
                ]
            )
        ]

        super().__init__(model, content, controller)

# Main
def main(page: ft.Page):
    # MVC set-up
    model = MainModel()
    controller = MainController(page, model)
    view = MainView(controller, model)

    # Settings
    page.title = "Morden Sidebar"
    page.theme_mode = "dark"
    page.bgcolor = "white54"
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    page.add(
        *view.content
    )

    page.update()


if __name__ == '__main__':
    ft.app(target=main)
