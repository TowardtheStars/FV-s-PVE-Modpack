#loader contenttweaker

import mods.contenttweaker.Item;
import mods.contenttweaker.VanillaFactory;

var tab = VanillaFactory.createCreativeTab("arsenalexpansion", <minecraft:diamond_sword>);
tab.register();
var test_sword = VanillaFactory.createItem("arsenalexpansion_test_sword");
test_sword.maxStackSize = 1;
test_sword.createCreativeTab = tab;
test_sword.toolClass = "sword";
test_sword.register();

