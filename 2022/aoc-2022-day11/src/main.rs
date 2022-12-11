use aoc_2022_common::read_lines;

fn main() {
    let part1_result = part1("../inputs/day11.txt");
    let part2_result = part2("../inputs/day11.txt");

    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

struct Monkey {
    items: Vec<i64>,
    divisible_by: i64,
    operation: String,
    true_target: usize,
    false_target: usize,
    inspections: i64
}

fn part1(filename: &str) -> i64 {
    let lines = read_lines(filename);
    
    let monkeys = parse_monkeys(lines);

    return do_monkey_business(monkeys, 20, 3);
}

fn part2(filename: &str) -> i64 {
    let lines = read_lines(filename);

    let monkeys = parse_monkeys(lines);

    return do_monkey_business(monkeys, 10_000, 1);
}

fn do_monkey_business(mut monkeys: Vec<Monkey>, rounds: i64, worry_divisor: i64) -> i64 {
    let common_base = monkeys.iter().fold(1, |base, m| base * m.divisible_by);

    for _ in 0..rounds {
        for i in 0..monkeys.len() {
            for item_i in 0..monkeys[i].items.len() {
                let new_item = inpsect_item(monkeys[i].items[item_i], &monkeys[i].operation, worry_divisor) % common_base;
                monkeys[i].inspections += 1;

                if new_item % monkeys[i].divisible_by == 0 {
                    let target = (&mut monkeys[i]).true_target;
                    monkeys[target].items.push(new_item);
                } else {
                    let target = (&mut monkeys[i]).false_target;
                    monkeys[target].items.push(new_item);
                }
            }
            monkeys[i].items.clear();
        }
    }

    let mut inspections: Vec<i64> = monkeys.iter().map(|m| m.inspections).collect::<Vec<i64>>();
    inspections.sort();
    inspections.reverse();

    return inspections[0] * inspections[1];
}

fn inpsect_item(old: i64, operation: &str, worry_divisor: i64) -> i64 {
    let operation_parts: Vec<&str> = operation.split(" ").collect();
    let operator = operation_parts[1];
    let rhs = if operation_parts[2] == "old" { old } else { operation_parts[2].parse::<i64>().unwrap() };
    
    let mut new = 0;
    
    if operator == "*" {
        new = old * rhs;
    } else if operator == "+" {
        new = old + rhs;
    }
    
    return new / worry_divisor;
}

fn parse_monkeys(lines: Vec<String>) -> Vec<Monkey> {
    let mut monkeys: Vec<Monkey> = Vec::new();

    let mut current_monkey = Monkey {
        items: vec![],
        divisible_by: 0,
        operation: "".to_string(),
        true_target: 0,
        false_target: 0,
        inspections: 0
    };

    for line in lines {
        if line.starts_with("  Starting") {
            let items: Vec<i64> = line.split_at(18).1.split(", ")
                .map(|i| i.parse::<i64>().unwrap()).collect();
            current_monkey.items = items;
        } else if line.starts_with("  Operation") {
            current_monkey.operation = line.split_at(19).1.to_string();
        } else if line.starts_with("  Test") {
            current_monkey.divisible_by = line.split_at(21).1.parse::<i64>().unwrap();
        } else if line.starts_with("    If true") {
            current_monkey.true_target = line.split_at(29).1.parse::<usize>().unwrap();
        } else if line.starts_with("    If false") {
            current_monkey.false_target = line.split_at(30).1.parse::<usize>().unwrap();
        } else if line == "" {
            monkeys.push(current_monkey);
            current_monkey = Monkey {
                items: vec![],
                divisible_by: 0,
                operation: "".to_string(),
                true_target: 0,
                false_target: 0,
                inspections: 0
            };
        }
    }
    
    return monkeys;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("../inputs/test_input/day11.txt"), 10605);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../inputs/test_input/day11.txt"), 2713310158);
    }

    #[test]
    fn answer_part1() {
        assert_eq!(part1("../inputs/day11.txt"), 76728);
    }

    #[test]
    fn answer_part2() {
        assert_eq!(part2("../inputs/day11.txt"), 21553910156);
    }
}