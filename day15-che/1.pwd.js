Java.perform(function () {
    // 包.类
    var UserModel = Java.use("com.che168.autotradercloud.user.model.UserModel");
    var SecurityUtil = Java.use("com.autohome.ahkit.utils.SecurityUtil");

    UserModel.loginByPassword.implementation = function (str, str2, str3, str4, str5, responseCallback) {
        console.log("-----------------------请求来了-----------------------");
        console.log("用户名", str2);
        console.log("密码", str3);
        var res = this.loginByPassword(str, str2, str3, str4, str5, responseCallback);
        return res;
    };

    SecurityUtil.encodeMD5.implementation = function (str) {
        console.log("明文：", str);
        var res = this.encodeMD5(str);
        console.log("md5加密结果=", res);
        return res;
    }
});