
// Redeuce furnace output for ores from 1 ingot to 3 nuggets
import crafttweaker.oredict.IOreDict;
var all_entries = oreDict.entries;
for entry in all_entries{
    if entry.name.startsWith("ingot"){
        var metalName = entry.name.substring(5, entry.name.length);
        if ((oreDict has "nugget" ~ metalName) & (oreDict has "ore" ~ metalName)) {
            furnace.remove(oreDict.get("ingot" ~ metalName), oreDict.get("ore" ~ metalName));
            furnace.addRecipe(oreDict.get("nugget" ~ metalName).firstItem * 3, oreDict.get("ore" ~ metalName), 0.4);
            print("Successfully altered furnace recipe for metal: " ~ metalName);
            if (oreDict has "orePoor" ~ metalName) {
                furnace.remove(oreDict.get("nugget" ~ metalName) * 3, oreDict.get("orePoor" ~ metalName));
                furnace.addRecipe(oreDict.get("nugget" ~ metalName).firstItem, oreDict.get("orePoor" ~ metalName), 0.4);
            }
        }
    }
}



