from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color

class LoginPage(App):
    def build(self):
        # Set the window size (adjust as needed for your mobile app)
        Window.size = (300, 500)
        Window.clearcolor = (1, 1, 1, 1)  # Set the window background color to white (1, 1, 1, 1)

        layout = RelativeLayout()

        # Add a white background
        with layout.canvas:
            Color(1, 1, 1, 1)  # White color
            self.background = Rectangle(pos=layout.pos, size=layout.size)

        #welcome tag
        welcome_label = Label(text='Welcome back! Glad to see you!', font_size=25, size_hint_y=None, height=30, pos_hint={'center_x': 0.5, 'center_y': 0.9})
        welcome_label.color = (0,0,0,1)
        
        # Username Input Field
        username_label = Label(text='Enter Your Email', font_size=30, size_hint_y=None, height=30, pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.username_input = TextInput(multiline=False, size_hint_y=None, height=50, pos_hint={'center_x': 0.5, 'center_y': 0.6})
        username_label.color = (0, 0, 0, 1)  # Set text color to black
        self.username_input.text_color = (0, 0, 0, 1)  # Set input text color to black

        # Password Input Field
        password_label = Label(text='Password', font_size=30, size_hint_y=None, height=30, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.password_input = TextInput(multiline=False, password=True, size_hint_y=None, height=50, pos_hint={'center_x': 0.5, 'center_y': 0.4})
        password_label.color = (0, 0, 0, 1)  # Set text color to black
        self.password_input.text_color = (2, 2, 1, 1)  # Set input text color to black

        # Login Button
        login_button = Button(text='Login', font_size=30, size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        login_button.background_color = (0, 2, 255, 255)
        login_button.bind(on_press=self.login)

        layout.add_widget(welcome_label)
        layout.add_widget(username_label)
        layout.add_widget(self.username_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)

        return layout

    def login(self, instance):
        # You can implement your login logic here
        username = self.username_input.text
        password = self.password_input.text

        if username == 'your_username' and password == 'your_password':
            print("Login successful")
        else:
            print("Login failed")

if __name__ == '__main__':
    LoginPage().run()
