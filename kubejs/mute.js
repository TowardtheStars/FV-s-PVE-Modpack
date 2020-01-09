

var j = json.read("kubejs/resources/mute.json");
var keyword = j.get('keyword')
var players = j.get('players');

var regex = "(";
if (keyword.size > 0){
    keyword.forEach(function(element) {
        regex = regex + element.asString + "|";
    });

    regex = regex.substring(0, regex.length - 1);
    regex = regex + ')';
}

events.listen("player.chat", function(event){
    if (event.message.search(regex))
    {
        event.cancel();
    }

    if (players.contains(event.player.name)){
        event.cancel();
    }
});
