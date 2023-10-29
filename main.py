from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.uix.boxlayout import BoxLayout

class LoginPage(App):
    def build(self):
        # Set the window size
        Window.size = (0.8 * Window.width, 0.8 * Window.height)
        Window.clearcolor = (1, 1, 1, 1)  # Set the window background color to white

        layout = RelativeLayout()

        # Add a white background
        with layout.canvas:
            Color(1, 1, 1, 1)
            self.background = Rectangle(pos=layout.pos, size=layout.size)

        # Welcome tags
        welcome_label = Label(text="[b]Welcome back![/b]", font_size=55, color=(0, 0, 0, 1), size_hint_y=None, height=30, pos_hint={'center_x': 0.5, 'center_y': 0.86}, markup=True)
        welcome_label2 = Label(text="[b]Glad to see you!![/b]", font_size=55, color=(0, 0, 0, 1), size_hint_y=None, height=30, pos_hint={'center_x': 0.5, 'center_y': 0.8}, markup=True)
        
        
        # Username Input Field
        self.username_input = TextInput(multiline=False, size_hint=(None, None), size=(450, 50), font_size=24, pos_hint={'center_x': 0.5, 'center_y': 0.6}, hint_text="Enter your email")

        # Create a BoxLayout for password input and "See Password" button
        password_layout = BoxLayout(orientation='horizontal', spacing=-1, size_hint=(None, None), size=(450, 50), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        # Password Input Field
        self.password_input = TextInput(multiline=False, password=True, size_hint=(1, None), height=50, font_size=24, hint_text="Enter your password")
        
        # "See Password" Button
        see_password_button = Button(
            text='\uf06e',
            font_name='fonts/fa-solid-900',  
            font_size=26,
            size_hint=(None, None),
            size=(50, 50),
            on_press=self.toggle_password_visibility
        )

        password_layout.add_widget(self.password_input)
        password_layout.add_widget(see_password_button)

        # Login Button
        login_button = Button(text='Login', font_size=30, background_color=(0, 2, 230, 245), size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        login_button.bind(on_press=self.login)

        layout.add_widget(welcome_label)
        layout.add_widget(welcome_label2)
        layout.add_widget(self.username_input)
        layout.add_widget(password_layout)
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

    def toggle_password_visibility(self, instance):
        # Toggle the password visibility
        self.password_input.password = not self.password_input.password

if _name_ == '_main_':
    LoginPage().run()
