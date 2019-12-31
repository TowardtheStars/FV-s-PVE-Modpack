
var update_tick = 600;

events.listen("player.tick", function(event){
    if (event.player && event.player.server && event.player.ticksExisted % update_tick === 0)
    {
        if (!event.player.data.gamestages.has("beginner"))
        {
            event.player.server.runCommand("/xp -100l " + event.player.name)
            if (mod.isLoaded("scalinghealth"))
            {
                event.player.server.runCommand("/scalinghealth difficulty set 0 " + event.player.name)
            }
            if (mod.isLoaded("ftbutilities"))
            {
                event.player.server.runCommand("/heal " + event.player.name)
            }
        }
    }
})