use aoc_2022_common::read_lines;

fn main() {
    let part1_result = part1("../inputs/day5.txt");
    let part2_result = part2("../inputs/day5.txt");

    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

fn part1(filename: &str) -> String {
    let lines = read_lines(filename);
    let mut iter = lines.iter();

    let initial: Vec<&String> = iter.by_ref().take_while(|l| !l.is_empty()).collect();
    let moves: Vec<&String> = iter.collect();

    let mut stacks = read_initial_state(initial);
    
    for move_string in moves {
        let (amount, from, to) = parse_move(move_string);
        for _ in 0..amount {
            let i = from as usize;
            let j = to as usize;
            let item = stacks[i].pop().unwrap();
            stacks[j].push(item);
        }
    }

    return stacks.iter().map(|s| s.last().unwrap()).collect();
}

fn part2(filename: &str) -> String {
    let lines = read_lines(filename);
    let mut iter = lines.iter();

    let initial: Vec<&String> = iter.by_ref().take_while(|l| !l.is_empty()).collect();
    let moves: Vec<&String> = iter.collect();

    let mut stacks = read_initial_state(initial);

    for move_string in moves {
        let (amount, from, to) = parse_move(move_string);
        let mut intermediate_stack: Vec<char> = Vec::new();
        let mut target = 0;
        for _ in 0..amount {
            let i = from as usize;
            target = to as usize;
            let item = stacks[i].pop().unwrap();
            intermediate_stack.insert(0, item);
        }
        intermediate_stack.iter().for_each(|thing| stacks[target].push(*thing));
    }

    return stacks.iter().map(|s| s.last().unwrap()).collect();
}

fn read_initial_state(initial: Vec<&String>) -> Vec<Vec<char>> {
    let n_stacks = ((initial[0].len() as f32) / 4.0).ceil() as i32;
    
    let mut stacks: Vec<Vec<char>> = Vec::new();
    for _ in 0..n_stacks {
        stacks.push(Vec::new());
    }

    for line in initial {
        let bytes = line.as_bytes();
        if bytes[1] as char != '1' {
            for _i in 0..n_stacks {
                let index: usize = _i as usize;
                let item = bytes[index * 4 + 1] as char;
                if item != ' ' {
                    stacks[index].insert(0, item);
                }
            }
        }
    }
    
    return stacks;
}

fn parse_move(string: &String) -> (i32, i32, i32) {
    let mut split = string.split(" ");
    let amount = split.nth(1).unwrap().parse::<i32>().unwrap();
    let from = split.nth(1).unwrap().parse::<i32>().unwrap();
    let to = split.nth(1).unwrap().parse::<i32>().unwrap();
    return (amount, from - 1, to - 1);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("../inputs/test_input/day5.txt"), "CMZ");
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../inputs/test_input/day5.txt"), "MCD");
    }

    #[test]
    fn answer_part1() {
        assert_eq!(part1("../inputs/day5.txt"), "CVCWCRTVQ");
    }

    #[test]
    fn answer_part2() {
        assert_eq!(part2("../inputs/day5.txt"), "CNSCZWLVT");
    }
}