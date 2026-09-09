# ruby -r ./fizzbuzz.rb -e test

# @param {Integer} n
# @return {String[]}
def fizz_buzz(n)
    (1..n).map do
        case 
        when _1 % 3 == 0 && _1 % 5 == 0
            "FizzBuzz"
        when _1 % 3 == 0
            "Fizz"
        when _1 % 5 == 0
            "Buzz"
        else
            "#{_1}"
        end
    end
end

def test
  tests = [
    {    
      expect: ["1","2","Fizz"],
      given: 3,
    },

    {  
      expect: ["1","2","Fizz","4","Buzz"],
      given: 5,
    },

    {  
      expect: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"],
      given: 15,
    },
  ]

  tests.each do |test|
    given = test[:given]
    expect = test[:expect]
    res = fizz_buzz(given)
    if expect != res
      raise StandardError.new("Unexpected result, want=#{expect}, got=#{res}")
    end
  end
end