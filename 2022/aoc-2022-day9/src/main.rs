use std::collections::HashSet;
use aoc_2022_common::read_lines;

fn main() {
    let part1_result = part1("../inputs/day9.txt");
    let part2_result = part2("../inputs/day9.txt");

    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

struct Coordinate {
    x: isize,
    y: isize
}

fn part1(filename: &str) -> usize {
    let lines = read_lines(filename);
    let mut visited: HashSet<String> = HashSet::new();
    
    let mut head_pos = Coordinate { x: 0, y: 0 };
    let mut tail_pos = Coordinate { x: 0, y: 0 };

    visited.insert(format!("{},{}", tail_pos.x, tail_pos.y));
    
    for line in lines {
        let parts: Vec<&str> = line.split(" ").collect();
        let direction: &str = parts[0];
        let amount: usize = parts[1].parse().unwrap();
        
        for _ in 0..amount {
            if direction == "R" {
                head_pos.x += 1;
            } else if direction == "L" {
                head_pos.x -= 1;
            } else if direction == "U" {
                head_pos.y -= 1;
            } else if direction == "D" {
                head_pos.y += 1;
            }
            
            let (x, y) = resolve_move(&head_pos, &tail_pos);
            tail_pos.x += x;
            tail_pos.y += y;
            
            visited.insert(format!("{},{}", tail_pos.x, tail_pos.y));
        }
    }
    
    return visited.len();
}

fn part2(filename: &str) -> usize {
    let lines = read_lines(filename);
    let mut visited: HashSet<String> = HashSet::new();

    let mut knots: Vec<Coordinate> = Vec::new();
    for _ in 0..10 {
        knots.push(Coordinate { x: 0, y: 0 });
    }

    visited.insert(format!("{},{}", knots[9].x, knots[9].y));

    for line in lines {
        let parts: Vec<&str> = line.split(" ").collect();
        let direction: &str = parts[0];
        let amount: usize = parts[1].parse().unwrap();

        for _ in 0..amount {
            if direction == "R" {
                knots[0].x += 1;
            } else if direction == "L" {
                knots[0].x -= 1;
            } else if direction == "U" {
                knots[0].y -= 1;
            } else if direction == "D" {
                knots[0].y += 1;
            }
            
            for knot in 0..knots.len() - 1 {
                let (x, y) = resolve_move(&knots[knot], &knots[knot + 1]);
                knots[knot + 1].x += x;
                knots[knot + 1].y += y;
            }

            visited.insert(format!("{},{}", knots[9].x, knots[9].y));
        }
    }

    return visited.len();
}

fn resolve_move(head_pos: &Coordinate, tail_pos: &Coordinate) -> (isize, isize) {
    if (head_pos.y - tail_pos.y).abs() > 1 || (head_pos.x - tail_pos.x).abs() > 1 {
        return ((head_pos.x - tail_pos.x).signum(), (head_pos.y - tail_pos.y).signum())
    }
    
    return (0, 0);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("../inputs/test_input/day9.txt"), 13);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../inputs/test_input/day9.txt"), 36);
    }

    #[test]
    fn answer_part1() {
        assert_eq!(part1("../inputs/day9.txt"), 6284);
    }

    #[test]
    fn answer_part2() {
        assert_eq!(part2("../inputs/day9.txt"), 2661);
    }
}