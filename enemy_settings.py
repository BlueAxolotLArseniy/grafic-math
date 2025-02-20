
from dataclasses import dataclass


@dataclass
class EnemySettings:
    fire_rate: int
    speed: int
    image_path: str
    health: int
    bullet_damage: float
    bullet_speed: float
