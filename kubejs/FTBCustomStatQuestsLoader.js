
// Quest for player place block counts

var quests = [
    {
        event_listen : "block.place",
        quest_id : "b77a0f6a",
        maxProgress : 100000,
    },
    {
        event_listen : "item.right_click",
        quest_id : "fd6f2fec",
        maxProgress : 1024,
        condition : function (event){
            return event.item.item.registryName=='tconstruct:throwball' && event.item.data == 1;
        }
    }
];


quests.forEach(
    function (entry){
        if (! entry.condition){
            entry.condition = function (event){return true;};
        }
        events.listen("ftbquests.custom_task." + entry.quest_id, function(event){
            event.maxProgress = entry.maxProgress
        });
        log.info("ftbquests.custom_task event triggered for quest id: "+ entry.quest_id)
    }
);

quests.forEach(
    function (entry){
        events.listen(entry.event_listen, function(event){
            if(entry.condition(event) && event.player) {
                event.player.data.ftbquests.addProgress(entry.quest_id, 1);
            }
        });
    }
)

