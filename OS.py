import pygame
import random
import math
import sys
from datetime import datetime

# ---------------- CONFIG ----------------
WIDTH, HEIGHT = 1024, 768
FPS = 60

BG = (5, 8, 10)
GREEN = (0, 255, 120)
CYAN = (0, 200, 255)
RED = (255, 60, 60)
AMBER = (255, 180, 60)
GRAY = (120, 120, 120)

LOG_LINES = 26

LOG_MESSAGES = [
    "[CORE] Neural branch expanded",
    "[AI] Recursive depth increased",
    "[NET] Signal triangulated",
    "[SYS] Heuristic drift corrected",
    "[MEM] Volatile cache overwritten",
    "[WARN] Pattern instability detected",
    "[OK] Stabilization complete",
    "[CORE] Predictive loop refined",
    "[AI] Autonomous cycle executed",
    "[NET] External vector mapped",
]

# ---------------------------------------
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()

pygame.display.set_caption("VOIDFRAME // BLACKCORE OS")
clock = pygame.time.Clock()


font_small = pygame.font.SysFont("consolas", 14)
font_medium = pygame.font.SysFont("consolas", 18)
font_large = pygame.font.SysFont("consolas", 28)

logs = []

def add_log():
    msg = random.choice(LOG_MESSAGES)
    timestamp = datetime.now().strftime("%H:%M:%S")
    logs.append(f"{timestamp} {msg}")
    if len(logs) > LOG_LINES:
        logs.pop(0)

for _ in range(LOG_LINES):
    add_log()

# AI CORE NODES
nodes = []
for _ in range(40):
    nodes.append({
        "x": WIDTH//2 + random.randint(-120, 120),
        "y": HEIGHT//2 + random.randint(-120, 120),
        "vx": random.uniform(-0.3, 0.3),
        "vy": random.uniform(-0.3, 0.3),
    })

alert_timer = 0
alert_active = False

# ---------------- MAIN LOOP ----------------
running = True
while running:
    clock.tick(FPS)
    screen.fill(BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # ---- RANDOM LOG UPDATES ----
    if random.random() < 0.05:
        add_log()

    # ---- ALERT SYSTEM ----
    if not alert_active and random.random() < 0.002:
        alert_active = True
        alert_timer = random.randint(60, 120)

    if alert_active:
        alert_timer -= 1
        if alert_timer <= 0:
            alert_active = False

    # ---- LEFT LOG PANEL ----
    pygame.draw.rect(screen, (10, 15, 20), (20, 20, 420, HEIGHT - 40))
    for i, line in enumerate(logs):
        color = GREEN if "[WARN]" not in line else RED
        text = font_small.render(line, True, color)
        screen.blit(text, (30, 30 + i * 22))

    # ---- RIGHT METRICS ----
    pygame.draw.rect(screen, (10, 15, 20), (WIDTH - 300, 20, 280, HEIGHT - 40))
    metrics = [
        ("CPU LOAD", random.randint(70, 95)),
        ("AI LOAD", random.randint(80, 98)),
        ("SIGNAL", random.randint(50, 90)),
        ("LATENCY", random.randint(12, 60)),
    ]

    for i, (label, value) in enumerate(metrics):
        t = font_medium.render(f"{label}: {value}%", True, CYAN)
        screen.blit(t, (WIDTH - 280, 40 + i * 40))
        pygame.draw.rect(
            screen,
            CYAN,
            (WIDTH - 280, 65 + i * 40, value * 2, 6),
        )

    # ---- AI CORE VISUAL ----
    center_x, center_y = WIDTH // 2, HEIGHT // 2

    for n in nodes:
        n["x"] += n["vx"]
        n["y"] += n["vy"]

        if abs(n["x"] - center_x) > 150:
            n["vx"] *= -1
        if abs(n["y"] - center_y) > 150:
            n["vy"] *= -1

    for a in nodes:
        for b in nodes:
            dist = math.hypot(a["x"] - b["x"], a["y"] - b["y"])
            if dist < 90:
                pygame.draw.line(
                    screen,
                    GREEN,
                    (a["x"], a["y"]),
                    (b["x"], b["y"]),
                    1,
                )

    for n in nodes:
        pygame.draw.circle(screen, GREEN, (int(n["x"]), int(n["y"])), 2)

    core_label = font_large.render("AUTONOMOUS AI CORE", True, CYAN)
    screen.blit(core_label, (center_x - 160, center_y - 200))

    # ---- ALERT OVERLAY ----
    if alert_active:
        alert_text = font_large.render("ANOMALOUS DATA STREAM", True, RED)
        screen.blit(alert_text, (center_x - 220, 40))

    # ---- BOTTOM STATUS ----
    pygame.draw.line(screen, GRAY, (20, HEIGHT - 40), (WIDTH - 20, HEIGHT - 40), 1)
    status = font_small.render(
        "CORE STATE: ADAPTIVE | THREADS ACTIVE | VOIDFRAME ONLINE",
        True,
        GREEN,
    )
    screen.blit(status, (20, HEIGHT - 30))

    pygame.display.flip()

pygame.quit()
sys.exit()
