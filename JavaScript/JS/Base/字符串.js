// 正常的字符串是用单引号或者双引号包裹使用
console.log('a')
console.log("a")
// 需要特殊处理时使用转义字符 \
console.log('a\nb')
console.log('a\ta')
console.log('\u4e2d') //unicode写法 \u####
console.log('\x41') //Ascll码

//多行字符串
var a = `
hello
world
111
`
console.log(a)

//模版字符串
var name = '张三'
var age = 20
var msg02 = `姓名：${name}, 年龄：${age}`

//字符串长度
var str = 'hello'
console.log(str.length)
//通过下标访问字符串
console.log(str[0])
//字符串的不可变性
str[0] = 'a'
console.log(str)
//大小写转化
str = str.toUpperCase() //大写
console.log(str)
str = str.toLowerCase() //小写
console.log(str)
//字符串截取，substring()，截取范围[)
var linx = 'asdfghjkl'
var linx02 = linx.substring(0, 3) //截取0到3的字符，不包含3
console.log(linx02)