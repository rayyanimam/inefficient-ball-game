import pygame, sys, random

pygame.init()

screen_width = 720
screen_height = 960

paddle_x_speed = 0

score = 0

ball_x_speed = random.choice((-7, -6, -5, 5, 6, 7)) # ball can either go left or right
ball_y_speed = random.choice((5, 6, 7))

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("the bouncing ball") # name of the game

fps = pygame.time.Clock() # to cap the fps

text_font = pygame.font.Font(None, 40)
 	
paddle = pygame.Rect(screen_width/2 - 100, 920, 200, 20) # puts the paddle in the center of the x pos

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30) 
ball_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255)) 

score_change = []

y_values = (100,200,300,400,500)

while True:
	score_text = text_font.render(f'score: {score}', False, (255, 255, 255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				paddle_x_speed -= 6
			if event.key == pygame.K_RIGHT:
				paddle_x_speed += 6
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				paddle_x_speed += 6
			if event.key == pygame.K_RIGHT:
				paddle_x_speed -= 6

	if paddle.left <= 20:
		paddle.left = 20
	if paddle.right >= 700:
		paddle.right = 700

	if ball.colliderect(paddle):
		score_change = [0,0,1]
		score += random.choice(score_change)
		ball_color = (random.randint(100,255), random.randint(100,255), random.randint(100,255))
		ball_x_speed *= random.uniform(1, 1.01)
		ball_y_speed *= random.uniform(-1,-1.04)	

	if ball.top <= 0:
		score_change = [0,0,0,1]
		score += random.choice(score_change)
		ball_y_speed *= random.uniform(-1.001,-1.02)
	if ball.left <= 0 or ball.right >= screen_width:
		score_change = [0,0,0,1]
		score += random.choice(score_change)
		ball_x_speed *= random.uniform(-1.001,-1.02)

	if ball.y >= 1100:
		if score >= 3:
			score -= 3
		ball.x = screen_width/2 - 15
		ball.y = random.choice(y_values)
		ball_x_speed *= 0.95
		ball_y_speed *= 0.95

	screen.fill((40,40,40))

	pygame.draw.rect(screen, 'white', paddle)
	pygame.draw.ellipse(screen, ball_color, ball)
	screen.blit(score_text, (screen_width/2 - score_text.get_rect().width/2, 40))
	
	paddle.x += paddle_x_speed

	ball.x += ball_x_speed
	ball.y += ball_y_speed

	pygame.display.update()
	fps.tick(60)
