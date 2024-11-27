//js中的对象是以键值对方式存在的
/*
所有的键都是字符串，值都是任意对象
var 对象名 = {
    属性名: 属性值,
    属性名: 属性值,
    属性名: 属性值
}
*/ 

var user = {
    openid:'dsadsa',
    username:'linx',
    phone:'12112222',
    email:''
}
//修改对象的属性值
user.openid = 'd44444a';
user.username = 'linx';
user.phone = '12346568';
user.email = "1212@qq.com"
//动态添加属性，直接为新的属性赋值即可
user.pet =  ['狗','21212'];
console.log(user)
//删除对象属性
delete user.openid;
console.log(user)
//判断属性是否在对象中
//1. in 可以用于判断对象是否继承与某个父类
//2. hasOwnProperty() 判断是否是该对象自身的属性
console.log('openid' in user);
console.log(user.hasOwnProperty('email'))