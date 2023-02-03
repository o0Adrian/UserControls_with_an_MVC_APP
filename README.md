# Before we start

IMPORTANT: This is a workaround. In the future I will improve flet-mvc library to add decorators send/receive in order to connect them without the need of sending objects directly to the UserControl. See "What is next" below.

## Flet's User Controls in a nutshell:

In simple terms, flet User Control objects are Controls created by the users. Controls like: Container, Text, Row... Literally they can be used as any other control in our view.

Why are they useful? They are meant to be reusable. Let's say I create two applications and want them to have a certain block of "view", then I can just create my own UserControl.

Please reference flet documentation: [UserControls](https://flet.dev/docs/guides/python/user-controls/)

Essentially they should be created using an MVC Architecture. Currently I haven't created a correct structure for them. Please give me some time to create the best practices for them. In the meantime we will use ModernNabBar User Control created by LineIndent


## ModernNavBar UserControl:

As mentioned I am not the author of the NavBar UserControl, the developer and author is LineIndent, please visit his repository and give him some stars :)! [flet-modern-navbar](https://github.com/LineIndent/flet-modern-navbar)
His youtube channel is: [@Lineindent](https://www.youtube.com/@lineindent)

### * Changes made from Line Indent's version

The only thing that I changed from Line Indent's version is that I made it independent.

**As mentioned:** a UserControl should not depend to a certain app, becuase it should have the capacity of being used in different apps.

Please see/compare how I changed the *build* method as well as added the *AnimateSidebar* inside the UserControl, not outside as in the original version.

# Explanation

In summary, in order to connect a User Control to our main app it's as simple as conecting either the app's controller, model, view, page or anything that you want, into the UserControl.

```python

class MyControl(ft.UserControl):
    def __init__(self, parent_controller):
        self.parent_controller = parent_controller # <- here
        
        ## Other examples could be:
        # self.parent_model = parent_model
        # self.parent_page = parent_page
        # Or anything else that you want to send from the app to this user control

        super().__init__()
```

Then we will send the controller (as for this example) into the control when being used in the View:

```python
class View(FletView):
    def __init__(self, controller, model):
        content = [
            ft.Row(
                controls= [
                    ModernNavBar(controller), # <- here we send the controller to our UserControl
                    ...
                ]
            )
        ]

        super().__init__(model, content, controller)
```

It's as easy as that.

Please see line 21 from navbar.py and line 7 from main.py this is an example of how to conect them. Also see line 29 for another possible solution, in that case we will need to send the model and controller to the UserControl. But it's another good solution.

# What is next?

As mentioned in the first paragraph, this is a work around, in the future I will try to work on send/receive decorator that will allow the user to make a conection between a UserControl and a main app or even UserControl to another UserControl!

something like:

```python
class MyControl(ft.UserControl):
    def __init__(self):
        super().__init__()
    
    @send
    def on_icon_click(self, e):
        return SomeAction


class MySecondControl(ft.UserControl):
    def __init__(self):
        super().__init__()
    
    @receive(action=SomeAction)
    def on_icon_click(self, action):
        ...
```
