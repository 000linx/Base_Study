//js中的数组可以包含任何类型
var arr = [1,2,3.14,'Hello',null,true];
//访问数组的长度
console.log(arr.length)
//修改数组长度
arr.length = 10
console.log(arr) //修改后数组如果数组中的元素不足10个，将用empty表示
console.log(arr.length)
//slice()，截取数组
