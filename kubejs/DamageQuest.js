
events.listen('entity.attack', function(event){
    // player = utils.server.getPlayer(event.source.actual.persistentID)
    player = utils.server.getPlayer(event.entity.persistentID)
    if (player)
    {
        utils.server.tell("Player ["+player.name+"] is attacking!")
        if (event.damage < 666.5 && event.damage > 665.5)
        {
            player.data.ftbquests.addProgress('ab29065d', 1)
        }
    }
})
