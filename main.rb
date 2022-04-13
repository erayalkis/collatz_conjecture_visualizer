require 'squid'

class Node

  attr_accessor :val, :next, :prev
  def initialize(val = 0)
    @val = val
    @next = nil
    @prev = nil 
  end

  def iterate_rest
    curr = self

    while curr
      if curr.next
        print "(#{curr.val}) -> "
      else
        print "#{curr.val}"
      end
      curr = curr.next
    end

    puts ""
  end

end



def main(n)
  return puts "n can't be 0 or lower (n is #{n})" if n <= 0

  data = {}
  step = 0

  curr = n
  until curr == 1
    if curr % 2 != 0
      data[step] = curr
      curr = (curr * 3) + 1
      data[step] = curr if curr == 1
      step += 1
    else
      data[step] = curr
      curr = curr / 2
      data[step] = curr if curr == 1
      step += 1
    end
  end

  puts "Took #{step} steps to reach loop"

  filename = "./out#{Time.new}"
  Prawn::ManualBuilder::Example.generate(filename) do
    data = data
    chart data
  end
end

puts main(27)
