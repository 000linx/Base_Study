//js中的数组可以包含任何类型
var arr = [1,2,3.14,'Hello',null,true];
//访问数组的长度
console.log(arr.length);
//修改数组长度
arr.length = 10;
console.log(arr); //修改后数组如果数组中的元素不足10个，将用empty表示
console.log(arr.length);
//slice()，截取数组[)
var s = arr.slice(1,3);//从索引1开始，到索引3结束，但不包括索引3
console.log(s);
//push()，pop()，push()向数组末尾添加若干元素，pop()则把数组的最后一个元素删除
arr.push('a','b');
console.log(arr);
arr.pop();   
console.log(arr);
//unshift()，shift()，unshift()向数组的头部添加若干元素，shift()则把数组的第一个元素删除
arr.unshift('a','b');
console.log(arr);
arr.shift();
console.log(arr);
//sort()排序，reverse()反转，concat()拼接
console.log(arr.sort());
console.log(arr.reverse());
//concat不会修改原数组，而是返回一个新的数组，通过concat()可以把当前的Array和另一个Array连接起来，并返回一个新的Array
console.log(arr.concat([1,2,3]));
console.log(arr);
//连接符join()，将数组中的元素以特定的符号连接在一起
console.log(arr.join('-'));
