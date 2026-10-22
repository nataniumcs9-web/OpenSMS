from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton

from kivy.lang import Builder
from kivy.properties import StringProperty

Builder.load_string('''
<ButtonControl>:
    size_hint_x: 1
    height: "48dp"
    theme_bg_color: "Custom"
    md_bg_color: root.btn_colour
    MDButtonIcon:
        icon: root.btn_icon
        theme_text_color: "Custom"
        text_color: "white"
    MDButtonText:
        text: root.btn_txt
        theme_text_color: "Custom"
        text_color: "white"

<AppHomeBox>:
    orientation: "vertical"
    padding: "18dp", "14dp", "18dp", "8dp"
    canvas.before:
        Color:
            rgba: (0.96, 0.97, 0.99, 1)
        Rectangle:
            pos: self.pos
            size: self.size

    MDScrollView:
        do_scroll_x: False
        bar_width: 0

        MDBoxLayout:
            orientation: "vertical"
            adaptive_height: True
            spacing: "16dp"

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "2dp"
                MDLabel:
                    text: "Your messaging hub"
                    font_style: "Headline"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: "#172B4D"
                    adaptive_height: True
                MDLabel:
                    text: "Control your SMS gateway from one simple dashboard."
                    font_style: "Body"
                    role: "medium"
                    theme_text_color: "Custom"
                    text_color: "#68778D"
                    adaptive_height: True

            MDCard:
                orientation: "vertical"
                size_hint_y: None
                height: "230dp"
                padding: "20dp"
                spacing: "10dp"
                radius: [24, 24, 24, 24]
                theme_bg_color: "Custom"
                md_bg_color: "#17345C"

                MDLabel:
                    text: "SMS API  /  DEVICE GATEWAY"
                    font_style: "Label"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: "#B8CAE2"
                    adaptive_height: True

                MDLabel:
                    text: "Your server"
                    font_style: "Headline"
                    role: "medium"
                    theme_text_color: "Custom"
                    text_color: "#FFFFFF"
                    adaptive_height: True

                MDLabel:
                    id: api_srv_lbl
                    text: "API Server is not running"
                    font_style: "Body"
                    role: "medium"
                    theme_text_color: "Custom"
                    text_color: "#E4ECF7"
                    adaptive_height: True

                Widget:
                    size_hint_y: 1

                ButtonControl:
                    id: api_srv_btn
                    btn_colour: "#168B68"
                    style: "filled"
                    on_release: app.api_server_mgr(self)

            MDLabel:
                text: "Quick access"
                font_style: "Title"
                role: "medium"
                theme_text_color: "Custom"
                text_color: "#172B4D"
                adaptive_height: True

            MDBoxLayout:
                adaptive_height: True
                spacing: "10dp"

                MDButton:
                    style: "outlined"
                    size_hint_x: 1
                    on_release: app.goto_app_settings()
                    MDButtonIcon:
                        icon: "tune-variant"
                    MDButtonText:
                        text: "Settings"

                MDButton:
                    style: "outlined"
                    size_hint_x: 1
                    on_release: app.goto_logs_screen()
                    MDButtonIcon:
                        icon: "text-box-outline"
                    MDButtonText:
                        text: "Activity logs"

            MDCard:
                orientation: "vertical"
                adaptive_height: True
                padding: "16dp"
                spacing: "6dp"
                radius: [20, 20, 20, 20]
                theme_bg_color: "Custom"
                md_bg_color: "#FFFFFF"

                MDLabel:
                    text: "Connect an app"
                    font_style: "Title"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: "#172B4D"
                    adaptive_height: True
                MDLabel:
                    text: "Use the SMS API endpoint to send messages through this Android device. Keep your API key private."
                    font_style: "Body"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: "#68778D"
                    adaptive_height: True
''')


class AppHomeBox(MDBoxLayout):
    pass


class ButtonControl(MDButton):
    btn_icon = StringProperty("play")
    btn_txt = StringProperty("Start server")
    btn_colour = StringProperty("#168B68")
