class SettingsGame:
    def __init__(self):
        self.FPS = 1
        self.screen_width = 1040 + 1
        self.screen_height = 880 + 1
        self.square_size = 40
        self.FPS = 20

        """Number of squares"""
        self.width_square_number = int(self.screen_width / self.square_size)
        self.height_square_number = int(self.screen_height / self.square_size)

        """Colors"""
        self.white_color = (255, 255, 255)
        self.black_color = (0, 0, 0)
        self.blue_color = (51, 153, 255)
        self.red_color = (255, 0, 0)
        self.green_color = (51, 255, 000)

        """Snake Directions"""
        self.right = "Right"
        self.left = "Left"
        self.up = "Up"
        self.down = "Down"

        self.start_direction = self.right

        """Snake Game Settings"""
        self.status_game = True
        self.number_members = 3
        self.number_apples = 2
