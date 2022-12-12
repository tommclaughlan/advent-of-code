use aoc_2022_common::read_lines;

fn main() {
    let part1_result = part1("../inputs/day12.txt");
    let part2_result = part2("../inputs/day12.txt");

    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

#[derive(Clone, Copy)]
struct Node {
    coords: (usize, usize),
    height: usize,
    value: usize,
    visited: bool
}

fn part1(filename: &str) -> usize {
    let lines = read_lines(filename);
    
    let (grid,  start, end) = parse_grid(lines);

    return find_shortest_path(grid, start.coords, end.coords);
}

fn part2(filename: &str) -> usize {
    let lines = read_lines(filename);
    let (grid, _, end) = parse_grid(lines);

    let mut shortest = 99999;

    let mut starting_points: Vec<(usize, usize)> = Vec::new();

    for row in &grid {
        for col in row {
            if col.height == 1 {
                starting_points.push(col.coords);
            }
        }
    }

    for point in starting_points {
        let path = find_shortest_path(grid.clone(), point, end.coords);
        // path will be zero if we are on an isolated node
        if path < shortest && path > 0 {
            shortest = path;
        }
    }

    return shortest;
}

fn find_shortest_path(mut grid: Vec<Vec<Node>>, start: (usize, usize), end: (usize, usize)) -> usize {
    let mut explore_stack: Vec<(usize, usize)> = Vec::new();

    let mut current = start;

    explore_stack.push(current);

    while explore_stack.len() > 0 {
        current = explore_stack[0];
        let current_value = grid[current.0][current.1].value;

        if current.0 > 0 && can_move(grid[current.0][current.1], grid[current.0 - 1][current.1]) {
            grid[current.0 - 1][current.1].value = current_value + 1;
            if !explore_stack.contains(&grid[current.0 - 1][current.1].coords) {
                explore_stack.push(grid[current.0 - 1][current.1].coords);
            }
        }
        if current.0 < grid.len() - 1 && can_move(grid[current.0][current.1], grid[current.0 + 1][current.1]) {
            grid[current.0 + 1][current.1].value = current_value + 1;
            if !explore_stack.contains(&grid[current.0 + 1][current.1].coords) {
                explore_stack.push(grid[current.0 + 1][current.1].coords);
            }
        }
        if current.1 > 0 && can_move(grid[current.0][current.1], grid[current.0][current.1 - 1]) {
            grid[current.0][current.1 - 1].value = current_value + 1;
            if !explore_stack.contains(&grid[current.0][current.1 - 1].coords) {
                explore_stack.push(grid[current.0][current.1 - 1].coords);
            }
        }
        if current.1 < grid[0].len() - 1 && can_move(grid[current.0][current.1], grid[current.0][current.1 + 1]) {
            grid[current.0][current.1 + 1].value = current_value + 1;
            if !explore_stack.contains(&grid[current.0][current.1 + 1].coords) {
                explore_stack.push(grid[current.0][current.1 + 1].coords);
            }
        }

        explore_stack.remove(0);
        grid[current.0][current.1].visited = true;
    }

    return grid[end.0][end.1].value;
}

fn can_move(from: Node, to: Node) -> bool {
    return (!to.visited) && (to.height as isize - from.height as isize <= 1);
}

fn parse_grid(lines: Vec<String>) -> (Vec<Vec<Node>>, Node, Node) {
    let mut grid: Vec<Vec<Node>> = Vec::new();
    
    let mut start: Node = Node {
        coords: (0, 0),
        height: 0,
        value: 0,
        visited: false,
    };
    let mut end: Node = Node {
        coords: (0, 0),
        height: 0,
        value: 0,
        visited: false,
    };

    for line in lines {
        let mut row: Vec<Node> = Vec::new();
        for char in line.chars() {
            if char == 'S' {
                start = Node {
                    coords: (grid.len(), row.len()),
                    height: 1,
                    value: 0,
                    visited: false
                };
                row.push(start);
            } else if char == 'E' {
                end = Node {
                    coords: (grid.len(), row.len()),
                    height: 26,
                    value: 0,
                    visited: false
                };
                row.push(end);
            } else {
                row.push(Node {
                    coords: (grid.len(), row.len()),
                    height: (char as usize) - 96,
                    value: 0,
                    visited: false
                });
            }
        }
        grid.push(row);
    }

    return (grid, start, end);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("../inputs/test_input/day12.txt"), 31);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../inputs/test_input/day12.txt"), 29);
    }

    #[test]
    fn answer_part1() {
        assert_eq!(part1("../inputs/day12.txt"), 383);
    }

    #[test]
    fn answer_part2() {
        assert_eq!(part2("../inputs/day12.txt"), 377);
    }
}