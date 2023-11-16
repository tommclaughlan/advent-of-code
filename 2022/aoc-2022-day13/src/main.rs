use aoc_2022_common::read_lines;

fn main() {
    let part1_result = part1("../inputs/day14.txt");
    let part2_result = part2("../inputs/day14.txt");

    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

fn part1(filename: &str) -> i32 {
    let lines = read_lines(filename);
    return 0;
}

fn part2(filename: &str) -> i32 {
    let lines = read_lines(filename);
    return 0;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("../inputs/test_input/day14.txt"), 0);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../inputs/test_input/day14.txt"), 0);
    }

    #[test]
    fn answer_part1() {
        assert_eq!(part1("../inputs/day14.txt"), 0);
    }

    #[test]
    fn answer_part2() {
        assert_eq!(part2("../inputs/day14.txt"), 0);
    }
}