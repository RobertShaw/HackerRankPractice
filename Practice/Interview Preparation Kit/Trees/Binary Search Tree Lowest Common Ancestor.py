def lca(root, v1, v2):
    if root is None:
        return None
    previousCommonNode = root
    v1Node = root
    v2Node = root
    
    while v1Node == v2Node:
        previousCommonNode = v1Node
        if v1 < v1Node.info:
            if v1Node.left:
                v1Node = v1Node.left
            else:
                return None
        elif v1 > v1Node.info:
            if v1Node.right:
                v1Node = v1Node.right
            else:
                return None
        if v2 < v2Node.info:
            if v2Node.left:
                v2Node = v2Node.left
            else:
                return None
        elif v2 > v2Node.info:
            if v2Node.right:
                v2Node = v2Node.right
            else:
                return None
    return previousCommonNode
