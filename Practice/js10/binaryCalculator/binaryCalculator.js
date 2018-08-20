document.getElementById("btn0").onclick = function(){
      document.getElementById("res").innerHTML += "0";
};

document.getElementById("btn1").onclick = function(){
      document.getElementById("res").innerHTML += "1";
};

document.getElementById("btnClr").onclick = function(){
      document.getElementById("res").innerHTML = "";
};

document.getElementById("btnEql").onclick = function(){
    var regex = /([01]+)([+-x*])([01]+)/;
    
    var matches = document.getElementById("res").innerHTML.match(regex);
    var x = parseInt(matches[1],2);
    var y = parseInt(matches[3],2);
    switch(matches[2]){
        case "+":
            document.getElementById("res").innerHTML = (x+y).toString(2);
            break;
        case "-": 
            document.getElementById("res").innerHTML = (x-y).toString(2);
            break;
        case "*": 
            document.getElementById("res").innerHTML = (x*y).toString(2);
            break;
        case "/": 
            document.getElementById("res").innerHTML = Math.floor((x/y)).toString(2);
            break;
    }
};

document.getElementById("btnSum").onclick = function(){
      document.getElementById("res").innerHTML += "+";
};

document.getElementById("btnSub").onclick = function(){
      document.getElementById("res").innerHTML += "-";
};

document.getElementById("btnMul").onclick = function(){
    document.getElementById("res").innerHTML += "*"; 
};
document.getElementById("btnDiv").onclick = function(){
    document.getElementById("res").innerHTML += "/";
};
