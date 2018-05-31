// Print out all the node data squared

// search down the tree
// grab the data from each node

// creating Nodes for our trees
function Node(val){
  this.value = val;
  this.left = null;
  this.right = null;
}


function BinarySearchTree(){
  this.root = null;
}

BinarySearchTree.prototype.walk = function() {
    let identity = (a) => a;

    function _walk(node, func=identity, data = []){

        if (node !== null){
            data.push(node.value);
            _walk(node.left,identity, data);
            _walk(node.right, identity, data);
        }
        return data;
    }
    return _walk(this.root)
}

BinarySearchTree.prototype.push = function(val){
   var root = this.root;

   if(!root){
      this.root = new Node(val);
      return;
   }

   var currentNode = root;
   var newNode = new Node(val);

   while(currentNode){
      if(val < currentNode.value){
          if(!currentNode.left){
             currentNode.left = newNode;
             break;
          }
          else{
             currentNode = currentNode.left;
        }
     }
     else{
         if(!currentNode.right){
            currentNode.right = newNode;
            break;
         }
         else{
            currentNode = currentNode.right;
         }
     }
  }

}


var bst = new BinarySearchTree();
bst.push(3);
bst.push(2);
bst.push(4);
bst.push(1);
bst.push(5);


// Push entire Node instead of just pushing value function call as the argument to push