class Link (object):
  def __init__ (self, data = None, next = None):
    self.data = data
    self.next = next
  
  def __str__ (self):
    string = str(self.data)
    return string

class LinkedList (object):
  # initialize the linked list
  def __init__ (self):
    self.first = None

  # get number of links 
  def get_num_links (self):
    counter = 0
    x = self.first

    while x != None:
      counter = counter + 1
      x = x.next
    
    return x

  # add an item at the beginning of the list
  def insert_first (self, data): 
    x = Link(data)
    x.next = self.first
    self.first = x

  # add an item at the end of a list
  def insert_last (self, data): 
    x = Link(data)
    y = self.first
    if (x == None):
      self.first = x
      return

    while y != None:
      y = y.next
      y.next = x

  # add an item in an ordered list in ascending order
  def insert_in_order (self, data): 
    if (self.first == None):
      self.insert_first(data)
      return
    
    if (self.first.data > data):
      self.insert_first(data)
      return
    else:
      new = Link(data)
      x, y = self.first, self.first
      while (x.data < data):
        if (x.next == None):
          self.insert_last(data)
          return
        else:
          y = x
          x = x.next
      y.next = new
      new.next = x

  # search in an unordered list, return None if not found
  def find_unordered (self, data): 
    x = self.first
    if (x == None):
      return None
    else:
      while (x.data != data):
        if (x.next != None):
          x = x.next
        else:
          return None
      return x.data

  # Search in an ordered list, return None if not found
  def find_ordered (self, data): 
    x = self.first
    if (x == None):
      return None
    else:
      while (x.data != data):
        if (x.next == None) or (x.data > data):
          return None
        else:
          x = x.next
      return x.data

  # Delete and return Link from an unordered list or None if not found
  def delete_link (self, data):
    x, y = self.first, self.first
    if (x == None):
      return None

    while (x.data != data):
      if (x.next == None):
        return None
      else: 
        y = x
        x = x.next
      
      if (x == self.first):
        self.first = self.first.next
      else:
        y.next = x.next


      return x

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    x = self.first
    count = 0
    st = ''

    while (x != None):
      count = count + 1
      st = st + str(x.data) + ' '
      x = x.next
      if (count == 10):
        count = 0
        st = st + '\n'

    return st.strip()

  # Copy the contents of a list and return new list
  def copy_list (self):
    x = self.first
    y = LinkedList()
    
    while (x != None):
      y.insert_last(x.data)
      x = x.next
    
    return y
  # Reverse the contents of a list and return new list
  def reverse_list (self): 
    x = self.first
    y = LinkedList()

    while (x != None):
      y.insert_first(x.data)
      x = x.next

    return y
  # Sort the contents of a list in ascending order and return new list
  def sort_list (self):
    x = self.first
    y = LinkedList()

    while (x != None):
      y.insert_in_order(x.data)
      if (x.next != None):
        x = x.next
      else:
        break

    return y

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    x = self.first

    while (x.next != None):
      if (x.data > x.next.data):
        return False
      else:
        x = x.next
    return True

  # Return True if a list is empty or False otherwise
  def is_empty (self): 
    x = self.first
    return x == None

  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other): 
    X = self.first
    y = LinkedList()

    while (x != None):
      y.insert_last(x.data)
      x = x.next

    z = other.first
    while (z != None):
      y.insert_last(z.data)
      z = z.next

    return y

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    num1 = self.get_num_links()
    num2 = other.get_num_links()

    if (num1 != num2):
      return False
    
    if (self.is_empty() and other.is_empty()):
      return True
    
    x = self.first
    y = other.first

    for i in range(num1):
      if (x.data != y.data):
        return False
      x = x.next
      y = y.next
    
    return True


  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self):
    x = self.first
    y = LinkedList()

    no_dupes = []
    while (x != None):
      if (x.data in no_dupes):
        pass
      else:
        no_dupes.append(x.data)
        y.insert_last(x.data)
      x = x.next
    return y

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  test_items = [54, 24, 78, 23, 14, 50, 96, 37, 42, 62]
  test_list = LinkedList()
  print('Test insert_first(): ')
  for x in test_items:
    test_list.insert_first(x)
  print(test_list)
  print()

  # Test method insert_last()
  print('Test insert_last(): ')
  for x in test_items:
    test_list.insert_last(x)
  print(test_list)
  print()

  # Test method insert_in_order()
  print('Test insert_in_order(): ')
  for x in test_items:
    test_list.insert_in_order(x)
  print(test_list)
  print()

  # Test method get_num_links()
  print('Test get_num_links(): ')
  print(test_list.get_num_links())
  print()

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there 
  print('Test find_unordered(data): ')
  print(test_list.find_unordered(50) != None)
  print('Test find_unordered(no data): ')
  print(test_list.find_unordered(50) == None)
  print()

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there 
  print('Test find_ordered(data): ')
  print(test_list.find_ordered(50) != None)
  print('Test find_ordered(no data): ')
  print(test_list.find_ordered(50) == None)
  print()

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 
  test_link_del = LinkedList()
  for x in test_items:
    test_link_del.insert_last(x)

  print('Test delete_link(data): ')
  print(test_list.delete(37) != None)
  print('Test delete_link(no data): ')
  print(test_link.delete(37) == None)
  print()

  # Test method copy_list()
  copy_test = LinkedList()
  for x in test_items:
    copy_test.insert_in_order(x)

  print('Test copy_list(): ')
  print(copy_test.copy_list())
  print()

  # Test method reverse_list()
  rev_test = LinkedList()
  for x in test_items:
    rev_test.insert_in_order(x)
  print('Test reverse_list(): ')

  print(rev_test.reverse_list())
  print()

  # Test method sort_list()
  sort_test = LinkedList()
  for x in test_items:
    sort_test.insert_in_order(x)

  print('Test sort_list(): ')
  print(sort_test.sort_list())
  print()

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  issort_test = LinkedList()
  for x in test_items:
    issort_test.insert_in_order(x)

  print('Test is_sorted(): ')
  print(issort_test.is_sorted() == True)
  print(issort_test.is_sorted() != True)
  print()

  # Test method is_empty()
  emp_test = LinkedList()
  for x in test_items:
    emp_test.insert_in_order(x)

  print('Test is_empty(): ')
  print(emp_test.is_empty())
  print()

  # Test method merge_list()
  print('Test merge_list(): ')
  merge_1 = LinkedList()
  for x in range (20, 30, 2):
    merge_1.insert_last(x)
  merge_2 = LinkedList()
  for x in range (35, 45, 2):
    merge_2.insert_last(x)

  merged = merge_1.merge_list(merge_2)
  print(merged)
  print()

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  print('Test is_equal(): ')
  print(merge_1.isEqual(merge_1)
  print(merge_1.isEqual(merge_2))
  print()

  # Test remove_duplicates()
  print('Test remove_duplicates(): ')
  dupe_test = LinkedList()
  for x in test_items:
    dupe_test.insert_in_order(x)
  dupe_test.insert_first(50)

  print(dupe_test.remove_duplicates())

if __name__ == "__main__":
  main()