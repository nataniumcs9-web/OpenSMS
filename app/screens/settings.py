from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField

from kivy.lang import Builder

Builder.load_string('''
<ApiKeyTxtbox>:
    mode: "outlined"
    readonly: True

<SettingsBox>:
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
            id: main_scroll_bx
            orientation: "vertical"
            adaptive_height: True
            spacing: "14dp"

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "2dp"
                MDLabel:
                    text: "Settings"
                    font_style: "Headline"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: "#172B4D"
                    adaptive_height: True
                MDLabel:
                    text: "Keep your device gateway configured the way you need it."
                    font_style: "Body"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: "#68778D"
                    adaptive_height: True

            MDCard:
                orientation: "vertical"
                adaptive_height: True
                padding: "8dp"
                radius: [20, 20, 20, 20]
                theme_bg_color: "Custom"
                md_bg_color: "#FFFFFF"
                MDListItem:
                    MDListItemLeadingIcon:
                        icon: "rocket-launch-outline"
                    MDListItemHeadlineText:
                        text: "Start server automatically"
                    MDListItemSupportingText:
                        text: "Start the API when the app opens"
                    MDSwitch:
                        id: auto_start_sw
                        pos_hint: {"center_y": 0.5}
                        icon_active: "check"
                        icon_inactive: "close"
                        icon_active_color: "#168B68"
                        track_color_active: "#168B68"
                        on_release: app.save_settings(self, "switch")

            MDCard:
                orientation: "vertical"
                adaptive_height: True
                padding: "16dp"
                spacing: "8dp"
                radius: [20, 20, 20, 20]
                theme_bg_color: "Custom"
                md_bg_color: "#FFFFFF"
                MDLabel:
                    text: "API port"
                    font_style: "Title"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: "#172B4D"
                    adaptive_height: True
                MDLabel:
                    text: "Changing the port requires restarting the server."
                    font_style: "Body"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: "#68778D"
                    adaptive_height: True
                MDTextField:
                    id: port_no_inp
                    mode: "outlined"
                    input_filter: "int"
                    hint_text: "Port number"

            MDCard:
                orientation: "horizontal"
                adaptive_height: True
                padding: "16dp"
                spacing: "10dp"
                radius: [20, 20, 20, 20]
                theme_bg_color: "Custom"
                md_bg_color: "#FFFFFF"
                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: "4dp"
                    MDLabel:
                        text: "API key"
                        font_style: "Title"
                        role: "small"
                        theme_text_color: "Custom"
                        text_color: "#172B4D"
                        adaptive_height: True
                    MDLabel:
                        text: "Generate a new key to replace the current one."
                        font_style: "Body"
                        role: "small"
                        theme_text_color: "Custom"
                        text_color: "#68778D"
                        adaptive_height: True
                MDFabButton:
                    icon: "autorenew"
                    style: "small"
                    theme_bg_color: "Custom"
                    md_bg_color: "#E8EFFA"
                    pos_hint: {"center_y": 0.5}
                    on_release: app.new_api_key_pop()

            MDBoxLayout:
                adaptive_height: True
                spacing: "10dp"
                MDButton:
                    style: "filled"
                    theme_bg_color: "Custom"
                    md_bg_color: "#17345C"
                    on_release: app.save_settings(self)
                    MDButtonIcon:
                        icon: "content-save-outline"
                        theme_text_color: "Custom"
                        text_color: "#FFFFFF"
                    MDButtonText:
                        text: "Save changes"
                        theme_text_color: "Custom"
                        text_color: "#FFFFFF"
                MDButton:
                    style: "outlined"
                    on_release: app.reset_settings(self)
                    MDButtonIcon:
                        icon: "restore"
                    MDButtonText:
                        text: "Reset"
''')


class SettingsBox(MDBoxLayout):
    pass


class ApiKeyTxtbox(MDTextField):
    pass
