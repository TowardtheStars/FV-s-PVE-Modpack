
val SArray = [
    "Iron",
    "Gold",
    "Abyssalnite",
    "Silver",
    "Copper",
    "Tin",
    "Aluminum", "Aluminium",
    "Lead",
    "Nickel",
    "Uranium",
    "Cobalt",
    "Ardite"
] as string[];


for metalName in SArray {
    if ((oreDict has "ingot" ~ metalName) & (oreDict has "nugget" ~ metalName) & (oreDict has "ore" ~ metalName)) {
        furnace.remove(oreDict.get("ingot" ~ metalName), oreDict.get("ore" ~ metalName));
        furnace.addRecipe(oreDict.get("nugget" ~ metalName).firstItem * 3, oreDict.get("ore" ~ metalName), 0.4);
        print("Successfully altered furnace recipe for metal: " ~ metalName);
    }
}