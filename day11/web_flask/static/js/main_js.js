//디지털 시계
setInterval(myWatch, 1000)   //1초 간격으로 시간설정

function myWatch(){
    var date = new Date();   //날짜,시간 객체 생성
    var now = date.toLocaleTimeString();  //시간 출력 객체 생성
    document.getElementById('display').innerHTML = now
}