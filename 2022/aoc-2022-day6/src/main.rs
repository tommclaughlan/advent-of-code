use std::collections::HashSet;
use aoc_2022_common::read_lines;

fn main() {
    let part1_result = part1("../inputs/day6.txt");
    let part2_result = part2("../inputs/day6.txt");

    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

fn part1(filename: &str) -> i32 {
    let line = read_lines(filename).pop().unwrap();

    return find_packet_index(line, 4);
}

fn part2(filename: &str) -> i32 {
    let line = read_lines(filename).pop().unwrap();

    return find_packet_index(line, 14);
}

fn find_packet_index(input: String, packet_length: usize) -> i32 {
    for i in packet_length..input.len() {
        let candidate = &input[(i-packet_length)..i];
        let char_set: HashSet<char> = candidate.chars().collect();
        if char_set.len() == packet_length {
            return i as i32;
        }
    }

    return 0;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("../inputs/test_input/day6.txt"), 7);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../inputs/test_input/day6.txt"), 19);
    }

    #[test]
    fn answer_part1() {
        assert_eq!(part1("../inputs/day6.txt"), 1833);
    }

    #[test]
    fn answer_part2() {
        assert_eq!(part2("../inputs/day6.txt"), 3425);
    }
}