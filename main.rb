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

  head = Node.new(n)
  steps = 0

  curr_node = head
  curr = n
  until curr == 1
    if curr % 2 != 0
      curr = (curr * 3) + 1
      curr_node.next = Node.new(curr)
      curr_node = curr_node.next
      steps += 1
    else
      curr = curr / 2
      curr_node.next = Node.new(curr)
      curr_node = curr_node.next
      steps += 1
    end
  end

  puts "Took #{steps} steps to reach loop"
  head
end

main(341).iterate_rest
