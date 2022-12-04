use std::collections::HashSet;
use aoc_2022_common::read_lines;
use itertools::Itertools;

fn main() {
    let part1_result = part1("../inputs/day3.txt");
    let part2_result = part2("../inputs/day3.txt");

    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

fn part1(filename: &str) -> i32 {
    let mut sum = 0;
    for line in read_lines(filename) {
        let len = line.len();
        let parts: (&str, &str) = line.split_at(len / 2);
        let first_common = parts.0.chars().find(|c| parts.1.contains(*c));
        sum += get_priority(first_common.unwrap());
    }

    return sum;
}

fn part2(filename: &str) -> i32 {
    let mut sum = 0;

    for (a, b, c) in read_lines(filename).iter().tuples() {
        // ALL THE HASH SETS PLEASE
        let set_a: HashSet<char> = a.chars().collect();
        let set_b: HashSet<char>  = b.chars().collect();
        let set_c: HashSet<char>  = c.chars().collect();

        let intersection_ab: HashSet<char> = set_a.intersection(&set_b).cloned().collect();
        let intersection_abc: HashSet<char> = intersection_ab.intersection(&set_c).cloned().collect();
        sum += get_priority(*intersection_abc.iter().next().unwrap());
    }

    return sum;
}

fn get_priority(item: char) -> i32 {
    let val = item as i32;
    if val > 96 {
        return val - 96;
    }
    return val - 38;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("../inputs/test_input/day3.txt"), 157);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../inputs/test_input/day3.txt"), 70);
    }

    #[test]
    fn answer_part1() {
        assert_eq!(part1("../inputs/day3.txt"), 8349);
    }

    #[test]
    fn answer_part2() {
        assert_eq!(part2("../inputs/day3.txt"), 2681);
    }
}