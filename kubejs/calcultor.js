// calculator

function ishackmsg(msg){
    var f1 = msg.search("event|block|nbt|client|events|facing|fluid|ftbquests|ingredient|item|json|log|mod|oredict|runtime|text|utils|uuid|eval") != -1
    var f2 = false;
    mod.list.forEach(function(element){
        f2 = f2 || (msg.search(element) != -1)
    })
    f2 = f2 || (msg.search("minecraft") != -1);
    return f1 || f2;
}

var json_hack_record = "./local/fvspve/hackers.json"
var hack_quest_id = "bbf177bc"
function reward_hacker(player){
    player.tell("§cYou dirty hacker!")
    player.tell("§cYou are going to have a BAD time!")
    if (player.server)
    {
        if (mod.isLoaded("ftbquests"))
            player.data.ftbquests.addProgress(hack_quest_id, 1)
        utils.server.runCommand(command("effect", player.name, "minecraft:mining_fatigue", 30, 3))
        utils.server.runCommand(command("effect", player.name, "minecraft:weakness", 30, 3))
        utils.server.runCommand(command("effect", player.name, "minecraft:slowness", 30, 10))
        utils.server.runCommand(command("effect", player.name, "minecraft:nausea"), 30, 1)
    }
}

events.listen("player.chat", function (event){
    if (event.message.charAt(0) == '=' && event.message.length > 1)
    {
        var expression = String(event.message.substring(1))
        log.info("Calculator expression: " + expression)
        log.info("Search result: " + expression.search("[a-df-zA-DF-Z\^\$\#\@\[\{\}\"\'\/:;]"))
        if (expression.search("[a-df-zA-DF-Z\^\$\#\@\[\{\}\"\'\/:;]") != -1)
        {
            if (ishackmsg(expression))
            {
                reward_hacker(event.player)
            }else{
                event.player.tell("Invalid algebra expression")
            }
        }else{
            var result = eval(expression)
            event.player.tell(result)
        }
        event.cancel()
    }
    
})
