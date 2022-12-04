use aoc_2022_common::read_lines;
use itertools::Itertools;

fn main() {
    let part1_result = part1("../inputs/day4.txt");
    let part2_result = part2("../inputs/day4.txt");

    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

fn part1(filename: &str) -> i32 {
    let mut sum = 0;
    for line in read_lines(filename) {
        let parts: (&str, &str) = line.split(",").tuples().next().unwrap();
        if either_contains(parts.0, parts.1) {
            sum += 1;
        }
    }

    return sum;
}

fn part2(filename: &str) -> i32 {
    let mut sum = 0;

    for line in read_lines(filename) {
        let parts: (&str, &str) = line.split(",").tuples().next().unwrap();
        if either_overlap(parts.0, parts.1) {
            sum += 1;
        }
    }

    return sum;
}

fn either_contains(a: &str, b: &str) -> bool {
    let a_parts = split_to_pair(a);
    let b_parts = split_to_pair(b);

    if a_parts.0 >= b_parts.0 && a_parts.1 <= b_parts.1 ||
        b_parts.0 >= a_parts.0 && b_parts.1 <= a_parts.1 {
        return true;
    }

    return false;
}

fn either_overlap(a: &str, b: &str) -> bool {
    let a_parts = split_to_pair(a);
    let b_parts = split_to_pair(b);

    if a_parts.1 >= b_parts.0 && a_parts.1 <= b_parts.1 ||
        b_parts.1 >= a_parts.0 && b_parts.1 <= a_parts.1 {
        return true;
    }

    return false;
}

fn split_to_pair(string: &str) -> (i32, i32) {
    string.split("-").map(|p| p.parse::<i32>().unwrap()).tuples().next().unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("../inputs/test_input/day4.txt"), 2);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../inputs/test_input/day4.txt"), 4);
    }

    #[test]
    fn answer_part1() {
        assert_eq!(part1("../inputs/day4.txt"), 560);
    }

    #[test]
    fn answer_part2() {
        assert_eq!(part2("../inputs/day4.txt"), 839);
    }
}