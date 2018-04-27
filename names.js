// Given: an array containing hashes of names

// Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

// Example:

// list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
// // returns 'Bart, Lisa & Maggie'

// list([ {name: 'Bart'}, {name: 'Lisa'} ])
// // returns 'Bart & Lisa'

// list([ {name: 'Bart'} ])
// // returns 'Bart'

// list([])
// // returns ''
// Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
// 
// list(["sally", "jo", "jade", "jim"])

function list(names){
  //your code here
  let ans = "" ;
  let i = 0;
  if (names.length === 1) {
    return names;
  }
  else if (names.length === 2) {
    return names.join(" & ");
  }
  else{
    while (i < names.length) {
        if (i == names.length - 1) {
            ans += "& " + names[i];
        } else {
            ans += names[i] + " ";
        }
        i++;
        console.log(i);
    }
    return ans;
  }
}