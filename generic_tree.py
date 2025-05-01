# this program is (Generic Tree) that is used to create a -> (directory tree) 
# where each node can have multiple children.

import os

class Node:
    def __init__(self, name, path,  is_dir=True, size=0):
        self.name = name
        self.path = path
        self.is_dir = is_dir
        self.size = size
        self.children = []
        
        
def create_dir_tree(root_p=None):
    if root_p is None:
        root_p = os.getenv('Location', os.path.expanduser('~/home/pcpath/music'))
        
    if not os.path.exists(root_p):
        print(f'Error: the path {root_p}')
        return None
            
    root_name = os.path.basename(root_p)
    root = Node(root_name, root_p)
        
    def build_tree(node):
        if node.is_dir:
            try:
                entries = os.listdir(node.path)
                entries = [e for e in entries if not e.startswith(".")]
                entries.sort()
                        
            except PermissionError:
                print('file dir is not accesable.')
                return # Skip folder if can not access it.
                    
                    
            for entry in entries:
                exntry_path = os.path.join(node.path, entry)
                is_directory = os.path.isdir(exntry_path)
                size = 0
                if not  is_directory:
                    try: 
                        size = os.path.getsize(exntry_path)
                    except:
                        size = 0
                child_node = Node(entry, exntry_path, is_directory, size)
                node.children.append(child_node)
                build_tree(child_node)
                        
                        
    build_tree(root)
    return root
    
def print_dir_tree(node, indent=" ", show_size=False):
        size_info = f":  ({node.size}, bytes)" if  show_size and not node.is_dir else ""
        # if you want to show folder-only including files
        
        # change in to node.name --> to show the tree by name 
        # inside subdirectory
        
        # change in to node.path + node.name 
        # --> to show the tree by path (folder-only including files)
        
        print(indent + "+_" + node.path + node.name + size_info)
        for child in node.children:
            print_dir_tree(child, indent + "  ", show_size=show_size)
            
            
tree = create_dir_tree()
print_dir_tree(tree, show_size=True)


   
            
        
