import math

from util.runner import Runner


class Day(Runner):
    def parse_input(self):
        line = next(self.input)
        values = line[13:].split(', ')
        xs = values[0][2:].split('..')
        ys = values[1][2:].split('..')

        return [int(v) for v in xs + ys]

    def part1(self):
        target = self.parse_input()
        # at some point we will return to y=0, at which point our velocity will be -(u+1)
        # which will mean if we start with u >= the edge of the target, we will overshoot
        # therefore initial velocity should be abs(y_min) - 1
        u = -target[2] - 1
        # each step we go we reduce velocity by 1, up to 0 at the highest point.
        # working backwards this is 1+2+3...+u-1+u - which simplifies to u(u+1)/2
        return int((u * (u + 1)) / 2)

    def part2(self):
        target = self.parse_input()
        # vx can be at maximum x_max and at minimum the solution for x of x(x+1)/2=x_min
        # which gives 0 = x**2 + x - (2*x_min)
        c = -2 * target[0]
        min_vx = math.ceil(-1 + (math.sqrt(1 ** 2 - (4 * c))) / 2)
        max_vx = target[1]

        # as above, vy can by maximum of -y_min - 1, and minimum of y_min
        max_vy = -target[2] - 1
        min_vy = target[2]

        # maximum time step from t=0 up to vy=0 (2*max_vy + 1), plus additional step to reach target
        t_max = (max_vy * 2) + 2

        velocities = set()

        # there must be a generalisation for this...
        # also could probably pre-compute potential x and y velocities to speed it up but OH WELL
        for vx in range(min_vx, max_vx + 1):
            for vy in range(min_vy, max_vy + 1):
                for t in range(0, t_max):
                    x_pos = get_x_pos(vx, t)
                    y_pos = get_y_pos(vy, t)

                    # if we have gone past either of the edges by this time step, we can give up
                    if x_pos > target[1] or y_pos < target[2]:
                        break

                    if target[0] <= x_pos <= target[1] and target[3] >= y_pos >= target[2]:
                        velocities.add((vx, vy))

        return len(velocities)


def get_x_pos(vx, max_t):
    x_pos = 0
    for t in range(max_t):
        x_pos += vx
        vx = vx - 1 if vx > 0 else 0
    return x_pos


def get_y_pos(vy, max_t):
    y_pos = 0
    for t in range(max_t):
        y_pos += vy
        vy -= 1
    return y_pos


Day(17)
