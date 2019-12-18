var array1 = [3 , "foo" , {name "John"} , 5040];

var array2 = [{name "Doe"} , 256 , 100];
Array.prototype.push.apply(array1, array2);
