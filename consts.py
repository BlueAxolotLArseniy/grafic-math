from pygame import Rect
from enemy_settings import EnemySettings


DEBUG_MODE = True

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

GAME_FIELD_RECT = Rect(-1500, -1500, 3000, 3000)

STARS_COUNT = 50

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (252, 107, 3)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = BLACK

FPS = 60

MOVE_PLAYER_SPEED = 8
BASE_PLAYER_HEALTH = 100
PLAYER_BULLET_DAMAGE = 5
PLAYER_BULLET_SPEED = 30

BULLET_MAX_DISTANCE = 1500

ENABLE_ENEMIES = True
DUMMY_ENEMIES = False
MAX_QUANTITY_ENEMIES = 4



ENEMY1_SETTINGS = EnemySettings(
    fire_rate=10,
    speed=5,
    image_path='images/game/enemy1barrels.png',
    health=150,
    bullet_damage=2.5,
    bullet_speed=20
)

ENEMY2_SETTINGS = EnemySettings(
    fire_rate=20,
    speed=3,
    image_path='images/game/enemy2barrels.png',
    health=100,
    bullet_damage=5,
    bullet_speed=15
)
