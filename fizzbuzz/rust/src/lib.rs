const FIZZ_BUZZ_MAP: [(u64, &str); 2] = [(3, "Fizz"), (5, "Buzz")];

pub fn fizzbuzz(n: u64) -> Vec<String> {
    let mut answer: Vec<String> = vec![];

    for i in 1..=n {
        let mut ret = String::new();
        for (k, fizz_or_buzz) in &FIZZ_BUZZ_MAP {
            if i % k == 0 {
                ret.push_str(fizz_or_buzz)
            }
        }

        if ret.is_empty() {
            answer.push(i.to_string())
        } else {
            answer.push(ret)
        }
    }

    answer
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn with_3() {
        let result = fizzbuzz(3);
        assert_eq!(result, vec!["1", "2", "Fizz"]);
    }

    #[test]
    fn with_5() {
        let result = fizzbuzz(5);
        assert_eq!(result, vec!["1","2","Fizz","4","Buzz"]);
    }

    #[test]
    fn with_15() {
        let result = fizzbuzz(15);
        assert_eq!(result, vec!["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]);
    }
}
