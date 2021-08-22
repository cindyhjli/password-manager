import arcade
import arcade.gui

width = 400
height = 700
title = "passwordapp"


class MainView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instagram", width / 2, 650, arcade.color.BRIGHT_NAVY_BLUE, 20,
                         anchor_x="center", font_name='Verdana Bold')
        arcade.draw_text("< Back", 15, 652, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text("Edit", 325, 652, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text("Username", 30, 570, arcade.color.BRIGHT_NAVY_BLUE, 18, font_name='Verdana Bold')
        arcade.draw_text("@cd_tech", 30, 540, arcade.color.BLACK, 18)
        arcade.draw_text("Password", 30, 480, arcade.color.BRIGHT_NAVY_BLUE, 18, font_name='Verdana Bold')
        arcade.draw_text("wo14g31IU", 30, 450, arcade.color.BLACK, 18)
        self.icon_list: arcade.SpriteList = arcade.SpriteList()
        add = Icon("Images/7.png", 0.04)
        add.position = 180, 493
        self.icon_list.append(add)
        self.icon_list.draw()
        arcade.draw_text("Url", 30, 400, arcade.color.BRIGHT_NAVY_BLUE, 18, font_name='Verdana Bold')
        arcade.draw_text("www.instagram.com", 30, 370, arcade.color.BLACK, 18)
        arcade.draw_text("Tag", 30, 310, arcade.color.BRIGHT_NAVY_BLUE, 18, font_name='Verdana Bold')
        arcade.draw_text("Social Media", 30, 280, arcade.color.PURPLE, 18)


class Icon(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename=filename, scale=scale)


def main():
    window = arcade.Window(width, height, title)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()


main()
