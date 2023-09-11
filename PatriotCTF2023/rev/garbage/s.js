<script>

function checkName(name){

    var check  = name.split("").reverse().join("");
    return check === "uyjnimda" ? !0 : !1;
}

function checkLength(pwd){
     return (password.length % 6 === 0 )? !0:!1;
    }
function checkValidity(password){
    const arr = Array.from(password).map(ok);
    function ok(e){
        if (e.charCodeAt(0)<= 122 && e.charCodeAt(0) >=97 ){
        return e.charCodeAt(0);
    }}

    let sum = 0;
    for (let i = 0; i < arr.length; i+=6){
        var add = arr[i] & arr[i + 2]; 
        var or = arr[i + 1] | arr[i + 4]; 
        var xor = arr[i + 3] ^ arr[i + 5];
        if (add === 0x60   && or === 0x61   && xor === 0x6) sum += add + or - xor; 
    }
   return  sum === 0xbb ? !0 : !1;
}
</script>
// /check.php 
var btn = document.getElementsByClassName('btn-1')[0];
btn.addEventListener('click',(e)=>{
    e.preventDefault();

    var nam = document.getElementById('name').value;
    if(!(checkName(nam))){         
         alert('Incorrect Name! 😥😥')
    }
    else{
           alert('Correct Name! 🙂🙂')
    }

    var pwd = document.getElementById('password').value;
    if(!checkValidity(pwd) && !checkLength(pwd)){
            alert('Incorrect Password! 😥😥')
    }
    else{
           alert('Correct Password! 🙂🙂')
    }
});
