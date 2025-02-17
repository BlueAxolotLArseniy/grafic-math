from pygame import Rect
from enemy_settings import EnemySettings


DEBUG_MODE = True

SCREEN_WIDTH = 960  # 1920 // 2
SCREEN_HEIGHT = 540  # 1080 // 2

HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

GAME_FIELD_RECT = Rect(-1500, -1500, 3000, 3000)

STARS_COUNT = 500

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (252, 107, 3)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = BLACK

FPS = 120

MOVE_PLAYER_SPEED = 8
BULLET_SPEED = 15
BULLET_MAX_DISTANCE = 1000

BASE_PLAYER_HEALTH = 100

ENABLE_ENEMIES = True
DUMMY_ENEMIES = False

ENEMY1_SETTINGS = EnemySettings(
    fire_rate=10,
    speed=5,
    image_path='images/game/enemy1barrels.png',
    health=150
)

ENEMY2_SETTINGS = EnemySettings(
    fire_rate=14,
    speed=3,
    image_path='images/game/enemy2barrels.png',
    health=100
)
