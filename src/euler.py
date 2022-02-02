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
            y += self.derivative(points) * step_size
            points = [x, y]
            print(points)
        
class generalEuler:
    def __init__(self, derivatives):
        self.derivatives = derivatives
        self.dimensions = [key for key in derivatives]

    def calc_derivatives_at_point(self, point):
        answer = {}
        for key in point[1]:
            answer[key] = self.derivatives[key](point[0], point[1])
        return answer

    def calc_new_state(self, point, step_size):
        new_state = {}
        old_state = point[1]
        for dimension in self.dimensions:
            derivative = self.calc_derivatives_at_point(point)[dimension]
            new_state[dimension] = old_state[dimension] + step_size * derivative
        return new_state

    def calc_estimated_points(self, points, step_size = 2, num_steps = 3):
        current_point = points
        point_array = [current_point]
        for i in range(0, num_steps):
            t = current_point[0] + step_size
            state = self.calc_new_state(current_point, step_size)
            current_point = (t, state)
            point_array.append(current_point)
        return point_array

