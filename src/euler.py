class euler_method:
    def __init__(self, derivative):
        self.derivative = derivative
    
    def calc_derivative_at_point(self, point):
        return self.derivative(point)
    
    def calc_estimated_points(self, point = [1, 1], step_size = 0.5, num_steps = 10):
        points = list(point)
        print(points)
        x = points[0]
        y = points[1]
        for i in range(0, num_steps):
            x += step_size
            y += self.derivative(points)
            points = [x, y]
            print(points)
        