import arcade



SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600





class MyGame(arcade.Window):

    """ Main application class. """



    def __init__(self, width, height):

        super().__init__(width, height)



        arcade.set_background_color(arcade.color.AMAZON)



    def setup(self):

        # Set up your game here

        pass



    def on_draw(self):

        """ Render the screen. """

        arcade.start_render()

        # Your drawing code goes here



    def update(self, delta_time):

        """ All the logic to move, and the game logic goes here. """

        pass





def main():

    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)

    game.setup()

    arcade.run()





if __name__ == "__main__":

    main()

# SELANJUTNYA


SPRITE_SCALING_COIN = 0.2



coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)

# SELANJUTNYA

def setup(self):

    """ Set up the game and initialize the variables. """



    # Membuat list sprite

    self.player_list = arcade.SpriteList()

    self.coin_list = arcade.SpriteList()



    # Skor

    self.score = 0



    # Menyiapkan pemain
def draw_pine_tree(x, y):

    """ This function draws a pine tree at the specified location. """

    

    # Menggambar segitiga di bagian atas. 

    # Kita butuh tiga poin x, y untuk menggambar segitiga

    arcade.draw_triangle_filled(x + 40, y,       # Poin 1

                                x, y - 100,      # Poin 2

                                x + 80, y - 100, # Poin 3

                                arcade.color.DARK_GREEN)


