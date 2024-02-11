import pygame
import pygame.sprite
# ---------------
import random, sys, pymunk
import neat, os, math
import matplotlib.pyplot as plt
# screen
pygame.init()
screenWidth, screenHeight = 700, 700
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
pygame.display.set_caption("Puzzle")
clock = pygame.time.Clock()
pygame.display.flip()
# color
def RANDOM_COLOR():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
# text
class Text:
    def __init__(self, text, font_size, color, position):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.position = position
        self.font = pygame.font.Font(None, self.font_size)  # You can specify a font file or use None for default font
        self.rendered_text = None

    def update(self, new_text):
        self.text = new_text
        self.rendered_text = None  # Clear the rendered text to update it

    def render(self, screen):
        if self.rendered_text is None:
            self.rendered_text = self.font.render(self.text, True, self.color)
        screen.blit(self.rendered_text, self.position)
Information_text = Text("0",30,BLACK,(screenWidth / 2, 0))
# sprites
all_sprites_list = pygame.sprite.Group()
# food
food_list = pygame.sprite.Group()
class Food(pygame.sprite.Sprite):
    def __init__(self,x,y,radius,color):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
# enemie
ememies_list = pygame.sprite.Group()
class Enemies(pygame.sprite.Sprite):
    def __init__(self,x,y,radius, color, speed):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.type = random.randint(0,1)
        self.direction = 0
        self.vel_vector = pygame.math.Vector2(0,-self.speed)
        self.target_point = pygame.math.Vector2(x, y)
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.alive = True

    def move(self):
        direction_vector = self.target_point - pygame.math.Vector2(self.rect.center)
        # Update velocity based on direction towards target point
        if direction_vector.length() > 0:
            direction_vector.normalize_ip()
            self.vel_vector = direction_vector * self.speed
        self.rect.center += self.vel_vector
    
    def hit_object(self):
        if (self.rect.right < 0 or self.rect.left > screenWidth or
                self.rect.bottom < 0 or self.rect.top > screenHeight):
            self.alive = False

    def get_data(self):
        # Return data about the enemy's position, velocity, and radius
        return [self.rect.centerx, self.rect.centery, self.vel_vector.x, self.vel_vector.y, self.radius]

    def give_point(self, target_x, target_y, value):
        # Adjust the target point based on the given value
        self.target_point += pygame.math.Vector2(target_x, target_y) * value

# logic functions
def remove(index):
    ememies_list.remove(index)
    ge.pop(index)
    nets.pop(index)

foodTimer = 0
def addFood():
    global foodTimer
    foodTimer += 1
    if foodTimer % 100 == 0:
        for _ in range(random.randint(1,100)):
            if random.randint(0,1) == 1: 
                color = RED 
            else: 
                color = GREEN
            food = Food(random.randint(0,screenWidth - 5), random.randint(0, screenHeight - 5),5,color)
            food_list.add(food)
            all_sprites_list.add(food)
# loop
generation_counter = 0
def Loop():
    global ememies_list, generation_counter
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        screen.fill(WHITE)
        # food
        addFood()
        for enemy in ememies_list:
            collided_sprites = pygame.sprite.spritecollide(enemy, food_list, False)
            if collided_sprites:
                for collided_sprite in collided_sprites:
                    if collided_sprite in food_list:
                        if enemy.type == 1 and collided_sprite.color == RED or enemy.type == 2 and collided_sprite.color == GREEN:
                            enemy.give_point(collided_sprite.x,collided_sprite.y, 2)
                        else:
                            enemy.give_point(collided_sprite.x,collided_sprite.y, -1)
                        collided_sprite.kill()
        # enemy
        ememies_list = pygame.sprite.Group([enemy for enemy in ememies_list if enemy.alive])
        if len(ememies_list) == 0:
            break

        for i, enemy in enumerate(ememies_list):
            if i < len(ge):
                ge[i].fitness += 1
                if not enemy.alive:
                    remove(i)

        for i, enemy in enumerate(ememies_list):
            if i < len(nets):
                output = nets[i].activate(enemy.get_data())
                enemy.give_point(output[0],output[1], 1)
                if output[0] > 0.7:
                    enemy.direction = 1
                if output[1] > 0.7:
                    enemy.direction = -1
                if output[0] <= 0.7 and output[1] <= 0.7:
                    enemy.direction = 0

        alive_enemies = [enemy for enemy in ememies_list if enemy.alive]
        for enemy in ememies_list:
            enemy.move()
            enemy.hit_object()
        all_sprites_list.draw(screen)
        food_list.draw(screen)
        # update
        pygame.display.flip()
        pygame.display.update()
        clock.tick(64)
# neat
def eval_genomes(genomes,config):
    global ememies_list, ge, nets, generation_counter

    ge = []
    nets = []

    for genome_id, genome in genomes:
        x = random.randint(0, screenWidth - 20)
        y = random.randint(0, screenHeight - 20)
        enemie = Enemies(x,y,10,RANDOM_COLOR(),1)
        ememies_list.add(enemie)
        all_sprites_list.add(enemie)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        ge.append(genome)
        genome.fitness = 0
    
    Loop()
    generation_counter += 1

def run(config_path):
    global pop

    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.run(eval_genomes, 500)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir,r"config-feedforward.txt")
    run(config_path)
