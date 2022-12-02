use std::path::Path;
use aoc_2022_common::*;

fn main() {
    let part1_result = part1("../inputs/day1.txt");
    let part2_result = part2("../inputs/day1.txt");

    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

fn part1(filename: &str) -> i32 {
    let elves = count_elves(filename);

    return elves.iter().copied().max().unwrap();
}

fn part2(filename: &str) -> i32 {
    let mut elves = count_elves(filename);
    elves.sort();
    elves.reverse();

    let mut sum = 0;

    for i in 0..=2 {
        sum += elves[i];
    }

    return sum;
}

fn count_elves<P>(filename: P) -> Vec<i32> where P: AsRef<Path> {
    let mut elves = Vec::new();
    let mut last_elf = 0;

    if let Ok(lines) = read_file(filename) {
        for line in lines {
            if let Ok(value) = line {
                if value.is_empty() {
                    elves.push(last_elf);
                    last_elf = 0;
                } else {
                    last_elf += value.parse::<i32>().unwrap();
                }
            }
        }
    }
    if last_elf > 0 {
        elves.push(last_elf);
    }

    return elves;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("../inputs/test_input/day1.txt"), 24000);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../inputs/test_input/day1.txt"), 45000);
    }
}