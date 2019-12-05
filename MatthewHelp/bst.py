# import Fraction
class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.height = 0
      self.top = None
      self.right = None
      self.left = None

  def __init__(self):
      self.top = None
      self.__root = Binary_Search_Tree.__BST_Node(None)
      self.__root.left = Binary_Search_Tree.__BST_Node(None)
      self.__root.left.height = 0
      self.__root.left.top = self.__root
      self.__root.right = Binary_Search_Tree.__BST_Node(None)
      self.__root.right.height = 0
      self.__root.right.top = self.__root

  def __height_check(self, node):
      if self.__root.value == None:
          print('height is zero becasue no root')
          height = 0
          return height
      elif node.left.value is not None and node.right.value is not None:
          heightL = node.left.height
          heightR = node.right.height
          if heightR > heightL:
              print('heightcheck r > l: ', height)
              height = heightR + 1
              return height
          elif heightR < heightL:
              print('heightcheck r < l: ', height)
              height = heightL + 1
              return height
          elif heightR == heightL:
              print('heightcheck r = l: ', height)
              height = heightR + 1
              return height
      elif node.left.value == None and node.right.value is not None:
          height = 1 + node.left.height
          print('heightcheck, right child is none:', node.height)
          return
      elif node.right.value == None and node.left.value is not None:
          node.height = 1 + node.right.height
          print('heightcheck, left child is none: ', node.height)
          return
      elif node.left.value == None and node.right.value == None:
          node.height = 1
          print('heightcheck children are None: ', node.height)
          return

  def insert_element(self, value):
      self.__insert(value)
      print('next step is balance')
      return self.__balance(value)

  def __insert(self, value):
      if self.__root.value == None:
          self.__root.value = value
      else:
          node = self.__root
          self.__recursive_insert(node, value)

  def __recursive_insert(self, node, value):
      if value < node.value:
          node = node.left
          if node.value == None:
              node.value = value
              node.left = Binary_Search_Tree.__BST_Node(None)
              node.left.top = node
              node.right = Binary_Search_Tree.__BST_Node(None)
              node.right.top = node
              print('this will output a height check')
              self.__height_check(node)
              self.__height_check(self.__root)
              print('returning node value <')
              return node
          else:
              self.__recursive_insert(node, value)
      elif value > node.value:
          node = node.right
          if node.value == None:
              node.value = value
              node.left = Binary_Search_Tree.__BST_Node(None)
              node.left.top = node
              node.right = Binary_Search_Tree.__BST_Node(None)
              node.right.top = node
              print('this will output a height check')
              self.__height_check(node)
              self.__height_check(self.__root)
              print('returning node value >')
              return node
          else:
              self.__recursive_insert(node, value)
      else:
          raise ValueError
      print('this will output a height check')
      node.height = self.__height_check(node)
      self.__root.height = self.__height_check(self.__root)

  def remove_element(self, value):
      if self.__root.value == value:
          if self.__root.left.value == None and self.__root.right.value == None:
              self.__root.value = None
              return self
          else:
              self.__recursive_remove(value, self.__root)
              # return __balance(value)

      else:
          if value > self.__root.value:
              node = self.__root.right
              self.__recursive_remove(value, node)
              # return __balance(value)

          if value < self.__root.value:
              node = self.__root.left
              self.__recursive_remove(value, node)

  def __recursive_remove(self, value, node):
      if value < node.value:
          if node.left.value is not None:
              node = node.left
              self.__recursive_remove(value, node)
          else:
              node = node.right
              self.__recursive_remove(value, node)

      elif value > node.value:
          if node.right.value is not None:
              node = node.right
              self.__recursive_remove(value, node)

      elif value == node.value:
          if node.left.value == None and node.right.value == None:
              node.value = None
          elif node.left.value == None and node.right.value is not None:
              if node.top.value > node.value:
                  node.right.top = node.top
                  node.top.left = node.right
                  node.value = None
                  node.right = None
                  node.left = None
              else:
                  node.right.top = node.top
                  node.top.right = node.right
                  node.value = None
                  node.right = None
                  node.left = None

          elif node.left.value is not None and node.right.value == None:
              if node.top.value > node.value:
                  node.left.top = node.top
                  node.top.left = node.left
                  node.value = None
                  node.left = None
                  node.right = None
              else:
                  node.left.top = node.top
                  node.top.right = node.left
                  node.value = None
                  node.left = None
                  node.right = None

          elif node.left.value is not None and node.right.value is not None:
              remove_val = self.__find_remove_value(node.right)
              node.value = remove_val
      else:
          raise ValueError

  def __find_remove_value(self, node):
      if node.left.value is not None:
          node = node.left
          return self.__find_remove_value(node)
      elif node.left.value == None and node.right.value is not None:
          nodeval = node.value
          node.right.top = node.top
          node.top.right = node.right
          node.value = None
          node.left = None
          node.right = None
          return nodeval
      elif node.right.value == None:
          nodeval = node.value
          node.value = None
          node.left = node
          node.right = node
          node.top = node
          return nodeval

  def in_order(self):
     if self.__root.value == None:
         return '[ ]'
     array = []
     node = self.__root
     self.__in_order_recursion(node, array)
     return '[ ' + ', '.join(array) + ' ]'

  def __in_order_recursion(self, node, array):
      if node.left.value is not None:
          self.__in_order_recursion(node.left, array)
          array.append(str(node.value))
          if node.right.value is not None:
             node = node.right
             self.__in_order_recursion(node, array)
      else:
          array.append(str(node.value))
          if node.right.value is not None:
              node = node.right
              self.__in_order_recursion(node, array)

  def pre_order(self):
     array = []
     node = self.__root
     self.__pre_order_recursion(node, array)
     return '[ ' + ', '.join(array) + ' ]'

  def __pre_order_recursion(self, node, array):
      if node.left.value is not None:
         array.append(str(node.value))
         self.__pre_order_recursion(node.left, array)
         if node.right.value is not None:
             node = node.right
             self.__pre_order_recursion(node, array)

      else:
          array.append(str(node.value))
          if node.right.value is not None:
              node = node.right
              self.__pre_order_recursion(node, array)

  def __post_order_recursion(self, node, array):
      if node.value is not None:
          self.__post_order_recursion(node.left, array)
          if node.right.value is not None:
              self.__post_order_recursion(node.right, array)
          array.append(str(node.value))

  def post_order(self):
      array = []
      node = self.__root
      self.__post_order_recursion(node, array)
      return '[ ' + ', '.join(array) + ' ]'

  def get_height(self):
      if self.__root.value == None:
          return
      if self.__root.left.value == None and self.__root.right.value == None:
          self.__root.height = 1
          return self.__root.height
      else:
          print('left height: ', self.__root.left.height)
          print('right height: ', self.__root.right.height)
          return self.__root.height

  def __str__(self):
      return self.in_order()

  def __balance(self, t):
      print('root height is:', self.__root.height)
      # 1. Get to the desired node, recursive?
      if t == self.__root.value:
          print('returning t == root')
          return
      elif t < self.__root.value:
          print('<')
          node = self.__root.left
          self.__balance_recur(node, t)
          print(self.__root.value)
      elif t > self.__root.value:
          print('>')
          node = self.__root.right
          self.__balance_recur(node, t)
          print(self.__root.value)


  def __balance_recur(self, node, value):
      if value < node.value:
          print('< recur')
          node = node.left
          self.__balance_recur(node, value)
      elif value > node.value:
          print('> recur')
          node = node.right
          self.__balance_recur(node, value)
      else:
          print('program at hCheck')
          # 2. go to the root of that subtree
          node = node.top
          # print('height of left child: ', node.left.height )
          # print('left child is: ', node.left.value)
          # print('left parent is: ', node.left.top.value)
          # print('height of right child: ', node.right.height )
          # print('right child is: ', node.right.value)
          # print('right parent is: ', node.right.top.value)
          # print('root is: ', self.__root.value)
          # 3. Check height of that subtree
          print(node.left.height)
          print(node.left.height)
          hCheck = node.left.height - node.right.height
          # 4. balance if needed, if not then go to the parent of the root to check next subtree
          if node == self.__root:
              if hCheck < -1:
                  self.__root.right.top = None #Step 1 set the top of the root.right to None, since it is becoming the root
                  self.__root.top = self.__root.right #Step 2 Change the top pointer on the existing root to the new root

                  kValue = self.__root.right.left #Step 3 Create a pointer to the existing left value of the new root
                  self.__root.right.left = self.__root #Step 4 and 5 Change the left of the new root to the existing root
                  self.__root = self.__root.right #Step 6 Change the existing root to be the new roto

                  self.__root.left.right = kValue #Step 7.1 Change the left of the old root to be the old left of the new root
                  kValue.top = self.__root.left #Step 7.2 Change the top of the old left of the new root to be the new root.left
                  print('returning from root < check')
                  return
              elif hCheck > 1:
                  self.__root.left.top = None #Step 1 set the top of the root.right to None, since it is becoming the root
                  self.__root.top = self.__root.left#Step 2 Change the top pointer on the existing root to the new root

                  kValue = self.__root.left.right #Step 3 Create a pointer to the existing left value of the new root
                  self.__root.left.right = self.__root #Step 4 and 5 Change the left of the new root to the existing root
                  self.__root = self.__root.left #Step 6 Change the existing root to be the new roto

                  self.__root.right.left = kValue #Step 7.1 Change the left of the old root to be the old left of the new root
                  kValue.top = self.__root.right #Step 7.2 Change the top of the old left of the new root to be the new root.left
                  print('returning from root > check')
                  return
              else:
                  print('returning from root height check')
                  return
          else:
             if hCheck < -1:
                 node.right.top = None #Step 1 set the top of the root.right to None, since it is becoming the root
                 node.top = node.right #Step 2 Change the top pointer on the existing root to the new root

                 kValue = node.right.left #Step 3 Create a pointer to the existing left value of the new root
                 node.right.left = node #Step 4 and 5 Change the left of the new root to the existing root
                 node = node.right #Step 6 Change the existing root to be the new roto

                 node.left.right = kValue #Step 7.1 Change the left of the old root to be the old left of the new root
                 kValue.top = self.node #Step 7.2 Change the top of the old left of the new root to be the new root.left
                 print('returning from node < check')
                 return
             elif hCheck > 1:
                 node.left.top = None #Step 1 set the top of the root.right to None, since it is becoming the root
                 node.top = node.left #Step 2 Change the top pointer on the existing root to the new root

                 kValue = node.left.right #Step 3 Create a pointer to the existing left value of the new root
                 node.left.right = node #Step 4 and 5 Change the left of the new root to the existing root
                 node = node.left #Step 6 Change the existing root to be the new roto

                 node.right.left = kValue #Step 7.1 Change the left of the old root to be the old left of the new root
                 kValue.top = self.node #Step 7.2 Change the top of the old left of the new root to be the new root.left
                 print('returning from node > check')
                 return
             else:
                 print('node.top is: ', node.top.value)
                 print('returning from node check')
                 return

if __name__ == '__main__':
    trees = Binary_Search_Tree()
    trees.insert_element(10)
    print(str(trees))
    print('height at root:',(trees.get_height()))
    trees.insert_element(9)
    print('height with 2:', (trees.get_height()))
    print(str(trees))
    # trees.insert_element(8)
    # print(trees.get_height())
    # trees.insert_element(10)
    # trees.insert_element(15)
    # trees.insert_element(5)
    # trees.insert_element(7)
    # trees.insert_element(12)
    # trees.insert_element(6)
    # trees.insert_element(9)
    # print(str(trees))
    # trees.remove_element(10)
    # #print(trees.get_height())
    # print(str(trees))
