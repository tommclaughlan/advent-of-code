use std::collections::HashSet;
use aoc_2022_common::read_lines;

fn main() {
    let part1_result = part1("../inputs/day10.txt");
    let part2_result = part2("../inputs/day10.txt");

    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

fn part1(filename: &str) -> isize {
    let mut x = 1;
    
    let mut tick = 1;
    
    let mut sum = 0;
    
    for line in read_lines(filename) {
        if line != "noop" {
            let parts: Vec<&str> = line.split(" ").collect();
            if parts[0] == "addx" {
                for _ in 0..2 {
                    if (tick - 20) % 40 == 0 {
                        sum += x * tick;
                    }
                    tick += 1;
                }
                x += parts[1].parse::<isize>().unwrap();
            }
        } else {
            tick += 1;
        }
    }
    
    return sum;
}

fn part2(filename: &str) -> isize {
    let mut x = 1;

    let mut tick = 0;

    for line in read_lines(filename) {
        if line != "noop" {
            let parts: Vec<&str> = line.split(" ").collect();
            if parts[0] == "addx" {
                for _ in 0..2 {
                    draw_pixel(x, tick % 40);
                    tick += 1;
                }
                x += parts[1].parse::<isize>().unwrap();
            }
        } else {
            draw_pixel(x, tick % 40);
            tick += 1;
        }
    }

    return 0;
}

fn draw_pixel(x: isize, pos: isize) {
    if pos == 0 {
        println!();
    }
    if (pos - x).abs() <= 1 {
        print!("##");
    } else {
        print!("  ");
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("../inputs/test_input/day10.txt"), 11340);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../inputs/test_input/day10.txt"), 0);
    }

    #[test]
    fn answer_part1() {
        assert_eq!(part1("../inputs/day10.txt"), 14360);
    }

    #[test]
    fn answer_part2() {
        assert_eq!(part2("../inputs/day10.txt"), 0);
    }
}