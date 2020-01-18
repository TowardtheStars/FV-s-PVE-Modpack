//This file was created via CT-GUI! Editing it is not advised!
//Dont touch me!
//#Remove
furnace.remove(<projectred-core:resource_item>);
#ignoreBracketErrors
recipes.remove(<bonsaitrees:bonsaipot>);
recipes.remove(<iceandfire:sapphire_block>);
recipes.remove(<biomesoplenty:gem_block:6>);
//Dont touch me!
//#Add
furnace.addRecipe(<projectred-core:resource_item>, <minecraftfuture:smoothstone>, 0.0);
recipes.addShaped(<bonsaitrees:bonsaipot>, [[null, null, null],[<minecraft:brick_block>, null, <minecraft:brick_block>], [<minecraft:brick_block>, <minecraft:brick_block>, <minecraft:brick_block>]]);
recipes.addShaped(<iceandfire:sapphire_block>, [[<iceandfire:sapphire_gem>, <iceandfire:sapphire_gem>, <iceandfire:sapphire_gem>],[<iceandfire:sapphire_gem>, <iceandfire:sapphire_gem>, <iceandfire:sapphire_gem>], [<iceandfire:sapphire_gem>, <iceandfire:sapphire_gem>, <iceandfire:sapphire_gem>]]);
recipes.addShaped(<biomesoplenty:gem_block:6>, [[<biomesoplenty:gem:6>, <biomesoplenty:gem:6>, <biomesoplenty:gem:6>],[<biomesoplenty:gem:6>, <biomesoplenty:gem:6>, <biomesoplenty:gem:6>], [<biomesoplenty:gem:6>, <biomesoplenty:gem:6>, <biomesoplenty:gem:6>]]);
//File End
