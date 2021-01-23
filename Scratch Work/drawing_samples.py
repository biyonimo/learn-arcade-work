# Import the "arcade" library
import arcade
arcade.open_window(600, 600, "YONI_YONI")

# Keep the window up until someone closes it.
# Set the background color
# arcade.set_background_color((255, 59, 10))        #  arcade.color.AMBER)
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
