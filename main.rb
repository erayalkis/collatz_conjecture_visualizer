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
      puts curr.val
      curr = curr.next
    end
  end

end



def main(n)
  head = Node.new(n)

  curr_node = head
  curr = n
  until curr == 1

    if curr % 2 != 0
      curr = (curr * 3) + 1
      curr_node.next = Node.new(curr)
      curr_node = curr_node.next
    else
      curr = curr / 2
      curr_node.next = Node.new(curr)
      curr_node = curr_node.next
    end
  end

  head
end

result = main(7)

result.iterate_rest