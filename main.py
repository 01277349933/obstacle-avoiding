import random

class ObstacleAvoidingRobot:
    def __init__(self):
        self.direction = "forward"

    def detect_obstacle(self):
        return random.choice([True, False])

    def move(self):
        if self.detect_obstacle():
            self.direction = random.choice(["left", "right"])
            print(f"Obstacle detected! Turning {self.direction}")
        else:
            print("Moving Forward")

    def run(self):
        for _ in range(20):
            self.move()

robot = ObstacleAvoidingRobot()
robot.run()
