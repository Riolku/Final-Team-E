import pygame


def healthbar(surface, max_health_color, current_health_color, x, y, current_health, max_health, health_bar_height):
    # draws the health bar at max value
    pygame.draw.rect(surface, max_health_color, (x, y, max_health, health_bar_height), 0)

    # draws the health bar at current value
    pygame.draw.rect(surface, current_health_color, (
        x, y, int(max(min(current_health / float(max_health) * max_health, max_health), 0)), health_bar_height), 0)