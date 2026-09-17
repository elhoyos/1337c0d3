# ruby rover.rb

class Rover
  attr_reader :x, :y

  def initialize(x, y)
    @x = x
    @y = y
  end

  def to_s
    "<Rover x=#{@x} y=#{@y}>"
  end

  def left
    @x -= 1
  end

  def right
    @x += 1
  end

  def up
    @y += 1
  end

  def down
    @y -= 1
  end
end

def test
  puts "Unit testing..."
  tests = [
    {
      init: [1, 1],
      moves: [:left, :right, :up, :down],
      exp: [1, 1],
    },
    {
      init: [0, 0],
      moves: [:left, :left, :left, :down],
      exp: [-3, -1],
    },
    {
      init: [0, 0],
      moves: [:left, :up, :up, :down, :left, :right],
      exp: [-1, 1],
    }
  ]

  tests.each do |test|
    r = Rover.new(*test[:init])
    test[:moves].each do |move|
      case move
      when :left
        r.left
      when :right
        r.right
      when :up
        r.up
      when :down
        r.down
      else
        raise ArgumentError.new("Unsupported move #{move}")
      end
    end

    position = [r.x, r.y]
    if test[:exp] != position
      raise RuntimeError.new("Unexpected rover position, exp=#{test[:exp]}, got=#{position}")
    end
  end

  puts "✅ All tests pass"
end

def print_help
  puts <<~HELP
    To move the rover use:
    - a: LEFT
    - d: RIGHT
    - w: UP
    - s: DOWN

    "h" or "help" to print this help.
    "test" to run the unit tests.
    "q" to exit.
  HELP
end

puts "Welcome to Rover"
print_help

PROMPT = "> "

rover = Rover.new(0, 0)

loop do
  print PROMPT

  begin
    line = gets&.rstrip
  rescue Interrupt
    line = "q" # graceful exit of Ctrl+C 
  end

  break if !line

  case line
  when "a"
    rover.left
  when "d"
    rover.right
  when "w"
    rover.up
  when "s"
    rover.down
  when "test"
    test
    exit(0)
  when "q"
    exit(0)
  else
    print_help
  end

  puts "#> #{rover}"
end