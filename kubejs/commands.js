
function command(){
    var i = 0;
        var result = "";
        for (i = 0; i < arguments.length; i++)
        {
            result += (arguments[i]).toString();
            result += ' ';
        }
        return "/" + result;
}
