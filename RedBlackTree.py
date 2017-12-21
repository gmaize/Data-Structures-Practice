class RedBlackNode:
	def __init__(self, key, value, isRed=True):
		self.key = key
		self.value = value
		self.isRed = isRed
		self.left = None
		self.right = None
		self.parent = None

class RedBlackTree:
	def __init__(self):
		self.root = None

	def redBlackTreeInsert(self, key, value):
		newNode = RedBlackNode(key, value, True)
		curNode = self.root
		parentNode = None
		while curNode is not None:
			parentNode = curNode
			if newNode.value <= curNode.value:
				curNode = curNode.left
			else:
				curNode = curNode.right
		if parentNode is None: #tree was empty
			self.root = newNode
		elif newNode.value <= parentNode.value:
			parentNode.left = newNode
		else:
			parentNode.right = newNode
		newNode.parent = parentNode
		self.redBlackTreeFixup(newNode)

	def redBlackTreeFixup(self, node):
		while node.parent is not None and node.parent.isRed:
			if node.parent is node.parent.parent.left:
				uncle = node.parent.parent.right
			else:
				uncle = node.parent.parent.left
			
			#uncle is red
			if uncle is not None and uncle.isRed:
				node.parent.isRed = False
				uncle.isRed = False
				node.parent.parent.isRed = True
				node = node.parent.parent
				continue
		
			#uncle is black (or non-existent)
			if node.parent is node.parent.parent.left: #left left or left right
				if node is node.parent.right: #left right
					node = node.parent
					self.leftRotate(node)
				node.parent.isRed = False
				node.parent.parent.isRed = True
				self.rightRotate(node.parent.parent)
				
			else: #right right or right left
				if node is node.parent.left: #right left
					node = node.parent
					self.rightRotate(node)
				node.parent.isRed = False
				node.parent.parent.isRed = True
				self.leftRotate(node.parent.parent)
		self.root.isRed = False

	def leftRotate(self, node):
		replacementNode = node.right
		if node is self.root:
			self.root = replacementNode
		elif node is node.parent.left:
			node.parent.left = replacementNode
		elif node is node.parent.right:
			node.parent.right = replacementNode
		node.right = replacementNode.left
		if node.right is not None:
			node.right.parent = node
		replacementNode.left = node
		replacementNode.parent = node.parent
		node.parent = replacementNode

	def rightRotate(self, node):
		replacementNode = node.left
		if node is self.root:
			self.root = replacementNode
		elif node is node.parent.left:
			node.parent.left = replacementNode
		elif node is node.parent.right:
			node.parent.right = replacementNode
		node.left = replacementNode.right
		if node.left is not None:
			node.left.parent = node
		replacementNode.right = node
		replacementNode.parent = node.parent
		node.parent = replacementNode
