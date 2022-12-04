use std::fs::File;
use std::io::{BufRead, BufReader, Lines, Result};
use std::path::Path;

pub fn read_file<P>(file_path: P) -> Result<Lines<BufReader<File>>> where P: AsRef<Path>{
    let file = File::open(file_path)?;
    Ok(BufReader::new(file).lines())
}

pub fn read_lines<P>(file_path: P) -> Vec<String> where P: AsRef<Path> {
    let file = File::open(file_path).unwrap();
    return BufReader::new(file).lines()
        .map(|l| l.unwrap())
        .collect();
}