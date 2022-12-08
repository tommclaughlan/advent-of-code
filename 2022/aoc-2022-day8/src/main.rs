use aoc_2022_common::read_lines;

fn main() {
    let part1_result = part1("../inputs/day8.txt");
    let part2_result = part2("../inputs/day8.txt");

    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

struct Tree {
    height: i32,
    visible: bool
}

fn part1(filename: &str) -> usize {
    let lines = read_lines(filename);
    
    let mut map = create_map(lines);
    
    let height = map.len();
    let width = map[0].len();

    let mut from_top = vec![0; width];
    let mut from_bottom = vec![0; width];
    let mut from_left = vec![0; height];
    let mut from_right = vec![0; height];
    
    for j in 0..width {
        for i in 0..height {
            if i == 0 || j == 0 || i == height-1 || j == width-1 {
                // edges are always visible
                map[i][j].visible = true;
            }

            if map[i][j].height > from_top[j] {
                map[i][j].visible = true;
                from_top[j] = map[i][j].height;
            }

            if map[i][j].height > from_left[i] {
                map[i][j].visible = true;
                from_left[i] = map[i][j].height;
            }

            if map[i][width - j - 1].height > from_right[i] {
                map[i][width - j - 1].visible = true;
                from_right[i] = map[i][width - j - 1].height;
            }

            if map[height - i - 1][j].height > from_bottom[j] {
                map[height - i - 1][j].visible = true;
                from_bottom[j] = map[height - i - 1][j].height;
            }
        }
    }
    
    let mut sum = 0;
    for i in 0..height {
        sum += map[i].iter().filter(|t| t.visible).count();
    }

    return sum;
}

fn part2(filename: &str) -> usize {
    let lines = read_lines(filename);

    let map = create_map(lines);

    let height = map.len();
    let width = map[0].len();
    
    let mut largest = 0;

    for j in 1..width-1 {
        for i in 1..height-1 {
            let right_score = get_score(j, i, "R", &map);
            let left_score = get_score(j, i, "L", &map);
            let up_score = get_score(j, i, "U", &map);
            let down_score = get_score(j, i, "D", &map);
            
            let total_score = right_score * left_score * up_score * down_score;
            if total_score > largest {
                largest = total_score;
            }
        }
    }

    return largest;
}

fn get_score(x_pos: usize, y_pos: usize, direction: &str, map: &Vec<Vec<Tree>>) -> usize {
    let mut count = 0;
    let current: i32 = map[y_pos][x_pos].height;
    
    if direction == "L" {
        for x in 0..x_pos {
            count += 1;
            if map[y_pos][x_pos - x - 1].height >= current {
                return count;
            }
        }
    } else if direction == "R" {
        for x in (x_pos+1)..map[0].len() {
            count += 1;
            if map[y_pos][x].height >= current {
                return count;
            }
        }
    } else if direction == "U" {
        for y in 0..y_pos {
            count += 1;
            if map[y_pos - y - 1][x_pos].height >= current {
                return count;
            }
        }
    } else if direction == "D" {
        for y in (y_pos+1)..map.len() {
            count += 1;
            if map[y][x_pos].height >= current {
                return count;
            }
        }
    }
    
    return count;
}

fn create_map(lines: Vec<String>) -> Vec<Vec<Tree>> {
    let mut result: Vec<Vec<Tree>> = Vec::new();

    for line in lines {
        let row: Vec<Tree> = line.chars().map(|c| Tree { height: c.to_digit(10).unwrap() as i32, visible: false }).collect();
        result.push(row);
    }
    
    return result;
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("../inputs/test_input/day8.txt"), 21);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("../inputs/test_input/day8.txt"), 8);
    }

    #[test]
    fn answer_part1() {
        assert_eq!(part1("../inputs/day8.txt"), 1676);
    }

    #[test]
    fn answer_part2() {
        assert_eq!(part2("../inputs/day8.txt"), 313200);
    }
}