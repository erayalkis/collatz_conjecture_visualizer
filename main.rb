class Node

  attr_accessor :val, :next, :prev
  def initialize(val = 0)
    @val = val
    @next = nil
    @prev = nil 
  end

  def iterate_rest
    curr = self
    puts curr.val
    puts curr.next.val
  end

end



def main(n)
  head = Node.new(n)

  curr = n
  until curr == 1
    puts curr == 1

    if curr % 2 == 0
      curr = (curr * 3) + 1
      head.next = Node.new(curr)
    else
      curr = curr / 2
      head.next = Node.new(curr)
    end
  end

  head
end

result = main(21)

result.iterate_rest