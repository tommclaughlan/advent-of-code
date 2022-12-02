use std::io;
use std::fs::File;
use std::io::BufRead;
use std::path::Path;

pub fn read_file<P>(file_path: P) -> io::Result<io::Lines<io::BufReader<File>>> where P: AsRef<Path>{
    let file = File::open(file_path)?;
    Ok(io::BufReader::new(file).lines())
}
