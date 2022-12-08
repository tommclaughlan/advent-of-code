use std::collections::HashMap;
use aoc_2022_common::read_lines;

fn main() {
    let part1_result = part1("../inputs/day7.txt");
    let part2_result = part2("../inputs/day7.txt");

    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

struct Directory {
    files: Vec<i32>,
    directories: HashMap<String, Directory>
}

trait Size {
    fn get_size(&self) -> i32;
}

impl Size for Directory {
    fn get_size(&self) -> i32 {
        let mut size = 0;
        for file in self.files.iter() {
            size += file;
        }
        for dir in self.directories.values().into_iter() {
            size += dir.get_size();
        }
        
        return size;
    }
}

fn part1(filename: &str) -> i32 {
    let lines = read_lines(filename);
    
    let root = parse_tree(lines);
    
    let sum = sum_dirs_at_most(&root, 100_000, 0);
    
    return sum;
}

fn part2(filename: &str) -> i32 {
    let total_space = 70_000_000;
    let required_space = 30_000_000;
    
    let lines = read_lines(filename);

    let root = parse_tree(lines);
    
    let free_space = total_space - root.get_size();
    let target_to_free = required_space - free_space;    

    let sum = find_smallest_dir_above(&root, target_to_free, total_space);

    return sum;
}

fn sum_dirs_at_most(current: &Directory, max_size: i32, mut sum: i32) -> i32 {
    if current.get_size() < max_size {
        sum += current.get_size();
    }
    
    let children = current.directories.values();
    
    for dir in children {
        sum = sum_dirs_at_most(dir, max_size, sum);
    }

    return sum;
}

fn find_smallest_dir_above(current: &Directory, req_size: i32, mut smallest: i32) -> i32 {
    let size = current.get_size();
    if size < smallest && size > req_size {
        smallest = current.get_size();
    }

    let children = current.directories.values();

    for dir in children {
        smallest = find_smallest_dir_above(dir, req_size, smallest);
    }

    return smallest;
}

fn parse_tree(lines: Vec<String>) -> Directory {
    let mut current_path: Vec<String> = Vec::new();
    let mut root = Directory {
        files: vec![],
        directories: Default::default()
    };

    let mut current = &mut root;

    for line in lines {
        let parts: Vec<&str> = line.split(" ").collect();
        if parts[0] == "$" {
            if parts[1] == "cd" {
                let target = parts[2].to_string();
                if target == "/" {
                    current_path.clear();
                    current_path.push("/root".parse().unwrap());
                } else if target == ".." {
                    current_path.pop();
                } else {
                    current_path.push(target);
                }

                for path in current_path.iter() {
                    if path == "/root" {
                        current = &mut root;
                    } else {
                        current = current.directories.get_mut(path).unwrap();
                    }
                }
            }
        } else if parts[0] == "dir" {
            let dir_name = parts[1];
            current.directories.insert(dir_name.parse().unwrap(), Directory {
                files: vec![],
                directories: Default::default()
            });
        } else {
            let file_size: i32 = parts[0].parse().unwrap();
            current.files.push(file_size);
        }
    }
    return root;
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("../inputs/test_input/day7.txt"), 95437);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../inputs/test_input/day7.txt"), 24933642);
    }

    #[test]
    fn answer_part1() {
        assert_eq!(part1("../inputs/day7.txt"), 1444896);
    }

    #[test]
    fn answer_part2() {
        assert_eq!(part2("../inputs/day7.txt"), 404395);
    }
}