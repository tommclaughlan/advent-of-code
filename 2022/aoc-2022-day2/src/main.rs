use std::collections::HashMap;
use aoc_2022_common::read_file;

fn main() {
    let part1_result = part1("../inputs/day2.txt");
    let part2_result = part2("../inputs/day2.txt");

    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

fn part1(filename: &str) -> i32 {
    let mut score = 0;
    if let Ok(lines) = read_file(filename) {
        for line in lines {
            if let Ok(value) = line {
                let parts: Vec<&str> = value.split(" ").collect();
                let opponent = parts[0];
                let to_play = parts[1];
                score += shape_score(to_play) + get_score(opponent, to_play);
            }
        }
    }

    return score;
}

fn part2(filename: &str) -> i32 {
    let mut score = 0;
    if let Ok(lines) = read_file(filename) {
        for line in lines {
            if let Ok(value) = line {
                let parts: Vec<&str> = value.split(" ").collect();
                let opponent = parts[0];
                let outcome = parts[1];
                let to_play = get_shape(opponent, outcome);
                score += shape_score(to_play) + outcome_score(outcome);
            }
        }
    }

    return score;
}

fn shape_score(shape: &str) -> i32 {
    return HashMap::from([
        ("X", 1),
        ("Y", 2),
        ("Z", 3)
    ])[shape];
}

fn get_score(a: &str, b: &str) -> i32 {
    let rock_scores = HashMap::from([
        ("X", 3),
        ("Y", 6),
        ("Z", 0)
    ]);
    let paper_scores = HashMap::from([
        ("X", 0),
        ("Y", 3),
        ("Z", 6)
    ]);
    let scissors_scores = HashMap::from([
        ("X", 6),
        ("Y", 0),
        ("Z", 3)
    ]);

    let scores = HashMap::from([
        ("A", rock_scores),
        ("B", paper_scores),
        ("C", scissors_scores)
    ]);

    return scores[a][b];
}

fn outcome_score(outcome: &str) -> i32 {
    return HashMap::from([
        ("X", 0),
        ("Y", 3),
        ("Z", 6)
    ])[outcome];
}

fn get_shape(a: &str, outcome: &str) -> &'static str {
    let losses = HashMap::from([
        ("A", "Z"),
        ("B", "X"),
        ("C", "Y")
    ]);
    let draws = HashMap::from([
        ("A", "X"),
        ("B", "Y"),
        ("C", "Z")
    ]);
    let wins = HashMap::from([
        ("A", "Y"),
        ("B", "Z"),
        ("C", "X")
    ]);

    let scores = HashMap::from([
        ("X", losses),
        ("Y", draws),
        ("Z", wins)
    ]);

    return scores[outcome][a];
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("../inputs/test_input/day2.txt"), 15);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../inputs/test_input/day2.txt"), 12);
    }
}