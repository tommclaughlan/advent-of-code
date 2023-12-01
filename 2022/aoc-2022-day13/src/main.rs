use std::cmp::{min, Ordering};
use std::string::ToString;
use aoc_2022_common::read_lines;

fn main() {
    let part1_result = part1("../inputs/day13.txt");
    let part2_result = part2("../inputs/day13.txt");

    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

#[derive(Clone)]
struct Packet {
    is_list: bool,
    children: Vec<Packet>,
    value: i32
}

trait AsString {
    fn to_string(&self) -> String;
}

impl AsString for Packet {
    fn to_string(&self) -> String {
        if self.is_list {
            return format!("[{}]", self.children.iter().map(|x| x.to_string()).collect::<Vec<String>>().join(", "));
        } else {
            return self.value.to_string();
        }
    }
}

fn part1(filename: &str) -> usize {
    let lines = read_lines(filename);
    
    let mut pairs: Vec<Vec<Packet>> = Vec::new();
    
    let mut current_pair: Vec<Packet> = Vec::new();
    
    for line in lines {
        if line == "" {
            pairs.push(current_pair);
            current_pair = Vec::new();
        } else {
            let mut characters: Vec<char> = line.chars().collect();
            let packet = parse_list(&mut characters);
            current_pair.push(packet);
        }
    }
    
    if current_pair.len() > 0 {
        pairs.push(current_pair);
    }
    
    let mut indices: Vec<usize> = Vec::new();
    
    for i in 0..pairs.len() {
        let left = pairs[i][0].clone();
        let right = pairs[i][1].clone();
        
        let result = compare_packets(left, right);
        if result == Ordering::Less {
            indices.push(i + 1);
        }
    }
    
    return indices.iter().copied().reduce(|a, i| a + i).unwrap();
}

fn part2(filename: &str) -> usize {
    let mut lines = read_lines(filename);
    lines.push("[[2]]".to_string());
    lines.push("[[6]]".to_string());
    
    let mut all_packets: Vec<Packet> = Vec::new();
    
    for line in lines {
        if line != "" {
            let mut characters: Vec<char> = line.chars().collect();
            let packet = parse_list(&mut characters);
            all_packets.push(packet);
        }
    }

    all_packets.sort_by(|l, r| compare_packets(l.clone(), r.clone()));
    let list: Vec<String> = all_packets.iter().map(|a| a.to_string()).collect();
    let start = list.iter().position(|x| x.eq("[[2]]")).unwrap() + 1;
    let end = list.iter().position(|x| x.eq("[[6]]")).unwrap() + 1;
    
    return start * end;
}

fn compare_packets(lhs: Packet, rhs: Packet) -> Ordering {
    if lhs.is_list && rhs.is_list {
        for i in 0..min(lhs.children.len(), rhs.children.len()) {
            let left = lhs.children[i].clone();
            let right = rhs.children[i].clone();
            let result = compare_packets(left, right);
            if result != Ordering::Equal {
                return result;
            }
        }

        if lhs.children.len() < rhs.children.len() {
            return Ordering::Less;
        } else if rhs.children.len() < lhs.children.len() {
            return Ordering::Greater;
        }
        return Ordering::Equal;
    } else if !lhs.is_list && !rhs.is_list {
        if lhs.value < rhs.value {
            return Ordering::Less;
        } else if lhs.value > rhs.value {
            return Ordering::Greater;
        }
        return Ordering::Equal;
    } else {
        // one list, one int
        if lhs.is_list {
            return compare_packets(lhs, Packet {
                is_list: true,
                children: vec![rhs],
                value: 0
            });
        } else {
            return compare_packets(Packet {
                is_list: true,
                children: vec![lhs],
                value: 0
            }, rhs);
        }
    }
}

fn parse_element(to_parse: &mut Vec<char>) -> Packet {
    return if to_parse[0] == '[' {
        parse_list(to_parse)
    } else {
        let digit: i32;
        // urgh hack this cos of 2 digit numbers :(
        // i should do something nicer here but THIS HAS RUINED MY DAY
        if to_parse[1] == ',' || to_parse[1] == ']' {
            digit = to_parse.remove(0).to_digit(10).unwrap() as i32;
        } else {
            digit = format!("{}{}", to_parse.remove(0), to_parse.remove(0)).parse::<i32>().unwrap();
        }
        Packet {
            is_list: false,
            children: vec![],
            value: digit
        }
    }
}

fn parse_list(to_parse: &mut Vec<char>) -> Packet {
    to_parse.remove(0); // leading '['
    let mut packet = Packet {
        is_list: true,
        children: vec![],
        value: 0
    };
    while to_parse[0] != ']' {
        if to_parse[0] == ',' {
            to_parse.remove(0);
        }
        packet.children.push(parse_element(to_parse));
    }
    to_parse.remove(0); // trailing ']'
    
    return packet;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("../inputs/test_input/day13.txt"), 13);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../inputs/test_input/day13.txt"), 140);
    }

    #[test]
    fn answer_part1() {
        assert_eq!(part1("../inputs/day13.txt"), 5330);
    }

    #[test]
    fn answer_part2() {
        assert_eq!(part2("../inputs/day13.txt"), 27648);
    }
}