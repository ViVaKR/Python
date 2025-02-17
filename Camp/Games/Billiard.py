#! /usr/bin/env python3

import pygame
import math
import random

# Pygame 초기화
pygame.init()
# 화면 크기 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RandomPocketBall")
# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
GUIDE_COLOR = (0, 0, 0)
# 당구공 색상
BALL_COLORS = [
    (255, 255, 255),
    (255, 215, 0),
    (255, 0, 0),
    (0, 0, 255),
    (255, 165, 0),
    (128, 0, 128),
    (0, 255, 0),
    (255, 192, 203),
    (0, 255, 255),
]
# 공 설정
BALL_RADIUS = 15
HOLE_RADIUS = 25
ball_positions = []
ball_velocities = [[0, 0] for _ in range(9)]
# 게임 설정
angle = 0
power = 0
# 마찰 설정
current_friction = 0.99  # 마찰을 약간 더 높여서 공이 더 빨리 멈추도록 설정
# 폰트 설정
font = pygame.font.SysFont("Arial", 20)
large_font = pygame.font.SysFont("Arial", 40)
# 구멍 위치
holes = [(65, 65), (WIDTH - 65, 65), (65, HEIGHT - 65), (WIDTH - 65, HEIGHT - 65)]


# 테이블 그리기 함수
def draw_table():
    screen.fill(GREEN)
    pygame.draw.rect(screen, BLACK, (50, 50, WIDTH - 100, HEIGHT - 100), 5)
    for hole in holes:
        pygame.draw.circle(screen, BLACK, hole, HOLE_RADIUS)


# 공 그리기 함수
def draw_balls():
    for i, pos in enumerate(ball_positions):
        pygame.draw.circle(
            screen, BALL_COLORS[i], (int(pos[0]), int(pos[1])), BALL_RADIUS
        )
        pygame.draw.circle(
            screen, BLACK, (int(pos[0]), int(pos[1])), BALL_RADIUS, 1
        )  # 외곽선
        ball_number_text = font.render(str(i + 1), True, BLACK)
        ball_number_rect = ball_number_text.get_rect(center=(int(pos[0]), int(pos[1])))
        screen.blit(ball_number_text, ball_number_rect)


# 조준 가이드 그리기 함수
def draw_aiming_guide(angle):
    start_pos = ball_positions[selected_ball]
    end_pos = (
        start_pos[0] + math.cos(math.radians(angle)) * 100,
        start_pos[1] - math.sin(math.radians(angle)) * 100,
    )
    for i in range(10):
        t = i / 10
        x = int(start_pos[0] + t * (end_pos[0] - start_pos[0]))
        y = int(start_pos[1] + t * (end_pos[1] - start_pos[1]))
        pygame.draw.circle(screen, GUIDE_COLOR, (x, y), 2)


# 파워 레벨 그리기 함수
def draw_power_level(power):
    power_text = font.render(f"Power: {power}/100", True, BLACK)
    power_bar_length = 200
    power_bar_height = 20
    pygame.draw.rect(screen, BLACK, (10, 40, power_bar_length, power_bar_height), 2)
    pygame.draw.rect(
        screen, WHITE, (10, 40, power_bar_length * (power / 100), power_bar_height)
    )
    screen.blit(power_text, (10, 10))


# 시도 횟수 그리기 함수
def draw_attempt_count(attempts):
    attempt_text = font.render(f"Attempts: {attempts}", True, BLACK)
    pygame.draw.rect(screen, WHITE, (10, HEIGHT - 40, 150, 30))
    screen.blit(attempt_text, (10, HEIGHT - 40))


# 공 위치 업데이트 함수
def update_positions():
    global can_shoot
    can_shoot = True
    for i, pos in enumerate(ball_positions):
        pos[0] += ball_velocities[i][0]
        pos[1] += ball_velocities[i][1]
        ball_velocities[i][0] *= current_friction
        ball_velocities[i][1] *= current_friction
        if math.sqrt(ball_velocities[i][0] ** 2 + ball_velocities[i][1] ** 2) >= 0.1:
            can_shoot = False
        # 테이블 범위 내에서 벽과의 충돌 처리
        if pos[0] <= 65 + BALL_RADIUS or pos[0] >= WIDTH - 65 - BALL_RADIUS:
            ball_velocities[i][0] *= -1
        if pos[1] <= 65 + BALL_RADIUS or pos[1] >= HEIGHT - 65 - BALL_RADIUS:
            ball_velocities[i][1] *= -1


# 공 충돌 처리 함수
def handle_collisions():
    for i in range(len(ball_positions)):
        for j in range(i + 1, len(ball_positions)):
            dx = ball_positions[j][0] - ball_positions[i][0]
            dy = ball_positions[j][1] - ball_positions[i][1]
            distance = math.sqrt(dx**2 + dy**2)
            if distance < 2 * BALL_RADIUS:
                # 물리 공식을 사용하여 충돌 후 새 속도 계산
                angle = math.atan2(dy, dx)
                v_i = ball_velocities[i]
                v_j = ball_velocities[j]
                mass_i = mass_j = 1  # 두 공의 질량이 같다고 가정
                # 속도 차이와 위치 차이의 내적 계산
                dot_product = (v_i[0] - v_j[0]) * dx + (v_i[1] - v_j[1]) * dy
                norm_sq = dx * dx + dy * dy
                # 충돌 영향 계산
                impact = (2 * mass_j / (mass_i + mass_j)) * (dot_product / norm_sq)
                # 속도 업데이트
                ball_velocities[i][0] -= impact * dx
                ball_velocities[i][1] -= impact * dy
                ball_velocities[j][0] += impact * dx
                ball_velocities[j][1] += impact * dy
                # 공이 겹치지 않도록 처리
                overlap = 2 * BALL_RADIUS - distance
                ball_positions[i][0] -= dx * (overlap / (2 * distance))
                ball_positions[i][1] -= dy * (overlap / (2 * distance))
                ball_positions[j][0] += dx * (overlap / (2 * distance))
                ball_positions[j][1] += dy * (overlap / (2 * distance))


# 공이 구멍에 들어갔는지 확인하는 함수
def check_result():
    global new_game_prompt, success, fail, pocketed_sum
    for i, pos in enumerate(ball_positions):
        for hole in holes:
            if (
                math.sqrt((pos[0] - hole[0]) ** 2 + (pos[1] - hole[1]) ** 2)
                < HOLE_RADIUS + BALL_RADIUS
            ):
                if pos[0] != -100:  # 아직 포켓에 들어가지 않은 공만 체크
                    pocketed_sum += 1
                    ball_positions[i] = [-100, -100]  # 화면 밖으로 이동시켜 공을 제거
                if i == selected_ball:
                    fail = True
    pocketed_count = sum(
        1 for pos in ball_positions if pos[0] == -100 and pos[1] == -100
    )
    if pocketed_count >= 3:
        success = True
        new_game_prompt = True
    if fail:
        new_game_prompt = True


# 게임 초기화 함수
def reset_game():
    global ball_positions, ball_velocities, angle, power, attempts, can_shoot, success, current_friction, selected_ball, new_game_prompt, pocketed_sum, fail, select_ball_prompt
    ball_positions = []
    while len(ball_positions) < 9:
        x = random.randint(65 + BALL_RADIUS, WIDTH - 65 - BALL_RADIUS)
        y = random.randint(65 + BALL_RADIUS, HEIGHT - 65 - BALL_RADIUS)
        if all(
            math.sqrt((x - pos[0]) ** 2 + (y - pos[1]) ** 2) >= 2 * BALL_RADIUS
            for pos in ball_positions
        ):
            ball_positions.append([x, y])
    ball_velocities = [[0, 0] for _ in range(9)]
    angle = 0
    power = 0
    attempts = 0
    can_shoot = False
    success = False
    current_friction = 0.99
    selected_ball = -1
    new_game_prompt = False
    pocketed_sum = 0
    fail = False
    select_ball_prompt = True


reset_game()
# 메인 게임 루프
running = True
clock = pygame.time.Clock()
attempts = 0
can_shoot = False
success = False
fail = False
new_game_prompt = False
selected_ball = -1
select_ball_prompt = True
while running:
    draw_table()
    draw_balls()
    draw_power_level(power)
    draw_attempt_count(attempts)
    if new_game_prompt:
        if success:
            prompt_text = large_font.render("SUCCESS! NEW GAME? (Y/N)", True, WHITE)
            score_text = large_font.render(f"ATTEMPTS: {attempts}", True, WHITE)
            screen.blit(
                score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 50)
            )
        else:
            prompt_text = large_font.render("FAIL! NEW GAME? (Y/N)", True, WHITE)
        screen.blit(
            prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, HEIGHT // 2)
        )
    elif select_ball_prompt:
        select_ball_text = large_font.render("SELECT BALL (1-9)", True, WHITE)
        screen.blit(
            select_ball_text,
            (WIDTH // 2 - select_ball_text.get_width() // 2, HEIGHT // 2),
        )
    else:
        draw_aiming_guide(angle)
    keys = pygame.key.get_pressed()
    if can_shoot and selected_ball != -1 and not new_game_prompt:
        if keys[pygame.K_UP]:
            power = min(100, power + 1)
        if keys[pygame.K_DOWN]:
            power = max(0, power - 1)
        if keys[pygame.K_LEFT]:
            angle = (angle - 1) % 360
        if keys[pygame.K_RIGHT]:
            angle = (angle + 1) % 360
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not new_game_prompt:
                if event.key == pygame.K_0:
                    new_game_prompt = True
                elif event.key == pygame.K_1:
                    selected_ball = 0
                    select_ball_prompt = False
                elif event.key == pygame.K_2:
                    selected_ball = 1
                    select_ball_prompt = False
                elif event.key == pygame.K_3:
                    selected_ball = 2
                    select_ball_prompt = False
                elif event.key == pygame.K_4:
                    selected_ball = 3
                    select_ball_prompt = False
                elif event.key == pygame.K_5:
                    selected_ball = 4
                    select_ball_prompt = False
                elif event.key == pygame.K_6:
                    selected_ball = 5
                    select_ball_prompt = False
                elif event.key == pygame.K_7:
                    selected_ball = 6
                    select_ball_prompt = False
                elif event.key == pygame.K_8:
                    selected_ball = 7
                    select_ball_prompt = False
                elif event.key == pygame.K_9:
                    selected_ball = 8
                    select_ball_prompt = False
                elif event.key == pygame.K_SPACE and can_shoot and selected_ball != -1:
                    ball_velocities[selected_ball] = [
                        math.cos(math.radians(angle)) * power / 5,
                        -math.sin(math.radians(angle)) * power / 5,
                    ]
                    attempts += 1
                    can_shoot = False
                elif event.key == pygame.K_r:
                    new_game_prompt = True
            else:
                if event.key == pygame.K_y:
                    reset_game()
                elif event.key == pygame.K_n:
                    running = False
    if (
        not success
        and not fail
        and selected_ball != -1
        and not new_game_prompt
        and not select_ball_prompt
    ):
        update_positions()
        handle_collisions()
        check_result()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
