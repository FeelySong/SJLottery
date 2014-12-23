<?php
session_start();
error_reporting(0);
require_once 'conn.php';
$id=$_GET['id'];
$flag=$_POST['flag'];
if($flag=='confirm'){
    $id=$_POST['id'];
    $loginpass=$_POST['loginpass'];
    $validcode=$_POST['validcode'];
    $id=$_POST['id'];
    $username=$_POST['username'];
    $nickname=$_POST['nickname'];
    $qq=$_POST['qq'];
    $pwd=$_POST['pwd'];
    $validcode_source=$_POST['validcode_source'];
    $level=0;//用户级别

    $sql = "select * from ssc_member WHERE username='" . $username . "'";
    $query = mysql_query($sql);
    $dduser = mysql_fetch_array($query);
    if($dduser){
            echo "<script>alert('此账号已经存在，请重新输入');history.go(-1);</script>"; 
            exit;
    }
    if($_SESSION['valicode']==$validcode_source){
            $rebate=Get_member_reg(rebate,$id);
            $stra=explode(";",$rebate);
            for ($i=0; $i<count($stra)-1; $i++) {
                    $strb=explode(",",$stra[$i]);
                    $strb_new=($strb[1]>0.1)?($strb[1]-0.1):(0);;
                    $flevel=($strb_new>$flevel)?($strb_new):($flevel);
                    $rebate_new.=$strb[0].','.$strb_new.','.$strb[2].";";
            }	

            $sql = "insert into ssc_member set username='" . $username . "', password='" . md5($pwd) . "', nickname='" . $nickname . "', regfrom='&" .Get_member_reg(username,$id)."&".Get_member_reg(regfrom,$id). "', regup='" .Get_member_reg(username,$id). "', regtop='" .Get_member_reg(regtop,$id) . "', rebate='" . $rebate_new . "', flevel='" . $flevel . "', level='" . $level . "', regdate='" . date("Y-m-d H:i:s") . "'";
            $exe = mysql_query($sql);


            echo "<script language=javascript>alert('注册成功');window.location='default_frame.php';</script>";
            exit;		
    }else{
             echo("<script>alert('验证码不正确，请重新输入');location='register.php'</script>");
    }
}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<HTML xmlns="http://www.w3.org/1999/xhtml">
<HEAD>
<META http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
<TITLE>用户注册</TITLE>
<SCRIPT LANGUAGE='JavaScript'>function ResumeError() {return true;} window.onerror = ResumeError; </SCRIPT> 
<SCRIPT type="text/javascript" src="js/jquery.js"></SCRIPT>
<SCRIPT type="text/javascript" src="js/jquery.md5.js"></SCRIPT>
<script language="javascript" type="text/javascript" src="js/common.js"></script>
<LINK href="css/login.css" rel="stylesheet" type="text/css" />
</HEAD>
<BODY>
<script type="text/javascript">
if(top.location != self.location) {top.location=self.location;}
$(document).ready(function(){
	$("input.text").focus(
		function(){
			$("input.text").parent().parent().removeClass("inputGreen");
			$(this).parent().parent().addClass("inputGreen");}
	);
	$("input.text").blur(
		function(){ 
			$(this).parent().parent().removeClass("inputGreen");}
	);
	$("#pwd")[0].value = '';
	$("#validcode_source")[0].value = '';
	$("#checkpassword")[0].value = '';
//	$("#validate").attr('src',"/index.php/Public/verify/"+Math.random());
	$("#username").focus();
}); 
function refreshimg(){
document.getElementById("vcsImg").src="ValiCode_new.php?"+  new Date().getTime();
}
function LoginNow() { 
   var username=$("#username").val();
   var nickname=$("#nickname").val();
    var typepw = $("#pwd").val();
    
    var checkpassword=$("#checkpassword").val();
    var randnum = $("#validcode_source").val();
	//$("#pwd")[0].value = '12345678901234567890';

	if( !validateUserName(username) )
	  {
	     alert("登陆帐号 不符合规则，请重新输入");
	     $("#username").focus();
		 return false;
	  }
	  if( !validateNickName(nickname) )
	  {
	  	alert("呢称 不符合规则，请重新输入");
	  	$("#nickname").focus();
		return false;
	  }
	
	 if( !validateUserPss(typepw) )
	 {
	  	alert("为了您的帐号安全,密码必须由数字和字母组成!\n不允许使用纯数字或纯字母做密码,请重新填写!");
	  	$("#pwd").focus();
		return false;
	 }
	 if(checkpassword!=typepw)
	 {
	  	alert("验证密码 不正确，请重新输入");
	  	$("#checkpassword").focus();
		return false;
	 }
	 
    if (randnum == '') {
        alert('请填写 图片验证码');
        return false;
    }
  
   
    $("#loginpass")[0].value = typepw;
   
    document.forms['login'].submit();     
}
</script>

<div id="allbox">
    <div id="header">
       <div id="header_content">
          <div id="header_logo"></div>
          <div id="header_right">
			  <div id="header_tips"><?php echo $webname;?>欢迎您</div>
			  <div id="header_menu" style='margin-left:400px;'></div>
           </div>
         </div>  	
     </div>
     <div id="top_line"></div>
		<div id="reg_content">
			<div id="content_reg_box_top"></div>
			
	<div id="content_reg_box_bottom"></div>
</div>
</div>
</BODY>
</HTML>