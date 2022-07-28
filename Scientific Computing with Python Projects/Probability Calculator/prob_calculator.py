import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = [key for key, value in kwargs.items() for _ in range(value)]

    def draw(self, num):
        removed_contents = []
        if num < len(self.contents):
            for _ in range(num):
                removed = self.contents.pop(random.randrange(len(self.contents)))
                removed_contents.append(removed)
            return removed_contents
        else:
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m_count = 0
    exp_balls_list = [key for key, value in expected_balls.items() for _ in range(value)]
    for _ in range(num_experiments):
        exp = copy.deepcopy(hat)
        exp_draw = exp.draw(num_balls_drawn)

        if check_event(exp_draw, exp_balls_list):
            m_count += 1

    return m_count / num_experiments


def check_event(exp_draw, exp_balls_list):
    for ball in exp_balls_list:
        if ball in exp_draw:
            exp_draw.remove(ball)
        else:
            return False
    return True


