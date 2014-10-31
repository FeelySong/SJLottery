<?php
session_start();
error_reporting(0);
require_once 'conn.php';
if($webzt!='1'){
	echo "<script>window.location='".$gourl."';</script>"; 
	exit;
}

if($_SESSION["sess_uid"]!="" && $_SESSION["username"] !="" && $_SESSION["valid"]!=""){
	$result = mysql_query("select * from ssc_online where valid='".$_SESSION["valid"]."' and username='".$_SESSION["username"] ."'");  
	$total = mysql_num_rows($result);
	if($total!=0){
		echo "<script language=javascript>window.location='default_frame.php';</script>";
		exit;
	}
}

$sql = "select * from ssc_lockip WHERE ip='" . $_SERVER['REMOTE_ADDR'] . "'";
$query = mysql_query($sql);
$dduser = mysql_fetch_array($query);
if(empty($dduser)){
}else{
	echo "<script>window.location='".$gourl."';</script>"; 
	exit;
}

if($_POST['act']=="login"){
$name = trim($_POST['username']);
$vcode = trim($_POST['validcode_source']);

if ($name == "" || $pwd == "") {
	echo "<script language=javascript>window.location='./';</script>";
	exit;
}
if ($vcode != $_SESSION['valicode']) {
	echo "<script language=javascript>alert('验证码不正确，请重新输入');window.location='./';</script>";
	exit;
}

$sql = "select * from ssc_member WHERE username='" . $name . "'";
$query = mysql_query($sql);
$dduser = mysql_fetch_array($query);

if(empty($dduser)){
	echo "<script>window.location='".$gourl."';</script>"; 
	exit;
}else{
	$pwd2 = $dduser['password'];
	$uid = $dduser['id'];
	$pwd= md5($pwd);
	if($pwd == $pwd2){
		if($dduser['zt']==2){
			echo "<script language=javascript>alert('您的帐户被锁定！');window.location='./';</script>";
			exit;
		}
		$_SESSION["sess_uid"] = $uid; 
		$_SESSION["username"] = $name; 
		$_SESSION["level"] = $dduser['level'];
		$_SESSION["valid"] = mt_rand(100000,999999);

		require_once 'ip.php';
		$ip1 = $_SERVER['REMOTE_ADDR'];
		$iplocation = new iplocate();
		$address=$iplocation->getaddress($ip1);
		$iparea = $address['area1'].$address['area2'];

//		$ip1=$_SERVER['REMOTE_ADDR'];
//		$ip2=explode(".",$ip1);
//		if(count($ip2)==4){
//			$ip3=$ip2[0]*256*256*256+$ip2[1]*256*256+$ip2[2]*256+$ip2[3];
						
//			$sql = "select * from ssc_ipdata WHERE StartIP<=".$ip3." and EndIP>=".$ip3."";
//			$quip = mysql_query($sql) or  die("数据库修改出错". mysql_error());
//			$dip = mysql_fetch_array($quip);
//			$iparea = $dip['Country']." ".$dip['Local'];
//		}
		$exe = mysql_query("update ssc_member set lognums=lognums+1, lastip2=lastip, lastarea2=lastarea, lastdate2=lastdate, lastip='".$ip1."', lastarea='".$iparea."', lastdate='".date("Y-m-d H:i:s")."' where username='".$name."'");
		$exe = mysql_query("insert into ssc_memberlogin set uid='".$dduser['id']."', username='".$name."', nickname='".$dduser['nickname']."', loginip='".$ip1."', loginarea='".$iparea."', explorer='".$_SERVER['HTTP_USER_AGENT']."', logindate='".date("Y-m-d H:i:s")."', level='".$dduser['level']."'");
		$exe = mysql_query( "delete from ssc_online where username='".$name."'");
		$exe=mysql_query("delete from ssc_online where username='".$name."'") or  die("数据库修改出错". mysql_error());
		$exe=mysql_query("insert into ssc_online set uid='".$dduser['id']."', username='".$name."', nickname='".$dduser['nickname']."', ip='".$ip1."', explorer='".$_SERVER['HTTP_USER_AGENT']."', addr='".$iparea."', adddate='".date("Y-m-d H:i:s")."', updatedate='".date("Y-m-d H:i:s")."', valid='".$_SESSION["valid"]."', level='".$dduser['level']."'") or  die("数据库修改出错". mysql_error());
		$sqla = "select * from ssc_total WHERE logdate='" . date("Y-m-d") . "'";
		$rsa = mysql_query($sqla);
		$rowa = mysql_fetch_array($rsa);
		if(empty($rowa)){
			$exe=mysql_query("insert into ssc_total set nums".$dduser['level']."=nums".$dduser['level']."+1, logdate='" . date("Y-m-d") . "'") or  die("数据库修改出错". mysql_error());
		}else{
			$exe=mysql_query("update ssc_total set nums".$dduser['level']."=nums".$dduser['level']."+1 where logdate='" . date("Y-m-d") . "'") or  die("数据库修改出错". mysql_error());
		}

//登录充值开始		
$sql_jc = "select * from ssc_huodong where id=3";
$rs_jc = mysql_query($sql_jc);
$row_jc = mysql_fetch_array($rs_jc);	
if($row_jc['kg']==1){
		$sql_login = "select count(id) as tj from ssc_memberlogin WHERE uid='" .$dduser['id']. "' and logindate like'%".date("Y-m-d")."%'";
		$rs_login = mysql_query($sql_login);
		$row_login = mysql_fetch_array($rs_login);	
		
		$sql_loginip= "select count(id) as tjip from ssc_memberlogin WHERE loginip='".$ip1."' and logindate like'%".date("Y-m-d")."%'";
		$rs_loginip = mysql_query($sql_loginip);
		$row_loginip = mysql_fetch_array($rs_loginip);	
	
	if($row_login['tj']==1 && $row_loginip['tjip']==1){

		$sqla = "select * from ssc_member WHERE id='" . $dduser['id'] . "'";
		$rsa = mysql_query($sqla);
		$rowa = mysql_fetch_array($rsa);
		$leftmoney=$rowa['leftmoney'];
		$sqlc = "select * from ssc_record order by id desc limit 1";		//帐变
		$rsc = mysql_query($sqlc);
		$rowc = mysql_fetch_array($rsc);
		$dan1 = sprintf("%07s",strtoupper(base_convert($rowc['id']+1,10,36)));
			$lmoney=$row_jc['jieguo'];
		
			$sqla="insert into ssc_record set dan='".$dan1."', uid='".$dduser['id']."', username='".Get_mname($dduser['id'])."', types='60', smoney=".$lmoney.",leftmoney=leftmoney+".$lmoney.", regtop='".$rowa['regtop']."', regup='".$rowa['regup']."', regfrom='".$rowa['regfrom']."', adddate='".date("Y-m-d H:i:s")."'";
			$exe=mysql_query($sqla) or  die("数据库修改出错6!!!".mysql_error());

			$sqlb="insert into ssc_savelist set uid='".$dduser['id']."', username='".Get_mname($dduser['id'])."', bank='登录充值', bankid='0', cardno='', money=".$lmoney.", sxmoney='0', rmoney=".$lmoney.", adddate='".date("Y-m-d H:i:s")."',zt='1',types='60'";
			$exe=mysql_query($sqlb) or  die("数据库修改出错6!!!".mysql_error());


			$sql="update ssc_member set leftmoney =(leftmoney+".$lmoney."),totalmoney=(totalmoney+".$lmoney.") where id ='".$dduser['id']."'";
			$exe=mysql_query($sql) or  die("数据库修改出错6!!!".mysql_error());		
	}	
}		
//登录充值结束		
		
		echo "<script language=javascript>window.location='default_frame.php';</script>";
		exit;
	}else{
		echo "<script language=javascript>alert('登陆失败，请检查您的帐户名与密码');window.location='./';</script>";
		exit;
	}
    }
}
?>


<html xmlns="http://www.w3.org/1999/xhtml">
<head>
   <meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
   <title>会员登录 - 壹号平台</title>
   <SCRIPT LANGUAGE='JavaScript'>function ResumeError() {return true;} window.onerror = ResumeError; </SCRIPT>
   <script src="js/keyboard/jquery.min.js" type="text/javascript"></script>
   <script src="/Views/Script/uaredirect.js" type="text/javascript"></script>
   <script type="text/javascript">uaredirect("http://new.1hssc.com/Mobile");</script>
   <link href="/1hd/Views/CPSsc/Member/ttn/Noname3.css" rel="stylesheet" type="text/css" />

</head>
    <body class="body_bg">
        <div id="header">
            <div class="wrap">
                <div id="logo" class="l">
                    <h1 class="l"><a target="_self" href=""></a></h1>
                </div>
             
                <div class="nav"><a href="http://www2.53kf.com/webCompany.php?arg=10078894&style=1&language=cn&lytype=0&charset=gbk&kflist=off&kf=&zdkf_type=1&referer=http%3A%2F%2Fbeta.1hssc.com%2FMember%2FSignIn%236d&keyword=&tfrom=1&tpl=crystal_blue" target="_blank" style="background: url(/Views/CPSsc/Images/ptkefu.png) no-repeat top;" class="w_right"></a></div>
            </div>
        </div>
            <div class="login_wrap">
                <div class="wrap" id="main">
                    <div class="login_pic010">
                    </div>
                    <div class="login_erwm">
                        <div class="login-erwmdl">
                              <p class="erwn"><img style="width:104px; height:104px;" src="1hd/Views/CPSsc/Images/erwm.png" /></p>
                              <p class="ora">手机扫描，快速登录</p>
                              <p class="gray">请使用客户端扫描</p>
                        </div>
                    </div>
                    <div class="login_box">
                        <div class="lg_box">
                            <div class="top_b"></div>
                            <div class="bg">
                                <div class="content">
                                    <h3 class="login_t">用户登录</h3>
                                    <div class="reg_lnk"></div>
                                    <div class="phone_login">
                                    </div>
                                    <div class="other_login"></div>
                                        
                                    <div class="tip_box">
                                        <div  style="display: none;" id="dis" class="cnt">
                                        </div>
                                    </div>
                                      <ul class="login_m">
                                          <form action="default_frame.php" style="margin: 0px; padding: 0px"  id="login" name="login" method="POST">
                                              <li>
                                                  <span class="sp_l">用户名</span>
                                                  <span class="sp_r">
                                                      <input type="text" id="us" placeholder="邮箱/用户名" name="username" class="login_input" value="">
                                                  </span>
                                              </li>                                 
                                              <li>
                                                  <span class="sp_l">密&nbsp;&nbsp;&nbsp;码</span>
                                                  <span class="sp_r">
                                                    <input type="password" id="ps" name="password" class="login_input" value="">
                                                  </span>
                                              </li>
                                              <li class="login_yzm">
                                                  <span class="sp_l">验证码</span>
                                                  <span class="sp_r">
                                                    <input type="text"  maxlength="4" style="ime-mode: disabled;" class="login_code" name="validcode_source" id="vs">
                                                    <span id="verifystatus" class=""></span>                              
                                                    <span class="veid" id="veid">
                                                        <img width="90" height="35" onclick="this.src='ValiCode_New.php?';return false;" src="ValiCode_New.php"  style="cursor:pointer;" title="重新获取验证码">
                                                    </span>
                                                    <a onclick="displayyz();return false;" title="重新获取验证码" href="javascript:;" class="fresh">重新获取验证码</a> 
                                                  </span>
                                              </li>
                                              <li>
                                                  <span class="sp_l">&nbsp;</span>
                                                  <input type="submit" onclick="return LoginNow()" value="" style="float:left;color: rgb(255, 255, 255); background-position: 0px 0px; " onmouseout="this.style.backgroundPosition='0px 0px';" onmouseover="this.style.backgroundPosition='0px -45px';this.style.color='#FFFFFF';" class="login_btn">
                                                      <span id="fp"><a href="1hd/Member/FindType" style="cursor:pointer">忘记密码？</a></span>
                                                  <input type="button" onclick="checkRegist()" id="btnRegist"   style="float:left;color: rgb(255, 255, 255); background-position: 0px 0px; " onmouseout="this.style.backgroundPosition='0px 0px';" class="regist_btn">
                                              </li>
                                              <li style="text-align: center;">&nbsp;</li>
                                          </form>
                                      </ul>
                                      <div class="login-ptn">    
                                  </div>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
              </div>
        <div class="footer" style="border:0px;border-top: 2px solid #3C7EC8;">
            
            <div class="copy_new">
                <div class="security">
                    <a class="security07" target="_blank" title="qualys secure" href="/Views/about/1.htm">&nbsp;</a>
                    <a class="security11" target="_blank" title="norton" href="http://www.symantec.com/en/au/index.jsp">&nbsp;</a>
                    <a class="security10" target="_blank" title="安全联盟标识">&nbsp;</a>
                    <a rel="nofollow" class="security04" title="公共信息网络安全监察" href="/Views/about/4.htm">公共信息网<br>络安全监察</a>
                    <a rel="nofollow" class="security05" target="_blank" href="/Views/about/5.htm">中国信用企业<br><span>点击查验电子证书</span></a>
                    <a rel="nofollow" class="security03" target="_blank" href="/Views/about/6.htm">网上交易<br>保障中心</a>
                    <a rel="nofollow" class="security09" target="_blank" href="/Views/about/7.htm">工商网监<br>电子标识</a>
                    <a rel="nofollow" class="security08" target="_blank" href="/Views/about/8.htm">&nbsp;</a></div>
            </div>
            <p style="text-align:center;">Copyright ©2005-2014 壹号平台版权所有&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.52fucai.com" target="_blank">联系我们</a></p>
            <p style="text-align: center">备案：<a href="http://www.miitbeian.gov.cn/" target="_blank">京ICP备11007746号-4</a>  增值电信业务经营许可证：京B2-20060298  京网文：[2012]0801-202号</p>
        </div>
        
<script>
   function checkRegist() {
        var HomeUrl = "http://new.1hssc.com";
        window.location.href = HomeUrl + "/Member/Regist?r=" + "";
    }
    $(document).ready(function () {
        $("#btnRegist").hide();
        if ("" != "") {
            $("#fp").hide();
            $("#btnRegist").show();
        }
    }
    
    function displayyz() {
        $("#vs").val("");
        $("#veid").html("<img width='90' height='35' src='ValiCode_New.php" + Math.random() + "' onclick='displayyz()' style='cursor: pointer;' title='重新获取验证码'>");
    }


    function LoginNow(){
    alert('请填写 通行证账号');
    var loginuser = $("#username").val();
    var loginpwd = $("#Password").val();
    var randnum = $("#validcode_source").val();
    if (loginuser == ''){
        alert('请填写 通行证账号');
        return false;
    }
    if (loginpwd == ''){
        alert('请填写 通行证账号');
        return false;
    }
    if (randnum == '') {
        alert('请填写 图片验证码');
        return false;
    }
    var submitvc = $.md5(randnum);
    $("#validcode")[0].value = submitvc;
    document.forms['login'].submit();
    return true;
    }
</script>
    </body>
<?php echo $count ?>
</html>

