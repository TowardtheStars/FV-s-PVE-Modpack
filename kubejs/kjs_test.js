events.listen("player.chat", function(event){
    if (event.message.charAt(0) == '*' && event.message.length > 1)
    {
        var expression = String(event.message.substring(1))
        log.info("KubeJS expression: " + expression)
        if (event.player.creativeMode)
        {
            var result = eval(expression)
            event.player.tell(result.toString())
            event.cancel()
        }
    }
})