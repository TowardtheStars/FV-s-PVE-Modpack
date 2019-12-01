// calculator

events.listen("player.chat", function (event){
    if (event.message.charAt(0) == '=' && event.message.length > 1)
    {
        var expression = event.message.substring(1)
        var result = eval(expression)
        // event.server.runCommand(command('tell', event.username, result))
        // log.info(command('tell', event.username, result))
        event.player.tell(result)
        event.cancel()
    }
})
