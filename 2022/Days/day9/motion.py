class Motion:
    def __init__(self, direction: str, step: str):
        self.direction = direction
        self.step = int(step)

    def get_direction(self) -> str:
        return self.direction
    
    def get_step(self) -> int:
        return self.step
    
    def get_motion(self) -> tuple[str, int]:
        return (self.direction, self.step)

    def __str__(self) -> str:
        return f"direction: {self.direction} - step: {self.step}"