smallestDistances xs = [dist | (a, b, c) <- xs, let dist = (a^2 + b^2 + c^2)**0.5, dist < 10]
