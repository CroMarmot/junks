'use strict'
var app = angular.module("swda", [])

app.controller("swdaCtrl",function($scope,$timeout){
  $scope.time = ''
  $scope.msg = ''
  $scope.tasklist = [];
  var saveTasklist2Local = function(){
    if(window.localStorage){
      localStorage.setItem('tasklist',JSON.stringify($scope.tasklist));
    }
  }
  $scope.onRemoveClick = function(index){
    $scope.tasklist.splice(index,1);
    saveTasklist2Local();
  }
  $scope.onAddClick = function(){
    $scope.tasklist = $scope.tasklist.concat({
      t:$scope.time,
      m: $scope.msg == ''?"Time out:"+$scope.time:$scope.msg,
      lefttime: null
    })
    $scope.time = ''
    $scope.msg = ''
    saveTasklist2Local();
  }
  $scope.onCheckNotificationAllowedClick = function(){
    if (!("Notification" in window))
      alert("This browser does not support desktop notification");
    else if (Notification.permission === "granted")
      var notification = new Notification("OK Allowed!");
    else if (Notification.permission !== "denied") {
      Notification.requestPermission(function (permission) {
        if (permission === "granted") {
          var notification = new Notification("OK Allowed!");
        }else{
          alert("Unsuccessful!");
        }
      });
    }
  }
  var nextday= function(ti){
    if((new Date(ti.y+"-"+ti.m+"-"+(ti.d+1))).toString() == "Invalid Date"){
      if((new Date(ti.y+"-"+(ti.m+1)+"-1")).toString() == "Invalid Date"){
        ti.y++
        return
      }
      ti.m++
      return
    }
    ti.d++
  }
  // "HH:MM" -> "1 + YYYY-MM-DD HH:MM"
  var formatnextday = function(str){
    var dtmp = new Date()
    var constinfo = {y:dtmp.getFullYear(),m:dtmp.getMonth(),d:dtmp.getDate()}
    if(!str.includes('-')){
      nextday(constinfo)
      return constinfo.y+"-"+(constinfo.m+1)+"-"+constinfo.d+" "+str
    }
    return str
  }
  // "HH:MM" -> "YYYY-MM-DD HH:MM"
  var formatdate = function(str){
    var dtmp = new Date()
    var constinfo = {y:dtmp.getFullYear(),m:dtmp.getMonth(),d:dtmp.getDate()}
    if(!str.includes('-')){
      return constinfo.y+"-"+(constinfo.m+1)+"-"+constinfo.d+" "+str
    }
    return str
  }
  var getformatdiff = function(tdiff){
    if(tdiff < 0) return 'PASSED'
    tdiff = Math.floor(tdiff/1000)
    var d = (tdiff - tdiff % 86400)/86400
    var h = Math.floor((tdiff % 86400) / 3600)
    var m = Math.floor((tdiff % 3600) / 60)
    var s = tdiff % 60
    if(d == 0){
      if(h == 0){
        if(m == 0){
          return s
        }
        return m+" : "+s
      }
      return h+" : "+m+" : "+s
    }
    return d+" day(s) "+h+" : "+m+" : "+s
  }
  var notifyMsg = function(msg){
    // Let's check if the browser supports notifications
    if (!("Notification" in window))
      alert(msg);
    // Let's check whether notification permissions have already been granted
    else if (Notification.permission === "granted")
      // If it's okay let's create a notification
      var notification = new Notification(msg);
    // Otherwise, we need to ask the user for permission
    else if (Notification.permission !== "denied") {
      Notification.requestPermission(function (permission) {
        // If the user accepts, let's create a notification
        if (permission === "granted") {
          var notification = new Notification(msg);
        }
      });
    }
    // At last, if the user has denied notifications, and you
    // want to be respectful there is no need to bother them any more.
  }
  var timeop = function(){
    var dtmp = new Date()
    $scope.date = dtmp.toString()
    var i;
    for(i=0;i<$scope.tasklist.length;i++){
      var calcdiff = ((new Date(formatdate($scope.tasklist[i].t))).getTime()) - (dtmp.getTime())
      if(String(calcdiff) == "NaN"){
        $scope.tasklist[i].lefttime = "Invalid"
        continue;
      }
      if(calcdiff < 0){
        if(calcdiff > -1500){ // time out!
          notifyMsg($scope.tasklist[i].m)
        }
        var newcalcdiff = ((new Date(formatnextday($scope.tasklist[i].t))).getTime()) - (dtmp.getTime())
        if(newcalcdiff >= 0)
          calcdiff = newcalcdiff
      }
      $scope.tasklist[i].lefttime = getformatdiff(calcdiff)
    }
  }
  $scope.onTimeout = function(){
    $timeout(function(){
      timeop()
      $scope.onTimeout()
    },1000)
  }
  var init = function(){
    if(window.localStorage){
      var tl = JSON.parse(localStorage.getItem('tasklist'));
      if(tl != null)
        $scope.tasklist = tl //tl;
      else
        $scope.tasklist = [];
    }
  }
  init();
  $scope.onTimeout()
})
