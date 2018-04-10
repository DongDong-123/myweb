 //获取form的元素对象
var myForm = document.getElementById('myForm');
var Names = myForm.username; 
var Pwd = myForm.password;
//获取span的对象
var namNotice = document.getElementById('nam-notice');
var pwdNotice = document.getElementById('pwd-notice');
//声明全局变量
var namResult;
var pwdResult;
var namevalue = 0;
var passwdvalue = 0;

//用户名验证
Names.onfocus=function(){
	// console.log('获取焦点');
	namNotice.innerHTML = '请输入6-12位的字母，数字，下划线';
	namNotice.style.color = '#ccc' ;
};
Names.onblur=function(){
	// console.log('失去焦点');
	var nam = Names.value;
	// console.log("nam=",nam);
	var reg = /^\w{6,12}$/;
	namResult = reg.test(nam);  //给全局变量重新赋值
	// console.log("namResult=",namResult);
	if(namResult){
		namNotice.innerHTML = '√ 输入正确';
		namNotice.style.color = 'green';
		// $('#login-but').removeAttr('disabled');
		namevalue=1;

	}else{
		namNotice.innerHTML = 'X 输入错误，请重新输入';
		namNotice.style.color = 'red';
		// $('#login-but').attr('disabled','true');
		passwdvalue = 0;
	};
	if(namevalue+passwdvalue==2){
	$('#login-but').removeAttr('disabled');
	};
};

//密码验证
	Pwd.onfocus=function(){
	// console.log('获取焦点');
	pwdNotice.innerHTML = '请输入6-18位的字母，数字，下划线或字符';
	pwdNotice.style.color = '#ccc';
};
//失去焦点事件
Pwd.onblur=function(){
	// console.log('失去焦点');
	var pwds = Pwd.value;
	// console.log(pwds);
	//设置匹配规则
	var reg = /^(\w|\D){6,18}$/;
	pwdResult = reg.test(pwds);  //给全局变量重新赋值
	// console.log("pwdResult=",pwdResult);
	if(pwdResult==true){
		pwdNotice.innerHTML = '√  输入正确';
		pwdNotice.style.color = 'green';
		passwdvalue=1;

	}else{
		pwdNotice.innerHTML = 'X 格式错误，请重新输入';
		pwdNotice.style.color = 'red';
		passwdvalue=0;
	};
	// 判断用户输入是否有效
	if(namevalue+passwdvalue==2){
	$('#login-but').removeAttr('disabled');
	}
};

