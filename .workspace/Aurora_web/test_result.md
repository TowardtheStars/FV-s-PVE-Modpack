# KubeJS Document

## Global

|Name|Type
|--|--
| block|BlockUtilities
| client|ClientWrapper
| events|Events
| facing|FacingWrapper
| fluid|FluidWrapper
| ftbquests|FTB Quests Integration
| ingredient|Ingredient Utilities
| item|ItemUtilities
| json|JSONUtilities
| log|LoggerWrapper
| mod|ScriptModData
| nbt|NBTUtilities
| oredict|OreDictionaryUtilities
| runtime|HashMap
| text|TextUtilities
| utils|UtilsWrapper
| uuid|UUIDUtilities

---

## Constants

|Name|Type|Value
|--|--|--
| AIR_BLOCK|BlockAir|minecraft:air
| AIR_ITEM|ItemAir|minecraft:air
| AQUA|TextColor|Enum Constant
| BLACK|TextColor|Enum Constant
| BLUE|TextColor|Enum Constant
| DARK_AQUA|TextColor|Enum Constant
| DARK_BLUE|TextColor|Enum Constant
| DARK_GRAY|TextColor|Enum Constant
| DARK_GREEN|TextColor|Enum Constant
| DARK_PURPLE|TextColor|Enum Constant
| DARK_RED|TextColor|Enum Constant
| GOLD|TextColor|Enum Constant
| GRAY|TextColor|Enum Constant
| GREEN|TextColor|Enum Constant
| HOUR|long|3600000
| LIGHT_PURPLE|TextColor|Enum Constant
| MAIN_HAND|EnumHand|Enum Constant
| MINUTE|long|60000
| OFF_HAND|EnumHand|Enum Constant
| RARITY_COMMON|EnumRarity|Enum Constant
| RARITY_EPIC|EnumRarity|Enum Constant
| RARITY_RARE|EnumRarity|Enum Constant
| RARITY_UNCOMMON|EnumRarity|Enum Constant
| RED|TextColor|Enum Constant
| SECOND|long|1000
| SLOT_CHEST|EntityEquipmentSlot|Enum Constant
| SLOT_FEET|EntityEquipmentSlot|Enum Constant
| SLOT_HEAD|EntityEquipmentSlot|Enum Constant
| SLOT_LEGS|EntityEquipmentSlot|Enum Constant
| SLOT_MAINHAND|EntityEquipmentSlot|Enum Constant
| SLOT_OFFHAND|EntityEquipmentSlot|Enum Constant
| TOOL_TYPE_AXE|String|"axe"
| TOOL_TYPE_PICKAXE|String|"pickaxe"
| TOOL_TYPE_SHOVEL|String|"shovel"
| WHITE|TextColor|Enum Constant
| YELLOW|TextColor|Enum Constant

---

## Event List

|ID|Type|Can cancel|Client|Server
|--|--|--|--|--
|block.break|BlockBreakEvent|Yes|No|Yes
|block.drops|BlockDropsEvent|No|No|Yes
|block.left_click|BlockLeftClickEvent|Yes|Yes|Yes
|block.place|BlockPlaceEvent|Yes|No|Yes
|block.registry|BlockRegistryEvent|No|Yes|Yes
|block.right_click|BlockRightClickEvent|Yes|Yes|Yes
|client.debug_info|DebugInfoEvent|No|Yes|No
|client.logged_in|ClientLoggedInEvent|No|Yes|No
|client.tick|ClientTickEvent|No|Yes|No
|command.registry|CommandRegistryEvent|No|No|Yes
|command.run|CommandEvent|Yes|No|Yes
|entity.attack|LivingEntityAttackEvent|Yes|Yes|Yes
|entity.check_spawn|CheckLivingEntitySpawnEvent|Yes|Yes|Yes
|entity.death|LivingEntityDeathEvent|Yes|Yes|Yes
|entity.drops|LivingEntityDropsEvent|Yes|Yes|Yes
|entity.spawned|EntitySpawnedEvent|Yes|Yes|Yes
|ftbquests.completed|QuestObjectCompletedEvent|No|Yes|Yes
|ftbquests.custom_reward|CustomRewardEvent|Yes|Yes|Yes
|ftbquests.custom_task|CustomTaskEvent|Yes|Yes|Yes
|ftbquests.started|TaskStartedEvent|No|Yes|Yes
|gamestage.added|GameStageEvent|No|Yes|Yes
|gamestage.removed|GameStageEvent|No|Yes|Yes
|item.crafted|ItemCraftedEvent|No|No|Yes
|item.entity_interact|ItemEntityInteractEvent|Yes|Yes|Yes
|item.left_click|ItemLeftClickEvent|No|Yes|No
|item.pickup|ItemPickupEvent|Yes|Yes|Yes
|item.registry|ItemRegistryEvent|No|Yes|Yes
|item.right_click|ItemRightClickEvent|Yes|Yes|Yes
|item.right_click_empty|ItemRightClickEmptyEvent|No|Yes|No
|item.smelted|ItemSmeltedEvent|No|No|Yes
|item.toss|ItemTossEvent|Yes|Yes|Yes
|loaded|Event|No|Yes|Yes
|player.advancement|PlayerAdvancementEvent|No|No|Yes
|player.chat|PlayerChatEvent|Yes|No|Yes
|player.chest.closed|ChestEvent|No|Yes|Yes
|player.chest.opened|ChestEvent|No|Yes|Yes
|player.data_from_client|NetworkEvent|Yes|No|Yes
|player.data_from_server|NetworkEvent|Yes|Yes|No
|player.inventory.changed|InventoryChangedEvent|No|Yes|Yes
|player.inventory.closed|InventoryEvent|No|Yes|Yes
|player.inventory.opened|InventoryEvent|No|Yes|Yes
|player.logged_in|SimplePlayerEvent|No|No|Yes
|player.logged_out|SimplePlayerEvent|No|No|Yes
|player.tick|SimplePlayerEvent|No|No|Yes
|postinit|Event|No|Yes|Yes
|recipes.alloy_smelter|AlloySmelterRecipeEvent|No|Yes|Yes
|recipes.compressor|CompressorRecipeEvent|No|Yes|Yes
|recipes.crafting_table|CraftingTableRecipeEvent|No|Yes|Yes
|recipes.furnace|FurnaceRecipeEvent|No|Yes|Yes
|recipes.pulverizer|PulverizerRecipeEvent|No|Yes|Yes
|recipes.remove.input|RemoveRecipesEvent|No|Yes|Yes
|recipes.remove.output|RemoveRecipesEvent|No|Yes|Yes
|server.load|SimpleServerEvent|No|No|Yes
|server.tick|SimpleServerEvent|No|No|Yes
|server.unload|SimpleServerEvent|No|No|Yes
|unloaded|Event|No|Yes|Yes
|world.explosion.post|ExplosionEventJS$Post|No|No|Yes
|world.explosion.pre|ExplosionEventJS$Pre|Yes|No|Yes
|world.load|SimpleWorldEvent|No|No|Yes
|world.missing_mappings|MissingMappingEvent|No|Yes|Yes
|world.tick|SimpleWorldEvent|No|No|Yes
|world.unload|SimpleWorldEvent|No|No|Yes

---

## BlockUtilities

|Class
|--
|dev.latvian.kubejs.bindings.BlockWrapper

---

|Extends
|--

---

|Fields|Type
|--|--
|  facing|Map\<String, EnumFacing>
|  material|Map\<String, Material>
|  typeList|List\<ID>

---

|Methods|Return Type
|--|--
| custom(BlockPredicate b)|BlockPredicate
| entity(Object o)|BlockEntityPredicate
| getBlock(ID id)|Block
| id(Object arg0, Map\<String, Object> arg1)|BlockIDPredicate
| id(Object o)|BlockIDPredicate
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ClientWrapper

|Class
|--
|dev.latvian.kubejs.client.ClientWrapper

---

|Extends
|--

---

|Fields|Type
|--|--
|  currentGui|GuiScreen
|  minecraft|Minecraft
|  player|ClientPlayer
|  world|ClientWorld

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Events

|Class
|--
|dev.latvian.kubejs.bindings.ScriptEventsWrapper

---

|Extends
|--

---

|Methods|Return Type
|--|--
| listen(String eventID, EventHandler handler) This method will register event listener, and callback function will be called when event is fired form mod|void
| listenAll(String[] eventIDs, EventHandler handler) This method will register one event listener for multiple events|void
| post(String eventID, Object data)|void
| post(String eventID)|void
| postCancellable(String eventID, Object data)|boolean
| postCancellable(String eventID)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## FacingWrapper

|Class
|--
|dev.latvian.kubejs.bindings.FacingWrapper

---

|Extends
|--

---

|Fields|Type
|--|--
|  down|EnumFacing
|  east|EnumFacing
|  map|Map\<String, EnumFacing>
|  north|EnumFacing
|  south|EnumFacing
|  up|EnumFacing
|  west|EnumFacing

---

|Methods|Return Type
|--|--
| getHorizontalIndex(EnumFacing e)|int
| getIndex(EnumFacing e)|int
| getPitch(EnumFacing e)|float
| getYaw(EnumFacing e)|float
| opposite(EnumFacing e)|EnumFacing
| rotateY(EnumFacing e)|EnumFacing
| wait(long arg0, int arg1)|void
| wait(long l)|void
| x(EnumFacing e)|int
| y(EnumFacing e)|int
| z(EnumFacing e)|int

---

## FluidWrapper

|Class
|--
|dev.latvian.kubejs.fluid.FluidWrapper

---

|Extends
|--

---

|Fields|Type
|--|--
|  list|List\<String>
|  typeMap|Map\<String, Fluid>

---

|Methods|Return Type
|--|--
| getType(Object o)|Fluid
| of(Object o)|FluidStack
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## FTB Quests Integration

|Class
|--
|com.feed_the_beast.ftbquests.integration.kubejs.FTBQuestsKubeJSWrapper

---

|Extends
|--

---

|Fields|Type
|--|--
|  changeProgressTypes|Map\<String, ChangeProgress>
|  questObjectTypes|Map\<String, QuestObjectType>
|  questShapes|Map\<String, QuestShape>

---

|Methods|Return Type
|--|--
| getData(World world, short team) Quest data from team UID|QuestData
| getData(World world, String team) Quest data from team ID|QuestData
| getData(Player player) Quest data from player|QuestData
| getFile(World world) Currently loaded quest file. Can be null|QuestFile
| getObject(World world, Object id) Quest object from object UID|QuestObjectBase
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Ingredient Utilities

|Class
|--
|dev.latvian.kubejs.bindings.IngredientWrapper

---

|Extends
|--

---

|Fields|Type
|--|--
|  all Return ingredient that matches any item|Ingredient
|  none Return ingredient that doesn't match any item|Ingredient

---

|Methods|Return Type
|--|--
| custom(Predicate\<ItemStack> predicate) Returns a custom ingredient using function(item){return [true/false based on item];}|Ingredient
| matchAny(Object[] o) Returns ingredient that matches any of other ingredients|Ingredient
| mod(String modID) Returns mod ingredient, matches all items from mod ID|Ingredient
| of(Object object) Returns ingredient from input|Ingredient
| ore(String oreName) Returns Ore Dictionary ingredient|Ingredient
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemUtilities

|Class
|--
|dev.latvian.kubejs.bindings.ItemWrapper

---

|Extends
|--

---

|Fields|Type
|--|--
|  empty|ItemStack
|  list|List\<ItemStack>
|  typeList|List\<ID>

---

|Methods|Return Type
|--|--
| clearListCache()|void
| fireworks(Map\<String, Object> properties)|Fireworks
| getItem(ID id)|Item
| of(Object o)|ItemStack
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## JSONUtilities

|Class
|--
|dev.latvian.kubejs.bindings.JsonWrapper

---

|Extends
|--

---

|Fields|Type
|--|--
|  jsonNull|JsonNull

---

|Methods|Return Type
|--|--
| array()|JsonArray
| copy(JsonElement json)|JsonElement
| fromString(String json)|JsonElement
| object()|JsonObject
| of(Object json)|JsonElement
| primitiveObject(JsonElement json)|Object
| read(File f)|Object
| read(String s)|Object
| toPrettyString(JsonElement json)|String
| toString(JsonElement json)|String
| wait(long arg0, int arg1)|void
| wait(long l)|void
| write(File arg0, Object arg1)|void
| write(String arg0, Object arg1)|void

---

## LoggerWrapper

|Class
|--
|dev.latvian.kubejs.util.LoggerWrapperJS

---

|Extends
|--

---

|Methods|Return Type
|--|--
| error(Object text, Object[] objects)|void
| info(Object text, Object[] objects)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void
| warn(Object text, Object[] objects)|void

---

## ScriptModData

|Class
|--
|dev.latvian.kubejs.script.ScriptModData

---

|Extends
|--

---

|Fields|Type
|--|--
|  list|Set\<String>
|  mcVersion|String
|  modVersion|String
|  type|String

---

|Methods|Return Type
|--|--
| getInfo(String modID)|ScriptModData$ModInfo
| isLoaded(String modID)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NBTUtilities

|Class
|--
|dev.latvian.kubejs.bindings.NBTWrapper

---

|Extends
|--

---

|Fields|Type
|--|--
|  emptyString|NBTString
|  nullCompound|NBTCompound
|  nullList|NBTList
|  nullTag|NBTNull

---

|Methods|Return Type
|--|--
| newCompound()|NBTCompound
| newList()|NBTList
| of(Object o)|NBTBase
| read(String file)|Object
| read(File file)|Object
| wait(long arg0, int arg1)|void
| wait(long l)|void
| write(File file, NBTCompound nbt)|void
| write(String file, NBTCompound nbt)|void

---

## OreDictionaryUtilities

|Class
|--
|dev.latvian.kubejs.bindings.OreDictWrapper

---

|Extends
|--

---

|Fields|Type
|--|--
|  dyes|List\<String>

---

|Methods|Return Type
|--|--
| add(Ingredient json, String json)|void
| getNames(ItemStack item)|List\<String>
| remove(Ingredient json, String json)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TextUtilities

|Class
|--
|dev.latvian.kubejs.bindings.TextWrapper

---

|Extends
|--

---

|Fields|Type
|--|--
|  colors|Map\<String, TextColor>

---

|Methods|Return Type
|--|--
| aqua(Text text) Aqua text|Text
| black(Text text) Black text|Text
| blue(Text text) Blue text|Text
| darkAqua(Text text) Dark aqua text|Text
| darkBlue(Text text) Dark blue text|Text
| darkGray(Text text) Dark gray text|Text
| darkGreen(Text text) Dark green text|Text
| darkPurple(Text text) Dark purple text|Text
| darkRed(Text text) Dark red text|Text
| fromJson(JsonElement j) Creates text component from JSON|Text
| gold(Text text) Gold text|Text
| gray(Text text) Gray text|Text
| green(Text text) Green text|Text
| join(Text arg0, Iterable\<Text> arg1) Joins text components together|Text
| lightPurple(Text text) Light purple text|Text
| of(Object o) Creates text component from any object|Text
| red(Text text) Red text|Text
| string(String text) Creates text component from string|Text
| translate(String key, Object[] objects) Creates text component from language key and extra objects|Text
| translate(String key) Creates text component from language key|Text
| wait(long arg0, int arg1)|void
| wait(long l)|void
| white(Text text) White text|Text
| yellow(Text text) Yellow text|Text

---

## UtilsWrapper

|Class
|--
|dev.latvian.kubejs.bindings.UtilsWrapper

---

|Extends
|--

---

|Fields|Type
|--|--
|  clientWorld|World
|  random|Random
|  server|Server
|  systemTime|long

---

|Methods|Return Type
|--|--
| createLogger(String s)|LoggerWrapper
| emptyList()|List\<T>
| emptyMap()|Map\<K, V>
| getField(String arg0, String arg1)|Field
| getField(String arg0, String arg1, String arg2)|Field
| getField(Class arg0, String arg1)|Field
| getField(Class arg0, String arg1, String arg2)|Field
| getPotion(Object o)|Potion
| getSound(Object o)|SoundEvent
| getStat(Object o)|StatBase
| getToolType(String s)|String
| getWorld(World w)|World
| id(Object o)|ID
| id(String arg0, String arg1)|ID
| newCountingMap()|CountingMap
| newList()|List
| newMap()|Map
| newSet()|Set
| overlay(String arg0, Object[] arg1)|Overlay
| parseDouble(Object arg0, double arg1)|double
| parseInt(Object arg0, int arg1)|int
| queueIO(Runnable r)|void
| randomOf(Random arg0, Collection\<Object> arg1)|Object
| regex(String s)|Pattern
| regex(String arg0, int arg1)|Pattern
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## UUIDUtilities

|Class
|--
|dev.latvian.kubejs.bindings.UUIDWrapper

---

|Extends
|--

---

|Methods|Return Type
|--|--
| fromString(String string)|UUID
| toString(UUID id)|String
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockAir

|Class
|--
|net.minecraft.block.BlockAir

---

|Extends
|--
|Block

---

|Fields|Type
|--|--
|  delegate|RegistryDelegate\<T>
|  field_149763_I|float
|  field_149765_K|float
|  field_149772_a|CreativeTabs
|  field_149781_w|float
|  field_149782_v|float
|  field_176227_L|BlockStateContainer
|  registryName|ResourceLocation
|  registryType|Class\<T>

---

|Methods|Return Type
|--|--
| addDestroyEffects(World arg0, BlockPos arg1, ParticleManager arg2)|boolean
| addHitEffects(BlockState arg0, World arg1, RayTraceResult arg2, ParticleManager arg3)|boolean
| addLandingEffects(BlockState arg0, WorldServer arg1, BlockPos arg2, BlockState arg3, EntityLivingBase arg4, int arg5)|boolean
| addRunningEffects(BlockState arg0, World arg1, BlockPos arg2, Entity arg3)|boolean
| beginLeavesDecay(BlockState arg0, World arg1, BlockPos arg2)|void
| canBeConnectedTo(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean
| canBeReplacedByLeaves(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| canConnectRedstone(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| canCreatureSpawn(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityLiving$SpawnPlacementType arg3)|boolean
| canEntityDestroy(BlockState arg0, BlockAccess arg1, BlockPos arg2, Entity arg3)|boolean
| canHarvestBlock(BlockAccess arg0, BlockPos arg1, EntityPlayer arg2)|boolean
| canPlaceTorchOnTop(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| canRenderInLayer(BlockState arg0, BlockRenderLayer arg1)|boolean
| canSilkHarvest(World arg0, BlockPos arg1, BlockState arg2, EntityPlayer arg3)|boolean
| canSustainLeaves(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| canSustainPlant(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3, Plantable arg4)|boolean
| createTileEntity(World arg0, BlockState arg1)|TileEntity
| doesSideBlockChestOpening(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| doesSideBlockRendering(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| func_149637_q(BlockState b)|boolean
| func_149638_a(Entity e)|float
| func_149645_b(BlockState b)|EnumBlockRenderType
| func_149647_a(CreativeTabs c)|Block
| func_149652_G()|boolean
| func_149653_t()|boolean
| func_149656_h(BlockState b)|EnumPushReaction
| func_149659_a(Explosion e)|boolean
| func_149662_c(BlockState b)|boolean
| func_149663_c(String s)|Block
| func_149666_a(CreativeTabs arg0, NonNullList\<ItemStack> arg1)|void
| func_149667_c(Block b)|boolean
| func_149675_a(boolean b)|Block
| func_149679_a(int arg0, Random arg1)|int
| func_149686_d(BlockState b)|boolean
| func_149688_o(BlockState b)|Material
| func_149698_L()|boolean
| func_149703_v()|boolean
| func_149708_J()|CreativeTabs
| func_149710_n(BlockState b)|boolean
| func_149711_c(float f)|Block
| func_149713_g(int i)|Block
| func_149715_a(float f)|Block
| func_149716_u()|boolean
| func_149717_k(BlockState b)|int
| func_149721_r(BlockState b)|boolean
| func_149722_s()|Block
| func_149730_j(BlockState b)|boolean
| func_149732_F()|String
| func_149738_a(World w)|int
| func_149739_a()|String
| func_149740_M(BlockState b)|boolean
| func_149744_f(BlockState b)|boolean
| func_149745_a(Random r)|int
| func_149750_m(BlockState b)|int
| func_149751_l(BlockState b)|boolean
| func_149752_b(float f)|Block
| func_176194_O()|BlockStateContainer
| func_176195_g(BlockState arg0, World arg1, BlockPos arg2)|float
| func_176196_c(World arg0, BlockPos arg1)|boolean
| func_176197_a(World arg0, BlockPos arg1, Entity arg2, Vec3d arg3)|Vec3d
| func_176198_a(World arg0, BlockPos arg1, EnumFacing arg2)|boolean
| func_176199_a(World arg0, BlockPos arg1, Entity arg2)|void
| func_176200_f(BlockAccess arg0, BlockPos arg1)|boolean
| func_176201_c(BlockState b)|int
| func_176203_a(int i)|BlockState
| func_176205_b(BlockAccess arg0, BlockPos arg1)|boolean
| func_176206_d(World arg0, BlockPos arg1, BlockState arg2)|void
| func_176208_a(World arg0, BlockPos arg1, BlockState arg2, EntityPlayer arg3)|void
| func_176209_a(BlockState arg0, boolean arg1)|boolean
| func_176211_b(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|int
| func_176213_c(World arg0, BlockPos arg1, BlockState arg2)|void
| func_176214_u(BlockState b)|boolean
| func_176216_a(World arg0, Entity arg1)|void
| func_176218_Q()|Block$EnumOffsetType
| func_176221_a(BlockState arg0, BlockAccess arg1, BlockPos arg2)|BlockState
| func_176223_P()|BlockState
| func_176224_k(World arg0, BlockPos arg1)|void
| func_176225_a(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| func_176226_b(World arg0, BlockPos arg1, BlockState arg2, int arg3)|void
| func_180633_a(World arg0, BlockPos arg1, BlockState arg2, EntityLivingBase arg3, ItemStack arg4)|void
| func_180634_a(World arg0, BlockPos arg1, BlockState arg2, Entity arg3)|void
| func_180636_a(BlockState arg0, World arg1, BlockPos arg2, Vec3d arg3, Vec3d arg4)|RayTraceResult
| func_180637_b(World arg0, BlockPos arg1, int arg2)|void
| func_180639_a(World arg0, BlockPos arg1, BlockState arg2, EntityPlayer arg3, EnumHand arg4, EnumFacing arg5, float arg6, float arg7, float arg8)|boolean
| func_180640_a(BlockState arg0, World arg1, BlockPos arg2)|AxisAlignedBB
| func_180641_l(BlockState arg0, World arg1, BlockPos arg2)|int
| func_180642_a(World arg0, BlockPos arg1, EnumFacing arg2, float arg3, float arg4, float arg5, int arg6, EntityLivingBase arg7)|BlockState
| func_180645_a(World arg0, BlockPos arg1, BlockState arg2, Random arg3)|void
| func_180646_a(BlockState arg0, BlockAccess arg1, BlockPos arg2)|AxisAlignedBB
| func_180647_a(BlockState arg0, EntityPlayer arg1, World arg2, BlockPos arg3)|float
| func_180649_a(World arg0, BlockPos arg1, EntityPlayer arg2)|void
| func_180650_b(World arg0, BlockPos arg1, BlockState arg2, Random arg3)|void
| func_180651_a(BlockState b)|int
| func_180652_a(World arg0, BlockPos arg1, Explosion arg2)|void
| func_180653_a(World arg0, BlockPos arg1, BlockState arg2, float arg3, int arg4)|void
| func_180655_c(BlockState arg0, World arg1, BlockPos arg2, Random arg3)|void
| func_180656_a(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|int
| func_180657_a(World arg0, EntityPlayer arg1, BlockPos arg2, BlockState arg3, TileEntity arg4, ItemStack arg5)|void
| func_180658_a(World arg0, BlockPos arg1, Entity arg2, float arg3)|void
| func_180659_g(BlockState arg0, BlockAccess arg1, BlockPos arg2)|MapColor
| func_180660_a(BlockState arg0, Random arg1, int arg2)|Item
| func_180663_b(World arg0, BlockPos arg1, BlockState arg2)|void
| func_180664_k()|BlockRenderLayer
| func_181623_g()|boolean
| func_185467_w()|SoundType
| func_185471_a(BlockState arg0, Mirror arg1)|BlockState
| func_185473_a(World arg0, BlockPos arg1, BlockState arg2)|ItemStack
| func_185477_a(BlockState arg0, World arg1, BlockPos arg2, AxisAlignedBB arg3, List\<AxisAlignedBB> arg4, Entity arg5, boolean arg6)|void
| func_185481_k(BlockState b)|boolean
| func_185484_c(BlockState arg0, BlockAccess arg1, BlockPos arg2)|int
| func_185485_f(BlockState b)|float
| func_185496_a(BlockState arg0, BlockAccess arg1, BlockPos arg2)|AxisAlignedBB
| func_185499_a(BlockState arg0, Rotation arg1)|BlockState
| func_189539_a(BlockState arg0, World arg1, BlockPos arg2, int arg3, int arg4)|boolean
| func_189540_a(BlockState arg0, World arg1, BlockPos arg2, Block arg3, BlockPos arg4)|void
| func_189872_a(BlockState arg0, Entity arg1)|boolean
| func_190946_v(BlockState b)|boolean
| func_190948_a(ItemStack arg0, World arg1, List\<String> arg2, TooltipFlag arg3)|void
| func_190949_e(BlockState arg0, BlockAccess arg1, BlockPos arg2)|Vec3d
| func_193383_a(BlockAccess arg0, BlockState arg1, BlockPos arg2, EnumFacing arg3)|BlockFaceShape
| getAiPathNodeType(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityLiving arg3)|PathNodeType
| getAiPathNodeType(BlockState arg0, BlockAccess arg1, BlockPos arg2)|PathNodeType
| getBeaconColorMultiplier(BlockState arg0, World arg1, BlockPos arg2, BlockPos arg3)|float[]
| getBedDirection(BlockState arg0, BlockAccess arg1, BlockPos arg2)|EnumFacing
| getBedSpawnPosition(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityPlayer arg3)|BlockPos
| getBlockLiquidHeight(World arg0, BlockPos arg1, BlockState arg2, Material arg3)|float
| getDrops(BlockAccess arg0, BlockPos arg1, BlockState arg2, int arg3)|List\<ItemStack>
| getDrops(NonNullList\<ItemStack> arg0, BlockAccess arg1, BlockPos arg2, BlockState arg3, int arg4)|void
| getEnchantPowerBonus(World arg0, BlockPos arg1)|float
| getExpDrop(BlockState arg0, BlockAccess arg1, BlockPos arg2, int arg3)|int
| getExplosionResistance(World arg0, BlockPos arg1, Entity arg2, Explosion arg3)|float
| getExtendedState(BlockState arg0, BlockAccess arg1, BlockPos arg2)|BlockState
| getFireSpreadSpeed(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|int
| getFlammability(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|int
| getFogColor(World arg0, BlockPos arg1, BlockState arg2, Entity arg3, Vec3d arg4, float arg5)|Vec3d
| getHarvestLevel(BlockState b)|int
| getHarvestTool(BlockState b)|String
| getLightOpacity(BlockState arg0, BlockAccess arg1, BlockPos arg2)|int
| getLightValue(BlockState arg0, BlockAccess arg1, BlockPos arg2)|int
| getPickBlock(BlockState arg0, RayTraceResult arg1, World arg2, BlockPos arg3, EntityPlayer arg4)|ItemStack
| getSlipperiness(BlockState arg0, BlockAccess arg1, BlockPos arg2, Entity arg3)|float
| getSoundType(BlockState arg0, World arg1, BlockPos arg2, Entity arg3)|SoundType
| getStateAtViewpoint(BlockState arg0, BlockAccess arg1, BlockPos arg2, Vec3d arg3)|BlockState
| getStateForPlacement(World arg0, BlockPos arg1, EnumFacing arg2, float arg3, float arg4, float arg5, int arg6, EntityLivingBase arg7, EnumHand arg8)|BlockState
| getValidRotations(World arg0, BlockPos arg1)|EnumFacing[]
| getWeakChanges(BlockAccess arg0, BlockPos arg1)|boolean
| hasTileEntity(BlockState b)|boolean
| isAABBInsideLiquid(World arg0, BlockPos arg1, AxisAlignedBB arg2)|Boolean
| isAABBInsideMaterial(World arg0, BlockPos arg1, AxisAlignedBB arg2, Material arg3)|Boolean
| isAir(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| isBeaconBase(BlockAccess arg0, BlockPos arg1, BlockPos arg2)|boolean
| isBed(BlockState arg0, BlockAccess arg1, BlockPos arg2, Entity arg3)|boolean
| isBedFoot(BlockAccess arg0, BlockPos arg1)|boolean
| isBurning(BlockAccess arg0, BlockPos arg1)|boolean
| isEntityInsideMaterial(BlockAccess arg0, BlockPos arg1, BlockState arg2, Entity arg3, double arg4, Material arg5, boolean arg6)|Boolean
| isFertile(World arg0, BlockPos arg1)|boolean
| isFireSource(World arg0, BlockPos arg1, EnumFacing arg2)|boolean
| isFlammable(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean
| isFoliage(BlockAccess arg0, BlockPos arg1)|boolean
| isLadder(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityLivingBase arg3)|boolean
| isLeaves(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| isNormalCube(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| isReplaceableOreGen(BlockState arg0, BlockAccess arg1, BlockPos arg2, Predicate\<BlockState> arg3)|boolean
| isSideSolid(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| isStickyBlock(BlockState b)|boolean
| isToolEffective(String arg0, BlockState arg1)|boolean
| isWood(BlockAccess arg0, BlockPos arg1)|boolean
| observedNeighborChange(BlockState arg0, World arg1, BlockPos arg2, Block arg3, BlockPos arg4)|void
| onBlockExploded(World arg0, BlockPos arg1, Explosion arg2)|void
| onNeighborChange(BlockAccess arg0, BlockPos arg1, BlockPos arg2)|void
| onPlantGrow(BlockState arg0, World arg1, BlockPos arg2, BlockPos arg3)|void
| quantityDropped(BlockState arg0, int arg1, Random arg2)|int
| recolorBlock(World arg0, BlockPos arg1, EnumFacing arg2, EnumDyeColor arg3)|boolean
| removedByPlayer(BlockState arg0, World arg1, BlockPos arg2, EntityPlayer arg3, boolean arg4)|boolean
| rotateBlock(World arg0, BlockPos arg1, EnumFacing arg2)|boolean
| setBedOccupied(BlockAccess arg0, BlockPos arg1, EntityPlayer arg2, boolean arg3)|void
| setDefaultSlipperiness(float f)|void
| setHarvestLevel(String arg0, int arg1, BlockState arg2)|void
| setHarvestLevel(String arg0, int arg1)|void
| shouldCheckWeakPower(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemAir

|Class
|--
|net.minecraft.item.ItemAir

---

|Extends
|--
|Item

---

|Fields|Type
|--|--
|  creativeTabs|CreativeTabs[]
|  delegate|RegistryDelegate\<T>
|  registryName|ResourceLocation
|  registryType|Class\<T>
|  repairable|boolean
|  tileEntityItemStackRenderer|TileEntityItemStackRenderer

---

|Methods|Return Type
|--|--
| canApplyAtEnchantingTable(ItemStack arg0, Enchantment arg1)|boolean
| canContinueUsing(ItemStack arg0, ItemStack arg1)|boolean
| canDestroyBlockInCreative(World arg0, BlockPos arg1, ItemStack arg2, EntityPlayer arg3)|boolean
| canDisableShield(ItemStack arg0, ItemStack arg1, EntityLivingBase arg2, EntityLivingBase arg3)|boolean
| canHarvestBlock(BlockState arg0, ItemStack arg1)|boolean
| createEntity(World arg0, Entity arg1, ItemStack arg2)|Entity
| doesSneakBypassUse(ItemStack arg0, BlockAccess arg1, BlockPos arg2, EntityPlayer arg3)|boolean
| func_111205_h(EntityEquipmentSlot e)|Multimap\<String, AttributeModifier>
| func_111207_a(ItemStack arg0, EntityPlayer arg1, EntityLivingBase arg2, EnumHand arg3)|boolean
| func_150893_a(ItemStack arg0, BlockState arg1)|float
| func_150895_a(CreativeTabs arg0, NonNullList\<ItemStack> arg1)|void
| func_150897_b(BlockState b)|boolean
| func_179215_a(NBTTagCompound n)|boolean
| func_179218_a(ItemStack arg0, World arg1, BlockState arg2, BlockPos arg3, EntityLivingBase arg4)|boolean
| func_180614_a(EntityPlayer arg0, World arg1, BlockPos arg2, EnumHand arg3, EnumFacing arg4, float arg5, float arg6, float arg7)|EnumActionResult
| func_185040_i()|boolean
| func_185043_a(ResourceLocation arg0, ItemPropertyGetter arg1)|void
| func_185045_a(ResourceLocation r)|ItemPropertyGetter
| func_190903_i()|ItemStack
| func_194125_a(CreativeTabs c)|boolean
| func_77612_l()|int
| func_77613_e(ItemStack i)|EnumRarity
| func_77614_k()|boolean
| func_77615_a(ItemStack arg0, World arg1, EntityLivingBase arg2, int arg3)|void
| func_77616_k(ItemStack i)|boolean
| func_77619_b()|int
| func_77622_d(ItemStack arg0, World arg1, EntityPlayer arg2)|void
| func_77624_a(ItemStack arg0, World arg1, List\<String> arg2, TooltipFlag arg3)|void
| func_77625_d(int i)|Item
| func_77626_a(ItemStack i)|int
| func_77627_a(boolean b)|Item
| func_77629_n_()|boolean
| func_77634_r()|boolean
| func_77636_d(ItemStack i)|boolean
| func_77637_a(CreativeTabs c)|Item
| func_77639_j()|int
| func_77640_w()|CreativeTabs
| func_77642_a(Item i)|Item
| func_77643_m_()|boolean
| func_77644_a(ItemStack arg0, EntityLivingBase arg1, EntityLivingBase arg2)|boolean
| func_77645_m()|boolean
| func_77647_b(int i)|int
| func_77651_p()|boolean
| func_77653_i(ItemStack i)|String
| func_77654_b(ItemStack arg0, World arg1, EntityLivingBase arg2)|ItemStack
| func_77655_b(String s)|Item
| func_77656_e(int i)|Item
| func_77657_g(ItemStack i)|String
| func_77658_a()|String
| func_77659_a(World arg0, EntityPlayer arg1, EnumHand arg2)|ActionResult\<ItemStack>
| func_77661_b(ItemStack i)|EnumAction
| func_77662_d()|boolean
| func_77663_a(ItemStack arg0, World arg1, Entity arg2, int arg3, boolean arg4)|void
| func_77664_n()|Item
| func_77667_c(ItemStack i)|String
| func_77668_q()|Item
| func_82788_x()|boolean
| func_82789_a(ItemStack arg0, ItemStack arg1)|boolean
| getAnimationParameters(ItemStack arg0, World arg1, EntityLivingBase arg2)|ImmutableMap\<String, TimeValue>
| getArmorModel(EntityLivingBase arg0, ItemStack arg1, EntityEquipmentSlot arg2, ModelBiped arg3)|ModelBiped
| getArmorTexture(ItemStack arg0, Entity arg1, EntityEquipmentSlot arg2, String arg3)|String
| getAttributeModifiers(EntityEquipmentSlot arg0, ItemStack arg1)|Multimap\<String, AttributeModifier>
| getContainerItem(ItemStack i)|ItemStack
| getCreatorModId(ItemStack i)|String
| getDamage(ItemStack i)|int
| getDurabilityForDisplay(ItemStack i)|double
| getEntityLifespan(ItemStack arg0, World arg1)|int
| getEquipmentSlot(ItemStack i)|EntityEquipmentSlot
| getFontRenderer(ItemStack i)|FontRenderer
| getForgeRarity(ItemStack i)|Rarity
| getHarvestLevel(ItemStack arg0, String arg1, EntityPlayer arg2, BlockState arg3)|int
| getHighlightTip(ItemStack arg0, String arg1)|String
| getHorseArmorTexture(EntityLiving arg0, ItemStack arg1)|String
| getHorseArmorType(ItemStack i)|HorseArmorType
| getItemBurnTime(ItemStack i)|int
| getItemEnchantability(ItemStack i)|int
| getItemStackLimit(ItemStack i)|int
| getMaxDamage(ItemStack i)|int
| getMetadata(ItemStack i)|int
| getNBTShareTag(ItemStack i)|NBTTagCompound
| getRGBDurabilityForDisplay(ItemStack i)|int
| getSmeltingExperience(ItemStack i)|float
| getToolClasses(ItemStack i)|Set\<String>
| getXpRepairRatio(ItemStack i)|float
| hasContainerItem(ItemStack i)|boolean
| hasCustomEntity(ItemStack i)|boolean
| initCapabilities(ItemStack arg0, NBTTagCompound arg1)|CapabilityProvider
| isBeaconPayment(ItemStack i)|boolean
| isBookEnchantable(ItemStack arg0, ItemStack arg1)|boolean
| isDamaged(ItemStack i)|boolean
| isShield(ItemStack arg0, EntityLivingBase arg1)|boolean
| isValidArmor(ItemStack arg0, EntityEquipmentSlot arg1, Entity arg2)|boolean
| onArmorTick(World arg0, EntityPlayer arg1, ItemStack arg2)|void
| onBlockStartBreak(ItemStack arg0, BlockPos arg1, EntityPlayer arg2)|boolean
| onDroppedByPlayer(ItemStack arg0, EntityPlayer arg1)|boolean
| onEntityItemUpdate(EntityItem e)|boolean
| onEntitySwing(EntityLivingBase arg0, ItemStack arg1)|boolean
| onHorseArmorTick(World arg0, EntityLiving arg1, ItemStack arg2)|void
| onItemUseFirst(EntityPlayer arg0, World arg1, BlockPos arg2, EnumFacing arg3, float arg4, float arg5, float arg6, EnumHand arg7)|EnumActionResult
| onLeftClickEntity(ItemStack arg0, EntityPlayer arg1, Entity arg2)|boolean
| onUsingTick(ItemStack arg0, EntityLivingBase arg1, int arg2)|void
| readNBTShareTag(ItemStack arg0, NBTTagCompound arg1)|void
| renderHelmetOverlay(ItemStack arg0, EntityPlayer arg1, ScaledResolution arg2, float arg3)|void
| setDamage(ItemStack arg0, int arg1)|void
| setHarvestLevel(String arg0, int arg1)|void
| setNoRepair()|Item
| shouldCauseBlockBreakReset(ItemStack arg0, ItemStack arg1)|boolean
| shouldCauseReequipAnimation(ItemStack arg0, ItemStack arg1, boolean arg2)|boolean
| showDurabilityBar(ItemStack i)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TextColor

|Class
|--
|dev.latvian.kubejs.text.TextColor

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  code|char
|  color|int
|  declaringClass|Class\<E>
|  name|String
|  textFormatting|TextFormatting

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumHand

|Class
|--
|net.minecraft.util.EnumHand

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumRarity

|Class
|--
|net.minecraft.item.EnumRarity

---

|Extends
|--
|Enum
|Rarity

---

|Fields|Type
|--|--
|  color|TextFormatting
|  declaringClass|Class\<E>
|  field_77934_f|String
|  field_77937_e|TextFormatting
|  name|String

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityEquipmentSlot

|Class
|--
|net.minecraft.inventory.EntityEquipmentSlot

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_188450_d()|String
| func_188452_c()|int
| func_188453_a()|EntityEquipmentSlot$Type
| func_188454_b()|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockBreakEvent

|Class
|--
|dev.latvian.kubejs.block.BlockBreakEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|block.break|Yes|No|Yes

---

|Fields|Type
|--|--
|  block|Block
|  entity|Entity
|  player|Player
|  server|Server
|  world|World
|  xp|int

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| cancel()|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockDropsEvent

|Class
|--
|dev.latvian.kubejs.block.BlockDropsEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|block.drops|No|No|Yes

---

|Fields|Type
|--|--
|  axeLevel|int
|  block|Block
|  dropChance|float
|  drops|List\<ItemStack>
|  entity|Entity
|  fortuneLevel|int
|  item|ItemStack
|  pickaxeLevel|int
|  player|Player
|  server|Server
|  shovelLevel|int
|  silkTouching|boolean
|  world|World

---

|Methods|Return Type
|--|--
| addDrop(ItemStack item, float chance)|void
| addGameStage(String s)|void
| getItemHarvestLevel(String s)|int
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockLeftClickEvent

|Class
|--
|dev.latvian.kubejs.block.BlockLeftClickEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|block.left_click|Yes|Yes|Yes

---

|Fields|Type
|--|--
|  block|Block
|  entity|Entity
|  facing|EnumFacing
|  item|ItemStack
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| cancel()|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockPlaceEvent

|Class
|--
|dev.latvian.kubejs.block.BlockPlaceEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|block.place|Yes|No|Yes

---

|Fields|Type
|--|--
|  block|Block
|  entity|Entity
|  hand|EnumHand
|  item|ItemStack
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| cancel()|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockRegistryEvent

|Class
|--
|dev.latvian.kubejs.block.BlockRegistryEventJS

---

|Extends
|--
|Event

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|block.registry|No|Yes|Yes

---

|Methods|Return Type
|--|--
| create(String s)|BlockBuilder
| register(String arg0, Block arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockRightClickEvent

|Class
|--
|dev.latvian.kubejs.block.BlockRightClickEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|block.right_click|Yes|Yes|Yes

---

|Fields|Type
|--|--
|  block|Block
|  entity|Entity
|  facing|EnumFacing
|  hand|EnumHand
|  item|ItemStack
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| cancel()|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## DebugInfoEvent

|Class
|--
|dev.latvian.kubejs.client.DebugInfoEventJS

---

|Extends
|--
|Event

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|client.debug_info|No|Yes|No

---

|Fields|Type
|--|--
|  left|List\<String>
|  right|List\<String>
|  showDebug|boolean

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ClientLoggedInEvent

|Class
|--
|dev.latvian.kubejs.client.ClientLoggedInEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|client.logged_in|No|Yes|No

---

|Fields|Type
|--|--
|  entity|Entity
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ClientTickEvent

|Class
|--
|dev.latvian.kubejs.client.ClientTickEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|client.tick|No|Yes|No

---

|Fields|Type
|--|--
|  entity|Entity
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CommandRegistryEvent

|Class
|--
|dev.latvian.kubejs.command.CommandRegistryEventJS

---

|Extends
|--
|ServerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|command.registry|No|No|Yes

---

|Fields|Type
|--|--
|  server|Server

---

|Methods|Return Type
|--|--
| create(String s)|CommandBuilder
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CommandEvent

|Class
|--
|dev.latvian.kubejs.server.CommandEventJS

---

|Extends
|--
|ServerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|command.run|Yes|No|Yes

---

|Fields|Type
|--|--
|  command|String
|  parameters|String[]
|  sender|CommandSender
|  server|Server

---

|Methods|Return Type
|--|--
| cancel()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## LivingEntityAttackEvent

|Class
|--
|dev.latvian.kubejs.entity.LivingEntityAttackEventJS

---

|Extends
|--
|LivingEntityEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|entity.attack|Yes|Yes|Yes

---

|Fields|Type
|--|--
|  damage|float
|  entity|Entity
|  server|Server
|  source|DamageSource
|  world|World

---

|Methods|Return Type
|--|--
| cancel()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CheckLivingEntitySpawnEvent

|Class
|--
|dev.latvian.kubejs.entity.CheckLivingEntitySpawnEventJS

---

|Extends
|--
|LivingEntityEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|entity.check_spawn|Yes|Yes|Yes

---

|Fields|Type
|--|--
|  block|Block
|  entity|Entity
|  server|Server
|  world|World
|  x|float
|  y|float
|  z|float

---

|Methods|Return Type
|--|--
| cancel()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## LivingEntityDeathEvent

|Class
|--
|dev.latvian.kubejs.entity.LivingEntityDeathEventJS

---

|Extends
|--
|LivingEntityEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|entity.death|Yes|Yes|Yes

---

|Fields|Type
|--|--
|  entity|Entity
|  server|Server
|  source|DamageSource
|  world|World

---

|Methods|Return Type
|--|--
| cancel()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## LivingEntityDropsEvent

|Class
|--
|dev.latvian.kubejs.entity.LivingEntityDropsEventJS

---

|Extends
|--
|LivingEntityEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|entity.drops|Yes|Yes|Yes

---

|Fields|Type
|--|--
|  drops|List\<ItemEntity>
|  entity|Entity
|  lootingLevel|int
|  recentlyHit|boolean
|  server|Server
|  source|DamageSource
|  world|World

---

|Methods|Return Type
|--|--
| addDrop(ItemStack item, float chance)|ItemEntity
| cancel()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntitySpawnedEvent

|Class
|--
|dev.latvian.kubejs.entity.EntitySpawnedEventJS

---

|Extends
|--
|EntityEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|entity.spawned|Yes|Yes|Yes

---

|Fields|Type
|--|--
|  entity|Entity
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| cancel()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## QuestObjectCompletedEvent

|Class
|--
|com.feed_the_beast.ftbquests.integration.kubejs.QuestObjectCompletedEventJS

---

|Extends
|--
|Event

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|ftbquests.completed|No|Yes|Yes

---

|Fields|Type
|--|--
|  data|QuestData
|  notifiedPlayers List of notified players. It isn't always the list of online members of that team, for example, this list is empty when invisible quest was completed|EntityArrayList
|  object|QuestObject
|  onlineMembers List of all online team members|EntityArrayList

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CustomRewardEvent

|Class
|--
|com.feed_the_beast.ftbquests.integration.kubejs.CustomRewardEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|ftbquests.custom_reward|Yes|Yes|Yes

---

|Fields|Type
|--|--
|  entity|Entity
|  notify|boolean
|  player|Player
|  reward|CustomReward
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| cancel()|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CustomTaskEvent

|Class
|--
|com.feed_the_beast.ftbquests.integration.kubejs.CustomTaskEventJS

---

|Extends
|--
|Event

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|ftbquests.custom_task|Yes|Yes|Yes

---

|Fields|Type
|--|--
|  task|CustomTask

---

|Methods|Return Type
|--|--
| cancel()|void
| setCheck(CustomTaskChecker c) Check callback - function (player), is called every x ticks. You can change x with setCheckTimer()|void
| setCheckTimer(int i) How often in ticks the callback function should be checked|void
| setEnableButton(boolean b) Enable checking on button click|void
| setMaxProgress(long l) Max progress of this task|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TaskStartedEvent

|Class
|--
|com.feed_the_beast.ftbquests.integration.kubejs.TaskStartedEventJS

---

|Extends
|--
|Event

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|ftbquests.started|No|Yes|Yes

---

|Fields|Type
|--|--
|  taskData|TaskData

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GameStageEvent

|Class
|--
|dev.latvian.kubejs.integration.gamestages.GameStageEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|gamestage.removed|No|Yes|Yes

---

|Fields|Type
|--|--
|  entity|Entity
|  player|Player
|  server|Server
|  stage|String
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemCraftedEvent

|Class
|--
|dev.latvian.kubejs.item.ItemCraftedEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|item.crafted|No|No|Yes

---

|Fields|Type
|--|--
|  block|Block
|  entity|Entity
|  item|ItemStack
|  matrix|Inventory
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemEntityInteractEvent

|Class
|--
|dev.latvian.kubejs.item.ItemEntityInteractEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|item.entity_interact|Yes|Yes|Yes

---

|Fields|Type
|--|--
|  entity|Entity
|  hand|EnumHand
|  item|ItemStack
|  player|Player
|  server|Server
|  target|Entity
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| cancel()|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemLeftClickEvent

|Class
|--
|dev.latvian.kubejs.item.ItemLeftClickEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|item.left_click|No|Yes|No

---

|Fields|Type
|--|--
|  entity|Entity
|  item|ItemStack
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemPickupEvent

|Class
|--
|dev.latvian.kubejs.item.ItemPickupEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|item.pickup|Yes|Yes|Yes

---

|Fields|Type
|--|--
|  entity|Entity
|  item|ItemStack
|  itemEntity|Entity
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| cancel()|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemRegistryEvent

|Class
|--
|dev.latvian.kubejs.item.ItemRegistryEventJS

---

|Extends
|--
|Event

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|item.registry|No|Yes|Yes

---

|Methods|Return Type
|--|--
| create(String s)|ItemBuilder
| createBlockItem(String s)|ItemBuilder
| register(String arg0, Item arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemRightClickEvent

|Class
|--
|dev.latvian.kubejs.item.ItemRightClickEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|item.right_click|Yes|Yes|Yes

---

|Fields|Type
|--|--
|  entity|Entity
|  hand|EnumHand
|  item|ItemStack
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| cancel()|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemRightClickEmptyEvent

|Class
|--
|dev.latvian.kubejs.item.ItemRightClickEmptyEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|item.right_click_empty|No|Yes|No

---

|Fields|Type
|--|--
|  entity|Entity
|  hand|EnumHand
|  item|ItemStack
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemSmeltedEvent

|Class
|--
|dev.latvian.kubejs.item.ItemSmeltedEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|item.smelted|No|No|Yes

---

|Fields|Type
|--|--
|  entity|Entity
|  item|ItemStack
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemTossEvent

|Class
|--
|dev.latvian.kubejs.item.ItemTossEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|item.toss|Yes|Yes|Yes

---

|Fields|Type
|--|--
|  entity|Entity
|  item|ItemStack
|  itemEntity|Entity
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| cancel()|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Event

|Class
|--
|dev.latvian.kubejs.event.EventJS

---

|Extends
|--

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|loaded|No|Yes|Yes

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PlayerAdvancementEvent

|Class
|--
|dev.latvian.kubejs.player.PlayerAdvancementEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|player.advancement|No|No|Yes

---

|Fields|Type
|--|--
|  advancement|Advancement
|  entity|Entity
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PlayerChatEvent

|Class
|--
|dev.latvian.kubejs.player.PlayerChatEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|player.chat|Yes|No|Yes

---

|Fields|Type
|--|--
|  entity|Entity
|  message|String
|  player|Player
|  server|Server
|  username|String
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| cancel()|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ChestEvent

|Class
|--
|dev.latvian.kubejs.player.ChestEventJS

---

|Extends
|--
|InventoryEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|player.chest.closed|No|Yes|Yes

---

|Fields|Type
|--|--
|  block|Block
|  entity|Entity
|  inventory|Inventory
|  inventoryContainer|Container
|  player|Player
|  server|Server
|  world|World
|  wrappedInventory|Inventory

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NetworkEvent

|Class
|--
|dev.latvian.kubejs.net.NetworkEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|player.data_from_client|Yes|No|Yes

---

|Fields|Type
|--|--
|  channel|String
|  data|NBTCompound
|  entity|Entity
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| cancel()|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## InventoryChangedEvent

|Class
|--
|dev.latvian.kubejs.player.InventoryChangedEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|player.inventory.changed|No|Yes|Yes

---

|Fields|Type
|--|--
|  entity|Entity
|  item Will be non-empty when a single item has changed|ItemStack
|  player|Player
|  server|Server
|  slot Slot index that changed, can be -1|int
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## InventoryEvent

|Class
|--
|dev.latvian.kubejs.player.InventoryEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|player.inventory.closed|No|Yes|Yes

---

|Fields|Type
|--|--
|  entity|Entity
|  inventoryContainer|Container
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SimplePlayerEvent

|Class
|--
|dev.latvian.kubejs.player.SimplePlayerEventJS

---

|Extends
|--
|PlayerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|player.tick|No|No|Yes

---

|Fields|Type
|--|--
|  entity|Entity
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AlloySmelterRecipeEvent

|Class
|--
|dev.latvian.kubejs.crafting.AlloySmelterRecipeEventJS

---

|Extends
|--
|RecipeEventBase

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|recipes.alloy_smelter|No|Yes|Yes

---

|Fields|Type
|--|--
|  mod|String

---

|Methods|Return Type
|--|--
| add(Map\<String, Object> m)|void
| create(Collection\<Object> arg0, Object arg1)|AlloySmelterRecipeEventJS$AlloySmelterRecipe
| create(Object arg0, Object arg1, Object arg2)|AlloySmelterRecipeEventJS$AlloySmelterRecipe
| remove(Object o)|void
| removeInput(Object o)|void
| removePrimary(Object o)|void
| removeSecondary(Object o)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CompressorRecipeEvent

|Class
|--
|dev.latvian.kubejs.crafting.CompressorRecipeEventJS

---

|Extends
|--
|RecipeEventBase

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|recipes.compressor|No|Yes|Yes

---

|Fields|Type
|--|--
|  mod|String

---

|Methods|Return Type
|--|--
| add(Map\<String, Object> m)|void
| create(Object arg0, Object arg1)|CompressorRecipeEventJS$CompressorRecipe
| remove(Object o)|void
| removeInput(Object o)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CraftingTableRecipeEvent

|Class
|--
|dev.latvian.kubejs.crafting.CraftingTableRecipeEventJS

---

|Extends
|--
|Event

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|recipes.crafting_table|No|Yes|Yes

---

|Methods|Return Type
|--|--
| add(String arg0, Object arg1)|void
| addShaped(Object arg0, String[] arg1, Map\<String, Object> arg2)|void
| addShaped(String arg0, Object arg1, String[] arg2, Map\<String, Object> arg3)|void
| addShapeless(Object arg0, Object[] arg1)|void
| addShapeless(String arg0, Object arg1, Object[] arg2)|void
| remove(Object o)|void
| removeAdvanced(Predicate\<Recipe> p)|void
| removeGroup(Object o)|void
| removeID(Object o)|void
| removeMod(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## FurnaceRecipeEvent

|Class
|--
|dev.latvian.kubejs.crafting.FurnaceRecipeEventJS

---

|Extends
|--
|RecipeEventBase

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|recipes.furnace|No|Yes|Yes

---

|Fields|Type
|--|--
|  mod|String

---

|Methods|Return Type
|--|--
| add(Map\<String, Object> m)|void
| create(Object arg0, Object arg1)|FurnaceRecipeEventJS$FurnaceRecipe
| remove(Object o)|void
| removeInput(Object o)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PulverizerRecipeEvent

|Class
|--
|dev.latvian.kubejs.crafting.PulverizerRecipeEventJS

---

|Extends
|--
|RecipeEventBase

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|recipes.pulverizer|No|Yes|Yes

---

|Fields|Type
|--|--
|  mod|String

---

|Methods|Return Type
|--|--
| add(Map\<String, Object> m)|void
| create(Object arg0, Object arg1)|PulverizerRecipeEventJS$PulverizerRecipe
| remove(Object o)|void
| removeInput(Object o)|void
| removePrimary(Object o)|void
| removeSecondary(Object o)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RemoveRecipesEvent

|Class
|--
|dev.latvian.kubejs.crafting.RemoveRecipesEventJS

---

|Extends
|--
|Event

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|recipes.remove.input|No|Yes|Yes

---

|Fields|Type
|--|--
|  mod|String
|  type|String

---

|Methods|Return Type
|--|--
| remove(Object o)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SimpleServerEvent

|Class
|--
|dev.latvian.kubejs.server.SimpleServerEventJS

---

|Extends
|--
|ServerEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|server.tick|No|No|Yes

---

|Fields|Type
|--|--
|  server|Server

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ExplosionEventJS$Post

|Class
|--
|dev.latvian.kubejs.world.ExplosionEventJS$Post

---

|Extends
|--
|ExplosionEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|world.explosion.post|No|No|Yes

---

|Fields|Type
|--|--
|  affectedBlocks|List\<Block>
|  affectedEntities|EntityArrayList
|  block|Block
|  exploder|LivingEntity
|  position|Vec3d
|  server|Server
|  world|World
|  x|double
|  y|double
|  z|double

---

|Methods|Return Type
|--|--
| removeAffectedBlock(Block b)|void
| removeAffectedEntity(Entity e)|void
| removeAllAffectedBlocks()|void
| removeAllAffectedEntities()|void
| removeKnockback()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ExplosionEventJS$Pre

|Class
|--
|dev.latvian.kubejs.world.ExplosionEventJS$Pre

---

|Extends
|--
|ExplosionEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|world.explosion.pre|Yes|No|Yes

---

|Fields|Type
|--|--
|  block|Block
|  exploder|LivingEntity
|  position|Vec3d
|  server|Server
|  world|World
|  x|double
|  y|double
|  z|double

---

|Methods|Return Type
|--|--
| cancel()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SimpleWorldEvent

|Class
|--
|dev.latvian.kubejs.world.SimpleWorldEventJS

---

|Extends
|--
|WorldEvent

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|world.tick|No|No|Yes

---

|Fields|Type
|--|--
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MissingMappingEvent

|Class
|--
|dev.latvian.kubejs.block.MissingMappingEventJS

---

|Extends
|--
|Event

---

|Event|Can cancel|True if event can be cancelled|Client|True if event is fired on client side|Server|True if event is fired on server side
|--|--|--|--
|world.missing_mappings|No|Yes|Yes

---

|Fields|Type
|--|--
|  registry|ID

---

|Methods|Return Type
|--|--
| fail(Object o)|void
| forEachMapping(Object arg0, Consumer\<RegistryEvent$MissingMappings$Mapping> arg1)|void
| ignore(Object o)|void
| remap(Object arg0, Object arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void
| warn(Object o)|void

---

## EnumFacing

|Class
|--
|net.minecraft.util.EnumFacing

---

|Extends
|--
|Enum
|StringSerializable

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_176610_l()|String
| func_176730_m()|Vec3i
| func_176732_a(EnumFacing$Axis e)|EnumFacing
| func_176734_d()|EnumFacing
| func_176735_f()|EnumFacing
| func_176736_b()|int
| func_176740_k()|EnumFacing$Axis
| func_176742_j()|String
| func_176743_c()|EnumFacing$AxisDirection
| func_176745_a()|int
| func_176746_e()|EnumFacing
| func_185119_l()|float
| func_82599_e()|int
| func_82601_c()|int
| func_96559_d()|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Material

|Class
|--
|dev.latvian.kubejs.block.MaterialJS

---

|Extends
|--

---

|Fields|Type
|--|--
|  id|String
|  minecraftMaterial|Material

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ID

|Class
|--
|dev.latvian.kubejs.util.ID

---

|Extends
|--
|Comparable

---

|Fields|Type
|--|--
|  namespace|String
|  path|String

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(ID i)|int
| isNull()|boolean
| mc()|ResourceLocation
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockPredicate

|Interface
|--
|dev.latvian.kubejs.block.predicate.BlockPredicate

---

|Extends
|--

---

|Methods|Return Type
|--|--
| check(Block block)|boolean

---

## BlockEntityPredicate

|Class
|--
|dev.latvian.kubejs.block.predicate.BlockEntityPredicate

---

|Extends
|--
|BlockPredicate

---

|Methods|Return Type
|--|--
| check(Block b)|boolean
| data(BlockEntityPredicateDataCheck b)|BlockEntityPredicate
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Block

|Class
|--
|net.minecraft.block.Block

---

|Extends
|--
|IForgeRegistryEntry$Impl

---

|Fields|Type
|--|--
|  delegate|RegistryDelegate\<T>
|  field_149763_I|float
|  field_149765_K|float
|  field_149772_a|CreativeTabs
|  field_149781_w|float
|  field_149782_v|float
|  field_176227_L|BlockStateContainer
|  registryName|ResourceLocation
|  registryType|Class\<T>

---

|Methods|Return Type
|--|--
| addDestroyEffects(World arg0, BlockPos arg1, ParticleManager arg2)|boolean
| addHitEffects(BlockState arg0, World arg1, RayTraceResult arg2, ParticleManager arg3)|boolean
| addLandingEffects(BlockState arg0, WorldServer arg1, BlockPos arg2, BlockState arg3, EntityLivingBase arg4, int arg5)|boolean
| addRunningEffects(BlockState arg0, World arg1, BlockPos arg2, Entity arg3)|boolean
| beginLeavesDecay(BlockState arg0, World arg1, BlockPos arg2)|void
| canBeConnectedTo(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean
| canBeReplacedByLeaves(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| canConnectRedstone(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| canCreatureSpawn(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityLiving$SpawnPlacementType arg3)|boolean
| canEntityDestroy(BlockState arg0, BlockAccess arg1, BlockPos arg2, Entity arg3)|boolean
| canHarvestBlock(BlockAccess arg0, BlockPos arg1, EntityPlayer arg2)|boolean
| canPlaceTorchOnTop(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| canRenderInLayer(BlockState arg0, BlockRenderLayer arg1)|boolean
| canSilkHarvest(World arg0, BlockPos arg1, BlockState arg2, EntityPlayer arg3)|boolean
| canSustainLeaves(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| canSustainPlant(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3, Plantable arg4)|boolean
| createTileEntity(World arg0, BlockState arg1)|TileEntity
| doesSideBlockChestOpening(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| doesSideBlockRendering(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| func_149637_q(BlockState b)|boolean
| func_149638_a(Entity e)|float
| func_149645_b(BlockState b)|EnumBlockRenderType
| func_149647_a(CreativeTabs c)|Block
| func_149652_G()|boolean
| func_149653_t()|boolean
| func_149656_h(BlockState b)|EnumPushReaction
| func_149659_a(Explosion e)|boolean
| func_149662_c(BlockState b)|boolean
| func_149663_c(String s)|Block
| func_149666_a(CreativeTabs arg0, NonNullList\<ItemStack> arg1)|void
| func_149667_c(Block b)|boolean
| func_149675_a(boolean b)|Block
| func_149679_a(int arg0, Random arg1)|int
| func_149686_d(BlockState b)|boolean
| func_149688_o(BlockState b)|Material
| func_149698_L()|boolean
| func_149703_v()|boolean
| func_149708_J()|CreativeTabs
| func_149710_n(BlockState b)|boolean
| func_149711_c(float f)|Block
| func_149713_g(int i)|Block
| func_149715_a(float f)|Block
| func_149716_u()|boolean
| func_149717_k(BlockState b)|int
| func_149721_r(BlockState b)|boolean
| func_149722_s()|Block
| func_149730_j(BlockState b)|boolean
| func_149732_F()|String
| func_149738_a(World w)|int
| func_149739_a()|String
| func_149740_M(BlockState b)|boolean
| func_149744_f(BlockState b)|boolean
| func_149745_a(Random r)|int
| func_149750_m(BlockState b)|int
| func_149751_l(BlockState b)|boolean
| func_149752_b(float f)|Block
| func_176194_O()|BlockStateContainer
| func_176195_g(BlockState arg0, World arg1, BlockPos arg2)|float
| func_176196_c(World arg0, BlockPos arg1)|boolean
| func_176197_a(World arg0, BlockPos arg1, Entity arg2, Vec3d arg3)|Vec3d
| func_176198_a(World arg0, BlockPos arg1, EnumFacing arg2)|boolean
| func_176199_a(World arg0, BlockPos arg1, Entity arg2)|void
| func_176200_f(BlockAccess arg0, BlockPos arg1)|boolean
| func_176201_c(BlockState b)|int
| func_176203_a(int i)|BlockState
| func_176205_b(BlockAccess arg0, BlockPos arg1)|boolean
| func_176206_d(World arg0, BlockPos arg1, BlockState arg2)|void
| func_176208_a(World arg0, BlockPos arg1, BlockState arg2, EntityPlayer arg3)|void
| func_176209_a(BlockState arg0, boolean arg1)|boolean
| func_176211_b(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|int
| func_176213_c(World arg0, BlockPos arg1, BlockState arg2)|void
| func_176214_u(BlockState b)|boolean
| func_176216_a(World arg0, Entity arg1)|void
| func_176218_Q()|Block$EnumOffsetType
| func_176221_a(BlockState arg0, BlockAccess arg1, BlockPos arg2)|BlockState
| func_176223_P()|BlockState
| func_176224_k(World arg0, BlockPos arg1)|void
| func_176225_a(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| func_176226_b(World arg0, BlockPos arg1, BlockState arg2, int arg3)|void
| func_180633_a(World arg0, BlockPos arg1, BlockState arg2, EntityLivingBase arg3, ItemStack arg4)|void
| func_180634_a(World arg0, BlockPos arg1, BlockState arg2, Entity arg3)|void
| func_180636_a(BlockState arg0, World arg1, BlockPos arg2, Vec3d arg3, Vec3d arg4)|RayTraceResult
| func_180637_b(World arg0, BlockPos arg1, int arg2)|void
| func_180639_a(World arg0, BlockPos arg1, BlockState arg2, EntityPlayer arg3, EnumHand arg4, EnumFacing arg5, float arg6, float arg7, float arg8)|boolean
| func_180640_a(BlockState arg0, World arg1, BlockPos arg2)|AxisAlignedBB
| func_180641_l(BlockState arg0, World arg1, BlockPos arg2)|int
| func_180642_a(World arg0, BlockPos arg1, EnumFacing arg2, float arg3, float arg4, float arg5, int arg6, EntityLivingBase arg7)|BlockState
| func_180645_a(World arg0, BlockPos arg1, BlockState arg2, Random arg3)|void
| func_180646_a(BlockState arg0, BlockAccess arg1, BlockPos arg2)|AxisAlignedBB
| func_180647_a(BlockState arg0, EntityPlayer arg1, World arg2, BlockPos arg3)|float
| func_180649_a(World arg0, BlockPos arg1, EntityPlayer arg2)|void
| func_180650_b(World arg0, BlockPos arg1, BlockState arg2, Random arg3)|void
| func_180651_a(BlockState b)|int
| func_180652_a(World arg0, BlockPos arg1, Explosion arg2)|void
| func_180653_a(World arg0, BlockPos arg1, BlockState arg2, float arg3, int arg4)|void
| func_180655_c(BlockState arg0, World arg1, BlockPos arg2, Random arg3)|void
| func_180656_a(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|int
| func_180657_a(World arg0, EntityPlayer arg1, BlockPos arg2, BlockState arg3, TileEntity arg4, ItemStack arg5)|void
| func_180658_a(World arg0, BlockPos arg1, Entity arg2, float arg3)|void
| func_180659_g(BlockState arg0, BlockAccess arg1, BlockPos arg2)|MapColor
| func_180660_a(BlockState arg0, Random arg1, int arg2)|Item
| func_180663_b(World arg0, BlockPos arg1, BlockState arg2)|void
| func_180664_k()|BlockRenderLayer
| func_181623_g()|boolean
| func_185467_w()|SoundType
| func_185471_a(BlockState arg0, Mirror arg1)|BlockState
| func_185473_a(World arg0, BlockPos arg1, BlockState arg2)|ItemStack
| func_185477_a(BlockState arg0, World arg1, BlockPos arg2, AxisAlignedBB arg3, List\<AxisAlignedBB> arg4, Entity arg5, boolean arg6)|void
| func_185481_k(BlockState b)|boolean
| func_185484_c(BlockState arg0, BlockAccess arg1, BlockPos arg2)|int
| func_185485_f(BlockState b)|float
| func_185496_a(BlockState arg0, BlockAccess arg1, BlockPos arg2)|AxisAlignedBB
| func_185499_a(BlockState arg0, Rotation arg1)|BlockState
| func_189539_a(BlockState arg0, World arg1, BlockPos arg2, int arg3, int arg4)|boolean
| func_189540_a(BlockState arg0, World arg1, BlockPos arg2, Block arg3, BlockPos arg4)|void
| func_189872_a(BlockState arg0, Entity arg1)|boolean
| func_190946_v(BlockState b)|boolean
| func_190948_a(ItemStack arg0, World arg1, List\<String> arg2, TooltipFlag arg3)|void
| func_190949_e(BlockState arg0, BlockAccess arg1, BlockPos arg2)|Vec3d
| func_193383_a(BlockAccess arg0, BlockState arg1, BlockPos arg2, EnumFacing arg3)|BlockFaceShape
| getAiPathNodeType(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityLiving arg3)|PathNodeType
| getAiPathNodeType(BlockState arg0, BlockAccess arg1, BlockPos arg2)|PathNodeType
| getBeaconColorMultiplier(BlockState arg0, World arg1, BlockPos arg2, BlockPos arg3)|float[]
| getBedDirection(BlockState arg0, BlockAccess arg1, BlockPos arg2)|EnumFacing
| getBedSpawnPosition(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityPlayer arg3)|BlockPos
| getBlockLiquidHeight(World arg0, BlockPos arg1, BlockState arg2, Material arg3)|float
| getDrops(BlockAccess arg0, BlockPos arg1, BlockState arg2, int arg3)|List\<ItemStack>
| getDrops(NonNullList\<ItemStack> arg0, BlockAccess arg1, BlockPos arg2, BlockState arg3, int arg4)|void
| getEnchantPowerBonus(World arg0, BlockPos arg1)|float
| getExpDrop(BlockState arg0, BlockAccess arg1, BlockPos arg2, int arg3)|int
| getExplosionResistance(World arg0, BlockPos arg1, Entity arg2, Explosion arg3)|float
| getExtendedState(BlockState arg0, BlockAccess arg1, BlockPos arg2)|BlockState
| getFireSpreadSpeed(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|int
| getFlammability(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|int
| getFogColor(World arg0, BlockPos arg1, BlockState arg2, Entity arg3, Vec3d arg4, float arg5)|Vec3d
| getHarvestLevel(BlockState b)|int
| getHarvestTool(BlockState b)|String
| getLightOpacity(BlockState arg0, BlockAccess arg1, BlockPos arg2)|int
| getLightValue(BlockState arg0, BlockAccess arg1, BlockPos arg2)|int
| getPickBlock(BlockState arg0, RayTraceResult arg1, World arg2, BlockPos arg3, EntityPlayer arg4)|ItemStack
| getSlipperiness(BlockState arg0, BlockAccess arg1, BlockPos arg2, Entity arg3)|float
| getSoundType(BlockState arg0, World arg1, BlockPos arg2, Entity arg3)|SoundType
| getStateAtViewpoint(BlockState arg0, BlockAccess arg1, BlockPos arg2, Vec3d arg3)|BlockState
| getStateForPlacement(World arg0, BlockPos arg1, EnumFacing arg2, float arg3, float arg4, float arg5, int arg6, EntityLivingBase arg7, EnumHand arg8)|BlockState
| getValidRotations(World arg0, BlockPos arg1)|EnumFacing[]
| getWeakChanges(BlockAccess arg0, BlockPos arg1)|boolean
| hasTileEntity(BlockState b)|boolean
| isAABBInsideLiquid(World arg0, BlockPos arg1, AxisAlignedBB arg2)|Boolean
| isAABBInsideMaterial(World arg0, BlockPos arg1, AxisAlignedBB arg2, Material arg3)|Boolean
| isAir(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| isBeaconBase(BlockAccess arg0, BlockPos arg1, BlockPos arg2)|boolean
| isBed(BlockState arg0, BlockAccess arg1, BlockPos arg2, Entity arg3)|boolean
| isBedFoot(BlockAccess arg0, BlockPos arg1)|boolean
| isBurning(BlockAccess arg0, BlockPos arg1)|boolean
| isEntityInsideMaterial(BlockAccess arg0, BlockPos arg1, BlockState arg2, Entity arg3, double arg4, Material arg5, boolean arg6)|Boolean
| isFertile(World arg0, BlockPos arg1)|boolean
| isFireSource(World arg0, BlockPos arg1, EnumFacing arg2)|boolean
| isFlammable(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean
| isFoliage(BlockAccess arg0, BlockPos arg1)|boolean
| isLadder(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityLivingBase arg3)|boolean
| isLeaves(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| isNormalCube(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| isReplaceableOreGen(BlockState arg0, BlockAccess arg1, BlockPos arg2, Predicate\<BlockState> arg3)|boolean
| isSideSolid(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| isStickyBlock(BlockState b)|boolean
| isToolEffective(String arg0, BlockState arg1)|boolean
| isWood(BlockAccess arg0, BlockPos arg1)|boolean
| observedNeighborChange(BlockState arg0, World arg1, BlockPos arg2, Block arg3, BlockPos arg4)|void
| onBlockExploded(World arg0, BlockPos arg1, Explosion arg2)|void
| onNeighborChange(BlockAccess arg0, BlockPos arg1, BlockPos arg2)|void
| onPlantGrow(BlockState arg0, World arg1, BlockPos arg2, BlockPos arg3)|void
| quantityDropped(BlockState arg0, int arg1, Random arg2)|int
| recolorBlock(World arg0, BlockPos arg1, EnumFacing arg2, EnumDyeColor arg3)|boolean
| removedByPlayer(BlockState arg0, World arg1, BlockPos arg2, EntityPlayer arg3, boolean arg4)|boolean
| rotateBlock(World arg0, BlockPos arg1, EnumFacing arg2)|boolean
| setBedOccupied(BlockAccess arg0, BlockPos arg1, EntityPlayer arg2, boolean arg3)|void
| setDefaultSlipperiness(float f)|void
| setHarvestLevel(String arg0, int arg1, BlockState arg2)|void
| setHarvestLevel(String arg0, int arg1)|void
| shouldCheckWeakPower(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockIDPredicate

|Class
|--
|dev.latvian.kubejs.block.predicate.BlockIDPredicate

---

|Extends
|--
|BlockPredicate

---

|Fields|Type
|--|--
|  blockProperties|List\<BlockIDPredicate$PropertyObject>
|  blockState|BlockState

---

|Methods|Return Type
|--|--
| check(Block b)|boolean
| setHardness(float f)|void
| setHarvestLevel(String arg0, int arg1)|void
| setLightLevel(float f)|void
| setResistance(float f)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void
| with(String key, String value)|BlockIDPredicate

---

## GuiScreen

|Class
|--
|net.minecraft.client.gui.GuiScreen

---

|Extends
|--
|Gui
|GuiYesNoCallback

---

|Fields|Type
|--|--
|  field_146287_f|int
|  field_146288_g|long
|  field_146290_a|GuiButton
|  field_146291_p|boolean
|  field_146292_n|List\<GuiButton>
|  field_146294_l|int
|  field_146295_m|int
|  field_146297_k|Minecraft
|  field_146298_h|int
|  field_73735_i|float

---

|Methods|Return Type
|--|--
| func_146269_k()|void
| func_146270_b(int i)|void
| func_146274_d()|void
| func_146276_q_()|void
| func_146278_c(int i)|void
| func_146279_a(String arg0, int arg1, int arg2)|void
| func_146280_a(Minecraft arg0, int arg1, int arg2)|void
| func_146281_b()|void
| func_146282_l()|void
| func_146283_a(List\<String> arg0, int arg1, int arg2)|void
| func_175174_a(float arg0, float arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_175175_a(int arg0, int arg1, TextureAtlasSprite arg2, int arg3, int arg4)|void
| func_175273_b(Minecraft arg0, int arg1, int arg2)|void
| func_175275_f(String s)|void
| func_175276_a(TextComponent t)|boolean
| func_175281_b(String arg0, boolean arg1)|void
| func_183500_a(int arg0, int arg1)|void
| func_191927_a(ItemStack i)|List\<String>
| func_193975_a(boolean b)|void
| func_193976_p()|boolean
| func_73729_b(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73731_b(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73732_a(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73733_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73863_a(int arg0, int arg1, float arg2)|void
| func_73866_w_()|void
| func_73868_f()|boolean
| func_73876_c()|void
| func_73878_a(boolean arg0, int arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Minecraft

|Class
|--
|net.minecraft.client.Minecraft

---

|Extends
|--
|ThreadListener
|SnooperInfo

---

|Fields|Type
|--|--
|  field_110449_ao|List\<ResourcePack>
|  field_110450_ap|DefaultResourcePack
|  field_110451_am|ReloadableResourceManager
|  field_147125_j|Entity
|  field_175612_E|boolean
|  field_175618_aM|BlockRendererDispatcher
|  field_181542_y|FrameTimer
|  field_184132_p|DebugRenderer
|  field_191950_u|CreativeSettings
|  field_71412_D|File
|  field_71415_G|boolean
|  field_71417_B|MouseHelper
|  field_71424_I|Profiler
|  field_71426_K|String
|  field_71428_T|Timer
|  field_71438_f|RenderGlobal
|  field_71439_g|EntityPlayerSP
|  field_71440_d|int
|  field_71441_e|WorldClient
|  field_71442_b|PlayerControllerMP
|  field_71443_c|int
|  field_71446_o|TextureManager
|  field_71452_i|ParticleManager
|  field_71454_w|boolean
|  field_71456_v|GuiIngame
|  field_71460_t|EntityRenderer
|  field_71461_s|LoadingScreenRenderer
|  field_71462_r|GuiScreen
|  field_71464_q|FontRenderer
|  field_71466_p|FontRenderer
|  field_71467_ac|int
|  field_71474_y|GameSettings
|  field_71476_x|RayTraceResult
|  itemColors|ItemColors
|  searchTreeManager|SearchTreeManager

---

|Methods|Return Type
|--|--
| func_110432_I()|Session
| func_110434_K()|TextureManager
| func_110436_a()|void
| func_110437_J()|Proxy
| func_110438_M()|ResourcePackRepository
| func_110442_L()|ResourceManager
| func_135016_M()|LanguageManager
| func_147104_D()|ServerData
| func_147107_h()|boolean
| func_147108_a(GuiScreen g)|void
| func_147109_W()|MusicTicker$MusicType
| func_147110_a()|Framebuffer
| func_147111_S()|boolean
| func_147112_ai()|void
| func_147113_T()|boolean
| func_147114_u()|NetHandlerPlayClient
| func_147116_af()|void
| func_147117_R()|TextureMap
| func_147118_V()|SoundHandler
| func_147121_ag()|void
| func_152342_ad()|SkinManager
| func_152343_a(Callable\<V> c)|ListenableFuture\<V>
| func_152344_a(Runnable r)|ListenableFuture\<Object>
| func_152345_ab()|boolean
| func_152347_ac()|MinecraftSessionService
| func_152348_aa()|void
| func_152349_b()|boolean
| func_175597_ag()|ItemRenderer
| func_175598_ae()|RenderManager
| func_175599_af()|RenderItem
| func_175600_c()|String
| func_175601_h()|void
| func_175602_ab()|BlockRendererDispatcher
| func_175603_A()|ListenableFuture\<Object>
| func_175606_aa()|Entity
| func_175607_a(Entity e)|void
| func_180510_a(TextureManager t)|void
| func_181037_M()|PropertyMap
| func_181535_r()|MusicTicker
| func_181536_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5, int arg6, int arg7, int arg8, int arg9)|void
| func_181537_a(boolean b)|void
| func_181539_aj()|FrameTimer
| func_181540_al()|boolean
| func_184119_a(ItemStack arg0, TileEntity arg1)|ItemStack
| func_184121_ak()|float
| func_184123_d()|String
| func_184125_al()|BlockColors
| func_184126_aj()|DataFixer
| func_189648_am()|boolean
| func_193032_ao()|Tutorial
| func_193033_an()|GuiToast
| func_193986_ar()|void
| func_193987_a(SearchTreeManager$Key\<T> s)|SearchTree\<T>
| func_193989_ak()|float
| func_70000_a(Snooper s)|void
| func_70001_b(Snooper s)|void
| func_70002_Q()|boolean
| func_71351_a(ServerData s)|void
| func_71352_k()|void
| func_71353_a(WorldClient arg0, String arg1)|void
| func_71354_a(int i)|void
| func_71355_q()|boolean
| func_71356_B()|boolean
| func_71359_d()|SaveFormat
| func_71364_i()|void
| func_71370_a(int arg0, int arg1)|void
| func_71371_a(String arg0, String arg1, WorldSettings arg2)|void
| func_71372_G()|boolean
| func_71377_b(CrashReport c)|void
| func_71378_E()|Snooper
| func_71381_h()|void
| func_71385_j()|void
| func_71387_A()|boolean
| func_71396_d(CrashReport c)|CrashReport
| func_71398_f()|void
| func_71400_g()|void
| func_71401_C()|IntegratedServer
| func_71403_a(WorldClient w)|void
| func_71404_a(CrashReport c)|void
| func_71405_e()|void
| func_71407_l()|void
| func_90020_K()|int
| func_99999_d()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ClientPlayer

|Class
|--
|dev.latvian.kubejs.player.ClientPlayerJS

---

|Extends
|--
|Player

---

|Fields|Type
|--|--
|  absorptionAmount|float
|  alive|boolean
|  ambientCreature|boolean
|  animal|boolean
|  attackingEntity|LivingEntity
|  block Block position of the entity|Block
|  boss|boolean
|  child|boolean
|  creativeMode|boolean
|  customName Custom display name|String
|  customNameAlwaysVisible Custom display name will always be visible above head|boolean
|  data Temporary data, mods can attach objects to this|AttachedData
|  displayName|Text
|  elytraFlying|boolean
|  eyeHeight|float
|  facing|EnumFacing
|  fake|boolean
|  fallDistance|float
|  foodLevel|int
|  frame|boolean
|  fullNBT Entity NBT|NBTCompound
|  glowing|boolean
|  hasCustomName Checks if custom display name is set|boolean
|  health|float
|  horizontalFacing|EnumFacing
|  id|UUID
|  idleTime|int
|  inventory|Inventory
|  invisible|boolean
|  item|ItemStack
|  lastAttackedEntity|LivingEntity
|  lastAttackedEntityTime|int
|  lastDamageSource|DamageSource
|  living|boolean
|  mainHandItem|ItemStack
|  maxHealth|float
|  minecraftEntity|Entity
|  minecraftLivingEntity|EntityLivingBase
|  minecraftPlayer|EntityPlayer
|  miningBlock|boolean
|  monster|boolean
|  motionX|double
|  motionY|double
|  motionZ|double
|  mouseItem|ItemStack
|  movementSpeed|float
|  name|String
|  nbt|NBTCompound
|  noClip|boolean
|  noGravity|boolean
|  offHandItem|ItemStack
|  onGround|boolean
|  onLadder|boolean
|  openInventory|Container
|  passengers|EntityArrayList
|  pitch|float
|  player|boolean
|  potionEffects|EntityPotionEffects
|  profile|GameProfile
|  reachDistance|double
|  recursivePassengers|EntityArrayList
|  revengeTarget|LivingEntity
|  revengeTimer|int
|  ridingEntity|Entity
|  selectedSlot|int
|  server|Server
|  silent|boolean
|  sleeping|boolean
|  sneaking|boolean
|  spectator|boolean
|  sprinting|boolean
|  stats|PlayerStats
|  stepHeight|float
|  tags|Set\<String>
|  teamID Scoreboard team ID|String
|  ticksExisted|int
|  type|ID
|  undead|boolean
|  waterCreature|boolean
|  world|World
|  x|double
|  xp|int
|  xpLevel|int
|  y|double
|  yaw|float
|  z|double

---

|Methods|Return Type
|--|--
| addExhaustion(float f)|void
| addFood(int food, float modifier)|void
| addMotion(double x, double y, double z)|void
| addXP(int xp)|void
| addXPLevels(int levels)|void
| attack(float hp)|void
| attack(String source, float hp)|void
| boostElytraFlight()|void
| canEntityBeSeen(Entity entity)|boolean
| closeInventory()|void
| closeOverlay(String s)|void
| closeOverlay(Overlay o)|void
| damageHeldItem()|void
| damageHeldItem(EnumHand hand, int amount)|void
| dismountRidingEntity()|void
| extinguish()|void
| getEquipment(EntityEquipmentSlot slot)|ItemStack
| getHeldItem(EnumHand hand)|ItemStack
| getNBTData(String key) Get specific value from custom NBT|NBTBase
| give(ItemStack item)|void
| giveInHand(ItemStack item)|void
| heal(float hp)|void
| isHoldingInAnyHand(Ingredient ingredient)|boolean
| isOnSameTeam(Entity entity) Checks if this entity is on the same scoreboard team as another entity|boolean
| isOnScoreboardTeam(String teamID) Checks if this entity is on scoreboard team|boolean
| isPassenger(Entity entity)|boolean
| kill()|void
| openOverlay(Overlay o)|void
| playSound(Object id, float volume, float pitch) Play sound at entity. Must be played from server side|void
| playSound(Object id) Play sound at entity. Must be played from server side|void
| rayTrace()|Map\<String, Object>
| rayTrace(double distance)|Map\<String, Object>
| removePassengers()|void
| runCommand(String command) Runs command as if the sender was running it, ignoring permissions|int
| sendData(String channel, Object data)|void
| sendInventoryUpdate()|void
| setEquipment(EntityEquipmentSlot slot, ItemStack item)|void
| setHeldItem(EnumHand hand, ItemStack item)|void
| setMotion(double x, double y, double z)|void
| setNBTData(String key, Object nbt) Set specific value in custom NBT|void
| setOnFire(int seconds) Sets entity on fire for x seconds|void
| setPosition(double x, double y, double z)|void
| setPosition(Block block)|void
| setPositionAndRotation(double x, double y, double z, float yaw, float pitch)|void
| setRotation(float yaw, float pitch)|void
| setStatusMessage(Object message)|void
| spawn()|void
| startRiding(Entity entity, boolean force)|boolean
| swingArm(EnumHand hand)|void
| tell(Text message) Tell message in chat|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ClientWorld

|Class
|--
|dev.latvian.kubejs.world.ClientWorldJS

---

|Extends
|--
|World

---

|Fields|Type
|--|--
|  clientPlayerData|ClientPlayerData
|  data Temporary data, mods can attach objects to this|AttachedData
|  daytime|boolean
|  dimension|int
|  entities|EntityArrayList
|  gameRules|GameRules
|  localTime|long
|  minecraft|Minecraft
|  minecraftWorld|World
|  overworld|boolean
|  players|EntityArrayList
|  raining|boolean
|  seed|long
|  server|Server
|  thundering|boolean
|  time|long

---

|Methods|Return Type
|--|--
| createEntity(Object o)|Entity
| createEntityList(Collection\<? extends net.minecraft.entity.Entity> c)|EntityArrayList
| createExplosion(double x, double y, double z)|Explosion
| getBlock(int x, int y, int z)|Block
| getBlock(BlockPos pos)|Block
| getBlock(TileEntity blockEntity)|Block
| getEntity(Entity e)|Entity
| getLivingEntity(Entity e)|LivingEntity
| getPlayer(Entity e)|Player
| getPlayerData(EntityPlayer e)|ClientPlayerData
| getPlayerData(EntityPlayer e)|PlayerData
| setRainStrength(float strength)|void
| spawnFireworks(double x, double y, double z, Fireworks properties)|void
| spawnLightning(double x, double y, double z, boolean effectOnly)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EventHandler

|Interface
|--
|dev.latvian.kubejs.event.IEventHandler

---

|Extends
|--

---

|Methods|Return Type
|--|--
| onEvent(Event e)|void

---

## Fluid

|Class
|--
|net.minecraftforge.fluids.Fluid

---

|Extends
|--

---

|Fields|Type
|--|--
|  block|Block
|  color|int
|  density|int
|  emptySound|SoundEvent
|  fillSound|SoundEvent
|  flowing|ResourceLocation
|  gaseous|boolean
|  lighterThanAir|boolean
|  luminosity|int
|  name|String
|  overlay|ResourceLocation
|  rarity|EnumRarity
|  still|ResourceLocation
|  temperature|int
|  unlocalizedName|String
|  viscosity|int

---

|Methods|Return Type
|--|--
| canBePlacedInWorld()|boolean
| doesVaporize(FluidStack f)|boolean
| getLocalizedName(FluidStack f)|String
| vaporize(EntityPlayer arg0, World arg1, BlockPos arg2, FluidStack arg3)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## FluidStack

|Class
|--
|dev.latvian.kubejs.fluid.FluidStackJS

---

|Extends
|--

---

|Fields|Type
|--|--
|  amount|int
|  empty|boolean
|  fluid|Fluid
|  fluidName|String
|  fluidStack|FluidStack
|  nbt|NBTCompound

---

|Methods|Return Type
|--|--
| amount(int i)|FluidStack
| copy()|FluidStack
| nbt(Object o)|FluidStack
| strongEquals(Object o)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ChangeProgress

|Class
|--
|com.feed_the_beast.ftbquests.quest.ChangeProgress

---

|Extends
|--
|Enum
|WithID

---

|Fields|Type
|--|--
|  complete|boolean
|  declaringClass|Class\<E>
|  dependencies|boolean
|  id|String
|  reset|boolean

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## QuestObjectType

|Class
|--
|com.feed_the_beast.ftbquests.quest.QuestObjectType

---

|Extends
|--
|Enum
|WithID
|Predicate

---

|Fields|Type
|--|--
|  color|TextFormatting
|  declaringClass|Class\<E>
|  displayName|String
|  flag|int
|  id|String
|  translationKey|String

---

|Methods|Return Type
|--|--
| and(Predicate\<? super T> p)|Predicate\<T>
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| negate()|Predicate\<T>
| or(Predicate\<? super T> p)|Predicate\<T>
| ordinal()|int
| test(Object o)|boolean
| test(QuestObjectBase q)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## QuestShape

|Class
|--
|com.feed_the_beast.ftbquests.quest.QuestShape

---

|Extends
|--
|Icon
|WithID

---

|Fields|Type
|--|--
|  background|ImageIcon
|  empty|boolean
|  id|String
|  ingredient|Object
|  json|JsonElement
|  outline|ImageIcon
|  shape|ImageIcon

---

|Methods|Return Type
|--|--
| bindTexture()|void
| combineWith(Icon[] i)|Icon
| combineWith(Icon i)|Icon
| copy()|Icon
| createPixelBuffer()|PixelBuffer
| draw(int arg0, int arg1, int arg2, int arg3, Color4I arg4)|void
| draw(int arg0, int arg1, int arg2, int arg3)|void
| draw3D(Color4I c)|void
| drawStatic(int arg0, int arg1, int arg2, int arg3)|void
| hasPixelBuffer()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void
| withBorder(int i)|Icon
| withOutline(Color4I arg0, boolean arg1)|Icon
| withTint(Color4I c)|Icon

---

## World

|Class
|--
|dev.latvian.kubejs.world.WorldJS

---

|Extends
|--
|WithAttachedData

---

|Fields|Type
|--|--
|  data Temporary data, mods can attach objects to this|AttachedData
|  daytime|boolean
|  dimension|int
|  entities|EntityArrayList
|  gameRules|GameRules
|  localTime|long
|  minecraftWorld|World
|  overworld|boolean
|  players|EntityArrayList
|  raining|boolean
|  seed|long
|  server|Server
|  thundering|boolean
|  time|long

---

|Methods|Return Type
|--|--
| createEntity(Object o)|Entity
| createEntityList(Collection\<? extends net.minecraft.entity.Entity> c)|EntityArrayList
| createExplosion(double x, double y, double z)|Explosion
| getBlock(int x, int y, int z)|Block
| getBlock(BlockPos pos)|Block
| getBlock(TileEntity blockEntity)|Block
| getEntity(Entity e)|Entity
| getLivingEntity(Entity e)|LivingEntity
| getPlayer(Entity e)|Player
| setRainStrength(float strength)|void
| spawnFireworks(double x, double y, double z, Fireworks properties)|void
| spawnLightning(double x, double y, double z, boolean effectOnly)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## QuestData

|Class
|--
|com.feed_the_beast.ftbquests.quest.QuestData

---

|Extends
|--

---

|Fields|Type
|--|--
|  areDependenciesCompleteCache|Int2ByteOpenHashMap
|  claimedPlayerRewards|Map\<UUID, IntOpenHashSet>
|  claimedTeamRewards|IntOpenHashSet
|  displayName|TextComponent
|  file|QuestFile
|  onlineMembers|List\<? extends net.minecraft.entity.player.EntityPlayer>
|  progressCache|Int2ByteOpenHashMap
|  taskData|Int2ObjectOpenHashMap\<TaskData>
|  teamID|String
|  teamUID|short

---

|Methods|Return Type
|--|--
| checkAutoCompletion(Quest q)|void
| createTaskData(Task t)|void
| getTaskData(Task t)|TaskData
| isRewardClaimed(UUID arg0, Reward arg1)|boolean
| markDirty()|void
| removeTask(Task t)|void
| setRewardClaimed(UUID arg0, Reward arg1)|boolean
| unclaimRewards(Collection\<Reward> c)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Player

|Class
|--
|dev.latvian.kubejs.player.PlayerJS

---

|Extends
|--
|LivingEntity
|WithAttachedData

---

|Attached
|--
|FTB Quests Player Data ftbquests
|GameStagesPlayerData gamestages

---

|Fields|Type
|--|--
|  absorptionAmount|float
|  alive|boolean
|  ambientCreature|boolean
|  animal|boolean
|  attackingEntity|LivingEntity
|  block Block position of the entity|Block
|  boss|boolean
|  child|boolean
|  creativeMode|boolean
|  customName Custom display name|String
|  customNameAlwaysVisible Custom display name will always be visible above head|boolean
|  data Temporary data, mods can attach objects to this|AttachedData
|  displayName|Text
|  elytraFlying|boolean
|  eyeHeight|float
|  facing|EnumFacing
|  fake|boolean
|  fallDistance|float
|  foodLevel|int
|  frame|boolean
|  fullNBT Entity NBT|NBTCompound
|  glowing|boolean
|  hasCustomName Checks if custom display name is set|boolean
|  health|float
|  horizontalFacing|EnumFacing
|  id|UUID
|  idleTime|int
|  inventory|Inventory
|  invisible|boolean
|  item|ItemStack
|  lastAttackedEntity|LivingEntity
|  lastAttackedEntityTime|int
|  lastDamageSource|DamageSource
|  living|boolean
|  mainHandItem|ItemStack
|  maxHealth|float
|  minecraftEntity|Entity
|  minecraftLivingEntity|EntityLivingBase
|  minecraftPlayer|EntityPlayer
|  miningBlock|boolean
|  monster|boolean
|  motionX|double
|  motionY|double
|  motionZ|double
|  mouseItem|ItemStack
|  movementSpeed|float
|  name|String
|  nbt|NBTCompound
|  noClip|boolean
|  noGravity|boolean
|  offHandItem|ItemStack
|  onGround|boolean
|  onLadder|boolean
|  openInventory|Container
|  passengers|EntityArrayList
|  pitch|float
|  player|boolean
|  potionEffects|EntityPotionEffects
|  profile|GameProfile
|  reachDistance|double
|  recursivePassengers|EntityArrayList
|  revengeTarget|LivingEntity
|  revengeTimer|int
|  ridingEntity|Entity
|  selectedSlot|int
|  server|Server
|  silent|boolean
|  sleeping|boolean
|  sneaking|boolean
|  spectator|boolean
|  sprinting|boolean
|  stats|PlayerStats
|  stepHeight|float
|  tags|Set\<String>
|  teamID Scoreboard team ID|String
|  ticksExisted|int
|  type|ID
|  undead|boolean
|  waterCreature|boolean
|  world|World
|  x|double
|  xp|int
|  xpLevel|int
|  y|double
|  yaw|float
|  z|double

---

|Methods|Return Type
|--|--
| addExhaustion(float f)|void
| addFood(int food, float modifier)|void
| addMotion(double x, double y, double z)|void
| addXP(int xp)|void
| addXPLevels(int levels)|void
| attack(float hp)|void
| attack(String source, float hp)|void
| boostElytraFlight()|void
| canEntityBeSeen(Entity entity)|boolean
| closeInventory()|void
| closeOverlay(Overlay o)|void
| closeOverlay(String s)|void
| damageHeldItem()|void
| damageHeldItem(EnumHand hand, int amount)|void
| dismountRidingEntity()|void
| extinguish()|void
| getEquipment(EntityEquipmentSlot slot)|ItemStack
| getHeldItem(EnumHand hand)|ItemStack
| getNBTData(String key) Get specific value from custom NBT|NBTBase
| give(ItemStack item)|void
| giveInHand(ItemStack item)|void
| heal(float hp)|void
| isHoldingInAnyHand(Ingredient ingredient)|boolean
| isOnSameTeam(Entity entity) Checks if this entity is on the same scoreboard team as another entity|boolean
| isOnScoreboardTeam(String teamID) Checks if this entity is on scoreboard team|boolean
| isPassenger(Entity entity)|boolean
| kill()|void
| openOverlay(Overlay o)|void
| playSound(Object id, float volume, float pitch) Play sound at entity. Must be played from server side|void
| playSound(Object id) Play sound at entity. Must be played from server side|void
| rayTrace()|Map\<String, Object>
| rayTrace(double distance)|Map\<String, Object>
| removePassengers()|void
| runCommand(String command) Runs command as if the sender was running it, ignoring permissions|int
| sendData(String channel, Object data)|void
| sendInventoryUpdate()|void
| setEquipment(EntityEquipmentSlot slot, ItemStack item)|void
| setHeldItem(EnumHand hand, ItemStack item)|void
| setMotion(double x, double y, double z)|void
| setNBTData(String key, Object nbt) Set specific value in custom NBT|void
| setOnFire(int seconds) Sets entity on fire for x seconds|void
| setPosition(double x, double y, double z)|void
| setPosition(Block block)|void
| setPositionAndRotation(double x, double y, double z, float yaw, float pitch)|void
| setRotation(float yaw, float pitch)|void
| setStatusMessage(Object message)|void
| spawn()|void
| startRiding(Entity entity, boolean force)|boolean
| swingArm(EnumHand hand)|void
| tell(Text message) Tell message in chat|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## QuestFile

|Class
|--
|com.feed_the_beast.ftbquests.quest.QuestFile

---

|Extends
|--
|QuestObject

---

|Fields|Type
|--|--
|  allData|Collection\<? extends com.feed_the_beast.ftbquests.quest.QuestData>
|  allObjects|Collection\<QuestObjectBase>
|  altIcon|Icon
|  altTitle|String
|  chapters|List\<Chapter>
|  client|boolean
|  codeString|String
|  defaultQuestDisableJEI|boolean
|  defaultRewardAutoclaim|RewardAutoClaim
|  defaultRewardTeam|boolean
|  defaultShape|QuestShape
|  defaultTeamConsumeItems|boolean
|  disableGui|boolean
|  disableToast|boolean
|  dropLootCrates|boolean
|  emergencyItems|List\<ItemStack>
|  emergencyItemsCooldown|Ticks
|  file|File
|  fileVersion|int
|  folder|File
|  folderName|String
|  fullScreenQuestView|boolean
|  icon|Icon
|  id|int
|  invalid|boolean
|  loading|boolean
|  lootCrateNoDrop|EntityWeight
|  objectType|QuestObjectType
|  parentID|int
|  questChapter|Chapter
|  questFile|QuestFile
|  rewardTables|List\<RewardTable>
|  tags|Set\<String>
|  title|String
|  unformattedTitle|String
|  yellowDisplayName|String

---

|Methods|Return Type
|--|--
| cacheProgress()|boolean
| canEdit()|boolean
| changeProgress(QuestData arg0, ChangeProgress arg1)|void
| clearCachedData()|void
| clearCachedProgress()|void
| collect(Class\<T> c)|List\<T>
| collect(Class\<T> arg0, Predicate\<QuestObjectBase> arg1)|List\<T>
| create(QuestObjectType arg0, int arg1, NBTTagCompound arg2)|QuestObjectBase
| createSubGroup(ConfigGroup c)|ConfigGroup
| createTabContent()|Optional\<Node>
| deleteChildren()|void
| deleteObject(int i)|void
| deleteSelf()|void
| editedFromGUI()|void
| forceProgress(QuestData arg0, ChangeProgress arg1, boolean arg2)|void
| get(int i)|QuestObject
| getBase(int i)|QuestObjectBase
| getChapter(int i)|Chapter
| getConfig(ConfigGroup c)|void
| getData(Entity e)|QuestData
| getData(short s)|QuestData
| getData(String s)|QuestData
| getID(Object o)|int
| getLootCrate(String s)|LootCrate
| getQuest(int i)|Quest
| getRandomLootCrate(Entity arg0, Random arg1)|LootCrate
| getRelativeProgress(QuestData q)|int
| getRelativeProgressFromChildren(QuestData q)|int
| getReward(int i)|Reward
| getRewardTable(String s)|RewardTable
| getRewardTable(int i)|RewardTable
| getTask(int i)|Task
| getUnclaimedRewards(UUID arg0, QuestData arg1, boolean arg2)|int
| getVisibleChapters(QuestData arg0, boolean arg1)|List\<Chapter>
| hasTag(String s)|boolean
| isComplete(QuestData q)|boolean
| isStarted(QuestData q)|boolean
| isVisible(QuestData q)|boolean
| loadText()|QuestObjectText
| onCompleted(QuestData arg0, List\<EntityPlayerMP> arg1)|void
| onCreated()|void
| onEditButtonClicked()|void
| readData(NBTTagCompound n)|void
| readDataFull(File f)|void
| readID(int i)|int
| readIndex(File f)|int[]
| readNetData(DataIn d)|void
| readNetDataFull(DataIn d)|void
| refreshIDMap()|void
| refreshJEI()|int
| remove(int i)|QuestObjectBase
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeData(NBTTagCompound n)|void
| writeDataFull(File f)|void
| writeNetData(DataOut d)|void
| writeNetDataFull(DataOut d)|void

---

## QuestObjectBase

|Class
|--
|com.feed_the_beast.ftbquests.quest.QuestObjectBase

---

|Extends
|--

---

|Fields|Type
|--|--
|  altIcon|Icon
|  altTitle|String
|  codeString|String
|  file|File
|  icon|Icon
|  id|int
|  invalid|boolean
|  objectType|QuestObjectType
|  parentID|int
|  questChapter|Chapter
|  questFile|QuestFile
|  tags|Set\<String>
|  title|String
|  unformattedTitle|String
|  yellowDisplayName|String

---

|Methods|Return Type
|--|--
| changeProgress(QuestData arg0, ChangeProgress arg1)|void
| clearCachedData()|void
| createSubGroup(ConfigGroup c)|ConfigGroup
| createTabContent()|Optional\<Node>
| deleteChildren()|void
| deleteSelf()|void
| editedFromGUI()|void
| forceProgress(QuestData arg0, ChangeProgress arg1, boolean arg2)|void
| getConfig(ConfigGroup c)|void
| hasTag(String s)|boolean
| loadText()|QuestObjectText
| onCreated()|void
| onEditButtonClicked()|void
| readData(NBTTagCompound n)|void
| readNetData(DataIn d)|void
| refreshJEI()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeData(NBTTagCompound n)|void
| writeNetData(DataOut d)|void

---

## Ingredient

|Interface
|--
|dev.latvian.kubejs.item.ingredient.IngredientJS

---

|Extends
|--

---

|Fields|Type
|--|--
|  count|int
|  empty|boolean
|  first|ItemStack
|  stacks|Set\<ItemStack>
|  vanillaPredicate|Predicate\<ItemStack>

---

|Methods|Return Type
|--|--
| count(int i)|Ingredient
| filter(Ingredient i)|Ingredient
| not()|Ingredient
| test(ItemStack i)|boolean
| testVanilla(ItemStack i)|boolean

---

## ItemStack

|Class
|--
|dev.latvian.kubejs.item.ItemStackJS

---

|Extends
|--
|Ingredient

---

|Fields|Type
|--|--
|  block|boolean
|  copy|ItemStack
|  count|int
|  data|int
|  empty|boolean
|  enchantments|Map\<ID, int>
|  first|ItemStack
|  id|ID
|  item|Item
|  itemStack|ItemStack
|  mod|String
|  name|Text
|  nbt|NBTCompound
|  nbtOrNew|NBTCompound
|  stacks|Set\<ItemStack>
|  vanillaPredicate|Predicate\<ItemStack>

---

|Methods|Return Type
|--|--
| addLore(Object o)|void
| areItemsEqual(ItemStack i)|boolean
| areItemsEqual(ItemStack i)|boolean
| count(int i)|ItemStack
| count(int i)|Ingredient
| data(int i)|ItemStack
| enchant(Map\<Object, int> m)|ItemStack
| filter(Ingredient i)|Ingredient
| getEnchantment(Object o)|int
| getHarvestLevel(String arg0, Player arg1, Block arg2)|int
| getHarvestLevel(String s)|int
| hasSubItems()|boolean
| ignoreNBT()|IgnoreNBTIngredient
| name(String s)|ItemStack
| nbt(Object o)|ItemStack
| not()|Ingredient
| strongEquals(Object o)|boolean
| test(ItemStack i)|boolean
| testVanilla(ItemStack i)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void
| wildcardData()|ItemStack

---

## Fireworks

|Class
|--
|dev.latvian.kubejs.world.FireworksJS

---

|Extends
|--

---

|Fields|Type
|--|--
|  explosions|List\<FireworksJS$Explosion>
|  flight|int
|  lifeTime|int

---

|Methods|Return Type
|--|--
| createFireworkRocket(World arg0, double arg1, double arg2, double arg3)|EntityFireworkRocket
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Item

|Class
|--
|net.minecraft.item.Item

---

|Extends
|--
|IForgeRegistryEntry$Impl

---

|Fields|Type
|--|--
|  creativeTabs|CreativeTabs[]
|  delegate|RegistryDelegate\<T>
|  registryName|ResourceLocation
|  registryType|Class\<T>
|  repairable|boolean
|  tileEntityItemStackRenderer|TileEntityItemStackRenderer

---

|Methods|Return Type
|--|--
| canApplyAtEnchantingTable(ItemStack arg0, Enchantment arg1)|boolean
| canContinueUsing(ItemStack arg0, ItemStack arg1)|boolean
| canDestroyBlockInCreative(World arg0, BlockPos arg1, ItemStack arg2, EntityPlayer arg3)|boolean
| canDisableShield(ItemStack arg0, ItemStack arg1, EntityLivingBase arg2, EntityLivingBase arg3)|boolean
| canHarvestBlock(BlockState arg0, ItemStack arg1)|boolean
| createEntity(World arg0, Entity arg1, ItemStack arg2)|Entity
| doesSneakBypassUse(ItemStack arg0, BlockAccess arg1, BlockPos arg2, EntityPlayer arg3)|boolean
| func_111205_h(EntityEquipmentSlot e)|Multimap\<String, AttributeModifier>
| func_111207_a(ItemStack arg0, EntityPlayer arg1, EntityLivingBase arg2, EnumHand arg3)|boolean
| func_150893_a(ItemStack arg0, BlockState arg1)|float
| func_150895_a(CreativeTabs arg0, NonNullList\<ItemStack> arg1)|void
| func_150897_b(BlockState b)|boolean
| func_179215_a(NBTTagCompound n)|boolean
| func_179218_a(ItemStack arg0, World arg1, BlockState arg2, BlockPos arg3, EntityLivingBase arg4)|boolean
| func_180614_a(EntityPlayer arg0, World arg1, BlockPos arg2, EnumHand arg3, EnumFacing arg4, float arg5, float arg6, float arg7)|EnumActionResult
| func_185040_i()|boolean
| func_185043_a(ResourceLocation arg0, ItemPropertyGetter arg1)|void
| func_185045_a(ResourceLocation r)|ItemPropertyGetter
| func_190903_i()|ItemStack
| func_194125_a(CreativeTabs c)|boolean
| func_77612_l()|int
| func_77613_e(ItemStack i)|EnumRarity
| func_77614_k()|boolean
| func_77615_a(ItemStack arg0, World arg1, EntityLivingBase arg2, int arg3)|void
| func_77616_k(ItemStack i)|boolean
| func_77619_b()|int
| func_77622_d(ItemStack arg0, World arg1, EntityPlayer arg2)|void
| func_77624_a(ItemStack arg0, World arg1, List\<String> arg2, TooltipFlag arg3)|void
| func_77625_d(int i)|Item
| func_77626_a(ItemStack i)|int
| func_77627_a(boolean b)|Item
| func_77629_n_()|boolean
| func_77634_r()|boolean
| func_77636_d(ItemStack i)|boolean
| func_77637_a(CreativeTabs c)|Item
| func_77639_j()|int
| func_77640_w()|CreativeTabs
| func_77642_a(Item i)|Item
| func_77643_m_()|boolean
| func_77644_a(ItemStack arg0, EntityLivingBase arg1, EntityLivingBase arg2)|boolean
| func_77645_m()|boolean
| func_77647_b(int i)|int
| func_77651_p()|boolean
| func_77653_i(ItemStack i)|String
| func_77654_b(ItemStack arg0, World arg1, EntityLivingBase arg2)|ItemStack
| func_77655_b(String s)|Item
| func_77656_e(int i)|Item
| func_77657_g(ItemStack i)|String
| func_77658_a()|String
| func_77659_a(World arg0, EntityPlayer arg1, EnumHand arg2)|ActionResult\<ItemStack>
| func_77661_b(ItemStack i)|EnumAction
| func_77662_d()|boolean
| func_77663_a(ItemStack arg0, World arg1, Entity arg2, int arg3, boolean arg4)|void
| func_77664_n()|Item
| func_77667_c(ItemStack i)|String
| func_77668_q()|Item
| func_82788_x()|boolean
| func_82789_a(ItemStack arg0, ItemStack arg1)|boolean
| getAnimationParameters(ItemStack arg0, World arg1, EntityLivingBase arg2)|ImmutableMap\<String, TimeValue>
| getArmorModel(EntityLivingBase arg0, ItemStack arg1, EntityEquipmentSlot arg2, ModelBiped arg3)|ModelBiped
| getArmorTexture(ItemStack arg0, Entity arg1, EntityEquipmentSlot arg2, String arg3)|String
| getAttributeModifiers(EntityEquipmentSlot arg0, ItemStack arg1)|Multimap\<String, AttributeModifier>
| getContainerItem(ItemStack i)|ItemStack
| getCreatorModId(ItemStack i)|String
| getDamage(ItemStack i)|int
| getDurabilityForDisplay(ItemStack i)|double
| getEntityLifespan(ItemStack arg0, World arg1)|int
| getEquipmentSlot(ItemStack i)|EntityEquipmentSlot
| getFontRenderer(ItemStack i)|FontRenderer
| getForgeRarity(ItemStack i)|Rarity
| getHarvestLevel(ItemStack arg0, String arg1, EntityPlayer arg2, BlockState arg3)|int
| getHighlightTip(ItemStack arg0, String arg1)|String
| getHorseArmorTexture(EntityLiving arg0, ItemStack arg1)|String
| getHorseArmorType(ItemStack i)|HorseArmorType
| getItemBurnTime(ItemStack i)|int
| getItemEnchantability(ItemStack i)|int
| getItemStackLimit(ItemStack i)|int
| getMaxDamage(ItemStack i)|int
| getMetadata(ItemStack i)|int
| getNBTShareTag(ItemStack i)|NBTTagCompound
| getRGBDurabilityForDisplay(ItemStack i)|int
| getSmeltingExperience(ItemStack i)|float
| getToolClasses(ItemStack i)|Set\<String>
| getXpRepairRatio(ItemStack i)|float
| hasContainerItem(ItemStack i)|boolean
| hasCustomEntity(ItemStack i)|boolean
| initCapabilities(ItemStack arg0, NBTTagCompound arg1)|CapabilityProvider
| isBeaconPayment(ItemStack i)|boolean
| isBookEnchantable(ItemStack arg0, ItemStack arg1)|boolean
| isDamaged(ItemStack i)|boolean
| isShield(ItemStack arg0, EntityLivingBase arg1)|boolean
| isValidArmor(ItemStack arg0, EntityEquipmentSlot arg1, Entity arg2)|boolean
| onArmorTick(World arg0, EntityPlayer arg1, ItemStack arg2)|void
| onBlockStartBreak(ItemStack arg0, BlockPos arg1, EntityPlayer arg2)|boolean
| onDroppedByPlayer(ItemStack arg0, EntityPlayer arg1)|boolean
| onEntityItemUpdate(EntityItem e)|boolean
| onEntitySwing(EntityLivingBase arg0, ItemStack arg1)|boolean
| onHorseArmorTick(World arg0, EntityLiving arg1, ItemStack arg2)|void
| onItemUseFirst(EntityPlayer arg0, World arg1, BlockPos arg2, EnumFacing arg3, float arg4, float arg5, float arg6, EnumHand arg7)|EnumActionResult
| onLeftClickEntity(ItemStack arg0, EntityPlayer arg1, Entity arg2)|boolean
| onUsingTick(ItemStack arg0, EntityLivingBase arg1, int arg2)|void
| readNBTShareTag(ItemStack arg0, NBTTagCompound arg1)|void
| renderHelmetOverlay(ItemStack arg0, EntityPlayer arg1, ScaledResolution arg2, float arg3)|void
| setDamage(ItemStack arg0, int arg1)|void
| setHarvestLevel(String arg0, int arg1)|void
| setNoRepair()|Item
| shouldCauseBlockBreakReset(ItemStack arg0, ItemStack arg1)|boolean
| shouldCauseReequipAnimation(ItemStack arg0, ItemStack arg1, boolean arg2)|boolean
| showDurabilityBar(ItemStack i)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ScriptModData$ModInfo

|Class
|--
|dev.latvian.kubejs.script.ScriptModData$ModInfo

---

|Extends
|--

---

|Fields|Type
|--|--
|  id|String
|  name|String
|  version|String

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NBTString

|Class
|--
|dev.latvian.kubejs.util.nbt.NBTStringJS

---

|Extends
|--
|NBTBase

---

|Fields|Type
|--|--
|  copy|NBTBase
|  empty|boolean
|  id|byte
|  nbtString|String
|  string|String

---

|Methods|Return Type
|--|--
| asByte()|byte
| asByteArray()|byte[]
| asCompound()|NBTCompound
| asDouble()|double
| asFloat()|float
| asInt()|int
| asIntArray()|int[]
| asList()|NBTList
| asLong()|long
| asLongArray()|long[]
| asNumber()|Number
| asShort()|short
| asString()|String
| createNBT()|NBTBase
| isNull()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NBTCompound

|Class
|--
|dev.latvian.kubejs.util.nbt.NBTCompoundJS

---

|Extends
|--
|NBTBase

---

|Fields|Type
|--|--
|  copy|NBTCompound
|  empty|boolean
|  id|byte
|  nbtString|String
|  size|int

---

|Methods|Return Type
|--|--
| asByte()|byte
| asByteArray()|byte[]
| asCompound()|NBTCompound
| asDouble()|double
| asFloat()|float
| asInt()|int
| asIntArray()|int[]
| asList()|NBTList
| asLong()|long
| asLongArray()|long[]
| asNumber()|Number
| asShort()|short
| asString()|String
| compoundOrNew(String s)|NBTCompound
| createNBT()|NBTBase
| createNBT()|NBTTagCompound
| get(String s)|NBTBase
| get(String arg0, int arg1)|NBTBase
| isNull()|boolean
| listOrNew(String s)|NBTList
| remove(String s)|NBTBase
| set(String arg0, Object arg1)|NBTBase
| set(Map\<String, Object> m)|NBTCompound
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NBTList

|Class
|--
|dev.latvian.kubejs.util.nbt.NBTListJS

---

|Extends
|--
|NBTBase
|Iterable

---

|Fields|Type
|--|--
|  copy|NBTBase
|  empty|boolean
|  id|byte
|  nbtString|String
|  size|int

---

|Methods|Return Type
|--|--
| add(Object o)|void
| asByte()|byte
| asByteArray()|byte[]
| asCompound()|NBTCompound
| asDouble()|double
| asFloat()|float
| asInt()|int
| asIntArray()|int[]
| asList()|NBTList
| asLong()|long
| asLongArray()|long[]
| asNumber()|Number
| asShort()|short
| asString()|String
| compoundOrNew(int i)|NBTCompound
| createNBT()|NBTBase
| forEach(Consumer\<? super T> c)|void
| get(int i)|NBTBase
| isNull()|boolean
| iterator()|Iterator\<NBTBase>
| listOrNew(int i)|NBTList
| remove(int i)|NBTBase
| set(int arg0, Object arg1)|NBTBase
| spliterator()|Spliterator\<T>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NBTNull

|Class
|--
|dev.latvian.kubejs.util.nbt.NBTNullJS

---

|Extends
|--
|NBTBase

---

|Fields|Type
|--|--
|  copy|NBTBase
|  empty|boolean
|  id|byte
|  nbtString|String

---

|Methods|Return Type
|--|--
| asByte()|byte
| asByteArray()|byte[]
| asCompound()|NBTCompound
| asDouble()|double
| asFloat()|float
| asInt()|int
| asIntArray()|int[]
| asList()|NBTList
| asLong()|long
| asLongArray()|long[]
| asNumber()|Number
| asShort()|short
| asString()|String
| createNBT()|NBTBase
| isNull()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NBTBase

|Interface
|--
|dev.latvian.kubejs.util.nbt.NBTBaseJS

---

|Extends
|--

---

|Fields|Type
|--|--
|  copy|NBTBase
|  empty|boolean
|  id|byte
|  nbtString|String

---

|Methods|Return Type
|--|--
| asByte()|byte
| asByteArray()|byte[]
| asCompound()|NBTCompound
| asDouble()|double
| asFloat()|float
| asInt()|int
| asIntArray()|int[]
| asList()|NBTList
| asLong()|long
| asLongArray()|long[]
| asNumber()|Number
| asShort()|short
| asString()|String
| createNBT()|NBTBase
| isNull()|boolean

---

## Text

|Class
|--
|dev.latvian.kubejs.text.Text

---

|Extends
|--
|Iterable
|Comparable
|JsonSerializable

---

|Fields|Type
|--|--
|  formattedString|String
|  json Convert text to json|JsonElement
|  propertiesAsJson|JsonObject
|  siblings List of siblings|List\<Text>
|  unformattedString|String

---

|Methods|Return Type
|--|--
| append(Text sibling) Append text and end of this one|Text
| aqua() Set color to aqua|Text
| black() Set color to black|Text
| blue() Set color to blue|Text
| bold(Boolean b) Set bold|Text
| bold() Set bold|Text
| click(String s) Set click URL|Text
| color(TextColor value) Set color|Text
| compareTo(Text t)|int
| compareTo(Object o)|int
| component()|TextComponent
| copy() Create a deep copy of this text|Text
| darkAqua() Set color to dark aqua|Text
| darkBlue() Set color to dark blue|Text
| darkGray() Set color to dark gray|Text
| darkGreen() Set color to dark green|Text
| darkPurple() Set color to dark purple|Text
| darkRed() Set color to dark red|Text
| forEach(Consumer\<? super T> c)|void
| gold() Set color to gold|Text
| gray() Set color to gray|Text
| green() Set color to green|Text
| hasSiblings() True if this text component has sibling components|boolean
| hover(Text text) Set hover text|Text
| insertion(String s) Set insertion text|Text
| italic() Set italic|Text
| italic(Boolean b) Set italic|Text
| iterator()|Iterator\<Text>
| lightPurple() Set color to light purple|Text
| obfuscated(Boolean b) Set obfuscated|Text
| obfuscated() Set obfuscated|Text
| red() Set color to red|Text
| setPropertiesFromJson(JsonObject j)|void
| spliterator()|Spliterator\<T>
| strikethrough(Boolean b) Set strikethrough|Text
| strikethrough() Set strikethrough|Text
| underlined() Set underlined|Text
| underlined(Boolean b) Set underlined|Text
| wait(long arg0, int arg1)|void
| wait(long l)|void
| white() Set color to white|Text
| yellow() Set color to yellow|Text

---

## Server

|Class
|--
|dev.latvian.kubejs.server.ServerJS

---

|Extends
|--
|MessageSender
|WithAttachedData

---

|Fields|Type
|--|--
|  data Temporary data, mods can attach objects to this|AttachedData
|  dedicated|boolean
|  displayName|Text
|  hardcore|boolean
|  minecraftServer|MinecraftServer
|  motd|String
|  name|String
|  overworld|ServerWorld
|  players|EntityArrayList
|  running|boolean
|  singlePlayer|boolean
|  worlds List of all currently loaded worlds|List\<ServerWorld>

---

|Methods|Return Type
|--|--
| getAdvancement(Object id)|Advancement
| getEntities(String filter)|EntityArrayList
| getPlayer(String name)|Player
| getPlayer(EntityPlayer minecraftPlayer)|Player
| getPlayer(UUID uuid)|Player
| getWorld(World minecraftWorld)|World
| getWorld(int dimension)|World
| runCommand(String s) Runs command as if the sender was running it, ignoring permissions|int
| schedule(long timer, Object data, ScheduledEventCallback callback)|ScheduledEvent
| scheduleInTicks(long ticks, Object data, ScheduledEventCallback callback)|ScheduledEvent
| sendDataToAll(String channel, Object data)|void
| setStatusMessage(Object o) Set status message|void
| stop()|void
| tell(Object o) Tell message in chat|void
| updateWorldList()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Field

|Class
|--
|dev.latvian.kubejs.util.FieldJS

---

|Extends
|--

---

|Methods|Return Type
|--|--
| get(Object o)|Object
| set(Object arg0, Object arg1)|boolean
| staticGet()|Object
| staticSet(Object o)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Potion

|Class
|--
|net.minecraft.potion.Potion

---

|Extends
|--
|IForgeRegistryEntry$Impl

---

|Fields|Type
|--|--
|  curativeItems|List\<ItemStack>
|  delegate|RegistryDelegate\<T>
|  field_188415_h|boolean
|  registryName|ResourceLocation
|  registryType|Class\<T>

---

|Methods|Return Type
|--|--
| func_111183_a(int arg0, AttributeModifier arg1)|double
| func_111184_a(Attribute arg0, String arg1, double arg2, int arg3)|Potion
| func_111185_a(EntityLivingBase arg0, AbstractAttributeMap arg1, int arg2)|void
| func_111186_k()|Map\<Attribute, AttributeModifier>
| func_111187_a(EntityLivingBase arg0, AbstractAttributeMap arg1, int arg2)|void
| func_180793_a(Entity arg0, Entity arg1, EntityLivingBase arg2, int arg3, double arg4)|void
| func_188408_i()|boolean
| func_188413_j()|Potion
| func_76390_b(String s)|Potion
| func_76392_e()|int
| func_76393_a()|String
| func_76394_a(EntityLivingBase arg0, int arg1)|void
| func_76397_a(int arg0, int arg1)|boolean
| func_76398_f()|boolean
| func_76400_d()|boolean
| func_76401_j()|int
| func_76403_b()|boolean
| getGuiSortColor(PotionEffect p)|int
| renderHUDEffect(int arg0, int arg1, PotionEffect arg2, Minecraft arg3, float arg4)|void
| renderHUDEffect(PotionEffect arg0, Gui arg1, int arg2, int arg3, float arg4, float arg5)|void
| renderInventoryEffect(int arg0, int arg1, PotionEffect arg2, Minecraft arg3)|void
| renderInventoryEffect(PotionEffect arg0, Gui arg1, int arg2, int arg3, float arg4)|void
| shouldRender(PotionEffect p)|boolean
| shouldRenderHUD(PotionEffect p)|boolean
| shouldRenderInvText(PotionEffect p)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SoundEvent

|Class
|--
|net.minecraft.util.SoundEvent

---

|Extends
|--
|IForgeRegistryEntry$Impl

---

|Fields|Type
|--|--
|  delegate|RegistryDelegate\<T>
|  registryName|ResourceLocation
|  registryType|Class\<T>

---

|Methods|Return Type
|--|--
| func_187503_a()|ResourceLocation
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## StatBase

|Class
|--
|net.minecraft.stats.StatBase

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_75972_f|boolean
|  field_75975_e|String

---

|Methods|Return Type
|--|--
| func_150951_e()|TextComponent
| func_150952_k()|ScoreCriteria
| func_150954_l()|Class\<? extends net.minecraft.util.IJsonSerializable>
| func_75966_h()|StatBase
| func_75968_a(int i)|String
| func_75971_g()|StatBase
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## World

|Class
|--
|net.minecraft.world.World

---

|Extends
|--
|BlockAccess
|CapabilityProvider
|FoamFixWorldRemovable

---

|Fields|Type
|--|--
|  captureBlockSnapshots|boolean
|  capturedBlockSnapshots|ArrayList\<BlockSnapshot>
|  currentMoonPhaseFactorBody|float
|  field_147482_g|List\<TileEntity>
|  field_175730_i|List\<TileEntity>
|  field_72982_D|VillageCollection
|  field_72984_F|Profiler
|  field_72995_K|boolean
|  field_72996_f|List\<Entity>
|  field_73003_n|float
|  field_73004_o|float
|  field_73007_j|List\<Entity>
|  field_73010_i|List\<EntityPlayer>
|  field_73011_w|WorldProvider
|  field_73012_v|Random
|  field_73017_q|float
|  field_73018_p|float
|  persistentChunks|ImmutableSetMultimap\<ChunkPos, ForgeChunkManager$Ticket>
|  perWorldStorage|MapStorage
|  restoringBlockSnapshots|boolean

---

|Methods|Return Type
|--|--
| calculateInitialWeatherBody()|void
| canBlockFreezeBody(BlockPos arg0, boolean arg1)|boolean
| canMineBlockBody(EntityPlayer arg0, BlockPos arg1)|boolean
| canSnowAtBody(BlockPos arg0, boolean arg1)|boolean
| countEntities(EnumCreatureType arg0, boolean arg1)|int
| foamfix_removeUnloadedEntities()|void
| func_130001_d()|float
| func_147442_i(float f)|void
| func_147447_a(Vec3d arg0, Vec3d arg1, boolean arg2, boolean arg3, boolean arg4)|RayTraceResult
| func_147448_a(Collection\<TileEntity> c)|void
| func_147457_a(TileEntity t)|void
| func_147458_c(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_147470_e(AxisAlignedBB a)|boolean
| func_152378_a(UUID u)|EntityPlayer
| func_175623_d(BlockPos b)|boolean
| func_175624_G()|WorldType
| func_175625_s(BlockPos b)|TileEntity
| func_175626_b(BlockPos arg0, int arg1)|int
| func_175627_a(BlockPos arg0, EnumFacing arg1)|int
| func_175636_b(double arg0, double arg1, double arg2, double arg3)|boolean
| func_175639_b(StructureBoundingBox arg0, boolean arg1)|boolean
| func_175640_z(BlockPos b)|boolean
| func_175641_c(BlockPos arg0, Block arg1, int arg2, int arg3)|void
| func_175642_b(EnumSkyBlock arg0, BlockPos arg1)|int
| func_175643_b()|World
| func_175644_a(Class\<? extends T> arg0, Predicate\<? super T> arg1)|List\<T>
| func_175645_m(BlockPos b)|BlockPos
| func_175646_b(BlockPos arg0, TileEntity arg1)|void
| func_175647_a(Class\<? extends T> arg0, AxisAlignedBB arg1, Predicate\<? super T> arg2)|List\<T>
| func_175648_a(BlockPos arg0, int arg1, boolean arg2)|boolean
| func_175649_E(BlockPos b)|DifficultyInstance
| func_175650_b(Collection\<Entity> c)|void
| func_175651_c(BlockPos arg0, EnumFacing arg1)|int
| func_175652_B(BlockPos b)|void
| func_175653_a(EnumSkyBlock arg0, BlockPos arg1, int arg2)|void
| func_175654_a(BlockPos arg0, Block arg1, int arg2, int arg3)|void
| func_175655_b(BlockPos arg0, boolean arg1)|boolean
| func_175656_a(BlockPos arg0, BlockState arg1)|boolean
| func_175657_ab()|int
| func_175658_ac()|int
| func_175659_aa()|EnumDifficulty
| func_175660_a(EntityPlayer arg0, BlockPos arg1)|boolean
| func_175661_b(Class\<? extends T> arg0, Predicate\<? super T> arg1)|List\<T>
| func_175662_w(BlockPos b)|boolean
| func_175664_x(BlockPos b)|boolean
| func_175665_u(BlockPos b)|boolean
| func_175666_e(BlockPos arg0, Block arg1)|void
| func_175667_e(BlockPos b)|boolean
| func_175668_a(BlockPos arg0, boolean arg1)|boolean
| func_175669_a(int arg0, BlockPos arg1, int arg2)|void
| func_175670_e(BlockPos arg0, boolean arg1)|boolean
| func_175671_l(BlockPos b)|int
| func_175672_r(BlockPos b)|BlockPos
| func_175674_a(Entity arg0, AxisAlignedBB arg1, Predicate\<? super net.minecraft.entity.Entity> arg2)|List\<Entity>
| func_175675_v(BlockPos b)|boolean
| func_175676_y(BlockPos b)|int
| func_175677_d(BlockPos arg0, boolean arg1)|boolean
| func_175678_i(BlockPos b)|boolean
| func_175679_n(BlockPos b)|void
| func_175681_c(Collection\<Entity> c)|void
| func_175682_a(EnumParticleTypes arg0, boolean arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, int[] arg8)|void
| func_175684_a(BlockPos arg0, Block arg1, int arg2)|void
| func_175685_c(BlockPos arg0, Block arg1, boolean arg2)|void
| func_175687_A(BlockPos b)|int
| func_175688_a(EnumParticleTypes arg0, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, int[] arg7)|void
| func_175690_a(BlockPos arg0, TileEntity arg1)|void
| func_175691_a(BlockPos arg0, Block arg1)|boolean
| func_175692_b(int i)|void
| func_175693_T()|MapStorage
| func_175694_M()|BlockPos
| func_175695_a(BlockPos arg0, Block arg1, EnumFacing arg2)|void
| func_175697_a(BlockPos arg0, int arg1)|boolean
| func_175698_g(BlockPos b)|boolean
| func_175699_k(BlockPos b)|int
| func_175700_a(TileEntity t)|boolean
| func_175701_a(BlockPos b)|boolean
| func_175702_c(int i)|void
| func_175704_b(BlockPos arg0, BlockPos arg1)|void
| func_175705_a(EnumSkyBlock arg0, BlockPos arg1)|int
| func_175706_a(BlockPos arg0, BlockPos arg1, boolean arg2)|boolean
| func_175707_a(BlockPos arg0, BlockPos arg1)|boolean
| func_175708_f(BlockPos arg0, boolean arg1)|boolean
| func_175709_b(BlockPos arg0, EnumFacing arg1)|boolean
| func_175710_j(BlockPos b)|boolean
| func_175711_a(StructureBoundingBox s)|boolean
| func_175712_a(StructureBoundingBox arg0, boolean arg1)|List\<NextTickListEntry>
| func_175713_t(BlockPos b)|void
| func_175714_ae()|VillageCollection
| func_175715_c(int arg0, BlockPos arg1, int arg2)|void
| func_175718_b(int arg0, BlockPos arg1, int arg2)|void
| func_175719_a(EntityPlayer arg0, BlockPos arg1, EnumFacing arg2)|boolean
| func_175721_c(BlockPos arg0, boolean arg1)|int
| func_175722_b(BlockPos arg0, Block arg1, boolean arg2)|void
| func_175723_af()|WorldBorder
| func_175724_o(BlockPos b)|float
| func_175725_q(BlockPos b)|BlockPos
| func_175726_f(BlockPos b)|Chunk
| func_175727_C(BlockPos b)|boolean
| func_180494_b(BlockPos b)|Biome
| func_180495_p(BlockPos b)|BlockState
| func_180497_b(BlockPos arg0, Block arg1, int arg2, int arg3)|void
| func_180498_a(EntityPlayer arg0, int arg1, BlockPos arg2, int arg3)|void
| func_180500_c(EnumSkyBlock arg0, BlockPos arg1)|boolean
| func_180501_a(BlockPos arg0, BlockState arg1, int arg2)|boolean
| func_180502_D(BlockPos b)|boolean
| func_181544_b(int i)|void
| func_181545_F()|int
| func_184133_a(EntityPlayer arg0, BlockPos arg1, SoundEvent arg2, SoundCategory arg3, float arg4, float arg5)|void
| func_184134_a(double arg0, double arg1, double arg2, SoundEvent arg3, SoundCategory arg4, float arg5, float arg6, boolean arg7)|void
| func_184135_a(Packet\<?> p)|void
| func_184136_b(Entity arg0, double arg1)|EntityPlayer
| func_184137_a(double arg0, double arg1, double arg2, double arg3, boolean arg4)|EntityPlayer
| func_184138_a(BlockPos arg0, BlockState arg1, BlockState arg2, int arg3)|void
| func_184139_a(BlockPos arg0, double arg1, double arg2)|EntityPlayer
| func_184141_c(BlockPos b)|BlockState
| func_184142_a(Entity arg0, double arg1, double arg2)|EntityPlayer
| func_184143_b(AxisAlignedBB a)|boolean
| func_184144_a(Entity arg0, AxisAlignedBB arg1)|List\<AxisAlignedBB>
| func_184145_b(BlockPos arg0, Block arg1)|boolean
| func_184146_ak()|LootTableManager
| func_184148_a(EntityPlayer arg0, double arg1, double arg2, double arg3, SoundEvent arg4, SoundCategory arg5, float arg6, float arg7)|void
| func_184149_a(BlockPos arg0, SoundEvent arg1)|void
| func_184150_a(double arg0, double arg1, double arg2, double arg3, double arg4, Function\<EntityPlayer, double> arg5, Predicate\<EntityPlayer> arg6)|EntityPlayer
| func_189507_a(BlockPos arg0, BlockState arg1, Random arg2)|void
| func_189509_E(BlockPos b)|boolean
| func_189649_b(int arg0, int arg1)|int
| func_190522_c(BlockPos arg0, Block arg1)|void
| func_190523_a(int arg0, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, int[] arg7)|void
| func_190524_a(BlockPos arg0, Block arg1, BlockPos arg2)|void
| func_190525_a(double arg0, double arg1, double arg2, double arg3, Predicate\<Entity> arg4)|EntityPlayer
| func_190526_b(int arg0, int arg1)|boolean
| func_190527_a(Block arg0, BlockPos arg1, boolean arg2, EnumFacing arg3, Entity arg4)|boolean
| func_190528_a(String arg0, BlockPos arg1, boolean arg2)|BlockPos
| func_190529_b(BlockPos arg0, Block arg1, BlockPos arg2)|void
| func_191503_g(Entity e)|boolean
| func_72800_K()|int
| func_72819_i(float f)|float
| func_72820_D()|long
| func_72823_a(String arg0, WorldSavedData arg1)|void
| func_72824_f(float f)|Vec3d
| func_72826_c(float f)|float
| func_72827_u()|String
| func_72829_c(AxisAlignedBB a)|boolean
| func_72833_a(Entity arg0, float arg1)|Vec3d
| func_72835_b()|void
| func_72838_d(Entity e)|boolean
| func_72839_b(Entity arg0, AxisAlignedBB arg1)|List\<Entity>
| func_72841_b(String s)|int
| func_72842_a(Vec3d arg0, AxisAlignedBB arg1)|float
| func_72843_D(int arg0, int arg1, int arg2)|Random
| func_72847_b(Entity e)|void
| func_72848_b(WorldEventListener w)|void
| func_72853_d()|int
| func_72854_c()|void
| func_72855_b(AxisAlignedBB a)|boolean
| func_72857_a(Class\<? extends T> arg0, AxisAlignedBB arg1, Entity arg2)|Entity
| func_72860_G()|SaveHandler
| func_72863_F()|ChunkProvider
| func_72866_a(Entity arg0, boolean arg1)|void
| func_72867_j(float f)|float
| func_72870_g(Entity e)|void
| func_72872_a(Class\<? extends T> arg0, AxisAlignedBB arg1)|List\<T>
| func_72875_a(AxisAlignedBB arg0, Material arg1)|boolean
| func_72876_a(Entity arg0, double arg1, double arg2, double arg3, float arg4, boolean arg5)|Explosion
| func_72877_b(long l)|void
| func_72880_h(float f)|float
| func_72882_A()|void
| func_72885_a(Entity arg0, double arg1, double arg2, double arg3, float arg4, boolean arg5, boolean arg6)|Explosion
| func_72890_a(Entity arg0, double arg1)|EntityPlayer
| func_72891_a(boolean arg0, boolean arg1)|void
| func_72894_k(float f)|void
| func_72896_J()|boolean
| func_72897_h(Entity e)|void
| func_72900_e(Entity e)|void
| func_72901_a(Vec3d arg0, Vec3d arg1, boolean arg2)|RayTraceResult
| func_72905_C()|long
| func_72906_B()|void
| func_72907_a(Class\<?> c)|int
| func_72910_y()|List\<Entity>
| func_72911_I()|boolean
| func_72912_H()|WorldInfo
| func_72914_a(CrashReport c)|CrashReportCategory
| func_72916_c(int arg0, int arg1)|boolean
| func_72917_a(AxisAlignedBB arg0, Entity arg1)|boolean
| func_72918_a(AxisAlignedBB arg0, Material arg1, Entity arg2)|boolean
| func_72919_O()|double
| func_72920_a(Chunk arg0, boolean arg1)|List\<NextTickListEntry>
| func_72923_a(Entity e)|void
| func_72924_a(String s)|EntityPlayer
| func_72929_e(float f)|float
| func_72933_a(Vec3d arg0, Vec3d arg1)|RayTraceResult
| func_72935_r()|boolean
| func_72939_s()|void
| func_72940_L()|int
| func_72942_c(Entity e)|boolean
| func_72943_a(Class\<? extends net.minecraft.world.storage.WorldSavedData> arg0, String arg1)|WorldSavedData
| func_72948_g(float f)|Vec3d
| func_72953_d(AxisAlignedBB a)|boolean
| func_72954_a(WorldEventListener w)|void
| func_72955_a(boolean b)|boolean
| func_72959_q()|BiomeProvider
| func_72960_a(Entity arg0, byte arg1)|void
| func_72963_a(WorldSettings w)|void
| func_72964_e(int arg0, int arg1)|Chunk
| func_72966_v()|void
| func_72967_a(float f)|int
| func_72971_b(float f)|float
| func_72973_f(Entity e)|void
| func_72974_f()|void
| func_72975_g(int arg0, int arg1, int arg2, int arg3)|void
| func_72981_t()|String
| func_73045_a(int i)|Entity
| func_73046_m()|MinecraftServer
| func_82734_g(int arg0, int arg1)|int
| func_82736_K()|GameRules
| func_82737_E()|long
| func_82738_a(long l)|void
| func_83015_S()|Calendar
| func_92088_a(double arg0, double arg1, double arg2, double arg3, double arg4, double arg5, NBTTagCompound arg6)|void
| func_96441_U()|Scoreboard
| getBiomeForCoordsBody(BlockPos b)|Biome
| getBlockLightOpacity(BlockPos b)|int
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getCloudColorBody(float f)|Vec3d
| getPersistentChunkIterable(Iterator\<Chunk> i)|Iterator\<Chunk>
| getSkyColorBody(Entity arg0, float arg1)|Vec3d
| getStarBrightnessBody(float f)|float
| getSunBrightnessBody(float f)|float
| getSunBrightnessFactor(float f)|float
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isSideSolid(BlockPos arg0, EnumFacing arg1, boolean arg2)|boolean
| isSideSolid(BlockPos arg0, EnumFacing arg1)|boolean
| markAndNotifyBlock(BlockPos arg0, Chunk arg1, BlockState arg2, BlockState arg3, int arg4)|void
| markTileEntitiesInChunkForRemoval(Chunk c)|void
| updateWeatherBody()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CountingMap

|Class
|--
|dev.latvian.kubejs.util.CountingMap

---

|Extends
|--

---

|Fields|Type
|--|--
|  entries|List\<CountingMap$Entry>
|  keys|Set\<Object>
|  size|int
|  totalCount|long
|  values|Collection\<long>

---

|Methods|Return Type
|--|--
| add(Object arg0, long arg1)|long
| clear()|void
| forEach(Consumer\<CountingMap$Entry> c)|void
| get(Object o)|long
| set(Object arg0, long arg1)|long
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Overlay

|Class
|--
|dev.latvian.kubejs.util.Overlay

---

|Extends
|--

---

|Fields|Type
|--|--
|  alwaysOnTop|boolean
|  color|int
|  icon|ItemStack
|  id|String
|  text|List\<Text>

---

|Methods|Return Type
|--|--
| add(Object o)|Overlay
| alwaysOnTop()|Overlay
| color(int i)|Overlay
| color(String s)|Overlay
| icon(Object o)|Overlay
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RegistryDelegate

|Interface
|--
|net.minecraftforge.registries.IRegistryDelegate

---

|Extends
|--

---

|Methods|Return Type
|--|--
| get()|Object
| name()|ResourceLocation
| type()|Class\<T>

---

## CreativeTabs

|Class
|--
|net.minecraft.creativetab.CreativeTabs

---

|Extends
|--

---

|Fields|Type
|--|--
|  backgroundImage|ResourceLocation
|  field_78034_o|String
|  labelColor|int
|  searchbarWidth|int
|  tabPage|int

---

|Methods|Return Type
|--|--
| func_111225_m()|EnumEnchantmentType[]
| func_111226_a(EnumEnchantmentType e)|boolean
| func_111229_a(EnumEnchantmentType[] e)|CreativeTabs
| func_151244_d()|ItemStack
| func_192394_m()|boolean
| func_78013_b()|String
| func_78014_h()|CreativeTabs
| func_78015_f()|String
| func_78016_d()|ItemStack
| func_78017_i()|boolean
| func_78018_a(NonNullList\<ItemStack> n)|void
| func_78019_g()|boolean
| func_78020_k()|int
| func_78021_a()|int
| func_78022_j()|CreativeTabs
| func_78023_l()|boolean
| func_78024_c()|String
| func_78025_a(String s)|CreativeTabs
| hasSearchBar()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockStateContainer

|Class
|--
|net.minecraft.block.state.BlockStateContainer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_177619_a()|ImmutableList\<BlockState>
| func_177621_b()|BlockState
| func_177622_c()|Block
| func_177623_d()|Collection\<net.minecraft.block.properties.IProperty\<?>>
| func_185920_a(String s)|Property\<?>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ResourceLocation

|Class
|--
|net.minecraft.util.ResourceLocation

---

|Extends
|--
|Comparable

---

|Fields|Type
|--|--
|  field_110625_b|String
|  field_110626_a|String

---

|Methods|Return Type
|--|--
| compareTo(ResourceLocation r)|int
| compareTo(Object o)|int
| func_110623_a()|String
| func_110624_b()|String
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockPos

|Class
|--
|net.minecraft.util.math.BlockPos

---

|Extends
|--
|Vec3i

---

|Methods|Return Type
|--|--
| compareTo(Vec3i v)|int
| compareTo(Object o)|int
| func_177951_i(Vec3i v)|double
| func_177952_p()|int
| func_177954_c(double arg0, double arg1, double arg2)|double
| func_177955_d(Vec3i v)|BlockPos
| func_177955_d(Vec3i v)|Vec3i
| func_177956_o()|int
| func_177957_d(double arg0, double arg1, double arg2)|double
| func_177958_n()|int
| func_177963_a(double arg0, double arg1, double arg2)|BlockPos
| func_177964_d(int i)|BlockPos
| func_177965_g(int i)|BlockPos
| func_177967_a(EnumFacing arg0, int arg1)|BlockPos
| func_177968_d()|BlockPos
| func_177970_e(int i)|BlockPos
| func_177971_a(Vec3i v)|BlockPos
| func_177972_a(EnumFacing e)|BlockPos
| func_177973_b(Vec3i v)|BlockPos
| func_177974_f()|BlockPos
| func_177976_e()|BlockPos
| func_177977_b()|BlockPos
| func_177978_c()|BlockPos
| func_177979_c(int i)|BlockPos
| func_177981_b(int i)|BlockPos
| func_177982_a(int arg0, int arg1, int arg2)|BlockPos
| func_177984_a()|BlockPos
| func_177985_f(int i)|BlockPos
| func_177986_g()|long
| func_185332_f(int arg0, int arg1, int arg2)|double
| func_185334_h()|BlockPos
| func_190942_a(Rotation r)|BlockPos
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ParticleManager

|Class
|--
|net.minecraft.client.particle.ParticleManager

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_78876_b|ArrayDeque[][]

---

|Methods|Return Type
|--|--
| addBlockHitEffects(BlockPos arg0, RayTraceResult arg1)|void
| func_178926_a(Entity arg0, EnumParticleTypes arg1)|void
| func_178927_a(int arg0, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, int[] arg7)|Particle
| func_178929_a(int arg0, ParticleFactory arg1)|void
| func_180532_a(BlockPos arg0, EnumFacing arg1)|void
| func_180533_a(BlockPos arg0, BlockState arg1)|void
| func_191271_a(Entity arg0, EnumParticleTypes arg1, int arg2)|void
| func_78868_a()|void
| func_78869_b()|String
| func_78870_a(World w)|void
| func_78872_b(Entity arg0, float arg1)|void
| func_78873_a(Particle p)|void
| func_78874_a(Entity arg0, float arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockState

|Interface
|--
|net.minecraft.block.state.IBlockState

---

|Extends
|--
|BlockBehaviors
|BlockProperties

---

|Methods|Return Type
|--|--
| doesSideBlockChestOpening(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean
| doesSideBlockRendering(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean
| func_177226_a(Property\<T> arg0, Comparable arg1)|BlockState
| func_177227_a()|Collection\<net.minecraft.block.properties.IProperty\<?>>
| func_177228_b()|ImmutableMap\<net.minecraft.block.properties.IProperty\<?>, java.lang.Comparable\<?>>
| func_177229_b(Property\<T> p)|Comparable
| func_177230_c()|Block
| func_177231_a(Property\<T> p)|BlockState
| func_185887_b(World arg0, BlockPos arg1)|float
| func_185888_a(World arg0, BlockPos arg1)|int
| func_185889_a(BlockAccess arg0, BlockPos arg1)|int
| func_185890_d(BlockAccess arg0, BlockPos arg1)|AxisAlignedBB
| func_185891_c()|int
| func_185892_j()|float
| func_185893_b(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|int
| func_185894_c(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean
| func_185895_e()|boolean
| func_185896_q()|boolean
| func_185897_m()|boolean
| func_185898_k()|boolean
| func_185899_b(BlockAccess arg0, BlockPos arg1)|BlockState
| func_185900_c(BlockAccess arg0, BlockPos arg1)|AxisAlignedBB
| func_185901_i()|EnumBlockRenderType
| func_185902_a(Mirror m)|BlockState
| func_185903_a(EntityPlayer arg0, World arg1, BlockPos arg2)|float
| func_185904_a()|Material
| func_185905_o()|EnumPushReaction
| func_185906_d()|int
| func_185907_a(Rotation r)|BlockState
| func_185908_a(World arg0, BlockPos arg1, AxisAlignedBB arg2, List\<AxisAlignedBB> arg3, Entity arg4, boolean arg5)|void
| func_185909_g(BlockAccess arg0, BlockPos arg1)|MapColor
| func_185910_a(World arg0, BlockPos arg1, Vec3d arg2, Vec3d arg3)|RayTraceResult
| func_185911_a(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|int
| func_185912_n()|boolean
| func_185913_b()|boolean
| func_185914_p()|boolean
| func_185915_l()|boolean
| func_185916_f()|boolean
| func_185917_h()|boolean
| func_185918_c(World arg0, BlockPos arg1)|AxisAlignedBB
| func_189546_a(World arg0, BlockPos arg1, Block arg2, BlockPos arg3)|void
| func_189547_a(World arg0, BlockPos arg1, int arg2, int arg3)|boolean
| func_189884_a(Entity e)|boolean
| func_191057_i()|boolean
| func_191058_s()|boolean
| func_191059_e(BlockAccess arg0, BlockPos arg1)|Vec3d
| func_193401_d(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|BlockFaceShape
| getLightOpacity(BlockAccess arg0, BlockPos arg1)|int
| getLightValue(BlockAccess arg0, BlockPos arg1)|int
| isSideSolid(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean

---

## RayTraceResult

|Class
|--
|net.minecraft.util.math.RayTraceResult

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_178784_b|EnumFacing
|  field_72307_f|Vec3d
|  field_72308_g|Entity
|  field_72313_a|RayTraceResult$Type
|  hitInfo|Object
|  subHit|int

---

|Methods|Return Type
|--|--
| func_178782_a()|BlockPos
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WorldServer

|Class
|--
|net.minecraft.world.WorldServer

---

|Extends
|--
|World
|ThreadListener

---

|Fields|Type
|--|--
|  captureBlockSnapshots|boolean
|  capturedBlockSnapshots|ArrayList\<BlockSnapshot>
|  chunkSaveLocation|File
|  currentMoonPhaseFactorBody|float
|  customTeleporters|List\<Teleporter>
|  field_147482_g|List\<TileEntity>
|  field_175730_i|List\<TileEntity>
|  field_72982_D|VillageCollection
|  field_72984_F|Profiler
|  field_72995_K|boolean
|  field_72996_f|List\<Entity>
|  field_73003_n|float
|  field_73004_o|float
|  field_73007_j|List\<Entity>
|  field_73010_i|List\<EntityPlayer>
|  field_73011_w|WorldProvider
|  field_73012_v|Random
|  field_73017_q|float
|  field_73018_p|float
|  field_73058_d|boolean
|  persistentChunks|ImmutableSetMultimap\<ChunkPos, ForgeChunkManager$Ticket>
|  perWorldStorage|MapStorage
|  restoringBlockSnapshots|boolean

---

|Methods|Return Type
|--|--
| calculateInitialWeatherBody()|void
| canBlockFreezeBody(BlockPos arg0, boolean arg1)|boolean
| canMineBlockBody(EntityPlayer arg0, BlockPos arg1)|boolean
| canSnowAtBody(BlockPos arg0, boolean arg1)|boolean
| countEntities(EnumCreatureType arg0, boolean arg1)|int
| foamfix_removeUnloadedEntities()|void
| func_104140_m()|void
| func_130001_d()|float
| func_147442_i(float f)|void
| func_147447_a(Vec3d arg0, Vec3d arg1, boolean arg2, boolean arg3, boolean arg4)|RayTraceResult
| func_147448_a(Collection\<TileEntity> c)|void
| func_147457_a(TileEntity t)|void
| func_147458_c(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_147470_e(AxisAlignedBB a)|boolean
| func_152344_a(Runnable r)|ListenableFuture\<Object>
| func_152345_ab()|boolean
| func_152378_a(UUID u)|EntityPlayer
| func_175623_d(BlockPos b)|boolean
| func_175624_G()|WorldType
| func_175625_s(BlockPos b)|TileEntity
| func_175626_b(BlockPos arg0, int arg1)|int
| func_175627_a(BlockPos arg0, EnumFacing arg1)|int
| func_175636_b(double arg0, double arg1, double arg2, double arg3)|boolean
| func_175639_b(StructureBoundingBox arg0, boolean arg1)|boolean
| func_175640_z(BlockPos b)|boolean
| func_175641_c(BlockPos arg0, Block arg1, int arg2, int arg3)|void
| func_175642_b(EnumSkyBlock arg0, BlockPos arg1)|int
| func_175643_b()|World
| func_175644_a(Class\<? extends T> arg0, Predicate\<? super T> arg1)|List\<T>
| func_175645_m(BlockPos b)|BlockPos
| func_175646_b(BlockPos arg0, TileEntity arg1)|void
| func_175647_a(Class\<? extends T> arg0, AxisAlignedBB arg1, Predicate\<? super T> arg2)|List\<T>
| func_175648_a(BlockPos arg0, int arg1, boolean arg2)|boolean
| func_175649_E(BlockPos b)|DifficultyInstance
| func_175650_b(Collection\<Entity> c)|void
| func_175651_c(BlockPos arg0, EnumFacing arg1)|int
| func_175652_B(BlockPos b)|void
| func_175653_a(EnumSkyBlock arg0, BlockPos arg1, int arg2)|void
| func_175654_a(BlockPos arg0, Block arg1, int arg2, int arg3)|void
| func_175655_b(BlockPos arg0, boolean arg1)|boolean
| func_175656_a(BlockPos arg0, BlockState arg1)|boolean
| func_175657_ab()|int
| func_175658_ac()|int
| func_175659_aa()|EnumDifficulty
| func_175660_a(EntityPlayer arg0, BlockPos arg1)|boolean
| func_175661_b(Class\<? extends T> arg0, Predicate\<? super T> arg1)|List\<T>
| func_175662_w(BlockPos b)|boolean
| func_175664_x(BlockPos b)|boolean
| func_175665_u(BlockPos b)|boolean
| func_175666_e(BlockPos arg0, Block arg1)|void
| func_175667_e(BlockPos b)|boolean
| func_175668_a(BlockPos arg0, boolean arg1)|boolean
| func_175669_a(int arg0, BlockPos arg1, int arg2)|void
| func_175670_e(BlockPos arg0, boolean arg1)|boolean
| func_175671_l(BlockPos b)|int
| func_175672_r(BlockPos b)|BlockPos
| func_175674_a(Entity arg0, AxisAlignedBB arg1, Predicate\<? super net.minecraft.entity.Entity> arg2)|List\<Entity>
| func_175675_v(BlockPos b)|boolean
| func_175676_y(BlockPos b)|int
| func_175677_d(BlockPos arg0, boolean arg1)|boolean
| func_175678_i(BlockPos b)|boolean
| func_175679_n(BlockPos b)|void
| func_175681_c(Collection\<Entity> c)|void
| func_175682_a(EnumParticleTypes arg0, boolean arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, int[] arg8)|void
| func_175684_a(BlockPos arg0, Block arg1, int arg2)|void
| func_175685_c(BlockPos arg0, Block arg1, boolean arg2)|void
| func_175687_A(BlockPos b)|int
| func_175688_a(EnumParticleTypes arg0, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, int[] arg7)|void
| func_175690_a(BlockPos arg0, TileEntity arg1)|void
| func_175691_a(BlockPos arg0, Block arg1)|boolean
| func_175692_b(int i)|void
| func_175693_T()|MapStorage
| func_175694_M()|BlockPos
| func_175695_a(BlockPos arg0, Block arg1, EnumFacing arg2)|void
| func_175697_a(BlockPos arg0, int arg1)|boolean
| func_175698_g(BlockPos b)|boolean
| func_175699_k(BlockPos b)|int
| func_175700_a(TileEntity t)|boolean
| func_175701_a(BlockPos b)|boolean
| func_175702_c(int i)|void
| func_175704_b(BlockPos arg0, BlockPos arg1)|void
| func_175705_a(EnumSkyBlock arg0, BlockPos arg1)|int
| func_175706_a(BlockPos arg0, BlockPos arg1, boolean arg2)|boolean
| func_175707_a(BlockPos arg0, BlockPos arg1)|boolean
| func_175708_f(BlockPos arg0, boolean arg1)|boolean
| func_175709_b(BlockPos arg0, EnumFacing arg1)|boolean
| func_175710_j(BlockPos b)|boolean
| func_175711_a(StructureBoundingBox s)|boolean
| func_175712_a(StructureBoundingBox arg0, boolean arg1)|List\<NextTickListEntry>
| func_175713_t(BlockPos b)|void
| func_175714_ae()|VillageCollection
| func_175715_c(int arg0, BlockPos arg1, int arg2)|void
| func_175718_b(int arg0, BlockPos arg1, int arg2)|void
| func_175719_a(EntityPlayer arg0, BlockPos arg1, EnumFacing arg2)|boolean
| func_175721_c(BlockPos arg0, boolean arg1)|int
| func_175722_b(BlockPos arg0, Block arg1, boolean arg2)|void
| func_175723_af()|WorldBorder
| func_175724_o(BlockPos b)|float
| func_175725_q(BlockPos b)|BlockPos
| func_175726_f(BlockPos b)|Chunk
| func_175727_C(BlockPos b)|boolean
| func_175732_a(EnumCreatureType arg0, Biome$SpawnListEntry arg1, BlockPos arg2)|boolean
| func_175733_a(UUID u)|Entity
| func_175734_a(EnumCreatureType arg0, BlockPos arg1)|Biome$SpawnListEntry
| func_175739_a(EnumParticleTypes arg0, double arg1, double arg2, double arg3, int arg4, double arg5, double arg6, double arg7, double arg8, int[] arg9)|void
| func_180494_b(BlockPos b)|Biome
| func_180495_p(BlockPos b)|BlockState
| func_180497_b(BlockPos arg0, Block arg1, int arg2, int arg3)|void
| func_180498_a(EntityPlayer arg0, int arg1, BlockPos arg2, int arg3)|void
| func_180500_c(EnumSkyBlock arg0, BlockPos arg1)|boolean
| func_180501_a(BlockPos arg0, BlockState arg1, int arg2)|boolean
| func_180502_D(BlockPos b)|boolean
| func_180504_m()|BlockPos
| func_180505_a(EnumParticleTypes arg0, boolean arg1, double arg2, double arg3, double arg4, int arg5, double arg6, double arg7, double arg8, double arg9, int[] arg10)|void
| func_181544_b(int i)|void
| func_181545_F()|int
| func_184133_a(EntityPlayer arg0, BlockPos arg1, SoundEvent arg2, SoundCategory arg3, float arg4, float arg5)|void
| func_184134_a(double arg0, double arg1, double arg2, SoundEvent arg3, SoundCategory arg4, float arg5, float arg6, boolean arg7)|void
| func_184135_a(Packet\<?> p)|void
| func_184136_b(Entity arg0, double arg1)|EntityPlayer
| func_184137_a(double arg0, double arg1, double arg2, double arg3, boolean arg4)|EntityPlayer
| func_184138_a(BlockPos arg0, BlockState arg1, BlockState arg2, int arg3)|void
| func_184139_a(BlockPos arg0, double arg1, double arg2)|EntityPlayer
| func_184141_c(BlockPos b)|BlockState
| func_184142_a(Entity arg0, double arg1, double arg2)|EntityPlayer
| func_184143_b(AxisAlignedBB a)|boolean
| func_184144_a(Entity arg0, AxisAlignedBB arg1)|List\<AxisAlignedBB>
| func_184145_b(BlockPos arg0, Block arg1)|boolean
| func_184146_ak()|LootTableManager
| func_184148_a(EntityPlayer arg0, double arg1, double arg2, double arg3, SoundEvent arg4, SoundCategory arg5, float arg6, float arg7)|void
| func_184149_a(BlockPos arg0, SoundEvent arg1)|void
| func_184150_a(double arg0, double arg1, double arg2, double arg3, double arg4, Function\<EntityPlayer, double> arg5, Predicate\<EntityPlayer> arg6)|EntityPlayer
| func_184161_a(EntityPlayerMP arg0, EnumParticleTypes arg1, boolean arg2, double arg3, double arg4, double arg5, int arg6, double arg7, double arg8, double arg9, double arg10, int[] arg11)|void
| func_184163_y()|TemplateManager
| func_184164_w()|PlayerChunkMap
| func_189507_a(BlockPos arg0, BlockState arg1, Random arg2)|void
| func_189509_E(BlockPos b)|boolean
| func_189649_b(int arg0, int arg1)|int
| func_190522_c(BlockPos arg0, Block arg1)|void
| func_190523_a(int arg0, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, int[] arg7)|void
| func_190524_a(BlockPos arg0, Block arg1, BlockPos arg2)|void
| func_190525_a(double arg0, double arg1, double arg2, double arg3, Predicate\<Entity> arg4)|EntityPlayer
| func_190526_b(int arg0, int arg1)|boolean
| func_190527_a(Block arg0, BlockPos arg1, boolean arg2, EnumFacing arg3, Entity arg4)|boolean
| func_190528_a(String arg0, BlockPos arg1, boolean arg2)|BlockPos
| func_190529_b(BlockPos arg0, Block arg1, BlockPos arg2)|void
| func_191503_g(Entity e)|boolean
| func_191952_z()|AdvancementManager
| func_193037_A()|FunctionManager
| func_72800_K()|int
| func_72819_i(float f)|float
| func_72820_D()|long
| func_72823_a(String arg0, WorldSavedData arg1)|void
| func_72824_f(float f)|Vec3d
| func_72826_c(float f)|float
| func_72827_u()|String
| func_72829_c(AxisAlignedBB a)|boolean
| func_72833_a(Entity arg0, float arg1)|Vec3d
| func_72835_b()|void
| func_72838_d(Entity e)|boolean
| func_72839_b(Entity arg0, AxisAlignedBB arg1)|List\<Entity>
| func_72841_b(String s)|int
| func_72842_a(Vec3d arg0, AxisAlignedBB arg1)|float
| func_72843_D(int arg0, int arg1, int arg2)|Random
| func_72847_b(Entity e)|void
| func_72848_b(WorldEventListener w)|void
| func_72853_d()|int
| func_72854_c()|void
| func_72855_b(AxisAlignedBB a)|boolean
| func_72857_a(Class\<? extends T> arg0, AxisAlignedBB arg1, Entity arg2)|Entity
| func_72860_G()|SaveHandler
| func_72863_F()|ChunkProvider
| func_72863_F()|ChunkProviderServer
| func_72866_a(Entity arg0, boolean arg1)|void
| func_72867_j(float f)|float
| func_72870_g(Entity e)|void
| func_72872_a(Class\<? extends T> arg0, AxisAlignedBB arg1)|List\<T>
| func_72875_a(AxisAlignedBB arg0, Material arg1)|boolean
| func_72876_a(Entity arg0, double arg1, double arg2, double arg3, float arg4, boolean arg5)|Explosion
| func_72877_b(long l)|void
| func_72880_h(float f)|float
| func_72882_A()|void
| func_72885_a(Entity arg0, double arg1, double arg2, double arg3, float arg4, boolean arg5, boolean arg6)|Explosion
| func_72890_a(Entity arg0, double arg1)|EntityPlayer
| func_72891_a(boolean arg0, boolean arg1)|void
| func_72894_k(float f)|void
| func_72896_J()|boolean
| func_72897_h(Entity e)|void
| func_72900_e(Entity e)|void
| func_72901_a(Vec3d arg0, Vec3d arg1, boolean arg2)|RayTraceResult
| func_72905_C()|long
| func_72906_B()|void
| func_72907_a(Class\<?> c)|int
| func_72910_y()|List\<Entity>
| func_72911_I()|boolean
| func_72912_H()|WorldInfo
| func_72914_a(CrashReport c)|CrashReportCategory
| func_72916_c(int arg0, int arg1)|boolean
| func_72917_a(AxisAlignedBB arg0, Entity arg1)|boolean
| func_72918_a(AxisAlignedBB arg0, Material arg1, Entity arg2)|boolean
| func_72919_O()|double
| func_72920_a(Chunk arg0, boolean arg1)|List\<NextTickListEntry>
| func_72923_a(Entity e)|void
| func_72924_a(String s)|EntityPlayer
| func_72929_e(float f)|float
| func_72933_a(Vec3d arg0, Vec3d arg1)|RayTraceResult
| func_72935_r()|boolean
| func_72939_s()|void
| func_72940_L()|int
| func_72942_c(Entity e)|boolean
| func_72943_a(Class\<? extends net.minecraft.world.storage.WorldSavedData> arg0, String arg1)|WorldSavedData
| func_72948_g(float f)|Vec3d
| func_72953_d(AxisAlignedBB a)|boolean
| func_72954_a(WorldEventListener w)|void
| func_72955_a(boolean b)|boolean
| func_72959_q()|BiomeProvider
| func_72960_a(Entity arg0, byte arg1)|void
| func_72963_a(WorldSettings w)|void
| func_72964_e(int arg0, int arg1)|Chunk
| func_72966_v()|void
| func_72967_a(float f)|int
| func_72971_b(float f)|float
| func_72973_f(Entity e)|void
| func_72974_f()|void
| func_72975_g(int arg0, int arg1, int arg2, int arg3)|void
| func_72981_t()|String
| func_73039_n()|EntityTracker
| func_73041_k()|void
| func_73044_a(boolean arg0, ProgressUpdate arg1)|void
| func_73045_a(int i)|Entity
| func_73046_m()|MinecraftServer
| func_73056_e()|boolean
| func_82734_g(int arg0, int arg1)|int
| func_82736_K()|GameRules
| func_82737_E()|long
| func_82738_a(long l)|void
| func_82742_i()|void
| func_83015_S()|Calendar
| func_85176_s()|Teleporter
| func_92088_a(double arg0, double arg1, double arg2, double arg3, double arg4, double arg5, NBTTagCompound arg6)|void
| func_96441_U()|Scoreboard
| getBiomeForCoordsBody(BlockPos b)|Biome
| getBlockLightOpacity(BlockPos b)|int
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getCloudColorBody(float f)|Vec3d
| getPersistentChunkIterable(Iterator\<Chunk> i)|Iterator\<Chunk>
| getSkyColorBody(Entity arg0, float arg1)|Vec3d
| getStarBrightnessBody(float f)|float
| getSunBrightnessBody(float f)|float
| getSunBrightnessFactor(float f)|float
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isSideSolid(BlockPos arg0, EnumFacing arg1, boolean arg2)|boolean
| isSideSolid(BlockPos arg0, EnumFacing arg1)|boolean
| markAndNotifyBlock(BlockPos arg0, Chunk arg1, BlockState arg2, BlockState arg3, int arg4)|void
| markTileEntitiesInChunkForRemoval(Chunk c)|void
| updateWeatherBody()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityLivingBase

|Class
|--
|net.minecraft.entity.EntityLivingBase

---

|Extends
|--
|Entity

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_110153_bc|float
|  field_110158_av|int
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_184617_aD|int
|  field_184618_aE|float
|  field_184619_aG|float
|  field_184622_au|EnumHand
|  field_184627_bm|ItemStack
|  field_184628_bn|int
|  field_190534_ay|int
|  field_191988_bg|float
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_70701_bs|float
|  field_70702_br|float
|  field_70703_bu|boolean
|  field_70704_bt|float
|  field_70718_bc|int
|  field_70720_be|int
|  field_70721_aZ|float
|  field_70725_aQ|int
|  field_70726_aT|float
|  field_70727_aS|float
|  field_70732_aI|float
|  field_70733_aJ|float
|  field_70737_aN|int
|  field_70738_aO|int
|  field_70739_aP|float
|  field_70747_aH|float
|  field_70755_b|EntityLivingBase
|  field_70758_at|float
|  field_70759_as|float
|  field_70760_ar|float
|  field_70761_aq|float
|  field_70769_ao|float
|  field_70770_ap|float
|  field_70771_an|int
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_82175_bq|boolean
|  field_98038_p|boolean
|  itemInUseMaxDuration|int
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| curePotionEffects(ItemStack i)|void
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_110124_au()|UUID
| func_110138_aP()|float
| func_110139_bj()|float
| func_110140_aT()|AbstractAttributeMap
| func_110142_aN()|CombatTracker
| func_110143_aJ()|float
| func_110144_aD()|EntityLivingBase
| func_110145_l(Entity e)|void
| func_110148_a(Attribute a)|AttributeInstance
| func_110149_m(float f)|void
| func_130011_c(Entity e)|void
| func_130014_f_()|World
| func_142013_aG()|int
| func_142015_aE()|int
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_152111_bt()|void
| func_152112_bu()|void
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_184582_a(EntityEquipmentSlot e)|ItemStack
| func_184583_d(DamageSource d)|boolean
| func_184585_cz()|boolean
| func_184586_b(EnumHand e)|ItemStack
| func_184587_cr()|boolean
| func_184589_d(Potion p)|void
| func_184591_cq()|EnumHandSide
| func_184592_cb()|ItemStack
| func_184595_k(double arg0, double arg1, double arg2)|boolean
| func_184596_c(Potion p)|PotionEffect
| func_184597_cx()|void
| func_184598_c(EnumHand e)|void
| func_184599_cB()|int
| func_184600_cs()|EnumHand
| func_184602_cy()|void
| func_184603_cC()|boolean
| func_184605_cv()|int
| func_184607_cu()|ItemStack
| func_184609_a(EnumHand e)|void
| func_184611_a(EnumHand arg0, ItemStack arg1)|void
| func_184612_cw()|int
| func_184613_cA()|boolean
| func_184614_ca()|ItemStack
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_189748_bU()|DamageSource
| func_190530_aW()|boolean
| func_190630_a(EntityEquipmentSlot e)|boolean
| func_190631_cK()|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_191986_a(float arg0, float arg1, float arg2)|void
| func_191987_a(BlockPos arg0, boolean arg1)|void
| func_193076_bZ()|Map\<Potion, PotionEffect>
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70604_c(EntityLivingBase e)|void
| func_70606_j(float f)|void
| func_70608_bn()|boolean
| func_70613_aW()|boolean
| func_70617_f_()|boolean
| func_70631_g_()|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70636_d()|void
| func_70637_d(boolean b)|void
| func_70643_av()|EntityLivingBase
| func_70644_a(Potion p)|boolean
| func_70645_a(DamageSource d)|void
| func_70648_aU()|boolean
| func_70651_bq()|Collection\<PotionEffect>
| func_70652_k(Entity e)|boolean
| func_70653_a(Entity arg0, float arg1, double arg2, double arg3)|void
| func_70654_ax()|int
| func_70658_aO()|int
| func_70659_e(float f)|void
| func_70660_b(Potion p)|PotionEffect
| func_70662_br()|boolean
| func_70668_bt()|EnumCreatureAttribute
| func_70669_a(ItemStack i)|void
| func_70674_bp()|void
| func_70676_i(float f)|Vec3d
| func_70678_g(float f)|float
| func_70681_au()|Random
| func_70685_l(Entity e)|boolean
| func_70687_e(PotionEffect p)|boolean
| func_70689_ay()|float
| func_70690_d(PotionEffect p)|void
| func_70691_i(float f)|void
| func_71001_a(Entity arg0, int arg1)|void
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_85034_r(int i)|void
| func_85035_bI()|int
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_94060_bK()|EntityLivingBase
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderFaceForward(EntityPlayer e)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Entity

|Class
|--
|net.minecraft.entity.Entity

---

|Extends
|--
|CommandSender
|CapabilitySerializable

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_190534_ay|int
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_98038_p|boolean
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_110124_au()|UUID
| func_130014_f_()|World
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_190530_aW()|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70676_i(float f)|Vec3d
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockAccess

|Interface
|--
|net.minecraft.world.IBlockAccess

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_175623_d(BlockPos b)|boolean
| func_175624_G()|WorldType
| func_175625_s(BlockPos b)|TileEntity
| func_175626_b(BlockPos arg0, int arg1)|int
| func_175627_a(BlockPos arg0, EnumFacing arg1)|int
| func_180494_b(BlockPos b)|Biome
| func_180495_p(BlockPos b)|BlockState
| isSideSolid(BlockPos arg0, EnumFacing arg1, boolean arg2)|boolean

---

## EntityLiving$SpawnPlacementType

|Class
|--
|net.minecraft.entity.EntityLiving$SpawnPlacementType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| canSpawnAt(World arg0, BlockPos arg1)|boolean
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityPlayer

|Class
|--
|net.minecraft.entity.player.EntityPlayer

---

|Extends
|--
|EntityLivingBase

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  defaultEyeHeight|float
|  displayNameString|String
|  entityData|NBTTagCompound
|  eyeHeight|float
|  field_110153_bc|float
|  field_110158_av|int
|  field_175152_f|int
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_184617_aD|int
|  field_184618_aE|float
|  field_184619_aG|float
|  field_184622_au|EnumHand
|  field_184627_bm|ItemStack
|  field_184628_bn|int
|  field_190534_ay|int
|  field_191988_bg|float
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_70701_bs|float
|  field_70702_br|float
|  field_70703_bu|boolean
|  field_70704_bt|float
|  field_70718_bc|int
|  field_70720_be|int
|  field_70721_aZ|float
|  field_70725_aQ|int
|  field_70726_aT|float
|  field_70727_aS|float
|  field_70732_aI|float
|  field_70733_aJ|float
|  field_70737_aN|int
|  field_70738_aO|int
|  field_70739_aP|float
|  field_70747_aH|float
|  field_70755_b|EntityLivingBase
|  field_70758_at|float
|  field_70759_as|float
|  field_70760_ar|float
|  field_70761_aq|float
|  field_70769_ao|float
|  field_70770_ap|float
|  field_70771_an|int
|  field_71067_cb|int
|  field_71068_ca|int
|  field_71069_bz|Container
|  field_71070_bA|Container
|  field_71071_by|InventoryPlayer
|  field_71075_bZ|PlayerCapabilities
|  field_71076_b|int
|  field_71079_bU|float
|  field_71081_bT|BlockPos
|  field_71082_cx|float
|  field_71083_bS|boolean
|  field_71085_bR|double
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71089_bV|float
|  field_71090_bL|int
|  field_71091_bM|double
|  field_71093_bK|int
|  field_71094_bP|double
|  field_71095_bQ|double
|  field_71096_bN|double
|  field_71097_bO|double
|  field_71104_cf|EntityFishHook
|  field_71106_cc|float
|  field_71107_bF|float
|  field_71109_bG|float
|  field_82151_R|float
|  field_82153_h|int
|  field_82175_bq|boolean
|  field_98038_p|boolean
|  itemInUseMaxDuration|int
|  persistentID|UUID
|  prefixes|Collection\<TextComponent>
|  spawnDimension|int
|  suffixes|Collection\<TextComponent>
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| addPrefix(TextComponent t)|void
| addSuffix(TextComponent t)|void
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| curePotionEffects(ItemStack i)|void
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_110124_au()|UUID
| func_110138_aP()|float
| func_110139_bj()|float
| func_110140_aT()|AbstractAttributeMap
| func_110142_aN()|CombatTracker
| func_110143_aJ()|float
| func_110144_aD()|EntityLivingBase
| func_110145_l(Entity e)|void
| func_110148_a(Attribute a)|AttributeInstance
| func_110149_m(float f)|void
| func_130011_c(Entity e)|void
| func_130014_f_()|World
| func_142013_aG()|int
| func_142015_aE()|int
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_146097_a(ItemStack arg0, boolean arg1, boolean arg2)|EntityItem
| func_146103_bH()|GameProfile
| func_146105_b(TextComponent arg0, boolean arg1)|void
| func_152111_bt()|void
| func_152112_bu()|void
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_175138_ci()|int
| func_175140_cp()|boolean
| func_175141_a(TileEntitySign t)|void
| func_175142_cm()|boolean
| func_175144_cb()|boolean
| func_175145_a(StatBase s)|void
| func_175146_a(LockCode l)|boolean
| func_175148_a(EnumPlayerModelParts e)|boolean
| func_175149_v()|boolean
| func_175150_k(boolean b)|void
| func_175151_a(BlockPos arg0, EnumFacing arg1, ItemStack arg2)|boolean
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180468_a(InteractionObject i)|void
| func_180469_a(BlockPos b)|EntityPlayer$SleepResult
| func_180470_cg()|BlockPos
| func_180472_a(Merchant m)|void
| func_180473_a(BlockPos arg0, boolean arg1)|void
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_184582_a(EntityEquipmentSlot e)|ItemStack
| func_184583_d(DamageSource d)|boolean
| func_184585_cz()|boolean
| func_184586_b(EnumHand e)|ItemStack
| func_184587_cr()|boolean
| func_184589_d(Potion p)|void
| func_184591_cq()|EnumHandSide
| func_184592_cb()|ItemStack
| func_184595_k(double arg0, double arg1, double arg2)|boolean
| func_184596_c(Potion p)|PotionEffect
| func_184597_cx()|void
| func_184598_c(EnumHand e)|void
| func_184599_cB()|int
| func_184600_cs()|EnumHand
| func_184602_cy()|void
| func_184603_cC()|boolean
| func_184605_cv()|int
| func_184607_cu()|ItemStack
| func_184609_a(EnumHand e)|void
| func_184611_a(EnumHand arg0, ItemStack arg1)|void
| func_184612_cw()|int
| func_184613_cA()|boolean
| func_184614_ca()|ItemStack
| func_184809_a(CommandBlockBaseLogic c)|void
| func_184810_cG()|void
| func_184811_cZ()|CooldownTracker
| func_184812_l_()|boolean
| func_184813_a(BlockState b)|float
| func_184814_a(ItemStack arg0, EnumHand arg1)|void
| func_184816_a(EntityItem e)|ItemStack
| func_184817_da()|float
| func_184818_cX()|float
| func_184819_a(EnumHandSide e)|void
| func_184821_cY()|void
| func_184823_b(BlockState b)|boolean
| func_184824_a(TileEntityCommandBlock t)|void
| func_184825_o(float f)|float
| func_184826_a(AbstractHorse arg0, Inventory arg1)|void
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_189748_bU()|DamageSource
| func_189807_a(TileEntityStructure t)|void
| func_189808_dh()|boolean
| func_190530_aW()|boolean
| func_190630_a(EntityEquipmentSlot e)|boolean
| func_190631_cK()|boolean
| func_190775_a(Entity arg0, EnumHand arg1)|EnumActionResult
| func_190777_m(boolean b)|void
| func_191521_c(ItemStack i)|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_191986_a(float arg0, float arg1, float arg2)|void
| func_191987_a(BlockPos arg0, boolean arg1)|void
| func_192021_a(List\<Recipe> l)|void
| func_192022_b(List\<Recipe> l)|void
| func_192023_dk()|NBTTagCompound
| func_192024_a(ItemStack arg0, int arg1)|void
| func_192025_dl()|NBTTagCompound
| func_192027_g(NBTTagCompound n)|boolean
| func_193076_bZ()|Map\<Potion, PotionEffect>
| func_193102_a(ResourceLocation[] r)|void
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70065_x()|void
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70604_c(EntityLivingBase e)|void
| func_70606_j(float f)|void
| func_70608_bn()|boolean
| func_70613_aW()|boolean
| func_70617_f_()|boolean
| func_70631_g_()|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70636_d()|void
| func_70637_d(boolean b)|void
| func_70643_av()|EntityLivingBase
| func_70644_a(Potion p)|boolean
| func_70645_a(DamageSource d)|void
| func_70648_aU()|boolean
| func_70651_bq()|Collection\<PotionEffect>
| func_70652_k(Entity e)|boolean
| func_70653_a(Entity arg0, float arg1, double arg2, double arg3)|void
| func_70654_ax()|int
| func_70658_aO()|int
| func_70659_e(float f)|void
| func_70660_b(Potion p)|PotionEffect
| func_70662_br()|boolean
| func_70664_aZ()|void
| func_70668_bt()|EnumCreatureAttribute
| func_70669_a(ItemStack i)|void
| func_70674_bp()|void
| func_70676_i(float f)|Vec3d
| func_70678_g(float f)|float
| func_70681_au()|Random
| func_70685_l(Entity e)|boolean
| func_70687_e(PotionEffect p)|boolean
| func_70689_ay()|float
| func_70690_d(PotionEffect p)|void
| func_70691_i(float f)|void
| func_70996_bM()|boolean
| func_70999_a(boolean arg0, boolean arg1, boolean arg2)|void
| func_71000_j(double arg0, double arg1, double arg2)|void
| func_71001_a(Entity arg0, int arg1)|void
| func_71004_bE()|void
| func_71005_bN()|InventoryEnderChest
| func_71007_a(Inventory i)|void
| func_71009_b(Entity e)|void
| func_71016_p()|void
| func_71019_a(ItemStack arg0, boolean arg1)|EntityItem
| func_71020_j(float f)|void
| func_71023_q(int i)|void
| func_71024_bL()|FoodStats
| func_71026_bH()|boolean
| func_71029_a(StatBase s)|void
| func_71033_a(GameType g)|void
| func_71037_bA()|int
| func_71040_bB(boolean b)|EntityItem
| func_71043_e(boolean b)|boolean
| func_71047_c(Entity e)|void
| func_71050_bK()|int
| func_71051_bG()|float
| func_71053_j()|void
| func_71059_n(Entity e)|void
| func_71060_bI()|int
| func_71064_a(StatBase arg0, int arg1)|void
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_82242_a(int i)|void
| func_82243_bO()|float
| func_82245_bX()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_85034_r(int i)|void
| func_85035_bI()|int
| func_85039_t(int i)|void
| func_85040_s(int i)|void
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_94060_bK()|EntityLivingBase
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96122_a(EntityPlayer e)|boolean
| func_96123_co()|Scoreboard
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| getBedLocation(int i)|BlockPos
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getDigSpeed(BlockState arg0, BlockPos arg1)|float
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| hasSpawnDimension()|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| isSpawnForced(int i)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| openGui(Object arg0, int arg1, World arg2, int arg3, int arg4, int arg5)|void
| refreshDisplayName()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| setSpawnChunk(BlockPos arg0, boolean arg1, int arg2)|void
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderFaceForward(EntityPlayer e)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockRenderLayer

|Class
|--
|net.minecraft.util.BlockRenderLayer

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Plantable

|Interface
|--
|net.minecraftforge.common.IPlantable

---

|Extends
|--

---

|Methods|Return Type
|--|--
| getPlant(BlockAccess arg0, BlockPos arg1)|BlockState
| getPlantType(BlockAccess arg0, BlockPos arg1)|EnumPlantType

---

## TileEntity

|Class
|--
|net.minecraft.tileentity.TileEntity

---

|Extends
|--
|CapabilitySerializable

---

|Fields|Type
|--|--
|  renderBoundingBox|AxisAlignedBB
|  tileData|NBTTagCompound

---

|Methods|Return Type
|--|--
| canRenderBreaking()|boolean
| deserializeNBT(NBTBase n)|void
| deserializeNBT(NBTTagCompound n)|void
| func_145748_c_()|TextComponent
| func_145828_a(CrashReportCategory c)|void
| func_145829_t()|void
| func_145830_o()|boolean
| func_145831_w()|World
| func_145832_p()|int
| func_145833_n()|double
| func_145834_a(World w)|void
| func_145835_a(double arg0, double arg1, double arg2)|double
| func_145836_u()|void
| func_145837_r()|boolean
| func_145838_q()|Block
| func_145839_a(NBTTagCompound n)|void
| func_145842_c(int arg0, int arg1)|boolean
| func_145843_s()|void
| func_174877_v()|BlockPos
| func_174878_a(BlockPos b)|void
| func_183000_F()|boolean
| func_189515_b(NBTTagCompound n)|NBTTagCompound
| func_189517_E_()|NBTTagCompound
| func_189518_D_()|SPacketUpdateTileEntity
| func_189667_a(Rotation r)|void
| func_189668_a(Mirror m)|void
| func_70296_d()|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| handleUpdateTag(NBTTagCompound n)|void
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| hasFastRenderer()|boolean
| onChunkUnload()|void
| onDataPacket(NetworkManager arg0, SPacketUpdateTileEntity arg1)|void
| onLoad()|void
| restrictNBTCopy()|boolean
| serializeNBT()|NBTBase
| serializeNBT()|NBTTagCompound
| shouldRefresh(World arg0, BlockPos arg1, BlockState arg2, BlockState arg3)|boolean
| shouldRenderInPass(int i)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumBlockRenderType

|Class
|--
|net.minecraft.util.EnumBlockRenderType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumPushReaction

|Class
|--
|net.minecraft.block.material.EnumPushReaction

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Explosion

|Class
|--
|net.minecraft.world.Explosion

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_77280_f|float
|  field_77281_g|List\<BlockPos>
|  field_77282_d|double
|  field_77283_e|Entity
|  field_77284_b|double
|  field_77285_c|double
|  field_77286_a|boolean
|  field_77287_j|World
|  field_77288_k|Map\<EntityPlayer, Vec3d>
|  field_77290_i|Random
|  field_82755_b|boolean
|  position|Vec3d

---

|Methods|Return Type
|--|--
| func_180342_d()|void
| func_180343_e()|List\<BlockPos>
| func_77277_b()|Map\<EntityPlayer, Vec3d>
| func_77278_a()|void
| func_77279_a(boolean b)|void
| func_94613_c()|EntityLivingBase
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NonNullList

|Class
|--
|net.minecraft.util.NonNullList

---

|Extends
|--
|AbstractList

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(int arg0, Object arg1)|void
| add(Object o)|boolean
| addAll(int arg0, Collection\<? extends E> arg1)|boolean
| addAll(Collection\<? extends E> c)|boolean
| clear()|void
| contains(Object o)|boolean
| containsAll(Collection\<?> c)|boolean
| forEach(Consumer\<? super T> c)|void
| get(int i)|Object
| indexOf(Object o)|int
| iterator()|Iterator\<E>
| lastIndexOf(Object o)|int
| listIterator(int i)|ListIterator\<E>
| listIterator()|ListIterator\<E>
| parallelStream()|Stream\<E>
| remove(int i)|Object
| remove(Object o)|boolean
| removeAll(Collection\<?> c)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| replaceAll(UnaryOperator\<E> u)|void
| retainAll(Collection\<?> c)|boolean
| set(int arg0, Object arg1)|Object
| size()|int
| sort(Comparator\<? super E> c)|void
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| subList(int arg0, int arg1)|List\<E>
| toArray(Object[] o)|Object[]
| toArray()|Object[]
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemStack

|Class
|--
|net.minecraft.item.ItemStack

---

|Extends
|--
|CapabilitySerializable

---

|Methods|Return Type
|--|--
| areCapsCompatible(ItemStack i)|boolean
| deserializeNBT(NBTBase n)|void
| deserializeNBT(NBTTagCompound n)|void
| doesSneakBypassUse(BlockAccess arg0, BlockPos arg1, EntityPlayer arg2)|boolean
| func_111282_a(EntityPlayer arg0, EntityLivingBase arg1, EnumHand arg2)|boolean
| func_111283_C(EntityEquipmentSlot e)|Multimap\<String, AttributeModifier>
| func_135074_t()|void
| func_150997_a(BlockState b)|float
| func_150998_b(BlockState b)|boolean
| func_151000_E()|TextComponent
| func_151001_c(String s)|ItemStack
| func_179543_a(String s)|NBTTagCompound
| func_179544_c(Block b)|boolean
| func_179546_a(EntityPlayer arg0, World arg1, BlockPos arg2, EnumHand arg3, EnumFacing arg4, float arg5, float arg6, float arg7)|EnumActionResult
| func_179547_d(Block b)|boolean
| func_179548_a(World arg0, BlockState arg1, BlockPos arg2, EntityPlayer arg3)|void
| func_185129_a(String arg0, AttributeModifier arg1, EntityEquipmentSlot arg2)|void
| func_185136_b(ItemStack i)|boolean
| func_190915_d(int i)|void
| func_190916_E()|int
| func_190917_f(int i)|void
| func_190918_g(int i)|void
| func_190919_e(String s)|void
| func_190920_e(int i)|void
| func_190921_D()|int
| func_190924_f(String s)|ItemStack
| func_190925_c(String s)|NBTTagCompound
| func_190926_b()|boolean
| func_77942_o()|boolean
| func_77945_a(World arg0, Entity arg1, int arg2, boolean arg3)|void
| func_77946_l()|ItemStack
| func_77948_v()|boolean
| func_77950_b(World arg0, EntityLivingBase arg1)|ItemStack
| func_77951_h()|boolean
| func_77952_i()|int
| func_77953_t()|EnumRarity
| func_77955_b(NBTTagCompound n)|NBTTagCompound
| func_77956_u()|boolean
| func_77957_a(World arg0, EntityPlayer arg1, EnumHand arg2)|ActionResult\<ItemStack>
| func_77958_k()|int
| func_77960_j()|int
| func_77961_a(EntityLivingBase arg0, EntityPlayer arg1)|void
| func_77962_s()|boolean
| func_77964_b(int i)|void
| func_77966_a(Enchantment arg0, int arg1)|void
| func_77969_a(ItemStack i)|boolean
| func_77972_a(int arg0, EntityLivingBase arg1)|void
| func_77973_b()|Item
| func_77974_b(World arg0, EntityLivingBase arg1, int arg2)|void
| func_77975_n()|EnumAction
| func_77976_d()|int
| func_77977_a()|String
| func_77978_p()|NBTTagCompound
| func_77979_a(int i)|ItemStack
| func_77980_a(World arg0, EntityPlayer arg1, int arg2)|void
| func_77981_g()|boolean
| func_77982_d(NBTTagCompound n)|void
| func_77983_a(String arg0, NBTBase arg1)|void
| func_77984_f()|boolean
| func_77985_e()|boolean
| func_77986_q()|NBTTagList
| func_77988_m()|int
| func_82833_r()|String
| func_82835_x()|boolean
| func_82836_z()|EntityItemFrame
| func_82837_s()|boolean
| func_82838_A()|int
| func_82839_y()|boolean
| func_82840_a(EntityPlayer arg0, TooltipFlag arg1)|List\<String>
| func_82841_c(int i)|void
| func_82842_a(EntityItemFrame e)|void
| func_96631_a(int arg0, Random arg1, EntityPlayerMP arg2)|boolean
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| onItemUseFirst(EntityPlayer arg0, World arg1, BlockPos arg2, EnumHand arg3, EnumFacing arg4, float arg5, float arg6, float arg7)|EnumActionResult
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Material

|Class
|--
|net.minecraft.block.material.Material

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_151565_r()|MapColor
| func_186274_m()|EnumPushReaction
| func_76217_h()|boolean
| func_76218_k()|boolean
| func_76220_a()|boolean
| func_76222_j()|boolean
| func_76224_d()|boolean
| func_76228_b()|boolean
| func_76229_l()|boolean
| func_76230_c()|boolean
| func_76231_i()|Material
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Vec3d

|Class
|--
|net.minecraft.util.math.Vec3d

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_72448_b|double
|  field_72449_c|double
|  field_72450_a|double

---

|Methods|Return Type
|--|--
| func_178785_b(float f)|Vec3d
| func_178786_a(double arg0, double arg1, double arg2)|Vec3d
| func_178787_e(Vec3d v)|Vec3d
| func_178788_d(Vec3d v)|Vec3d
| func_178789_a(float f)|Vec3d
| func_186678_a(double d)|Vec3d
| func_186679_c(double arg0, double arg1, double arg2)|double
| func_189985_c()|double
| func_72429_b(Vec3d arg0, double arg1)|Vec3d
| func_72430_b(Vec3d v)|double
| func_72431_c(Vec3d v)|Vec3d
| func_72432_b()|Vec3d
| func_72433_c()|double
| func_72434_d(Vec3d arg0, double arg1)|Vec3d
| func_72435_c(Vec3d arg0, double arg1)|Vec3d
| func_72436_e(Vec3d v)|double
| func_72438_d(Vec3d v)|double
| func_72441_c(double arg0, double arg1, double arg2)|Vec3d
| func_72444_a(Vec3d v)|Vec3d
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Block$EnumOffsetType

|Class
|--
|net.minecraft.block.Block$EnumOffsetType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AxisAlignedBB

|Class
|--
|net.minecraft.util.math.AxisAlignedBB

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_72334_f|double
|  field_72336_d|double
|  field_72337_e|double
|  field_72338_b|double
|  field_72339_c|double
|  field_72340_a|double

---

|Methods|Return Type
|--|--
| func_111270_a(AxisAlignedBB a)|AxisAlignedBB
| func_181656_b()|boolean
| func_186660_b(Vec3d v)|boolean
| func_186662_g(double d)|AxisAlignedBB
| func_186664_h(double d)|AxisAlignedBB
| func_186666_e(double d)|AxisAlignedBB
| func_186667_c(Vec3d v)|boolean
| func_186668_a(double arg0, double arg1, double arg2, double arg3, double arg4, double arg5)|boolean
| func_186669_d(Vec3d v)|boolean
| func_186670_a(BlockPos b)|AxisAlignedBB
| func_189972_c()|Vec3d
| func_189973_a(Vec3d arg0, Vec3d arg1)|boolean
| func_191194_a(Vec3d v)|AxisAlignedBB
| func_191195_a(double arg0, double arg1, double arg2)|AxisAlignedBB
| func_191500_a(AxisAlignedBB a)|AxisAlignedBB
| func_72314_b(double arg0, double arg1, double arg2)|AxisAlignedBB
| func_72316_a(AxisAlignedBB arg0, double arg1)|double
| func_72317_d(double arg0, double arg1, double arg2)|AxisAlignedBB
| func_72318_a(Vec3d v)|boolean
| func_72320_b()|double
| func_72321_a(double arg0, double arg1, double arg2)|AxisAlignedBB
| func_72322_c(AxisAlignedBB arg0, double arg1)|double
| func_72323_b(AxisAlignedBB arg0, double arg1)|double
| func_72326_a(AxisAlignedBB a)|boolean
| func_72327_a(Vec3d arg0, Vec3d arg1)|RayTraceResult
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MapColor

|Class
|--
|net.minecraft.block.material.MapColor

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_76290_q|int
|  field_76291_p|int

---

|Methods|Return Type
|--|--
| func_151643_b(int i)|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SoundType

|Class
|--
|net.minecraft.block.SoundType

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_185860_m|float
|  field_185861_n|float

---

|Methods|Return Type
|--|--
| func_185841_e()|SoundEvent
| func_185842_g()|SoundEvent
| func_185843_a()|float
| func_185844_d()|SoundEvent
| func_185845_c()|SoundEvent
| func_185846_f()|SoundEvent
| func_185847_b()|float
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Mirror

|Class
|--
|net.minecraft.util.Mirror

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_185800_a(EnumFacing e)|Rotation
| func_185802_a(int arg0, int arg1)|int
| func_185803_b(EnumFacing e)|EnumFacing
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Rotation

|Class
|--
|net.minecraft.util.Rotation

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_185830_a(Rotation r)|Rotation
| func_185831_a(EnumFacing e)|EnumFacing
| func_185833_a(int arg0, int arg1)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TooltipFlag

|Interface
|--
|net.minecraft.client.util.ITooltipFlag

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_194127_a()|boolean

---

## BlockFaceShape

|Class
|--
|net.minecraft.block.state.BlockFaceShape

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityLiving

|Class
|--
|net.minecraft.entity.EntityLiving

---

|Extends
|--
|EntityLivingBase

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_110153_bc|float
|  field_110158_av|int
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_184617_aD|int
|  field_184618_aE|float
|  field_184619_aG|float
|  field_184622_au|EnumHand
|  field_184627_bm|ItemStack
|  field_184628_bn|int
|  field_190534_ay|int
|  field_191988_bg|float
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_70696_bz|EntityLivingBase
|  field_70701_bs|float
|  field_70702_br|float
|  field_70703_bu|boolean
|  field_70704_bt|float
|  field_70714_bg|EntityAITasks
|  field_70715_bh|EntityAITasks
|  field_70718_bc|int
|  field_70720_be|int
|  field_70721_aZ|float
|  field_70725_aQ|int
|  field_70726_aT|float
|  field_70727_aS|float
|  field_70728_aV|int
|  field_70732_aI|float
|  field_70733_aJ|float
|  field_70737_aN|int
|  field_70738_aO|int
|  field_70739_aP|float
|  field_70747_aH|float
|  field_70755_b|EntityLivingBase
|  field_70757_a|int
|  field_70758_at|float
|  field_70759_as|float
|  field_70760_ar|float
|  field_70761_aq|float
|  field_70769_ao|float
|  field_70770_ap|float
|  field_70771_an|int
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_82175_bq|boolean
|  field_98038_p|boolean
|  itemInUseMaxDuration|int
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| curePotionEffects(ItemStack i)|void
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_104002_bU()|boolean
| func_110124_au()|UUID
| func_110138_aP()|float
| func_110139_bj()|float
| func_110140_aT()|AbstractAttributeMap
| func_110142_aN()|CombatTracker
| func_110143_aJ()|float
| func_110144_aD()|EntityLivingBase
| func_110145_l(Entity e)|void
| func_110148_a(Attribute a)|AttributeInstance
| func_110149_m(float f)|void
| func_110160_i(boolean arg0, boolean arg1)|void
| func_110162_b(Entity arg0, boolean arg1)|void
| func_110163_bv()|void
| func_110166_bE()|Entity
| func_110167_bD()|boolean
| func_130011_c(Entity e)|void
| func_130014_f_()|World
| func_142013_aG()|int
| func_142015_aE()|int
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_152111_bt()|void
| func_152112_bu()|void
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_175446_cd()|boolean
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180482_a(DifficultyInstance arg0, EntityLivingData arg1)|EntityLivingData
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_184582_a(EntityEquipmentSlot e)|ItemStack
| func_184583_d(DamageSource d)|boolean
| func_184585_cz()|boolean
| func_184586_b(EnumHand e)|ItemStack
| func_184587_cr()|boolean
| func_184589_d(Potion p)|void
| func_184591_cq()|EnumHandSide
| func_184592_cb()|ItemStack
| func_184595_k(double arg0, double arg1, double arg2)|boolean
| func_184596_c(Potion p)|PotionEffect
| func_184597_cx()|void
| func_184598_c(EnumHand e)|void
| func_184599_cB()|int
| func_184600_cs()|EnumHand
| func_184602_cy()|void
| func_184603_cC()|boolean
| func_184605_cv()|int
| func_184607_cu()|ItemStack
| func_184609_a(EnumHand e)|void
| func_184611_a(EnumHand arg0, ItemStack arg1)|void
| func_184612_cw()|int
| func_184613_cA()|boolean
| func_184614_ca()|ItemStack
| func_184638_cS()|boolean
| func_184641_n(boolean b)|void
| func_184642_a(EntityEquipmentSlot arg0, float arg1)|void
| func_184643_a(PathNodeType p)|float
| func_184644_a(PathNodeType arg0, float arg1)|void
| func_184646_p(float f)|void
| func_184649_cE()|int
| func_184652_a(EntityPlayer e)|boolean
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_189748_bU()|DamageSource
| func_190530_aW()|boolean
| func_190630_a(EntityEquipmentSlot e)|boolean
| func_190631_cK()|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_191986_a(float arg0, float arg1, float arg2)|void
| func_191987_a(BlockPos arg0, boolean arg1)|void
| func_191989_p(float f)|void
| func_193076_bZ()|Map\<Potion, PotionEffect>
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70058_J()|boolean
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70601_bi()|boolean
| func_70603_bj()|float
| func_70604_c(EntityLivingBase e)|void
| func_70605_aq()|EntityMoveHelper
| func_70606_j(float f)|void
| func_70608_bn()|boolean
| func_70613_aW()|boolean
| func_70615_aA()|void
| func_70617_f_()|boolean
| func_70624_b(EntityLivingBase e)|void
| func_70625_a(Entity arg0, float arg1, float arg2)|void
| func_70627_aG()|int
| func_70631_g_()|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70635_at()|EntitySenses
| func_70636_d()|void
| func_70637_d(boolean b)|void
| func_70638_az()|EntityLivingBase
| func_70641_bl()|int
| func_70642_aH()|void
| func_70643_av()|EntityLivingBase
| func_70644_a(Potion p)|boolean
| func_70645_a(DamageSource d)|void
| func_70646_bf()|int
| func_70648_aU()|boolean
| func_70651_bq()|Collection\<PotionEffect>
| func_70652_k(Entity e)|boolean
| func_70653_a(Entity arg0, float arg1, double arg2, double arg3)|void
| func_70654_ax()|int
| func_70656_aK()|void
| func_70657_f(float f)|void
| func_70658_aO()|int
| func_70659_e(float f)|void
| func_70660_b(Potion p)|PotionEffect
| func_70661_as()|PathNavigate
| func_70662_br()|boolean
| func_70668_bt()|EnumCreatureAttribute
| func_70669_a(ItemStack i)|void
| func_70671_ap()|EntityLookHelper
| func_70674_bp()|void
| func_70676_i(float f)|Vec3d
| func_70678_g(float f)|float
| func_70681_au()|Random
| func_70683_ar()|EntityJumpHelper
| func_70685_l(Entity e)|boolean
| func_70686_a(Class\<? extends net.minecraft.entity.EntityLivingBase> c)|boolean
| func_70687_e(PotionEffect p)|boolean
| func_70689_ay()|float
| func_70690_d(PotionEffect p)|void
| func_70691_i(float f)|void
| func_71001_a(Entity arg0, int arg1)|void
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_82171_bF()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_85034_r(int i)|void
| func_85035_bI()|int
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_94060_bK()|EntityLivingBase
| func_94061_f(boolean b)|void
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| func_98052_bS()|boolean
| func_98053_h(boolean b)|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderFaceForward(EntityPlayer e)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PathNodeType

|Class
|--
|net.minecraft.pathfinding.PathNodeType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_186289_a()|float
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumDyeColor

|Class
|--
|net.minecraft.item.EnumDyeColor

---

|Extends
|--
|Enum
|StringSerializable

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>
|  field_176793_x|TextFormatting

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_176610_l()|String
| func_176762_d()|String
| func_176765_a()|int
| func_176767_b()|int
| func_192396_c()|String
| func_193349_f()|float[]
| func_193350_e()|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TileEntityItemStackRenderer

|Class
|--
|net.minecraft.client.renderer.tileentity.TileEntityItemStackRenderer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_179022_a(ItemStack i)|void
| func_192838_a(ItemStack arg0, float arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Enchantment

|Class
|--
|net.minecraft.enchantment.Enchantment

---

|Extends
|--
|IForgeRegistryEntry$Impl

---

|Fields|Type
|--|--
|  allowedOnBooks|boolean
|  delegate|RegistryDelegate\<T>
|  field_77351_y|EnumEnchantmentType
|  registryName|ResourceLocation
|  registryType|Class\<T>

---

|Methods|Return Type
|--|--
| canApplyAtEnchantingTable(ItemStack i)|boolean
| func_151367_b(EntityLivingBase arg0, Entity arg1, int arg2)|void
| func_151368_a(EntityLivingBase arg0, Entity arg1, int arg2)|void
| func_152376_a(int arg0, EnumCreatureAttribute arg1)|float
| func_185260_a(EntityLivingBase e)|List\<ItemStack>
| func_185261_e()|boolean
| func_190936_d()|boolean
| func_191560_c(Enchantment e)|boolean
| func_77316_c(int i)|String
| func_77317_b(int i)|int
| func_77318_a(int arg0, DamageSource arg1)|int
| func_77319_d()|int
| func_77320_a()|String
| func_77321_a(int i)|int
| func_77322_b(String s)|Enchantment
| func_77324_c()|Enchantment$Rarity
| func_77325_b()|int
| func_92089_a(ItemStack i)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AttributeModifier

|Class
|--
|net.minecraft.entity.ai.attributes.AttributeModifier

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_111164_d()|double
| func_111165_e()|boolean
| func_111166_b()|String
| func_111167_a()|UUID
| func_111168_a(boolean b)|AttributeModifier
| func_111169_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NBTTagCompound

|Class
|--
|net.minecraft.nbt.NBTTagCompound

---

|Extends
|--
|NBTBase

---

|Fields|Type
|--|--
|  field_74784_a|Map\<String, NBTBase>

---

|Methods|Return Type
|--|--
| func_150295_c(String arg0, int arg1)|NBTTagList
| func_150296_c()|Set\<String>
| func_150297_b(String arg0, int arg1)|boolean
| func_150299_b(String s)|byte
| func_179237_a(NBTTagCompound n)|void
| func_186854_a(String arg0, UUID arg1)|void
| func_186855_b(String s)|boolean
| func_186856_d()|int
| func_186857_a(String s)|UUID
| func_74732_a()|byte
| func_74737_b()|NBTBase
| func_74737_b()|NBTTagCompound
| func_74757_a(String arg0, boolean arg1)|void
| func_74759_k(String s)|int[]
| func_74760_g(String s)|float
| func_74762_e(String s)|int
| func_74763_f(String s)|long
| func_74764_b(String s)|boolean
| func_74765_d(String s)|short
| func_74767_n(String s)|boolean
| func_74768_a(String arg0, int arg1)|void
| func_74769_h(String s)|double
| func_74770_j(String s)|byte[]
| func_74771_c(String s)|byte
| func_74772_a(String arg0, long arg1)|void
| func_74773_a(String arg0, byte[] arg1)|void
| func_74774_a(String arg0, byte arg1)|void
| func_74775_l(String s)|NBTTagCompound
| func_74776_a(String arg0, float arg1)|void
| func_74777_a(String arg0, short arg1)|void
| func_74778_a(String arg0, String arg1)|void
| func_74779_i(String s)|String
| func_74780_a(String arg0, double arg1)|void
| func_74781_a(String s)|NBTBase
| func_74782_a(String arg0, NBTBase arg1)|void
| func_74783_a(String arg0, int[] arg1)|void
| func_82580_o(String s)|void
| func_82582_d()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumActionResult

|Class
|--
|net.minecraft.util.EnumActionResult

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemPropertyGetter

|Interface
|--
|net.minecraft.item.IItemPropertyGetter

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_185085_a(ItemStack arg0, World arg1, EntityLivingBase arg2)|float

---

## ActionResult

|Class
|--
|net.minecraft.util.ActionResult

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_188397_a()|EnumActionResult
| func_188398_b()|Object
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumAction

|Class
|--
|net.minecraft.item.EnumAction

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TimeValue

|Interface
|--
|net.minecraftforge.common.animation.ITimeValue

---

|Extends
|--

---

|Methods|Return Type
|--|--
| apply(float f)|float

---

## ModelBiped

|Class
|--
|net.minecraft.client.model.ModelBiped

---

|Extends
|--
|ModelBase

---

|Fields|Type
|--|--
|  field_178720_f|ModelRenderer
|  field_178721_j|ModelRenderer
|  field_178722_k|ModelRenderer
|  field_178723_h|ModelRenderer
|  field_178724_i|ModelRenderer
|  field_187075_l|ModelBiped$ArmPose
|  field_187076_m|ModelBiped$ArmPose
|  field_78089_u|int
|  field_78090_t|int
|  field_78091_s|boolean
|  field_78092_r|List\<ModelRenderer>
|  field_78093_q|boolean
|  field_78095_p|float
|  field_78115_e|ModelRenderer
|  field_78116_c|ModelRenderer
|  field_78117_n|boolean

---

|Methods|Return Type
|--|--
| func_178686_a(ModelBase m)|void
| func_178719_a(boolean b)|void
| func_187073_a(float arg0, EnumHandSide arg1)|void
| func_78084_a(String s)|TextureOffset
| func_78086_a(EntityLivingBase arg0, float arg1, float arg2, float arg3)|void
| func_78087_a(float arg0, float arg1, float arg2, float arg3, float arg4, float arg5, Entity arg6)|void
| func_78088_a(Entity arg0, float arg1, float arg2, float arg3, float arg4, float arg5, float arg6)|void
| func_85181_a(Random r)|ModelRenderer
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## FontRenderer

|Class
|--
|net.minecraft.client.gui.FontRenderer

---

|Extends
|--
|ResourceManagerReloadListener

---

|Fields|Type
|--|--
|  enabled|boolean
|  field_111273_g|ResourceLocation
|  field_78285_g|int[]
|  field_78286_d|int[]
|  field_78287_e|byte[]
|  field_78288_b|int
|  field_78289_c|Random
|  field_78293_l|boolean
|  field_78299_w|boolean
|  field_78300_v|boolean
|  field_78304_r|int
|  fontRendererHook|FontRendererHook
|  gameSettings|GameSettings
|  locationFontTextureBase|ResourceLocation
|  offsetBold|float

---

|Methods|Return Type
|--|--
| func_110549_a(ResourceManager r)|void
| func_111272_d()|void
| func_175063_a(String arg0, float arg1, float arg2, int arg3)|int
| func_175064_b(char c)|int
| func_175065_a(String arg0, float arg1, float arg2, int arg3, boolean arg4)|int
| func_180455_b(String arg0, float arg1, float arg2, int arg3, boolean arg4)|int
| func_78255_a(String arg0, boolean arg1)|void
| func_78256_a(String s)|int
| func_78259_e(String arg0, int arg1)|int
| func_78260_a()|boolean
| func_78262_a(String arg0, int arg1, boolean arg2)|String
| func_78263_a(char c)|int
| func_78264_a(boolean b)|void
| func_78265_b()|void
| func_78267_b(String arg0, int arg1)|int
| func_78269_a(String arg0, int arg1)|String
| func_78271_c(String arg0, int arg1)|List\<String>
| func_78275_b(boolean b)|void
| func_78276_b(String arg0, int arg1, int arg2, int arg3)|int
| func_78279_b(String arg0, int arg1, int arg2, int arg3, int arg4)|void
| func_82883_a()|boolean
| func_98306_d()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Rarity

|Interface
|--
|net.minecraftforge.common.IRarity

---

|Extends
|--

---

|Fields|Type
|--|--
|  color|TextFormatting
|  name|String

---

|Methods|Return Type
|--|--

---

## HorseArmorType

|Class
|--
|net.minecraft.entity.passive.HorseArmorType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_188573_b()|String
| func_188574_d()|String
| func_188578_c()|int
| func_188579_a()|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CapabilityProvider

|Interface
|--
|net.minecraftforge.common.capabilities.ICapabilityProvider

---

|Extends
|--

---

|Methods|Return Type
|--|--
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean

---

## EntityItem

|Class
|--
|net.minecraft.entity.item.EntityItem

---

|Extends
|--
|Entity

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_145804_b|int
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_190534_ay|int
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_70290_d|float
|  field_70291_e|int
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_98038_p|boolean
|  lifespan|int
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_110124_au()|UUID
| func_130014_f_()|World
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145797_a(String s)|void
| func_145798_i()|String
| func_145799_b(String s)|void
| func_145800_j()|String
| func_145818_k_()|boolean
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_174867_a(int i)|void
| func_174868_q()|void
| func_174869_p()|void
| func_174870_v()|void
| func_174871_r()|void
| func_174872_o()|int
| func_174873_u()|void
| func_174874_s()|boolean
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_190530_aW()|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70288_d()|void
| func_70289_a(EntityItem e)|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70676_i(float f)|Vec3d
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_90999_ad()|boolean
| func_92058_a(ItemStack i)|void
| func_92059_d()|ItemStack
| func_94059_bO()|boolean
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ScaledResolution

|Class
|--
|net.minecraft.client.gui.ScaledResolution

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_78324_d()|double
| func_78325_e()|int
| func_78326_a()|int
| func_78327_c()|double
| func_78328_b()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TextFormatting

|Class
|--
|net.minecraft.util.text.TextFormatting

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>
|  field_96329_z|char

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_175746_b()|int
| func_96297_d()|String
| func_96301_b()|boolean
| func_96302_c()|boolean
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityEquipmentSlot$Type

|Class
|--
|net.minecraft.inventory.EntityEquipmentSlot$Type

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PlayerEvent

|Class
|--
|dev.latvian.kubejs.player.PlayerEventJS

---

|Extends
|--
|LivingEntityEvent

---

|Fields|Type
|--|--
|  entity|Entity
|  player|Player
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| addGameStage(String s)|void
| hasGameStage(String s)|boolean
| removeGameStage(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Block

|Class
|--
|dev.latvian.kubejs.world.BlockContainerJS

---

|Extends
|--

---

|Fields|Type
|--|--
|  blockState|BlockState
|  canSeeSky|boolean
|  canSnow|boolean
|  canSnowCheckingLight|boolean
|  dimension|int
|  down|Block
|  east|Block
|  entity|TileEntity
|  entityData|NBTCompound
|  entityID|ID
|  id|ID
|  item|ItemStack
|  light|int
|  material|Material
|  minecraftWorld|World
|  north|Block
|  pos|BlockPos
|  properties|Map\<String, String>
|  south|Block
|  up|Block
|  west|Block
|  world|World
|  x|int
|  y|int
|  z|int

---

|Methods|Return Type
|--|--
| clearCache()|void
| createEntity(Object o)|Entity
| createExplosion()|Explosion
| getInventory(EnumFacing e)|Inventory
| offset(int arg0, int arg1, int arg2)|Block
| offset(EnumFacing arg0, int arg1)|Block
| offset(EnumFacing e)|Block
| set(Object o)|void
| set(Object arg0, Map\<?, ?> arg1, int arg2)|void
| set(Object arg0, Map\<?, ?> arg1)|void
| spawnFireworks(Fireworks f)|void
| spawnLightning(boolean b)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Entity

|Class
|--
|dev.latvian.kubejs.entity.EntityJS

---

|Extends
|--
|MessageSender

---

|Fields|Type
|--|--
|  alive|boolean
|  ambientCreature|boolean
|  animal|boolean
|  block Block position of the entity|Block
|  boss|boolean
|  customName Custom display name|String
|  customNameAlwaysVisible Custom display name will always be visible above head|boolean
|  displayName|Text
|  eyeHeight|float
|  facing|EnumFacing
|  fallDistance|float
|  frame|boolean
|  fullNBT Entity NBT|NBTCompound
|  glowing|boolean
|  hasCustomName Checks if custom display name is set|boolean
|  horizontalFacing|EnumFacing
|  id|UUID
|  invisible|boolean
|  item|ItemStack
|  living|boolean
|  minecraftEntity|Entity
|  monster|boolean
|  motionX|double
|  motionY|double
|  motionZ|double
|  name|String
|  nbt Custom NBT you can use for saving custom data|NBTCompound
|  noClip|boolean
|  noGravity|boolean
|  onGround|boolean
|  passengers|EntityArrayList
|  pitch|float
|  player|boolean
|  profile|GameProfile
|  recursivePassengers|EntityArrayList
|  ridingEntity|Entity
|  server|Server
|  silent|boolean
|  sneaking|boolean
|  sprinting|boolean
|  stepHeight|float
|  tags|Set\<String>
|  teamID Scoreboard team ID|String
|  ticksExisted|int
|  type|ID
|  waterCreature|boolean
|  world|World
|  x|double
|  y|double
|  yaw|float
|  z|double

---

|Methods|Return Type
|--|--
| addMotion(double x, double y, double z)|void
| attack(float hp)|void
| attack(String source, float hp)|void
| dismountRidingEntity()|void
| extinguish()|void
| getNBTData(String key) Get specific value from custom NBT|NBTBase
| isOnSameTeam(Entity entity) Checks if this entity is on the same scoreboard team as another entity|boolean
| isOnScoreboardTeam(String teamID) Checks if this entity is on scoreboard team|boolean
| isPassenger(Entity entity)|boolean
| kill()|void
| playSound(Object id, float volume, float pitch) Play sound at entity. Must be played from server side|void
| playSound(Object id) Play sound at entity. Must be played from server side|void
| removePassengers()|void
| runCommand(String command) Runs command as if the sender was running it, ignoring permissions|int
| setMotion(double x, double y, double z)|void
| setNBTData(String key, Object nbt) Set specific value in custom NBT|void
| setOnFire(int seconds) Sets entity on fire for x seconds|void
| setPosition(double x, double y, double z)|void
| setPosition(Block block)|void
| setPositionAndRotation(double x, double y, double z, float yaw, float pitch)|void
| setRotation(float yaw, float pitch)|void
| setStatusMessage(Text text) Set status message|void
| spawn() Spawn entity in world|void
| startRiding(Entity entity, boolean force)|boolean
| tell(Text message) Tell message in chat|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockBuilder

|Class
|--
|dev.latvian.kubejs.block.BlockBuilder

---

|Extends
|--

---

|Fields|Type
|--|--
|  id|ID

---

|Methods|Return Type
|--|--
| add()|void
| fullBlock(boolean fullBlock)|BlockBuilder
| hardness(float hardness)|BlockBuilder
| harvestTool(String tool, int level)|BlockBuilder
| layer(String layer)|BlockBuilder
| lightLevel(float light)|BlockBuilder
| material(Material material)|BlockBuilder
| opaque(boolean opaque)|BlockBuilder
| resistance(float resistance)|BlockBuilder
| translationKey(String translationKey)|BlockBuilder
| unbreakable()|BlockBuilder
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ServerEvent

|Class
|--
|dev.latvian.kubejs.server.ServerEventJS

---

|Extends
|--
|Event

---

|Fields|Type
|--|--
|  server|Server

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CommandBuilder

|Class
|--
|dev.latvian.kubejs.command.CommandBuilder

---

|Extends
|--

---

|Fields|Type
|--|--
|  aliases|List\<String>
|  callback|Consumer\<CommandBase>
|  execute|CommandBuilder$ExecuteFunction
|  name|String
|  requiredPermissionLevel|int
|  username|CommandBuilder$UsernameFunction

---

|Methods|Return Type
|--|--
| add()|void
| alias(String s)|CommandBuilder
| execute(CommandBuilder$ExecuteFunction c)|CommandBuilder
| op()|CommandBuilder
| username(int i)|CommandBuilder
| username(CommandBuilder$UsernameFunction c)|CommandBuilder
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CommandSender

|Class
|--
|dev.latvian.kubejs.command.CommandSender

---

|Extends
|--
|MessageSender

---

|Fields|Type
|--|--
|  block|Block
|  displayName|Text
|  name|String
|  player|Player
|  sender|CommandSender
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| runCommand(String s) Runs command as if the sender was running it, ignoring permissions|int
| setStatusMessage(Object o) Set status message|void
| tell(Object o) Tell message in chat|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## LivingEntityEvent

|Class
|--
|dev.latvian.kubejs.entity.LivingEntityEventJS

---

|Extends
|--
|EntityEvent

---

|Fields|Type
|--|--
|  entity|Entity
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## DamageSource

|Class
|--
|dev.latvian.kubejs.entity.DamageSourceJS

---

|Extends
|--

---

|Fields|Type
|--|--
|  actual|Entity
|  immediate|Entity
|  source|DamageSource
|  type|String
|  world|World

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemEntity

|Class
|--
|dev.latvian.kubejs.entity.ItemEntityJS

---

|Extends
|--
|Entity

---

|Fields|Type
|--|--
|  alive|boolean
|  ambientCreature|boolean
|  animal|boolean
|  block Block position of the entity|Block
|  boss|boolean
|  customName Custom display name|String
|  customNameAlwaysVisible Custom display name will always be visible above head|boolean
|  displayName|Text
|  eyeHeight|float
|  facing|EnumFacing
|  fallDistance|float
|  frame|boolean
|  fullNBT Entity NBT|NBTCompound
|  glowing|boolean
|  hasCustomName Checks if custom display name is set|boolean
|  horizontalFacing|EnumFacing
|  id|UUID
|  invisible|boolean
|  item|ItemStack
|  lifespan|int
|  living|boolean
|  minecraftEntity|Entity
|  monster|boolean
|  motionX|double
|  motionY|double
|  motionZ|double
|  name|String
|  nbt Custom NBT you can use for saving custom data|NBTCompound
|  noClip|boolean
|  noGravity|boolean
|  onGround|boolean
|  owner|String
|  passengers|EntityArrayList
|  pitch|float
|  player|boolean
|  profile|GameProfile
|  recursivePassengers|EntityArrayList
|  ridingEntity|Entity
|  server|Server
|  silent|boolean
|  sneaking|boolean
|  sprinting|boolean
|  stepHeight|float
|  tags|Set\<String>
|  teamID Scoreboard team ID|String
|  thrower|String
|  ticksExisted|int
|  type|ID
|  waterCreature|boolean
|  world|World
|  x|double
|  y|double
|  yaw|float
|  z|double

---

|Methods|Return Type
|--|--
| addMotion(double x, double y, double z)|void
| attack(float hp)|void
| attack(String source, float hp)|void
| dismountRidingEntity()|void
| extinguish()|void
| getNBTData(String key) Get specific value from custom NBT|NBTBase
| isOnSameTeam(Entity entity) Checks if this entity is on the same scoreboard team as another entity|boolean
| isOnScoreboardTeam(String teamID) Checks if this entity is on scoreboard team|boolean
| isPassenger(Entity entity)|boolean
| kill()|void
| playSound(Object id, float volume, float pitch) Play sound at entity. Must be played from server side|void
| playSound(Object id) Play sound at entity. Must be played from server side|void
| removePassengers()|void
| runCommand(String command) Runs command as if the sender was running it, ignoring permissions|int
| setDefaultPickupDelay()|void
| setInfinitePickupDelay()|void
| setMotion(double x, double y, double z)|void
| setNBTData(String key, Object nbt) Set specific value in custom NBT|void
| setNoDespawn()|void
| setNoPickupDelay()|void
| setOnFire(int seconds) Sets entity on fire for x seconds|void
| setPickupDelay(int i)|void
| setPosition(double x, double y, double z)|void
| setPosition(Block block)|void
| setPositionAndRotation(double x, double y, double z, float yaw, float pitch)|void
| setRotation(float yaw, float pitch)|void
| setStatusMessage(Text text) Set status message|void
| spawn() Spawn entity in world|void
| startRiding(Entity entity, boolean force)|boolean
| tell(Text message) Tell message in chat|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityEvent

|Class
|--
|dev.latvian.kubejs.entity.EntityEventJS

---

|Extends
|--
|WorldEvent

---

|Fields|Type
|--|--
|  entity|Entity
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityArrayList

|Class
|--
|dev.latvian.kubejs.player.EntityArrayList

---

|Extends
|--
|ArrayList
|MessageSender

---

|Fields|Type
|--|--
|  displayName|Text
|  empty|boolean
|  first|Entity
|  name|String
|  world|World

---

|Methods|Return Type
|--|--
| add(int arg0, Object arg1)|void
| add(Object o)|boolean
| addAll(int arg0, Collection\<? extends E> arg1)|boolean
| addAll(Collection\<? extends E> c)|boolean
| clear()|void
| clone()|Object
| contains(Object o)|boolean
| containsAll(Collection\<?> c)|boolean
| ensureCapacity(int i)|void
| filter(Predicate\<Entity> filter)|EntityArrayList
| forEach(Consumer\<? super E> c)|void
| get(int i)|Object
| indexOf(Object o)|int
| iterator()|Iterator\<E>
| kill()|void
| lastIndexOf(Object o)|int
| listIterator(int i)|ListIterator\<E>
| listIterator()|ListIterator\<E>
| parallelStream()|Stream\<E>
| playSound(Object id, float volume, float pitch)|void
| playSound(Object id)|void
| remove(Object o)|boolean
| remove(int i)|Object
| removeAll(Collection\<?> c)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| replaceAll(UnaryOperator\<E> u)|void
| retainAll(Collection\<?> c)|boolean
| runCommand(String command) Runs command as if the sender was running it, ignoring permissions|int
| sendData(String channel, Object data)|void
| set(int arg0, Object arg1)|Object
| setStatusMessage(Text message) Set status message|void
| size()|int
| sort(Comparator\<? super E> c)|void
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| subList(int arg0, int arg1)|List\<E>
| tell(Text message) Tell message in chat|void
| toArray()|Object[]
| toArray(Object[] o)|Object[]
| trimToSize()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## QuestObject

|Class
|--
|com.feed_the_beast.ftbquests.quest.QuestObject

---

|Extends
|--
|QuestObjectBase

---

|Fields|Type
|--|--
|  altIcon|Icon
|  altTitle|String
|  codeString|String
|  disableToast|boolean
|  file|File
|  icon|Icon
|  id|int
|  invalid|boolean
|  objectType|QuestObjectType
|  parentID|int
|  questChapter|Chapter
|  questFile|QuestFile
|  tags|Set\<String>
|  title|String
|  unformattedTitle|String
|  yellowDisplayName|String

---

|Methods|Return Type
|--|--
| cacheProgress()|boolean
| changeProgress(QuestData arg0, ChangeProgress arg1)|void
| clearCachedData()|void
| createSubGroup(ConfigGroup c)|ConfigGroup
| createTabContent()|Optional\<Node>
| deleteChildren()|void
| deleteSelf()|void
| editedFromGUI()|void
| forceProgress(QuestData arg0, ChangeProgress arg1, boolean arg2)|void
| getConfig(ConfigGroup c)|void
| getRelativeProgress(QuestData q)|int
| getRelativeProgressFromChildren(QuestData q)|int
| hasTag(String s)|boolean
| isComplete(QuestData q)|boolean
| isStarted(QuestData q)|boolean
| isVisible(QuestData q)|boolean
| loadText()|QuestObjectText
| onCompleted(QuestData arg0, List\<EntityPlayerMP> arg1)|void
| onCreated()|void
| onEditButtonClicked()|void
| readData(NBTTagCompound n)|void
| readNetData(DataIn d)|void
| refreshJEI()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeData(NBTTagCompound n)|void
| writeNetData(DataOut d)|void

---

## CustomReward

|Class
|--
|com.feed_the_beast.ftbquests.quest.reward.CustomReward

---

|Extends
|--
|Reward

---

|Fields|Type
|--|--
|  altIcon|Icon
|  altTitle|String
|  autoClaimType|RewardAutoClaim
|  buttonText|String
|  codeString|String
|  excludeFromClaimAll|boolean
|  file|File
|  icon|Icon
|  id|int
|  ingredient|Object
|  invalid|boolean
|  objectType|QuestObjectType
|  parentID|int
|  quest|Quest
|  questChapter|Chapter
|  questFile|QuestFile
|  tags|Set\<String>
|  team|EnumTristate
|  teamReward|boolean
|  title|String
|  type|RewardType
|  unformattedTitle|String
|  yellowDisplayName|String

---

|Methods|Return Type
|--|--
| addMouseOverText(List\<String> l)|void
| addTitleInMouseOverText()|boolean
| changeProgress(QuestData arg0, ChangeProgress arg1)|void
| claim(EntityPlayerMP arg0, boolean arg1)|void
| claimAutomated(TileEntity arg0, EntityPlayerMP arg1)|ItemStack
| clearCachedData()|void
| createSubGroup(ConfigGroup c)|ConfigGroup
| createTabContent()|Optional\<Node>
| deleteChildren()|void
| deleteSelf()|void
| editedFromGUI()|void
| forceProgress(QuestData arg0, ChangeProgress arg1, boolean arg2)|void
| getConfig(ConfigGroup c)|void
| hasTag(String s)|boolean
| loadText()|QuestObjectText
| onButtonClicked(boolean b)|void
| onCreated()|void
| onEditButtonClicked()|void
| readData(NBTTagCompound n)|void
| readNetData(DataIn d)|void
| refreshJEI()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeData(NBTTagCompound n)|void
| writeNetData(DataOut d)|void

---

## CustomTask

|Class
|--
|com.feed_the_beast.ftbquests.quest.task.CustomTask

---

|Extends
|--
|Task

---

|Fields|Type
|--|--
|  altIcon|Icon
|  altTitle|String
|  buttonText|String
|  check|CustomTask$Check
|  checkTimer|int
|  codeString|String
|  disableToast|boolean
|  enableButton|boolean
|  file|File
|  icon|Icon
|  id|int
|  ingredient|Object
|  invalid|boolean
|  maxProgress|long
|  maxProgressString|String
|  objectType|QuestObjectType
|  parentID|int
|  quest|Quest
|  questChapter|Chapter
|  questFile|QuestFile
|  screenCoreClass|Class\<? extends com.feed_the_beast.ftbquests.tile.TileTaskScreenCore>
|  screenPartClass|Class\<? extends com.feed_the_beast.ftbquests.tile.TileTaskScreenPart>
|  tags|Set\<String>
|  title|String
|  type|TaskType
|  unformattedTitle|String
|  yellowDisplayName|String

---

|Methods|Return Type
|--|--
| addMouseOverText(List\<String> arg0, TaskData arg1)|void
| addTitleInMouseOverText()|boolean
| autoSubmitOnPlayerTick()|int
| cacheProgress()|boolean
| canInsertItem()|boolean
| changeProgress(QuestData arg0, ChangeProgress arg1)|void
| clearCachedData()|void
| consumesResources()|boolean
| createData(QuestData q)|TaskData
| createScreenCore(World w)|TileTaskScreenCore
| createScreenPart(World w)|TileTaskScreenPart
| createSubGroup(ConfigGroup c)|ConfigGroup
| createTabContent()|Optional\<Node>
| deleteChildren()|void
| deleteSelf()|void
| drawGUI(TaskData arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawScreen(TaskData t)|void
| editedFromGUI()|void
| forceProgress(QuestData arg0, ChangeProgress arg1, boolean arg2)|void
| getConfig(ConfigGroup c)|void
| getRelativeProgress(QuestData q)|int
| getRelativeProgressFromChildren(QuestData q)|int
| hasTag(String s)|boolean
| hideProgressNumbers()|boolean
| isComplete(QuestData q)|boolean
| isStarted(QuestData q)|boolean
| isVisible(QuestData q)|boolean
| loadText()|QuestObjectText
| onButtonClicked(boolean b)|void
| onCompleted(QuestData arg0, List\<EntityPlayerMP> arg1)|void
| onCreated()|void
| onEditButtonClicked()|void
| readData(NBTTagCompound n)|void
| readNetData(DataIn d)|void
| refreshJEI()|int
| submitItemsOnInventoryChange()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeData(NBTTagCompound n)|void
| writeNetData(DataOut d)|void

---

## CustomTaskChecker

|Interface
|--
|com.feed_the_beast.ftbquests.integration.kubejs.CustomTaskCheckerJS

---

|Extends
|--

---

|Methods|Return Type
|--|--
| check(CustomTask$Data arg0, Player arg1)|void

---

## TaskData

|Class
|--
|com.feed_the_beast.ftbquests.quest.task.TaskData

---

|Extends
|--
|CapabilityProvider
|ItemHandler

---

|Fields|Type
|--|--
|  complete|boolean
|  data|QuestData
|  progress|long
|  progressString|String
|  relativeProgress|int
|  slots|int
|  started|boolean
|  task|Task

---

|Methods|Return Type
|--|--
| addProgress(long l)|void
| extractItem(int arg0, int arg1, boolean arg2)|ItemStack
| getCapability(Capability\<C> arg0, EnumFacing arg1)|Object
| getSlotLimit(int i)|int
| getStackInSlot(int i)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| insertItem(int arg0, ItemStack arg1, boolean arg2)|ItemStack
| insertItem(ItemStack arg0, boolean arg1, boolean arg2, EntityPlayer arg3)|ItemStack
| isItemValid(int arg0, ItemStack arg1)|boolean
| readProgress(long l)|void
| setProgress(long l)|void
| submitTask(EntityPlayerMP arg0, Collection\<ItemStack> arg1, boolean arg2)|boolean
| submitTask(EntityPlayerMP e)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Inventory

|Class
|--
|dev.latvian.kubejs.item.InventoryJS

---

|Extends
|--

---

|Fields|Type
|--|--
|  empty|boolean
|  size|int

---

|Methods|Return Type
|--|--
| clear(Ingredient ingredient)|void
| clear()|void
| count(Ingredient filter)|int
| count()|int
| countNonEmpty()|int
| countNonEmpty(Ingredient filter)|int
| extract(int slot, int amount, boolean simulate)|ItemStack
| find()|int
| find(Ingredient filter)|int
| get(int slot)|ItemStack
| getBlock(World w)|Block
| getSlotLimit(int slot)|int
| insert(int slot, ItemStack arg1, boolean simulate)|ItemStack
| isItemValid(int slot, ItemStack arg1)|boolean
| markDirty()|void
| set(int slot, ItemStack item)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemBuilder

|Class
|--
|dev.latvian.kubejs.item.ItemBuilder

---

|Extends
|--

---

|Fields|Type
|--|--
|  id|ID

---

|Methods|Return Type
|--|--
| add()|void
| containerItem(ID id)|ItemBuilder
| glow(boolean glow)|ItemBuilder
| maxDamage(int damage)|ItemBuilder
| maxStackSize(int size)|ItemBuilder
| model(String model)|ItemBuilder
| rarity(EnumRarity rarity)|ItemBuilder
| tool(String type, int level)|ItemBuilder
| tooltip(Text text)|ItemBuilder
| translationKey(String translationKey)|ItemBuilder
| unstackable()|ItemBuilder
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Advancement

|Class
|--
|dev.latvian.kubejs.player.AdvancementJS

---

|Extends
|--

---

|Fields|Type
|--|--
|  advancement|Advancement
|  children|Set\<Advancement>
|  description|Text
|  displayText|Text
|  parent|Advancement
|  title|Text

---

|Methods|Return Type
|--|--
| addChild(Advancement a)|void
| hasDisplay()|boolean
| id()|ID
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Container

|Class
|--
|net.minecraft.inventory.Container

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_75149_d|List\<ContainerListener>
|  field_75151_b|List\<Slot>
|  field_75152_c|int
|  field_75153_a|NonNullList\<ItemStack>

---

|Methods|Return Type
|--|--
| func_184996_a(int arg0, int arg1, ClickType arg2, EntityPlayer arg3)|ItemStack
| func_190896_a(List\<ItemStack> l)|void
| func_75128_a(EntityPlayer arg0, boolean arg1)|void
| func_75129_b(EntityPlayer e)|boolean
| func_75130_a(Inventory i)|void
| func_75132_a(ContainerListener c)|void
| func_75134_a(EntityPlayer e)|void
| func_75136_a(InventoryPlayer i)|short
| func_75137_b(int arg0, int arg1)|void
| func_75138_a()|NonNullList\<ItemStack>
| func_75139_a(int i)|Slot
| func_75140_a(EntityPlayer arg0, int arg1)|boolean
| func_75141_a(int arg0, ItemStack arg1)|void
| func_75142_b()|void
| func_75145_c(EntityPlayer e)|boolean
| func_75147_a(Inventory arg0, int arg1)|Slot
| func_82846_b(EntityPlayer arg0, int arg1)|ItemStack
| func_82847_b(ContainerListener c)|void
| func_94530_a(ItemStack arg0, Slot arg1)|boolean
| func_94531_b(Slot s)|boolean
| invtweaks$largeChest()|boolean
| invtweaks$rowSize()|int
| invtweaks$showButtons()|boolean
| invtweaks$slotMap()|Map
| invtweaks$validChest()|boolean
| invtweaks$validInventory()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Inventory

|Interface
|--
|net.minecraft.inventory.IInventory

---

|Extends
|--
|WorldNameable

---

|Methods|Return Type
|--|--
| func_145748_c_()|TextComponent
| func_145818_k_()|boolean
| func_174885_b(int arg0, int arg1)|void
| func_174886_c(EntityPlayer e)|void
| func_174887_a_(int i)|int
| func_174888_l()|void
| func_174889_b(EntityPlayer e)|void
| func_174890_g()|int
| func_191420_l()|boolean
| func_70005_c_()|String
| func_70296_d()|void
| func_70297_j_()|int
| func_70298_a(int arg0, int arg1)|ItemStack
| func_70299_a(int arg0, ItemStack arg1)|void
| func_70300_a(EntityPlayer e)|boolean
| func_70301_a(int i)|ItemStack
| func_70302_i_()|int
| func_70304_b(int i)|ItemStack
| func_94041_b(int arg0, ItemStack arg1)|boolean

---

## RecipeEventBase

|Class
|--
|dev.latvian.kubejs.crafting.RecipeEventBaseJS

---

|Extends
|--
|Event

---

|Fields|Type
|--|--
|  mod|String

---

|Methods|Return Type
|--|--
| add(Map\<String, Object> m)|void
| remove(Object o)|void
| removeInput(Object o)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AlloySmelterRecipeEventJS$AlloySmelterRecipe

|Class
|--
|dev.latvian.kubejs.crafting.AlloySmelterRecipeEventJS$AlloySmelterRecipe

---

|Extends
|--
|Recipe

---

|Fields|Type
|--|--
|  input|List\<Ingredient>
|  output|ItemStack
|  power|float
|  secondaryOutput|ItemStack
|  secondaryOutputChance|float

---

|Methods|Return Type
|--|--
| add()|void
| input(Object o)|AlloySmelterRecipeEventJS$AlloySmelterRecipe
| output(Object o)|AlloySmelterRecipeEventJS$AlloySmelterRecipe
| power(float f)|AlloySmelterRecipeEventJS$AlloySmelterRecipe
| secondary(Object arg0, float arg1)|AlloySmelterRecipeEventJS$AlloySmelterRecipe
| secondary(Object o)|AlloySmelterRecipeEventJS$AlloySmelterRecipe
| set(Map m)|Recipe
| set(Map\<String, Object> m)|AlloySmelterRecipeEventJS$AlloySmelterRecipe
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CompressorRecipeEventJS$CompressorRecipe

|Class
|--
|dev.latvian.kubejs.crafting.CompressorRecipeEventJS$CompressorRecipe

---

|Extends
|--
|Recipe

---

|Fields|Type
|--|--
|  input|Ingredient
|  output|ItemStack
|  power|float

---

|Methods|Return Type
|--|--
| add()|void
| input(Object o)|CompressorRecipeEventJS$CompressorRecipe
| output(Object o)|CompressorRecipeEventJS$CompressorRecipe
| power(float f)|CompressorRecipeEventJS$CompressorRecipe
| set(Map m)|Recipe
| set(Map\<String, Object> m)|CompressorRecipeEventJS$CompressorRecipe
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Recipe

|Interface
|--
|net.minecraft.item.crafting.IRecipe

---

|Extends
|--
|ForgeRegistryEntry

---

|Fields|Type
|--|--
|  registryName|ResourceLocation
|  registryType|Class\<V>

---

|Methods|Return Type
|--|--
| func_179532_b(InventoryCrafting i)|NonNullList\<ItemStack>
| func_192399_d()|boolean
| func_192400_c()|NonNullList\<Ingredient>
| func_193358_e()|String
| func_194133_a(int arg0, int arg1)|boolean
| func_77569_a(InventoryCrafting arg0, World arg1)|boolean
| func_77571_b()|ItemStack
| func_77572_b(InventoryCrafting i)|ItemStack

---

## FurnaceRecipeEventJS$FurnaceRecipe

|Class
|--
|dev.latvian.kubejs.crafting.FurnaceRecipeEventJS$FurnaceRecipe

---

|Extends
|--
|Recipe

---

|Fields|Type
|--|--
|  experience|float
|  input|Ingredient
|  output|ItemStack

---

|Methods|Return Type
|--|--
| add()|void
| input(Object o)|FurnaceRecipeEventJS$FurnaceRecipe
| output(Object o)|FurnaceRecipeEventJS$FurnaceRecipe
| set(Map m)|Recipe
| set(Map\<String, Object> m)|FurnaceRecipeEventJS$FurnaceRecipe
| wait(long arg0, int arg1)|void
| wait(long l)|void
| xp(float f)|FurnaceRecipeEventJS$FurnaceRecipe

---

## PulverizerRecipeEventJS$PulverizerRecipe

|Class
|--
|dev.latvian.kubejs.crafting.PulverizerRecipeEventJS$PulverizerRecipe

---

|Extends
|--
|Recipe

---

|Fields|Type
|--|--
|  input|Ingredient
|  output|ItemStack
|  power|float
|  secondaryOutput|ItemStack
|  secondaryOutputChance|float

---

|Methods|Return Type
|--|--
| add()|void
| input(Object o)|PulverizerRecipeEventJS$PulverizerRecipe
| output(Object o)|PulverizerRecipeEventJS$PulverizerRecipe
| power(float f)|PulverizerRecipeEventJS$PulverizerRecipe
| secondary(Object arg0, float arg1)|PulverizerRecipeEventJS$PulverizerRecipe
| secondary(Object o)|PulverizerRecipeEventJS$PulverizerRecipe
| set(Map m)|Recipe
| set(Map\<String, Object> m)|PulverizerRecipeEventJS$PulverizerRecipe
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ExplosionEvent

|Class
|--
|dev.latvian.kubejs.world.ExplosionEventJS

---

|Extends
|--
|WorldEvent

---

|Fields|Type
|--|--
|  block|Block
|  exploder|LivingEntity
|  position|Vec3d
|  server|Server
|  world|World
|  x|double
|  y|double
|  z|double

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## LivingEntity

|Class
|--
|dev.latvian.kubejs.entity.LivingEntityJS

---

|Extends
|--
|Entity

---

|Fields|Type
|--|--
|  absorptionAmount|float
|  alive|boolean
|  ambientCreature|boolean
|  animal|boolean
|  attackingEntity|LivingEntity
|  block Block position of the entity|Block
|  boss|boolean
|  child|boolean
|  customName Custom display name|String
|  customNameAlwaysVisible Custom display name will always be visible above head|boolean
|  displayName|Text
|  elytraFlying|boolean
|  eyeHeight|float
|  facing|EnumFacing
|  fallDistance|float
|  frame|boolean
|  fullNBT Entity NBT|NBTCompound
|  glowing|boolean
|  hasCustomName Checks if custom display name is set|boolean
|  health|float
|  horizontalFacing|EnumFacing
|  id|UUID
|  idleTime|int
|  invisible|boolean
|  item|ItemStack
|  lastAttackedEntity|LivingEntity
|  lastAttackedEntityTime|int
|  lastDamageSource|DamageSource
|  living|boolean
|  mainHandItem|ItemStack
|  maxHealth|float
|  minecraftEntity|Entity
|  minecraftLivingEntity|EntityLivingBase
|  monster|boolean
|  motionX|double
|  motionY|double
|  motionZ|double
|  movementSpeed|float
|  name|String
|  nbt Custom NBT you can use for saving custom data|NBTCompound
|  noClip|boolean
|  noGravity|boolean
|  offHandItem|ItemStack
|  onGround|boolean
|  onLadder|boolean
|  passengers|EntityArrayList
|  pitch|float
|  player|boolean
|  potionEffects|EntityPotionEffects
|  profile|GameProfile
|  reachDistance|double
|  recursivePassengers|EntityArrayList
|  revengeTarget|LivingEntity
|  revengeTimer|int
|  ridingEntity|Entity
|  server|Server
|  silent|boolean
|  sleeping|boolean
|  sneaking|boolean
|  sprinting|boolean
|  stepHeight|float
|  tags|Set\<String>
|  teamID Scoreboard team ID|String
|  ticksExisted|int
|  type|ID
|  undead|boolean
|  waterCreature|boolean
|  world|World
|  x|double
|  y|double
|  yaw|float
|  z|double

---

|Methods|Return Type
|--|--
| addMotion(double x, double y, double z)|void
| attack(float hp)|void
| attack(String source, float hp)|void
| canEntityBeSeen(Entity entity)|boolean
| damageHeldItem()|void
| damageHeldItem(EnumHand hand, int amount)|void
| dismountRidingEntity()|void
| extinguish()|void
| getEquipment(EntityEquipmentSlot slot)|ItemStack
| getHeldItem(EnumHand hand)|ItemStack
| getNBTData(String key) Get specific value from custom NBT|NBTBase
| heal(float hp)|void
| isHoldingInAnyHand(Ingredient ingredient)|boolean
| isOnSameTeam(Entity entity) Checks if this entity is on the same scoreboard team as another entity|boolean
| isOnScoreboardTeam(String teamID) Checks if this entity is on scoreboard team|boolean
| isPassenger(Entity entity)|boolean
| kill()|void
| playSound(Object id, float volume, float pitch) Play sound at entity. Must be played from server side|void
| playSound(Object id) Play sound at entity. Must be played from server side|void
| rayTrace()|Map\<String, Object>
| rayTrace(double distance)|Map\<String, Object>
| removePassengers()|void
| runCommand(String command) Runs command as if the sender was running it, ignoring permissions|int
| setEquipment(EntityEquipmentSlot slot, ItemStack item)|void
| setHeldItem(EnumHand hand, ItemStack item)|void
| setMotion(double x, double y, double z)|void
| setNBTData(String key, Object nbt) Set specific value in custom NBT|void
| setOnFire(int seconds) Sets entity on fire for x seconds|void
| setPosition(double x, double y, double z)|void
| setPosition(Block block)|void
| setPositionAndRotation(double x, double y, double z, float yaw, float pitch)|void
| setRotation(float yaw, float pitch)|void
| setStatusMessage(Text text) Set status message|void
| spawn() Spawn entity in world|void
| startRiding(Entity entity, boolean force)|boolean
| swingArm(EnumHand hand)|void
| tell(Text message) Tell message in chat|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WorldEvent

|Class
|--
|dev.latvian.kubejs.world.WorldEventJS

---

|Extends
|--
|Event

---

|Fields|Type
|--|--
|  server|Server
|  world|World

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RegistryEvent$MissingMappings$Mapping

|Class
|--
|net.minecraftforge.event.RegistryEvent$MissingMappings$Mapping

---

|Extends
|--

---

|Fields|Type
|--|--
|  action|RegistryEvent$MissingMappings$Action
|  id|int
|  key|ResourceLocation
|  registry|ForgeRegistry\<T>
|  target|ForgeRegistryEntry

---

|Methods|Return Type
|--|--
| fail()|void
| ignore()|void
| remap(ForgeRegistryEntry f)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void
| warn()|void

---

## StringSerializable

|Interface
|--
|net.minecraft.util.IStringSerializable

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_176610_l()|String

---

## Vec3i

|Class
|--
|net.minecraft.util.math.Vec3i

---

|Extends
|--
|Comparable

---

|Methods|Return Type
|--|--
| compareTo(Vec3i v)|int
| compareTo(Object o)|int
| func_177951_i(Vec3i v)|double
| func_177952_p()|int
| func_177954_c(double arg0, double arg1, double arg2)|double
| func_177955_d(Vec3i v)|Vec3i
| func_177956_o()|int
| func_177957_d(double arg0, double arg1, double arg2)|double
| func_177958_n()|int
| func_185332_f(int arg0, int arg1, int arg2)|double
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumFacing$Axis

|Class
|--
|net.minecraft.util.EnumFacing$Axis

---

|Extends
|--
|Enum
|Predicate
|StringSerializable

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| and(Predicate\<? super T> p)|Predicate\<T>
| apply(EnumFacing e)|boolean
| apply(Object o)|boolean
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_176610_l()|String
| func_176716_d()|EnumFacing$Plane
| func_176719_a()|String
| func_176720_b()|boolean
| func_176722_c()|boolean
| name()|String
| negate()|Predicate\<T>
| or(Predicate\<? super T> p)|Predicate\<T>
| ordinal()|int
| test(Object o)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumFacing$AxisDirection

|Class
|--
|net.minecraft.util.EnumFacing$AxisDirection

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_179524_a()|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockEntityPredicateDataCheck

|Interface
|--
|dev.latvian.kubejs.block.predicate.BlockEntityPredicateDataCheck

---

|Extends
|--

---

|Methods|Return Type
|--|--
| checkData(NBTCompound n)|boolean

---

## IForgeRegistryEntry$Impl

|Class
|--
|net.minecraftforge.registries.IForgeRegistryEntry$Impl

---

|Extends
|--
|ForgeRegistryEntry

---

|Fields|Type
|--|--
|  delegate|RegistryDelegate\<T>
|  registryName|ResourceLocation
|  registryType|Class\<T>

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockIDPredicate$PropertyObject

|Class
|--
|dev.latvian.kubejs.block.predicate.BlockIDPredicate$PropertyObject

---

|Extends
|--

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Gui

|Class
|--
|net.minecraft.client.gui.Gui

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_73735_i|float

---

|Methods|Return Type
|--|--
| func_175174_a(float arg0, float arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_175175_a(int arg0, int arg1, TextureAtlasSprite arg2, int arg3, int arg4)|void
| func_73729_b(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73731_b(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73732_a(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73733_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GuiYesNoCallback

|Interface
|--
|net.minecraft.client.gui.GuiYesNoCallback

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_73878_a(boolean arg0, int arg1)|void

---

## GuiButton

|Class
|--
|net.minecraft.client.gui.GuiButton

---

|Extends
|--
|Gui

---

|Fields|Type
|--|--
|  field_146120_f|int
|  field_146121_g|int
|  field_146124_l|boolean
|  field_146125_m|boolean
|  field_146126_j|String
|  field_146127_k|int
|  field_146128_h|int
|  field_146129_i|int
|  field_73735_i|float
|  packedFGColour|int

---

|Methods|Return Type
|--|--
| func_146111_b(int arg0, int arg1)|void
| func_146113_a(SoundHandler s)|void
| func_146115_a()|boolean
| func_146116_c(Minecraft arg0, int arg1, int arg2)|boolean
| func_146117_b()|int
| func_146118_a(int arg0, int arg1)|void
| func_175174_a(float arg0, float arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_175175_a(int arg0, int arg1, TextureAtlasSprite arg2, int arg3, int arg4)|void
| func_175211_a(int i)|void
| func_191745_a(Minecraft arg0, int arg1, int arg2, float arg3)|void
| func_73729_b(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73731_b(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73732_a(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73733_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TextureAtlasSprite

|Class
|--
|net.minecraft.client.renderer.texture.TextureAtlasSprite

---

|Extends
|--

---

|Fields|Type
|--|--
|  animationActive|boolean
|  animationIndex|int
|  animationMetadata|AnimationMetadataSection
|  baseU|float
|  baseV|float
|  dependencies|Collection\<ResourceLocation>
|  field_110982_k|AnimationMetadataSection
|  framesTextureData|List\<int[][]>
|  glSpriteTextureId|int
|  indexInMap|int
|  isDependencyParent|boolean
|  isEmissive|boolean
|  isShadersSprite|boolean
|  isSpriteSingle|boolean
|  mipmapLevels|int
|  sheetHeight|int
|  sheetWidth|int
|  spriteEmissive|TextureAtlasSprite
|  spriteNormal|TextureAtlasSprite
|  spriteSingle|TextureAtlasSprite
|  spriteSpecular|TextureAtlasSprite

---

|Methods|Return Type
|--|--
| bindSpriteTexture()|void
| deleteSpriteTexture()|void
| func_110966_b(int i)|void
| func_110967_i()|int
| func_110968_a(List\<int[][]> l)|void
| func_110969_c(int i)|void
| func_110970_k()|int
| func_110971_a(int arg0, int arg1, int arg2, int arg3, boolean arg4)|void
| func_130010_a()|int
| func_130098_m()|boolean
| func_130099_d(int i)|void
| func_130102_n()|void
| func_130103_l()|void
| func_147963_d(int i)|void
| func_147965_a(int i)|int[][]
| func_180599_n()|void
| func_188536_b(float f)|float
| func_188537_a(float f)|float
| func_188538_a(PngSizeInfo arg0, boolean arg1)|void
| func_188539_a(Resource arg0, int arg1)|void
| func_94206_g()|float
| func_94207_b(double d)|float
| func_94209_e()|float
| func_94210_h()|float
| func_94211_a()|int
| func_94212_f()|float
| func_94214_a(double d)|float
| func_94215_i()|String
| func_94216_b()|int
| func_94217_a(TextureAtlasSprite t)|void
| func_94219_l()|void
| getSpriteU16(float f)|double
| getSpriteV16(float f)|double
| hasCustomLoader(ResourceManager arg0, ResourceLocation arg1)|boolean
| load(ResourceManager arg0, ResourceLocation arg1, Function\<ResourceLocation, TextureAtlasSprite> arg2)|boolean
| toSingleU(float f)|float
| toSingleV(float f)|float
| updateIndexInMap(CounterInt c)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TextComponent

|Interface
|--
|net.minecraft.util.text.ITextComponent

---

|Extends
|--
|Iterable

---

|Methods|Return Type
|--|--
| forEach(Consumer\<? super T> c)|void
| func_150253_a()|List\<TextComponent>
| func_150254_d()|String
| func_150255_a(Style s)|TextComponent
| func_150256_b()|Style
| func_150257_a(TextComponent t)|TextComponent
| func_150258_a(String s)|TextComponent
| func_150259_f()|TextComponent
| func_150260_c()|String
| func_150261_e()|String
| iterator()|Iterator\<T>
| spliterator()|Spliterator\<T>

---

## ThreadListener

|Interface
|--
|net.minecraft.util.IThreadListener

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_152344_a(Runnable r)|ListenableFuture\<Object>
| func_152345_ab()|boolean

---

## SnooperInfo

|Interface
|--
|net.minecraft.profiler.ISnooperInfo

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_70000_a(Snooper s)|void
| func_70001_b(Snooper s)|void
| func_70002_Q()|boolean

---

## ResourcePack

|Interface
|--
|net.minecraft.client.resources.IResourcePack

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_110586_a()|BufferedImage
| func_110587_b()|Set\<String>
| func_110589_b(ResourceLocation r)|boolean
| func_110590_a(ResourceLocation r)|InputStream
| func_130077_b()|String
| func_135058_a(MetadataSerializer arg0, String arg1)|MetadataSection

---

## DefaultResourcePack

|Class
|--
|net.minecraft.client.resources.DefaultResourcePack

---

|Extends
|--
|ResourcePack

---

|Methods|Return Type
|--|--
| func_110586_a()|BufferedImage
| func_110587_b()|Set\<String>
| func_110589_b(ResourceLocation r)|boolean
| func_110590_a(ResourceLocation r)|InputStream
| func_130077_b()|String
| func_135058_a(MetadataSerializer arg0, String arg1)|MetadataSection
| func_152780_c(ResourceLocation r)|InputStream
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ReloadableResourceManager

|Interface
|--
|net.minecraft.client.resources.IReloadableResourceManager

---

|Extends
|--
|ResourceManager

---

|Methods|Return Type
|--|--
| func_110536_a(ResourceLocation r)|Resource
| func_110541_a(List\<ResourcePack> l)|void
| func_110542_a(ResourceManagerReloadListener r)|void
| func_135055_a()|Set\<String>
| func_135056_b(ResourceLocation r)|List\<Resource>

---

## BlockRendererDispatcher

|Class
|--
|net.minecraft.client.renderer.BlockRendererDispatcher

---

|Extends
|--
|ResourceManagerReloadListener

---

|Methods|Return Type
|--|--
| func_110549_a(ResourceManager r)|void
| func_175016_a(BlockState arg0, float arg1)|void
| func_175018_a(BlockState arg0, BlockPos arg1, BlockAccess arg2, BufferBuilder arg3)|boolean
| func_175019_b()|BlockModelRenderer
| func_175020_a(BlockState arg0, BlockPos arg1, TextureAtlasSprite arg2, BlockAccess arg3)|void
| func_175023_a()|BlockModelShapes
| func_184389_a(BlockState b)|BakedModel
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## FrameTimer

|Class
|--
|net.minecraft.util.FrameTimer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_181746_c()|long[]
| func_181747_a(long l)|void
| func_181748_a(long arg0, int arg1)|int
| func_181749_a()|int
| func_181750_b()|int
| func_181751_b(int i)|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## DebugRenderer

|Class
|--
|net.minecraft.client.renderer.debug.DebugRenderer

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_188286_a|DebugRenderer$IDebugRenderer
|  field_188287_b|DebugRenderer$IDebugRenderer
|  field_190077_c|DebugRenderer$IDebugRenderer
|  field_190078_d|DebugRenderer$IDebugRenderer
|  field_191325_e|DebugRenderer$IDebugRenderer
|  field_191557_f|DebugRenderer$IDebugRenderer
|  field_193852_g|DebugRenderer$IDebugRenderer

---

|Methods|Return Type
|--|--
| func_190073_a(float arg0, long arg1)|void
| func_190074_a()|boolean
| func_190075_b()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CreativeSettings

|Class
|--
|net.minecraft.client.settings.CreativeSettings

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_192562_a()|void
| func_192563_a(int i)|HotbarSnapshot
| func_192564_b()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MouseHelper

|Class
|--
|net.minecraft.util.MouseHelper

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_74375_b|int
|  field_74377_a|int

---

|Methods|Return Type
|--|--
| func_74372_a()|void
| func_74373_b()|void
| func_74374_c()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Profiler

|Class
|--
|net.minecraft.profiler.Profiler

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_76327_a|boolean
|  profilerGlobalEnabled|boolean

---

|Methods|Return Type
|--|--
| func_194339_b(Supplier\<String> s)|void
| func_194340_a(Supplier\<String> s)|void
| func_76317_a()|void
| func_76318_c(String s)|void
| func_76319_b()|void
| func_76320_a(String s)|void
| func_76321_b(String s)|List\<Profiler$Result>
| func_76322_c()|String
| startSection(Class\<?> c)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Timer

|Class
|--
|net.minecraft.util.Timer

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_194147_b|float
|  field_194148_c|float
|  field_194149_e|float
|  field_74280_b|int

---

|Methods|Return Type
|--|--
| func_74275_a()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RenderGlobal

|Class
|--
|net.minecraft.client.renderer.RenderGlobal

---

|Extends
|--
|WorldEventListener
|ResourceManagerReloadListener

---

|Fields|Type
|--|--
|  chunksToResortTransparency|Set
|  chunksToUpdateForced|Set
|  chunksToUpdatePrev|Set\<RenderChunk>
|  cloudRenderer|CloudRenderer
|  countActiveRenderers|int
|  countChunksToUpdate|int
|  countEntitiesRendered|int
|  countLoadedChunks|int
|  countLoadedChunksPrev|int
|  countRenderers|int
|  countTileEntitiesRendered|int
|  field_147593_P|Map\<BlockPos, Sound>
|  field_147595_R|boolean
|  field_147596_f|double
|  field_147597_g|double
|  field_147602_h|double
|  field_174987_D|double
|  field_174988_E|int
|  field_174989_F|int
|  field_174990_G|int
|  field_174991_A|ShaderGroup
|  field_174992_B|double
|  field_174993_C|double
|  field_174994_L|double
|  field_174995_M|ChunkRenderDispatcher
|  field_174996_N|ChunkRenderContainer
|  field_174997_H|double
|  field_174998_I|double
|  field_174999_J|double
|  field_175000_K|double
|  field_175001_U|ClippingHelper
|  field_175002_T|boolean
|  field_175003_W|Vector3d
|  field_175004_V|Vector4f[]
|  field_175005_X|boolean
|  field_175007_a|RenderChunkFactory
|  field_175008_n|ViewFrustum
|  field_175009_l|Set\<RenderChunk>
|  field_175010_j|RenderManager
|  field_175011_u|VertexBuffer
|  field_175012_t|VertexBuffer
|  field_175013_s|VertexBuffer
|  field_175014_r|VertexFormat
|  field_175015_z|Framebuffer
|  field_181024_n|Set\<TileEntity>
|  field_184386_ad|boolean
|  field_184387_ae|Set\<BlockPos>
|  field_72738_E|Map\<int, DestroyBlockProgress>
|  field_72739_F|int
|  field_72740_G|int
|  field_72748_H|int
|  field_72749_I|int
|  field_72750_J|int
|  field_72755_R|List\<RenderGlobal$ContainerLocalRenderInformation>
|  field_72769_h|WorldClient
|  field_72770_i|TextureManager
|  field_72771_w|int
|  field_72772_v|int
|  field_72773_u|int
|  field_72777_q|Minecraft
|  field_72781_x|int
|  field_94141_F|TextureAtlasSprite[]
|  renderDistance|int
|  renderDistanceSq|int
|  renderedEntity|Entity
|  renderEnv|RenderEnv
|  renderInfosEntities|List
|  renderInfosEntitiesNormal|List
|  renderInfosEntitiesShadow|List
|  renderInfosNormal|List
|  renderInfosShadow|List
|  renderInfosTileEntities|List
|  renderInfosTileEntitiesNormal|List
|  renderInfosTileEntitiesShadow|List
|  renderOverlayDamaged|boolean
|  renderOverlayEyes|boolean
|  visibilityDeque|Deque
|  world|WorldClient
|  worldChunkProvider|ChunkProvider
|  worldChunkProviderMap|Long2ObjectMap\<Chunk>

---

|Methods|Return Type
|--|--
| clearRenderInfos()|void
| func_110549_a(ResourceManager r)|void
| func_147585_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_174959_b(BlockPos b)|void
| func_174962_a(Entity arg0, double arg1)|Vector3f
| func_174963_q()|void
| func_174964_o()|void
| func_174965_a(Iterator\<DestroyBlockProgress> i)|void
| func_174966_b()|void
| func_174967_a(long l)|void
| func_174968_a(BufferBuilder arg0, float arg1, boolean arg2)|void
| func_174969_t()|void
| func_174970_a(Entity arg0, double arg1, Camera arg2, int arg3, boolean arg4)|void
| func_174971_n()|void
| func_174972_a(EnumParticleTypes arg0, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, int[] arg7)|void
| func_174974_b(int arg0, boolean arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, int[] arg8)|Particle
| func_174975_c()|void
| func_174976_a(float arg0, int arg1)|void
| func_174977_a(BlockRenderLayer arg0, double arg1, int arg2, Entity arg3)|int
| func_174978_c(BlockPos b)|Set\<EnumFacing>
| func_174979_m()|void
| func_174980_p()|void
| func_174981_a(Tessellator arg0, BufferBuilder arg1, Entity arg2, float arg3)|void
| func_174982_a(BlockRenderLayer b)|void
| func_174984_a(double arg0, double arg1, double arg2)|void
| func_174985_d()|boolean
| func_174986_e()|void
| func_180439_a(EntityPlayer arg0, int arg1, BlockPos arg2, int arg3)|void
| func_180440_a(int arg0, BlockPos arg1, int arg2)|void
| func_180441_b(int arg0, BlockPos arg1, int arg2)|void
| func_180442_a(int arg0, boolean arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, int[] arg8)|void
| func_180443_s()|void
| func_180444_a(BufferBuilder b)|void
| func_180445_c(float arg0, int arg1, double arg2, double arg3, double arg4)|void
| func_180446_a(Entity arg0, Camera arg1, float arg2)|void
| func_180447_b(float arg0, int arg1, double arg2, double arg3, double arg4)|void
| func_180448_r()|void
| func_180449_a(Entity arg0, float arg1)|void
| func_181023_a(Collection\<TileEntity> arg0, Collection\<TileEntity> arg1)|void
| func_184375_a(EntityPlayer arg0, SoundEvent arg1, SoundCategory arg2, double arg3, double arg4, double arg5, float arg6, float arg7)|void
| func_184376_a(World arg0, BlockPos arg1, BlockState arg2, BlockState arg3, int arg4)|void
| func_184377_a(SoundEvent arg0, BlockPos arg1)|void
| func_184382_g()|int
| func_184383_a(Entity arg0, Entity arg1, Camera arg2)|boolean
| func_184384_n()|boolean
| func_184385_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5, boolean arg6)|void
| func_190570_a(int arg0, boolean arg1, boolean arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, int[] arg9)|void
| func_190571_b(int arg0, boolean arg1, boolean arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, int[] arg9)|Particle
| func_190572_a(boolean b)|int
| func_193054_a(World arg0, BlockPos arg1, boolean arg2)|void
| func_72703_a(Entity e)|void
| func_72709_b(Entity e)|void
| func_72712_a()|void
| func_72720_a(int arg0, int arg1)|void
| func_72721_a(double arg0, double arg1, double arg2, float arg3)|boolean
| func_72723_d()|String
| func_72728_f()|void
| func_72731_b(EntityPlayer arg0, RayTraceResult arg1, int arg2, float arg3)|void
| func_72732_a(WorldClient w)|void
| func_72734_e()|void
| func_72735_c()|String
| getRenderChunk(BlockPos b)|RenderChunk
| getRenderChunkOffset(BlockPos arg0, RenderChunk arg1, EnumFacing arg2, boolean arg3, int arg4)|RenderChunk
| resetClouds()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityPlayerSP

|Class
|--
|net.minecraft.client.entity.EntityPlayerSP

---

|Extends
|--
|AbstractClientPlayer

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  defaultEyeHeight|float
|  displayNameString|String
|  entityData|NBTTagCompound
|  entityShoulderLeft|EntityShoulderRiding
|  entityShoulderRight|EntityShoulderRiding
|  eyeHeight|float
|  field_110153_bc|float
|  field_110158_av|int
|  field_175152_f|int
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_184617_aD|int
|  field_184618_aE|float
|  field_184619_aG|float
|  field_184622_au|EnumHand
|  field_184627_bm|ItemStack
|  field_184628_bn|int
|  field_184835_a|float
|  field_184836_b|float
|  field_184837_c|float
|  field_190534_ay|int
|  field_191988_bg|float
|  field_192036_cb|RecipeBook
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_70701_bs|float
|  field_70702_br|float
|  field_70703_bu|boolean
|  field_70704_bt|float
|  field_70718_bc|int
|  field_70720_be|int
|  field_70721_aZ|float
|  field_70725_aQ|int
|  field_70726_aT|float
|  field_70727_aS|float
|  field_70732_aI|float
|  field_70733_aJ|float
|  field_70737_aN|int
|  field_70738_aO|int
|  field_70739_aP|float
|  field_70747_aH|float
|  field_70755_b|EntityLivingBase
|  field_70758_at|float
|  field_70759_as|float
|  field_70760_ar|float
|  field_70761_aq|float
|  field_70769_ao|float
|  field_70770_ap|float
|  field_70771_an|int
|  field_71067_cb|int
|  field_71068_ca|int
|  field_71069_bz|Container
|  field_71070_bA|Container
|  field_71071_by|InventoryPlayer
|  field_71075_bZ|PlayerCapabilities
|  field_71076_b|int
|  field_71079_bU|float
|  field_71080_cy|float
|  field_71081_bT|BlockPos
|  field_71082_cx|float
|  field_71083_bS|boolean
|  field_71085_bR|double
|  field_71086_bY|float
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71089_bV|float
|  field_71090_bL|int
|  field_71091_bM|double
|  field_71093_bK|int
|  field_71094_bP|double
|  field_71095_bQ|double
|  field_71096_bN|double
|  field_71097_bO|double
|  field_71104_cf|EntityFishHook
|  field_71106_cc|float
|  field_71107_bF|float
|  field_71109_bG|float
|  field_71154_f|float
|  field_71155_g|float
|  field_71156_d|int
|  field_71157_e|int
|  field_71158_b|MovementInput
|  field_71163_h|float
|  field_71164_i|float
|  field_71174_a|NetHandlerPlayClient
|  field_82151_R|float
|  field_82153_h|int
|  field_82175_bq|boolean
|  field_98038_p|boolean
|  itemInUseMaxDuration|int
|  locationOfCape|ResourceLocation
|  nameClear|String
|  persistentID|UUID
|  prefixes|Collection\<TextComponent>
|  spawnDimension|int
|  suffixes|Collection\<TextComponent>
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| addPrefix(TextComponent t)|void
| addSuffix(TextComponent t)|void
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| curePotionEffects(ItemStack i)|void
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_110124_au()|UUID
| func_110138_aP()|float
| func_110139_bj()|float
| func_110140_aT()|AbstractAttributeMap
| func_110142_aN()|CombatTracker
| func_110143_aJ()|float
| func_110144_aD()|EntityLivingBase
| func_110145_l(Entity e)|void
| func_110148_a(Attribute a)|AttributeInstance
| func_110149_m(float f)|void
| func_110303_q()|ResourceLocation
| func_110306_p()|ResourceLocation
| func_110317_t()|boolean
| func_110319_bJ()|float
| func_130011_c(Entity e)|void
| func_130014_f_()|World
| func_142013_aG()|int
| func_142015_aE()|int
| func_142021_k()|String
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_146097_a(ItemStack arg0, boolean arg1, boolean arg2)|EntityItem
| func_146103_bH()|GameProfile
| func_146105_b(TextComponent arg0, boolean arg1)|void
| func_146107_m()|StatisticsManager
| func_152111_bt()|void
| func_152112_bu()|void
| func_152122_n()|boolean
| func_152123_o()|boolean
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_175138_ci()|int
| func_175140_cp()|boolean
| func_175141_a(TileEntitySign t)|void
| func_175142_cm()|boolean
| func_175144_cb()|boolean
| func_175145_a(StatBase s)|void
| func_175146_a(LockCode l)|boolean
| func_175148_a(EnumPlayerModelParts e)|boolean
| func_175149_v()|boolean
| func_175150_k(boolean b)|void
| func_175151_a(BlockPos arg0, EnumFacing arg1, ItemStack arg2)|boolean
| func_175154_l()|String
| func_175155_b()|NetworkPlayerInfo
| func_175156_o()|float
| func_175158_f(String s)|void
| func_175159_q()|void
| func_175163_u()|void
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180468_a(InteractionObject i)|void
| func_180469_a(BlockPos b)|EntityPlayer$SleepResult
| func_180470_cg()|BlockPos
| func_180472_a(Merchant m)|void
| func_180473_a(BlockPos arg0, boolean arg1)|void
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_184582_a(EntityEquipmentSlot e)|ItemStack
| func_184583_d(DamageSource d)|boolean
| func_184585_cz()|boolean
| func_184586_b(EnumHand e)|ItemStack
| func_184587_cr()|boolean
| func_184589_d(Potion p)|void
| func_184591_cq()|EnumHandSide
| func_184592_cb()|ItemStack
| func_184595_k(double arg0, double arg1, double arg2)|boolean
| func_184596_c(Potion p)|PotionEffect
| func_184597_cx()|void
| func_184598_c(EnumHand e)|void
| func_184599_cB()|int
| func_184600_cs()|EnumHand
| func_184602_cy()|void
| func_184603_cC()|boolean
| func_184605_cv()|int
| func_184607_cu()|ItemStack
| func_184609_a(EnumHand e)|void
| func_184611_a(EnumHand arg0, ItemStack arg1)|void
| func_184612_cw()|int
| func_184613_cA()|boolean
| func_184614_ca()|ItemStack
| func_184809_a(CommandBlockBaseLogic c)|void
| func_184810_cG()|void
| func_184811_cZ()|CooldownTracker
| func_184812_l_()|boolean
| func_184813_a(BlockState b)|float
| func_184814_a(ItemStack arg0, EnumHand arg1)|void
| func_184816_a(EntityItem e)|ItemStack
| func_184817_da()|float
| func_184818_cX()|float
| func_184819_a(EnumHandSide e)|void
| func_184821_cY()|void
| func_184823_b(BlockState b)|boolean
| func_184824_a(TileEntityCommandBlock t)|void
| func_184825_o(float f)|float
| func_184826_a(AbstractHorse arg0, Inventory arg1)|void
| func_184833_s()|boolean
| func_184834_t()|ResourceLocation
| func_184838_M()|boolean
| func_184839_n(int i)|void
| func_184840_I()|int
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_189748_bU()|DamageSource
| func_189807_a(TileEntityStructure t)|void
| func_189808_dh()|boolean
| func_189809_N()|boolean
| func_190530_aW()|boolean
| func_190630_a(EntityEquipmentSlot e)|boolean
| func_190631_cK()|boolean
| func_190775_a(Entity arg0, EnumHand arg1)|EnumActionResult
| func_190777_m(boolean b)|void
| func_191521_c(ItemStack i)|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_191986_a(float arg0, float arg1, float arg2)|void
| func_191987_a(BlockPos arg0, boolean arg1)|void
| func_192021_a(List\<Recipe> l)|void
| func_192022_b(List\<Recipe> l)|void
| func_192023_dk()|NBTTagCompound
| func_192024_a(ItemStack arg0, int arg1)|void
| func_192025_dl()|NBTTagCompound
| func_192027_g(NBTTagCompound n)|boolean
| func_192035_E()|RecipeBook
| func_193076_bZ()|Map\<Potion, PotionEffect>
| func_193102_a(ResourceLocation[] r)|void
| func_193103_a(Recipe r)|void
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70065_x()|void
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70604_c(EntityLivingBase e)|void
| func_70606_j(float f)|void
| func_70608_bn()|boolean
| func_70613_aW()|boolean
| func_70617_f_()|boolean
| func_70626_be()|void
| func_70631_g_()|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70636_d()|void
| func_70637_d(boolean b)|void
| func_70643_av()|EntityLivingBase
| func_70644_a(Potion p)|boolean
| func_70645_a(DamageSource d)|void
| func_70648_aU()|boolean
| func_70651_bq()|Collection\<PotionEffect>
| func_70652_k(Entity e)|boolean
| func_70653_a(Entity arg0, float arg1, double arg2, double arg3)|void
| func_70654_ax()|int
| func_70658_aO()|int
| func_70659_e(float f)|void
| func_70660_b(Potion p)|PotionEffect
| func_70662_br()|boolean
| func_70664_aZ()|void
| func_70668_bt()|EnumCreatureAttribute
| func_70669_a(ItemStack i)|void
| func_70674_bp()|void
| func_70676_i(float f)|Vec3d
| func_70678_g(float f)|float
| func_70681_au()|Random
| func_70685_l(Entity e)|boolean
| func_70687_e(PotionEffect p)|boolean
| func_70689_ay()|float
| func_70690_d(PotionEffect p)|void
| func_70691_i(float f)|void
| func_70996_bM()|boolean
| func_70999_a(boolean arg0, boolean arg1, boolean arg2)|void
| func_71000_j(double arg0, double arg1, double arg2)|void
| func_71001_a(Entity arg0, int arg1)|void
| func_71004_bE()|void
| func_71005_bN()|InventoryEnderChest
| func_71007_a(Inventory i)|void
| func_71009_b(Entity e)|void
| func_71016_p()|void
| func_71019_a(ItemStack arg0, boolean arg1)|EntityItem
| func_71020_j(float f)|void
| func_71023_q(int i)|void
| func_71024_bL()|FoodStats
| func_71026_bH()|boolean
| func_71029_a(StatBase s)|void
| func_71033_a(GameType g)|void
| func_71037_bA()|int
| func_71040_bB(boolean b)|EntityItem
| func_71043_e(boolean b)|boolean
| func_71047_c(Entity e)|void
| func_71050_bK()|int
| func_71051_bG()|float
| func_71053_j()|void
| func_71059_n(Entity e)|void
| func_71060_bI()|int
| func_71064_a(StatBase arg0, int arg1)|void
| func_71150_b(float f)|void
| func_71152_a(float arg0, int arg1, int arg2)|void
| func_71165_d(String s)|void
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_82242_a(int i)|void
| func_82243_bO()|float
| func_82245_bX()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_85034_r(int i)|void
| func_85035_bI()|int
| func_85039_t(int i)|void
| func_85040_s(int i)|void
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_94060_bK()|EntityLivingBase
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96122_a(EntityPlayer e)|boolean
| func_96123_co()|Scoreboard
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| getBedLocation(int i)|BlockPos
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getDigSpeed(BlockState arg0, BlockPos arg1)|float
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| hasElytraCape()|boolean
| hasSpawnDimension()|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| isSpawnForced(int i)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| openGui(Object arg0, int arg1, World arg2, int arg3, int arg4, int arg5)|void
| refreshDisplayName()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| setSpawnChunk(BlockPos arg0, boolean arg1, int arg2)|void
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderFaceForward(EntityPlayer e)|boolean
| shouldRiderSit()|boolean
| updateSyncFields(EntityPlayerSP e)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WorldClient

|Class
|--
|net.minecraft.client.multiplayer.WorldClient

---

|Extends
|--
|World

---

|Fields|Type
|--|--
|  captureBlockSnapshots|boolean
|  capturedBlockSnapshots|ArrayList\<BlockSnapshot>
|  currentMoonPhaseFactorBody|float
|  field_147482_g|List\<TileEntity>
|  field_175730_i|List\<TileEntity>
|  field_72982_D|VillageCollection
|  field_72984_F|Profiler
|  field_72995_K|boolean
|  field_72996_f|List\<Entity>
|  field_73003_n|float
|  field_73004_o|float
|  field_73007_j|List\<Entity>
|  field_73010_i|List\<EntityPlayer>
|  field_73011_w|WorldProvider
|  field_73012_v|Random
|  field_73017_q|float
|  field_73018_p|float
|  persistentChunks|ImmutableSetMultimap\<ChunkPos, ForgeChunkManager$Ticket>
|  perWorldStorage|MapStorage
|  playerUpdate|boolean
|  restoringBlockSnapshots|boolean

---

|Methods|Return Type
|--|--
| calculateInitialWeatherBody()|void
| canBlockFreezeBody(BlockPos arg0, boolean arg1)|boolean
| canMineBlockBody(EntityPlayer arg0, BlockPos arg1)|boolean
| canSnowAtBody(BlockPos arg0, boolean arg1)|boolean
| countEntities(EnumCreatureType arg0, boolean arg1)|int
| foamfix_removeUnloadedEntities()|void
| func_130001_d()|float
| func_147442_i(float f)|void
| func_147447_a(Vec3d arg0, Vec3d arg1, boolean arg2, boolean arg3, boolean arg4)|RayTraceResult
| func_147448_a(Collection\<TileEntity> c)|void
| func_147457_a(TileEntity t)|void
| func_147458_c(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_147470_e(AxisAlignedBB a)|boolean
| func_152378_a(UUID u)|EntityPlayer
| func_175623_d(BlockPos b)|boolean
| func_175624_G()|WorldType
| func_175625_s(BlockPos b)|TileEntity
| func_175626_b(BlockPos arg0, int arg1)|int
| func_175627_a(BlockPos arg0, EnumFacing arg1)|int
| func_175636_b(double arg0, double arg1, double arg2, double arg3)|boolean
| func_175639_b(StructureBoundingBox arg0, boolean arg1)|boolean
| func_175640_z(BlockPos b)|boolean
| func_175641_c(BlockPos arg0, Block arg1, int arg2, int arg3)|void
| func_175642_b(EnumSkyBlock arg0, BlockPos arg1)|int
| func_175643_b()|World
| func_175644_a(Class\<? extends T> arg0, Predicate\<? super T> arg1)|List\<T>
| func_175645_m(BlockPos b)|BlockPos
| func_175646_b(BlockPos arg0, TileEntity arg1)|void
| func_175647_a(Class\<? extends T> arg0, AxisAlignedBB arg1, Predicate\<? super T> arg2)|List\<T>
| func_175648_a(BlockPos arg0, int arg1, boolean arg2)|boolean
| func_175649_E(BlockPos b)|DifficultyInstance
| func_175650_b(Collection\<Entity> c)|void
| func_175651_c(BlockPos arg0, EnumFacing arg1)|int
| func_175652_B(BlockPos b)|void
| func_175653_a(EnumSkyBlock arg0, BlockPos arg1, int arg2)|void
| func_175654_a(BlockPos arg0, Block arg1, int arg2, int arg3)|void
| func_175655_b(BlockPos arg0, boolean arg1)|boolean
| func_175656_a(BlockPos arg0, BlockState arg1)|boolean
| func_175657_ab()|int
| func_175658_ac()|int
| func_175659_aa()|EnumDifficulty
| func_175660_a(EntityPlayer arg0, BlockPos arg1)|boolean
| func_175661_b(Class\<? extends T> arg0, Predicate\<? super T> arg1)|List\<T>
| func_175662_w(BlockPos b)|boolean
| func_175664_x(BlockPos b)|boolean
| func_175665_u(BlockPos b)|boolean
| func_175666_e(BlockPos arg0, Block arg1)|void
| func_175667_e(BlockPos b)|boolean
| func_175668_a(BlockPos arg0, boolean arg1)|boolean
| func_175669_a(int arg0, BlockPos arg1, int arg2)|void
| func_175670_e(BlockPos arg0, boolean arg1)|boolean
| func_175671_l(BlockPos b)|int
| func_175672_r(BlockPos b)|BlockPos
| func_175674_a(Entity arg0, AxisAlignedBB arg1, Predicate\<? super net.minecraft.entity.Entity> arg2)|List\<Entity>
| func_175675_v(BlockPos b)|boolean
| func_175676_y(BlockPos b)|int
| func_175677_d(BlockPos arg0, boolean arg1)|boolean
| func_175678_i(BlockPos b)|boolean
| func_175679_n(BlockPos b)|void
| func_175681_c(Collection\<Entity> c)|void
| func_175682_a(EnumParticleTypes arg0, boolean arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, int[] arg8)|void
| func_175684_a(BlockPos arg0, Block arg1, int arg2)|void
| func_175685_c(BlockPos arg0, Block arg1, boolean arg2)|void
| func_175687_A(BlockPos b)|int
| func_175688_a(EnumParticleTypes arg0, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, int[] arg7)|void
| func_175690_a(BlockPos arg0, TileEntity arg1)|void
| func_175691_a(BlockPos arg0, Block arg1)|boolean
| func_175692_b(int i)|void
| func_175693_T()|MapStorage
| func_175694_M()|BlockPos
| func_175695_a(BlockPos arg0, Block arg1, EnumFacing arg2)|void
| func_175697_a(BlockPos arg0, int arg1)|boolean
| func_175698_g(BlockPos b)|boolean
| func_175699_k(BlockPos b)|int
| func_175700_a(TileEntity t)|boolean
| func_175701_a(BlockPos b)|boolean
| func_175702_c(int i)|void
| func_175704_b(BlockPos arg0, BlockPos arg1)|void
| func_175705_a(EnumSkyBlock arg0, BlockPos arg1)|int
| func_175706_a(BlockPos arg0, BlockPos arg1, boolean arg2)|boolean
| func_175707_a(BlockPos arg0, BlockPos arg1)|boolean
| func_175708_f(BlockPos arg0, boolean arg1)|boolean
| func_175709_b(BlockPos arg0, EnumFacing arg1)|boolean
| func_175710_j(BlockPos b)|boolean
| func_175711_a(StructureBoundingBox s)|boolean
| func_175712_a(StructureBoundingBox arg0, boolean arg1)|List\<NextTickListEntry>
| func_175713_t(BlockPos b)|void
| func_175714_ae()|VillageCollection
| func_175715_c(int arg0, BlockPos arg1, int arg2)|void
| func_175718_b(int arg0, BlockPos arg1, int arg2)|void
| func_175719_a(EntityPlayer arg0, BlockPos arg1, EnumFacing arg2)|boolean
| func_175721_c(BlockPos arg0, boolean arg1)|int
| func_175722_b(BlockPos arg0, Block arg1, boolean arg2)|void
| func_175723_af()|WorldBorder
| func_175724_o(BlockPos b)|float
| func_175725_q(BlockPos b)|BlockPos
| func_175726_f(BlockPos b)|Chunk
| func_175727_C(BlockPos b)|boolean
| func_180494_b(BlockPos b)|Biome
| func_180495_p(BlockPos b)|BlockState
| func_180497_b(BlockPos arg0, Block arg1, int arg2, int arg3)|void
| func_180498_a(EntityPlayer arg0, int arg1, BlockPos arg2, int arg3)|void
| func_180500_c(EnumSkyBlock arg0, BlockPos arg1)|boolean
| func_180501_a(BlockPos arg0, BlockState arg1, int arg2)|boolean
| func_180502_D(BlockPos b)|boolean
| func_180503_b(BlockPos arg0, BlockState arg1)|boolean
| func_181544_b(int i)|void
| func_181545_F()|int
| func_184133_a(EntityPlayer arg0, BlockPos arg1, SoundEvent arg2, SoundCategory arg3, float arg4, float arg5)|void
| func_184134_a(double arg0, double arg1, double arg2, SoundEvent arg3, SoundCategory arg4, float arg5, float arg6, boolean arg7)|void
| func_184135_a(Packet\<?> p)|void
| func_184136_b(Entity arg0, double arg1)|EntityPlayer
| func_184137_a(double arg0, double arg1, double arg2, double arg3, boolean arg4)|EntityPlayer
| func_184138_a(BlockPos arg0, BlockState arg1, BlockState arg2, int arg3)|void
| func_184139_a(BlockPos arg0, double arg1, double arg2)|EntityPlayer
| func_184141_c(BlockPos b)|BlockState
| func_184142_a(Entity arg0, double arg1, double arg2)|EntityPlayer
| func_184143_b(AxisAlignedBB a)|boolean
| func_184144_a(Entity arg0, AxisAlignedBB arg1)|List\<AxisAlignedBB>
| func_184145_b(BlockPos arg0, Block arg1)|boolean
| func_184146_ak()|LootTableManager
| func_184148_a(EntityPlayer arg0, double arg1, double arg2, double arg3, SoundEvent arg4, SoundCategory arg5, float arg6, float arg7)|void
| func_184149_a(BlockPos arg0, SoundEvent arg1)|void
| func_184150_a(double arg0, double arg1, double arg2, double arg3, double arg4, Function\<EntityPlayer, double> arg5, Predicate\<EntityPlayer> arg6)|EntityPlayer
| func_184153_a(int arg0, int arg1, int arg2, int arg3, Random arg4, boolean arg5, BlockPos$MutableBlockPos arg6)|void
| func_184156_a(BlockPos arg0, SoundEvent arg1, SoundCategory arg2, float arg3, float arg4, boolean arg5)|void
| func_189507_a(BlockPos arg0, BlockState arg1, Random arg2)|void
| func_189509_E(BlockPos b)|boolean
| func_189649_b(int arg0, int arg1)|int
| func_190522_c(BlockPos arg0, Block arg1)|void
| func_190523_a(int arg0, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, int[] arg7)|void
| func_190524_a(BlockPos arg0, Block arg1, BlockPos arg2)|void
| func_190525_a(double arg0, double arg1, double arg2, double arg3, Predicate\<Entity> arg4)|EntityPlayer
| func_190526_b(int arg0, int arg1)|boolean
| func_190527_a(Block arg0, BlockPos arg1, boolean arg2, EnumFacing arg3, Entity arg4)|boolean
| func_190528_a(String arg0, BlockPos arg1, boolean arg2)|BlockPos
| func_190529_b(BlockPos arg0, Block arg1, BlockPos arg2)|void
| func_191503_g(Entity e)|boolean
| func_72800_K()|int
| func_72819_i(float f)|float
| func_72820_D()|long
| func_72823_a(String arg0, WorldSavedData arg1)|void
| func_72824_f(float f)|Vec3d
| func_72826_c(float f)|float
| func_72827_u()|String
| func_72829_c(AxisAlignedBB a)|boolean
| func_72833_a(Entity arg0, float arg1)|Vec3d
| func_72835_b()|void
| func_72838_d(Entity e)|boolean
| func_72839_b(Entity arg0, AxisAlignedBB arg1)|List\<Entity>
| func_72841_b(String s)|int
| func_72842_a(Vec3d arg0, AxisAlignedBB arg1)|float
| func_72843_D(int arg0, int arg1, int arg2)|Random
| func_72847_b(Entity e)|void
| func_72848_b(WorldEventListener w)|void
| func_72853_d()|int
| func_72854_c()|void
| func_72855_b(AxisAlignedBB a)|boolean
| func_72857_a(Class\<? extends T> arg0, AxisAlignedBB arg1, Entity arg2)|Entity
| func_72860_G()|SaveHandler
| func_72863_F()|ChunkProvider
| func_72863_F()|ChunkProviderClient
| func_72866_a(Entity arg0, boolean arg1)|void
| func_72867_j(float f)|float
| func_72870_g(Entity e)|void
| func_72872_a(Class\<? extends T> arg0, AxisAlignedBB arg1)|List\<T>
| func_72875_a(AxisAlignedBB arg0, Material arg1)|boolean
| func_72876_a(Entity arg0, double arg1, double arg2, double arg3, float arg4, boolean arg5)|Explosion
| func_72877_b(long l)|void
| func_72880_h(float f)|float
| func_72882_A()|void
| func_72885_a(Entity arg0, double arg1, double arg2, double arg3, float arg4, boolean arg5, boolean arg6)|Explosion
| func_72890_a(Entity arg0, double arg1)|EntityPlayer
| func_72891_a(boolean arg0, boolean arg1)|void
| func_72894_k(float f)|void
| func_72896_J()|boolean
| func_72897_h(Entity e)|void
| func_72900_e(Entity e)|void
| func_72901_a(Vec3d arg0, Vec3d arg1, boolean arg2)|RayTraceResult
| func_72905_C()|long
| func_72906_B()|void
| func_72907_a(Class\<?> c)|int
| func_72910_y()|List\<Entity>
| func_72911_I()|boolean
| func_72912_H()|WorldInfo
| func_72914_a(CrashReport c)|CrashReportCategory
| func_72916_c(int arg0, int arg1)|boolean
| func_72917_a(AxisAlignedBB arg0, Entity arg1)|boolean
| func_72918_a(AxisAlignedBB arg0, Material arg1, Entity arg2)|boolean
| func_72919_O()|double
| func_72920_a(Chunk arg0, boolean arg1)|List\<NextTickListEntry>
| func_72923_a(Entity e)|void
| func_72924_a(String s)|EntityPlayer
| func_72929_e(float f)|float
| func_72933_a(Vec3d arg0, Vec3d arg1)|RayTraceResult
| func_72935_r()|boolean
| func_72939_s()|void
| func_72940_L()|int
| func_72942_c(Entity e)|boolean
| func_72943_a(Class\<? extends net.minecraft.world.storage.WorldSavedData> arg0, String arg1)|WorldSavedData
| func_72948_g(float f)|Vec3d
| func_72953_d(AxisAlignedBB a)|boolean
| func_72954_a(WorldEventListener w)|void
| func_72955_a(boolean b)|boolean
| func_72959_q()|BiomeProvider
| func_72960_a(Entity arg0, byte arg1)|void
| func_72963_a(WorldSettings w)|void
| func_72964_e(int arg0, int arg1)|Chunk
| func_72966_v()|void
| func_72967_a(float f)|int
| func_72971_b(float f)|float
| func_72973_f(Entity e)|void
| func_72974_f()|void
| func_72975_g(int arg0, int arg1, int arg2, int arg3)|void
| func_72981_t()|String
| func_73022_a()|void
| func_73025_a(int arg0, int arg1, boolean arg2)|void
| func_73027_a(int arg0, Entity arg1)|void
| func_73028_b(int i)|Entity
| func_73029_E(int arg0, int arg1, int arg2)|void
| func_73031_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73045_a(int i)|Entity
| func_73046_m()|MinecraftServer
| func_82734_g(int arg0, int arg1)|int
| func_82736_K()|GameRules
| func_82737_E()|long
| func_82738_a(long l)|void
| func_83015_S()|Calendar
| func_92088_a(double arg0, double arg1, double arg2, double arg3, double arg4, double arg5, NBTTagCompound arg6)|void
| func_96441_U()|Scoreboard
| func_96443_a(Scoreboard s)|void
| getBiomeForCoordsBody(BlockPos b)|Biome
| getBlockLightOpacity(BlockPos b)|int
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getCloudColorBody(float f)|Vec3d
| getPersistentChunkIterable(Iterator\<Chunk> i)|Iterator\<Chunk>
| getSkyColorBody(Entity arg0, float arg1)|Vec3d
| getStarBrightnessBody(float f)|float
| getSunBrightnessBody(float f)|float
| getSunBrightnessFactor(float f)|float
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isSideSolid(BlockPos arg0, EnumFacing arg1, boolean arg2)|boolean
| isSideSolid(BlockPos arg0, EnumFacing arg1)|boolean
| markAndNotifyBlock(BlockPos arg0, Chunk arg1, BlockState arg2, BlockState arg3, int arg4)|void
| markTileEntitiesInChunkForRemoval(Chunk c)|void
| updateWeatherBody()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PlayerControllerMP

|Class
|--
|net.minecraft.client.multiplayer.PlayerControllerMP

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_178895_c|BlockPos
|  field_78770_f|float
|  field_78778_j|boolean
|  field_85183_f|ItemStack

---

|Methods|Return Type
|--|--
| func_110738_j()|boolean
| func_178887_k()|boolean
| func_178889_l()|GameType
| func_180511_b(BlockPos arg0, EnumFacing arg1)|boolean
| func_180512_c(BlockPos arg0, EnumFacing arg1)|boolean
| func_181040_m()|boolean
| func_187097_a(EntityPlayer arg0, Entity arg1, EnumHand arg2)|EnumActionResult
| func_187098_a(int arg0, int arg1, int arg2, ClickType arg3, EntityPlayer arg4)|ItemStack
| func_187099_a(EntityPlayerSP arg0, WorldClient arg1, BlockPos arg2, EnumFacing arg3, Vec3d arg4, EnumHand arg5)|EnumActionResult
| func_187100_a(int i)|void
| func_187101_a(EntityPlayer arg0, World arg1, EnumHand arg2)|EnumActionResult
| func_187102_a(EntityPlayer arg0, Entity arg1, RayTraceResult arg2, EnumHand arg3)|EnumActionResult
| func_187103_a(BlockPos b)|boolean
| func_192830_a(World arg0, StatisticsManager arg1, RecipeBook arg2)|EntityPlayerSP
| func_194338_a(int arg0, Recipe arg1, boolean arg2, EntityPlayer arg3)|void
| func_78745_b(EntityPlayer e)|void
| func_78746_a(GameType g)|void
| func_78747_a()|boolean
| func_78748_a(EntityPlayer e)|void
| func_78749_i()|boolean
| func_78752_a(ItemStack i)|void
| func_78755_b()|boolean
| func_78756_a(int arg0, int arg1)|void
| func_78757_d()|float
| func_78758_h()|boolean
| func_78761_a(ItemStack arg0, int arg1)|void
| func_78762_g()|boolean
| func_78763_f()|boolean
| func_78764_a(EntityPlayer arg0, Entity arg1)|void
| func_78765_e()|void
| func_78766_c(EntityPlayer e)|void
| func_78767_c()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TextureManager

|Class
|--
|net.minecraft.client.renderer.texture.TextureManager

---

|Extends
|--
|Tickable
|ResourceManagerReloadListener

---

|Fields|Type
|--|--
|  field_110585_a|Map\<ResourceLocation, TextureObject>

---

|Methods|Return Type
|--|--
| func_110549_a(ResourceManager r)|void
| func_110550_d()|void
| func_110577_a(ResourceLocation r)|void
| func_110578_a(String arg0, DynamicTexture arg1)|ResourceLocation
| func_110579_a(ResourceLocation arg0, TextureObject arg1)|boolean
| func_110580_a(ResourceLocation arg0, TickableTextureObject arg1)|boolean
| func_110581_b(ResourceLocation r)|TextureObject
| func_147645_c(ResourceLocation r)|void
| reloadBannerTextures()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GuiIngame

|Class
|--
|net.minecraft.client.gui.GuiIngame

---

|Extends
|--
|Gui

---

|Fields|Type
|--|--
|  field_191743_I|Map\<ChatType, java.util.List\<net.minecraft.client.gui.chat.IChatListener>>
|  field_73735_i|float
|  field_73843_a|float
|  field_92017_k|int

---

|Methods|Return Type
|--|--
| func_110326_a(String arg0, boolean arg1)|void
| func_146158_b()|GuiNewChat
| func_175174_a(float arg0, float arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_175175_a(int arg0, int arg1, TextureAtlasSprite arg2, int arg3, int arg4)|void
| func_175176_b(ScaledResolution arg0, int arg1)|void
| func_175177_a()|void
| func_175178_a(String arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_175179_f()|FontRenderer
| func_175180_a(float f)|void
| func_175181_h()|GuiPlayerTabOverlay
| func_175185_b(ScaledResolution s)|void
| func_175186_a(ScaledResolution arg0, int arg1)|void
| func_175187_g()|GuiSpectator
| func_175188_a(TextComponent arg0, boolean arg1)|void
| func_181029_i()|void
| func_181551_a(ScaledResolution s)|void
| func_184046_j()|GuiBossOverlay
| func_191742_a(ChatType arg0, TextComponent arg1)|void
| func_73729_b(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73731_b(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73732_a(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73733_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73831_a()|void
| func_73833_a(String s)|void
| func_73834_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityRenderer

|Class
|--
|net.minecraft.client.renderer.EntityRenderer

---

|Extends
|--
|ResourceManagerReloadListener

---

|Fields|Type
|--|--
|  avgServerTickDiff|float
|  avgServerTimeDiff|float
|  clipDistance|float
|  field_110922_T|ResourceLocation
|  field_147707_d|ShaderGroup
|  field_147709_v|MapItemRenderer
|  field_147711_ac|ResourceManager
|  field_147713_ae|int
|  field_175073_D|boolean
|  field_175074_C|boolean
|  field_175075_L|float
|  field_175076_N|float[]
|  field_175077_O|float[]
|  field_175078_W|boolean
|  field_175079_V|int
|  field_175080_Q|float
|  field_175081_S|float
|  field_175082_R|float
|  field_175083_ad|boolean
|  field_175084_ae|int
|  field_184374_E|long
|  field_190566_ab|ItemStack
|  field_190567_ac|int
|  field_190568_ad|float
|  field_190569_ae|float
|  field_78490_B|float
|  field_78491_C|float
|  field_78492_L|float
|  field_78496_H|float
|  field_78497_I|float
|  field_78498_J|float
|  field_78499_K|float
|  field_78500_U|boolean
|  field_78502_W|double
|  field_78503_V|double
|  field_78504_Q|int[]
|  field_78506_S|float
|  field_78507_R|float
|  field_78508_Y|long
|  field_78509_X|double
|  field_78510_Z|long
|  field_78513_d|DynamicTexture
|  field_78514_e|float
|  field_78516_c|ItemRenderer
|  field_78521_m|FloatBuffer
|  field_78526_w|MouseFilter
|  field_78527_v|MouseFilter
|  field_78528_u|Entity
|  field_78529_t|int
|  field_78530_s|float
|  field_78531_r|Minecraft
|  field_78534_ac|int
|  field_78535_ad|float
|  field_78536_aa|boolean
|  field_78537_ab|Random
|  field_78539_ae|float
|  field_82831_U|float
|  field_82832_V|float
|  fogStandard|boolean
|  fxaaShaders|ShaderGroup[]
|  initialized|boolean
|  lastServerTicks|int
|  lastServerTime|long
|  loadVisibleChunks|boolean
|  serverWaitTime|int
|  serverWaitTimeCurrent|int
|  updatedWorld|World

---

|Methods|Return Type
|--|--
| checkLoadVisibleChunks(Entity arg0, float arg1, Camera arg2, boolean arg3)|void
| frameFinish()|void
| frameInit()|void
| func_110549_a(ResourceManager r)|void
| func_147701_i()|MapItemRenderer
| func_147702_a()|boolean
| func_147704_a(int arg0, int arg1)|void
| func_147706_e()|ShaderGroup
| func_152430_c(float f)|void
| func_175066_a(Entity e)|void
| func_175068_a(int arg0, float arg1, long arg2)|void
| func_175069_a(ResourceLocation r)|void
| func_175070_n()|boolean
| func_175071_c()|void
| func_175072_h()|void
| func_180436_i()|void
| func_180437_a(RenderGlobal arg0, float arg1, int arg2, double arg3, double arg4, double arg5)|void
| func_180438_a(EntityLivingBase arg0, float arg1)|float
| func_181022_b()|void
| func_181560_a(float arg0, long arg1)|void
| func_184373_n()|void
| func_190563_a(int arg0, int arg1, float arg2)|void
| func_190564_k()|void
| func_190565_a(ItemStack i)|void
| func_191514_d(boolean b)|void
| func_78464_a()|void
| func_78466_h(float f)|void
| func_78467_g(float f)|void
| func_78468_a(int arg0, float arg1)|void
| func_78469_a(float arg0, float arg1, float arg2, float arg3)|FloatBuffer
| func_78470_f()|void
| func_78471_a(float arg0, long arg1)|void
| func_78472_g(float f)|void
| func_78473_a(float f)|void
| func_78474_d(float f)|void
| func_78475_f(float f)|void
| func_78476_b(float arg0, int arg1)|void
| func_78477_e()|void
| func_78478_c()|void
| func_78479_a(float arg0, int arg1)|void
| func_78481_a(float arg0, boolean arg1)|float
| func_78482_e(float f)|void
| func_78484_h()|void
| loadAllVisibleChunks(Entity arg0, double arg1, Camera arg2, boolean arg3)|void
| renderHand(float arg0, int arg1, boolean arg2, boolean arg3, boolean arg4)|void
| setFxaaShader(int i)|boolean
| updateMainMenu(GuiMainMenu g)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void
| waitForServerThread()|void

---

## LoadingScreenRenderer

|Class
|--
|net.minecraft.client.LoadingScreenRenderer

---

|Extends
|--
|ProgressUpdate

---

|Methods|Return Type
|--|--
| func_146586_a()|void
| func_73718_a(int i)|void
| func_73719_c(String s)|void
| func_73720_a(String s)|void
| func_73721_b(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GameSettings

|Class
|--
|net.minecraft.client.settings.GameSettings

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_151442_I|int
|  field_151444_V|KeyBinding
|  field_151445_Q|KeyBinding
|  field_151447_Z|KeyBinding
|  field_151448_g|boolean
|  field_151451_c|int
|  field_151452_as|float
|  field_151453_l|List\<String>
|  field_151455_aw|boolean
|  field_151456_ac|KeyBinding[]
|  field_151457_aa|KeyBinding
|  field_151458_ab|KeyBinding
|  field_152395_am|KeyBinding
|  field_178879_v|boolean
|  field_178881_t|boolean
|  field_178883_an|KeyBinding
|  field_181150_U|boolean
|  field_181151_V|boolean
|  field_181657_aC|boolean
|  field_183018_l|List\<String>
|  field_183509_X|boolean
|  field_186715_A|EnumHandSide
|  field_186716_M|int
|  field_186717_N|boolean
|  field_186718_X|KeyBinding
|  field_189422_N|boolean
|  field_189989_R|boolean
|  field_192571_R|int
|  field_193629_ap|KeyBinding
|  field_193630_aq|KeyBinding
|  field_193631_S|TutorialSteps
|  field_194146_ao|KeyBinding
|  field_74310_D|KeyBinding
|  field_74311_E|KeyBinding
|  field_74312_F|KeyBinding
|  field_74313_G|KeyBinding
|  field_74314_A|KeyBinding
|  field_74316_C|KeyBinding
|  field_74318_M|EnumDifficulty
|  field_74319_N|boolean
|  field_74320_O|int
|  field_74321_H|KeyBinding
|  field_74322_I|KeyBinding
|  field_74323_J|KeyBinding
|  field_74324_K|KeyBinding[]
|  field_74325_U|boolean
|  field_74326_T|boolean
|  field_74329_Q|boolean
|  field_74330_P|boolean
|  field_74332_R|String
|  field_74333_Y|float
|  field_74334_X|float
|  field_74335_Z|int
|  field_74336_f|boolean
|  field_74337_g|boolean
|  field_74338_d|boolean
|  field_74341_c|float
|  field_74343_n|EntityPlayer$EnumChatVisibility
|  field_74344_o|boolean
|  field_74345_l|int
|  field_74347_j|boolean
|  field_74348_k|int
|  field_74350_i|int
|  field_74351_w|KeyBinding
|  field_74352_v|boolean
|  field_74353_u|boolean
|  field_74355_t|boolean
|  field_74357_r|float
|  field_74358_q|boolean
|  field_74359_p|boolean
|  field_74362_aa|int
|  field_74363_ab|String
|  field_74366_z|KeyBinding
|  field_74368_y|KeyBinding
|  field_74370_x|KeyBinding
|  field_80005_w|boolean
|  field_82881_y|boolean
|  field_82882_x|boolean
|  field_85185_A|boolean
|  field_92117_D|boolean
|  field_92118_B|int
|  field_92119_C|int
|  field_96691_E|float
|  field_96692_F|float
|  field_96693_G|float
|  field_96694_H|float
|  ofAaLevel|int
|  ofAfLevel|int
|  ofAlternateBlocks|boolean
|  ofAnimatedExplosion|boolean
|  ofAnimatedFire|boolean
|  ofAnimatedFlame|boolean
|  ofAnimatedLava|int
|  ofAnimatedPortal|boolean
|  ofAnimatedRedstone|boolean
|  ofAnimatedSmoke|boolean
|  ofAnimatedTerrain|boolean
|  ofAnimatedTextures|boolean
|  ofAnimatedWater|int
|  ofAoLevel|float
|  ofAutoSaveTicks|int
|  ofBetterGrass|int
|  ofBetterSnow|boolean
|  ofChunkUpdates|int
|  ofChunkUpdatesDynamic|boolean
|  ofClearWater|boolean
|  ofClouds|int
|  ofCloudsHeight|float
|  ofConnectedTextures|int
|  ofCustomColors|boolean
|  ofCustomEntityModels|boolean
|  ofCustomFonts|boolean
|  ofCustomGuis|boolean
|  ofCustomItems|boolean
|  ofCustomSky|boolean
|  ofDrippingWaterLava|boolean
|  ofDroppedItems|int
|  ofDynamicFov|boolean
|  ofDynamicLights|int
|  ofEmissiveTextures|boolean
|  ofFastMath|boolean
|  ofFastRender|boolean
|  ofFireworkParticles|boolean
|  ofFogStart|float
|  ofFogType|int
|  ofFullscreenMode|String
|  ofKeyBindZoom|KeyBinding
|  ofLagometer|boolean
|  ofLazyChunkLoading|boolean
|  ofMipmapType|int
|  ofNaturalTextures|boolean
|  ofOcclusionFancy|boolean
|  ofPortalParticles|boolean
|  ofPotionParticles|boolean
|  ofProfiler|boolean
|  ofRain|int
|  ofRainSplash|boolean
|  ofRandomEntities|boolean
|  ofRenderRegions|boolean
|  ofScreenshotSize|int
|  ofShowCapes|boolean
|  ofShowFps|boolean
|  ofShowGlErrors|boolean
|  ofSky|boolean
|  ofSmartAnimations|boolean
|  ofSmoothBiomes|boolean
|  ofSmoothFps|boolean
|  ofSmoothWorld|boolean
|  ofStars|boolean
|  ofSunMoon|boolean
|  ofSwampColors|boolean
|  ofTime|int
|  ofTranslucentBlocks|int
|  ofTrees|int
|  ofVignette|int
|  ofVoidParticles|boolean
|  ofWaterParticles|boolean
|  ofWeather|boolean

---

|Methods|Return Type
|--|--
| func_151440_a(KeyBinding arg0, int arg1)|void
| func_178876_d()|Set\<EnumPlayerModelParts>
| func_178877_a(EnumPlayerModelParts e)|void
| func_178878_a(EnumPlayerModelParts arg0, boolean arg1)|void
| func_181147_e()|int
| func_181148_f()|boolean
| func_186711_a(SoundCategory s)|float
| func_186712_a(SoundCategory arg0, float arg1)|void
| func_74296_a(GameSettings$Options g)|float
| func_74297_c(GameSettings$Options g)|String
| func_74300_a()|void
| func_74303_b()|void
| func_74304_a(GameSettings$Options arg0, float arg1)|void
| func_74306_a(GameSettings$Options arg0, int arg1)|void
| func_74308_b(GameSettings$Options g)|boolean
| func_82879_c()|void
| loadOfOptions()|void
| onGuiClosed()|void
| resetSettings()|void
| saveOfOptions()|void
| setAllAnimations(boolean b)|void
| updateVSync()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemColors

|Class
|--
|net.minecraft.client.renderer.color.ItemColors

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_186728_a(ItemStack arg0, int arg1)|int
| func_186730_a(ItemColor arg0, Item[] arg1)|void
| func_186731_a(ItemColor arg0, Block[] arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SearchTreeManager

|Class
|--
|net.minecraft.client.util.SearchTreeManager

---

|Extends
|--
|ResourceManagerReloadListener

---

|Methods|Return Type
|--|--
| func_110549_a(ResourceManager r)|void
| func_194009_a(SearchTreeManager$Key\<T> arg0, SearchTree\<T> arg1)|void
| func_194010_a(SearchTreeManager$Key\<T> s)|SearchTree\<T>
| onResourceManagerReload_foamfix_old(ResourceManager r)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Session

|Class
|--
|net.minecraft.util.Session

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_111285_a()|String
| func_111286_b()|String
| func_148254_d()|String
| func_148255_b()|String
| func_148256_e()|GameProfile
| hasCachedProperties()|boolean
| setProperties(PropertyMap p)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ResourcePackRepository

|Class
|--
|net.minecraft.client.resources.ResourcePackRepository

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_110617_f|List\<ResourcePackRepository$Entry>
|  field_110620_b|ResourcePack
|  field_110621_c|MetadataSerializer

---

|Methods|Return Type
|--|--
| func_110609_b()|List\<ResourcePackRepository$Entry>
| func_110611_a()|void
| func_110612_e()|File
| func_110613_c()|List\<ResourcePackRepository$Entry>
| func_148527_a(List\<ResourcePackRepository$Entry> l)|void
| func_148529_f()|void
| func_148530_e()|ResourcePack
| func_177319_a(File f)|ListenableFuture\<Object>
| func_180601_a(String arg0, String arg1)|ListenableFuture\<Object>
| func_188565_b()|ResourcePackRepository$Entry
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ResourceManager

|Interface
|--
|net.minecraft.client.resources.IResourceManager

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_110536_a(ResourceLocation r)|Resource
| func_135055_a()|Set\<String>
| func_135056_b(ResourceLocation r)|List\<Resource>

---

## LanguageManager

|Class
|--
|net.minecraft.client.resources.LanguageManager

---

|Extends
|--
|ResourceManagerReloadListener

---

|Fields|Type
|--|--
|  field_135048_c|String

---

|Methods|Return Type
|--|--
| func_110549_a(ResourceManager r)|void
| func_135040_d()|SortedSet\<Language>
| func_135041_c()|Language
| func_135042_a()|boolean
| func_135043_a(List\<ResourcePack> l)|void
| func_135044_b()|boolean
| func_135045_a(Language l)|void
| func_191960_a(String s)|Language
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ServerData

|Class
|--
|net.minecraft.client.multiplayer.ServerData

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_147412_i|String
|  field_78841_f|boolean
|  field_78843_d|String
|  field_78844_e|long
|  field_78845_b|String
|  field_78846_c|String
|  field_78847_a|String
|  field_82821_f|int
|  field_82822_g|String

---

|Methods|Return Type
|--|--
| func_147407_a(String s)|void
| func_147409_e()|String
| func_152583_a(ServerData s)|void
| func_152584_a(ServerData$ServerResourceMode s)|void
| func_152586_b()|ServerData$ServerResourceMode
| func_181041_d()|boolean
| func_78836_a()|NBTTagCompound
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MusicTicker$MusicType

|Class
|--
|net.minecraft.client.audio.MusicTicker$MusicType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_148633_c()|int
| func_148634_b()|int
| func_188768_a()|SoundEvent
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Framebuffer

|Class
|--
|net.minecraft.client.shader.Framebuffer

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_147616_f|int
|  field_147617_g|int
|  field_147618_d|int
|  field_147619_e|boolean
|  field_147620_b|int
|  field_147621_c|int
|  field_147622_a|int
|  field_147623_j|int
|  field_147624_h|int
|  field_147625_i|float[]
|  stencilEnabled|boolean

---

|Methods|Return Type
|--|--
| enableStencil()|boolean
| func_147604_a(float arg0, float arg1, float arg2, float arg3)|void
| func_147605_b(int arg0, int arg1)|void
| func_147606_d()|void
| func_147607_a(int i)|void
| func_147608_a()|void
| func_147609_e()|void
| func_147610_a(boolean b)|void
| func_147611_b()|void
| func_147612_c()|void
| func_147613_a(int arg0, int arg1)|void
| func_147614_f()|void
| func_147615_c(int arg0, int arg1)|void
| func_178038_a(int arg0, int arg1, boolean arg2)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NetHandlerPlayClient

|Class
|--
|net.minecraft.client.network.NetHandlerPlayClient

---

|Extends
|--
|NetHandlerPlayClient

---

|Fields|Type
|--|--
|  field_147304_c|int
|  field_147310_i|Map\<UUID, NetworkPlayerInfo>

---

|Methods|Return Type
|--|--
| func_147231_a(TextComponent t)|void
| func_147234_a(SPacketBlockChange s)|void
| func_147235_a(SPacketSpawnObject s)|void
| func_147236_a(SPacketEntityStatus s)|void
| func_147237_a(SPacketSpawnPlayer s)|void
| func_147238_a(SPacketDestroyEntities s)|void
| func_147239_a(SPacketConfirmTransaction s)|void
| func_147240_a(SPacketCustomPayload s)|void
| func_147241_a(SPacketWindowItems s)|void
| func_147242_a(SPacketEntityEquipment s)|void
| func_147243_a(SPacketEntityAttach s)|void
| func_147244_a(SPacketEntityVelocity s)|void
| func_147245_a(SPacketWindowProperty s)|void
| func_147246_a(SPacketCollectItem s)|void
| func_147247_a(SPacketTeams s)|void
| func_147249_a(SPacketUpdateHealth s)|void
| func_147250_a(SPacketUpdateScore s)|void
| func_147251_a(SPacketChat s)|void
| func_147252_a(SPacketChangeGameState s)|void
| func_147253_a(SPacketDisconnect s)|void
| func_147254_a(SPacketDisplayObjective s)|void
| func_147256_a(SPacketPlayerListItem s)|void
| func_147257_a(SPacketHeldItemChange s)|void
| func_147259_a(SPacketEntity s)|void
| func_147260_a(SPacketEntityEffect s)|void
| func_147261_a(SPacketBlockAction s)|void
| func_147262_a(SPacketRemoveEntityEffect s)|void
| func_147263_a(SPacketChunkData s)|void
| func_147264_a(SPacketMaps s)|void
| func_147265_a(SPacketOpenWindow s)|void
| func_147266_a(SPacketSetSlot s)|void
| func_147267_a(SPacketEntityHeadLook s)|void
| func_147268_a(SPacketSignEditorOpen s)|void
| func_147270_a(SPacketPlayerAbilities s)|void
| func_147271_a(SPacketSpawnPosition s)|void
| func_147272_a(SPacketKeepAlive s)|void
| func_147273_a(SPacketUpdateTileEntity s)|void
| func_147274_a(SPacketTabComplete s)|void
| func_147275_a(SPacketEntityTeleport s)|void
| func_147276_a(SPacketCloseWindow s)|void
| func_147277_a(SPacketEffect s)|void
| func_147278_a(SPacketUseBed s)|void
| func_147279_a(SPacketAnimation s)|void
| func_147280_a(SPacketRespawn s)|void
| func_147281_a(SPacketSpawnMob s)|void
| func_147282_a(SPacketJoinGame s)|void
| func_147283_a(SPacketExplosion s)|void
| func_147284_a(SPacketEntityMetadata s)|void
| func_147285_a(SPacketTimeUpdate s)|void
| func_147286_a(SPacketSpawnExperienceOrb s)|void
| func_147287_a(SPacketMultiBlockChange s)|void
| func_147288_a(SPacketSpawnPainting s)|void
| func_147289_a(SPacketParticles s)|void
| func_147290_a(SPacketEntityProperties s)|void
| func_147291_a(SPacketScoreboardObjective s)|void
| func_147292_a(SPacketSpawnGlobalEntity s)|void
| func_147293_a(SPacketStatistics s)|void
| func_147294_a(SPacketBlockBreakAnim s)|void
| func_147295_a(SPacketSetExperience s)|void
| func_147296_c()|void
| func_147297_a(Packet\<?> p)|void
| func_147298_b()|NetworkManager
| func_175093_a(SPacketWorldBorder s)|void
| func_175094_a(SPacketCamera s)|void
| func_175095_a(SPacketResourcePackSend s)|void
| func_175096_a(SPacketPlayerListHeaderFooter s)|void
| func_175098_a(SPacketCombatEvent s)|void
| func_175099_a(SPacketTitle s)|void
| func_175101_a(SPacketServerDifficulty s)|void
| func_175102_a(UUID u)|NetworkPlayerInfo
| func_175104_a(String s)|NetworkPlayerInfo
| func_175105_e()|GameProfile
| func_175106_d()|Collection\<NetworkPlayerInfo>
| func_184323_a(SPacketMoveVehicle s)|void
| func_184324_a(SPacketCooldown s)|void
| func_184325_a(SPacketUpdateBossInfo s)|void
| func_184326_a(SPacketUnloadChunk s)|void
| func_184327_a(SPacketSoundEffect s)|void
| func_184328_a(SPacketSetPassengers s)|void
| func_184329_a(SPacketCustomSound s)|void
| func_184330_a(SPacketPlayerPosLook s)|void
| func_191980_a(SPacketRecipeBook s)|void
| func_191981_a(SPacketAdvancementInfo s)|void
| func_191982_f()|ClientAdvancementManager
| func_194022_a(SPacketSelectAdvancementsTab s)|void
| func_194307_a(SPacketPlaceGhostRecipe s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TextureMap

|Class
|--
|net.minecraft.client.renderer.texture.TextureMap

---

|Extends
|--
|AbstractTexture
|TickableTextureObject

---

|Fields|Type
|--|--
|  atlasHeight|int
|  atlasWidth|int
|  basePath|String
|  countAnimations|int
|  countAnimationsActive|int
|  countRegisteredSprites|int
|  field_110574_e|Map\<String, TextureAtlasSprite>
|  field_94252_e|Map\<String, TextureAtlasSprite>
|  mipmapLevels|int
|  multiTex|MultiTexID
|  multiTexID|MultiTexID
|  textureBound|boolean

---

|Methods|Return Type
|--|--
| completeResourceLocation(ResourceLocation r)|ResourceLocation
| func_110550_d()|void
| func_110551_a(ResourceManager r)|void
| func_110552_b()|int
| func_110571_b(ResourceManager r)|void
| func_110572_b(String s)|TextureAtlasSprite
| func_147631_c()|void
| func_147633_a(int i)|void
| func_174935_a()|void
| func_174936_b(boolean arg0, boolean arg1)|void
| func_174937_a(boolean arg0, boolean arg1)|void
| func_174942_a(ResourceLocation r)|TextureAtlasSprite
| func_174943_a(ResourceManager arg0, TextureMapPopulator arg1)|void
| func_174944_f()|TextureAtlasSprite
| func_184396_a(TextureAtlasSprite t)|ResourceLocation
| func_184397_a(ResourceManager arg0, TextureAtlasSprite arg1)|boolean
| func_94248_c()|void
| getIconByUV(double arg0, double arg1)|TextureAtlasSprite
| getRegisteredSprite(ResourceLocation r)|TextureAtlasSprite
| getSpriteSafe(String s)|TextureAtlasSprite
| getTextureExtry(String s)|TextureAtlasSprite
| setTextureEntry(TextureAtlasSprite t)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SoundHandler

|Class
|--
|net.minecraft.client.audio.SoundHandler

---

|Extends
|--
|ResourceManagerReloadListener
|Tickable

---

|Fields|Type
|--|--
|  field_147694_f|SoundManager

---

|Methods|Return Type
|--|--
| func_110549_a(ResourceManager r)|void
| func_147681_a(Sound arg0, int arg1)|void
| func_147682_a(Sound s)|void
| func_147683_b(Sound s)|void
| func_147685_d()|void
| func_147687_e()|void
| func_147689_b()|void
| func_147690_c()|void
| func_147691_a(EntityPlayer arg0, float arg1)|void
| func_147692_c(Sound s)|boolean
| func_184398_a(ResourceLocation r)|SoundEventAccessor
| func_184399_a(SoundCategory arg0, float arg1)|void
| func_184400_b(SoundEventListener s)|void
| func_184402_a(SoundEventListener s)|void
| func_189520_a(String arg0, SoundCategory arg1)|void
| func_73660_a()|void
| setListener(Entity arg0, float arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SkinManager

|Class
|--
|net.minecraft.client.resources.SkinManager

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_152788_a(GameProfile g)|Map\<MinecraftProfileTexture$Type, MinecraftProfileTexture>
| func_152789_a(MinecraftProfileTexture arg0, MinecraftProfileTexture$Type arg1, SkinManager$SkinAvailableCallback arg2)|ResourceLocation
| func_152790_a(GameProfile arg0, SkinManager$SkinAvailableCallback arg1, boolean arg2)|void
| func_152792_a(MinecraftProfileTexture arg0, MinecraftProfileTexture$Type arg1)|ResourceLocation
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MinecraftSessionService

|Interface
|--
|com.mojang.authlib.minecraft.MinecraftSessionService

---

|Extends
|--

---

|Methods|Return Type
|--|--
| fillProfileProperties(GameProfile arg0, boolean arg1)|GameProfile
| getTextures(GameProfile arg0, boolean arg1)|Map\<MinecraftProfileTexture$Type, MinecraftProfileTexture>
| hasJoinedServer(GameProfile arg0, String arg1, InetAddress arg2)|GameProfile
| joinServer(GameProfile arg0, String arg1, String arg2)|void

---

## ItemRenderer

|Class
|--
|net.minecraft.client.renderer.ItemRenderer

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_178111_g|RenderManager
|  field_178112_h|RenderItem
|  field_187467_d|ItemStack
|  field_187468_e|ItemStack
|  field_187469_f|float
|  field_187470_g|float
|  field_187471_h|float
|  field_187472_i|float
|  field_78455_a|Minecraft

---

|Methods|Return Type
|--|--
| func_178099_a(EntityLivingBase arg0, ItemStack arg1, ItemCameraTransforms$TransformType arg2)|void
| func_178100_c(float f)|float
| func_178101_a(float arg0, float arg1)|void
| func_178108_a(TextureAtlasSprite t)|void
| func_187453_a(EnumHandSide arg0, float arg1)|void
| func_187454_a(float arg0, EnumHandSide arg1, ItemStack arg2)|void
| func_187455_a(EnumHandSide e)|void
| func_187456_a(float arg0, float arg1, EnumHandSide arg2)|void
| func_187457_a(AbstractClientPlayer arg0, float arg1, float arg2, EnumHand arg3, float arg4, ItemStack arg5, float arg6)|void
| func_187458_c(float f)|void
| func_187459_b(EnumHandSide arg0, float arg1)|void
| func_187460_a(EnumHand e)|void
| func_187461_a(ItemStack i)|void
| func_187462_a(EntityLivingBase arg0, ItemStack arg1, ItemCameraTransforms$TransformType arg2, boolean arg3)|void
| func_187463_a(float arg0, float arg1, float arg2)|void
| func_187464_b()|void
| func_187465_a(float arg0, EnumHandSide arg1, float arg2, ItemStack arg3)|void
| func_187466_c()|void
| func_78440_a(float f)|void
| func_78441_a()|void
| func_78442_d()|void
| func_78447_b(float f)|void
| func_78448_c(float f)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RenderManager

|Class
|--
|net.minecraft.client.renderer.entity.RenderManager

---

|Extends
|--

---

|Fields|Type
|--|--
|  entityRenderMap|Map\<Class, Render>
|  field_147941_i|Entity
|  field_178636_l|Map\<String, RenderPlayer>
|  field_178637_m|RenderPlayer
|  field_78722_g|World
|  field_78723_d|double
|  field_78724_e|TextureManager
|  field_78725_b|double
|  field_78726_c|double
|  field_78728_n|double
|  field_78729_o|Map\<java.lang.Class\<? extends net.minecraft.entity.Entity>, net.minecraft.client.renderer.entity.Render\<? extends net.minecraft.entity.Entity>>
|  field_78730_l|double
|  field_78731_m|double
|  field_78732_j|float
|  field_78733_k|GameSettings
|  field_78734_h|Entity
|  field_78735_i|float
|  renderRender|Render
|  skinMap|Map\<String, RenderPlayer>

---

|Methods|Return Type
|--|--
| func_178627_a()|boolean
| func_178628_a(double arg0, double arg1, double arg2)|void
| func_178629_b(boolean b)|void
| func_178631_a(float f)|void
| func_178632_c(boolean b)|void
| func_178633_a(boolean b)|void
| func_178634_b()|boolean
| func_178635_a(Entity arg0, Camera arg1, double arg2, double arg3, double arg4)|boolean
| func_180597_a(World arg0, FontRenderer arg1, Entity arg2, Entity arg3, GameSettings arg4, float arg5)|void
| func_188388_a(Entity arg0, float arg1, boolean arg2)|void
| func_188389_a(Entity arg0, float arg1)|void
| func_188390_b(Entity e)|boolean
| func_188391_a(Entity arg0, double arg1, double arg2, double arg3, float arg4, float arg5, boolean arg6)|void
| func_78713_a(Entity e)|Render\<T>
| func_78714_a(double arg0, double arg1, double arg2)|double
| func_78715_a(Class\<? extends net.minecraft.entity.Entity> c)|Render\<T>
| func_78716_a()|FontRenderer
| func_78717_a(World w)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RenderItem

|Class
|--
|net.minecraft.client.renderer.RenderItem

---

|Extends
|--
|ResourceManagerReloadListener

---

|Fields|Type
|--|--
|  field_175057_n|TextureManager
|  field_175059_m|ItemModelMesher
|  field_184395_f|ItemColors
|  field_77023_b|float
|  modelManager|ModelManager

---

|Methods|Return Type
|--|--
| func_110549_a(ResourceManager r)|void
| func_175030_a(FontRenderer arg0, ItemStack arg1, int arg2, int arg3)|void
| func_175037_a()|ItemModelMesher
| func_175041_b()|void
| func_175042_a(ItemStack arg0, int arg1, int arg2)|void
| func_175048_a(Item arg0, int arg1, String arg2)|void
| func_175050_a(ItemStack i)|boolean
| func_180450_b(ItemStack arg0, int arg1, int arg2)|void
| func_180452_a(int arg0, int arg1, boolean arg2)|void
| func_180453_a(FontRenderer arg0, ItemStack arg1, int arg2, int arg3, String arg4)|void
| func_180454_a(ItemStack arg0, BakedModel arg1)|void
| func_181564_a(ItemStack arg0, ItemCameraTransforms$TransformType arg1)|void
| func_181565_a(BufferBuilder arg0, int arg1, int arg2, int arg3, int arg4, int arg5, int arg6, int arg7, int arg8)|void
| func_184391_a(EntityLivingBase arg0, ItemStack arg1, int arg2, int arg3)|void
| func_184392_a(ItemStack arg0, EntityLivingBase arg1, ItemCameraTransforms$TransformType arg2, boolean arg3)|void
| func_184393_a(ItemStack arg0, World arg1, EntityLivingBase arg2)|BakedModel
| func_184394_a(ItemStack arg0, BakedModel arg1, ItemCameraTransforms$TransformType arg2, boolean arg3)|void
| func_191961_a(BakedModel arg0, ItemStack arg1)|void
| func_191962_a(ItemStack arg0, int arg1, int arg2, BakedModel arg3)|void
| func_191965_a(BakedModel arg0, int arg1)|void
| func_191970_a(BufferBuilder arg0, List\<BakedQuad> arg1, int arg2, ItemStack arg3)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PropertyMap

|Class
|--
|com.mojang.authlib.properties.PropertyMap

---

|Extends
|--
|ForwardingMultimap

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| asMap()|Map\<K, java.util.Collection\<V>>
| clear()|void
| containsEntry(Object arg0, Object arg1)|boolean
| containsKey(Object o)|boolean
| containsValue(Object o)|boolean
| entries()|Collection\<java.util.Map$Entry\<K, V>>
| forEach(BiConsumer\<? super K, ? super V> b)|void
| get(Object o)|Collection\<V>
| keys()|Multiset\<K>
| keySet()|Set\<K>
| put(Object arg0, Object arg1)|boolean
| putAll(Object arg0, Iterable\<? extends V> arg1)|boolean
| putAll(Multimap\<? extends K, ? extends V> m)|boolean
| remove(Object arg0, Object arg1)|boolean
| removeAll(Object o)|Collection\<V>
| replaceValues(Object arg0, Iterable\<? extends V> arg1)|Collection\<V>
| size()|int
| values()|Collection\<V>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MusicTicker

|Class
|--
|net.minecraft.client.audio.MusicTicker

---

|Extends
|--
|Tickable

---

|Fields|Type
|--|--
|  field_147676_d|int
|  field_147678_c|Sound

---

|Methods|Return Type
|--|--
| func_181558_a(MusicTicker$MusicType m)|void
| func_73660_a()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockColors

|Class
|--
|net.minecraft.client.renderer.color.BlockColors

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_186722_a(BlockColor arg0, Block[] arg1)|void
| func_186724_a(BlockState arg0, BlockAccess arg1, BlockPos arg2, int arg3)|int
| func_189991_a(BlockState arg0, World arg1, BlockPos arg2)|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## DataFixer

|Class
|--
|net.minecraft.util.datafix.DataFixer

---

|Extends
|--
|DataFixer

---

|Fields|Type
|--|--
|  field_188262_d|int

---

|Methods|Return Type
|--|--
| func_188251_a(FixType arg0, NBTTagCompound arg1, int arg2)|NBTTagCompound
| func_188255_a(FixType arg0, DataWalker arg1)|void
| func_188256_a(FixType arg0, FixableData arg1)|void
| func_188257_a(FixType arg0, NBTTagCompound arg1)|NBTTagCompound
| func_188258_a(FixTypes arg0, DataWalker arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Tutorial

|Class
|--
|net.minecraft.client.tutorial.Tutorial

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_193292_a(TutorialSteps t)|void
| func_193293_a(MovementInput m)|void
| func_193294_a(WorldClient arg0, BlockPos arg1, BlockState arg2, float arg3)|void
| func_193295_e()|Minecraft
| func_193296_a()|void
| func_193297_a(WorldClient arg0, RayTraceResult arg1)|void
| func_193299_a(MouseHelper m)|void
| func_193300_b()|void
| func_193301_a(ItemStack i)|void
| func_193302_c()|void
| func_193303_d()|void
| func_194072_f()|GameType
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GuiToast

|Class
|--
|net.minecraft.client.gui.toasts.GuiToast

---

|Extends
|--
|Gui

---

|Fields|Type
|--|--
|  field_73735_i|float

---

|Methods|Return Type
|--|--
| func_175174_a(float arg0, float arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_175175_a(int arg0, int arg1, TextureAtlasSprite arg2, int arg3, int arg4)|void
| func_191783_a(ScaledResolution s)|void
| func_191788_b()|void
| func_192988_a(Toast t)|void
| func_192989_b()|Minecraft
| func_192990_a(Class\<? extends T> arg0, Object arg1)|Toast
| func_73729_b(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73731_b(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73732_a(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73733_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SearchTreeManager$Key

|Class
|--
|net.minecraft.client.util.SearchTreeManager$Key

---

|Extends
|--

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SearchTree

|Interface
|--
|net.minecraft.client.util.ISearchTree

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_194038_a(String s)|List\<T>

---

## Snooper

|Class
|--
|net.minecraft.profiler.Snooper

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_130105_g()|long
| func_152767_b(String arg0, Object arg1)|void
| func_152768_a(String arg0, Object arg1)|void
| func_76463_a()|void
| func_76465_c()|Map\<String, String>
| func_76468_d()|boolean
| func_76470_e()|void
| func_76471_b()|void
| func_80006_f()|String
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SaveFormat

|Interface
|--
|net.minecraft.world.storage.ISaveFormat

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_154333_a()|String
| func_154334_a(String s)|boolean
| func_154335_d(String s)|boolean
| func_186352_b(String arg0, String arg1)|File
| func_75799_b()|List\<WorldSummary>
| func_75800_d()|void
| func_75801_b(String s)|boolean
| func_75802_e(String s)|boolean
| func_75803_c(String s)|WorldInfo
| func_75804_a(String arg0, boolean arg1)|SaveHandler
| func_75805_a(String arg0, ProgressUpdate arg1)|boolean
| func_75806_a(String arg0, String arg1)|void
| func_90033_f(String s)|boolean

---

## WorldSettings

|Class
|--
|net.minecraft.world.WorldSettings

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_77158_f()|boolean
| func_77159_a()|WorldSettings
| func_77160_d()|long
| func_77162_e()|GameType
| func_77163_i()|boolean
| func_77164_g()|boolean
| func_77165_h()|WorldType
| func_77166_b()|WorldSettings
| func_77167_c()|boolean
| func_82749_j()|String
| func_82750_a(String s)|WorldSettings
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CrashReport

|Class
|--
|net.minecraft.crash.CrashReport

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_147149_a(File f)|boolean
| func_71497_f()|File
| func_71498_d()|String
| func_71501_a()|String
| func_71502_e()|String
| func_71505_b()|Throwable
| func_71506_a(StringBuilder s)|void
| func_85056_g()|CrashReportCategory
| func_85057_a(String arg0, int arg1)|CrashReportCategory
| func_85058_a(String s)|CrashReportCategory
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## IntegratedServer

|Class
|--
|net.minecraft.server.integrated.IntegratedServer

---

|Extends
|--
|MinecraftServer

---

|Fields|Type
|--|--
|  dataFixer|DataFixer
|  field_175589_i|Queue\<java.util.concurrent.FutureTask\<?>>
|  field_71302_d|String
|  field_71303_e|int
|  field_71304_b|Profiler
|  field_71305_c|WorldServer[]
|  field_71308_o|File
|  field_71311_j|long[]
|  field_71321_q|CommandManager
|  serverModName|String
|  worldTickTimes|Hashtable\<int, long[]>

---

|Methods|Return Type
|--|--
| func_104056_am()|boolean
| func_110454_ao()|Proxy
| func_110455_j()|int
| func_130014_f_()|World
| func_143006_e(int i)|void
| func_143007_ar()|int
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_147130_as()|MinecraftSessionService
| func_147132_au()|void
| func_147133_T()|String
| func_147134_at()|ServerStatusResponse
| func_147135_j()|EnumDifficulty
| func_147137_ag()|NetworkSystem
| func_147139_a(EnumDifficulty e)|void
| func_152344_a(Runnable r)|ListenableFuture\<Object>
| func_152345_ab()|boolean
| func_152357_F()|GameProfile[]
| func_152358_ax()|PlayerProfileCache
| func_152359_aw()|GameProfileRepository
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_175576_a(UUID u)|Entity
| func_175577_aI()|int
| func_175578_N()|boolean
| func_175579_a(World arg0, BlockPos arg1, EntityPlayer arg2)|boolean
| func_175580_aG()|int
| func_175581_ab()|String
| func_175582_h()|ServerCommandManager
| func_175584_a(String arg0, SaveHandler arg1)|void
| func_175586_a(Callable\<V> c)|ListenableFuture\<V>
| func_180425_c()|BlockPos
| func_180507_a_(String arg0, String arg1)|void
| func_181034_q()|boolean
| func_181035_ah()|boolean
| func_183002_r()|boolean
| func_184102_h()|MinecraftServer
| func_184103_al()|PlayerList
| func_184104_a(CommandSender arg0, String arg1, BlockPos arg2, boolean arg3)|List\<String>
| func_184105_a(PlayerList p)|void
| func_184106_y()|boolean
| func_184107_a(ServerStatusResponse s)|void
| func_184108_a(WorldServer w)|int
| func_184109_z()|File
| func_190518_ac()|boolean
| func_191949_aK()|AdvancementManager
| func_193030_aL()|FunctionManager
| func_193031_aM()|void
| func_70000_a(Snooper s)|void
| func_70001_b(Snooper s)|void
| func_70002_Q()|boolean
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_71187_D()|CommandManager
| func_71188_g(boolean b)|void
| func_71190_q()|void
| func_71191_d(int i)|void
| func_71193_K()|boolean
| func_71194_c(boolean b)|void
| func_71195_b_()|String
| func_71197_b()|boolean
| func_71199_h()|boolean
| func_71200_ad()|boolean
| func_71204_b(boolean b)|void
| func_71205_p(String s)|void
| func_71206_a(GameType arg0, boolean arg1)|String
| func_71207_Z()|int
| func_71209_f(String s)|File
| func_71213_z()|String[]
| func_71214_G()|String
| func_71217_p()|void
| func_71218_a(int i)|WorldServer
| func_71219_W()|boolean
| func_71220_V()|boolean
| func_71221_J()|String
| func_71222_d()|void
| func_71223_ag()|void
| func_71224_l(String s)|void
| func_71225_e()|boolean
| func_71228_a(CrashReport c)|void
| func_71229_d(boolean b)|void
| func_71230_b(CrashReport c)|CrashReport
| func_71231_X()|boolean
| func_71233_x()|int
| func_71235_a(GameType g)|void
| func_71236_h(String s)|void
| func_71237_c(String s)|void
| func_71238_n()|File
| func_71240_o()|void
| func_71241_aa()|boolean
| func_71242_L()|boolean
| func_71245_h(boolean b)|void
| func_71246_n(String s)|void
| func_71247_a(String arg0, String arg1, long arg2, WorldType arg3, String arg4)|void
| func_71249_w()|String
| func_71250_E()|KeyPair
| func_71251_e(boolean b)|void
| func_71253_a(KeyPair k)|void
| func_71254_M()|SaveFormat
| func_71255_r()|boolean
| func_71256_s()|void
| func_71257_f(boolean b)|void
| func_71259_af()|int
| func_71260_j()|void
| func_71261_m(String s)|void
| func_71262_S()|boolean
| func_71263_m()|void
| func_71264_H()|boolean
| func_71265_f()|GameType
| func_71266_T()|boolean
| func_71267_a(boolean b)|void
| func_71268_U()|boolean
| func_71270_I()|String
| func_71273_Y()|String
| func_71275_y()|int
| func_71278_l()|boolean
| func_71279_ae()|boolean
| func_71344_c()|boolean
| func_80003_ah()|Snooper
| func_82356_Z()|boolean
| run()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AttachedData

|Class
|--
|dev.latvian.kubejs.util.AttachedData

---

|Extends
|--
|HashMap

---

|Fields|Type
|--|--
|  empty|boolean
|  parent|Object

---

|Methods|Return Type
|--|--
| clear()|void
| clone()|Object
| compute(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| computeIfAbsent(Object arg0, Function\<? super K, ? extends V> arg1)|Object
| computeIfPresent(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| containsKey(Object o)|boolean
| containsValue(Object o)|boolean
| entrySet()|Set\<java.util.Map$Entry\<K, V>>
| forEach(BiConsumer\<? super K, ? super V> b)|void
| get(Object o)|Object
| getOrDefault(Object arg0, Object arg1)|Object
| keySet()|Set\<K>
| merge(Object arg0, Object arg1, BiFunction\<? super V, ? super V, ? extends V> arg2)|Object
| put(Object arg0, Object arg1)|Object
| putAll(Map\<? extends K, ? extends V> m)|void
| putIfAbsent(Object arg0, Object arg1)|Object
| remove(Object o)|Object
| remove(Object arg0, Object arg1)|boolean
| replace(Object arg0, Object arg1, Object arg2)|boolean
| replace(Object arg0, Object arg1)|Object
| replaceAll(BiFunction\<? super K, ? super V, ? extends V> b)|void
| size()|int
| values()|Collection\<V>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityPotionEffects

|Class
|--
|dev.latvian.kubejs.entity.EntityPotionEffectsJS

---

|Extends
|--

---

|Fields|Type
|--|--
|  active|Collection\<PotionEffect>
|  map|Map\<Potion, PotionEffect>

---

|Methods|Return Type
|--|--
| add(Object potion, int duration)|void
| add(Object potion, int duration, int amplifier)|void
| add(Object potion)|void
| add(Object potion, int duration, int amplifier, boolean ambient, boolean showParticles)|void
| clear()|void
| isApplicable(PotionEffect effect)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GameProfile

|Class
|--
|com.mojang.authlib.GameProfile

---

|Extends
|--

---

|Fields|Type
|--|--
|  complete|boolean
|  id|UUID
|  legacy|boolean
|  name|String
|  properties|PropertyMap

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PlayerStats

|Class
|--
|dev.latvian.kubejs.player.PlayerStatsJS

---

|Extends
|--

---

|Fields|Type
|--|--
|  player|Player

---

|Methods|Return Type
|--|--
| add(Object arg0, int arg1)|void
| get(Object o)|int
| set(Object arg0, int arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ClientPlayerData

|Class
|--
|dev.latvian.kubejs.player.ClientPlayerDataJS

---

|Extends
|--
|PlayerData

---

|Fields|Type
|--|--
|  data Temporary data, mods can attach objects to this|AttachedData
|  id|UUID
|  name|String
|  overworld|World
|  player|ClientPlayer
|  playerEntity|EntityPlayer
|  profile|GameProfile
|  world|ClientWorld

---

|Methods|Return Type
|--|--
| hasClientMod()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GameRules

|Class
|--
|dev.latvian.kubejs.server.GameRulesJS

---

|Extends
|--

---

|Methods|Return Type
|--|--
| getBoolean(String s)|boolean
| getInt(String s)|int
| getString(String s)|String
| set(String arg0, Object arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Explosion

|Class
|--
|dev.latvian.kubejs.world.ExplosionJS

---

|Extends
|--

---

|Fields|Type
|--|--
|  causesFire|boolean
|  damagesTerrain|boolean
|  exploder|Entity
|  strength|float
|  x|double
|  y|double
|  z|double

---

|Methods|Return Type
|--|--
| causesFire(boolean b)|Explosion
| damagesTerrain(boolean b)|Explosion
| explode()|void
| exploder(Entity e)|Explosion
| strength(float f)|Explosion
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PlayerData

|Class
|--
|dev.latvian.kubejs.player.PlayerDataJS

---

|Extends
|--
|WithAttachedData

---

|Fields|Type
|--|--
|  data Temporary data, mods can attach objects to this|AttachedData
|  id|UUID
|  name|String
|  overworld|World
|  player|Player
|  playerEntity|EntityPlayer
|  profile|GameProfile

---

|Methods|Return Type
|--|--
| hasClientMod()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## FluidStack

|Class
|--
|net.minecraftforge.fluids.FluidStack

---

|Extends
|--

---

|Fields|Type
|--|--
|  amount|int
|  fluid|Fluid
|  localizedName|String
|  tag|NBTTagCompound
|  unlocalizedName|String

---

|Methods|Return Type
|--|--
| containsFluid(FluidStack f)|boolean
| copy()|FluidStack
| isFluidEqual(ItemStack i)|boolean
| isFluidEqual(FluidStack f)|boolean
| isFluidStackIdentical(FluidStack f)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeToNBT(NBTTagCompound n)|NBTTagCompound

---

## WithID

|Interface
|--
|com.feed_the_beast.ftblib.lib.util.IWithID

---

|Extends
|--

---

|Fields|Type
|--|--
|  id|String

---

|Methods|Return Type
|--|--

---

## Icon

|Class
|--
|com.feed_the_beast.ftblib.lib.icon.Icon

---

|Extends
|--

---

|Fields|Type
|--|--
|  empty|boolean
|  ingredient|Object
|  json|JsonElement

---

|Methods|Return Type
|--|--
| bindTexture()|void
| combineWith(Icon[] i)|Icon
| combineWith(Icon i)|Icon
| copy()|Icon
| createPixelBuffer()|PixelBuffer
| draw(int arg0, int arg1, int arg2, int arg3)|void
| draw(int arg0, int arg1, int arg2, int arg3, Color4I arg4)|void
| draw3D(Color4I c)|void
| drawStatic(int arg0, int arg1, int arg2, int arg3)|void
| hasPixelBuffer()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void
| withBorder(int i)|Icon
| withOutline(Color4I arg0, boolean arg1)|Icon
| withTint(Color4I c)|Icon

---

## ImageIcon

|Class
|--
|com.feed_the_beast.ftblib.lib.icon.ImageIcon

---

|Extends
|--
|Icon

---

|Fields|Type
|--|--
|  empty|boolean
|  ingredient|Object
|  json|JsonElement
|  maxU|double
|  maxV|double
|  minU|double
|  minV|double
|  texture|ResourceLocation

---

|Methods|Return Type
|--|--
| bindTexture()|void
| combineWith(Icon[] i)|Icon
| combineWith(Icon i)|Icon
| copy()|Icon
| createPixelBuffer()|PixelBuffer
| draw(int arg0, int arg1, int arg2, int arg3, Color4I arg4)|void
| draw(int arg0, int arg1, int arg2, int arg3)|void
| draw3D(Color4I c)|void
| drawStatic(int arg0, int arg1, int arg2, int arg3)|void
| hasPixelBuffer()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void
| withBorder(int i)|Icon
| withOutline(Color4I arg0, boolean arg1)|Icon
| withTint(Color4I c)|Icon
| withUV(double arg0, double arg1, double arg2, double arg3)|ImageIcon
| withUVfromCoords(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|ImageIcon

---

## PixelBuffer

|Interface
|--
|com.feed_the_beast.ftblib.lib.client.IPixelBuffer

---

|Extends
|--

---

|Fields|Type
|--|--
|  height|int
|  pixels|int[]
|  width|int

---

|Methods|Return Type
|--|--
| copy()|PixelBuffer
| fill(int i)|void
| fill(int arg0, int arg1, int arg2, int arg3, int arg4)|void
| getRGB(int arg0, int arg1)|int
| getRGB(int arg0, int arg1, int arg2, int arg3, int[] arg4)|int[]
| getSubimage(int arg0, int arg1, int arg2, int arg3)|PixelBuffer
| setRGB(int arg0, int arg1, int arg2)|void
| setRGB(int arg0, int arg1, int arg2, int arg3, int[] arg4)|void
| setRGB(int arg0, int arg1, PixelBuffer arg2)|void
| toByteBuffer(boolean b)|ByteBuffer

---

## Color4I

|Class
|--
|com.feed_the_beast.ftblib.lib.icon.Color4I

---

|Extends
|--
|Icon

---

|Fields|Type
|--|--
|  empty|boolean
|  ingredient|Object
|  json|JsonElement
|  mutable|boolean

---

|Methods|Return Type
|--|--
| addBrightness(float f)|Color4I
| alphaf()|float
| alphai()|int
| bindTexture()|void
| bluef()|float
| bluei()|int
| combineWith(Icon[] i)|Icon
| combineWith(Icon i)|Icon
| copy()|Color4I
| copy()|Icon
| createPixelBuffer()|PixelBuffer
| draw(int arg0, int arg1, int arg2, int arg3, Color4I arg4)|void
| draw(int arg0, int arg1, int arg2, int arg3)|void
| draw3D(Color4I c)|void
| drawStatic(int arg0, int arg1, int arg2, int arg3)|void
| greenf()|float
| greeni()|int
| hasPixelBuffer()|boolean
| lerp(Color4I arg0, float arg1)|Color4I
| mutable()|MutableColor4I
| redf()|float
| redi()|int
| rgb()|int
| rgba()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void
| whiteIfEmpty()|Color4I
| withAlpha(int i)|Color4I
| withAlphaf(float f)|Color4I
| withBorder(int i)|Icon
| withOutline(Color4I arg0, boolean arg1)|Icon
| withTint(Color4I c)|Color4I
| withTint(Color4I c)|Icon

---

## WithAttachedData

|Interface
|--
|dev.latvian.kubejs.util.WithAttachedData

---

|Extends
|--

---

|Fields|Type
|--|--
|  data Temporary data, mods can attach objects to this|AttachedData

---

|Methods|Return Type
|--|--

---

## Int2ByteOpenHashMap

|Class
|--
|it.unimi.dsi.fastutil.ints.Int2ByteOpenHashMap

---

|Extends
|--
|AbstractInt2ByteMap
|Serializable
|Cloneable
|Hash

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| addTo(int arg0, byte arg1)|byte
| clear()|void
| clone()|Object
| clone()|Int2ByteOpenHashMap
| compute(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| computeIfAbsent(Object arg0, Function\<? super K, ? extends V> arg1)|Object
| computeIfPresent(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| containsKey(int i)|boolean
| containsKey(Object o)|boolean
| containsValue(byte b)|boolean
| containsValue(Object o)|boolean
| defaultReturnValue(byte b)|void
| defaultReturnValue()|byte
| entrySet()|ObjectSet\<java.util.Map$Entry\<java.lang.Integer, java.lang.Byte>>
| entrySet()|Set
| forEach(BiConsumer\<? super K, ? super V> b)|void
| get(int i)|byte
| get(int i)|byte
| get(Object o)|byte
| get(Object o)|Object
| getOrDefault(Object arg0, Object arg1)|Object
| growthFactor()|int
| growthFactor(int i)|void
| int2ByteEntrySet()|Int2ByteMap$FastEntrySet
| int2ByteEntrySet()|ObjectSet
| keySet()|IntSet
| keySet()|Set
| merge(Object arg0, Object arg1, BiFunction\<? super V, ? super V, ? extends V> arg2)|Object
| put(int arg0, byte arg1)|byte
| put(int arg0, byte arg1)|byte
| put(Object arg0, Object arg1)|Object
| putAll(Map\<? extends java.lang.Integer, ? extends java.lang.Byte> m)|void
| putIfAbsent(Object arg0, Object arg1)|Object
| rehash()|boolean
| remove(Object o)|Object
| remove(Object o)|byte
| remove(int i)|byte
| remove(Object arg0, Object arg1)|boolean
| replace(Object arg0, Object arg1)|Object
| replace(Object arg0, Object arg1, Object arg2)|boolean
| replaceAll(BiFunction\<? super K, ? super V, ? extends V> b)|void
| size()|int
| trim()|boolean
| trim(int i)|boolean
| values()|Collection
| values()|ByteCollection
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## IntOpenHashSet

|Class
|--
|it.unimi.dsi.fastutil.ints.IntOpenHashSet

---

|Extends
|--
|AbstractIntSet
|Serializable
|Cloneable
|Hash

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(int i)|boolean
| add(int i)|boolean
| add(Object o)|boolean
| addAll(Collection\<? extends java.lang.Integer> c)|boolean
| addAll(IntCollection i)|boolean
| clear()|void
| clone()|Object
| clone()|IntOpenHashSet
| contains(int i)|boolean
| contains(Object o)|boolean
| containsAll(Collection\<?> c)|boolean
| containsAll(IntCollection i)|boolean
| forEach(Consumer\<? super T> c)|void
| growthFactor()|int
| growthFactor(int i)|void
| intIterator()|IntIterator
| iterator()|Iterator
| iterator()|IntIterator
| parallelStream()|Stream\<E>
| rehash()|boolean
| rem(int i)|boolean
| rem(Object o)|boolean
| remove(int i)|boolean
| remove(Object o)|boolean
| removeAll(Collection\<?> c)|boolean
| removeAll(IntCollection i)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| retainAll(Collection\<?> c)|boolean
| retainAll(IntCollection i)|boolean
| size()|int
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| toArray()|Object[]
| toArray(Object[] o)|Object[]
| toArray(int[] i)|int[]
| toIntArray()|int[]
| toIntArray(int[] i)|int[]
| trim(int i)|boolean
| trim()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Int2ObjectOpenHashMap

|Class
|--
|it.unimi.dsi.fastutil.ints.Int2ObjectOpenHashMap

---

|Extends
|--
|AbstractInt2ObjectMap
|Serializable
|Cloneable
|Hash

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| clear()|void
| clone()|Int2ObjectOpenHashMap\<V>
| clone()|Object
| compute(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| computeIfAbsent(Object arg0, Function\<? super K, ? extends V> arg1)|Object
| computeIfPresent(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| containsKey(int i)|boolean
| containsKey(Object o)|boolean
| containsValue(Object o)|boolean
| defaultReturnValue(Object o)|void
| defaultReturnValue()|Object
| entrySet()|Set
| entrySet()|ObjectSet\<java.util.Map$Entry\<java.lang.Integer, V>>
| forEach(BiConsumer\<? super K, ? super V> b)|void
| get(int i)|Object
| get(int i)|Object
| get(Object o)|Object
| getOrDefault(Object arg0, Object arg1)|Object
| growthFactor(int i)|void
| growthFactor()|int
| int2ObjectEntrySet()|ObjectSet
| int2ObjectEntrySet()|Int2ObjectMap$FastEntrySet\<V>
| keySet()|IntSet
| keySet()|Set
| merge(Object arg0, Object arg1, BiFunction\<? super V, ? super V, ? extends V> arg2)|Object
| put(int arg0, Object arg1)|Object
| put(int arg0, Object arg1)|Object
| put(Object arg0, Object arg1)|Object
| putAll(Map\<? extends java.lang.Integer, ? extends V> m)|void
| putIfAbsent(Object arg0, Object arg1)|Object
| rehash()|boolean
| remove(Object o)|Object
| remove(int i)|Object
| remove(Object arg0, Object arg1)|boolean
| replace(Object arg0, Object arg1)|Object
| replace(Object arg0, Object arg1, Object arg2)|boolean
| replaceAll(BiFunction\<? super K, ? super V, ? extends V> b)|void
| size()|int
| trim(int i)|boolean
| trim()|boolean
| values()|Collection
| values()|ObjectCollection\<V>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Quest

|Class
|--
|com.feed_the_beast.ftbquests.quest.Quest

---

|Extends
|--
|QuestObject

---

|Fields|Type
|--|--
|  altIcon|Icon
|  altTitle|String
|  canRepeat|boolean
|  chapter|Chapter
|  codeString|String
|  customClick|String
|  dependencies|List\<QuestObject>
|  dependencyRequirement|DependencyRequirement
|  description|String
|  disableJEI|EnumTristate
|  disableToast|boolean
|  file|File
|  guidePage|String
|  hide|boolean
|  hideDependencyLines|boolean
|  hideTextUntilComplete|boolean
|  icon|Icon
|  id|int
|  invalid|boolean
|  minRequiredDependencies|int
|  objectType|QuestObjectType
|  parentID|int
|  questChapter|Chapter
|  questFile|QuestFile
|  rewards|List\<Reward>
|  shape|QuestShape
|  tags|Set\<String>
|  tasks|List\<Task>
|  text|String[]
|  title|String
|  unformattedTitle|String
|  x|byte
|  y|byte
|  yellowDisplayName|String

---

|Methods|Return Type
|--|--
| areDependenciesComplete(QuestData q)|boolean
| cacheProgress()|boolean
| canStartTasks(QuestData q)|boolean
| changeProgress(QuestData arg0, ChangeProgress arg1)|void
| checkRepeatableQuests(QuestData arg0, UUID arg1)|void
| clearCachedData()|void
| createSubGroup(ConfigGroup c)|ConfigGroup
| createTabContent()|Optional\<Node>
| deleteChildren()|void
| deleteSelf()|void
| editedFromGUI()|void
| forceProgress(QuestData arg0, ChangeProgress arg1, boolean arg2)|void
| getConfig(ConfigGroup c)|void
| getRelativeProgress(QuestData q)|int
| getRelativeProgressFromChildren(QuestData q)|int
| getTask(int i)|Task
| getUnclaimedRewards(UUID arg0, QuestData arg1, boolean arg2)|int
| hasDependency(QuestObject q)|boolean
| hasTag(String s)|boolean
| hasUnclaimedRewards(UUID arg0, QuestData arg1, boolean arg2)|boolean
| isComplete(QuestData q)|boolean
| isStarted(QuestData q)|boolean
| isVisible(QuestData q)|boolean
| loadText()|QuestObjectText
| onCompleted(QuestData arg0, List\<EntityPlayerMP> arg1)|void
| onCreated()|void
| onEditButtonClicked()|void
| readData(NBTTagCompound n)|void
| readNetData(DataIn d)|void
| refreshJEI()|int
| verifyDependencies(boolean b)|boolean
| verifyDependenciesInternal(QuestObject arg0, boolean arg1)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeData(NBTTagCompound n)|void
| writeNetData(DataOut d)|void

---

## Task

|Class
|--
|com.feed_the_beast.ftbquests.quest.task.Task

---

|Extends
|--
|QuestObject

---

|Fields|Type
|--|--
|  altIcon|Icon
|  altTitle|String
|  buttonText|String
|  codeString|String
|  disableToast|boolean
|  file|File
|  icon|Icon
|  id|int
|  ingredient|Object
|  invalid|boolean
|  maxProgress|long
|  maxProgressString|String
|  objectType|QuestObjectType
|  parentID|int
|  quest|Quest
|  questChapter|Chapter
|  questFile|QuestFile
|  screenCoreClass|Class\<? extends com.feed_the_beast.ftbquests.tile.TileTaskScreenCore>
|  screenPartClass|Class\<? extends com.feed_the_beast.ftbquests.tile.TileTaskScreenPart>
|  tags|Set\<String>
|  title|String
|  type|TaskType
|  unformattedTitle|String
|  yellowDisplayName|String

---

|Methods|Return Type
|--|--
| addMouseOverText(List\<String> arg0, TaskData arg1)|void
| addTitleInMouseOverText()|boolean
| autoSubmitOnPlayerTick()|int
| cacheProgress()|boolean
| canInsertItem()|boolean
| changeProgress(QuestData arg0, ChangeProgress arg1)|void
| clearCachedData()|void
| consumesResources()|boolean
| createData(QuestData q)|TaskData
| createScreenCore(World w)|TileTaskScreenCore
| createScreenPart(World w)|TileTaskScreenPart
| createSubGroup(ConfigGroup c)|ConfigGroup
| createTabContent()|Optional\<Node>
| deleteChildren()|void
| deleteSelf()|void
| drawGUI(TaskData arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawScreen(TaskData t)|void
| editedFromGUI()|void
| forceProgress(QuestData arg0, ChangeProgress arg1, boolean arg2)|void
| getConfig(ConfigGroup c)|void
| getRelativeProgress(QuestData q)|int
| getRelativeProgressFromChildren(QuestData q)|int
| hasTag(String s)|boolean
| hideProgressNumbers()|boolean
| isComplete(QuestData q)|boolean
| isStarted(QuestData q)|boolean
| isVisible(QuestData q)|boolean
| loadText()|QuestObjectText
| onButtonClicked(boolean b)|void
| onCompleted(QuestData arg0, List\<EntityPlayerMP> arg1)|void
| onCreated()|void
| onEditButtonClicked()|void
| readData(NBTTagCompound n)|void
| readNetData(DataIn d)|void
| refreshJEI()|int
| submitItemsOnInventoryChange()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeData(NBTTagCompound n)|void
| writeNetData(DataOut d)|void

---

## Reward

|Class
|--
|com.feed_the_beast.ftbquests.quest.reward.Reward

---

|Extends
|--
|QuestObjectBase

---

|Fields|Type
|--|--
|  altIcon|Icon
|  altTitle|String
|  autoClaimType|RewardAutoClaim
|  buttonText|String
|  codeString|String
|  excludeFromClaimAll|boolean
|  file|File
|  icon|Icon
|  id|int
|  ingredient|Object
|  invalid|boolean
|  objectType|QuestObjectType
|  parentID|int
|  quest|Quest
|  questChapter|Chapter
|  questFile|QuestFile
|  tags|Set\<String>
|  team|EnumTristate
|  teamReward|boolean
|  title|String
|  type|RewardType
|  unformattedTitle|String
|  yellowDisplayName|String

---

|Methods|Return Type
|--|--
| addMouseOverText(List\<String> l)|void
| addTitleInMouseOverText()|boolean
| changeProgress(QuestData arg0, ChangeProgress arg1)|void
| claim(EntityPlayerMP arg0, boolean arg1)|void
| claimAutomated(TileEntity arg0, EntityPlayerMP arg1)|ItemStack
| clearCachedData()|void
| createSubGroup(ConfigGroup c)|ConfigGroup
| createTabContent()|Optional\<Node>
| deleteChildren()|void
| deleteSelf()|void
| editedFromGUI()|void
| forceProgress(QuestData arg0, ChangeProgress arg1, boolean arg2)|void
| getConfig(ConfigGroup c)|void
| hasTag(String s)|boolean
| loadText()|QuestObjectText
| onButtonClicked(boolean b)|void
| onCreated()|void
| onEditButtonClicked()|void
| readData(NBTTagCompound n)|void
| readNetData(DataIn d)|void
| refreshJEI()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeData(NBTTagCompound n)|void
| writeNetData(DataOut d)|void

---

## FTB Quests Player Data

|Class
|--
|com.feed_the_beast.ftbquests.integration.kubejs.FTBQuestsKubeJSPlayerData

---

|Extends
|--

---

|Fields|Type
|--|--
|  canEdit Returns true if player is in editing mode|boolean
|  data|QuestData
|  file|QuestFile

---

|Methods|Return Type
|--|--
| addProgress(Object id, long progress)|void
| canStartQuest(Object id)|boolean
| complete(Object id)|void
| getProgress(Object id)|int
| isCompleted(Object id)|boolean
| isStarted(Object id)|boolean
| reset(Object id)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GameStagesPlayerData

|Class
|--
|dev.latvian.kubejs.integration.gamestages.GameStagesPlayerData

---

|Extends
|--

---

|Fields|Type
|--|--
|  list|Collection\<String>

---

|Methods|Return Type
|--|--
| add(String stage)|void
| clear()|void
| has(String stage)|boolean
| remove(String stage)|void
| set(String stage, boolean value)|boolean
| sync() Sends all stages from server to client|void
| toggle(String stage)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Chapter

|Class
|--
|com.feed_the_beast.ftbquests.quest.Chapter

---

|Extends
|--
|QuestObject

---

|Fields|Type
|--|--
|  altIcon|Icon
|  altTitle|String
|  alwaysInvisible|boolean
|  children|List\<Chapter>
|  codeString|String
|  description|List\<String>
|  disableToast|boolean
|  file|File
|  group|Chapter
|  icon|Icon
|  id|int
|  index|int
|  invalid|boolean
|  objectType|QuestObjectType
|  parentID|int
|  questChapter|Chapter
|  questFile|QuestFile
|  quests|List\<Quest>
|  tags|Set\<String>
|  title|String
|  unformattedTitle|String
|  yellowDisplayName|String

---

|Methods|Return Type
|--|--
| cacheProgress()|boolean
| changeProgress(QuestData arg0, ChangeProgress arg1)|void
| clearCachedData()|void
| createSubGroup(ConfigGroup c)|ConfigGroup
| createTabContent()|Optional\<Node>
| deleteChildren()|void
| deleteSelf()|void
| editedFromGUI()|void
| forceProgress(QuestData arg0, ChangeProgress arg1, boolean arg2)|void
| getConfig(ConfigGroup c)|void
| getRelativeProgress(QuestData q)|int
| getRelativeProgressFromChildren(QuestData q)|int
| getUnclaimedRewards(UUID arg0, QuestData arg1, boolean arg2)|int
| hasChildren()|boolean
| hasGroup()|boolean
| hasTag(String s)|boolean
| hasUnclaimedRewards(UUID arg0, QuestData arg1, boolean arg2)|boolean
| isComplete(QuestData q)|boolean
| isStarted(QuestData q)|boolean
| isVisible(QuestData q)|boolean
| loadText()|QuestObjectText
| onCompleted(QuestData arg0, List\<EntityPlayerMP> arg1)|void
| onCreated()|void
| onEditButtonClicked()|void
| readData(NBTTagCompound n)|void
| readNetData(DataIn d)|void
| refreshJEI()|int
| verifyDependenciesInternal(QuestObject arg0, boolean arg1)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeData(NBTTagCompound n)|void
| writeNetData(DataOut d)|void

---

## RewardAutoClaim

|Class
|--
|com.feed_the_beast.ftbquests.quest.reward.RewardAutoClaim

---

|Extends
|--
|Enum
|WithID

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>
|  id|String

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Ticks

|Class
|--
|com.feed_the_beast.ftblib.lib.math.Ticks

---

|Extends
|--

---

|Methods|Return Type
|--|--
| add(long l)|Ticks
| add(Ticks t)|Ticks
| days()|long
| daysd()|double
| equalsTimer(Ticks t)|boolean
| hasTicks()|boolean
| hours()|long
| hoursd()|double
| millis()|long
| minutes()|long
| minutesd()|double
| seconds()|long
| secondsd()|double
| ticks()|long
| toTimeString()|String
| wait(long arg0, int arg1)|void
| wait(long l)|void
| weeks()|long
| weeksd()|double
| x(double d)|Ticks
| x(long l)|Ticks

---

## EntityWeight

|Class
|--
|com.feed_the_beast.ftbquests.quest.loot.EntityWeight

---

|Extends
|--

---

|Fields|Type
|--|--
|  boss|int
|  monster|int
|  passive|int

---

|Methods|Return Type
|--|--
| getWeight(Entity e)|int
| readData(NBTTagCompound n)|void
| readNetData(DataIn d)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeData(NBTTagCompound n)|void
| writeNetData(DataOut d)|void

---

## RewardTable

|Class
|--
|com.feed_the_beast.ftbquests.quest.loot.RewardTable

---

|Extends
|--
|QuestObjectBase

---

|Fields|Type
|--|--
|  altIcon|Icon
|  altTitle|String
|  codeString|String
|  emptyWeight|int
|  fakeQuest|Quest
|  file|File
|  hideTooltip|boolean
|  icon|Icon
|  id|int
|  invalid|boolean
|  lootCrate|LootCrate
|  lootSize|int
|  objectType|QuestObjectType
|  parentID|int
|  questChapter|Chapter
|  questFile|QuestFile
|  rewards|List\<WeightedReward>
|  tags|Set\<String>
|  title|String
|  unformattedTitle|String
|  useTitle|boolean
|  yellowDisplayName|String

---

|Methods|Return Type
|--|--
| addMouseOverText(List\<String> arg0, boolean arg1, boolean arg2)|void
| changeProgress(QuestData arg0, ChangeProgress arg1)|void
| clearCachedData()|void
| createSubGroup(ConfigGroup c)|ConfigGroup
| createTabContent()|Optional\<Node>
| deleteChildren()|void
| deleteSelf()|void
| editedFromGUI()|void
| forceProgress(QuestData arg0, ChangeProgress arg1, boolean arg2)|void
| getConfig(ConfigGroup c)|void
| getTotalWeight(boolean b)|int
| hasTag(String s)|boolean
| loadText()|QuestObjectText
| onCreated()|void
| onEditButtonClicked()|void
| readData(NBTTagCompound n)|void
| readNetData(DataIn d)|void
| refreshJEI()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeData(NBTTagCompound n)|void
| writeNetData(DataOut d)|void

---

## ConfigGroup

|Class
|--
|com.feed_the_beast.ftblib.lib.config.ConfigGroup

---

|Extends
|--
|FinalIDObject

---

|Fields|Type
|--|--
|  displayName|TextComponent
|  groups|Collection\<ConfigGroup>
|  id|String
|  parent|ConfigGroup
|  path|String
|  valueKeyTree|List\<String>
|  values|Collection\<ConfigValueInstance>
|  valueTree|List\<ConfigValueInstance>

---

|Methods|Return Type
|--|--
| add(ConfigValueInstance c)|ConfigValueInstance
| add(String arg0, ConfigValue arg1, ConfigValue arg2)|ConfigValueInstance
| addBool(String arg0, BooleanSupplier arg1, BooleanConsumer arg2, boolean arg3)|ConfigValueInstance
| addDouble(String arg0, DoubleSupplier arg1, DoubleConsumer arg2, double arg3, double arg4, double arg5)|ConfigValueInstance
| addEnum(String arg0, Supplier\<T> arg1, Consumer\<T> arg2, NameMap\<T> arg3)|ConfigValueInstance
| addInt(String arg0, IntSupplier arg1, IntConsumer arg2, int arg3, int arg4, int arg5)|ConfigValueInstance
| addList(String arg0, Collection\<V> arg1, ConfigValue arg2, Function\<V, C> arg3, Function\<C, V> arg4)|ConfigValueInstance
| addLong(String arg0, LongSupplier arg1, LongConsumer arg2, long arg3, long arg4, long arg5)|ConfigValueInstance
| addString(String arg0, Supplier\<String> arg1, Consumer\<String> arg2, String arg3)|ConfigValueInstance
| addString(String arg0, Supplier\<String> arg1, Consumer\<String> arg2, String arg3, Pattern arg4)|ConfigValueInstance
| copy()|ConfigGroup
| deserializeNBT(NBTTagCompound n)|void
| getDisplayNameOf(ConfigValueInstance c)|TextComponent
| getGroup(String s)|ConfigGroup
| getInfoOf(ConfigValueInstance c)|TextComponent
| getNullableGroup(String s)|ConfigGroup
| getValue(String s)|ConfigValue
| getValueInstance(String s)|ConfigValueInstance
| hasValue(String s)|boolean
| removeValue(String s)|void
| serializeNBT()|NBTTagCompound
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## LootCrate

|Class
|--
|com.feed_the_beast.ftbquests.quest.loot.LootCrate

---

|Extends
|--

---

|Fields|Type
|--|--
|  color|Color4I
|  drops|EntityWeight
|  glow|boolean
|  itemName|String
|  stringID|String
|  table|RewardTable

---

|Methods|Return Type
|--|--
| createStack()|ItemStack
| getConfig(ConfigGroup c)|void
| readData(NBTTagCompound n)|void
| readNetData(DataIn d)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeData(NBTTagCompound n)|void
| writeNetData(DataOut d)|void

---

## QuestObjectText

|Class
|--
|com.feed_the_beast.ftbquests.util.QuestObjectText

---

|Extends
|--

---

|Methods|Return Type
|--|--
| getString(String s)|String
| getStringArray(String s)|String[]
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityPlayerMP

|Class
|--
|net.minecraft.entity.player.EntityPlayerMP

---

|Extends
|--
|EntityPlayer
|ContainerListener

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  defaultEyeHeight|float
|  displayNameString|String
|  entityData|NBTTagCompound
|  eyeHeight|float
|  field_110153_bc|float
|  field_110158_av|int
|  field_175152_f|int
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_184617_aD|int
|  field_184618_aE|float
|  field_184619_aG|float
|  field_184622_au|EnumHand
|  field_184627_bm|ItemStack
|  field_184628_bn|int
|  field_190534_ay|int
|  field_191988_bg|float
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_70701_bs|float
|  field_70702_br|float
|  field_70703_bu|boolean
|  field_70704_bt|float
|  field_70718_bc|int
|  field_70720_be|int
|  field_70721_aZ|float
|  field_70725_aQ|int
|  field_70726_aT|float
|  field_70727_aS|float
|  field_70732_aI|float
|  field_70733_aJ|float
|  field_70737_aN|int
|  field_70738_aO|int
|  field_70739_aP|float
|  field_70747_aH|float
|  field_70755_b|EntityLivingBase
|  field_70758_at|float
|  field_70759_as|float
|  field_70760_ar|float
|  field_70761_aq|float
|  field_70769_ao|float
|  field_70770_ap|float
|  field_70771_an|int
|  field_71067_cb|int
|  field_71068_ca|int
|  field_71069_bz|Container
|  field_71070_bA|Container
|  field_71071_by|InventoryPlayer
|  field_71075_bZ|PlayerCapabilities
|  field_71076_b|int
|  field_71079_bU|float
|  field_71081_bT|BlockPos
|  field_71082_cx|float
|  field_71083_bS|boolean
|  field_71085_bR|double
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71089_bV|float
|  field_71090_bL|int
|  field_71091_bM|double
|  field_71093_bK|int
|  field_71094_bP|double
|  field_71095_bQ|double
|  field_71096_bN|double
|  field_71097_bO|double
|  field_71104_cf|EntityFishHook
|  field_71106_cc|float
|  field_71107_bF|float
|  field_71109_bG|float
|  field_71131_d|double
|  field_71132_e|double
|  field_71133_b|MinecraftServer
|  field_71134_c|PlayerInteractionManager
|  field_71135_a|NetHandlerPlayServer
|  field_71136_j|boolean
|  field_71137_h|boolean
|  field_71138_i|int
|  field_71139_cq|int
|  field_82151_R|float
|  field_82153_h|int
|  field_82175_bq|boolean
|  field_98038_p|boolean
|  itemInUseMaxDuration|int
|  persistentID|UUID
|  prefixes|Collection\<TextComponent>
|  spawnDimension|int
|  suffixes|Collection\<TextComponent>
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| addPrefix(TextComponent t)|void
| addSuffix(TextComponent t)|void
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| curePotionEffects(ItemStack i)|void
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_110124_au()|UUID
| func_110138_aP()|float
| func_110139_bj()|float
| func_110140_aT()|AbstractAttributeMap
| func_110142_aN()|CombatTracker
| func_110143_aJ()|float
| func_110144_aD()|EntityLivingBase
| func_110145_l(Entity e)|void
| func_110148_a(Attribute a)|AttributeInstance
| func_110149_m(float f)|void
| func_110430_a(float arg0, float arg1, boolean arg2, boolean arg3)|void
| func_130011_c(Entity e)|void
| func_130014_f_()|World
| func_142013_aG()|int
| func_142015_aE()|int
| func_143004_u()|void
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_146097_a(ItemStack arg0, boolean arg1, boolean arg2)|EntityItem
| func_146103_bH()|GameProfile
| func_146105_b(TextComponent arg0, boolean arg1)|void
| func_147096_v()|EntityPlayer$EnumChatVisibility
| func_147099_x()|StatisticsManagerServer
| func_147100_a(CPacketClientSettings c)|void
| func_152111_bt()|void
| func_152112_bu()|void
| func_152339_d(Entity e)|void
| func_154331_x()|long
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_175138_ci()|int
| func_175140_cp()|boolean
| func_175141_a(TileEntitySign t)|void
| func_175142_cm()|boolean
| func_175144_cb()|boolean
| func_175145_a(StatBase s)|void
| func_175146_a(LockCode l)|boolean
| func_175148_a(EnumPlayerModelParts e)|boolean
| func_175149_v()|boolean
| func_175150_k(boolean b)|void
| func_175151_a(BlockPos arg0, EnumFacing arg1, ItemStack arg2)|boolean
| func_175173_a(Container arg0, Inventory arg1)|void
| func_175396_E()|TextComponent
| func_175397_a(String arg0, String arg1)|void
| func_175398_C()|Entity
| func_175399_e(Entity e)|void
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180468_a(InteractionObject i)|void
| func_180469_a(BlockPos b)|EntityPlayer$SleepResult
| func_180470_cg()|BlockPos
| func_180472_a(Merchant m)|void
| func_180473_a(BlockPos arg0, boolean arg1)|void
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_184582_a(EntityEquipmentSlot e)|ItemStack
| func_184583_d(DamageSource d)|boolean
| func_184585_cz()|boolean
| func_184586_b(EnumHand e)|ItemStack
| func_184587_cr()|boolean
| func_184589_d(Potion p)|void
| func_184591_cq()|EnumHandSide
| func_184592_cb()|ItemStack
| func_184595_k(double arg0, double arg1, double arg2)|boolean
| func_184596_c(Potion p)|PotionEffect
| func_184597_cx()|void
| func_184598_c(EnumHand e)|void
| func_184599_cB()|int
| func_184600_cs()|EnumHand
| func_184602_cy()|void
| func_184603_cC()|boolean
| func_184605_cv()|int
| func_184607_cu()|ItemStack
| func_184609_a(EnumHand e)|void
| func_184611_a(EnumHand arg0, ItemStack arg1)|void
| func_184612_cw()|int
| func_184613_cA()|boolean
| func_184614_ca()|ItemStack
| func_184809_a(CommandBlockBaseLogic c)|void
| func_184810_cG()|void
| func_184811_cZ()|CooldownTracker
| func_184812_l_()|boolean
| func_184813_a(BlockState b)|float
| func_184814_a(ItemStack arg0, EnumHand arg1)|void
| func_184816_a(EntityItem e)|ItemStack
| func_184817_da()|float
| func_184818_cX()|float
| func_184819_a(EnumHandSide e)|void
| func_184821_cY()|void
| func_184823_b(BlockState b)|boolean
| func_184824_a(TileEntityCommandBlock t)|void
| func_184825_o(float f)|float
| func_184826_a(AbstractHorse arg0, Inventory arg1)|void
| func_184846_L()|void
| func_184847_M()|void
| func_184848_d(Entity e)|void
| func_184850_K()|boolean
| func_189103_N()|void
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_189748_bU()|DamageSource
| func_189807_a(TileEntityStructure t)|void
| func_189808_dh()|boolean
| func_190530_aW()|boolean
| func_190630_a(EntityEquipmentSlot e)|boolean
| func_190631_cK()|boolean
| func_190775_a(Entity arg0, EnumHand arg1)|EnumActionResult
| func_190777_m(boolean b)|void
| func_191521_c(ItemStack i)|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_191986_a(float arg0, float arg1, float arg2)|void
| func_191987_a(BlockPos arg0, boolean arg1)|void
| func_192021_a(List\<Recipe> l)|void
| func_192022_b(List\<Recipe> l)|void
| func_192023_dk()|NBTTagCompound
| func_192024_a(ItemStack arg0, int arg1)|void
| func_192025_dl()|NBTTagCompound
| func_192027_g(NBTTagCompound n)|boolean
| func_192037_E()|RecipeBookServer
| func_192039_O()|PlayerAdvancements
| func_193076_bZ()|Map\<Potion, PotionEffect>
| func_193102_a(ResourceLocation[] r)|void
| func_193104_a(EntityPlayerMP arg0, boolean arg1)|void
| func_193105_t()|boolean
| func_193106_Q()|Vec3d
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70065_x()|void
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70604_c(EntityLivingBase e)|void
| func_70606_j(float f)|void
| func_70608_bn()|boolean
| func_70613_aW()|boolean
| func_70617_f_()|boolean
| func_70631_g_()|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70636_d()|void
| func_70637_d(boolean b)|void
| func_70643_av()|EntityLivingBase
| func_70644_a(Potion p)|boolean
| func_70645_a(DamageSource d)|void
| func_70648_aU()|boolean
| func_70651_bq()|Collection\<PotionEffect>
| func_70652_k(Entity e)|boolean
| func_70653_a(Entity arg0, float arg1, double arg2, double arg3)|void
| func_70654_ax()|int
| func_70658_aO()|int
| func_70659_e(float f)|void
| func_70660_b(Potion p)|PotionEffect
| func_70662_br()|boolean
| func_70664_aZ()|void
| func_70668_bt()|EnumCreatureAttribute
| func_70669_a(ItemStack i)|void
| func_70674_bp()|void
| func_70676_i(float f)|Vec3d
| func_70678_g(float f)|float
| func_70681_au()|Random
| func_70685_l(Entity e)|boolean
| func_70687_e(PotionEffect p)|boolean
| func_70689_ay()|float
| func_70690_d(PotionEffect p)|void
| func_70691_i(float f)|void
| func_70996_bM()|boolean
| func_70999_a(boolean arg0, boolean arg1, boolean arg2)|void
| func_71000_j(double arg0, double arg1, double arg2)|void
| func_71001_a(Entity arg0, int arg1)|void
| func_71004_bE()|void
| func_71005_bN()|InventoryEnderChest
| func_71007_a(Inventory i)|void
| func_71009_b(Entity e)|void
| func_71016_p()|void
| func_71019_a(ItemStack arg0, boolean arg1)|EntityItem
| func_71020_j(float f)|void
| func_71023_q(int i)|void
| func_71024_bL()|FoodStats
| func_71026_bH()|boolean
| func_71029_a(StatBase s)|void
| func_71033_a(GameType g)|void
| func_71037_bA()|int
| func_71040_bB(boolean b)|EntityItem
| func_71043_e(boolean b)|boolean
| func_71047_c(Entity e)|void
| func_71050_bK()|int
| func_71051_bG()|float
| func_71053_j()|void
| func_71059_n(Entity e)|void
| func_71060_bI()|int
| func_71064_a(StatBase arg0, int arg1)|void
| func_71110_a(Container arg0, NonNullList\<ItemStack> arg1)|void
| func_71111_a(Container arg0, int arg1, ItemStack arg2)|void
| func_71112_a(Container arg0, int arg1, int arg2)|void
| func_71113_k()|void
| func_71114_r()|String
| func_71116_b()|void
| func_71117_bO()|void
| func_71118_n()|void
| func_71120_a(Container c)|void
| func_71121_q()|WorldServer
| func_71122_b(double arg0, boolean arg1)|void
| func_71123_m()|void
| func_71127_g()|void
| func_71128_l()|void
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_82242_a(int i)|void
| func_82243_bO()|float
| func_82245_bX()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_85034_r(int i)|void
| func_85035_bI()|int
| func_85039_t(int i)|void
| func_85040_s(int i)|void
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_94060_bK()|EntityLivingBase
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96122_a(EntityPlayer e)|boolean
| func_96123_co()|Scoreboard
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| getBedLocation(int i)|BlockPos
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getDigSpeed(BlockState arg0, BlockPos arg1)|float
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| hasSpawnDimension()|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| isSpawnForced(int i)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| openGui(Object arg0, int arg1, World arg2, int arg3, int arg4, int arg5)|void
| refreshDisplayName()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| setSpawnChunk(BlockPos arg0, boolean arg1, int arg2)|void
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderFaceForward(EntityPlayer e)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## DataIn

|Class
|--
|com.feed_the_beast.ftblib.lib.io.DataIn

---

|Extends
|--

---

|Fields|Type
|--|--
|  position|int

---

|Methods|Return Type
|--|--
| readBlockState()|BlockState
| readBoolean()|boolean
| readByte()|byte
| readBytes(byte[] b)|void
| readBytes(byte[] arg0, int arg1, int arg2)|void
| readCollection(DataIn$Deserializer\<T> d)|Collection\<T>
| readCollection(Collection\<T> arg0, DataIn$Deserializer\<T> arg1)|Collection\<T>
| readDimPos()|BlockDimPos
| readDouble()|double
| readFloat()|float
| readIcon()|Icon
| readInt()|int
| readIntList()|IntList
| readItemStack()|ItemStack
| readJson()|JsonElement
| readLong()|long
| readMap(DataIn$Deserializer\<K> arg0, DataIn$Deserializer\<V> arg1)|Map\<K, V>
| readMap(Map\<K, V> arg0, DataIn$Deserializer\<K> arg1, DataIn$Deserializer\<V> arg2)|Map\<K, V>
| readNBT()|NBTTagCompound
| readNBTBase()|NBTBase
| readPos()|BlockPos
| readResourceLocation()|ResourceLocation
| readShort()|short
| readString()|String
| readTextComponent()|TextComponent
| readUnsignedByte()|short
| readUnsignedShort()|int
| readUUID()|UUID
| readVarInt()|int
| readVarLong()|long
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## DataOut

|Class
|--
|com.feed_the_beast.ftblib.lib.io.DataOut

---

|Extends
|--

---

|Fields|Type
|--|--
|  position|int

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeBlockState(BlockState b)|void
| writeBoolean(boolean b)|void
| writeByte(int i)|void
| writeBytes(byte[] b)|void
| writeBytes(byte[] arg0, int arg1, int arg2)|void
| writeCollection(Collection\<T> arg0, DataOut$Serializer\<T> arg1)|void
| writeDimPos(BlockDimPos b)|void
| writeDouble(double d)|void
| writeFloat(float f)|void
| writeIcon(Icon i)|void
| writeInt(int i)|void
| writeIntList(IntCollection i)|void
| writeItemStack(ItemStack i)|void
| writeJson(JsonElement j)|int
| writeLong(long l)|void
| writeMap(Map\<K, V> arg0, DataOut$Serializer\<K> arg1, DataOut$Serializer\<V> arg2)|void
| writeNBT(NBTTagCompound n)|void
| writeNBTBase(NBTBase n)|void
| writePos(Vec3i v)|void
| writeResourceLocation(ResourceLocation r)|void
| writeShort(int i)|void
| writeString(String s)|void
| writeTextComponent(TextComponent t)|void
| writeUUID(UUID u)|void
| writeVarInt(int i)|void
| writeVarLong(long l)|void

---

## IgnoreNBTIngredient

|Class
|--
|dev.latvian.kubejs.item.ingredient.IgnoreNBTIngredientJS

---

|Extends
|--
|Ingredient

---

|Fields|Type
|--|--
|  count|int
|  empty|boolean
|  first|ItemStack
|  stacks|Set\<ItemStack>
|  vanillaPredicate|Predicate\<ItemStack>

---

|Methods|Return Type
|--|--
| count(int i)|Ingredient
| filter(Ingredient i)|Ingredient
| not()|Ingredient
| test(ItemStack i)|boolean
| testVanilla(ItemStack i)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## FireworksJS$Explosion

|Class
|--
|dev.latvian.kubejs.world.FireworksJS$Explosion

---

|Extends
|--

---

|Fields|Type
|--|--
|  colors|IntOpenHashSet
|  fadeColors|IntOpenHashSet
|  flicker|boolean
|  shape|FireworksJS$Shape
|  trail|boolean

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityFireworkRocket

|Class
|--
|net.minecraft.entity.item.EntityFireworkRocket

---

|Extends
|--
|Entity

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_190534_ay|int
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_98038_p|boolean
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_110124_au()|UUID
| func_130014_f_()|World
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_190530_aW()|boolean
| func_191511_j()|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70676_i(float f)|Vec3d
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NBTBase

|Class
|--
|net.minecraft.nbt.NBTBase

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_74732_a()|byte
| func_74737_b()|NBTBase
| func_82582_d()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## JsonSerializable

|Interface
|--
|dev.latvian.kubejs.util.JsonSerializable

---

|Extends
|--

---

|Fields|Type
|--|--
|  json|JsonElement

---

|Methods|Return Type
|--|--

---

## MessageSender

|Interface
|--
|dev.latvian.kubejs.util.MessageSender

---

|Extends
|--

---

|Fields|Type
|--|--
|  displayName|Text
|  name|String

---

|Methods|Return Type
|--|--
| runCommand(String command) Runs command as if the sender was running it, ignoring permissions|int
| setStatusMessage(Text text) Set status message|void
| tell(Text text) Tell message in chat|void

---

## MinecraftServer

|Class
|--
|net.minecraft.server.MinecraftServer

---

|Extends
|--
|CommandSender
|Runnable
|ThreadListener
|SnooperInfo

---

|Fields|Type
|--|--
|  dataFixer|DataFixer
|  field_175589_i|Queue\<java.util.concurrent.FutureTask\<?>>
|  field_71302_d|String
|  field_71303_e|int
|  field_71304_b|Profiler
|  field_71305_c|WorldServer[]
|  field_71308_o|File
|  field_71311_j|long[]
|  field_71321_q|CommandManager
|  serverModName|String
|  worldTickTimes|Hashtable\<int, long[]>

---

|Methods|Return Type
|--|--
| func_104056_am()|boolean
| func_110454_ao()|Proxy
| func_110455_j()|int
| func_130014_f_()|World
| func_143006_e(int i)|void
| func_143007_ar()|int
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_147130_as()|MinecraftSessionService
| func_147132_au()|void
| func_147133_T()|String
| func_147134_at()|ServerStatusResponse
| func_147135_j()|EnumDifficulty
| func_147137_ag()|NetworkSystem
| func_147139_a(EnumDifficulty e)|void
| func_152344_a(Runnable r)|ListenableFuture\<Object>
| func_152345_ab()|boolean
| func_152357_F()|GameProfile[]
| func_152358_ax()|PlayerProfileCache
| func_152359_aw()|GameProfileRepository
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_175576_a(UUID u)|Entity
| func_175577_aI()|int
| func_175578_N()|boolean
| func_175579_a(World arg0, BlockPos arg1, EntityPlayer arg2)|boolean
| func_175580_aG()|int
| func_175581_ab()|String
| func_175582_h()|ServerCommandManager
| func_175584_a(String arg0, SaveHandler arg1)|void
| func_175586_a(Callable\<V> c)|ListenableFuture\<V>
| func_180425_c()|BlockPos
| func_180507_a_(String arg0, String arg1)|void
| func_181034_q()|boolean
| func_181035_ah()|boolean
| func_183002_r()|boolean
| func_184102_h()|MinecraftServer
| func_184103_al()|PlayerList
| func_184104_a(CommandSender arg0, String arg1, BlockPos arg2, boolean arg3)|List\<String>
| func_184105_a(PlayerList p)|void
| func_184106_y()|boolean
| func_184107_a(ServerStatusResponse s)|void
| func_184108_a(WorldServer w)|int
| func_184109_z()|File
| func_190518_ac()|boolean
| func_191949_aK()|AdvancementManager
| func_193030_aL()|FunctionManager
| func_193031_aM()|void
| func_70000_a(Snooper s)|void
| func_70001_b(Snooper s)|void
| func_70002_Q()|boolean
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_71187_D()|CommandManager
| func_71188_g(boolean b)|void
| func_71190_q()|void
| func_71191_d(int i)|void
| func_71193_K()|boolean
| func_71194_c(boolean b)|void
| func_71195_b_()|String
| func_71197_b()|boolean
| func_71199_h()|boolean
| func_71200_ad()|boolean
| func_71204_b(boolean b)|void
| func_71205_p(String s)|void
| func_71206_a(GameType arg0, boolean arg1)|String
| func_71207_Z()|int
| func_71209_f(String s)|File
| func_71213_z()|String[]
| func_71214_G()|String
| func_71217_p()|void
| func_71218_a(int i)|WorldServer
| func_71219_W()|boolean
| func_71220_V()|boolean
| func_71221_J()|String
| func_71222_d()|void
| func_71223_ag()|void
| func_71224_l(String s)|void
| func_71225_e()|boolean
| func_71228_a(CrashReport c)|void
| func_71229_d(boolean b)|void
| func_71230_b(CrashReport c)|CrashReport
| func_71231_X()|boolean
| func_71233_x()|int
| func_71235_a(GameType g)|void
| func_71236_h(String s)|void
| func_71237_c(String s)|void
| func_71238_n()|File
| func_71240_o()|void
| func_71241_aa()|boolean
| func_71242_L()|boolean
| func_71245_h(boolean b)|void
| func_71246_n(String s)|void
| func_71247_a(String arg0, String arg1, long arg2, WorldType arg3, String arg4)|void
| func_71249_w()|String
| func_71250_E()|KeyPair
| func_71251_e(boolean b)|void
| func_71253_a(KeyPair k)|void
| func_71254_M()|SaveFormat
| func_71255_r()|boolean
| func_71256_s()|void
| func_71257_f(boolean b)|void
| func_71259_af()|int
| func_71260_j()|void
| func_71261_m(String s)|void
| func_71262_S()|boolean
| func_71263_m()|void
| func_71264_H()|boolean
| func_71265_f()|GameType
| func_71266_T()|boolean
| func_71267_a(boolean b)|void
| func_71268_U()|boolean
| func_71270_I()|String
| func_71273_Y()|String
| func_71275_y()|int
| func_71278_l()|boolean
| func_71279_ae()|boolean
| func_80003_ah()|Snooper
| func_82356_Z()|boolean
| run()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ServerWorld

|Class
|--
|dev.latvian.kubejs.world.ServerWorldJS

---

|Extends
|--
|World

---

|Fields|Type
|--|--
|  data Temporary data, mods can attach objects to this|AttachedData
|  daytime|boolean
|  dimension|int
|  entities|EntityArrayList
|  gameRules|GameRules
|  localTime|long
|  minecraftWorld|World
|  overworld|boolean
|  players|EntityArrayList
|  raining|boolean
|  seed|long
|  server|Server
|  thundering|boolean
|  time|long

---

|Methods|Return Type
|--|--
| createEntity(Object o)|Entity
| createEntityList(Collection\<? extends net.minecraft.entity.Entity> c)|EntityArrayList
| createExplosion(double x, double y, double z)|Explosion
| getBlock(int x, int y, int z)|Block
| getBlock(BlockPos pos)|Block
| getBlock(TileEntity blockEntity)|Block
| getEntity(Entity e)|Entity
| getLivingEntity(Entity e)|LivingEntity
| getPlayer(Entity e)|Player
| getPlayerData(EntityPlayer e)|PlayerData
| getPlayerData(EntityPlayer e)|ServerPlayerData
| setRainStrength(float strength)|void
| spawnFireworks(double x, double y, double z, Fireworks properties)|void
| spawnLightning(double x, double y, double z, boolean effectOnly)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ScheduledEventCallback

|Interface
|--
|dev.latvian.kubejs.server.IScheduledEventCallback

---

|Extends
|--

---

|Methods|Return Type
|--|--
| onCallback(ScheduledEvent s)|void

---

## ScheduledEvent

|Class
|--
|dev.latvian.kubejs.server.ScheduledEvent

---

|Extends
|--

---

|Fields|Type
|--|--
|  data|Object
|  endTime|long
|  server|Server
|  timer|long
|  timerDuration|long
|  usingTicks|boolean

---

|Methods|Return Type
|--|--
| reschedule()|void
| reschedule(long timer)|ScheduledEvent
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Attribute

|Interface
|--
|net.minecraft.entity.ai.attributes.IAttribute

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_111108_a()|String
| func_111109_a(double d)|double
| func_111110_b()|double
| func_111111_c()|boolean
| func_180372_d()|Attribute

---

## AbstractAttributeMap

|Class
|--
|net.minecraft.entity.ai.attributes.AbstractAttributeMap

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_111146_a()|Collection\<AttributeInstance>
| func_111147_b(Multimap\<String, AttributeModifier> m)|void
| func_111148_a(Multimap\<String, AttributeModifier> m)|void
| func_111150_b(Attribute a)|AttributeInstance
| func_111151_a(Attribute a)|AttributeInstance
| func_111152_a(String s)|AttributeInstance
| func_180794_a(AttributeInstance a)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PotionEffect

|Class
|--
|net.minecraft.potion.PotionEffect

---

|Extends
|--
|Comparable

---

|Fields|Type
|--|--
|  curativeItems|List\<ItemStack>
|  field_188421_h|boolean
|  field_76460_b|int

---

|Methods|Return Type
|--|--
| addCurativeItem(ItemStack i)|void
| compareTo(Object o)|int
| compareTo(PotionEffect p)|int
| func_100011_g()|boolean
| func_100012_b(boolean b)|void
| func_188418_e()|boolean
| func_188419_a()|Potion
| func_76452_a(PotionEffect p)|void
| func_76453_d()|String
| func_76454_e()|int
| func_76455_a(EntityLivingBase e)|boolean
| func_76457_b(EntityLivingBase e)|void
| func_76458_c()|int
| func_76459_b()|int
| func_82719_a(NBTTagCompound n)|NBTTagCompound
| func_82720_e()|boolean
| isCurativeItem(ItemStack i)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ScoreCriteria

|Interface
|--
|net.minecraft.scoreboard.IScoreCriteria

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178790_c()|IScoreCriteria$EnumRenderType
| func_96636_a()|String
| func_96637_b()|boolean

---

## FoamFixWorldRemovable

|Interface
|--
|pl.asie.foamfix.coremod.patches.IFoamFixWorldRemovable

---

|Extends
|--

---

|Methods|Return Type
|--|--
| foamfix_removeUnloadedEntities()|void

---

## BlockSnapshot

|Class
|--
|net.minecraftforge.common.util.BlockSnapshot

---

|Extends
|--

---

|Fields|Type
|--|--
|  currentBlock|BlockState
|  dimId|int
|  flag|int
|  meta|int
|  nbt|NBTTagCompound
|  pos|BlockPos
|  registryName|ResourceLocation
|  replacedBlock|BlockState
|  tileEntity|TileEntity
|  world|World

---

|Methods|Return Type
|--|--
| restore()|boolean
| restore(boolean b)|boolean
| restore(boolean arg0, boolean arg1)|boolean
| restoreToLocation(World arg0, BlockPos arg1, boolean arg2, boolean arg3)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeToNBT(NBTTagCompound n)|void

---

## VillageCollection

|Class
|--
|net.minecraft.village.VillageCollection

---

|Extends
|--
|WorldSavedData

---

|Fields|Type
|--|--
|  field_76190_i|String

---

|Methods|Return Type
|--|--
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_176056_a(BlockPos arg0, int arg1)|Village
| func_176060_a(BlockPos b)|void
| func_189551_b(NBTTagCompound n)|NBTTagCompound
| func_75540_b()|List\<Village>
| func_75544_a()|void
| func_76184_a(NBTTagCompound n)|void
| func_76185_a()|void
| func_76186_a(boolean b)|void
| func_76188_b()|boolean
| func_82566_a(World w)|void
| serializeNBT()|NBTBase
| serializeNBT()|NBTTagCompound
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WorldProvider

|Class
|--
|net.minecraft.world.WorldProvider

---

|Extends
|--

---

|Fields|Type
|--|--
|  actualHeight|int
|  cloudRenderer|IRenderHandler
|  currentMoonPhaseFactor|float
|  daytime|boolean
|  dimension|int
|  field_76577_b|WorldType
|  field_82913_c|String
|  height|int
|  horizon|double
|  movementFactor|double
|  musicType|MusicTicker$MusicType
|  randomizedSpawnPoint|BlockPos
|  saveFolder|String
|  seed|long
|  skyRenderer|IRenderHandler
|  spawnPoint|BlockPos
|  weatherRenderer|IRenderHandler
|  worldTime|long

---

|Methods|Return Type
|--|--
| calculateInitialWeather()|void
| canBlockFreeze(BlockPos arg0, boolean arg1)|boolean
| canDoLightning(Chunk c)|boolean
| canDoRainSnowIce(Chunk c)|boolean
| canMineBlock(EntityPlayer arg0, BlockPos arg1)|boolean
| canSleepAt(EntityPlayer arg0, BlockPos arg1)|WorldProvider$WorldSleepResult
| canSnowAt(BlockPos arg0, boolean arg1)|boolean
| func_177495_o()|boolean
| func_177496_h()|BlockPos
| func_177497_p()|float[]
| func_177499_m()|BiomeProvider
| func_177500_n()|boolean
| func_177501_r()|WorldBorder
| func_186056_c(int arg0, int arg1)|boolean
| func_186057_q()|void
| func_186058_p()|DimensionType
| func_186059_r()|void
| func_186060_c()|ChunkGenerator
| func_186061_a(EntityPlayerMP e)|void
| func_186062_b(EntityPlayerMP e)|void
| func_191066_m()|boolean
| func_76557_i()|int
| func_76558_a(World w)|void
| func_76559_b(long l)|int
| func_76560_a(float arg0, float arg1)|float[]
| func_76561_g()|boolean
| func_76562_b(float arg0, float arg1)|Vec3d
| func_76563_a(long arg0, float arg1)|float
| func_76565_k()|double
| func_76566_a(int arg0, int arg1)|boolean
| func_76567_e()|boolean
| func_76568_b(int arg0, int arg1)|boolean
| func_76569_d()|boolean
| func_76571_f()|float
| getBiomeForCoords(BlockPos b)|Biome
| getCloudColor(float f)|Vec3d
| getLightmapColors(float arg0, float arg1, float arg2, float arg3, float[] arg4)|void
| getRespawnDimension(EntityPlayerMP e)|int
| getSkyColor(Entity arg0, float arg1)|Vec3d
| getStarBrightness(float f)|float
| getSunBrightness(float f)|float
| getSunBrightnessFactor(float f)|float
| initCapabilities()|CapabilityProvider
| isBlockHighHumidity(BlockPos b)|boolean
| resetRainAndThunder()|void
| setAllowedSpawnTypes(boolean arg0, boolean arg1)|void
| shouldClientCheckLighting()|boolean
| shouldMapSpin(String arg0, double arg1, double arg2, double arg3)|boolean
| updateWeather()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ChunkPos

|Class
|--
|net.minecraft.util.math.ChunkPos

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_77275_b|int
|  field_77276_a|int

---

|Methods|Return Type
|--|--
| func_180330_f()|int
| func_180331_a(int arg0, int arg1, int arg2)|BlockPos
| func_180332_e()|int
| func_180333_d()|int
| func_180334_c()|int
| func_185327_a(Entity e)|double
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ForgeChunkManager$Ticket

|Class
|--
|net.minecraftforge.common.ForgeChunkManager$Ticket

---

|Extends
|--

---

|Fields|Type
|--|--
|  chunkList|ImmutableSet\<ChunkPos>
|  chunkListDepth|int
|  entity|Entity
|  maxChunkListDepth|int
|  modData|NBTTagCompound
|  modId|String
|  playerName|String
|  playerTicket|boolean
|  type|ForgeChunkManager$Type
|  world|World

---

|Methods|Return Type
|--|--
| bindEntity(Entity e)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MapStorage

|Class
|--
|net.minecraft.world.storage.MapStorage

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_75742_a(Class\<? extends net.minecraft.world.storage.WorldSavedData> arg0, String arg1)|WorldSavedData
| func_75743_a(String s)|int
| func_75744_a()|void
| func_75745_a(String arg0, WorldSavedData arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumCreatureType

|Class
|--
|net.minecraft.entity.EnumCreatureType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_75598_a()|Class\<? extends net.minecraft.entity.passive.IAnimals>
| func_75599_d()|boolean
| func_75601_b()|int
| func_82705_e()|boolean
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WorldType

|Class
|--
|net.minecraft.world.WorldType

---

|Extends
|--

---

|Fields|Type
|--|--
|  cloudHeight|float
|  customizable|boolean

---

|Methods|Return Type
|--|--
| func_151357_h()|boolean
| func_151358_j()|WorldType
| func_151359_c()|String
| func_77125_e()|boolean
| func_77126_d()|boolean
| func_77127_a()|String
| func_77128_b()|String
| func_77131_c()|int
| func_77132_a(int i)|WorldType
| func_82747_f()|int
| getBiomeLayer(long arg0, GenLayer arg1, ChunkGeneratorSettings arg2)|GenLayer
| getBiomeProvider(World w)|BiomeProvider
| getChunkGenerator(World arg0, String arg1)|ChunkGenerator
| getHorizon(World w)|double
| getMinimumSpawnHeight(World w)|int
| getSpawnFuzz(WorldServer arg0, MinecraftServer arg1)|int
| handleSlimeSpawnReduction(Random arg0, World arg1)|boolean
| onCustomizeButton(Minecraft arg0, GuiCreateWorld arg1)|void
| onGUICreateWorldPress()|void
| voidFadeMagnitude()|double
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## StructureBoundingBox

|Class
|--
|net.minecraft.world.gen.structure.StructureBoundingBox

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_78892_f|int
|  field_78893_d|int
|  field_78894_e|int
|  field_78895_b|int
|  field_78896_c|int
|  field_78897_a|int

---

|Methods|Return Type
|--|--
| func_151535_h()|NBTTagIntArray
| func_175896_b()|Vec3i
| func_175898_b(Vec3i v)|boolean
| func_78880_d()|int
| func_78882_c()|int
| func_78883_b()|int
| func_78884_a(StructureBoundingBox s)|boolean
| func_78885_a(int arg0, int arg1, int arg2, int arg3)|boolean
| func_78886_a(int arg0, int arg1, int arg2)|void
| func_78888_b(StructureBoundingBox s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumSkyBlock

|Class
|--
|net.minecraft.world.EnumSkyBlock

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>
|  field_77198_c|int

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## DifficultyInstance

|Class
|--
|net.minecraft.world.DifficultyInstance

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_180168_b()|float
| func_180170_c()|float
| func_193845_a(float f)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumDifficulty

|Class
|--
|net.minecraft.world.EnumDifficulty

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_151525_a()|int
| func_151526_b()|String
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumParticleTypes

|Class
|--
|net.minecraft.util.EnumParticleTypes

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_179344_e()|boolean
| func_179345_d()|int
| func_179346_b()|String
| func_179348_c()|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NextTickListEntry

|Class
|--
|net.minecraft.world.NextTickListEntry

---

|Extends
|--
|Comparable

---

|Fields|Type
|--|--
|  field_180282_a|BlockPos
|  field_77180_e|long
|  field_82754_f|int

---

|Methods|Return Type
|--|--
| compareTo(NextTickListEntry n)|int
| compareTo(Object o)|int
| func_151351_a()|Block
| func_77176_a(long l)|NextTickListEntry
| func_82753_a(int i)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WorldBorder

|Class
|--
|net.minecraft.world.border.WorldBorder

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_177721_g()|double
| func_177722_l()|int
| func_177723_b(int i)|void
| func_177724_b(double d)|void
| func_177725_a(int i)|void
| func_177726_b()|double
| func_177727_n()|double
| func_177728_d()|double
| func_177729_b(double arg0, double arg1)|double
| func_177730_a(ChunkPos c)|boolean
| func_177731_f()|double
| func_177732_i()|long
| func_177733_e()|double
| func_177734_a()|EnumBorderStatus
| func_177736_c()|double
| func_177737_a(BorderListener b)|void
| func_177738_a(double arg0, double arg1, long arg2)|void
| func_177739_c(double arg0, double arg1)|void
| func_177740_p()|int
| func_177741_h()|double
| func_177742_m()|double
| func_177743_a(AxisAlignedBB a)|boolean
| func_177744_c(double d)|void
| func_177745_a(Entity e)|double
| func_177746_a(BlockPos b)|boolean
| func_177747_c(int i)|void
| func_177748_q()|int
| func_177749_o()|double
| func_177750_a(double d)|void
| func_177751_j()|double
| removeListener(BorderListener b)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Chunk

|Class
|--
|net.minecraft.world.chunk.Chunk

---

|Extends
|--
|CapabilityProvider

---

|Fields|Type
|--|--
|  capabilities|CapabilityDispatcher
|  field_189550_d|boolean
|  field_76634_f|int[]
|  field_76635_g|int
|  field_76638_b|int[]
|  field_76647_h|int
|  field_76652_q|ExtendedBlockStorage[]

---

|Methods|Return Type
|--|--
| func_150802_k()|boolean
| func_150804_b(boolean b)|void
| func_150809_p()|void
| func_150813_a(TileEntity t)|void
| func_177409_g(boolean b)|void
| func_177410_o()|boolean
| func_177411_a(BlockPos arg0, BiomeProvider arg1)|Biome
| func_177412_p()|World
| func_177413_a(EnumSkyBlock arg0, BlockPos arg1)|int
| func_177414_a(Entity arg0, AxisAlignedBB arg1, List\<Entity> arg2, Predicate\<? super net.minecraft.entity.Entity> arg3)|void
| func_177415_c(long l)|void
| func_177416_w()|long
| func_177417_c(boolean b)|void
| func_177419_t()|boolean
| func_177420_a(int[] i)|void
| func_177421_e(boolean b)|void
| func_177423_u()|boolean
| func_177424_a(BlockPos arg0, Chunk$EnumCreateEntityType arg1)|TileEntity
| func_177425_e(BlockPos b)|void
| func_177426_a(BlockPos arg0, TileEntity arg1)|void
| func_177427_f(boolean b)|void
| func_177429_s()|ClassInheritanceMultiMap[]
| func_177430_a(Class\<? extends T> arg0, AxisAlignedBB arg1, List\<T> arg2, Predicate\<? super T> arg3)|void
| func_177431_a(EnumSkyBlock arg0, BlockPos arg1, int arg2)|void
| func_177432_b(long l)|void
| func_177433_f(BlockPos b)|int
| func_177434_r()|Map\<BlockPos, TileEntity>
| func_177435_g(BlockPos b)|BlockState
| func_177436_a(BlockPos arg0, BlockState arg1)|BlockState
| func_177437_b(BlockPos b)|int
| func_177440_h(BlockPos b)|BlockPos
| func_177442_v()|int
| func_177443_a(BlockPos arg0, int arg1)|int
| func_177444_d(BlockPos b)|boolean
| func_177445_q()|int[]
| func_177446_d(boolean b)|void
| func_186030_a(ChunkProvider arg0, ChunkGenerator arg1)|void
| func_186032_a(int arg0, int arg1, int arg2)|BlockState
| func_186033_a(PacketBuffer arg0, int arg1, boolean arg2)|void
| func_186035_j()|boolean
| func_76587_i()|ExtendedBlockStorage[]
| func_76594_o()|void
| func_76595_e(int arg0, int arg1)|void
| func_76600_a(int arg0, int arg1)|boolean
| func_76601_a(boolean b)|boolean
| func_76602_a(ExtendedBlockStorage[] e)|void
| func_76603_b()|void
| func_76605_m()|byte[]
| func_76606_c(int arg0, int arg1)|boolean
| func_76608_a(Entity arg0, int arg1)|void
| func_76611_b(int arg0, int arg1)|int
| func_76612_a(Entity e)|void
| func_76613_n()|void
| func_76615_h(int arg0, int arg1, int arg2)|void
| func_76616_a(byte[] b)|void
| func_76617_a(long l)|Random
| func_76621_g()|boolean
| func_76622_b(Entity e)|void
| func_76623_d()|void
| func_76625_h()|int
| func_76630_e()|void
| func_76631_c()|void
| func_76632_l()|ChunkPos
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| removeInvalidTileEntity(BlockPos b)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Biome

|Class
|--
|net.minecraft.world.biome.Biome

---

|Extends
|--
|IForgeRegistryEntry$Impl

---

|Fields|Type
|--|--
|  delegate|RegistryDelegate\<T>
|  field_76752_A|BlockState
|  field_76753_B|BlockState
|  field_76760_I|BiomeDecorator
|  field_76791_y|String
|  registryName|ResourceLocation
|  registryType|Class\<T>
|  waterColorMultiplier|int

---

|Methods|Return Type
|--|--
| addDefaultFlowers()|void
| addFlower(BlockState arg0, int arg1)|void
| func_150559_j()|boolean
| func_150561_m()|Biome$TempCategory
| func_150562_l()|Class\<? extends net.minecraft.world.biome.Biome>
| func_150567_a(Random r)|WorldGenAbstractTree
| func_180622_a(World arg0, Random arg1, ChunkPrimer arg2, int arg3, int arg4, double arg5)|void
| func_180623_a(Random arg0, BlockPos arg1)|BlockFlower$EnumFlowerType
| func_180624_a(World arg0, Random arg1, BlockPos arg2)|void
| func_180625_c(BlockPos b)|int
| func_180626_a(BlockPos b)|float
| func_180627_b(BlockPos b)|int
| func_180628_b(World arg0, Random arg1, ChunkPrimer arg2, int arg3, int arg4, double arg5)|void
| func_185352_i()|boolean
| func_185353_n()|float
| func_185355_j()|float
| func_185359_l()|String
| func_185360_m()|float
| func_185361_o()|int
| func_185363_b()|boolean
| func_76727_i()|float
| func_76729_a()|BiomeDecorator
| func_76730_b(Random r)|WorldGenerator
| func_76731_a(float f)|int
| func_76736_e()|boolean
| func_76738_d()|boolean
| func_76741_f()|float
| func_76746_c()|boolean
| func_76747_a(EnumCreatureType e)|List\<Biome$SpawnListEntry>
| getModdedBiomeDecorator(BiomeDecorator b)|BiomeDecorator
| getModdedBiomeFoliageColor(int i)|int
| getModdedBiomeGrassColor(int i)|int
| plantFlower(World arg0, Random arg1, BlockPos arg2)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SoundCategory

|Class
|--
|net.minecraft.util.SoundCategory

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_187948_a()|String
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Packet

|Interface
|--
|net.minecraft.network.Packet

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void

---

## LootTableManager

|Class
|--
|net.minecraft.world.storage.loot.LootTableManager

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_186527_c|LoadingCache\<ResourceLocation, LootTable>

---

|Methods|Return Type
|--|--
| func_186521_a(ResourceLocation r)|LootTable
| func_186522_a()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WorldSavedData

|Class
|--
|net.minecraft.world.storage.WorldSavedData

---

|Extends
|--
|NBTSerializable

---

|Fields|Type
|--|--
|  field_76190_i|String

---

|Methods|Return Type
|--|--
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_189551_b(NBTTagCompound n)|NBTTagCompound
| func_76184_a(NBTTagCompound n)|void
| func_76185_a()|void
| func_76186_a(boolean b)|void
| func_76188_b()|boolean
| serializeNBT()|NBTBase
| serializeNBT()|NBTTagCompound
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WorldEventListener

|Interface
|--
|net.minecraft.world.IWorldEventListener

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_147585_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_174959_b(BlockPos b)|void
| func_180439_a(EntityPlayer arg0, int arg1, BlockPos arg2, int arg3)|void
| func_180440_a(int arg0, BlockPos arg1, int arg2)|void
| func_180441_b(int arg0, BlockPos arg1, int arg2)|void
| func_180442_a(int arg0, boolean arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, int[] arg8)|void
| func_184375_a(EntityPlayer arg0, SoundEvent arg1, SoundCategory arg2, double arg3, double arg4, double arg5, float arg6, float arg7)|void
| func_184376_a(World arg0, BlockPos arg1, BlockState arg2, BlockState arg3, int arg4)|void
| func_184377_a(SoundEvent arg0, BlockPos arg1)|void
| func_190570_a(int arg0, boolean arg1, boolean arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, int[] arg9)|void
| func_72703_a(Entity e)|void
| func_72709_b(Entity e)|void

---

## SaveHandler

|Interface
|--
|net.minecraft.world.storage.ISaveHandler

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_186340_h()|TemplateManager
| func_75755_a(WorldInfo arg0, NBTTagCompound arg1)|void
| func_75756_e()|PlayerFileData
| func_75757_d()|WorldInfo
| func_75758_b(String s)|File
| func_75759_a()|void
| func_75761_a(WorldInfo w)|void
| func_75762_c()|void
| func_75763_a(WorldProvider w)|ChunkLoader
| func_75765_b()|File

---

## ChunkProvider

|Interface
|--
|net.minecraft.world.chunk.IChunkProvider

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_186025_d(int arg0, int arg1)|Chunk
| func_186026_b(int arg0, int arg1)|Chunk
| func_191062_e(int arg0, int arg1)|boolean
| func_73148_d()|String
| func_73156_b()|boolean

---

## WorldInfo

|Class
|--
|net.minecraft.world.storage.WorldInfo

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_176118_b(double d)|void
| func_176119_g(boolean b)|void
| func_176120_C()|double
| func_176121_c(boolean b)|void
| func_176122_j(int i)|void
| func_176123_z()|boolean
| func_176124_d(double d)|void
| func_176125_f(double d)|void
| func_176126_D()|double
| func_176127_a(WorldSettings w)|void
| func_176128_f(boolean b)|void
| func_176129_e(double d)|void
| func_176130_y()|EnumDifficulty
| func_176131_J()|int
| func_176132_G()|double
| func_176133_A()|int
| func_176134_F()|long
| func_176135_e(long l)|void
| func_176136_k(int i)|void
| func_176137_E()|double
| func_176138_H()|double
| func_176139_K()|int
| func_176140_I()|double
| func_176141_c(double d)|void
| func_176142_i(int i)|void
| func_176143_a(BlockPos b)|void
| func_176144_a(EnumDifficulty e)|void
| func_176145_a(double d)|void
| func_180783_e(boolean b)|void
| func_186343_L()|boolean
| func_186344_K()|int
| func_186345_a(DimensionType arg0, NBTTagCompound arg1)|void
| func_186346_M()|String
| func_186347_a(DimensionType d)|NBTTagCompound
| func_76056_b(int i)|void
| func_76057_l()|long
| func_76058_a(int i)|void
| func_76059_o()|boolean
| func_76060_a(GameType g)|void
| func_76061_m()|boolean
| func_76062_a(String s)|void
| func_76063_b()|long
| func_76065_j()|String
| func_76067_t()|WorldType
| func_76068_b(long l)|void
| func_76069_a(boolean b)|void
| func_76070_v()|boolean
| func_76071_n()|int
| func_76072_h()|NBTTagCompound
| func_76073_f()|long
| func_76074_e()|int
| func_76075_d()|int
| func_76077_q()|GameType
| func_76078_e(int i)|void
| func_76079_c()|int
| func_76080_g(int i)|void
| func_76082_a(NBTTagCompound n)|NBTTagCompound
| func_76083_p()|int
| func_76084_b(boolean b)|void
| func_76085_a(WorldType w)|void
| func_76086_u()|boolean
| func_76087_c(int i)|void
| func_76088_k()|int
| func_76089_r()|boolean
| func_76090_f(int i)|void
| func_76091_d(boolean b)|void
| func_76092_g()|long
| func_76093_s()|boolean
| func_82571_y()|String
| func_82572_b(long l)|void
| func_82573_f()|long
| func_82574_x()|GameRules
| func_85118_a(CrashReportCategory c)|void
| getAdditionalProperty(String s)|NBTBase
| getDimensionData(int i)|NBTTagCompound
| setAdditionalProperties(Map\<String, NBTBase> m)|void
| setDimensionData(int arg0, NBTTagCompound arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CrashReportCategory

|Class
|--
|net.minecraft.crash.CrashReportCategory

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_147152_a()|StackTraceElement[]
| func_189529_a(String arg0, CrashReportDetail\<String> arg1)|void
| func_71499_a(String arg0, Throwable arg1)|void
| func_71507_a(String arg0, Object arg1)|void
| func_85069_a(StackTraceElement arg0, StackTraceElement arg1)|boolean
| func_85070_b(int i)|void
| func_85072_a(StringBuilder s)|void
| func_85073_a(int i)|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BiomeProvider

|Class
|--
|net.minecraft.world.biome.BiomeProvider

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_180300_a(BlockPos arg0, Biome arg1)|Biome
| func_180630_a(int arg0, int arg1, int arg2, List\<Biome> arg3, Random arg4)|BlockPos
| func_180631_a(BlockPos b)|Biome
| func_190943_d()|Biome
| func_190944_c()|boolean
| func_76931_a(Biome[] arg0, int arg1, int arg2, int arg3, int arg4, boolean arg5)|Biome[]
| func_76932_a()|List\<Biome>
| func_76933_b(Biome[] arg0, int arg1, int arg2, int arg3, int arg4)|Biome[]
| func_76937_a(Biome[] arg0, int arg1, int arg2, int arg3, int arg4)|Biome[]
| func_76938_b()|void
| func_76939_a(float arg0, int arg1)|float
| func_76940_a(int arg0, int arg1, int arg2, List\<Biome> arg3)|boolean
| getModdedBiomeGenerators(WorldType arg0, long arg1, GenLayer[] arg2)|GenLayer[]
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GameRules

|Class
|--
|net.minecraft.world.GameRules

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_180262_a(String arg0, String arg1, GameRules$ValueType arg2)|void
| func_180263_c(String s)|int
| func_180264_a(String arg0, GameRules$ValueType arg1)|boolean
| func_82763_b()|String[]
| func_82764_b(String arg0, String arg1)|void
| func_82765_e(String s)|boolean
| func_82766_b(String s)|boolean
| func_82767_a(String s)|String
| func_82768_a(NBTTagCompound n)|void
| func_82770_a()|NBTTagCompound
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Scoreboard

|Class
|--
|net.minecraft.scoreboard.Scoreboard

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_151392_a(String arg0, String arg1)|boolean
| func_178819_b(String arg0, ScoreObjective arg1)|boolean
| func_178820_a(String arg0, ScoreObjective arg1)|void
| func_178822_d(String arg0, ScoreObjective arg1)|void
| func_181140_a(Entity e)|void
| func_96508_e(String s)|ScorePlayerTeam
| func_96509_i(String s)|ScorePlayerTeam
| func_96510_d(String s)|Map\<ScoreObjective, Score>
| func_96511_d(ScorePlayerTeam s)|void
| func_96512_b(String arg0, ScorePlayerTeam arg1)|void
| func_96513_c(ScorePlayerTeam s)|void
| func_96514_c()|Collection\<ScoreObjective>
| func_96516_a(String s)|void
| func_96518_b(String s)|ScoreObjective
| func_96519_k(ScoreObjective s)|void
| func_96520_a(ScoreCriteria s)|Collection\<ScoreObjective>
| func_96522_a(ScoreObjective s)|void
| func_96523_a(ScorePlayerTeam s)|void
| func_96524_g(String s)|boolean
| func_96525_g()|Collection\<ScorePlayerTeam>
| func_96526_d()|Collection\<String>
| func_96527_f(String s)|ScorePlayerTeam
| func_96528_e()|Collection\<Score>
| func_96529_a(String arg0, ScoreObjective arg1)|Score
| func_96530_a(int arg0, ScoreObjective arg1)|void
| func_96531_f()|Collection\<String>
| func_96532_b(ScoreObjective s)|void
| func_96533_c(ScoreObjective s)|void
| func_96534_i(ScoreObjective s)|Collection\<Score>
| func_96535_a(String arg0, ScoreCriteria arg1)|ScoreObjective
| func_96536_a(Score s)|void
| func_96538_b(ScorePlayerTeam s)|void
| func_96539_a(int i)|ScoreObjective
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Capability

|Class
|--
|net.minecraftforge.common.capabilities.Capability

---

|Extends
|--

---

|Fields|Type
|--|--
|  defaultInstance|Object
|  name|String
|  storage|Capability$IStorage\<T>

---

|Methods|Return Type
|--|--
| cast(Object o)|Object
| readNBT(Object arg0, EnumFacing arg1, NBTBase arg2)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeNBT(Object arg0, EnumFacing arg1)|NBTBase

---

## CountingMap$Entry

|Class
|--
|dev.latvian.kubejs.util.CountingMap$Entry

---

|Extends
|--
|Comparable

---

|Fields|Type
|--|--
|  key|Object
|  value|long

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(CountingMap$Entry c)|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumEnchantmentType

|Class
|--
|net.minecraft.enchantment.EnumEnchantmentType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_77557_a(Item i)|boolean
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Property

|Interface
|--
|net.minecraft.block.properties.IProperty

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_177699_b()|Class\<T>
| func_177700_c()|Collection\<T>
| func_177701_a()|String
| func_177702_a(Comparable c)|String
| func_185929_b(String s)|Optional\<T>

---

## Particle

|Class
|--
|net.minecraft.client.particle.Particle

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_187123_c|double
|  field_187124_d|double
|  field_187125_e|double
|  field_187126_f|double
|  field_187127_g|double
|  field_187128_h|double
|  field_187129_i|double
|  field_187130_j|double
|  field_187131_k|double

---

|Methods|Return Type
|--|--
| func_180434_a(BufferBuilder arg0, Entity arg1, float arg2, float arg3, float arg4, float arg5, float arg6, float arg7)|void
| func_187108_a(AxisAlignedBB a)|void
| func_187109_b(double arg0, double arg1, double arg2)|void
| func_187110_a(double arg0, double arg1, double arg2)|void
| func_187111_c()|boolean
| func_187112_i()|void
| func_187113_k()|boolean
| func_187114_a(int i)|void
| func_187116_l()|AxisAlignedBB
| func_187117_a(TextureAtlasSprite t)|void
| func_189213_a()|void
| func_189214_a(float f)|int
| func_70534_d()|float
| func_70535_g()|float
| func_70536_a(int i)|void
| func_70537_b()|int
| func_70538_b(float arg0, float arg1, float arg2)|void
| func_70541_f(float f)|Particle
| func_70542_f()|float
| func_70543_e(float f)|Particle
| func_82338_g(float f)|void
| func_94053_h()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ParticleFactory

|Interface
|--
|net.minecraft.client.particle.IParticleFactory

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178902_a(int arg0, World arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, int[] arg8)|Particle

---

## BlockBehaviors

|Interface
|--
|net.minecraft.block.state.IBlockBehaviors

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_189546_a(World arg0, BlockPos arg1, Block arg2, BlockPos arg3)|void
| func_189547_a(World arg0, BlockPos arg1, int arg2, int arg3)|boolean

---

## BlockProperties

|Interface
|--
|net.minecraft.block.state.IBlockProperties

---

|Extends
|--

---

|Methods|Return Type
|--|--
| doesSideBlockChestOpening(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean
| doesSideBlockRendering(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean
| func_185887_b(World arg0, BlockPos arg1)|float
| func_185888_a(World arg0, BlockPos arg1)|int
| func_185889_a(BlockAccess arg0, BlockPos arg1)|int
| func_185890_d(BlockAccess arg0, BlockPos arg1)|AxisAlignedBB
| func_185891_c()|int
| func_185892_j()|float
| func_185893_b(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|int
| func_185894_c(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean
| func_185895_e()|boolean
| func_185896_q()|boolean
| func_185897_m()|boolean
| func_185898_k()|boolean
| func_185899_b(BlockAccess arg0, BlockPos arg1)|BlockState
| func_185900_c(BlockAccess arg0, BlockPos arg1)|AxisAlignedBB
| func_185901_i()|EnumBlockRenderType
| func_185902_a(Mirror m)|BlockState
| func_185903_a(EntityPlayer arg0, World arg1, BlockPos arg2)|float
| func_185904_a()|Material
| func_185905_o()|EnumPushReaction
| func_185906_d()|int
| func_185907_a(Rotation r)|BlockState
| func_185908_a(World arg0, BlockPos arg1, AxisAlignedBB arg2, List\<AxisAlignedBB> arg3, Entity arg4, boolean arg5)|void
| func_185909_g(BlockAccess arg0, BlockPos arg1)|MapColor
| func_185910_a(World arg0, BlockPos arg1, Vec3d arg2, Vec3d arg3)|RayTraceResult
| func_185911_a(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|int
| func_185912_n()|boolean
| func_185913_b()|boolean
| func_185914_p()|boolean
| func_185915_l()|boolean
| func_185916_f()|boolean
| func_185917_h()|boolean
| func_185918_c(World arg0, BlockPos arg1)|AxisAlignedBB
| func_189884_a(Entity e)|boolean
| func_191057_i()|boolean
| func_191058_s()|boolean
| func_191059_e(BlockAccess arg0, BlockPos arg1)|Vec3d
| func_193401_d(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|BlockFaceShape
| getLightOpacity(BlockAccess arg0, BlockPos arg1)|int
| getLightValue(BlockAccess arg0, BlockPos arg1)|int
| isSideSolid(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean

---

## RayTraceResult$Type

|Class
|--
|net.minecraft.util.math.RayTraceResult$Type

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Teleporter

|Class
|--
|net.minecraft.world.Teleporter

---

|Extends
|--
|Teleporter

---

|Fields|Type
|--|--
|  vanilla|boolean

---

|Methods|Return Type
|--|--
| func_180266_a(Entity arg0, float arg1)|void
| func_180620_b(Entity arg0, float arg1)|boolean
| func_85188_a(Entity e)|boolean
| func_85189_a(long l)|void
| placeEntity(World arg0, Entity arg1, float arg2)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Biome$SpawnListEntry

|Class
|--
|net.minecraft.world.biome.Biome$SpawnListEntry

---

|Extends
|--
|WeightedRandom$Item

---

|Fields|Type
|--|--
|  field_76292_a|int
|  field_76299_d|int
|  field_76300_b|Class\<? extends net.minecraft.entity.EntityLiving>
|  field_76301_c|int

---

|Methods|Return Type
|--|--
| newInstance(World w)|EntityLiving
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TemplateManager

|Class
|--
|net.minecraft.world.gen.structure.template.TemplateManager

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_186235_b(ResourceLocation r)|boolean
| func_186237_a(MinecraftServer arg0, ResourceLocation arg1)|Template
| func_186238_c(MinecraftServer arg0, ResourceLocation arg1)|boolean
| func_189941_a(ResourceLocation r)|void
| func_189942_b(MinecraftServer arg0, ResourceLocation arg1)|Template
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PlayerChunkMap

|Class
|--
|net.minecraft.server.management.PlayerChunkMap

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_152621_a(int arg0, int arg1)|boolean
| func_152622_a(int i)|void
| func_180244_a(BlockPos b)|void
| func_187300_b()|Iterator\<Chunk>
| func_187301_b(int arg0, int arg1)|PlayerChunkMapEntry
| func_187304_a(PlayerChunkMapEntry p)|void
| func_187305_b(PlayerChunkMapEntry p)|void
| func_72683_a(EntityPlayerMP e)|void
| func_72685_d(EntityPlayerMP e)|void
| func_72688_a()|WorldServer
| func_72693_b()|void
| func_72694_a(EntityPlayerMP arg0, int arg1, int arg2)|boolean
| func_72695_c(EntityPlayerMP e)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AdvancementManager

|Class
|--
|net.minecraft.advancements.AdvancementManager

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_192778_a(ResourceLocation r)|Advancement
| func_192779_a()|void
| func_192780_b()|Iterable\<Advancement>
| func_193767_b()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## FunctionManager

|Class
|--
|net.minecraft.advancements.FunctionManager

---

|Extends
|--
|Tickable

---

|Methods|Return Type
|--|--
| func_193058_a(ResourceLocation r)|FunctionObject
| func_193059_f()|void
| func_193062_a()|CommandManager
| func_193065_c()|int
| func_193066_d()|Map\<ResourceLocation, FunctionObject>
| func_194019_a(FunctionObject arg0, CommandSender arg1)|int
| func_73660_a()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ChunkProviderServer

|Class
|--
|net.minecraft.world.gen.ChunkProviderServer

---

|Extends
|--
|ChunkProvider

---

|Fields|Type
|--|--
|  field_186029_c|ChunkGenerator
|  field_73244_f|Long2ObjectMap\<Chunk>
|  field_73247_e|ChunkLoader
|  field_73251_h|WorldServer

---

|Methods|Return Type
|--|--
| func_104112_b()|void
| func_177458_a(EnumCreatureType arg0, BlockPos arg1)|List\<Biome$SpawnListEntry>
| func_180513_a(World arg0, String arg1, BlockPos arg2, boolean arg3)|BlockPos
| func_186025_d(int arg0, int arg1)|Chunk
| func_186026_b(int arg0, int arg1)|Chunk
| func_186027_a(boolean b)|boolean
| func_186028_c(int arg0, int arg1)|Chunk
| func_189548_a()|Collection\<Chunk>
| func_189549_a(Chunk c)|void
| func_191062_e(int arg0, int arg1)|boolean
| func_193413_a(World arg0, String arg1, BlockPos arg2)|boolean
| func_73148_d()|String
| func_73149_a(int arg0, int arg1)|boolean
| func_73152_e()|int
| func_73156_b()|boolean
| func_73157_c()|boolean
| func_73240_a()|void
| loadChunk(int arg0, int arg1, Runnable arg2)|Chunk
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityTracker

|Class
|--
|net.minecraft.entity.EntityTracker

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_151247_a(Entity arg0, Packet\<?> arg1)|void
| func_151248_b(Entity arg0, Packet\<?> arg1)|void
| func_180245_a(EntityPlayerMP e)|void
| func_187252_a(int i)|void
| func_72785_a(Entity arg0, int arg1, int arg2, boolean arg3)|void
| func_72786_a(Entity e)|void
| func_72787_a(EntityPlayerMP e)|void
| func_72788_a()|void
| func_72790_b(Entity e)|void
| func_72791_a(Entity arg0, int arg1, int arg2)|void
| func_85172_a(EntityPlayerMP arg0, Chunk arg1)|void
| getTrackingPlayers(Entity e)|Set\<? extends net.minecraft.entity.player.EntityPlayer>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ProgressUpdate

|Interface
|--
|net.minecraft.util.IProgressUpdate

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_146586_a()|void
| func_73718_a(int i)|void
| func_73719_c(String s)|void
| func_73720_a(String s)|void
| func_73721_b(String s)|void

---

## EntityDataManager

|Class
|--
|net.minecraft.network.datasync.EntityDataManager

---

|Extends
|--

---

|Fields|Type
|--|--
|  spawnBiome|Biome
|  spawnPosition|BlockPos

---

|Methods|Return Type
|--|--
| func_187214_a(DataParameter\<T> arg0, Object arg1)|void
| func_187216_a(PacketBuffer p)|void
| func_187217_b(DataParameter\<T> d)|void
| func_187218_a(List\<net.minecraft.network.datasync.EntityDataManager$DataEntry\<?>> l)|void
| func_187221_b()|List\<net.minecraft.network.datasync.EntityDataManager$DataEntry\<?>>
| func_187223_a()|boolean
| func_187225_a(DataParameter\<T> d)|Object
| func_187227_b(DataParameter\<T> arg0, Object arg1)|void
| func_187228_d()|boolean
| func_187230_e()|void
| func_187231_c()|List\<net.minecraft.network.datasync.EntityDataManager$DataEntry\<?>>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Teleporter

|Interface
|--
|net.minecraftforge.common.util.ITeleporter

---

|Extends
|--

---

|Fields|Type
|--|--
|  vanilla|boolean

---

|Methods|Return Type
|--|--
| placeEntity(World arg0, Entity arg1, float arg2)|void

---

## CombatTracker

|Class
|--
|net.minecraft.util.CombatTracker

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_151521_b()|TextComponent
| func_180134_f()|int
| func_180135_h()|EntityLivingBase
| func_94545_a()|void
| func_94547_a(DamageSource arg0, float arg1, float arg2)|void
| func_94549_h()|void
| func_94550_c()|EntityLivingBase
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AttributeInstance

|Interface
|--
|net.minecraft.entity.ai.attributes.IAttributeInstance

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_111121_a(AttributeModifier a)|void
| func_111122_c()|Collection\<AttributeModifier>
| func_111123_a()|Attribute
| func_111124_b(AttributeModifier a)|void
| func_111125_b()|double
| func_111126_e()|double
| func_111127_a(UUID u)|AttributeModifier
| func_111128_a(double d)|void
| func_111130_a(int i)|Collection\<AttributeModifier>
| func_142049_d()|void
| func_180374_a(AttributeModifier a)|boolean
| func_188479_b(UUID u)|void

---

## CommandResultStats$Type

|Class
|--
|net.minecraft.command.CommandResultStats$Type

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_179636_a()|int
| func_179637_b()|String
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CommandResultStats

|Class
|--
|net.minecraft.command.CommandResultStats

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_179668_a(NBTTagCompound n)|void
| func_179670_b(NBTTagCompound n)|void
| func_179671_a(CommandResultStats c)|void
| func_184932_a(MinecraftServer arg0, CommandSender arg1, CommandResultStats$Type arg2, int arg3)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## DamageSource

|Class
|--
|net.minecraft.util.DamageSource

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_76373_n|String

---

|Methods|Return Type
|--|--
| func_151517_h()|boolean
| func_151518_m()|DamageSource
| func_151519_b(EntityLivingBase e)|TextComponent
| func_180136_u()|boolean
| func_188404_v()|Vec3d
| func_76345_d()|float
| func_76346_g()|Entity
| func_76347_k()|boolean
| func_76348_h()|DamageSource
| func_76349_b()|DamageSource
| func_76350_n()|boolean
| func_76351_m()|DamageSource
| func_76352_a()|boolean
| func_76355_l()|String
| func_76357_e()|boolean
| func_76359_i()|DamageSource
| func_76361_j()|DamageSource
| func_76363_c()|boolean
| func_76364_f()|Entity
| func_82725_o()|boolean
| func_82726_p()|DamageSource
| func_94540_d()|DamageSource
| func_94541_c()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Team

|Class
|--
|net.minecraft.scoreboard.Team

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_142053_d(String s)|String
| func_142054_a(Team t)|boolean
| func_178770_i()|Team$EnumVisible
| func_178771_j()|Team$EnumVisible
| func_178775_l()|TextFormatting
| func_186681_k()|Team$CollisionRule
| func_96661_b()|String
| func_96665_g()|boolean
| func_96670_d()|Collection\<String>
| func_98297_h()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## DataParameter

|Class
|--
|net.minecraft.network.datasync.DataParameter

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_187155_a()|int
| func_187156_b()|DataSerializer\<T>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumHandSide

|Class
|--
|net.minecraft.util.EnumHandSide

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_188468_a()|EnumHandSide
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Vec2f

|Class
|--
|net.minecraft.util.math.Vec2f

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_189982_i|float
|  field_189983_j|float

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityLightningBolt

|Class
|--
|net.minecraft.entity.effect.EntityLightningBolt

---

|Extends
|--
|EntityWeatherEffect

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_190534_ay|int
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_70262_b|int
|  field_70264_a|long
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_98038_p|boolean
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_110124_au()|UUID
| func_130014_f_()|World
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_190530_aW()|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70676_i(float f)|Vec3d
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MoverType

|Class
|--
|net.minecraft.entity.MoverType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumCreatureAttribute

|Class
|--
|net.minecraft.entity.EnumCreatureAttribute

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CommandSender

|Interface
|--
|net.minecraft.command.ICommandSender

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_130014_f_()|World
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_180425_c()|BlockPos
| func_184102_h()|MinecraftServer
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String

---

## CapabilitySerializable

|Interface
|--
|net.minecraftforge.common.capabilities.ICapabilitySerializable

---

|Extends
|--
|CapabilityProvider
|NBTSerializable

---

|Methods|Return Type
|--|--
| deserializeNBT(NBTBase n)|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| serializeNBT()|NBTBase

---

## InventoryPlayer

|Class
|--
|net.minecraft.entity.player.InventoryPlayer

---

|Extends
|--
|Inventory

---

|Fields|Type
|--|--
|  field_184439_c|NonNullList\<ItemStack>
|  field_194017_h|int
|  field_70458_d|EntityPlayer
|  field_70460_b|NonNullList\<ItemStack>
|  field_70461_c|int
|  field_70462_a|NonNullList\<ItemStack>

---

|Methods|Return Type
|--|--
| func_145748_c_()|TextComponent
| func_145818_k_()|boolean
| func_174885_b(int arg0, int arg1)|void
| func_174886_c(EntityPlayer e)|void
| func_174887_a_(int i)|int
| func_174888_l()|void
| func_174889_b(EntityPlayer e)|void
| func_174890_g()|int
| func_174925_a(Item arg0, int arg1, int arg2, NBTTagCompound arg3)|int
| func_184429_b(ItemStack i)|int
| func_184430_d(int i)|void
| func_184432_b(BlockState b)|boolean
| func_184433_k()|int
| func_184434_a(ItemStack i)|void
| func_184437_d(ItemStack i)|void
| func_184438_a(BlockState b)|float
| func_191420_l()|boolean
| func_191971_c(int arg0, ItemStack arg1)|boolean
| func_191975_a(World arg0, ItemStack arg1)|void
| func_194014_c(ItemStack i)|int
| func_194015_p()|int
| func_194016_a(RecipeItemHelper arg0, boolean arg1)|void
| func_70005_c_()|String
| func_70296_d()|void
| func_70297_j_()|int
| func_70298_a(int arg0, int arg1)|ItemStack
| func_70299_a(int arg0, ItemStack arg1)|void
| func_70300_a(EntityPlayer e)|boolean
| func_70301_a(int i)|ItemStack
| func_70302_i_()|int
| func_70304_b(int i)|ItemStack
| func_70429_k()|void
| func_70431_c(ItemStack i)|boolean
| func_70432_d(ItemStack i)|int
| func_70436_m()|void
| func_70437_b(ItemStack i)|void
| func_70440_f(int i)|ItemStack
| func_70441_a(ItemStack i)|boolean
| func_70442_a(NBTTagList n)|NBTTagList
| func_70443_b(NBTTagList n)|void
| func_70445_o()|ItemStack
| func_70447_i()|int
| func_70448_g()|ItemStack
| func_70449_g(float f)|void
| func_70453_c(int i)|void
| func_70455_b(InventoryPlayer i)|void
| func_94041_b(int arg0, ItemStack arg1)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PlayerCapabilities

|Class
|--
|net.minecraft.entity.player.PlayerCapabilities

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_75098_d|boolean
|  field_75099_e|boolean
|  field_75100_b|boolean
|  field_75101_c|boolean
|  field_75102_a|boolean

---

|Methods|Return Type
|--|--
| func_75091_a(NBTTagCompound n)|void
| func_75092_a(float f)|void
| func_75093_a()|float
| func_75094_b()|float
| func_75095_b(NBTTagCompound n)|void
| func_82877_b(float f)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityFishHook

|Class
|--
|net.minecraft.entity.projectile.EntityFishHook

---

|Extends
|--
|Entity

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_146043_c|Entity
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_190534_ay|int
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_98038_p|boolean
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_110124_au()|UUID
| func_130014_f_()|World
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_146034_e()|int
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_190530_aW()|boolean
| func_190619_l()|EntityPlayer
| func_191516_a(int i)|void
| func_191517_b(int i)|void
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70676_i(float f)|Vec3d
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TileEntitySign

|Class
|--
|net.minecraft.tileentity.TileEntitySign

---

|Extends
|--
|TileEntity

---

|Fields|Type
|--|--
|  field_145915_a|TextComponent[]
|  field_145918_i|int
|  renderBoundingBox|AxisAlignedBB
|  tileData|NBTTagCompound

---

|Methods|Return Type
|--|--
| canRenderBreaking()|boolean
| deserializeNBT(NBTBase n)|void
| deserializeNBT(NBTTagCompound n)|void
| func_145748_c_()|TextComponent
| func_145828_a(CrashReportCategory c)|void
| func_145829_t()|void
| func_145830_o()|boolean
| func_145831_w()|World
| func_145832_p()|int
| func_145833_n()|double
| func_145834_a(World w)|void
| func_145835_a(double arg0, double arg1, double arg2)|double
| func_145836_u()|void
| func_145837_r()|boolean
| func_145838_q()|Block
| func_145839_a(NBTTagCompound n)|void
| func_145842_c(int arg0, int arg1)|boolean
| func_145843_s()|void
| func_145911_b()|EntityPlayer
| func_145912_a(EntityPlayer e)|void
| func_145913_a(boolean b)|void
| func_145914_a()|boolean
| func_174877_v()|BlockPos
| func_174878_a(BlockPos b)|void
| func_174880_d()|CommandResultStats
| func_174882_b(EntityPlayer e)|boolean
| func_183000_F()|boolean
| func_189515_b(NBTTagCompound n)|NBTTagCompound
| func_189517_E_()|NBTTagCompound
| func_189518_D_()|SPacketUpdateTileEntity
| func_189667_a(Rotation r)|void
| func_189668_a(Mirror m)|void
| func_70296_d()|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| handleUpdateTag(NBTTagCompound n)|void
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| hasFastRenderer()|boolean
| onChunkUnload()|void
| onDataPacket(NetworkManager arg0, SPacketUpdateTileEntity arg1)|void
| onLoad()|void
| restrictNBTCopy()|boolean
| serializeNBT()|NBTBase
| serializeNBT()|NBTTagCompound
| shouldRefresh(World arg0, BlockPos arg1, BlockState arg2, BlockState arg3)|boolean
| shouldRenderInPass(int i)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## LockCode

|Class
|--
|net.minecraft.world.LockCode

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_180157_a(NBTTagCompound n)|void
| func_180159_b()|String
| func_180160_a()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumPlayerModelParts

|Class
|--
|net.minecraft.entity.player.EnumPlayerModelParts

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_179326_d()|TextComponent
| func_179327_a()|int
| func_179328_b()|int
| func_179329_c()|String
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## InteractionObject

|Interface
|--
|net.minecraft.world.IInteractionObject

---

|Extends
|--
|WorldNameable

---

|Methods|Return Type
|--|--
| func_145748_c_()|TextComponent
| func_145818_k_()|boolean
| func_174875_k()|String
| func_174876_a(InventoryPlayer arg0, EntityPlayer arg1)|Container
| func_70005_c_()|String

---

## EntityPlayer$SleepResult

|Class
|--
|net.minecraft.entity.player.EntityPlayer$SleepResult

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Merchant

|Interface
|--
|net.minecraft.entity.IMerchant

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_110297_a_(ItemStack i)|void
| func_145748_c_()|TextComponent
| func_190670_t_()|World
| func_190671_u_()|BlockPos
| func_70930_a(MerchantRecipeList m)|void
| func_70931_l_()|EntityPlayer
| func_70932_a_(EntityPlayer e)|void
| func_70933_a(MerchantRecipe m)|void
| func_70934_b(EntityPlayer e)|MerchantRecipeList

---

## CommandBlockBaseLogic

|Class
|--
|net.minecraft.tileentity.CommandBlockBaseLogic

---

|Extends
|--
|CommandSender

---

|Methods|Return Type
|--|--
| func_130014_f_()|World
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145749_h()|TextComponent
| func_145750_b(TextComponent t)|void
| func_145751_f()|int
| func_145752_a(String s)|void
| func_145753_i()|String
| func_145754_b(String s)|void
| func_145755_a(World w)|boolean
| func_145756_e()|void
| func_145757_a(ByteBuf b)|void
| func_145759_b(NBTTagCompound n)|void
| func_145760_g()|int
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_175571_m()|boolean
| func_175572_n()|CommandResultStats
| func_175573_a(boolean b)|void
| func_175574_a(EntityPlayer e)|boolean
| func_180425_c()|BlockPos
| func_184102_h()|MinecraftServer
| func_184167_a(int i)|void
| func_189510_a(NBTTagCompound n)|NBTTagCompound
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CooldownTracker

|Class
|--
|net.minecraft.util.CooldownTracker

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_185141_a(Item i)|boolean
| func_185142_b(Item i)|void
| func_185143_a(Item arg0, float arg1)|float
| func_185144_a()|void
| func_185145_a(Item arg0, int arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TileEntityCommandBlock

|Class
|--
|net.minecraft.tileentity.TileEntityCommandBlock

---

|Extends
|--
|TileEntity

---

|Fields|Type
|--|--
|  renderBoundingBox|AxisAlignedBB
|  tileData|NBTTagCompound

---

|Methods|Return Type
|--|--
| canRenderBreaking()|boolean
| deserializeNBT(NBTBase n)|void
| deserializeNBT(NBTTagCompound n)|void
| func_145748_c_()|TextComponent
| func_145828_a(CrashReportCategory c)|void
| func_145829_t()|void
| func_145830_o()|boolean
| func_145831_w()|World
| func_145832_p()|int
| func_145833_n()|double
| func_145834_a(World w)|void
| func_145835_a(double arg0, double arg1, double arg2)|double
| func_145836_u()|void
| func_145837_r()|boolean
| func_145838_q()|Block
| func_145839_a(NBTTagCompound n)|void
| func_145842_c(int arg0, int arg1)|boolean
| func_145843_s()|void
| func_145993_a()|CommandBlockBaseLogic
| func_174877_v()|BlockPos
| func_174878_a(BlockPos b)|void
| func_175124_c()|CommandResultStats
| func_183000_F()|boolean
| func_184249_c()|boolean
| func_184250_a(boolean b)|void
| func_184251_i()|TileEntityCommandBlock$Mode
| func_184252_d(boolean b)|void
| func_184253_b(boolean b)|void
| func_184254_e()|boolean
| func_184255_d()|boolean
| func_184256_g()|boolean
| func_184257_h()|boolean
| func_184258_j()|boolean
| func_189515_b(NBTTagCompound n)|NBTTagCompound
| func_189517_E_()|NBTTagCompound
| func_189518_D_()|SPacketUpdateTileEntity
| func_189667_a(Rotation r)|void
| func_189668_a(Mirror m)|void
| func_70296_d()|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| handleUpdateTag(NBTTagCompound n)|void
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| hasFastRenderer()|boolean
| onChunkUnload()|void
| onDataPacket(NetworkManager arg0, SPacketUpdateTileEntity arg1)|void
| onLoad()|void
| restrictNBTCopy()|boolean
| serializeNBT()|NBTBase
| serializeNBT()|NBTTagCompound
| shouldRefresh(World arg0, BlockPos arg1, BlockState arg2, BlockState arg3)|boolean
| shouldRenderInPass(int i)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AbstractHorse

|Class
|--
|net.minecraft.entity.passive.AbstractHorse

---

|Extends
|--
|EntityAnimal
|InventoryChangedListener
|JumpingMount

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_110153_bc|float
|  field_110158_av|int
|  field_110278_bp|int
|  field_110279_bq|int
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_184617_aD|int
|  field_184618_aE|float
|  field_184619_aG|float
|  field_184622_au|EnumHand
|  field_184627_bm|ItemStack
|  field_184628_bn|int
|  field_190534_ay|int
|  field_191988_bg|float
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_70696_bz|EntityLivingBase
|  field_70701_bs|float
|  field_70702_br|float
|  field_70703_bu|boolean
|  field_70704_bt|float
|  field_70714_bg|EntityAITasks
|  field_70715_bh|EntityAITasks
|  field_70718_bc|int
|  field_70720_be|int
|  field_70721_aZ|float
|  field_70725_aQ|int
|  field_70726_aT|float
|  field_70727_aS|float
|  field_70728_aV|int
|  field_70732_aI|float
|  field_70733_aJ|float
|  field_70737_aN|int
|  field_70738_aO|int
|  field_70739_aP|float
|  field_70747_aH|float
|  field_70755_b|EntityLivingBase
|  field_70757_a|int
|  field_70758_at|float
|  field_70759_as|float
|  field_70760_ar|float
|  field_70761_aq|float
|  field_70769_ao|float
|  field_70770_ap|float
|  field_70771_an|int
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_82175_bq|boolean
|  field_98038_p|boolean
|  itemInUseMaxDuration|int
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| curePotionEffects(ItemStack i)|void
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_104002_bU()|boolean
| func_110124_au()|UUID
| func_110138_aP()|float
| func_110139_bj()|float
| func_110140_aT()|AbstractAttributeMap
| func_110142_aN()|CombatTracker
| func_110143_aJ()|float
| func_110144_aD()|EntityLivingBase
| func_110145_l(Entity e)|void
| func_110148_a(Attribute a)|AttributeInstance
| func_110149_m(float f)|void
| func_110160_i(boolean arg0, boolean arg1)|void
| func_110162_b(Entity arg0, boolean arg1)|void
| func_110163_bv()|void
| func_110166_bE()|Entity
| func_110167_bD()|boolean
| func_110173_bK()|boolean
| func_110174_bM()|float
| func_110175_bO()|boolean
| func_110177_bN()|void
| func_110195_a(int i)|void
| func_110198_t(int i)|int
| func_110199_f(EntityPlayer e)|void
| func_110201_q(float f)|float
| func_110204_cc()|boolean
| func_110205_ce()|boolean
| func_110206_u(int i)|void
| func_110209_cd()|boolean
| func_110215_cj()|double
| func_110219_q(boolean b)|void
| func_110223_p(float f)|float
| func_110227_p(boolean b)|void
| func_110234_j(boolean b)|void
| func_110238_s(int i)|void
| func_110242_l(boolean b)|void
| func_110246_bZ()|boolean
| func_110248_bS()|boolean
| func_110251_o(boolean b)|void
| func_110252_cg()|int
| func_110254_bY()|float
| func_110255_k(boolean b)|void
| func_110257_ck()|boolean
| func_110258_o(float f)|float
| func_110263_g(EntityPlayer e)|boolean
| func_130011_c(Entity e)|void
| func_130014_f_()|World
| func_142013_aG()|int
| func_142015_aE()|int
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_146082_f(EntityPlayer e)|void
| func_152111_bt()|void
| func_152112_bu()|void
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_175446_cd()|boolean
| func_175449_a(BlockPos arg0, int arg1)|void
| func_175501_a(int arg0, boolean arg1)|void
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180482_a(DifficultyInstance arg0, EntityLivingData arg1)|EntityLivingData
| func_180484_a(BlockPos b)|float
| func_180485_d(BlockPos b)|boolean
| func_180486_cf()|BlockPos
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_184582_a(EntityEquipmentSlot e)|ItemStack
| func_184583_d(DamageSource d)|boolean
| func_184585_cz()|boolean
| func_184586_b(EnumHand e)|ItemStack
| func_184587_cr()|boolean
| func_184589_d(Potion p)|void
| func_184591_cq()|EnumHandSide
| func_184592_cb()|ItemStack
| func_184595_k(double arg0, double arg1, double arg2)|boolean
| func_184596_c(Potion p)|PotionEffect
| func_184597_cx()|void
| func_184598_c(EnumHand e)|void
| func_184599_cB()|int
| func_184600_cs()|EnumHand
| func_184602_cy()|void
| func_184603_cC()|boolean
| func_184605_cv()|int
| func_184607_cu()|ItemStack
| func_184609_a(EnumHand e)|void
| func_184611_a(EnumHand arg0, ItemStack arg1)|void
| func_184612_cw()|int
| func_184613_cA()|boolean
| func_184614_ca()|ItemStack
| func_184638_cS()|boolean
| func_184641_n(boolean b)|void
| func_184642_a(EntityEquipmentSlot arg0, float arg1)|void
| func_184643_a(PathNodeType p)|float
| func_184644_a(PathNodeType arg0, float arg1)|void
| func_184645_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184646_p(float f)|void
| func_184649_cE()|int
| func_184652_a(EntityPlayer e)|boolean
| func_184775_b(int i)|void
| func_184776_b()|boolean
| func_184777_r_()|void
| func_184779_b(UUID u)|void
| func_184780_dh()|UUID
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_189748_bU()|DamageSource
| func_190530_aW()|boolean
| func_190630_a(EntityEquipmentSlot e)|boolean
| func_190631_cK()|boolean
| func_190676_dC()|int
| func_190677_dK()|boolean
| func_190682_f(ItemStack i)|boolean
| func_190684_dE()|boolean
| func_190685_dA()|boolean
| func_190687_dF()|void
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_191986_a(float arg0, float arg1, float arg2)|void
| func_191987_a(BlockPos arg0, boolean arg1)|void
| func_191989_p(float f)|void
| func_191993_do()|EntityPlayerMP
| func_193076_bZ()|Map\<Potion, PotionEffect>
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70058_J()|boolean
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70601_bi()|boolean
| func_70603_bj()|float
| func_70604_c(EntityLivingBase e)|void
| func_70605_aq()|EntityMoveHelper
| func_70606_j(float f)|void
| func_70608_bn()|boolean
| func_70613_aW()|boolean
| func_70615_aA()|void
| func_70617_f_()|boolean
| func_70624_b(EntityLivingBase e)|void
| func_70625_a(Entity arg0, float arg1, float arg2)|void
| func_70627_aG()|int
| func_70631_g_()|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70635_at()|EntitySenses
| func_70636_d()|void
| func_70637_d(boolean b)|void
| func_70638_az()|EntityLivingBase
| func_70641_bl()|int
| func_70642_aH()|void
| func_70643_av()|EntityLivingBase
| func_70644_a(Potion p)|boolean
| func_70645_a(DamageSource d)|void
| func_70646_bf()|int
| func_70648_aU()|boolean
| func_70651_bq()|Collection\<PotionEffect>
| func_70652_k(Entity e)|boolean
| func_70653_a(Entity arg0, float arg1, double arg2, double arg3)|void
| func_70654_ax()|int
| func_70656_aK()|void
| func_70657_f(float f)|void
| func_70658_aO()|int
| func_70659_e(float f)|void
| func_70660_b(Potion p)|PotionEffect
| func_70661_as()|PathNavigate
| func_70662_br()|boolean
| func_70668_bt()|EnumCreatureAttribute
| func_70669_a(ItemStack i)|void
| func_70671_ap()|EntityLookHelper
| func_70674_bp()|void
| func_70676_i(float f)|Vec3d
| func_70678_g(float f)|float
| func_70681_au()|Random
| func_70683_ar()|EntityJumpHelper
| func_70685_l(Entity e)|boolean
| func_70686_a(Class\<? extends net.minecraft.entity.EntityLivingBase> c)|boolean
| func_70687_e(PotionEffect p)|boolean
| func_70689_ay()|float
| func_70690_d(PotionEffect p)|void
| func_70691_i(float f)|void
| func_70781_l()|boolean
| func_70873_a(int i)|void
| func_70874_b()|int
| func_70875_t()|void
| func_70877_b(ItemStack i)|boolean
| func_70878_b(EntityAnimal e)|boolean
| func_70880_s()|boolean
| func_71001_a(Entity arg0, int arg1)|void
| func_76316_a(Inventory i)|void
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_82171_bF()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_85034_r(int i)|void
| func_85035_bI()|int
| func_90011_a(EntityAgeable e)|EntityAgeable
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_94060_bK()|EntityLivingBase
| func_94061_f(boolean b)|void
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| func_98052_bS()|boolean
| func_98053_h(boolean b)|void
| func_98054_a(boolean b)|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderFaceForward(EntityPlayer e)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TileEntityStructure

|Class
|--
|net.minecraft.tileentity.TileEntityStructure

---

|Extends
|--
|TileEntity

---

|Fields|Type
|--|--
|  renderBoundingBox|AxisAlignedBB
|  tileData|NBTTagCompound

---

|Methods|Return Type
|--|--
| canRenderBreaking()|boolean
| deserializeNBT(NBTBase n)|void
| deserializeNBT(NBTTagCompound n)|void
| func_145748_c_()|TextComponent
| func_145828_a(CrashReportCategory c)|void
| func_145829_t()|void
| func_145830_o()|boolean
| func_145831_w()|World
| func_145832_p()|int
| func_145833_n()|double
| func_145834_a(World w)|void
| func_145835_a(double arg0, double arg1, double arg2)|double
| func_145836_u()|void
| func_145837_r()|boolean
| func_145838_q()|Block
| func_145839_a(NBTTagCompound n)|void
| func_145842_c(int arg0, int arg1)|boolean
| func_145843_s()|void
| func_174877_v()|BlockPos
| func_174878_a(BlockPos b)|void
| func_183000_F()|boolean
| func_184404_a(String s)|void
| func_184405_a(TileEntityStructure$Mode t)|void
| func_184406_a(boolean b)|void
| func_184408_a(Rotation r)|void
| func_184409_c(BlockPos b)|void
| func_184410_b(String s)|void
| func_184411_a(Mirror m)|void
| func_184412_n()|boolean
| func_184414_b(BlockPos b)|void
| func_184417_l()|boolean
| func_184419_m()|boolean
| func_189515_b(NBTTagCompound n)|NBTTagCompound
| func_189517_E_()|NBTTagCompound
| func_189518_D_()|SPacketUpdateTileEntity
| func_189667_a(Rotation r)|void
| func_189668_a(Mirror m)|void
| func_189700_k()|TileEntityStructure$Mode
| func_189701_a(EntityPlayer e)|boolean
| func_189702_n()|float
| func_189703_e(boolean b)|void
| func_189705_a(ByteBuf b)|void
| func_189706_E()|void
| func_189707_H()|boolean
| func_189708_j()|String
| func_189709_F()|boolean
| func_189710_f(boolean b)|void
| func_189711_e()|BlockPos
| func_189712_b(boolean b)|boolean
| func_189713_m()|boolean
| func_189714_c(boolean b)|boolean
| func_189715_d()|String
| func_189716_h()|Mirror
| func_189717_g()|BlockPos
| func_189718_a(float f)|void
| func_189719_o()|long
| func_189720_a(EntityLivingBase e)|void
| func_189721_I()|boolean
| func_189722_G()|boolean
| func_189723_d(boolean b)|void
| func_189724_l()|void
| func_189725_a(long l)|void
| func_189726_i()|Rotation
| func_70296_d()|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| handleUpdateTag(NBTTagCompound n)|void
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| hasFastRenderer()|boolean
| onChunkUnload()|void
| onDataPacket(NetworkManager arg0, SPacketUpdateTileEntity arg1)|void
| onLoad()|void
| restrictNBTCopy()|boolean
| serializeNBT()|NBTBase
| serializeNBT()|NBTTagCompound
| shouldRefresh(World arg0, BlockPos arg1, BlockState arg2, BlockState arg3)|boolean
| shouldRenderInPass(int i)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## InventoryEnderChest

|Class
|--
|net.minecraft.inventory.InventoryEnderChest

---

|Extends
|--
|InventoryBasic

---

|Methods|Return Type
|--|--
| func_110132_b(InventoryChangedListener i)|void
| func_110133_a(String s)|void
| func_110134_a(InventoryChangedListener i)|void
| func_145748_c_()|TextComponent
| func_145818_k_()|boolean
| func_146031_a(TileEntityEnderChest t)|void
| func_174885_b(int arg0, int arg1)|void
| func_174886_c(EntityPlayer e)|void
| func_174887_a_(int i)|int
| func_174888_l()|void
| func_174889_b(EntityPlayer e)|void
| func_174890_g()|int
| func_174894_a(ItemStack i)|ItemStack
| func_191420_l()|boolean
| func_70005_c_()|String
| func_70296_d()|void
| func_70297_j_()|int
| func_70298_a(int arg0, int arg1)|ItemStack
| func_70299_a(int arg0, ItemStack arg1)|void
| func_70300_a(EntityPlayer e)|boolean
| func_70301_a(int i)|ItemStack
| func_70302_i_()|int
| func_70304_b(int i)|ItemStack
| func_70486_a(NBTTagList n)|void
| func_70487_g()|NBTTagList
| func_94041_b(int arg0, ItemStack arg1)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## FoodStats

|Class
|--
|net.minecraft.util.FoodStats

---

|Extends
|--
|AppleCoreFoodStats

---

|Fields|Type
|--|--
|  entityplayer|EntityPlayer
|  exhaustion|float
|  foodTimer|int
|  player|EntityPlayer
|  starveTimer|int

---

|Methods|Return Type
|--|--
| func_151686_a(ItemFood arg0, ItemStack arg1)|void
| func_75112_a(NBTTagCompound n)|void
| func_75113_a(float f)|void
| func_75114_a(int i)|void
| func_75115_e()|float
| func_75116_a()|int
| func_75117_b(NBTTagCompound n)|void
| func_75118_a(EntityPlayer e)|void
| func_75119_b(float f)|void
| func_75121_c()|boolean
| func_75122_a(int arg0, float arg1)|void
| setPrevFoodLevel(int i)|void
| setSaturation(float f)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GameType

|Class
|--
|net.minecraft.world.GameType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_77144_e()|boolean
| func_77145_d()|boolean
| func_77147_a(PlayerCapabilities p)|void
| func_77148_a()|int
| func_77149_b()|String
| func_82752_c()|boolean
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumPlantType

|Class
|--
|net.minecraftforge.common.EnumPlantType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketUpdateTileEntity

|Class
|--
|net.minecraft.network.play.server.SPacketUpdateTileEntity

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_148853_f()|int
| func_148857_g()|NBTTagCompound
| func_179823_a()|BlockPos
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NetworkManager

|Class
|--
|net.minecraft.network.NetworkManager

---

|Extends
|--
|SimpleChannelInboundHandler

---

|Fields|Type
|--|--
|  direction|EnumPacketDirection
|  sharable|boolean

---

|Methods|Return Type
|--|--
| acceptInboundMessage(Object o)|boolean
| channel()|Channel
| channelActive(ChannelHandlerContext c)|void
| channelInactive(ChannelHandlerContext c)|void
| channelRead(ChannelHandlerContext arg0, Object arg1)|void
| channelReadComplete(ChannelHandlerContext c)|void
| channelRegistered(ChannelHandlerContext c)|void
| channelUnregistered(ChannelHandlerContext c)|void
| channelWritabilityChanged(ChannelHandlerContext c)|void
| exceptionCaught(ChannelHandlerContext arg0, Throwable arg1)|void
| func_150718_a(TextComponent t)|void
| func_150719_a(NetHandler n)|void
| func_150721_g()|void
| func_150723_a(EnumConnectionState e)|void
| func_150724_d()|boolean
| func_150727_a(SecretKey s)|void
| func_150729_e()|NetHandler
| func_150730_f()|TextComponent
| func_150731_c()|boolean
| func_179288_a(Packet\<?> arg0, GenericFutureListener\<? extends io.netty.util.concurrent.Future\<? super java.lang.Void>> arg1, GenericFutureListener[] arg2)|void
| func_179289_a(int i)|void
| func_179290_a(Packet\<?> p)|void
| func_179291_h()|boolean
| func_179292_f()|boolean
| func_179293_l()|void
| func_74428_b()|void
| func_74430_c()|SocketAddress
| handlerAdded(ChannelHandlerContext c)|void
| handlerRemoved(ChannelHandlerContext c)|void
| userEventTriggered(ChannelHandlerContext arg0, Object arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NBTTagList

|Class
|--
|net.minecraft.nbt.NBTTagList

---

|Extends
|--
|NBTBase
|Iterable

---

|Fields|Type
|--|--
|  field_74747_a|List\<NBTBase>

---

|Methods|Return Type
|--|--
| forEach(Consumer\<? super T> c)|void
| func_150303_d()|int
| func_150304_a(int arg0, NBTBase arg1)|void
| func_150305_b(int i)|NBTTagCompound
| func_150306_c(int i)|int[]
| func_150307_f(int i)|String
| func_150308_e(int i)|float
| func_150309_d(int i)|double
| func_179238_g(int i)|NBTBase
| func_186858_c(int i)|int
| func_74732_a()|byte
| func_74737_b()|NBTBase
| func_74737_b()|NBTTagList
| func_74742_a(NBTBase n)|void
| func_74744_a(int i)|NBTBase
| func_74745_c()|int
| func_82582_d()|boolean
| iterator()|Iterator\<NBTBase>
| spliterator()|Spliterator\<T>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityItemFrame

|Class
|--
|net.minecraft.entity.item.EntityItemFrame

---

|Extends
|--
|EntityHanging

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_174860_b|EnumFacing
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_190534_ay|int
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_98038_p|boolean
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_110124_au()|UUID
| func_110128_b(Entity e)|void
| func_130014_f_()|World
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_146065_b(Entity arg0, boolean arg1)|void
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_174857_n()|BlockPos
| func_174866_q()|int
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_184523_o()|void
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_190530_aW()|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70518_d()|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70676_i(float f)|Vec3d
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_82329_d()|int
| func_82330_g()|int
| func_82333_j()|int
| func_82334_a(ItemStack i)|void
| func_82335_i()|ItemStack
| func_82336_g(int i)|void
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityAITasks

|Class
|--
|net.minecraft.entity.ai.EntityAITasks

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_75782_a|Set\<EntityAITasks$EntityAITaskEntry>

---

|Methods|Return Type
|--|--
| func_188525_d(int i)|void
| func_188526_c(int i)|void
| func_188527_a(int arg0, boolean arg1)|void
| func_188528_b(int i)|boolean
| func_75774_a()|void
| func_75776_a(int arg0, EntityAIBase arg1)|void
| func_85156_a(EntityAIBase e)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityLivingData

|Interface
|--
|net.minecraft.entity.IEntityLivingData

---

|Extends
|--

---

## EntityMoveHelper

|Class
|--
|net.minecraft.entity.ai.EntityMoveHelper

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_188491_h|EntityMoveHelper$Action

---

|Methods|Return Type
|--|--
| func_179917_d()|double
| func_179918_f()|double
| func_179919_e()|double
| func_188487_a(EntityMoveHelper e)|void
| func_188488_a(float arg0, float arg1)|void
| func_75638_b()|double
| func_75640_a()|boolean
| func_75641_c()|void
| func_75642_a(double arg0, double arg1, double arg2, double arg3)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntitySenses

|Class
|--
|net.minecraft.entity.ai.EntitySenses

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_75522_a(Entity e)|boolean
| func_75523_a()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PathNavigate

|Class
|--
|net.minecraft.pathfinding.PathNavigate

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_111269_d()|float
| func_179680_a(BlockPos b)|Path
| func_188553_i()|boolean
| func_188554_j()|void
| func_188555_b(BlockPos b)|boolean
| func_189566_q()|NodeProcessor
| func_75484_a(Path arg0, double arg1)|boolean
| func_75488_a(double arg0, double arg1, double arg2)|Path
| func_75489_a(double d)|void
| func_75492_a(double arg0, double arg1, double arg2, double arg3)|boolean
| func_75494_a(Entity e)|Path
| func_75497_a(Entity arg0, double arg1)|boolean
| func_75499_g()|void
| func_75500_f()|boolean
| func_75501_e()|void
| func_75505_d()|Path
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityLookHelper

|Class
|--
|net.minecraft.entity.ai.EntityLookHelper

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_75653_f|double
|  field_75654_g|double
|  field_75655_d|boolean
|  field_75656_e|double
|  field_75657_b|float
|  field_75658_c|float
|  field_75659_a|EntityLiving

---

|Methods|Return Type
|--|--
| func_180421_g()|double
| func_180422_f()|double
| func_180423_e()|double
| func_180424_b()|boolean
| func_75649_a()|void
| func_75650_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_75651_a(Entity arg0, float arg1, float arg2)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityJumpHelper

|Class
|--
|net.minecraft.entity.ai.EntityJumpHelper

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_75660_a()|void
| func_75661_b()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Enchantment$Rarity

|Class
|--
|net.minecraft.enchantment.Enchantment$Rarity

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_185270_a()|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ModelBase

|Class
|--
|net.minecraft.client.model.ModelBase

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_78089_u|int
|  field_78090_t|int
|  field_78091_s|boolean
|  field_78092_r|List\<ModelRenderer>
|  field_78093_q|boolean
|  field_78095_p|float

---

|Methods|Return Type
|--|--
| func_178686_a(ModelBase m)|void
| func_78084_a(String s)|TextureOffset
| func_78086_a(EntityLivingBase arg0, float arg1, float arg2, float arg3)|void
| func_78087_a(float arg0, float arg1, float arg2, float arg3, float arg4, float arg5, Entity arg6)|void
| func_78088_a(Entity arg0, float arg1, float arg2, float arg3, float arg4, float arg5, float arg6)|void
| func_85181_a(Random r)|ModelRenderer
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ModelRenderer

|Class
|--
|net.minecraft.client.model.ModelRenderer

---

|Extends
|--

---

|Fields|Type
|--|--
|  compiled|boolean
|  displayList|int
|  field_78795_f|float
|  field_78796_g|float
|  field_78797_d|float
|  field_78798_e|float
|  field_78799_b|float
|  field_78800_c|float
|  field_78801_a|float
|  field_78802_n|String
|  field_78803_o|int
|  field_78804_l|List\<ModelBox>
|  field_78805_m|List\<ModelRenderer>
|  field_78806_j|boolean
|  field_78807_k|boolean
|  field_78808_h|float
|  field_78809_i|boolean
|  field_78810_s|ModelBase
|  field_78811_r|int
|  field_78812_q|boolean
|  field_78813_p|int
|  field_82906_o|float
|  field_82907_q|float
|  field_82908_p|float
|  id|String
|  mirrorV|boolean
|  scaleX|float
|  scaleY|float
|  scaleZ|float
|  spriteList|List
|  textureLocation|ResourceLocation

---

|Methods|Return Type
|--|--
| addBox(int[][] arg0, float arg1, float arg2, float arg3, float arg4, float arg5, float arg6, float arg7)|void
| addSprite(float arg0, float arg1, float arg2, int arg3, int arg4, int arg5, float arg6)|void
| func_178769_a(float arg0, float arg1, float arg2, int arg3, int arg4, int arg5, boolean arg6)|ModelRenderer
| func_78784_a(int arg0, int arg1)|ModelRenderer
| func_78785_a(float f)|void
| func_78786_a(String arg0, float arg1, float arg2, float arg3, int arg4, int arg5, int arg6)|ModelRenderer
| func_78787_b(int arg0, int arg1)|ModelRenderer
| func_78788_d(float f)|void
| func_78789_a(float arg0, float arg1, float arg2, int arg3, int arg4, int arg5)|ModelRenderer
| func_78790_a(float arg0, float arg1, float arg2, int arg3, int arg4, int arg5, float arg6)|void
| func_78791_b(float f)|void
| func_78792_a(ModelRenderer m)|void
| func_78793_a(float arg0, float arg1, float arg2)|void
| func_78794_c(float f)|void
| getChild(String s)|ModelRenderer
| getChildDeep(String s)|ModelRenderer
| resetDisplayList()|void
| setModelUpdater(ModelUpdater m)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ModelBiped$ArmPose

|Class
|--
|net.minecraft.client.model.ModelBiped$ArmPose

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TextureOffset

|Class
|--
|net.minecraft.client.model.TextureOffset

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_78782_b|int
|  field_78783_a|int

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ResourceManagerReloadListener

|Interface
|--
|net.minecraft.client.resources.IResourceManagerReloadListener

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_110549_a(ResourceManager r)|void

---

## FontRendererHook

|Class
|--
|bre.smoothfont.FontRendererHook

---

|Extends
|--

---

|Fields|Type
|--|--
|  autoBrightnessDefault|int
|  autoBrightnessUnicode|int
|  boldFlag|boolean
|  brightnessBoundaryScaleFactorDefault|float
|  brightnessBoundaryScaleFactorUnicode|float
|  changeFont|boolean
|  disableFeatures|boolean
|  enableHookGetCharWidth|boolean
|  enableHookGetStringWidth|boolean
|  enableHookRenderChar|boolean
|  enableHookSizeStringToWidth|boolean
|  enableHookTrimStringToWidth|boolean
|  fontRenderer|FontRenderer
|  keepMcFontWidth|boolean
|  mcCharWidth|int[]
|  optifineCharWidthFloat|float[]
|  optimized|boolean
|  orthographic|boolean
|  precisionMode|int
|  reasonForDisable|String
|  roundedFontScale|float
|  shadowFlag|boolean
|  thinFontFlag|boolean

---

|Methods|Return Type
|--|--
| doDrawEnterHook()|void
| doDrawHook(float f)|float
| fontRendererExitHook()|void
| getCharWidthFloatGetCharIndexHook(char c)|int
| getCharWidthFloatTest(char c)|float
| getCharWidthGetCharIndexHook(char c)|int
| getCharWidthHook(char c)|int
| getStringWidthFloatHook(String s)|int
| getUnicodePageLocation(int i)|ResourceLocation
| initAfterConfigLoaded(boolean b)|void
| readFontTextureExitHook()|void
| readGlyphSizesExitHook()|void
| reloadResources()|void
| renderCharGetCharIndexHook(char c)|int
| renderCharHook(char arg0, boolean arg1)|float
| renderDefaultCharHook(int arg0, boolean arg1, float arg2, float arg3)|float
| renderStringAtPosEnterHook(String arg0, boolean arg1, boolean arg2)|void
| renderStringAtPosExitHook(boolean b)|void
| renderStringAtPosGetCharIndexHook(char c)|int
| renderStringExitHook(String s)|void
| renderStringHook(int i)|int
| renderUnicodeCharHook(char arg0, boolean arg1, byte[] arg2, float arg3, float arg4)|float
| setUnicodeFlagHook(boolean b)|boolean
| sizeStringToWidthFloatHook(String arg0, int arg1)|int
| trimStringToWidthFloatHook(String arg0, int arg1, boolean arg2)|String
| updateChangeFontFlag()|void
| updateHookFlags()|void
| updateMargins()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CommandBase

|Class
|--
|net.minecraft.command.CommandBase

---

|Extends
|--
|Command

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Command c)|int
| func_184881_a(MinecraftServer arg0, CommandSender arg1, String[] arg2)|void
| func_184882_a(MinecraftServer arg0, CommandSender arg1)|boolean
| func_184883_a(MinecraftServer arg0, CommandSender arg1, String[] arg2, BlockPos arg3)|List\<String>
| func_71514_a()|List\<String>
| func_71517_b()|String
| func_71518_a(CommandSender c)|String
| func_82358_a(String[] arg0, int arg1)|boolean
| func_82362_a()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CommandBuilder$ExecuteFunction

|Interface
|--
|dev.latvian.kubejs.command.CommandBuilder$ExecuteFunction

---

|Extends
|--

---

|Methods|Return Type
|--|--
| execute(CommandSender arg0, List\<String> arg1)|void

---

## CommandBuilder$UsernameFunction

|Interface
|--
|dev.latvian.kubejs.command.CommandBuilder$UsernameFunction

---

|Extends
|--

---

|Methods|Return Type
|--|--
| isUsername(List\<String> arg0, int arg1)|boolean

---

## EnumTristate

|Class
|--
|com.feed_the_beast.ftblib.lib.config.EnumTristate

---

|Extends
|--
|Enum
|StringSerializable

---

|Fields|Type
|--|--
|  color|Color4I
|  declaringClass|Class\<E>
|  default|boolean
|  false|boolean
|  opposite|EnumTristate
|  result|Event$Result
|  true|boolean

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_176610_l()|String
| get(boolean b)|boolean
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void
| write(NBTTagCompound arg0, String arg1)|void

---

## RewardType

|Class
|--
|com.feed_the_beast.ftbquests.quest.reward.RewardType

---

|Extends
|--
|IForgeRegistryEntry$Impl

---

|Fields|Type
|--|--
|  delegate|RegistryDelegate\<T>
|  displayName|String
|  excludeFromListRewards|boolean
|  guiProvider|RewardType$GuiProvider
|  icon|Icon
|  provider|RewardType$Provider
|  registryName|ResourceLocation
|  registryType|Class\<T>
|  typeForNBT|String

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CustomTask$Check

|Interface
|--
|com.feed_the_beast.ftbquests.quest.task.CustomTask$Check

---

|Extends
|--

---

|Methods|Return Type
|--|--
| check(CustomTask$Data arg0, EntityPlayerMP arg1)|void

---

## TaskType

|Class
|--
|com.feed_the_beast.ftbquests.quest.task.TaskType

---

|Extends
|--
|IForgeRegistryEntry$Impl

---

|Fields|Type
|--|--
|  delegate|RegistryDelegate\<T>
|  displayName|String
|  guiProvider|TaskType$GuiProvider
|  icon|Icon
|  provider|TaskType$Provider
|  registryName|ResourceLocation
|  registryType|Class\<T>
|  typeForNBT|String

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TileTaskScreenCore

|Class
|--
|com.feed_the_beast.ftbquests.tile.TileTaskScreenCore

---

|Extends
|--
|TileWithTeam
|ConfigCallback
|TaskScreen

---

|Fields|Type
|--|--
|  blockState|BlockState
|  brokenByCreative|boolean
|  dimPos|BlockDimPos
|  facing|EnumFacing
|  indestructible|boolean
|  inputModeIcon|ItemStack
|  inputOnly|boolean
|  offsetX|int
|  offsetY|int
|  offsetZ|int
|  paint|BlockState
|  renderBoundingBox|AxisAlignedBB
|  screen|TileTaskScreenCore
|  size|int
|  skin|BlockState
|  task|int
|  taskData|TaskData
|  team|String
|  tileData|NBTTagCompound

---

|Methods|Return Type
|--|--
| canRenderBreaking()|boolean
| checkIfDirty()|void
| createState(BlockState b)|BlockState
| deserializeNBT(NBTBase n)|void
| deserializeNBT(NBTTagCompound n)|void
| func_145748_c_()|TextComponent
| func_145818_k_()|boolean
| func_145828_a(CrashReportCategory c)|void
| func_145829_t()|void
| func_145830_o()|boolean
| func_145831_w()|World
| func_145832_p()|int
| func_145833_n()|double
| func_145834_a(World w)|void
| func_145835_a(double arg0, double arg1, double arg2)|double
| func_145836_u()|void
| func_145837_r()|boolean
| func_145838_q()|Block
| func_145839_a(NBTTagCompound n)|void
| func_145842_c(int arg0, int arg1)|boolean
| func_145843_s()|void
| func_174877_v()|BlockPos
| func_174878_a(BlockPos b)|void
| func_183000_F()|boolean
| func_189515_b(NBTTagCompound n)|NBTTagCompound
| func_189517_E_()|NBTTagCompound
| func_189518_D_()|SPacketUpdateTileEntity
| func_189667_a(Rotation r)|void
| func_189668_a(Mirror m)|void
| func_70005_c_()|String
| func_70296_d()|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| handleUpdateTag(NBTTagCompound n)|void
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| hasFastRenderer()|boolean
| isOwner(EntityPlayer e)|boolean
| notifyNeighbors()|void
| onChunkUnload()|void
| onClicked(EntityPlayerMP arg0, EnumHand arg1, double arg2, double arg3)|void
| onConfigSaved(ConfigGroup arg0, CommandSender arg1)|void
| onContentsChanged(boolean b)|void
| onDataPacket(NetworkManager arg0, SPacketUpdateTileEntity arg1)|void
| onLoad()|void
| onUpdatePacket(EnumSaveType e)|void
| paint(BlockState arg0, EnumFacing arg1, boolean arg2)|void
| playSound(SoundEvent arg0, SoundCategory arg1, float arg2, float arg3)|void
| readFromItem(ItemStack i)|void
| resetData()|void
| restrictNBTCopy()|boolean
| serializeNBT()|NBTBase
| serializeNBT()|NBTTagCompound
| setIDFromPlacer(EntityLivingBase e)|void
| shouldRefresh(World arg0, BlockPos arg1, BlockState arg2, BlockState arg3)|boolean
| shouldRenderInPass(int i)|boolean
| updateComparator()|boolean
| updateTiles(Task t)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeToItem(ItemStack i)|void
| writeToPickBlock(ItemStack i)|void

---

## TileTaskScreenPart

|Class
|--
|com.feed_the_beast.ftbquests.tile.TileTaskScreenPart

---

|Extends
|--
|TileBase
|TaskScreen

---

|Fields|Type
|--|--
|  blockState|BlockState
|  brokenByCreative|boolean
|  dimPos|BlockDimPos
|  offsetX|int
|  offsetY|int
|  offsetZ|int
|  paint|BlockState
|  renderBoundingBox|AxisAlignedBB
|  screen|TileTaskScreenCore
|  tileData|NBTTagCompound

---

|Methods|Return Type
|--|--
| canRenderBreaking()|boolean
| checkIfDirty()|void
| createState(BlockState b)|BlockState
| deserializeNBT(NBTBase n)|void
| deserializeNBT(NBTTagCompound n)|void
| func_145748_c_()|TextComponent
| func_145818_k_()|boolean
| func_145828_a(CrashReportCategory c)|void
| func_145829_t()|void
| func_145830_o()|boolean
| func_145831_w()|World
| func_145832_p()|int
| func_145833_n()|double
| func_145834_a(World w)|void
| func_145835_a(double arg0, double arg1, double arg2)|double
| func_145836_u()|void
| func_145837_r()|boolean
| func_145838_q()|Block
| func_145839_a(NBTTagCompound n)|void
| func_145842_c(int arg0, int arg1)|boolean
| func_145843_s()|void
| func_174877_v()|BlockPos
| func_174878_a(BlockPos b)|void
| func_183000_F()|boolean
| func_189515_b(NBTTagCompound n)|NBTTagCompound
| func_189517_E_()|NBTTagCompound
| func_189518_D_()|SPacketUpdateTileEntity
| func_189667_a(Rotation r)|void
| func_189668_a(Mirror m)|void
| func_70005_c_()|String
| func_70296_d()|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| handleUpdateTag(NBTTagCompound n)|void
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| hasFastRenderer()|boolean
| notifyNeighbors()|void
| onChunkUnload()|void
| onContentsChanged(boolean b)|void
| onDataPacket(NetworkManager arg0, SPacketUpdateTileEntity arg1)|void
| onLoad()|void
| onUpdatePacket(EnumSaveType e)|void
| paint(BlockState arg0, EnumFacing arg1, boolean arg2)|void
| playSound(SoundEvent arg0, SoundCategory arg1, float arg2, float arg3)|void
| readFromItem(ItemStack i)|void
| restrictNBTCopy()|boolean
| serializeNBT()|NBTBase
| serializeNBT()|NBTTagCompound
| setOffset(int arg0, int arg1, int arg2)|void
| shouldRefresh(World arg0, BlockPos arg1, BlockState arg2, BlockState arg3)|boolean
| shouldRenderInPass(int i)|boolean
| updateComparator()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeToItem(ItemStack i)|void
| writeToPickBlock(ItemStack i)|void

---

## CustomTask$Data

|Class
|--
|com.feed_the_beast.ftbquests.quest.task.CustomTask$Data

---

|Extends
|--
|TaskData

---

|Fields|Type
|--|--
|  complete|boolean
|  data|QuestData
|  progress|long
|  progressString|String
|  relativeProgress|int
|  slots|int
|  started|boolean
|  task|Task

---

|Methods|Return Type
|--|--
| addProgress(long l)|void
| extractItem(int arg0, int arg1, boolean arg2)|ItemStack
| getCapability(Capability\<C> arg0, EnumFacing arg1)|Object
| getSlotLimit(int i)|int
| getStackInSlot(int i)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| insertItem(int arg0, ItemStack arg1, boolean arg2)|ItemStack
| insertItem(ItemStack arg0, boolean arg1, boolean arg2, EntityPlayer arg3)|ItemStack
| isItemValid(int arg0, ItemStack arg1)|boolean
| readProgress(long l)|void
| setProgress(long l)|void
| submitTask(EntityPlayerMP arg0, Collection\<ItemStack> arg1, boolean arg2)|boolean
| submitTask(EntityPlayerMP e)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemHandler

|Interface
|--
|net.minecraftforge.items.IItemHandler

---

|Extends
|--

---

|Fields|Type
|--|--
|  slots|int

---

|Methods|Return Type
|--|--
| extractItem(int arg0, int arg1, boolean arg2)|ItemStack
| getSlotLimit(int i)|int
| getStackInSlot(int i)|ItemStack
| insertItem(int arg0, ItemStack arg1, boolean arg2)|ItemStack
| isItemValid(int arg0, ItemStack arg1)|boolean

---

## Advancement

|Class
|--
|net.minecraft.advancements.Advancement

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_192067_g()|ResourceLocation
| func_192068_c()|DisplayInfo
| func_192069_e()|Iterable\<Advancement>
| func_192070_b()|Advancement
| func_192071_a(Advancement a)|void
| func_192072_d()|AdvancementRewards
| func_192073_f()|Map\<String, Criterion>
| func_192074_h()|String[][]
| func_192075_a()|Advancement$Builder
| func_193123_j()|TextComponent
| func_193124_g()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ContainerListener

|Interface
|--
|net.minecraft.inventory.IContainerListener

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_175173_a(Container arg0, Inventory arg1)|void
| func_71110_a(Container arg0, NonNullList\<ItemStack> arg1)|void
| func_71111_a(Container arg0, int arg1, ItemStack arg2)|void
| func_71112_a(Container arg0, int arg1, int arg2)|void

---

## Slot

|Class
|--
|net.minecraft.inventory.Slot

---

|Extends
|--

---

|Fields|Type
|--|--
|  backgroundLocation|ResourceLocation
|  backgroundSprite|TextureAtlasSprite
|  field_75221_f|int
|  field_75222_d|int
|  field_75223_e|int
|  field_75224_c|Inventory
|  slotIndex|int

---

|Methods|Return Type
|--|--
| func_111238_b()|boolean
| func_178170_b(ItemStack i)|int
| func_178171_c()|String
| func_190901_a(EntityPlayer arg0, ItemStack arg1)|ItemStack
| func_75209_a(int i)|ItemStack
| func_75211_c()|ItemStack
| func_75214_a(ItemStack i)|boolean
| func_75215_d(ItemStack i)|void
| func_75216_d()|boolean
| func_75217_a(Inventory arg0, int arg1)|boolean
| func_75218_e()|void
| func_75219_a()|int
| func_75220_a(ItemStack arg0, ItemStack arg1)|void
| func_82869_a(EntityPlayer e)|boolean
| isSameInventory(Slot s)|boolean
| setBackgroundName(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ClickType

|Class
|--
|net.minecraft.inventory.ClickType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WorldNameable

|Interface
|--
|net.minecraft.world.IWorldNameable

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_145748_c_()|TextComponent
| func_145818_k_()|boolean
| func_70005_c_()|String

---

## Recipe

|Interface
|--
|dev.latvian.kubejs.crafting.RecipeJS

---

|Extends
|--

---

|Methods|Return Type
|--|--
| add()|void
| set(Map\<String, Object> m)|Recipe

---

## ForgeRegistryEntry

|Interface
|--
|net.minecraftforge.registries.IForgeRegistryEntry

---

|Extends
|--

---

|Fields|Type
|--|--
|  registryName|ResourceLocation
|  registryType|Class\<V>

---

|Methods|Return Type
|--|--

---

## InventoryCrafting

|Class
|--
|net.minecraft.inventory.InventoryCrafting

---

|Extends
|--
|Inventory

---

|Fields|Type
|--|--
|  field_174924_c|int
|  field_70464_b|int
|  field_70465_c|Container
|  field_70466_a|NonNullList\<ItemStack>

---

|Methods|Return Type
|--|--
| func_145748_c_()|TextComponent
| func_145818_k_()|boolean
| func_174885_b(int arg0, int arg1)|void
| func_174886_c(EntityPlayer e)|void
| func_174887_a_(int i)|int
| func_174888_l()|void
| func_174889_b(EntityPlayer e)|void
| func_174890_g()|int
| func_174922_i()|int
| func_174923_h()|int
| func_191420_l()|boolean
| func_194018_a(RecipeItemHelper r)|void
| func_70005_c_()|String
| func_70296_d()|void
| func_70297_j_()|int
| func_70298_a(int arg0, int arg1)|ItemStack
| func_70299_a(int arg0, ItemStack arg1)|void
| func_70300_a(EntityPlayer e)|boolean
| func_70301_a(int i)|ItemStack
| func_70302_i_()|int
| func_70304_b(int i)|ItemStack
| func_70463_b(int arg0, int arg1)|ItemStack
| func_94041_b(int arg0, ItemStack arg1)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Ingredient

|Class
|--
|net.minecraft.item.crafting.Ingredient

---

|Extends
|--
|Predicate

---

|Fields|Type
|--|--
|  field_193371_b|ItemStack[]
|  simple|boolean

---

|Methods|Return Type
|--|--
| and(Predicate\<? super T> p)|Predicate\<T>
| apply(ItemStack i)|boolean
| apply(Object o)|boolean
| func_193365_a()|ItemStack[]
| func_194139_b()|IntList
| negate()|Predicate\<T>
| or(Predicate\<? super T> p)|Predicate\<T>
| test(Object o)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RegistryEvent$MissingMappings$Action

|Class
|--
|net.minecraftforge.event.RegistryEvent$MissingMappings$Action

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ForgeRegistry

|Interface
|--
|net.minecraftforge.registries.IForgeRegistry

---

|Extends
|--
|Iterable

---

|Fields|Type
|--|--
|  entries|Set\<java.util.Map$Entry\<net.minecraft.util.ResourceLocation, V>>
|  keys|Set\<ResourceLocation>
|  registrySuperType|Class\<V>
|  values|List\<V>
|  valuesCollection|Collection\<V>

---

|Methods|Return Type
|--|--
| containsKey(ResourceLocation r)|boolean
| containsValue(ForgeRegistryEntry f)|boolean
| forEach(Consumer\<? super T> c)|void
| getKey(ForgeRegistryEntry f)|ResourceLocation
| getSlaveMap(ResourceLocation arg0, Class\<T> arg1)|Object
| getValue(ResourceLocation r)|ForgeRegistryEntry
| iterator()|Iterator\<T>
| register(ForgeRegistryEntry f)|void
| registerAll(ForgeRegistryEntry[] f)|void
| spliterator()|Spliterator\<T>

---

## EnumFacing$Plane

|Class
|--
|net.minecraft.util.EnumFacing$Plane

---

|Extends
|--
|Enum
|Predicate
|Iterable

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| and(Predicate\<? super T> p)|Predicate\<T>
| apply(Object o)|boolean
| apply(EnumFacing e)|boolean
| compareTo(Object o)|int
| compareTo(Enum e)|int
| forEach(Consumer\<? super T> c)|void
| func_179516_a()|EnumFacing[]
| func_179518_a(Random r)|EnumFacing
| iterator()|Iterator\<EnumFacing>
| name()|String
| negate()|Predicate\<T>
| or(Predicate\<? super T> p)|Predicate\<T>
| ordinal()|int
| spliterator()|Spliterator\<T>
| test(Object o)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AnimationMetadataSection

|Class
|--
|net.minecraft.client.resources.data.AnimationMetadataSection

---

|Extends
|--
|MetadataSection

---

|Methods|Return Type
|--|--
| func_110468_c(int i)|int
| func_110469_d()|int
| func_110470_b(int i)|boolean
| func_110471_a()|int
| func_110472_a(int i)|int
| func_110473_c()|int
| func_110474_b()|int
| func_130073_e()|Set\<int>
| func_177219_e()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PngSizeInfo

|Class
|--
|net.minecraft.client.renderer.texture.PngSizeInfo

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_188533_a|int
|  field_188534_b|int

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Resource

|Interface
|--
|net.minecraft.client.resources.IResource

---

|Extends
|--
|Closeable

---

|Methods|Return Type
|--|--
| close()|void
| func_110526_a(String s)|MetadataSection
| func_110527_b()|InputStream
| func_110528_c()|boolean
| func_177240_d()|String
| func_177241_a()|ResourceLocation

---

## CounterInt

|Class
|--
|net.optifine.util.CounterInt

---

|Extends
|--

---

|Fields|Type
|--|--
|  value|int

---

|Methods|Return Type
|--|--
| nextValue()|int
| reset()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Style

|Class
|--
|net.minecraft.util.text.Style

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_150243_f|Boolean
|  field_150244_g|Boolean
|  field_150245_d|Boolean
|  field_150246_e|Boolean
|  field_150247_b|TextFormatting
|  field_150248_c|Boolean
|  field_150249_a|Style
|  field_150251_h|ClickEvent
|  field_150252_i|HoverEvent
|  field_179990_j|String

---

|Methods|Return Type
|--|--
| func_150206_m()|Style
| func_150209_a(HoverEvent h)|Style
| func_150210_i()|HoverEvent
| func_150215_a()|TextFormatting
| func_150217_b(Boolean b)|Style
| func_150218_j()|String
| func_150221_a(Style s)|Style
| func_150223_b()|boolean
| func_150224_n()|Style
| func_150225_c(Boolean b)|Style
| func_150227_a(Boolean b)|Style
| func_150228_d(Boolean b)|Style
| func_150229_g()|boolean
| func_150232_l()|Style
| func_150233_f()|boolean
| func_150234_e()|boolean
| func_150235_h()|ClickEvent
| func_150236_d()|boolean
| func_150237_e(Boolean b)|Style
| func_150238_a(TextFormatting t)|Style
| func_150241_a(ClickEvent c)|Style
| func_150242_c()|boolean
| func_179986_j()|String
| func_179989_a(String s)|Style
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MetadataSerializer

|Class
|--
|net.minecraft.client.resources.data.MetadataSerializer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_110503_a(String arg0, JsonObject arg1)|MetadataSection
| func_110504_a(MetadataSectionSerializer\<T> arg0, Class\<T> arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MetadataSection

|Interface
|--
|net.minecraft.client.resources.data.IMetadataSection

---

|Extends
|--

---

## BufferBuilder

|Class
|--
|net.minecraft.client.renderer.BufferBuilder

---

|Extends
|--

---

|Fields|Type
|--|--
|  animatedSprites|BitSet
|  animatedSpritesCached|BitSet
|  blockLayer|BlockRenderLayer
|  colorDisabled|boolean
|  drawing|boolean
|  field_178997_d|int
|  field_178999_b|IntBuffer
|  field_179000_c|FloatBuffer
|  field_179006_k|int
|  field_179010_r|boolean
|  multiTexture|boolean
|  renderEnv|RenderEnv
|  sVertexBuilder|SVertexBuilder
|  xOffset|double
|  yOffset|double
|  zOffset|double

---

|Methods|Return Type
|--|--
| drawMultiTexture()|void
| func_178962_a(int arg0, int arg1, int arg2, int arg3)|void
| func_178965_a()|void
| func_178966_f()|ByteBuffer
| func_178968_d(int i)|void
| func_178969_c(double arg0, double arg1, double arg2)|void
| func_178972_a(int arg0, int arg1, int arg2, int arg3)|void
| func_178973_g()|VertexFormat
| func_178975_e(float arg0, float arg1, float arg2)|void
| func_178977_d()|void
| func_178978_a(float arg0, float arg1, float arg2, int arg3)|void
| func_178979_i()|int
| func_178981_a(int[] i)|void
| func_178987_a(double arg0, double arg1, double arg2)|void
| func_178989_h()|int
| func_178990_f(float arg0, float arg1, float arg2)|void
| func_178993_a(BufferBuilder$State b)|void
| func_178994_b(float arg0, float arg1, float arg2, int arg3)|void
| func_181662_b(double arg0, double arg1, double arg2)|BufferBuilder
| func_181663_c(float arg0, float arg1, float arg2)|BufferBuilder
| func_181664_j()|int
| func_181666_a(float arg0, float arg1, float arg2, float arg3)|BufferBuilder
| func_181667_k()|void
| func_181668_a(int arg0, VertexFormat arg1)|void
| func_181669_b(int arg0, int arg1, int arg2, int arg3)|BufferBuilder
| func_181672_a()|BufferBuilder$State
| func_181674_a(float arg0, float arg1, float arg2)|void
| func_181675_d()|void
| func_187314_a(int arg0, int arg1)|BufferBuilder
| func_187315_a(double arg0, double arg1)|BufferBuilder
| func_78909_a(int i)|int
| func_78914_f()|void
| getRenderEnv(BlockAccess arg0, BlockState arg1, BlockPos arg2)|RenderEnv
| putBulkData(ByteBuffer b)|void
| putColorMultiplierRgba(float arg0, float arg1, float arg2, float arg3, int arg4)|void
| putColorRGBA(int arg0, int arg1, int arg2, int arg3, int arg4)|void
| putSprite(TextureAtlasSprite t)|void
| setSprite(TextureAtlasSprite t)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockModelRenderer

|Class
|--
|net.minecraft.client.renderer.BlockModelRenderer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178262_a(BakedModel arg0, float arg1, float arg2, float arg3, float arg4)|void
| func_178266_a(BakedModel arg0, BlockState arg1, float arg2, boolean arg3)|void
| func_178267_a(BlockAccess arg0, BakedModel arg1, BlockState arg2, BlockPos arg3, BufferBuilder arg4, boolean arg5)|boolean
| func_187493_a(BlockAccess arg0, BakedModel arg1, BlockState arg2, BlockPos arg3, BufferBuilder arg4, boolean arg5, long arg6)|boolean
| func_187495_a(BlockState arg0, BakedModel arg1, float arg2, float arg3, float arg4, float arg5)|void
| func_187497_c(BlockAccess arg0, BakedModel arg1, BlockState arg2, BlockPos arg3, BufferBuilder arg4, boolean arg5, long arg6)|boolean
| func_187498_b(BlockAccess arg0, BakedModel arg1, BlockState arg2, BlockPos arg3, BufferBuilder arg4, boolean arg5, long arg6)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockModelShapes

|Class
|--
|net.minecraft.client.renderer.BlockModelShapes

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_178129_a|Map\<BlockState, BakedModel>

---

|Methods|Return Type
|--|--
| func_178120_a()|BlockStateMapper
| func_178121_a(Block arg0, StateMapper arg1)|void
| func_178122_a(BlockState b)|TextureAtlasSprite
| func_178123_a(Block[] b)|void
| func_178124_c()|void
| func_178125_b(BlockState b)|BakedModel
| func_178126_b()|ModelManager
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BakedModel

|Interface
|--
|net.minecraft.client.renderer.block.model.IBakedModel

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_177552_f()|ItemCameraTransforms
| func_177554_e()|TextureAtlasSprite
| func_177555_b()|boolean
| func_177556_c()|boolean
| func_188616_a(BlockState arg0, EnumFacing arg1, long arg2)|List\<BakedQuad>
| func_188617_f()|ItemOverrideList
| func_188618_c()|boolean
| handlePerspective(ItemCameraTransforms$TransformType i)|Pair\<? extends net.minecraft.client.renderer.block.model.IBakedModel, Matrix4f>
| isAmbientOcclusion(BlockState b)|boolean

---

## DebugRenderer$IDebugRenderer

|Interface
|--
|net.minecraft.client.renderer.debug.DebugRenderer$IDebugRenderer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_190060_a(float arg0, long arg1)|void

---

## HotbarSnapshot

|Class
|--
|net.minecraft.client.settings.HotbarSnapshot

---

|Extends
|--
|ArrayList

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(int arg0, Object arg1)|void
| add(Object o)|boolean
| addAll(int arg0, Collection\<? extends E> arg1)|boolean
| addAll(Collection\<? extends E> c)|boolean
| clear()|void
| clone()|Object
| contains(Object o)|boolean
| containsAll(Collection\<?> c)|boolean
| ensureCapacity(int i)|void
| forEach(Consumer\<? super E> c)|void
| func_192833_a(NBTTagList n)|void
| func_192834_a()|NBTTagList
| get(int i)|Object
| indexOf(Object o)|int
| iterator()|Iterator\<E>
| lastIndexOf(Object o)|int
| listIterator(int i)|ListIterator\<E>
| listIterator()|ListIterator\<E>
| parallelStream()|Stream\<E>
| remove(Object o)|boolean
| remove(int i)|Object
| removeAll(Collection\<?> c)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| replaceAll(UnaryOperator\<E> u)|void
| retainAll(Collection\<?> c)|boolean
| set(int arg0, Object arg1)|Object
| size()|int
| sort(Comparator\<? super E> c)|void
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| subList(int arg0, int arg1)|List\<E>
| toArray()|Object[]
| toArray(Object[] o)|Object[]
| trimToSize()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Profiler$Result

|Class
|--
|net.minecraft.profiler.Profiler$Result

---

|Extends
|--
|Comparable

---

|Fields|Type
|--|--
|  field_76330_b|double
|  field_76331_c|String
|  field_76332_a|double

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Profiler$Result p)|int
| func_76329_a()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RenderChunk

|Class
|--
|net.minecraft.client.renderer.chunk.RenderChunk

---

|Extends
|--

---

|Fields|Type
|--|--
|  boundingBoxParent|AabbFrame
|  chunk|Chunk
|  chunkRegionEmpty|boolean
|  field_178586_f|BlockPos$MutableBlockPos
|  field_178587_g|ReentrantLock
|  field_178588_d|World
|  field_178589_e|RenderGlobal
|  field_178590_b|CompiledChunk
|  field_178591_c|AxisAlignedBB
|  field_181056_j|Set\<TileEntity>
|  playerUpdate|boolean
|  regionX|int
|  regionZ|int
|  renderInfo|RenderGlobal$ContainerLocalRenderInformation

---

|Methods|Return Type
|--|--
| func_178565_b(int i)|VertexBuffer
| func_178566_a()|void
| func_178568_j()|BlockPos
| func_178569_m()|boolean
| func_178570_a(float arg0, float arg1, float arg2, ChunkCompileTaskGenerator arg3)|void
| func_178571_g()|CompiledChunk
| func_178572_f()|void
| func_178573_a(BufferBuilder arg0, BlockPos arg1)|void
| func_178574_d()|ChunkCompileTaskGenerator
| func_178575_a(boolean b)|void
| func_178577_a(int i)|boolean
| func_178579_c()|ReentrantLock
| func_178580_a(CompiledChunk c)|void
| func_178581_b(float arg0, float arg1, float arg2, ChunkCompileTaskGenerator arg3)|void
| func_178582_e()|ChunkCompileTaskGenerator
| func_178584_a(BlockRenderLayer arg0, float arg1, float arg2, float arg3, BufferBuilder arg4, CompiledChunk arg5)|void
| func_178585_h()|void
| func_181701_a(EnumFacing e)|BlockPos
| func_188281_o()|boolean
| func_188282_m()|void
| func_188283_p()|World
| func_189562_a(int arg0, int arg1, int arg2)|void
| getRenderChunkNeighbour(EnumFacing e)|RenderChunk
| getRenderChunkOffset16(ViewFrustum arg0, EnumFacing arg1)|RenderChunk
| isBoundingBoxInFrustum(Camera arg0, int arg1)|boolean
| setRenderChunkNeighbour(EnumFacing arg0, RenderChunk arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CloudRenderer

|Class
|--
|net.optifine.render.CloudRenderer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| endUpdateGlList()|void
| prepareToRender(boolean arg0, int arg1, float arg2, Vec3d arg3)|void
| renderGlList()|void
| reset()|void
| shouldUpdateGlList()|boolean
| startUpdateGlList()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Sound

|Interface
|--
|net.minecraft.client.audio.ISound

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_147649_g()|float
| func_147650_b()|ResourceLocation
| func_147651_i()|float
| func_147652_d()|int
| func_147653_e()|float
| func_147654_h()|float
| func_147655_f()|float
| func_147656_j()|ISound$AttenuationType
| func_147657_c()|boolean
| func_184364_b()|Sound
| func_184365_d()|SoundCategory
| func_184366_a(SoundHandler s)|SoundEventAccessor

---

## ShaderGroup

|Class
|--
|net.minecraft.client.shader.ShaderGroup

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_148018_a(float f)|void
| func_148020_a(String arg0, int arg1, int arg2)|void
| func_148021_a()|void
| func_148022_b()|String
| func_148023_a(String arg0, Framebuffer arg1, Framebuffer arg2)|Shader
| func_148026_a(int arg0, int arg1)|void
| func_152765_a(TextureManager arg0, ResourceLocation arg1)|void
| func_177066_a(String s)|Framebuffer
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ChunkRenderDispatcher

|Class
|--
|net.minecraft.client.renderer.chunk.ChunkRenderDispatcher

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178504_a()|String
| func_178505_b(RenderChunk r)|boolean
| func_178507_a(RenderChunk r)|boolean
| func_178509_c(RenderChunk r)|boolean
| func_178511_d()|ChunkCompileTaskGenerator
| func_178512_a(RegionRenderCacheBuilder r)|void
| func_178513_e()|void
| func_178514_b()|void
| func_178515_c()|RegionRenderCacheBuilder
| func_178516_a(long l)|boolean
| func_188244_g()|void
| func_188245_a(BlockRenderLayer arg0, BufferBuilder arg1, RenderChunk arg2, CompiledChunk arg3, double arg4)|ListenableFuture\<Object>
| func_188247_f()|boolean
| func_188248_h()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ChunkRenderContainer

|Class
|--
|net.minecraft.client.renderer.ChunkRenderContainer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178001_a(BlockRenderLayer b)|void
| func_178002_a(RenderChunk arg0, BlockRenderLayer arg1)|void
| func_178003_a(RenderChunk r)|void
| func_178004_a(double arg0, double arg1, double arg2)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ClippingHelper

|Class
|--
|net.minecraft.client.renderer.culling.ClippingHelper

---

|Extends
|--

---

|Fields|Type
|--|--
|  disabled|boolean
|  field_178625_b|float[]
|  field_178626_c|float[]
|  field_78554_d|float[]
|  field_78557_a|float[][]

---

|Methods|Return Type
|--|--
| func_78553_b(double arg0, double arg1, double arg2, double arg3, double arg4, double arg5)|boolean
| isBoxInFrustumFully(double arg0, double arg1, double arg2, double arg3, double arg4, double arg5)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Vector3d

|Class
|--
|net.minecraft.client.renderer.Vector3d

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_181059_a|double
|  field_181060_b|double
|  field_181061_c|double

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RenderChunkFactory

|Interface
|--
|net.minecraft.client.renderer.chunk.IRenderChunkFactory

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_189565_a(World arg0, RenderGlobal arg1, int arg2)|RenderChunk

---

## ViewFrustum

|Class
|--
|net.minecraft.client.renderer.ViewFrustum

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_178164_f|RenderChunk[]

---

|Methods|Return Type
|--|--
| deleteVboRegions()|void
| func_178160_a()|void
| func_178161_a(BlockPos b)|RenderChunk
| func_178163_a(double arg0, double arg1)|void
| func_187474_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5, boolean arg6)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## VertexBuffer

|Class
|--
|net.minecraft.client.renderer.vertex.VertexBuffer

---

|Extends
|--

---

|Fields|Type
|--|--
|  vboRange|VboRange
|  vboRegion|VboRegion

---

|Methods|Return Type
|--|--
| func_177358_a(int i)|void
| func_177359_a()|void
| func_177361_b()|void
| func_177362_c()|void
| func_181722_a(ByteBuffer b)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## VertexFormat

|Class
|--
|net.minecraft.client.renderer.vertex.VertexFormat

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_177338_f()|int
| func_177339_a()|void
| func_177340_e()|int
| func_177342_c()|int
| func_177343_g()|List\<VertexFormatElement>
| func_177344_b(int i)|int
| func_177345_h()|int
| func_177346_d()|boolean
| func_177347_a(int i)|boolean
| func_177348_c(int i)|VertexFormatElement
| func_177350_b()|boolean
| func_181719_f()|int
| func_181720_d(int i)|int
| func_181721_a(VertexFormatElement v)|VertexFormat
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## DestroyBlockProgress

|Class
|--
|net.minecraft.client.renderer.DestroyBlockProgress

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_180246_b()|BlockPos
| func_73106_e()|int
| func_73107_a(int i)|void
| func_82743_f()|int
| func_82744_b(int i)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RenderGlobal$ContainerLocalRenderInformation

|Class
|--
|net.minecraft.client.renderer.RenderGlobal$ContainerLocalRenderInformation

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_178034_b|EnumFacing
|  field_178035_c|int
|  field_178036_a|RenderChunk

---

|Methods|Return Type
|--|--
| func_189560_a(EnumFacing e)|boolean
| func_189561_a(byte arg0, EnumFacing arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RenderEnv

|Class
|--
|net.optifine.render.RenderEnv

---

|Extends
|--

---

|Fields|Type
|--|--
|  aoFace|BlockModelRenderer$AmbientOcclusionFace
|  blockId|int
|  blockState|BlockState
|  borderDirections|EnumFacing[]
|  borderFlags|boolean[]
|  borderFlags2|boolean[]
|  borderFlags3|boolean[]
|  boundsFlags|BitSet
|  breakingAnimation|boolean
|  colorizerBlockPosM|BlockPosM
|  listQuadsCustomizer|List\<BakedQuad>
|  metadata|int
|  overlaysRendered|boolean
|  quadBounds|float[]
|  regionRenderCacheBuilder|RegionRenderCacheBuilder
|  smartLeaves|boolean

---

|Methods|Return Type
|--|--
| getArrayQuadsCtm(BakedQuad arg0, BakedQuad arg1)|BakedQuad[]
| getArrayQuadsCtm(BakedQuad b)|BakedQuad[]
| getArrayQuadsCtm(BakedQuad arg0, BakedQuad arg1, BakedQuad arg2, BakedQuad arg3)|BakedQuad[]
| getArrayQuadsCtm(BakedQuad arg0, BakedQuad arg1, BakedQuad arg2)|BakedQuad[]
| getListQuadsCtmMultipass(BakedQuad[] b)|List\<BakedQuad>
| getListQuadsOverlay(BlockRenderLayer b)|ListQuadsOverlay
| reset(BlockAccess arg0, BlockState arg1, BlockPos arg2)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Long2ObjectMap

|Interface
|--
|it.unimi.dsi.fastutil.longs.Long2ObjectMap

---

|Extends
|--
|Long2ObjectFunction
|Map

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| clear()|void
| clear()|void
| compute(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| computeIfAbsent(Object arg0, Function\<? super K, ? extends V> arg1)|Object
| computeIfPresent(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| containsKey(long l)|boolean
| containsKey(Object o)|boolean
| containsKey(Object o)|boolean
| containsValue(Object o)|boolean
| defaultReturnValue(Object o)|void
| defaultReturnValue()|Object
| entrySet()|ObjectSet\<java.util.Map$Entry\<java.lang.Long, V>>
| entrySet()|Set\<java.util.Map$Entry\<K, V>>
| forEach(BiConsumer\<? super K, ? super V> b)|void
| get(long l)|Object
| get(Object o)|Object
| get(Object o)|Object
| getOrDefault(Object arg0, Object arg1)|Object
| keySet()|LongSet
| keySet()|Set\<K>
| long2ObjectEntrySet()|ObjectSet\<it.unimi.dsi.fastutil.longs.Long2ObjectMap$Entry\<V>>
| merge(Object arg0, Object arg1, BiFunction\<? super V, ? super V, ? extends V> arg2)|Object
| put(long arg0, Object arg1)|Object
| put(Object arg0, Object arg1)|Object
| put(Object arg0, Object arg1)|Object
| putAll(Map\<? extends K, ? extends V> m)|void
| putIfAbsent(Object arg0, Object arg1)|Object
| remove(long l)|Object
| remove(Object o)|Object
| remove(Object o)|Object
| remove(Object arg0, Object arg1)|boolean
| replace(Object arg0, Object arg1)|Object
| replace(Object arg0, Object arg1, Object arg2)|boolean
| replaceAll(BiFunction\<? super K, ? super V, ? extends V> b)|void
| size()|int
| size()|int
| values()|ObjectCollection\<V>
| values()|Collection\<V>

---

## Camera

|Interface
|--
|net.minecraft.client.renderer.culling.ICamera

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_78546_a(AxisAlignedBB a)|boolean
| func_78547_a(double arg0, double arg1, double arg2)|void

---

## Tessellator

|Class
|--
|net.minecraft.client.renderer.Tessellator

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178180_c()|BufferBuilder
| func_78381_a()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AbstractClientPlayer

|Class
|--
|net.minecraft.client.entity.AbstractClientPlayer

---

|Extends
|--
|EntityPlayer

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  defaultEyeHeight|float
|  displayNameString|String
|  entityData|NBTTagCompound
|  entityShoulderLeft|EntityShoulderRiding
|  entityShoulderRight|EntityShoulderRiding
|  eyeHeight|float
|  field_110153_bc|float
|  field_110158_av|int
|  field_175152_f|int
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_184617_aD|int
|  field_184618_aE|float
|  field_184619_aG|float
|  field_184622_au|EnumHand
|  field_184627_bm|ItemStack
|  field_184628_bn|int
|  field_184835_a|float
|  field_184836_b|float
|  field_184837_c|float
|  field_190534_ay|int
|  field_191988_bg|float
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_70701_bs|float
|  field_70702_br|float
|  field_70703_bu|boolean
|  field_70704_bt|float
|  field_70718_bc|int
|  field_70720_be|int
|  field_70721_aZ|float
|  field_70725_aQ|int
|  field_70726_aT|float
|  field_70727_aS|float
|  field_70732_aI|float
|  field_70733_aJ|float
|  field_70737_aN|int
|  field_70738_aO|int
|  field_70739_aP|float
|  field_70747_aH|float
|  field_70755_b|EntityLivingBase
|  field_70758_at|float
|  field_70759_as|float
|  field_70760_ar|float
|  field_70761_aq|float
|  field_70769_ao|float
|  field_70770_ap|float
|  field_70771_an|int
|  field_71067_cb|int
|  field_71068_ca|int
|  field_71069_bz|Container
|  field_71070_bA|Container
|  field_71071_by|InventoryPlayer
|  field_71075_bZ|PlayerCapabilities
|  field_71076_b|int
|  field_71079_bU|float
|  field_71081_bT|BlockPos
|  field_71082_cx|float
|  field_71083_bS|boolean
|  field_71085_bR|double
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71089_bV|float
|  field_71090_bL|int
|  field_71091_bM|double
|  field_71093_bK|int
|  field_71094_bP|double
|  field_71095_bQ|double
|  field_71096_bN|double
|  field_71097_bO|double
|  field_71104_cf|EntityFishHook
|  field_71106_cc|float
|  field_71107_bF|float
|  field_71109_bG|float
|  field_82151_R|float
|  field_82153_h|int
|  field_82175_bq|boolean
|  field_98038_p|boolean
|  itemInUseMaxDuration|int
|  locationOfCape|ResourceLocation
|  nameClear|String
|  persistentID|UUID
|  prefixes|Collection\<TextComponent>
|  spawnDimension|int
|  suffixes|Collection\<TextComponent>
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| addPrefix(TextComponent t)|void
| addSuffix(TextComponent t)|void
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| curePotionEffects(ItemStack i)|void
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_110124_au()|UUID
| func_110138_aP()|float
| func_110139_bj()|float
| func_110140_aT()|AbstractAttributeMap
| func_110142_aN()|CombatTracker
| func_110143_aJ()|float
| func_110144_aD()|EntityLivingBase
| func_110145_l(Entity e)|void
| func_110148_a(Attribute a)|AttributeInstance
| func_110149_m(float f)|void
| func_110303_q()|ResourceLocation
| func_110306_p()|ResourceLocation
| func_130011_c(Entity e)|void
| func_130014_f_()|World
| func_142013_aG()|int
| func_142015_aE()|int
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_146097_a(ItemStack arg0, boolean arg1, boolean arg2)|EntityItem
| func_146103_bH()|GameProfile
| func_146105_b(TextComponent arg0, boolean arg1)|void
| func_152111_bt()|void
| func_152112_bu()|void
| func_152122_n()|boolean
| func_152123_o()|boolean
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_175138_ci()|int
| func_175140_cp()|boolean
| func_175141_a(TileEntitySign t)|void
| func_175142_cm()|boolean
| func_175144_cb()|boolean
| func_175145_a(StatBase s)|void
| func_175146_a(LockCode l)|boolean
| func_175148_a(EnumPlayerModelParts e)|boolean
| func_175149_v()|boolean
| func_175150_k(boolean b)|void
| func_175151_a(BlockPos arg0, EnumFacing arg1, ItemStack arg2)|boolean
| func_175154_l()|String
| func_175155_b()|NetworkPlayerInfo
| func_175156_o()|float
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180468_a(InteractionObject i)|void
| func_180469_a(BlockPos b)|EntityPlayer$SleepResult
| func_180470_cg()|BlockPos
| func_180472_a(Merchant m)|void
| func_180473_a(BlockPos arg0, boolean arg1)|void
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_184582_a(EntityEquipmentSlot e)|ItemStack
| func_184583_d(DamageSource d)|boolean
| func_184585_cz()|boolean
| func_184586_b(EnumHand e)|ItemStack
| func_184587_cr()|boolean
| func_184589_d(Potion p)|void
| func_184591_cq()|EnumHandSide
| func_184592_cb()|ItemStack
| func_184595_k(double arg0, double arg1, double arg2)|boolean
| func_184596_c(Potion p)|PotionEffect
| func_184597_cx()|void
| func_184598_c(EnumHand e)|void
| func_184599_cB()|int
| func_184600_cs()|EnumHand
| func_184602_cy()|void
| func_184603_cC()|boolean
| func_184605_cv()|int
| func_184607_cu()|ItemStack
| func_184609_a(EnumHand e)|void
| func_184611_a(EnumHand arg0, ItemStack arg1)|void
| func_184612_cw()|int
| func_184613_cA()|boolean
| func_184614_ca()|ItemStack
| func_184809_a(CommandBlockBaseLogic c)|void
| func_184810_cG()|void
| func_184811_cZ()|CooldownTracker
| func_184812_l_()|boolean
| func_184813_a(BlockState b)|float
| func_184814_a(ItemStack arg0, EnumHand arg1)|void
| func_184816_a(EntityItem e)|ItemStack
| func_184817_da()|float
| func_184818_cX()|float
| func_184819_a(EnumHandSide e)|void
| func_184821_cY()|void
| func_184823_b(BlockState b)|boolean
| func_184824_a(TileEntityCommandBlock t)|void
| func_184825_o(float f)|float
| func_184826_a(AbstractHorse arg0, Inventory arg1)|void
| func_184833_s()|boolean
| func_184834_t()|ResourceLocation
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_189748_bU()|DamageSource
| func_189807_a(TileEntityStructure t)|void
| func_189808_dh()|boolean
| func_190530_aW()|boolean
| func_190630_a(EntityEquipmentSlot e)|boolean
| func_190631_cK()|boolean
| func_190775_a(Entity arg0, EnumHand arg1)|EnumActionResult
| func_190777_m(boolean b)|void
| func_191521_c(ItemStack i)|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_191986_a(float arg0, float arg1, float arg2)|void
| func_191987_a(BlockPos arg0, boolean arg1)|void
| func_192021_a(List\<Recipe> l)|void
| func_192022_b(List\<Recipe> l)|void
| func_192023_dk()|NBTTagCompound
| func_192024_a(ItemStack arg0, int arg1)|void
| func_192025_dl()|NBTTagCompound
| func_192027_g(NBTTagCompound n)|boolean
| func_193076_bZ()|Map\<Potion, PotionEffect>
| func_193102_a(ResourceLocation[] r)|void
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70065_x()|void
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70604_c(EntityLivingBase e)|void
| func_70606_j(float f)|void
| func_70608_bn()|boolean
| func_70613_aW()|boolean
| func_70617_f_()|boolean
| func_70631_g_()|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70636_d()|void
| func_70637_d(boolean b)|void
| func_70643_av()|EntityLivingBase
| func_70644_a(Potion p)|boolean
| func_70645_a(DamageSource d)|void
| func_70648_aU()|boolean
| func_70651_bq()|Collection\<PotionEffect>
| func_70652_k(Entity e)|boolean
| func_70653_a(Entity arg0, float arg1, double arg2, double arg3)|void
| func_70654_ax()|int
| func_70658_aO()|int
| func_70659_e(float f)|void
| func_70660_b(Potion p)|PotionEffect
| func_70662_br()|boolean
| func_70664_aZ()|void
| func_70668_bt()|EnumCreatureAttribute
| func_70669_a(ItemStack i)|void
| func_70674_bp()|void
| func_70676_i(float f)|Vec3d
| func_70678_g(float f)|float
| func_70681_au()|Random
| func_70685_l(Entity e)|boolean
| func_70687_e(PotionEffect p)|boolean
| func_70689_ay()|float
| func_70690_d(PotionEffect p)|void
| func_70691_i(float f)|void
| func_70996_bM()|boolean
| func_70999_a(boolean arg0, boolean arg1, boolean arg2)|void
| func_71000_j(double arg0, double arg1, double arg2)|void
| func_71001_a(Entity arg0, int arg1)|void
| func_71004_bE()|void
| func_71005_bN()|InventoryEnderChest
| func_71007_a(Inventory i)|void
| func_71009_b(Entity e)|void
| func_71016_p()|void
| func_71019_a(ItemStack arg0, boolean arg1)|EntityItem
| func_71020_j(float f)|void
| func_71023_q(int i)|void
| func_71024_bL()|FoodStats
| func_71026_bH()|boolean
| func_71029_a(StatBase s)|void
| func_71033_a(GameType g)|void
| func_71037_bA()|int
| func_71040_bB(boolean b)|EntityItem
| func_71043_e(boolean b)|boolean
| func_71047_c(Entity e)|void
| func_71050_bK()|int
| func_71051_bG()|float
| func_71053_j()|void
| func_71059_n(Entity e)|void
| func_71060_bI()|int
| func_71064_a(StatBase arg0, int arg1)|void
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_82242_a(int i)|void
| func_82243_bO()|float
| func_82245_bX()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_85034_r(int i)|void
| func_85035_bI()|int
| func_85039_t(int i)|void
| func_85040_s(int i)|void
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_94060_bK()|EntityLivingBase
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96122_a(EntityPlayer e)|boolean
| func_96123_co()|Scoreboard
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| getBedLocation(int i)|BlockPos
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getDigSpeed(BlockState arg0, BlockPos arg1)|float
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| hasElytraCape()|boolean
| hasSpawnDimension()|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| isSpawnForced(int i)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| openGui(Object arg0, int arg1, World arg2, int arg3, int arg4, int arg5)|void
| refreshDisplayName()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| setSpawnChunk(BlockPos arg0, boolean arg1, int arg2)|void
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderFaceForward(EntityPlayer e)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityShoulderRiding

|Class
|--
|net.minecraft.entity.passive.EntityShoulderRiding

---

|Extends
|--
|EntityTameable

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_110153_bc|float
|  field_110158_av|int
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_184617_aD|int
|  field_184618_aE|float
|  field_184619_aG|float
|  field_184622_au|EnumHand
|  field_184627_bm|ItemStack
|  field_184628_bn|int
|  field_190534_ay|int
|  field_191988_bg|float
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_70696_bz|EntityLivingBase
|  field_70701_bs|float
|  field_70702_br|float
|  field_70703_bu|boolean
|  field_70704_bt|float
|  field_70714_bg|EntityAITasks
|  field_70715_bh|EntityAITasks
|  field_70718_bc|int
|  field_70720_be|int
|  field_70721_aZ|float
|  field_70725_aQ|int
|  field_70726_aT|float
|  field_70727_aS|float
|  field_70728_aV|int
|  field_70732_aI|float
|  field_70733_aJ|float
|  field_70737_aN|int
|  field_70738_aO|int
|  field_70739_aP|float
|  field_70747_aH|float
|  field_70755_b|EntityLivingBase
|  field_70757_a|int
|  field_70758_at|float
|  field_70759_as|float
|  field_70760_ar|float
|  field_70761_aq|float
|  field_70769_ao|float
|  field_70770_ap|float
|  field_70771_an|int
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_82175_bq|boolean
|  field_98038_p|boolean
|  itemInUseMaxDuration|int
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| curePotionEffects(ItemStack i)|void
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_104002_bU()|boolean
| func_110124_au()|UUID
| func_110138_aP()|float
| func_110139_bj()|float
| func_110140_aT()|AbstractAttributeMap
| func_110142_aN()|CombatTracker
| func_110143_aJ()|float
| func_110144_aD()|EntityLivingBase
| func_110145_l(Entity e)|void
| func_110148_a(Attribute a)|AttributeInstance
| func_110149_m(float f)|void
| func_110160_i(boolean arg0, boolean arg1)|void
| func_110162_b(Entity arg0, boolean arg1)|void
| func_110163_bv()|void
| func_110166_bE()|Entity
| func_110167_bD()|boolean
| func_110173_bK()|boolean
| func_110174_bM()|float
| func_110175_bO()|boolean
| func_110177_bN()|void
| func_110195_a(int i)|void
| func_130011_c(Entity e)|void
| func_130014_f_()|World
| func_142013_aG()|int
| func_142015_aE()|int
| func_142018_a(EntityLivingBase arg0, EntityLivingBase arg1)|boolean
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_146082_f(EntityPlayer e)|void
| func_152111_bt()|void
| func_152112_bu()|void
| func_152114_e(EntityLivingBase e)|boolean
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_175446_cd()|boolean
| func_175449_a(BlockPos arg0, int arg1)|void
| func_175501_a(int arg0, boolean arg1)|void
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180482_a(DifficultyInstance arg0, EntityLivingData arg1)|EntityLivingData
| func_180484_a(BlockPos b)|float
| func_180485_d(BlockPos b)|boolean
| func_180486_cf()|BlockPos
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_184582_a(EntityEquipmentSlot e)|ItemStack
| func_184583_d(DamageSource d)|boolean
| func_184585_cz()|boolean
| func_184586_b(EnumHand e)|ItemStack
| func_184587_cr()|boolean
| func_184589_d(Potion p)|void
| func_184591_cq()|EnumHandSide
| func_184592_cb()|ItemStack
| func_184595_k(double arg0, double arg1, double arg2)|boolean
| func_184596_c(Potion p)|PotionEffect
| func_184597_cx()|void
| func_184598_c(EnumHand e)|void
| func_184599_cB()|int
| func_184600_cs()|EnumHand
| func_184602_cy()|void
| func_184603_cC()|boolean
| func_184605_cv()|int
| func_184607_cu()|ItemStack
| func_184609_a(EnumHand e)|void
| func_184611_a(EnumHand arg0, ItemStack arg1)|void
| func_184612_cw()|int
| func_184613_cA()|boolean
| func_184614_ca()|ItemStack
| func_184638_cS()|boolean
| func_184641_n(boolean b)|void
| func_184642_a(EntityEquipmentSlot arg0, float arg1)|void
| func_184643_a(PathNodeType p)|float
| func_184644_a(PathNodeType arg0, float arg1)|void
| func_184645_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184646_p(float f)|void
| func_184649_cE()|int
| func_184652_a(EntityPlayer e)|boolean
| func_184753_b()|UUID
| func_184754_b(UUID u)|void
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_189748_bU()|DamageSource
| func_190530_aW()|boolean
| func_190630_a(EntityEquipmentSlot e)|boolean
| func_190631_cK()|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_191986_a(float arg0, float arg1, float arg2)|void
| func_191987_a(BlockPos arg0, boolean arg1)|void
| func_191989_p(float f)|void
| func_191993_do()|EntityPlayerMP
| func_191994_f(EntityPlayer e)|boolean
| func_191995_du()|boolean
| func_193076_bZ()|Map\<Potion, PotionEffect>
| func_193101_c(EntityPlayer e)|void
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70058_J()|boolean
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70601_bi()|boolean
| func_70603_bj()|float
| func_70604_c(EntityLivingBase e)|void
| func_70605_aq()|EntityMoveHelper
| func_70606_j(float f)|void
| func_70608_bn()|boolean
| func_70613_aW()|boolean
| func_70615_aA()|void
| func_70617_f_()|boolean
| func_70624_b(EntityLivingBase e)|void
| func_70625_a(Entity arg0, float arg1, float arg2)|void
| func_70627_aG()|int
| func_70631_g_()|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70635_at()|EntitySenses
| func_70636_d()|void
| func_70637_d(boolean b)|void
| func_70638_az()|EntityLivingBase
| func_70641_bl()|int
| func_70642_aH()|void
| func_70643_av()|EntityLivingBase
| func_70644_a(Potion p)|boolean
| func_70645_a(DamageSource d)|void
| func_70646_bf()|int
| func_70648_aU()|boolean
| func_70651_bq()|Collection\<PotionEffect>
| func_70652_k(Entity e)|boolean
| func_70653_a(Entity arg0, float arg1, double arg2, double arg3)|void
| func_70654_ax()|int
| func_70656_aK()|void
| func_70657_f(float f)|void
| func_70658_aO()|int
| func_70659_e(float f)|void
| func_70660_b(Potion p)|PotionEffect
| func_70661_as()|PathNavigate
| func_70662_br()|boolean
| func_70668_bt()|EnumCreatureAttribute
| func_70669_a(ItemStack i)|void
| func_70671_ap()|EntityLookHelper
| func_70674_bp()|void
| func_70676_i(float f)|Vec3d
| func_70678_g(float f)|float
| func_70681_au()|Random
| func_70683_ar()|EntityJumpHelper
| func_70685_l(Entity e)|boolean
| func_70686_a(Class\<? extends net.minecraft.entity.EntityLivingBase> c)|boolean
| func_70687_e(PotionEffect p)|boolean
| func_70689_ay()|float
| func_70690_d(PotionEffect p)|void
| func_70691_i(float f)|void
| func_70781_l()|boolean
| func_70873_a(int i)|void
| func_70874_b()|int
| func_70875_t()|void
| func_70877_b(ItemStack i)|boolean
| func_70878_b(EntityAnimal e)|boolean
| func_70880_s()|boolean
| func_70902_q()|EntityLivingBase
| func_70902_q()|Entity
| func_70903_f(boolean b)|void
| func_70904_g(boolean b)|void
| func_70906_o()|boolean
| func_70907_r()|EntityAISit
| func_70909_n()|boolean
| func_71001_a(Entity arg0, int arg1)|void
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_82171_bF()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_85034_r(int i)|void
| func_85035_bI()|int
| func_90011_a(EntityAgeable e)|EntityAgeable
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_94060_bK()|EntityLivingBase
| func_94061_f(boolean b)|void
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| func_98052_bS()|boolean
| func_98053_h(boolean b)|void
| func_98054_a(boolean b)|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderFaceForward(EntityPlayer e)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RecipeBook

|Class
|--
|net.minecraft.stats.RecipeBook

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_192810_b(boolean b)|void
| func_192812_b()|boolean
| func_192813_a(boolean b)|void
| func_192815_c()|boolean
| func_193824_a(RecipeBook r)|void
| func_193825_e(Recipe r)|void
| func_193830_f(Recipe r)|boolean
| func_193831_b(Recipe r)|void
| func_194073_a(Recipe r)|void
| func_194074_f(Recipe r)|void
| func_194076_e(Recipe r)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MovementInput

|Class
|--
|net.minecraft.util.MovementInput

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_187255_c|boolean
|  field_187256_d|boolean
|  field_187257_e|boolean
|  field_187258_f|boolean
|  field_192832_b|float
|  field_78899_d|boolean
|  field_78901_c|boolean
|  field_78902_a|float

---

|Methods|Return Type
|--|--
| func_190020_b()|Vec2f
| func_78898_a()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## StatisticsManager

|Class
|--
|net.minecraft.stats.StatisticsManager

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_150871_b(EntityPlayer arg0, StatBase arg1, int arg2)|void
| func_150873_a(EntityPlayer arg0, StatBase arg1, int arg2)|void
| func_77444_a(StatBase s)|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NetworkPlayerInfo

|Class
|--
|net.minecraft.client.network.NetworkPlayerInfo

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_178863_g|String
|  field_187107_a|Map\<MinecraftProfileTexture$Type, ResourceLocation>

---

|Methods|Return Type
|--|--
| func_178835_l()|int
| func_178836_b(int i)|void
| func_178837_g()|ResourceLocation
| func_178838_a(int i)|void
| func_178839_a(GameType g)|void
| func_178843_c(long l)|void
| func_178844_b(long l)|void
| func_178845_a()|GameProfile
| func_178846_a(long l)|void
| func_178847_n()|long
| func_178848_b()|GameType
| func_178850_i()|ScorePlayerTeam
| func_178851_f()|String
| func_178853_c()|int
| func_178854_k()|TextComponent
| func_178855_p()|long
| func_178856_e()|boolean
| func_178857_c(int i)|void
| func_178858_o()|long
| func_178859_a(TextComponent t)|void
| func_178860_m()|int
| func_178861_h()|ResourceLocation
| func_187106_i()|ResourceLocation
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockPos$MutableBlockPos

|Class
|--
|net.minecraft.util.math.BlockPos$MutableBlockPos

---

|Extends
|--
|BlockPos

---

|Methods|Return Type
|--|--
| compareTo(Vec3i v)|int
| compareTo(Object o)|int
| func_177951_i(Vec3i v)|double
| func_177952_p()|int
| func_177954_c(double arg0, double arg1, double arg2)|double
| func_177955_d(Vec3i v)|Vec3i
| func_177955_d(Vec3i v)|BlockPos
| func_177956_o()|int
| func_177957_d(double arg0, double arg1, double arg2)|double
| func_177958_n()|int
| func_177963_a(double arg0, double arg1, double arg2)|BlockPos
| func_177964_d(int i)|BlockPos
| func_177965_g(int i)|BlockPos
| func_177967_a(EnumFacing arg0, int arg1)|BlockPos
| func_177968_d()|BlockPos
| func_177970_e(int i)|BlockPos
| func_177971_a(Vec3i v)|BlockPos
| func_177972_a(EnumFacing e)|BlockPos
| func_177973_b(Vec3i v)|BlockPos
| func_177974_f()|BlockPos
| func_177976_e()|BlockPos
| func_177977_b()|BlockPos
| func_177978_c()|BlockPos
| func_177979_c(int i)|BlockPos
| func_177981_b(int i)|BlockPos
| func_177982_a(int arg0, int arg1, int arg2)|BlockPos
| func_177984_a()|BlockPos
| func_177985_f(int i)|BlockPos
| func_177986_g()|long
| func_181079_c(int arg0, int arg1, int arg2)|BlockPos$MutableBlockPos
| func_185332_f(int arg0, int arg1, int arg2)|double
| func_185334_h()|BlockPos
| func_185336_p(int i)|void
| func_189532_c(double arg0, double arg1, double arg2)|BlockPos$MutableBlockPos
| func_189533_g(Vec3i v)|BlockPos$MutableBlockPos
| func_189534_c(EnumFacing arg0, int arg1)|BlockPos$MutableBlockPos
| func_189535_a(Entity e)|BlockPos$MutableBlockPos
| func_189536_c(EnumFacing e)|BlockPos$MutableBlockPos
| func_190942_a(Rotation r)|BlockPos
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ChunkProviderClient

|Class
|--
|net.minecraft.client.multiplayer.ChunkProviderClient

---

|Extends
|--
|ChunkProvider

---

|Methods|Return Type
|--|--
| func_186025_d(int arg0, int arg1)|Chunk
| func_186026_b(int arg0, int arg1)|Chunk
| func_191062_e(int arg0, int arg1)|boolean
| func_73148_d()|String
| func_73156_b()|boolean
| func_73158_c(int arg0, int arg1)|Chunk
| func_73234_b(int arg0, int arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Tickable

|Interface
|--
|net.minecraft.client.renderer.texture.ITickable

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_110550_d()|void

---

## TextureObject

|Interface
|--
|net.minecraft.client.renderer.texture.ITextureObject

---

|Extends
|--

---

|Fields|Type
|--|--
|  multiTexID|MultiTexID

---

|Methods|Return Type
|--|--
| func_110551_a(ResourceManager r)|void
| func_110552_b()|int
| func_174935_a()|void
| func_174936_b(boolean arg0, boolean arg1)|void

---

## DynamicTexture

|Class
|--
|net.minecraft.client.renderer.texture.DynamicTexture

---

|Extends
|--
|AbstractTexture

---

|Fields|Type
|--|--
|  multiTex|MultiTexID
|  multiTexID|MultiTexID

---

|Methods|Return Type
|--|--
| func_110551_a(ResourceManager r)|void
| func_110552_b()|int
| func_110564_a()|void
| func_110565_c()|int[]
| func_147631_c()|void
| func_174935_a()|void
| func_174936_b(boolean arg0, boolean arg1)|void
| func_174937_a(boolean arg0, boolean arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TickableTextureObject

|Interface
|--
|net.minecraft.client.renderer.texture.ITickableTextureObject

---

|Extends
|--
|TextureObject
|Tickable

---

|Fields|Type
|--|--
|  multiTexID|MultiTexID

---

|Methods|Return Type
|--|--
| func_110550_d()|void
| func_110551_a(ResourceManager r)|void
| func_110552_b()|int
| func_174935_a()|void
| func_174936_b(boolean arg0, boolean arg1)|void

---

## ChatType

|Class
|--
|net.minecraft.util.text.ChatType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_192583_a()|byte
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GuiNewChat

|Class
|--
|net.minecraft.client.gui.GuiNewChat

---

|Extends
|--
|Gui

---

|Fields|Type
|--|--
|  field_73735_i|float

---

|Methods|Return Type
|--|--
| func_146227_a(TextComponent t)|void
| func_146228_f()|int
| func_146229_b(int i)|void
| func_146230_a(int i)|void
| func_146231_a(boolean b)|void
| func_146232_i()|int
| func_146234_a(TextComponent arg0, int arg1)|void
| func_146236_a(int arg0, int arg1)|TextComponent
| func_146238_c()|List\<String>
| func_146239_a(String s)|void
| func_146240_d()|void
| func_146241_e()|boolean
| func_146242_c(int i)|void
| func_146244_h()|float
| func_146245_b()|void
| func_146246_g()|int
| func_175174_a(float arg0, float arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_175175_a(int arg0, int arg1, TextureAtlasSprite arg2, int arg3, int arg4)|void
| func_73729_b(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73731_b(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73732_a(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73733_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GuiPlayerTabOverlay

|Class
|--
|net.minecraft.client.gui.GuiPlayerTabOverlay

---

|Extends
|--
|Gui

---

|Fields|Type
|--|--
|  field_73735_i|float

---

|Methods|Return Type
|--|--
| func_175174_a(float arg0, float arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_175175_a(int arg0, int arg1, TextureAtlasSprite arg2, int arg3, int arg4)|void
| func_175243_a(NetworkPlayerInfo n)|String
| func_175244_b(TextComponent t)|void
| func_175246_a(boolean b)|void
| func_175248_a(TextComponent t)|void
| func_175249_a(int arg0, Scoreboard arg1, ScoreObjective arg2)|void
| func_181030_a()|void
| func_73729_b(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73731_b(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73732_a(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73733_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GuiSpectator

|Class
|--
|net.minecraft.client.gui.GuiSpectator

---

|Extends
|--
|Gui
|SpectatorMenuRecipient

---

|Fields|Type
|--|--
|  field_73735_i|float

---

|Methods|Return Type
|--|--
| func_175174_a(float arg0, float arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_175175_a(int arg0, int arg1, TextureAtlasSprite arg2, int arg3, int arg4)|void
| func_175257_a(SpectatorMenu s)|void
| func_175259_b(int i)|void
| func_175260_a(int i)|void
| func_175261_b()|void
| func_175262_a()|boolean
| func_175263_a(ScaledResolution s)|void
| func_175264_a(ScaledResolution arg0, float arg1)|void
| func_73729_b(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73731_b(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73732_a(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73733_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GuiBossOverlay

|Class
|--
|net.minecraft.client.gui.GuiBossOverlay

---

|Extends
|--
|Gui

---

|Fields|Type
|--|--
|  field_184060_g|Map\<UUID, BossInfoClient>
|  field_73735_i|float

---

|Methods|Return Type
|--|--
| func_175174_a(float arg0, float arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_175175_a(int arg0, int arg1, TextureAtlasSprite arg2, int arg3, int arg4)|void
| func_184051_a()|void
| func_184053_e()|boolean
| func_184054_d()|boolean
| func_184055_a(SPacketUpdateBossInfo s)|void
| func_184056_f()|boolean
| func_184057_b()|void
| func_73729_b(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73731_b(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73732_a(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73733_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MapItemRenderer

|Class
|--
|net.minecraft.client.gui.MapItemRenderer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_148246_a(MapData m)|void
| func_148249_a()|void
| func_148250_a(MapData arg0, boolean arg1)|void
| func_191205_a(String s)|MapItemRenderer$Instance
| func_191207_a(MapItemRenderer$Instance m)|MapData
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MouseFilter

|Class
|--
|net.minecraft.util.MouseFilter

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_180179_a()|void
| func_76333_a(float arg0, float arg1)|float
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GuiMainMenu

|Class
|--
|net.minecraft.client.gui.GuiMainMenu

---

|Extends
|--
|GuiScreen

---

|Fields|Type
|--|--
|  field_146287_f|int
|  field_146288_g|long
|  field_146290_a|GuiButton
|  field_146291_p|boolean
|  field_146292_n|List\<GuiButton>
|  field_146294_l|int
|  field_146295_m|int
|  field_146297_k|Minecraft
|  field_146298_h|int
|  field_73735_i|float

---

|Methods|Return Type
|--|--
| func_146269_k()|void
| func_146270_b(int i)|void
| func_146274_d()|void
| func_146276_q_()|void
| func_146278_c(int i)|void
| func_146279_a(String arg0, int arg1, int arg2)|void
| func_146280_a(Minecraft arg0, int arg1, int arg2)|void
| func_146281_b()|void
| func_146282_l()|void
| func_146283_a(List\<String> arg0, int arg1, int arg2)|void
| func_175174_a(float arg0, float arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_175175_a(int arg0, int arg1, TextureAtlasSprite arg2, int arg3, int arg4)|void
| func_175273_b(Minecraft arg0, int arg1, int arg2)|void
| func_175275_f(String s)|void
| func_175276_a(TextComponent t)|boolean
| func_175281_b(String arg0, boolean arg1)|void
| func_183500_a(int arg0, int arg1)|void
| func_191927_a(ItemStack i)|List\<String>
| func_193975_a(boolean b)|void
| func_193976_p()|boolean
| func_73729_b(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73731_b(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73732_a(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73733_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73863_a(int arg0, int arg1, float arg2)|void
| func_73866_w_()|void
| func_73868_f()|boolean
| func_73876_c()|void
| func_73878_a(boolean arg0, int arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## KeyBinding

|Class
|--
|net.minecraft.client.settings.KeyBinding

---

|Extends
|--
|Comparable

---

|Fields|Type
|--|--
|  displayName|String
|  field_151472_e|int
|  field_74512_d|int
|  keyConflictContext|KeyConflictContext
|  keyModifier|KeyModifier
|  keyModifierDefault|KeyModifier
|  setToDefaultValue|boolean

---

|Methods|Return Type
|--|--
| compareTo(KeyBinding k)|int
| compareTo(Object o)|int
| conflicts(KeyBinding k)|boolean
| func_151462_b(int i)|void
| func_151463_i()|int
| func_151464_g()|String
| func_151466_e()|String
| func_151468_f()|boolean
| func_151469_h()|int
| func_151470_d()|boolean
| hasKeyCodeModifierConflict(KeyBinding k)|boolean
| isActiveAndMatches(int i)|boolean
| setKeyModifierAndCode(KeyModifier arg0, int arg1)|void
| setToDefault()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TutorialSteps

|Class
|--
|net.minecraft.client.tutorial.TutorialSteps

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_193308_a()|String
| func_193309_a(Tutorial t)|TutorialStep
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityPlayer$EnumChatVisibility

|Class
|--
|net.minecraft.entity.player.EntityPlayer$EnumChatVisibility

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_151428_a()|int
| func_151429_b()|String
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GameSettings$Options

|Class
|--
|net.minecraft.client.settings.GameSettings$Options

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_148262_d(float f)|float
| func_148263_a(float f)|void
| func_148266_c(float f)|float
| func_148267_f()|float
| func_148268_e(float f)|float
| func_186707_e()|float
| func_74378_d()|String
| func_74380_a()|boolean
| func_74381_c()|int
| func_74382_b()|boolean
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemColor

|Interface
|--
|net.minecraft.client.renderer.color.IItemColor

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_186726_a(ItemStack arg0, int arg1)|int

---

## SearchTree

|Class
|--
|net.minecraft.client.util.SearchTree

---

|Extends
|--
|SearchTree

---

|Methods|Return Type
|--|--
| func_194038_a(String s)|List\<T>
| func_194040_a()|void
| func_194043_a(Object o)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ResourcePackRepository$Entry

|Class
|--
|net.minecraft.client.resources.ResourcePackRepository$Entry

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_110514_c()|ResourcePack
| func_110515_d()|String
| func_110516_a()|void
| func_110517_b()|void
| func_110518_a(TextureManager t)|void
| func_110519_e()|String
| func_183027_f()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Language

|Class
|--
|net.minecraft.client.resources.Language

---

|Extends
|--
|Comparable

---

|Fields|Type
|--|--
|  javaLocale|Locale

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Language l)|int
| func_135034_a()|String
| func_135035_b()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ServerData$ServerResourceMode

|Class
|--
|net.minecraft.client.multiplayer.ServerData$ServerResourceMode

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_152589_a()|TextComponent
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NetHandlerPlayClient

|Interface
|--
|net.minecraft.network.play.INetHandlerPlayClient

---

|Extends
|--
|NetHandler

---

|Methods|Return Type
|--|--
| func_147231_a(TextComponent t)|void
| func_147234_a(SPacketBlockChange s)|void
| func_147235_a(SPacketSpawnObject s)|void
| func_147236_a(SPacketEntityStatus s)|void
| func_147237_a(SPacketSpawnPlayer s)|void
| func_147238_a(SPacketDestroyEntities s)|void
| func_147239_a(SPacketConfirmTransaction s)|void
| func_147240_a(SPacketCustomPayload s)|void
| func_147241_a(SPacketWindowItems s)|void
| func_147242_a(SPacketEntityEquipment s)|void
| func_147243_a(SPacketEntityAttach s)|void
| func_147244_a(SPacketEntityVelocity s)|void
| func_147245_a(SPacketWindowProperty s)|void
| func_147246_a(SPacketCollectItem s)|void
| func_147247_a(SPacketTeams s)|void
| func_147249_a(SPacketUpdateHealth s)|void
| func_147250_a(SPacketUpdateScore s)|void
| func_147251_a(SPacketChat s)|void
| func_147252_a(SPacketChangeGameState s)|void
| func_147253_a(SPacketDisconnect s)|void
| func_147254_a(SPacketDisplayObjective s)|void
| func_147256_a(SPacketPlayerListItem s)|void
| func_147257_a(SPacketHeldItemChange s)|void
| func_147259_a(SPacketEntity s)|void
| func_147260_a(SPacketEntityEffect s)|void
| func_147261_a(SPacketBlockAction s)|void
| func_147262_a(SPacketRemoveEntityEffect s)|void
| func_147263_a(SPacketChunkData s)|void
| func_147264_a(SPacketMaps s)|void
| func_147265_a(SPacketOpenWindow s)|void
| func_147266_a(SPacketSetSlot s)|void
| func_147267_a(SPacketEntityHeadLook s)|void
| func_147268_a(SPacketSignEditorOpen s)|void
| func_147270_a(SPacketPlayerAbilities s)|void
| func_147271_a(SPacketSpawnPosition s)|void
| func_147272_a(SPacketKeepAlive s)|void
| func_147273_a(SPacketUpdateTileEntity s)|void
| func_147274_a(SPacketTabComplete s)|void
| func_147275_a(SPacketEntityTeleport s)|void
| func_147276_a(SPacketCloseWindow s)|void
| func_147277_a(SPacketEffect s)|void
| func_147278_a(SPacketUseBed s)|void
| func_147279_a(SPacketAnimation s)|void
| func_147280_a(SPacketRespawn s)|void
| func_147281_a(SPacketSpawnMob s)|void
| func_147282_a(SPacketJoinGame s)|void
| func_147283_a(SPacketExplosion s)|void
| func_147284_a(SPacketEntityMetadata s)|void
| func_147285_a(SPacketTimeUpdate s)|void
| func_147286_a(SPacketSpawnExperienceOrb s)|void
| func_147287_a(SPacketMultiBlockChange s)|void
| func_147288_a(SPacketSpawnPainting s)|void
| func_147289_a(SPacketParticles s)|void
| func_147290_a(SPacketEntityProperties s)|void
| func_147291_a(SPacketScoreboardObjective s)|void
| func_147292_a(SPacketSpawnGlobalEntity s)|void
| func_147293_a(SPacketStatistics s)|void
| func_147294_a(SPacketBlockBreakAnim s)|void
| func_147295_a(SPacketSetExperience s)|void
| func_175093_a(SPacketWorldBorder s)|void
| func_175094_a(SPacketCamera s)|void
| func_175095_a(SPacketResourcePackSend s)|void
| func_175096_a(SPacketPlayerListHeaderFooter s)|void
| func_175098_a(SPacketCombatEvent s)|void
| func_175099_a(SPacketTitle s)|void
| func_175101_a(SPacketServerDifficulty s)|void
| func_184323_a(SPacketMoveVehicle s)|void
| func_184324_a(SPacketCooldown s)|void
| func_184325_a(SPacketUpdateBossInfo s)|void
| func_184326_a(SPacketUnloadChunk s)|void
| func_184327_a(SPacketSoundEffect s)|void
| func_184328_a(SPacketSetPassengers s)|void
| func_184329_a(SPacketCustomSound s)|void
| func_184330_a(SPacketPlayerPosLook s)|void
| func_191980_a(SPacketRecipeBook s)|void
| func_191981_a(SPacketAdvancementInfo s)|void
| func_194022_a(SPacketSelectAdvancementsTab s)|void
| func_194307_a(SPacketPlaceGhostRecipe s)|void

---

## SPacketBlockChange

|Class
|--
|net.minecraft.network.play.server.SPacketBlockChange

---

|Extends
|--
|Packet

---

|Fields|Type
|--|--
|  field_148883_d|BlockState

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_179827_b()|BlockPos
| func_180728_a()|BlockState
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketSpawnObject

|Class
|--
|net.minecraft.network.play.server.SPacketSpawnObject

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_148993_l()|int
| func_148999_i()|int
| func_149000_e(int i)|void
| func_149001_c()|int
| func_149002_g(int i)|void
| func_149003_d(int i)|void
| func_149004_h()|int
| func_149006_k()|int
| func_149007_f(int i)|void
| func_149008_j()|int
| func_149009_m()|int
| func_149010_g()|int
| func_186879_b()|UUID
| func_186880_c()|double
| func_186881_e()|double
| func_186882_d()|double
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketEntityStatus

|Class
|--
|net.minecraft.network.play.server.SPacketEntityStatus

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149160_c()|byte
| func_149161_a(World w)|Entity
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketSpawnPlayer

|Class
|--
|net.minecraft.network.play.server.SPacketSpawnPlayer

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_148941_i()|byte
| func_148943_d()|int
| func_148944_c()|List\<net.minecraft.network.datasync.EntityDataManager$DataEntry\<?>>
| func_148945_j()|byte
| func_179819_c()|UUID
| func_186897_e()|double
| func_186898_d()|double
| func_186899_f()|double
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketDestroyEntities

|Class
|--
|net.minecraft.network.play.server.SPacketDestroyEntities

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149098_c()|int[]
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketConfirmTransaction

|Class
|--
|net.minecraft.network.play.server.SPacketConfirmTransaction

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_148888_e()|boolean
| func_148889_c()|int
| func_148890_d()|short
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketCustomPayload

|Class
|--
|net.minecraft.network.play.server.SPacketCustomPayload

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149169_c()|String
| func_180735_b()|PacketBuffer
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketWindowItems

|Class
|--
|net.minecraft.network.play.server.SPacketWindowItems

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_148910_d()|List\<ItemStack>
| func_148911_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketEntityEquipment

|Class
|--
|net.minecraft.network.play.server.SPacketEntityEquipment

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149389_d()|int
| func_149390_c()|ItemStack
| func_186969_c()|EntityEquipmentSlot
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketEntityAttach

|Class
|--
|net.minecraft.network.play.server.SPacketEntityAttach

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149402_e()|int
| func_149403_d()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketEntityVelocity

|Class
|--
|net.minecraft.network.play.server.SPacketEntityVelocity

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149409_f()|int
| func_149410_e()|int
| func_149411_d()|int
| func_149412_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketWindowProperty

|Class
|--
|net.minecraft.network.play.server.SPacketWindowProperty

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149180_e()|int
| func_149181_d()|int
| func_149182_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketCollectItem

|Class
|--
|net.minecraft.network.play.server.SPacketCollectItem

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149353_d()|int
| func_149354_c()|int
| func_191208_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketTeams

|Class
|--
|net.minecraft.network.play.server.SPacketTeams

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149306_d()|String
| func_149307_h()|int
| func_149308_i()|int
| func_149309_f()|String
| func_149310_g()|Collection\<String>
| func_149311_e()|String
| func_149312_c()|String
| func_179813_h()|int
| func_179814_i()|String
| func_186975_j()|String
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketUpdateHealth

|Class
|--
|net.minecraft.network.play.server.SPacketUpdateHealth

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149330_d()|int
| func_149331_e()|float
| func_149332_c()|float
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketUpdateScore

|Class
|--
|net.minecraft.network.play.server.SPacketUpdateScore

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149321_d()|String
| func_149323_e()|int
| func_149324_c()|String
| func_180751_d()|SPacketUpdateScore$Action
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketChat

|Class
|--
|net.minecraft.network.play.server.SPacketChat

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_148915_c()|TextComponent
| func_148916_d()|boolean
| func_192590_c()|ChatType
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketChangeGameState

|Class
|--
|net.minecraft.network.play.server.SPacketChangeGameState

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149137_d()|float
| func_149138_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketDisconnect

|Class
|--
|net.minecraft.network.play.server.SPacketDisconnect

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149165_c()|TextComponent
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketDisplayObjective

|Class
|--
|net.minecraft.network.play.server.SPacketDisplayObjective

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149370_d()|String
| func_149371_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketPlayerListItem

|Class
|--
|net.minecraft.network.play.server.SPacketPlayerListItem

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_179767_a()|List\<SPacketPlayerListItem$AddPlayerData>
| func_179768_b()|SPacketPlayerListItem$Action
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketHeldItemChange

|Class
|--
|net.minecraft.network.play.server.SPacketHeldItemChange

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149385_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketEntity

|Class
|--
|net.minecraft.network.play.server.SPacketEntity

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149060_h()|boolean
| func_149063_g()|byte
| func_149065_a(World w)|Entity
| func_149066_f()|byte
| func_179742_g()|boolean
| func_186951_c()|int
| func_186952_a()|int
| func_186953_b()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketEntityEffect

|Class
|--
|net.minecraft.network.play.server.SPacketEntityEffect

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149426_d()|int
| func_149427_e()|byte
| func_149428_f()|byte
| func_149429_c()|boolean
| func_179707_f()|boolean
| func_180755_e()|int
| func_186984_g()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketBlockAction

|Class
|--
|net.minecraft.network.play.server.SPacketBlockAction

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_148864_h()|int
| func_148868_c()|Block
| func_148869_g()|int
| func_179825_a()|BlockPos
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketRemoveEntityEffect

|Class
|--
|net.minecraft.network.play.server.SPacketRemoveEntityEffect

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_186967_a(World w)|Entity
| func_186968_a()|Potion
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketChunkData

|Class
|--
|net.minecraft.network.play.server.SPacketChunkData

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149271_f()|int
| func_149273_e()|int
| func_149274_i()|boolean
| func_149276_g()|int
| func_186946_a()|PacketBuffer
| func_189554_f()|List\<NBTTagCompound>
| func_189555_a(PacketBuffer arg0, Chunk arg1, boolean arg2, int arg3)|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketMaps

|Class
|--
|net.minecraft.network.play.server.SPacketMaps

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149188_c()|int
| func_179734_a(MapData m)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketOpenWindow

|Class
|--
|net.minecraft.network.play.server.SPacketOpenWindow

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_148897_h()|int
| func_148898_f()|int
| func_148900_g()|boolean
| func_148901_c()|int
| func_148902_e()|String
| func_179840_c()|TextComponent
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketSetSlot

|Class
|--
|net.minecraft.network.play.server.SPacketSetSlot

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149173_d()|int
| func_149174_e()|ItemStack
| func_149175_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketEntityHeadLook

|Class
|--
|net.minecraft.network.play.server.SPacketEntityHeadLook

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149380_c()|byte
| func_149381_a(World w)|Entity
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketSignEditorOpen

|Class
|--
|net.minecraft.network.play.server.SPacketSignEditorOpen

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_179777_a()|BlockPos
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketPlayerAbilities

|Class
|--
|net.minecraft.network.play.server.SPacketPlayerAbilities

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149101_g()|float
| func_149102_b(boolean b)|void
| func_149103_f()|boolean
| func_149104_a(float f)|void
| func_149105_e()|boolean
| func_149106_d()|boolean
| func_149107_h()|float
| func_149108_a(boolean b)|void
| func_149109_c(boolean b)|void
| func_149110_b(float f)|void
| func_149111_d(boolean b)|void
| func_149112_c()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketSpawnPosition

|Class
|--
|net.minecraft.network.play.server.SPacketSpawnPosition

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_179800_a()|BlockPos
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketKeepAlive

|Class
|--
|net.minecraft.network.play.server.SPacketKeepAlive

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149134_c()|long
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketTabComplete

|Class
|--
|net.minecraft.network.play.server.SPacketTabComplete

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149630_c()|String[]
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketEntityTeleport

|Class
|--
|net.minecraft.network.play.server.SPacketEntityTeleport

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149447_h()|byte
| func_149450_g()|byte
| func_149451_c()|int
| func_179697_g()|boolean
| func_186981_d()|double
| func_186982_b()|double
| func_186983_c()|double
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketCloseWindow

|Class
|--
|net.minecraft.network.play.server.SPacketCloseWindow

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketEffect

|Class
|--
|net.minecraft.network.play.server.SPacketEffect

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149241_e()|int
| func_149242_d()|int
| func_149244_c()|boolean
| func_179746_d()|BlockPos
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketUseBed

|Class
|--
|net.minecraft.network.play.server.SPacketUseBed

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149091_a(World w)|EntityPlayer
| func_179798_a()|BlockPos
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketAnimation

|Class
|--
|net.minecraft.network.play.server.SPacketAnimation

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_148977_d()|int
| func_148978_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketRespawn

|Class
|--
|net.minecraft.network.play.server.SPacketRespawn

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149080_f()|WorldType
| func_149081_d()|EnumDifficulty
| func_149082_c()|int
| func_149083_e()|GameType
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketSpawnMob

|Class
|--
|net.minecraft.network.play.server.SPacketSpawnMob

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149024_d()|int
| func_149025_e()|int
| func_149026_i()|int
| func_149027_c()|List\<net.minecraft.network.datasync.EntityDataManager$DataEntry\<?>>
| func_149028_l()|byte
| func_149030_m()|byte
| func_149031_k()|int
| func_149032_n()|byte
| func_149033_j()|int
| func_186890_c()|UUID
| func_186891_e()|double
| func_186892_f()|double
| func_186893_g()|double
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketJoinGame

|Class
|--
|net.minecraft.network.play.server.SPacketJoinGame

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149192_g()|EnumDifficulty
| func_149193_h()|int
| func_149194_f()|int
| func_149195_d()|boolean
| func_149196_i()|WorldType
| func_149197_c()|int
| func_149198_e()|GameType
| func_179744_h()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketExplosion

|Class
|--
|net.minecraft.network.play.server.SPacketExplosion

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149143_g()|double
| func_149144_d()|float
| func_149145_h()|double
| func_149146_i()|float
| func_149147_e()|float
| func_149148_f()|double
| func_149149_c()|float
| func_149150_j()|List\<BlockPos>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketEntityMetadata

|Class
|--
|net.minecraft.network.play.server.SPacketEntityMetadata

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149375_d()|int
| func_149376_c()|List\<net.minecraft.network.datasync.EntityDataManager$DataEntry\<?>>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketTimeUpdate

|Class
|--
|net.minecraft.network.play.server.SPacketTimeUpdate

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149365_d()|long
| func_149366_c()|long
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketSpawnExperienceOrb

|Class
|--
|net.minecraft.network.play.server.SPacketSpawnExperienceOrb

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_148985_c()|int
| func_148986_g()|int
| func_186884_d()|double
| func_186885_b()|double
| func_186886_c()|double
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketMultiBlockChange

|Class
|--
|net.minecraft.network.play.server.SPacketMultiBlockChange

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_179844_a()|SPacketMultiBlockChange$BlockUpdateData[]
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketSpawnPainting

|Class
|--
|net.minecraft.network.play.server.SPacketSpawnPainting

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_148961_h()|String
| func_148965_c()|int
| func_179836_c()|EnumFacing
| func_179837_b()|BlockPos
| func_186895_b()|UUID
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketParticles

|Class
|--
|net.minecraft.network.play.server.SPacketParticles

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149220_d()|double
| func_149221_g()|float
| func_149222_k()|int
| func_149223_i()|float
| func_149224_h()|float
| func_149225_f()|double
| func_149226_e()|double
| func_149227_j()|float
| func_179748_k()|int[]
| func_179749_a()|EnumParticleTypes
| func_179750_b()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketEntityProperties

|Class
|--
|net.minecraft.network.play.server.SPacketEntityProperties

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149441_d()|List\<SPacketEntityProperties$Snapshot>
| func_149442_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketScoreboardObjective

|Class
|--
|net.minecraft.network.play.server.SPacketScoreboardObjective

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149337_d()|String
| func_149338_e()|int
| func_149339_c()|String
| func_179817_d()|IScoreCriteria$EnumRenderType
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketSpawnGlobalEntity

|Class
|--
|net.minecraft.network.play.server.SPacketSpawnGlobalEntity

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149052_c()|int
| func_149053_g()|int
| func_186887_d()|double
| func_186888_b()|double
| func_186889_c()|double
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketStatistics

|Class
|--
|net.minecraft.network.play.server.SPacketStatistics

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_148974_c()|Map\<StatBase, int>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketBlockBreakAnim

|Class
|--
|net.minecraft.network.play.server.SPacketBlockBreakAnim

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_148845_c()|int
| func_148846_g()|int
| func_179821_b()|BlockPos
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketSetExperience

|Class
|--
|net.minecraft.network.play.server.SPacketSetExperience

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149395_e()|int
| func_149396_d()|int
| func_149397_c()|float
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketWorldBorder

|Class
|--
|net.minecraft.network.play.server.SPacketWorldBorder

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_179788_a(WorldBorder w)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketCamera

|Class
|--
|net.minecraft.network.play.server.SPacketCamera

---

|Extends
|--
|Packet

---

|Fields|Type
|--|--
|  field_179781_a|int

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_179780_a(World w)|Entity
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketResourcePackSend

|Class
|--
|net.minecraft.network.play.server.SPacketResourcePackSend

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_179783_a()|String
| func_179784_b()|String
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketPlayerListHeaderFooter

|Class
|--
|net.minecraft.network.play.server.SPacketPlayerListHeaderFooter

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_179700_a()|TextComponent
| func_179701_b()|TextComponent
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketCombatEvent

|Class
|--
|net.minecraft.network.play.server.SPacketCombatEvent

---

|Extends
|--
|Packet

---

|Fields|Type
|--|--
|  field_179772_d|int
|  field_179773_e|TextComponent
|  field_179774_b|int
|  field_179775_c|int
|  field_179776_a|SPacketCombatEvent$Event

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketTitle

|Class
|--
|net.minecraft.network.play.server.SPacketTitle

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_179803_e()|int
| func_179804_d()|int
| func_179805_b()|TextComponent
| func_179806_c()|int
| func_179807_a()|SPacketTitle$Type
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketServerDifficulty

|Class
|--
|net.minecraft.network.play.server.SPacketServerDifficulty

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_179830_a()|boolean
| func_179831_b()|EnumDifficulty
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketMoveVehicle

|Class
|--
|net.minecraft.network.play.server.SPacketMoveVehicle

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_186955_b()|double
| func_186956_c()|double
| func_186957_a()|double
| func_186958_e()|float
| func_186959_d()|float
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketCooldown

|Class
|--
|net.minecraft.network.play.server.SPacketCooldown

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_186920_a()|Item
| func_186922_b()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketUpdateBossInfo

|Class
|--
|net.minecraft.network.play.server.SPacketUpdateBossInfo

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_186900_e()|BossInfo$Color
| func_186901_i()|boolean
| func_186902_b()|SPacketUpdateBossInfo$Operation
| func_186904_f()|BossInfo$Overlay
| func_186906_d()|float
| func_186907_c()|TextComponent
| func_186908_a()|UUID
| func_186909_g()|boolean
| func_186910_h()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketUnloadChunk

|Class
|--
|net.minecraft.network.play.server.SPacketUnloadChunk

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_186940_a()|int
| func_186941_b()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketSoundEffect

|Class
|--
|net.minecraft.network.play.server.SPacketSoundEffect

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149207_d()|double
| func_149208_g()|float
| func_149209_h()|float
| func_149210_f()|double
| func_149211_e()|double
| func_186977_b()|SoundCategory
| func_186978_a()|SoundEvent
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketSetPassengers

|Class
|--
|net.minecraft.network.play.server.SPacketSetPassengers

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_186971_a()|int[]
| func_186972_b()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketCustomSound

|Class
|--
|net.minecraft.network.play.server.SPacketCustomSound

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_186925_e()|double
| func_186926_d()|double
| func_186927_f()|float
| func_186928_g()|float
| func_186929_b()|SoundCategory
| func_186930_a()|String
| func_186932_c()|double
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketPlayerPosLook

|Class
|--
|net.minecraft.network.play.server.SPacketPlayerPosLook

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_148928_d()|double
| func_148930_g()|float
| func_148931_f()|float
| func_148932_c()|double
| func_148933_e()|double
| func_179834_f()|Set\<SPacketPlayerPosLook$EnumFlags>
| func_186965_f()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketRecipeBook

|Class
|--
|net.minecraft.network.play.server.SPacketRecipeBook

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_192593_c()|boolean
| func_192594_d()|boolean
| func_192595_a()|List\<Recipe>
| func_193644_b()|List\<Recipe>
| func_194151_e()|SPacketRecipeBook$State
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketAdvancementInfo

|Class
|--
|net.minecraft.network.play.server.SPacketAdvancementInfo

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_192600_b()|Set\<ResourceLocation>
| func_192602_d()|boolean
| func_192603_a()|Map\<ResourceLocation, Advancement$Builder>
| func_192604_c()|Map\<ResourceLocation, AdvancementProgress>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ClientAdvancementManager

|Class
|--
|net.minecraft.client.multiplayer.ClientAdvancementManager

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_192803_d|Map\<Advancement, AdvancementProgress>

---

|Methods|Return Type
|--|--
| func_192798_a(ClientAdvancementManager$IListener c)|void
| func_192799_a(SPacketAdvancementInfo s)|void
| func_194229_a()|AdvancementList
| func_194230_a(Advancement arg0, boolean arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketSelectAdvancementsTab

|Class
|--
|net.minecraft.network.play.server.SPacketSelectAdvancementsTab

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayClient n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_194154_a()|ResourceLocation
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketPlaceGhostRecipe

|Class
|--
|net.minecraft.network.play.server.SPacketPlaceGhostRecipe

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayClient n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_194311_a()|Recipe
| func_194313_b()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AbstractTexture

|Class
|--
|net.minecraft.client.renderer.texture.AbstractTexture

---

|Extends
|--
|TextureObject

---

|Fields|Type
|--|--
|  multiTex|MultiTexID
|  multiTexID|MultiTexID

---

|Methods|Return Type
|--|--
| func_110551_a(ResourceManager r)|void
| func_110552_b()|int
| func_147631_c()|void
| func_174935_a()|void
| func_174936_b(boolean arg0, boolean arg1)|void
| func_174937_a(boolean arg0, boolean arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MultiTexID

|Class
|--
|net.optifine.shaders.MultiTexID

---

|Extends
|--

---

|Fields|Type
|--|--
|  base|int
|  norm|int
|  spec|int

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TextureMapPopulator

|Interface
|--
|net.minecraft.client.renderer.texture.ITextureMapPopulator

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_177059_a(TextureMap t)|void

---

## Tickable

|Interface
|--
|net.minecraft.util.ITickable

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_73660_a()|void

---

## SoundManager

|Class
|--
|net.minecraft.client.audio.SoundManager

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_148618_g|int
|  field_148620_e|SoundManager$SoundSystemStarterThread
|  field_148622_c|SoundHandler
|  field_148624_n|Map\<String, int>
|  field_148625_l|List\<TickableSound>
|  field_148629_h|Map\<String, Sound>
|  field_188776_k|Multimap\<SoundCategory, String>

---

|Methods|Return Type
|--|--
| func_148596_a()|void
| func_148597_a(Sound s)|boolean
| func_148599_a(Sound arg0, int arg1)|void
| func_148602_b(Sound s)|void
| func_148604_f()|void
| func_148605_d()|void
| func_148610_e()|void
| func_148611_c(Sound s)|void
| func_148613_b()|void
| func_148614_c()|void
| func_148615_a(EntityPlayer arg0, float arg1)|void
| func_188770_e(Sound s)|float
| func_188771_a(SoundCategory arg0, float arg1)|void
| func_188772_d(Sound s)|float
| func_188773_b(SoundEventListener s)|void
| func_188774_a(SoundEventListener s)|void
| func_189567_a(String arg0, SoundCategory arg1)|void
| setListener(Entity arg0, float arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SoundEventAccessor

|Class
|--
|net.minecraft.client.audio.SoundEventAccessor

---

|Extends
|--
|SoundEventAccessor

---

|Methods|Return Type
|--|--
| func_148720_g()|Object
| func_148720_g()|Sound
| func_148721_a()|int
| func_188712_c()|TextComponent
| func_188714_b()|ResourceLocation
| func_188715_a(SoundEventAccessor\<Sound> s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SoundEventListener

|Interface
|--
|net.minecraft.client.audio.ISoundEventListener

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_184067_a(Sound arg0, SoundEventAccessor arg1)|void

---

## MinecraftProfileTexture$Type

|Class
|--
|com.mojang.authlib.minecraft.MinecraftProfileTexture$Type

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MinecraftProfileTexture

|Class
|--
|com.mojang.authlib.minecraft.MinecraftProfileTexture

---

|Extends
|--

---

|Fields|Type
|--|--
|  hash|String
|  url|String

---

|Methods|Return Type
|--|--
| getMetadata(String s)|String
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SkinManager$SkinAvailableCallback

|Interface
|--
|net.minecraft.client.resources.SkinManager$SkinAvailableCallback

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_180521_a(MinecraftProfileTexture$Type arg0, ResourceLocation arg1, MinecraftProfileTexture arg2)|void

---

## ItemCameraTransforms$TransformType

|Class
|--
|net.minecraft.client.renderer.block.model.ItemCameraTransforms$TransformType

---

|Extends
|--
|Enum
|ModelPart

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Render

|Class
|--
|net.minecraft.client.renderer.entity.Render

---

|Extends
|--
|EntityRenderer

---

|Fields|Type
|--|--
|  entityClass|Class
|  field_76989_e|float
|  locationTextureCustom|ResourceLocation

---

|Methods|Return Type
|--|--
| func_110776_a(ResourceLocation r)|void
| func_177068_d()|RenderManager
| func_177071_a(Entity arg0, Camera arg1, double arg2, double arg3, double arg4)|boolean
| func_188295_H_()|boolean
| func_188297_a(boolean b)|void
| func_188300_b(Entity arg0, double arg1, double arg2, double arg3, float arg4, float arg5)|void
| func_76979_b(Entity arg0, double arg1, double arg2, double arg3, float arg4, float arg5)|void
| func_76983_a()|FontRenderer
| func_76986_a(Entity arg0, double arg1, double arg2, double arg3, float arg4, float arg5)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RenderPlayer

|Class
|--
|net.minecraft.client.renderer.entity.RenderPlayer

---

|Extends
|--
|RenderLivingBase

---

|Fields|Type
|--|--
|  entityClass|Class
|  field_177097_h|List\<net.minecraft.client.renderer.entity.layers.LayerRenderer\<T>>
|  field_76989_e|float
|  field_77045_g|ModelBase
|  layerRenderers|List\<net.minecraft.client.renderer.entity.layers.LayerRenderer\<T>>
|  locationTextureCustom|ResourceLocation
|  renderAgeInTicks|float
|  renderEntity|EntityLivingBase
|  renderHeadPitch|float
|  renderHeadYaw|float
|  renderLimbSwing|float
|  renderLimbSwingAmount|float
|  renderPartialTicks|float
|  renderScaleFactor|float

---

|Methods|Return Type
|--|--
| func_110775_a(AbstractClientPlayer a)|ResourceLocation
| func_110775_a(Entity e)|ResourceLocation
| func_110776_a(ResourceLocation r)|void
| func_177067_a(EntityLivingBase arg0, double arg1, double arg2, double arg3)|void
| func_177067_a(Entity arg0, double arg1, double arg2, double arg3)|void
| func_177068_d()|RenderManager
| func_177071_a(Entity arg0, Camera arg1, double arg2, double arg3, double arg4)|boolean
| func_177087_b()|ModelPlayer
| func_177087_b()|ModelBase
| func_177094_a(LayerRenderer l)|boolean
| func_177137_d(AbstractClientPlayer a)|void
| func_177138_b(AbstractClientPlayer a)|void
| func_177139_c(AbstractClientPlayer a)|void
| func_188295_H_()|boolean
| func_188297_a(boolean b)|void
| func_188300_b(Entity arg0, double arg1, double arg2, double arg3, float arg4, float arg5)|void
| func_188322_c(EntityLivingBase arg0, float arg1)|float
| func_76979_b(Entity arg0, double arg1, double arg2, double arg3, float arg4, float arg5)|void
| func_76983_a()|FontRenderer
| func_76986_a(AbstractClientPlayer arg0, double arg1, double arg2, double arg3, float arg4, float arg5)|void
| func_76986_a(Entity arg0, double arg1, double arg2, double arg3, float arg4, float arg5)|void
| func_76986_a(EntityLivingBase arg0, double arg1, double arg2, double arg3, float arg4, float arg5)|void
| func_82422_c()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemModelMesher

|Class
|--
|net.minecraft.client.renderer.ItemModelMesher

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178080_a(Item arg0, ItemMeshDefinition arg1)|void
| func_178082_a(Item i)|TextureAtlasSprite
| func_178083_a()|ModelManager
| func_178085_b()|void
| func_178086_a(Item arg0, int arg1, ModelResourceLocation arg2)|void
| func_178087_a(Item arg0, int arg1)|TextureAtlasSprite
| func_178089_a(ItemStack i)|BakedModel
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ModelManager

|Class
|--
|net.minecraft.client.renderer.block.model.ModelManager

---

|Extends
|--
|ResourceManagerReloadListener

---

|Methods|Return Type
|--|--
| func_110549_a(ResourceManager r)|void
| func_174951_a()|BakedModel
| func_174952_b()|TextureMap
| func_174953_a(ModelResourceLocation m)|BakedModel
| func_174954_c()|BlockModelShapes
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BakedQuad

|Class
|--
|net.minecraft.client.renderer.block.model.BakedQuad

---

|Extends
|--
|VertexProducer

---

|Fields|Type
|--|--
|  faceQuad|boolean
|  format|VertexFormat
|  fullFaceQuad|boolean
|  fullQuad|boolean
|  midX|float
|  midY|double
|  midZ|double
|  quadBounds|QuadBounds
|  quadEmissive|BakedQuad
|  vertexDataSingle|int[]

---

|Methods|Return Type
|--|--
| func_178209_a()|int[]
| func_178210_d()|EnumFacing
| func_178211_c()|int
| func_178212_b()|boolean
| func_187508_a()|TextureAtlasSprite
| pipe(VertexConsumer v)|void
| shouldApplyDiffuseLighting()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockColor

|Interface
|--
|net.minecraft.client.renderer.color.IBlockColor

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_186720_a(BlockState arg0, BlockAccess arg1, BlockPos arg2, int arg3)|int

---

## DataFixer

|Interface
|--
|net.minecraft.util.datafix.IDataFixer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_188251_a(FixType arg0, NBTTagCompound arg1, int arg2)|NBTTagCompound

---

## FixType

|Interface
|--
|net.minecraft.util.datafix.IFixType

---

|Extends
|--

---

## DataWalker

|Interface
|--
|net.minecraft.util.datafix.IDataWalker

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_188266_a(DataFixer arg0, NBTTagCompound arg1, int arg2)|NBTTagCompound

---

## FixableData

|Interface
|--
|net.minecraft.util.datafix.IFixableData

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_188216_a()|int
| func_188217_a(NBTTagCompound n)|NBTTagCompound

---

## FixTypes

|Class
|--
|net.minecraft.util.datafix.FixTypes

---

|Extends
|--
|Enum
|FixType

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Toast

|Interface
|--
|net.minecraft.client.gui.toasts.IToast

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_193652_b()|Object
| func_193653_a(GuiToast arg0, long arg1)|IToast$Visibility

---

## WorldSummary

|Class
|--
|net.minecraft.world.storage.WorldSummary

---

|Extends
|--
|Comparable

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(WorldSummary w)|int
| func_154336_c()|long
| func_186355_l()|boolean
| func_186356_m()|boolean
| func_186357_i()|String
| func_75783_h()|boolean
| func_75784_e()|long
| func_75785_d()|boolean
| func_75786_a()|String
| func_75788_b()|String
| func_75789_g()|boolean
| func_75790_f()|GameType
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CommandManager

|Interface
|--
|net.minecraft.command.ICommandManager

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_180524_a(CommandSender arg0, String arg1, BlockPos arg2)|List\<String>
| func_71555_a()|Map\<String, Command>
| func_71556_a(CommandSender arg0, String arg1)|int
| func_71557_a(CommandSender c)|List\<Command>

---

## ServerStatusResponse

|Class
|--
|net.minecraft.network.ServerStatusResponse

---

|Extends
|--

---

|Fields|Type
|--|--
|  json|String

---

|Methods|Return Type
|--|--
| func_151315_a(TextComponent t)|void
| func_151316_d()|String
| func_151317_a()|TextComponent
| func_151318_b()|ServerStatusResponse$Players
| func_151319_a(ServerStatusResponse$Players s)|void
| func_151320_a(String s)|void
| func_151321_a(ServerStatusResponse$Version s)|void
| func_151322_c()|ServerStatusResponse$Version
| invalidateJson()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NetworkSystem

|Class
|--
|net.minecraft.network.NetworkSystem

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_151277_a|boolean

---

|Methods|Return Type
|--|--
| func_151265_a(InetAddress arg0, int arg1)|void
| func_151267_d()|MinecraftServer
| func_151268_b()|void
| func_151269_c()|void
| func_151270_a()|SocketAddress
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PlayerProfileCache

|Class
|--
|net.minecraft.server.management.PlayerProfileCache

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_152661_c|Map\<String, PlayerProfileCache$ProfileEntry>

---

|Methods|Return Type
|--|--
| func_152649_a(GameProfile g)|void
| func_152652_a(UUID u)|GameProfile
| func_152654_a()|String[]
| func_152655_a(String s)|GameProfile
| func_152657_b()|void
| func_152658_c()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GameProfileRepository

|Interface
|--
|com.mojang.authlib.GameProfileRepository

---

|Extends
|--

---

|Methods|Return Type
|--|--
| findProfilesByNames(String[] arg0, Agent arg1, ProfileLookupCallback arg2)|void

---

## ServerCommandManager

|Class
|--
|net.minecraft.command.ServerCommandManager

---

|Extends
|--
|CommandHandler
|CommandListener

---

|Fields|Type
|--|--
|  field_71561_b|Set\<Command>

---

|Methods|Return Type
|--|--
| func_152372_a(CommandSender arg0, Command arg1, int arg2, String arg3, Object[] arg4)|void
| func_180524_a(CommandSender arg0, String arg1, BlockPos arg2)|List\<String>
| func_71555_a()|Map\<String, Command>
| func_71556_a(CommandSender arg0, String arg1)|int
| func_71557_a(CommandSender c)|List\<Command>
| func_71560_a(Command c)|Command
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PlayerList

|Class
|--
|net.minecraft.server.management.PlayerList

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_72407_n|boolean

---

|Methods|Return Type
|--|--
| func_148537_a(Packet\<?> arg0, int arg1)|void
| func_148539_a(TextComponent t)|void
| func_148540_a(Packet\<?> p)|void
| func_148542_a(SocketAddress arg0, GameProfile arg1)|String
| func_148543_a(EntityPlayer arg0, double arg1, double arg2, double arg3, double arg4, int arg5, Packet\<?> arg6)|void
| func_148544_a(TextComponent arg0, boolean arg1)|void
| func_148545_a(GameProfile g)|EntityPlayerMP
| func_152596_g(GameProfile g)|boolean
| func_152597_c(GameProfile g)|void
| func_152598_l()|String[]
| func_152599_k()|UserListWhitelist
| func_152600_g()|GameProfile[]
| func_152601_d(GameProfile g)|void
| func_152602_a(EntityPlayer e)|StatisticsManagerServer
| func_152603_m()|UserListOps
| func_152604_a(GameType g)|void
| func_152605_a(GameProfile g)|void
| func_152606_n()|String[]
| func_152607_e(GameProfile g)|boolean
| func_152608_h()|UserListBans
| func_152610_b(GameProfile g)|void
| func_152611_a(int i)|void
| func_152612_a(String s)|EntityPlayerMP
| func_177451_a(UUID u)|EntityPlayerMP
| func_177452_b(EntityPlayer arg0, TextComponent arg1)|void
| func_177453_a(EntityPlayer arg0, TextComponent arg1)|void
| func_181057_v()|List\<EntityPlayerMP>
| func_181058_b(boolean b)|String
| func_183023_f(GameProfile g)|boolean
| func_187242_a(EntityPlayerMP arg0, int arg1)|void
| func_187243_f(EntityPlayerMP e)|void
| func_187244_a()|void
| func_192054_h(EntityPlayerMP e)|PlayerAdvancements
| func_193244_w()|void
| func_72352_l()|int
| func_72354_b(EntityPlayerMP arg0, WorldServer arg1)|void
| func_72358_d(EntityPlayerMP e)|void
| func_72363_f()|UserListIPBans
| func_72364_a(WorldServer[] w)|void
| func_72365_p()|MinecraftServer
| func_72367_e(EntityPlayerMP e)|void
| func_72368_a(EntityPlayerMP arg0, int arg1, boolean arg2)|EntityPlayerMP
| func_72369_d()|String[]
| func_72371_a(boolean b)|void
| func_72372_a()|int
| func_72373_m()|String[]
| func_72374_b()|void
| func_72375_a(EntityPlayerMP arg0, WorldServer arg1)|void
| func_72377_c(EntityPlayerMP e)|void
| func_72378_q()|NBTTagCompound
| func_72380_a(EntityPlayerMP e)|NBTTagCompound
| func_72382_j(String s)|List\<EntityPlayerMP>
| func_72385_f(EntityPlayerMP e)|void
| func_72387_b(boolean b)|void
| func_72389_g()|void
| func_72392_r()|void
| func_72394_k()|int
| func_72395_o()|int
| func_82448_a(Entity arg0, int arg1, WorldServer arg2, WorldServer arg3)|void
| getPlayerNBT(EntityPlayerMP e)|NBTTagCompound
| initializeConnectionToPlayer(NetworkManager arg0, EntityPlayerMP arg1, NetHandlerPlayServer arg2)|void
| transferEntityToWorld(Entity arg0, int arg1, WorldServer arg2, WorldServer arg3, Teleporter arg4)|void
| transferEntityToWorld(Entity arg0, int arg1, WorldServer arg2, WorldServer arg3, Teleporter arg4)|void
| transferPlayerToDimension(EntityPlayerMP arg0, int arg1, Teleporter arg2)|void
| transferPlayerToDimension(EntityPlayerMP arg0, int arg1, Teleporter arg2)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MutableColor4I

|Class
|--
|com.feed_the_beast.ftblib.lib.icon.MutableColor4I

---

|Extends
|--
|Color4I

---

|Fields|Type
|--|--
|  empty|boolean
|  ingredient|Object
|  json|JsonElement
|  mutable|boolean

---

|Methods|Return Type
|--|--
| addBrightness(int i)|Color4I
| addBrightness(float f)|Color4I
| alphaf()|float
| alphai()|int
| bindTexture()|void
| bluef()|float
| bluei()|int
| combineWith(Icon[] i)|Icon
| combineWith(Icon i)|Icon
| copy()|MutableColor4I
| copy()|Color4I
| copy()|Icon
| createPixelBuffer()|PixelBuffer
| draw(int arg0, int arg1, int arg2, int arg3, Color4I arg4)|void
| draw(int arg0, int arg1, int arg2, int arg3)|void
| draw3D(Color4I c)|void
| drawStatic(int arg0, int arg1, int arg2, int arg3)|void
| greenf()|float
| greeni()|int
| hasPixelBuffer()|boolean
| lerp(Color4I arg0, float arg1)|Color4I
| mutable()|MutableColor4I
| redf()|float
| redi()|int
| rgb()|int
| rgba()|int
| set(Color4I c)|Color4I
| set(int arg0, int arg1)|Color4I
| set(int i)|Color4I
| set(int arg0, int arg1, int arg2, int arg3)|Color4I
| set(Color4I arg0, int arg1)|Color4I
| setAlpha(int i)|Color4I
| setFromHSB(float arg0, float arg1, float arg2)|Color4I
| wait(long arg0, int arg1)|void
| wait(long l)|void
| whiteIfEmpty()|Color4I
| withAlpha(int i)|Color4I
| withAlphaf(float f)|Color4I
| withBorder(int i)|Icon
| withOutline(Color4I arg0, boolean arg1)|Icon
| withTint(Color4I c)|Color4I
| withTint(Color4I c)|Icon

---

## AbstractInt2ByteMap

|Class
|--
|it.unimi.dsi.fastutil.ints.AbstractInt2ByteMap

---

|Extends
|--
|AbstractInt2ByteFunction
|Int2ByteMap
|Serializable

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| clear()|void
| compute(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| computeIfAbsent(Object arg0, Function\<? super K, ? extends V> arg1)|Object
| computeIfPresent(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| containsKey(int i)|boolean
| containsKey(Object o)|boolean
| containsValue(byte b)|boolean
| containsValue(Object o)|boolean
| defaultReturnValue(byte b)|void
| defaultReturnValue()|byte
| entrySet()|ObjectSet\<java.util.Map$Entry\<java.lang.Integer, java.lang.Byte>>
| entrySet()|Set
| forEach(BiConsumer\<? super K, ? super V> b)|void
| get(Object o)|byte
| get(Object o)|Object
| get(int i)|byte
| getOrDefault(Object arg0, Object arg1)|Object
| int2ByteEntrySet()|ObjectSet\<Int2ByteMap$Entry>
| keySet()|Set
| keySet()|IntSet
| merge(Object arg0, Object arg1, BiFunction\<? super V, ? super V, ? extends V> arg2)|Object
| put(int arg0, byte arg1)|byte
| put(int arg0, byte arg1)|byte
| put(Object arg0, Object arg1)|Object
| putAll(Map\<? extends java.lang.Integer, ? extends java.lang.Byte> m)|void
| putIfAbsent(Object arg0, Object arg1)|Object
| remove(int i)|byte
| remove(Object o)|byte
| remove(Object o)|Object
| remove(Object arg0, Object arg1)|boolean
| replace(Object arg0, Object arg1)|Object
| replace(Object arg0, Object arg1, Object arg2)|boolean
| replaceAll(BiFunction\<? super K, ? super V, ? extends V> b)|void
| size()|int
| size()|int
| values()|Collection
| values()|ByteCollection
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Hash

|Interface
|--
|it.unimi.dsi.fastutil.Hash

---

|Extends
|--

---

## ObjectSet

|Interface
|--
|it.unimi.dsi.fastutil.objects.ObjectSet

---

|Extends
|--
|ObjectCollection
|Set

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(Object o)|boolean
| add(Object o)|boolean
| addAll(Collection\<? extends E> c)|boolean
| addAll(Collection\<? extends E> c)|boolean
| clear()|void
| clear()|void
| contains(Object o)|boolean
| contains(Object o)|boolean
| containsAll(Collection\<?> c)|boolean
| containsAll(Collection\<?> c)|boolean
| forEach(Consumer\<? super T> c)|void
| iterator()|ObjectIterator\<K>
| iterator()|Iterator\<E>
| iterator()|Iterator\<T>
| iterator()|Iterator\<E>
| objectIterator()|ObjectIterator\<K>
| parallelStream()|Stream\<E>
| remove(Object o)|boolean
| removeAll(Collection\<?> c)|boolean
| removeAll(Collection\<?> c)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| retainAll(Collection\<?> c)|boolean
| retainAll(Collection\<?> c)|boolean
| size()|int
| size()|int
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| toArray(Object[] o)|Object[]
| toArray()|Object[]
| toArray()|Object[]
| toArray(Object[] o)|Object[]

---

## Int2ByteMap$FastEntrySet

|Interface
|--
|it.unimi.dsi.fastutil.ints.Int2ByteMap$FastEntrySet

---

|Extends
|--
|ObjectSet

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(Object o)|boolean
| add(Object o)|boolean
| addAll(Collection\<? extends E> c)|boolean
| addAll(Collection\<? extends E> c)|boolean
| clear()|void
| clear()|void
| contains(Object o)|boolean
| contains(Object o)|boolean
| containsAll(Collection\<?> c)|boolean
| containsAll(Collection\<?> c)|boolean
| fastIterator()|ObjectIterator\<Int2ByteMap$Entry>
| forEach(Consumer\<? super T> c)|void
| iterator()|ObjectIterator\<K>
| iterator()|Iterator\<E>
| iterator()|Iterator\<T>
| iterator()|Iterator\<E>
| objectIterator()|ObjectIterator\<K>
| parallelStream()|Stream\<E>
| remove(Object o)|boolean
| removeAll(Collection\<?> c)|boolean
| removeAll(Collection\<?> c)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| retainAll(Collection\<?> c)|boolean
| retainAll(Collection\<?> c)|boolean
| size()|int
| size()|int
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| toArray(Object[] o)|Object[]
| toArray()|Object[]
| toArray()|Object[]
| toArray(Object[] o)|Object[]

---

## IntSet

|Interface
|--
|it.unimi.dsi.fastutil.ints.IntSet

---

|Extends
|--
|IntCollection
|Set

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(int i)|boolean
| add(Object o)|boolean
| add(Object o)|boolean
| addAll(IntCollection i)|boolean
| addAll(Collection\<? extends E> c)|boolean
| addAll(Collection\<? extends E> c)|boolean
| clear()|void
| clear()|void
| contains(int i)|boolean
| contains(Object o)|boolean
| contains(Object o)|boolean
| containsAll(IntCollection i)|boolean
| containsAll(Collection\<?> c)|boolean
| containsAll(Collection\<?> c)|boolean
| forEach(Consumer\<? super T> c)|void
| intIterator()|IntIterator
| iterator()|IntIterator
| iterator()|Iterator\<E>
| iterator()|Iterator\<T>
| iterator()|Iterator\<E>
| parallelStream()|Stream\<E>
| rem(int i)|boolean
| remove(int i)|boolean
| remove(Object o)|boolean
| remove(Object o)|boolean
| removeAll(IntCollection i)|boolean
| removeAll(Collection\<?> c)|boolean
| removeAll(Collection\<?> c)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| retainAll(IntCollection i)|boolean
| retainAll(Collection\<?> c)|boolean
| retainAll(Collection\<?> c)|boolean
| size()|int
| size()|int
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| toArray(int[] i)|int[]
| toArray(Object[] o)|Object[]
| toArray()|Object[]
| toArray()|Object[]
| toArray(Object[] o)|Object[]
| toIntArray()|int[]
| toIntArray(int[] i)|int[]

---

## ByteCollection

|Interface
|--
|it.unimi.dsi.fastutil.bytes.ByteCollection

---

|Extends
|--
|Collection
|ByteIterable

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(byte b)|boolean
| add(Object o)|boolean
| addAll(ByteCollection b)|boolean
| addAll(Collection\<? extends E> c)|boolean
| byteIterator()|ByteIterator
| clear()|void
| contains(byte b)|boolean
| contains(Object o)|boolean
| containsAll(ByteCollection b)|boolean
| containsAll(Collection\<?> c)|boolean
| forEach(Consumer\<? super T> c)|void
| iterator()|ByteIterator
| iterator()|Iterator\<E>
| iterator()|Iterator\<T>
| parallelStream()|Stream\<E>
| rem(byte b)|boolean
| remove(Object o)|boolean
| removeAll(ByteCollection b)|boolean
| removeAll(Collection\<?> c)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| retainAll(ByteCollection b)|boolean
| retainAll(Collection\<?> c)|boolean
| size()|int
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| toArray(byte[] b)|byte[]
| toArray(Object[] o)|Object[]
| toArray()|Object[]
| toByteArray()|byte[]
| toByteArray(byte[] b)|byte[]

---

## AbstractIntSet

|Class
|--
|it.unimi.dsi.fastutil.ints.AbstractIntSet

---

|Extends
|--
|AbstractIntCollection
|Cloneable
|IntSet

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(int i)|boolean
| add(int i)|boolean
| add(Object o)|boolean
| addAll(IntCollection i)|boolean
| addAll(Collection\<? extends java.lang.Integer> c)|boolean
| clear()|void
| contains(int i)|boolean
| contains(Object o)|boolean
| containsAll(Collection\<?> c)|boolean
| containsAll(IntCollection i)|boolean
| forEach(Consumer\<? super T> c)|void
| intIterator()|IntIterator
| iterator()|IntIterator
| iterator()|Iterator
| parallelStream()|Stream\<E>
| rem(int i)|boolean
| rem(Object o)|boolean
| remove(int i)|boolean
| remove(Object o)|boolean
| removeAll(Collection\<?> c)|boolean
| removeAll(IntCollection i)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| retainAll(Collection\<?> c)|boolean
| retainAll(IntCollection i)|boolean
| size()|int
| size()|int
| size()|int
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| toArray()|Object[]
| toArray(Object[] o)|Object[]
| toArray(int[] i)|int[]
| toIntArray()|int[]
| toIntArray(int[] i)|int[]
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## IntCollection

|Interface
|--
|it.unimi.dsi.fastutil.ints.IntCollection

---

|Extends
|--
|Collection
|IntIterable

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(int i)|boolean
| add(Object o)|boolean
| addAll(IntCollection i)|boolean
| addAll(Collection\<? extends E> c)|boolean
| clear()|void
| contains(int i)|boolean
| contains(Object o)|boolean
| containsAll(IntCollection i)|boolean
| containsAll(Collection\<?> c)|boolean
| forEach(Consumer\<? super T> c)|void
| intIterator()|IntIterator
| iterator()|IntIterator
| iterator()|Iterator\<E>
| iterator()|Iterator\<T>
| parallelStream()|Stream\<E>
| rem(int i)|boolean
| remove(Object o)|boolean
| removeAll(IntCollection i)|boolean
| removeAll(Collection\<?> c)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| retainAll(IntCollection i)|boolean
| retainAll(Collection\<?> c)|boolean
| size()|int
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| toArray(int[] i)|int[]
| toArray(Object[] o)|Object[]
| toArray()|Object[]
| toIntArray()|int[]
| toIntArray(int[] i)|int[]

---

## IntIterator

|Interface
|--
|it.unimi.dsi.fastutil.ints.IntIterator

---

|Extends
|--
|Iterator

---

|Methods|Return Type
|--|--
| forEachRemaining(Consumer\<? super E> c)|void
| hasNext()|boolean
| next()|Object
| nextInt()|int
| remove()|void
| skip(int i)|int

---

## AbstractInt2ObjectMap

|Class
|--
|it.unimi.dsi.fastutil.ints.AbstractInt2ObjectMap

---

|Extends
|--
|AbstractInt2ObjectFunction
|Int2ObjectMap
|Serializable

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| clear()|void
| compute(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| computeIfAbsent(Object arg0, Function\<? super K, ? extends V> arg1)|Object
| computeIfPresent(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| containsKey(int i)|boolean
| containsKey(Object o)|boolean
| containsValue(Object o)|boolean
| defaultReturnValue(Object o)|void
| defaultReturnValue()|Object
| entrySet()|Set
| entrySet()|ObjectSet\<java.util.Map$Entry\<java.lang.Integer, V>>
| forEach(BiConsumer\<? super K, ? super V> b)|void
| get(Object o)|Object
| get(int i)|Object
| getOrDefault(Object arg0, Object arg1)|Object
| int2ObjectEntrySet()|ObjectSet\<it.unimi.dsi.fastutil.ints.Int2ObjectMap$Entry\<V>>
| keySet()|Set
| keySet()|IntSet
| merge(Object arg0, Object arg1, BiFunction\<? super V, ? super V, ? extends V> arg2)|Object
| put(int arg0, Object arg1)|Object
| put(Object arg0, Object arg1)|Object
| put(int arg0, Object arg1)|Object
| putAll(Map\<? extends java.lang.Integer, ? extends V> m)|void
| putIfAbsent(Object arg0, Object arg1)|Object
| remove(int i)|Object
| remove(Object o)|Object
| remove(Object arg0, Object arg1)|boolean
| replace(Object arg0, Object arg1)|Object
| replace(Object arg0, Object arg1, Object arg2)|boolean
| replaceAll(BiFunction\<? super K, ? super V, ? extends V> b)|void
| size()|int
| size()|int
| values()|Collection
| values()|ObjectCollection\<V>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Int2ObjectMap$FastEntrySet

|Interface
|--
|it.unimi.dsi.fastutil.ints.Int2ObjectMap$FastEntrySet

---

|Extends
|--
|ObjectSet

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(Object o)|boolean
| add(Object o)|boolean
| addAll(Collection\<? extends E> c)|boolean
| addAll(Collection\<? extends E> c)|boolean
| clear()|void
| clear()|void
| contains(Object o)|boolean
| contains(Object o)|boolean
| containsAll(Collection\<?> c)|boolean
| containsAll(Collection\<?> c)|boolean
| fastIterator()|ObjectIterator\<it.unimi.dsi.fastutil.ints.Int2ObjectMap$Entry\<V>>
| forEach(Consumer\<? super T> c)|void
| iterator()|ObjectIterator\<K>
| iterator()|Iterator\<E>
| iterator()|Iterator\<T>
| iterator()|Iterator\<E>
| objectIterator()|ObjectIterator\<K>
| parallelStream()|Stream\<E>
| remove(Object o)|boolean
| removeAll(Collection\<?> c)|boolean
| removeAll(Collection\<?> c)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| retainAll(Collection\<?> c)|boolean
| retainAll(Collection\<?> c)|boolean
| size()|int
| size()|int
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| toArray(Object[] o)|Object[]
| toArray()|Object[]
| toArray()|Object[]
| toArray(Object[] o)|Object[]

---

## ObjectCollection

|Interface
|--
|it.unimi.dsi.fastutil.objects.ObjectCollection

---

|Extends
|--
|Collection
|ObjectIterable

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(Object o)|boolean
| addAll(Collection\<? extends E> c)|boolean
| clear()|void
| contains(Object o)|boolean
| containsAll(Collection\<?> c)|boolean
| forEach(Consumer\<? super T> c)|void
| iterator()|ObjectIterator\<K>
| iterator()|Iterator\<E>
| iterator()|Iterator\<T>
| objectIterator()|ObjectIterator\<K>
| parallelStream()|Stream\<E>
| remove(Object o)|boolean
| removeAll(Collection\<?> c)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| retainAll(Collection\<?> c)|boolean
| size()|int
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| toArray(Object[] o)|Object[]
| toArray()|Object[]

---

## DependencyRequirement

|Class
|--
|com.feed_the_beast.ftbquests.quest.DependencyRequirement

---

|Extends
|--
|Enum
|WithID

---

|Fields|Type
|--|--
|  completed|boolean
|  declaringClass|Class\<E>
|  id|String
|  one|boolean

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WeightedReward

|Class
|--
|com.feed_the_beast.ftbquests.quest.loot.WeightedReward

---

|Extends
|--
|Comparable

---

|Fields|Type
|--|--
|  reward|Reward
|  weight|int

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(WeightedReward w)|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## FinalIDObject

|Class
|--
|com.feed_the_beast.ftblib.lib.util.FinalIDObject

---

|Extends
|--
|WithID

---

|Fields|Type
|--|--
|  id|String

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ConfigValueInstance

|Class
|--
|com.feed_the_beast.ftblib.lib.config.ConfigValueInstance

---

|Extends
|--
|FinalIDObject

---

|Fields|Type
|--|--
|  canEdit|boolean
|  defaultValue|ConfigValue
|  displayName|TextComponent
|  excluded|boolean
|  group|ConfigGroup
|  hidden|boolean
|  icon|Icon
|  id|String
|  info|TextComponent
|  order|int
|  path|String
|  useScrollBar|boolean
|  value|ConfigValue

---

|Methods|Return Type
|--|--
| copy(ConfigGroup c)|ConfigValueInstance
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeData(DataOut d)|void

---

## ConfigValue

|Class
|--
|com.feed_the_beast.ftblib.lib.config.ConfigValue

---

|Extends
|--
|WithID

---

|Fields|Type
|--|--
|  boolean|boolean
|  color|Color4I
|  empty|boolean
|  id|String
|  string|String
|  stringForGUI|TextComponent
|  timer|Ticks
|  variants|List\<String>

---

|Methods|Return Type
|--|--
| addInfo(ConfigValueInstance arg0, List\<String> arg1)|void
| copy()|ConfigValue
| equalsValue(ConfigValue c)|boolean
| getDouble()|double
| getInt()|int
| getLong()|long
| isNull()|boolean
| onClicked(OpenableGui arg0, ConfigValueInstance arg1, MouseButton arg2, Runnable arg3)|void
| readData(DataIn d)|void
| readFromNBT(NBTTagCompound arg0, String arg1)|void
| setValueFromJson(JsonElement j)|void
| setValueFromOtherValue(ConfigValue c)|void
| setValueFromString(CommandSender arg0, String arg1, boolean arg2)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeData(DataOut d)|void
| writeToNBT(NBTTagCompound arg0, String arg1)|void

---

## BooleanConsumer

|Interface
|--
|com.feed_the_beast.ftblib.lib.util.misc.BooleanConsumer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| accept(boolean b)|void

---

## NameMap

|Class
|--
|com.feed_the_beast.ftblib.lib.util.misc.NameMap

---

|Extends
|--
|Iterable
|DataIn$Deserializer
|DataOut$Serializer

---

|Fields|Type
|--|--
|  defaultValue|Object
|  keys|List\<String>
|  map|Map\<String, E>
|  values|List\<E>

---

|Methods|Return Type
|--|--
| forEach(Consumer\<? super T> c)|void
| get(String s)|Object
| get(int i)|Object
| getColor(Object o)|Color4I
| getDisplayName(CommandSender arg0, Object arg1)|TextComponent
| getIndex(Object o)|int
| getName(Object o)|String
| getNext(Object o)|Object
| getNullable(String s)|Object
| getPrevious(Object o)|Object
| getRandom(Random r)|Object
| getStringIndex(String s)|int
| iterator()|Iterator\<E>
| offset(Object arg0, int arg1)|Object
| read(DataIn d)|Object
| readFromNBT(NBTTagCompound arg0, String arg1, EnumSaveType arg2)|Object
| size()|int
| spliterator()|Spliterator\<T>
| wait(long arg0, int arg1)|void
| wait(long l)|void
| withDefault(Object o)|NameMap\<E>
| write(DataOut arg0, Object arg1)|void
| writeToNBT(NBTTagCompound arg0, String arg1, EnumSaveType arg2, Object arg3)|void

---

## PlayerInteractionManager

|Class
|--
|net.minecraft.server.management.PlayerInteractionManager

---

|Extends
|--

---

|Fields|Type
|--|--
|  blockReachDistance|double
|  field_73088_d|boolean
|  field_73090_b|EntityPlayerMP
|  field_73092_a|World

---

|Methods|Return Type
|--|--
| func_180237_b(BlockPos b)|boolean
| func_180238_e()|void
| func_180239_c()|boolean
| func_180784_a(BlockPos arg0, EnumFacing arg1)|void
| func_180785_a(BlockPos b)|void
| func_187250_a(EntityPlayer arg0, World arg1, ItemStack arg2, EnumHand arg3)|EnumActionResult
| func_187251_a(EntityPlayer arg0, World arg1, ItemStack arg2, EnumHand arg3, BlockPos arg4, EnumFacing arg5, float arg6, float arg7, float arg8)|EnumActionResult
| func_73075_a()|void
| func_73076_a(GameType g)|void
| func_73077_b(GameType g)|void
| func_73080_a(WorldServer w)|void
| func_73081_b()|GameType
| func_73083_d()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NetHandlerPlayServer

|Class
|--
|net.minecraft.network.NetHandlerPlayServer

---

|Extends
|--
|NetHandlerPlayServer
|Tickable

---

|Fields|Type
|--|--
|  field_147365_f|int
|  field_147367_d|MinecraftServer
|  field_147368_e|int
|  field_147369_b|EntityPlayerMP
|  field_147371_a|NetworkManager
|  field_184343_A|int
|  field_184362_y|Vec3d

---

|Methods|Return Type
|--|--
| func_147231_a(TextComponent t)|void
| func_147338_a(CPacketEnchantItem c)|void
| func_147339_a(CPacketConfirmTransaction c)|void
| func_147340_a(CPacketUseEntity c)|void
| func_147341_a(CPacketTabComplete c)|void
| func_147342_a(CPacketClientStatus c)|void
| func_147343_a(CPacketUpdateSign c)|void
| func_147344_a(CPacketCreativeInventoryAction c)|void
| func_147345_a(CPacketPlayerDigging c)|void
| func_147346_a(CPacketPlayerTryUseItem c)|void
| func_147347_a(CPacketPlayer c)|void
| func_147348_a(CPacketPlayerAbilities c)|void
| func_147349_a(CPacketCustomPayload c)|void
| func_147351_a(CPacketClickWindow c)|void
| func_147352_a(CPacketClientSettings c)|void
| func_147353_a(CPacketKeepAlive c)|void
| func_147354_a(CPacketChatMessage c)|void
| func_147355_a(CPacketHeldItemChange c)|void
| func_147356_a(CPacketCloseWindow c)|void
| func_147357_a(CPacketEntityAction c)|void
| func_147358_a(CPacketInput c)|void
| func_147359_a(Packet\<?> p)|void
| func_147362_b()|NetworkManager
| func_147364_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_175086_a(CPacketResourcePackStatus c)|void
| func_175087_a(CPacketAnimation c)|void
| func_175088_a(CPacketSpectate c)|void
| func_175089_a(double arg0, double arg1, double arg2, float arg3, float arg4, Set\<SPacketPlayerPosLook$EnumFlags> arg5)|void
| func_184337_a(CPacketPlayerTryUseItemOnBlock c)|void
| func_184338_a(CPacketVehicleMove c)|void
| func_184339_a(CPacketConfirmTeleport c)|void
| func_184340_a(CPacketSteerBoat c)|void
| func_191984_a(CPacketRecipeInfo c)|void
| func_194027_a(CPacketSeenAdvancements c)|void
| func_194028_b(TextComponent t)|void
| func_194308_a(CPacketPlaceRecipe c)|void
| func_73660_a()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## StatisticsManagerServer

|Class
|--
|net.minecraft.stats.StatisticsManagerServer

---

|Extends
|--
|StatisticsManager

---

|Methods|Return Type
|--|--
| func_150871_b(EntityPlayer arg0, StatBase arg1, int arg2)|void
| func_150873_a(EntityPlayer arg0, StatBase arg1, int arg2)|void
| func_150876_a(EntityPlayerMP e)|void
| func_150877_d()|void
| func_150881_a(String s)|Map\<StatBase, TupleIntJsonSerializable>
| func_150882_a()|void
| func_150883_b()|void
| func_77444_a(StatBase s)|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketClientSettings

|Class
|--
|net.minecraft.network.play.client.CPacketClientSettings

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayServer n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149520_f()|boolean
| func_149521_d()|int
| func_149523_e()|EntityPlayer$EnumChatVisibility
| func_149524_c()|String
| func_186991_f()|EnumHandSide
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RecipeBookServer

|Class
|--
|net.minecraft.stats.RecipeBookServer

---

|Extends
|--
|RecipeBook

---

|Methods|Return Type
|--|--
| func_192810_b(boolean b)|void
| func_192812_b()|boolean
| func_192813_a(boolean b)|void
| func_192815_c()|boolean
| func_192824_e()|NBTTagCompound
| func_192825_a(NBTTagCompound n)|void
| func_192826_c(EntityPlayerMP e)|void
| func_193824_a(RecipeBook r)|void
| func_193825_e(Recipe r)|void
| func_193830_f(Recipe r)|boolean
| func_193831_b(Recipe r)|void
| func_193834_b(List\<Recipe> arg0, EntityPlayerMP arg1)|void
| func_193835_a(List\<Recipe> arg0, EntityPlayerMP arg1)|void
| func_194073_a(Recipe r)|void
| func_194074_f(Recipe r)|void
| func_194076_e(Recipe r)|boolean
| func_194079_d()|List\<Recipe>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PlayerAdvancements

|Class
|--
|net.minecraft.advancements.PlayerAdvancements

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_192739_a(EntityPlayerMP e)|void
| func_192741_b(EntityPlayerMP e)|void
| func_192744_b(Advancement arg0, String arg1)|boolean
| func_192745_a()|void
| func_192747_a(Advancement a)|AdvancementProgress
| func_192749_b()|void
| func_192750_a(Advancement arg0, String arg1)|boolean
| func_193766_b()|void
| func_194220_a(Advancement a)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## DataIn$Deserializer

|Interface
|--
|com.feed_the_beast.ftblib.lib.io.DataIn$Deserializer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| read(DataIn d)|Object

---

## BlockDimPos

|Class
|--
|com.feed_the_beast.ftblib.lib.math.BlockDimPos

---

|Extends
|--

---

|Fields|Type
|--|--
|  blockPos|BlockPos
|  dim|int
|  posX|int
|  posY|int
|  posZ|int

---

|Methods|Return Type
|--|--
| add(int arg0, int arg1, int arg2)|BlockDimPos
| copy()|BlockDimPos
| equalsPos(BlockDimPos b)|boolean
| teleporter()|TeleporterDimPos
| toChunkPos()|ChunkDimPos
| toIntArray()|int[]
| toVec()|Vec3d
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## IntList

|Interface
|--
|it.unimi.dsi.fastutil.ints.IntList

---

|Extends
|--
|List
|Comparable
|IntCollection

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(int i)|boolean
| add(int arg0, int arg1)|void
| add(Object o)|boolean
| add(int arg0, Object arg1)|void
| add(Object o)|boolean
| addAll(IntList i)|boolean
| addAll(int arg0, IntList arg1)|boolean
| addAll(int arg0, IntCollection arg1)|boolean
| addAll(Collection\<? extends E> c)|boolean
| addAll(int arg0, Collection\<? extends E> arg1)|boolean
| addAll(IntCollection i)|boolean
| addAll(Collection\<? extends E> c)|boolean
| addElements(int arg0, int[] arg1, int arg2, int arg3)|void
| addElements(int arg0, int[] arg1)|void
| clear()|void
| clear()|void
| compareTo(Object o)|int
| contains(Object o)|boolean
| contains(int i)|boolean
| contains(Object o)|boolean
| containsAll(Collection\<?> c)|boolean
| containsAll(IntCollection i)|boolean
| containsAll(Collection\<?> c)|boolean
| forEach(Consumer\<? super T> c)|void
| get(int i)|Object
| getElements(int arg0, int[] arg1, int arg2, int arg3)|void
| getInt(int i)|int
| indexOf(int i)|int
| indexOf(Object o)|int
| intIterator()|IntIterator
| intListIterator()|IntListIterator
| intListIterator(int i)|IntListIterator
| intSubList(int arg0, int arg1)|IntList
| iterator()|IntListIterator
| iterator()|Iterator\<E>
| iterator()|IntIterator
| iterator()|Iterator\<E>
| iterator()|Iterator\<T>
| lastIndexOf(int i)|int
| lastIndexOf(Object o)|int
| listIterator(int i)|IntListIterator
| listIterator()|IntListIterator
| listIterator(int i)|ListIterator\<E>
| listIterator()|ListIterator\<E>
| parallelStream()|Stream\<E>
| rem(int i)|boolean
| remove(int i)|Object
| remove(Object o)|boolean
| remove(Object o)|boolean
| removeAll(Collection\<?> c)|boolean
| removeAll(IntCollection i)|boolean
| removeAll(Collection\<?> c)|boolean
| removeElements(int arg0, int arg1)|void
| removeIf(Predicate\<? super E> p)|boolean
| removeInt(int i)|int
| replaceAll(UnaryOperator\<E> u)|void
| retainAll(Collection\<?> c)|boolean
| retainAll(IntCollection i)|boolean
| retainAll(Collection\<?> c)|boolean
| set(int arg0, int arg1)|int
| set(int arg0, Object arg1)|Object
| size(int i)|void
| size()|int
| size()|int
| sort(Comparator\<? super E> c)|void
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| subList(int arg0, int arg1)|IntList
| subList(int arg0, int arg1)|List\<E>
| toArray()|Object[]
| toArray(Object[] o)|Object[]
| toArray(int[] i)|int[]
| toArray(Object[] o)|Object[]
| toArray()|Object[]
| toIntArray()|int[]
| toIntArray(int[] i)|int[]

---

## DataOut$Serializer

|Interface
|--
|com.feed_the_beast.ftblib.lib.io.DataOut$Serializer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| write(DataOut arg0, Object arg1)|void

---

## FireworksJS$Shape

|Class
|--
|dev.latvian.kubejs.world.FireworksJS$Shape

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>
|  type|int

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ServerPlayerData

|Class
|--
|dev.latvian.kubejs.player.ServerPlayerDataJS

---

|Extends
|--
|PlayerData

---

|Fields|Type
|--|--
|  data Temporary data, mods can attach objects to this|AttachedData
|  id|UUID
|  name|String
|  overworld|World
|  player|ServerPlayer
|  playerEntity|EntityPlayer
|  profile|GameProfile
|  server|Server

---

|Methods|Return Type
|--|--
| hasClientMod()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## IScoreCriteria$EnumRenderType

|Class
|--
|net.minecraft.scoreboard.IScoreCriteria$EnumRenderType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_178796_a()|String
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Village

|Class
|--
|net.minecraft.village.Village

---

|Extends
|--
|CapabilitySerializable

---

|Methods|Return Type
|--|--
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_179863_c(BlockPos b)|VillageDoorInfo
| func_179864_e(BlockPos b)|VillageDoorInfo
| func_179865_b(BlockPos b)|VillageDoorInfo
| func_179866_a(BlockPos b)|boolean
| func_180608_a()|BlockPos
| func_75558_f()|List\<VillageDoorInfo>
| func_75560_a(int i)|void
| func_75561_d()|int
| func_75562_e()|int
| func_75566_g()|boolean
| func_75567_c()|int
| func_75568_b()|int
| func_75571_b(EntityLivingBase e)|EntityLivingBase
| func_75575_a(EntityLivingBase e)|void
| func_75576_a(VillageDoorInfo v)|void
| func_82683_b(int i)|void
| func_82684_a(String s)|int
| func_82685_c(EntityLivingBase e)|EntityPlayer
| func_82686_i()|boolean
| func_82687_d(String s)|boolean
| func_82688_a(String arg0, int arg1)|int
| func_82689_b(NBTTagCompound n)|void
| func_82690_a(NBTTagCompound n)|void
| func_82691_a(World w)|void
| func_82692_h()|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPlayerReputation(UUID u)|int
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isPlayerReputationTooLow(UUID u)|boolean
| modifyPlayerReputation(UUID arg0, int arg1)|int
| serializeNBT()|NBTBase
| serializeNBT()|NBTTagCompound
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## IRenderHandler

|Class
|--
|net.minecraftforge.client.IRenderHandler

---

|Extends
|--

---

|Methods|Return Type
|--|--
| render(float arg0, WorldClient arg1, Minecraft arg2)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WorldProvider$WorldSleepResult

|Class
|--
|net.minecraft.world.WorldProvider$WorldSleepResult

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## DimensionType

|Class
|--
|net.minecraft.world.DimensionType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_186065_b()|String
| func_186067_c()|String
| func_186068_a()|int
| func_186070_d()|WorldProvider
| name()|String
| ordinal()|int
| setLoadSpawn(boolean b)|DimensionType
| shouldLoadSpawn()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ChunkGenerator

|Interface
|--
|net.minecraft.world.gen.IChunkGenerator

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_177458_a(EnumCreatureType arg0, BlockPos arg1)|List\<Biome$SpawnListEntry>
| func_180513_a(World arg0, String arg1, BlockPos arg2, boolean arg3)|BlockPos
| func_180514_a(Chunk arg0, int arg1, int arg2)|void
| func_185931_b(int arg0, int arg1)|void
| func_185932_a(int arg0, int arg1)|Chunk
| func_185933_a(Chunk arg0, int arg1, int arg2)|boolean
| func_193414_a(World arg0, String arg1, BlockPos arg2)|boolean

---

## ForgeChunkManager$Type

|Class
|--
|net.minecraftforge.common.ForgeChunkManager$Type

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GenLayer

|Class
|--
|net.minecraft.world.gen.layer.GenLayer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_75903_a(long arg0, long arg1)|void
| func_75904_a(int arg0, int arg1, int arg2, int arg3)|int[]
| func_75905_a(long l)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ChunkGeneratorSettings

|Class
|--
|net.minecraft.world.gen.ChunkGeneratorSettings

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_177777_D|int
|  field_177778_E|boolean
|  field_177779_F|int
|  field_177780_G|int
|  field_177781_A|boolean
|  field_177782_B|int
|  field_177783_C|boolean
|  field_177784_L|int
|  field_177785_M|int
|  field_177786_N|int
|  field_177787_O|int
|  field_177788_H|int
|  field_177789_I|int
|  field_177790_J|int
|  field_177791_K|int
|  field_177792_U|int
|  field_177793_T|int
|  field_177794_W|int
|  field_177795_V|int
|  field_177796_Q|int
|  field_177797_P|int
|  field_177798_S|int
|  field_177799_R|int
|  field_177800_Y|int
|  field_177801_X|int
|  field_177802_Z|int
|  field_177803_f|float
|  field_177804_g|float
|  field_177805_az|int
|  field_177806_d|float
|  field_177807_ay|int
|  field_177808_e|float
|  field_177809_b|float
|  field_177810_c|float
|  field_177811_a|float
|  field_177812_at|int
|  field_177813_n|float
|  field_177814_as|int
|  field_177815_o|float
|  field_177816_ar|int
|  field_177817_l|float
|  field_177818_aq|int
|  field_177819_m|float
|  field_177820_ax|int
|  field_177821_j|float
|  field_177822_aw|int
|  field_177823_k|float
|  field_177824_av|int
|  field_177825_h|float
|  field_177826_au|int
|  field_177827_i|float
|  field_177828_ak|int
|  field_177829_w|boolean
|  field_177830_al|int
|  field_177831_v|boolean
|  field_177832_ai|int
|  field_177833_u|boolean
|  field_177834_aj|int
|  field_177835_t|int
|  field_177836_ao|int
|  field_177837_s|boolean
|  field_177838_ap|int
|  field_177839_r|boolean
|  field_177840_am|int
|  field_177841_q|int
|  field_177842_an|int
|  field_177843_p|float
|  field_177844_ac|int
|  field_177845_ad|int
|  field_177846_aa|int
|  field_177847_ab|int
|  field_177848_ag|int
|  field_177849_ah|int
|  field_177850_z|boolean
|  field_177851_ae|int
|  field_177852_y|boolean
|  field_177853_af|int
|  field_177854_x|boolean
|  field_191077_z|boolean

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GuiCreateWorld

|Class
|--
|net.minecraft.client.gui.GuiCreateWorld

---

|Extends
|--
|GuiScreen

---

|Fields|Type
|--|--
|  field_146287_f|int
|  field_146288_g|long
|  field_146290_a|GuiButton
|  field_146291_p|boolean
|  field_146292_n|List\<GuiButton>
|  field_146294_l|int
|  field_146295_m|int
|  field_146297_k|Minecraft
|  field_146298_h|int
|  field_146331_K|int
|  field_146334_a|String
|  field_73735_i|float

---

|Methods|Return Type
|--|--
| func_146269_k()|void
| func_146270_b(int i)|void
| func_146274_d()|void
| func_146276_q_()|void
| func_146278_c(int i)|void
| func_146279_a(String arg0, int arg1, int arg2)|void
| func_146280_a(Minecraft arg0, int arg1, int arg2)|void
| func_146281_b()|void
| func_146282_l()|void
| func_146283_a(List\<String> arg0, int arg1, int arg2)|void
| func_146318_a(WorldInfo w)|void
| func_175174_a(float arg0, float arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_175175_a(int arg0, int arg1, TextureAtlasSprite arg2, int arg3, int arg4)|void
| func_175273_b(Minecraft arg0, int arg1, int arg2)|void
| func_175275_f(String s)|void
| func_175276_a(TextComponent t)|boolean
| func_175281_b(String arg0, boolean arg1)|void
| func_183500_a(int arg0, int arg1)|void
| func_191927_a(ItemStack i)|List\<String>
| func_193975_a(boolean b)|void
| func_193976_p()|boolean
| func_73729_b(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73731_b(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73732_a(FontRenderer arg0, String arg1, int arg2, int arg3, int arg4)|void
| func_73733_a(int arg0, int arg1, int arg2, int arg3, int arg4, int arg5)|void
| func_73863_a(int arg0, int arg1, float arg2)|void
| func_73866_w_()|void
| func_73868_f()|boolean
| func_73876_c()|void
| func_73878_a(boolean arg0, int arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NBTTagIntArray

|Class
|--
|net.minecraft.nbt.NBTTagIntArray

---

|Extends
|--
|NBTBase

---

|Methods|Return Type
|--|--
| func_150302_c()|int[]
| func_74732_a()|byte
| func_74737_b()|NBTBase
| func_74737_b()|NBTTagIntArray
| func_82582_d()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumBorderStatus

|Class
|--
|net.minecraft.world.border.EnumBorderStatus

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_177766_a()|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BorderListener

|Interface
|--
|net.minecraft.world.border.IBorderListener

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_177690_b(WorldBorder arg0, int arg1)|void
| func_177691_a(WorldBorder arg0, int arg1)|void
| func_177692_a(WorldBorder arg0, double arg1, double arg2, long arg3)|void
| func_177693_a(WorldBorder arg0, double arg1, double arg2)|void
| func_177694_a(WorldBorder arg0, double arg1)|void
| func_177695_c(WorldBorder arg0, double arg1)|void
| func_177696_b(WorldBorder arg0, double arg1)|void

---

## CapabilityDispatcher

|Class
|--
|net.minecraftforge.common.capabilities.CapabilityDispatcher

---

|Extends
|--
|NBTSerializable
|CapabilityProvider

---

|Methods|Return Type
|--|--
| areCompatible(CapabilityDispatcher c)|boolean
| deserializeNBT(NBTBase n)|void
| deserializeNBT(NBTTagCompound n)|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| serializeNBT()|NBTBase
| serializeNBT()|NBTTagCompound
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ExtendedBlockStorage

|Class
|--
|net.minecraft.world.chunk.storage.ExtendedBlockStorage

---

|Extends
|--

---

|Fields|Type
|--|--
|  blockRefCount|int

---

|Methods|Return Type
|--|--
| func_177484_a(int arg0, int arg1, int arg2, BlockState arg3)|void
| func_177485_a(int arg0, int arg1, int arg2)|BlockState
| func_186049_g()|BlockStateContainer
| func_76657_c(int arg0, int arg1, int arg2, int arg3)|void
| func_76659_c(NibbleArray n)|void
| func_76661_k()|NibbleArray
| func_76662_d()|int
| func_76663_a()|boolean
| func_76666_d(NibbleArray n)|void
| func_76670_c(int arg0, int arg1, int arg2)|int
| func_76671_l()|NibbleArray
| func_76672_e()|void
| func_76674_d(int arg0, int arg1, int arg2)|int
| func_76675_b()|boolean
| func_76677_d(int arg0, int arg1, int arg2, int arg3)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Chunk$EnumCreateEntityType

|Class
|--
|net.minecraft.world.chunk.Chunk$EnumCreateEntityType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ClassInheritanceMultiMap

|Class
|--
|net.minecraft.util.ClassInheritanceMultiMap

---

|Extends
|--
|AbstractSet

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(Object o)|boolean
| addAll(Collection\<? extends E> c)|boolean
| clear()|void
| contains(Object o)|boolean
| containsAll(Collection\<?> c)|boolean
| forEach(Consumer\<? super T> c)|void
| func_180215_b(Class\<S> c)|Iterable\<S>
| iterator()|Iterator\<T>
| parallelStream()|Stream\<E>
| remove(Object o)|boolean
| removeAll(Collection\<?> c)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| retainAll(Collection\<?> c)|boolean
| size()|int
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| toArray(Object[] o)|Object[]
| toArray()|Object[]
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PacketBuffer

|Class
|--
|net.minecraft.network.PacketBuffer

---

|Extends
|--
|ByteBuf

---

|Fields|Type
|--|--
|  direct|boolean
|  readable|boolean
|  readOnly|boolean
|  writable|boolean

---

|Methods|Return Type
|--|--
| alloc()|ByteBufAllocator
| array()|byte[]
| arrayOffset()|int
| asReadOnly()|ByteBuf
| bytesBefore(byte b)|int
| bytesBefore(int arg0, byte arg1)|int
| bytesBefore(int arg0, int arg1, byte arg2)|int
| capacity(int i)|ByteBuf
| capacity()|int
| clear()|ByteBuf
| compareTo(Object o)|int
| compareTo(ByteBuf b)|int
| copy()|ByteBuf
| copy(int arg0, int arg1)|ByteBuf
| discardReadBytes()|ByteBuf
| discardSomeReadBytes()|ByteBuf
| duplicate()|ByteBuf
| ensureWritable(int i)|ByteBuf
| ensureWritable(int arg0, boolean arg1)|int
| forEachByte(int arg0, int arg1, ByteProcessor arg2)|int
| forEachByte(ByteProcessor b)|int
| forEachByteDesc(ByteProcessor b)|int
| forEachByteDesc(int arg0, int arg1, ByteProcessor arg2)|int
| func_150786_a(NBTTagCompound n)|PacketBuffer
| func_150787_b(int i)|PacketBuffer
| func_150788_a(ItemStack i)|PacketBuffer
| func_150789_c(int i)|String
| func_150791_c()|ItemStack
| func_150792_a()|int
| func_150793_b()|NBTTagCompound
| func_179249_a(Enum\<?> e)|PacketBuffer
| func_179250_a(byte[] b)|PacketBuffer
| func_179251_a()|byte[]
| func_179252_a(UUID u)|PacketBuffer
| func_179253_g()|UUID
| func_179254_b(long l)|PacketBuffer
| func_179255_a(BlockPos b)|PacketBuffer
| func_179256_a(TextComponent t)|PacketBuffer
| func_179257_a(Class\<T> c)|Enum
| func_179258_d()|TextComponent
| func_179259_c()|BlockPos
| func_179260_f()|long
| func_180714_a(String s)|PacketBuffer
| func_186863_b()|int[]
| func_186865_a(long[] l)|PacketBuffer
| func_186873_b(long[] l)|long[]
| func_186875_a(int[] i)|PacketBuffer
| func_189423_a(long[] arg0, int arg1)|long[]
| func_189424_c(int i)|int[]
| func_189425_b(int i)|byte[]
| func_192572_a(ResourceLocation r)|PacketBuffer
| func_192573_m()|Date
| func_192574_a(Date d)|PacketBuffer
| func_192575_l()|ResourceLocation
| getBoolean(int i)|boolean
| getByte(int i)|byte
| getBytes(int arg0, ByteBuffer arg1)|ByteBuf
| getBytes(int arg0, OutputStream arg1, int arg2)|ByteBuf
| getBytes(int arg0, byte[] arg1)|ByteBuf
| getBytes(int arg0, GatheringByteChannel arg1, int arg2)|int
| getBytes(int arg0, FileChannel arg1, long arg2, int arg3)|int
| getBytes(int arg0, ByteBuf arg1)|ByteBuf
| getBytes(int arg0, ByteBuf arg1, int arg2)|ByteBuf
| getBytes(int arg0, ByteBuf arg1, int arg2, int arg3)|ByteBuf
| getBytes(int arg0, byte[] arg1, int arg2, int arg3)|ByteBuf
| getChar(int i)|char
| getCharSequence(int arg0, int arg1, Charset arg2)|CharSequence
| getDouble(int i)|double
| getFloat(int i)|float
| getInt(int i)|int
| getIntLE(int i)|int
| getLong(int i)|long
| getLongLE(int i)|long
| getMedium(int i)|int
| getMediumLE(int i)|int
| getShort(int i)|short
| getShortLE(int i)|short
| getUnsignedByte(int i)|short
| getUnsignedInt(int i)|long
| getUnsignedIntLE(int i)|long
| getUnsignedMedium(int i)|int
| getUnsignedMediumLE(int i)|int
| getUnsignedShort(int i)|int
| getUnsignedShortLE(int i)|int
| hasArray()|boolean
| hasMemoryAddress()|boolean
| indexOf(int arg0, int arg1, byte arg2)|int
| internalNioBuffer(int arg0, int arg1)|ByteBuffer
| markReaderIndex()|ByteBuf
| markWriterIndex()|ByteBuf
| maxCapacity()|int
| maxWritableBytes()|int
| memoryAddress()|long
| nioBuffer(int arg0, int arg1)|ByteBuffer
| nioBuffer()|ByteBuffer
| nioBufferCount()|int
| nioBuffers()|ByteBuffer[]
| nioBuffers(int arg0, int arg1)|ByteBuffer[]
| order()|ByteOrder
| order(ByteOrder b)|ByteBuf
| readableBytes()|int
| readBoolean()|boolean
| readByte()|byte
| readBytes(byte[] arg0, int arg1, int arg2)|ByteBuf
| readBytes(ByteBuffer b)|ByteBuf
| readBytes(OutputStream arg0, int arg1)|ByteBuf
| readBytes(GatheringByteChannel arg0, int arg1)|int
| readBytes(ByteBuf arg0, int arg1)|ByteBuf
| readBytes(int i)|ByteBuf
| readBytes(ByteBuf b)|ByteBuf
| readBytes(ByteBuf arg0, int arg1, int arg2)|ByteBuf
| readBytes(byte[] b)|ByteBuf
| readBytes(FileChannel arg0, long arg1, int arg2)|int
| readChar()|char
| readCharSequence(int arg0, Charset arg1)|CharSequence
| readDouble()|double
| readerIndex(int i)|ByteBuf
| readerIndex()|int
| readFloat()|float
| readInt()|int
| readIntLE()|int
| readLong()|long
| readLongLE()|long
| readMedium()|int
| readMediumLE()|int
| readRetainedSlice(int i)|ByteBuf
| readShort()|short
| readShortLE()|short
| readSlice(int i)|ByteBuf
| readUnsignedByte()|short
| readUnsignedInt()|long
| readUnsignedIntLE()|long
| readUnsignedMedium()|int
| readUnsignedMediumLE()|int
| readUnsignedShort()|int
| readUnsignedShortLE()|int
| refCnt()|int
| release(int i)|boolean
| release()|boolean
| resetReaderIndex()|ByteBuf
| resetWriterIndex()|ByteBuf
| retain(int i)|ByteBuf
| retain()|ReferenceCounted
| retain()|ByteBuf
| retain(int i)|ReferenceCounted
| retainedDuplicate()|ByteBuf
| retainedSlice(int arg0, int arg1)|ByteBuf
| retainedSlice()|ByteBuf
| setBoolean(int arg0, boolean arg1)|ByteBuf
| setByte(int arg0, int arg1)|ByteBuf
| setBytes(int arg0, ScatteringByteChannel arg1, int arg2)|int
| setBytes(int arg0, byte[] arg1, int arg2, int arg3)|ByteBuf
| setBytes(int arg0, ByteBuffer arg1)|ByteBuf
| setBytes(int arg0, FileChannel arg1, long arg2, int arg3)|int
| setBytes(int arg0, byte[] arg1)|ByteBuf
| setBytes(int arg0, ByteBuf arg1, int arg2)|ByteBuf
| setBytes(int arg0, ByteBuf arg1)|ByteBuf
| setBytes(int arg0, InputStream arg1, int arg2)|int
| setBytes(int arg0, ByteBuf arg1, int arg2, int arg3)|ByteBuf
| setChar(int arg0, int arg1)|ByteBuf
| setCharSequence(int arg0, CharSequence arg1, Charset arg2)|int
| setDouble(int arg0, double arg1)|ByteBuf
| setFloat(int arg0, float arg1)|ByteBuf
| setIndex(int arg0, int arg1)|ByteBuf
| setInt(int arg0, int arg1)|ByteBuf
| setIntLE(int arg0, int arg1)|ByteBuf
| setLong(int arg0, long arg1)|ByteBuf
| setLongLE(int arg0, long arg1)|ByteBuf
| setMedium(int arg0, int arg1)|ByteBuf
| setMediumLE(int arg0, int arg1)|ByteBuf
| setShort(int arg0, int arg1)|ByteBuf
| setShortLE(int arg0, int arg1)|ByteBuf
| setZero(int arg0, int arg1)|ByteBuf
| skipBytes(int i)|ByteBuf
| slice(int arg0, int arg1)|ByteBuf
| slice()|ByteBuf
| toString(Charset c)|String
| toString(int arg0, int arg1, Charset arg2)|String
| touch()|ByteBuf
| touch(Object o)|ByteBuf
| touch()|ReferenceCounted
| touch(Object o)|ReferenceCounted
| unwrap()|ByteBuf
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writableBytes()|int
| writeBoolean(boolean b)|ByteBuf
| writeByte(int i)|ByteBuf
| writeBytes(byte[] arg0, int arg1, int arg2)|ByteBuf
| writeBytes(byte[] b)|ByteBuf
| writeBytes(ByteBuf arg0, int arg1, int arg2)|ByteBuf
| writeBytes(ByteBuf arg0, int arg1)|ByteBuf
| writeBytes(ByteBuf b)|ByteBuf
| writeBytes(FileChannel arg0, long arg1, int arg2)|int
| writeBytes(ScatteringByteChannel arg0, int arg1)|int
| writeBytes(InputStream arg0, int arg1)|int
| writeBytes(ByteBuffer b)|ByteBuf
| writeChar(int i)|ByteBuf
| writeCharSequence(CharSequence arg0, Charset arg1)|int
| writeDouble(double d)|ByteBuf
| writeFloat(float f)|ByteBuf
| writeInt(int i)|ByteBuf
| writeIntLE(int i)|ByteBuf
| writeLong(long l)|ByteBuf
| writeLongLE(long l)|ByteBuf
| writeMedium(int i)|ByteBuf
| writeMediumLE(int i)|ByteBuf
| writerIndex()|int
| writerIndex(int i)|ByteBuf
| writeShort(int i)|ByteBuf
| writeShortLE(int i)|ByteBuf
| writeZero(int i)|ByteBuf

---

## BiomeDecorator

|Class
|--
|net.minecraft.world.biome.BiomeDecorator

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_150514_p|WorldGenFlowers
|  field_180293_d|ChunkGeneratorSettings
|  field_180294_c|BlockPos
|  field_180295_l|WorldGenerator
|  field_180296_j|WorldGenerator
|  field_180297_k|WorldGenerator
|  field_180298_q|WorldGenerator
|  field_180299_p|WorldGenerator
|  field_185425_a|boolean
|  field_189870_A|float
|  field_76798_D|int
|  field_76799_E|int
|  field_76800_F|int
|  field_76801_G|int
|  field_76802_A|int
|  field_76803_B|int
|  field_76804_C|int
|  field_76805_H|int
|  field_76806_I|int
|  field_76807_J|int
|  field_76808_K|boolean
|  field_76809_f|WorldGenerator
|  field_76810_g|WorldGenerator
|  field_76818_l|WorldGenerator
|  field_76819_m|WorldGenerator
|  field_76820_j|WorldGenerator
|  field_76821_k|WorldGenerator
|  field_76822_h|WorldGenerator
|  field_76823_i|WorldGenerator
|  field_76824_w|WorldGenerator
|  field_76825_v|WorldGenerator
|  field_76826_u|WorldGenerator
|  field_76827_t|WorldGenerator
|  field_76828_s|WorldGenerator
|  field_76831_p|WorldGenerator
|  field_76832_z|int
|  field_76833_y|int
|  field_76834_x|WorldGenerator

---

|Methods|Return Type
|--|--
| func_180292_a(World arg0, Random arg1, Biome arg2, BlockPos arg3)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Biome$TempCategory

|Class
|--
|net.minecraft.world.biome.Biome$TempCategory

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WorldGenAbstractTree

|Class
|--
|net.minecraft.world.gen.feature.WorldGenAbstractTree

---

|Extends
|--
|WorldGenerator

---

|Methods|Return Type
|--|--
| func_175904_e()|void
| func_180709_b(World arg0, Random arg1, BlockPos arg2)|boolean
| func_180711_a(World arg0, Random arg1, BlockPos arg2)|void
| isReplaceable(World arg0, BlockPos arg1)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ChunkPrimer

|Class
|--
|net.minecraft.world.chunk.ChunkPrimer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_177855_a(int arg0, int arg1, int arg2, BlockState arg3)|void
| func_177856_a(int arg0, int arg1, int arg2)|BlockState
| func_186138_a(int arg0, int arg1)|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockFlower$EnumFlowerType

|Class
|--
|net.minecraft.block.BlockFlower$EnumFlowerType

---

|Extends
|--
|Enum
|StringSerializable

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_176610_l()|String
| func_176963_d()|String
| func_176964_a()|BlockFlower$EnumFlowerColor
| func_176968_b()|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WorldGenerator

|Class
|--
|net.minecraft.world.gen.feature.WorldGenerator

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_175904_e()|void
| func_180709_b(World arg0, Random arg1, BlockPos arg2)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NetHandler

|Interface
|--
|net.minecraft.network.INetHandler

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_147231_a(TextComponent t)|void

---

## LootTable

|Class
|--
|net.minecraft.world.storage.loot.LootTable

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_186466_c|List\<LootPool>
|  frozen|boolean

---

|Methods|Return Type
|--|--
| addPool(LootPool l)|void
| freeze()|void
| func_186460_a(Inventory arg0, Random arg1, LootContext arg2)|void
| func_186462_a(Random arg0, LootContext arg1)|List\<ItemStack>
| getPool(String s)|LootPool
| removePool(String s)|LootPool
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NBTSerializable

|Interface
|--
|net.minecraftforge.common.util.INBTSerializable

---

|Extends
|--

---

|Methods|Return Type
|--|--
| deserializeNBT(NBTBase n)|void
| serializeNBT()|NBTBase

---

## PlayerFileData

|Interface
|--
|net.minecraft.world.storage.IPlayerFileData

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_75752_b(EntityPlayer e)|NBTTagCompound
| func_75753_a(EntityPlayer e)|void
| func_75754_f()|String[]

---

## ChunkLoader

|Interface
|--
|net.minecraft.world.chunk.storage.IChunkLoader

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_191063_a(int arg0, int arg1)|boolean
| func_75815_a(World arg0, int arg1, int arg2)|Chunk
| func_75816_a(World arg0, Chunk arg1)|void
| func_75817_a()|void
| func_75818_b()|void
| func_75819_b(World arg0, Chunk arg1)|void

---

## CrashReportDetail

|Interface
|--
|net.minecraft.crash.ICrashReportDetail

---

|Extends
|--
|Callable

---

|Methods|Return Type
|--|--
| call()|Object

---

## GameRules$ValueType

|Class
|--
|net.minecraft.world.GameRules$ValueType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ScoreObjective

|Class
|--
|net.minecraft.scoreboard.ScoreObjective

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178766_e()|IScoreCriteria$EnumRenderType
| func_178767_a(IScoreCriteria$EnumRenderType i)|void
| func_96678_d()|String
| func_96679_b()|String
| func_96680_c()|ScoreCriteria
| func_96681_a(String s)|void
| func_96682_a()|Scoreboard
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ScorePlayerTeam

|Class
|--
|net.minecraft.scoreboard.ScorePlayerTeam

---

|Extends
|--
|Team

---

|Methods|Return Type
|--|--
| func_142053_d(String s)|String
| func_142054_a(Team t)|boolean
| func_178770_i()|Team$EnumVisible
| func_178771_j()|Team$EnumVisible
| func_178772_a(Team$EnumVisible t)|void
| func_178773_b(Team$EnumVisible t)|void
| func_178774_a(TextFormatting t)|void
| func_178775_l()|TextFormatting
| func_186681_k()|Team$CollisionRule
| func_186682_a(Team$CollisionRule t)|void
| func_96660_a(boolean b)|void
| func_96661_b()|String
| func_96662_c(String s)|void
| func_96663_f()|String
| func_96664_a(String s)|void
| func_96665_g()|boolean
| func_96666_b(String s)|void
| func_96668_e()|String
| func_96669_c()|String
| func_96670_d()|Collection\<String>
| func_98297_h()|boolean
| func_98298_a(int i)|void
| func_98299_i()|int
| func_98300_b(boolean b)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Score

|Class
|--
|net.minecraft.scoreboard.Score

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178815_a(boolean b)|void
| func_178816_g()|boolean
| func_96645_d()|ScoreObjective
| func_96646_b(int i)|void
| func_96647_c(int i)|void
| func_96648_a()|void
| func_96649_a(int i)|void
| func_96650_f()|Scoreboard
| func_96652_c()|int
| func_96653_e()|String
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Capability$IStorage

|Interface
|--
|net.minecraftforge.common.capabilities.Capability$IStorage

---

|Extends
|--

---

|Methods|Return Type
|--|--
| readNBT(Capability\<T> arg0, Object arg1, EnumFacing arg2, NBTBase arg3)|void
| writeNBT(Capability\<T> arg0, Object arg1, EnumFacing arg2)|NBTBase

---

## WeightedRandom$Item

|Class
|--
|net.minecraft.util.WeightedRandom$Item

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_76292_a|int

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Template

|Class
|--
|net.minecraft.world.gen.structure.template.Template

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_186252_a(String s)|void
| func_186253_b(World arg0, BlockPos arg1, PlacementSettings arg2)|void
| func_186254_a(World arg0, BlockPos arg1, BlockPos arg2, boolean arg3, Block arg4)|void
| func_186256_b(NBTTagCompound n)|void
| func_186257_a(Rotation r)|BlockPos
| func_186258_a(BlockPos arg0, PlacementSettings arg1)|Map\<BlockPos, String>
| func_186259_a()|BlockPos
| func_186260_a(World arg0, BlockPos arg1, PlacementSettings arg2)|void
| func_186261_b()|String
| func_186262_a(PlacementSettings arg0, BlockPos arg1, PlacementSettings arg2, BlockPos arg3)|BlockPos
| func_189552_a(NBTTagCompound n)|NBTTagCompound
| func_189960_a(World arg0, BlockPos arg1, TemplateProcessor arg2, PlacementSettings arg3, int arg4)|void
| func_189961_a(BlockPos arg0, Mirror arg1, Rotation arg2)|BlockPos
| func_189962_a(World arg0, BlockPos arg1, PlacementSettings arg2, int arg3)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PlayerChunkMapEntry

|Class
|--
|net.minecraft.server.management.PlayerChunkMapEntry

---

|Extends
|--

---

|Fields|Type
|--|--
|  watchingPlayers|List\<EntityPlayerMP>

---

|Methods|Return Type
|--|--
| func_187264_a()|ChunkPos
| func_187265_a(int arg0, int arg1, int arg2)|void
| func_187266_f()|Chunk
| func_187267_a(Packet\<?> p)|void
| func_187268_a(boolean b)|boolean
| func_187269_a(Predicate\<EntityPlayerMP> p)|boolean
| func_187270_g()|double
| func_187271_a(double arg0, Predicate\<EntityPlayerMP> arg1)|boolean
| func_187272_b()|boolean
| func_187274_e()|boolean
| func_187275_d(EntityPlayerMP e)|boolean
| func_187276_a(EntityPlayerMP e)|void
| func_187277_b(EntityPlayerMP e)|void
| func_187278_c(EntityPlayerMP e)|void
| func_187279_c()|void
| func_187280_d()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## FunctionObject

|Class
|--
|net.minecraft.command.FunctionObject

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_193528_a()|FunctionObject$Entry[]
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Team$EnumVisible

|Class
|--
|net.minecraft.scoreboard.Team$EnumVisible

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>
|  field_178827_f|int
|  field_178830_e|String

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Team$CollisionRule

|Class
|--
|net.minecraft.scoreboard.Team$CollisionRule

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>
|  field_186693_e|String
|  field_186694_f|int

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## DataSerializer

|Interface
|--
|net.minecraft.network.datasync.DataSerializer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_187159_a(PacketBuffer p)|Object
| func_187160_a(PacketBuffer arg0, Object arg1)|void
| func_187161_a(int i)|DataParameter\<T>
| func_192717_a(Object o)|Object

---

## EntityWeatherEffect

|Class
|--
|net.minecraft.entity.effect.EntityWeatherEffect

---

|Extends
|--
|Entity

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_190534_ay|int
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_98038_p|boolean
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_110124_au()|UUID
| func_130014_f_()|World
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_190530_aW()|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70676_i(float f)|Vec3d
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RecipeItemHelper

|Class
|--
|net.minecraft.client.util.RecipeItemHelper

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_194124_a|Int2IntMap

---

|Methods|Return Type
|--|--
| accountStack(ItemStack arg0, int arg1)|void
| func_194112_a(ItemStack i)|void
| func_194114_b(Recipe arg0, IntList arg1)|int
| func_194116_a(Recipe arg0, IntList arg1)|boolean
| func_194118_a(Recipe arg0, IntList arg1, int arg2)|boolean
| func_194119_a()|void
| func_194120_a(int i)|boolean
| func_194121_a(Recipe arg0, int arg1, IntList arg2)|int
| func_194122_a(int arg0, int arg1)|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MerchantRecipeList

|Class
|--
|net.minecraft.village.MerchantRecipeList

---

|Extends
|--
|ArrayList

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(int arg0, Object arg1)|void
| add(Object o)|boolean
| addAll(int arg0, Collection\<? extends E> arg1)|boolean
| addAll(Collection\<? extends E> c)|boolean
| clear()|void
| clone()|Object
| contains(Object o)|boolean
| containsAll(Collection\<?> c)|boolean
| ensureCapacity(int i)|void
| forEach(Consumer\<? super E> c)|void
| func_151391_a(PacketBuffer p)|void
| func_77201_a(NBTTagCompound n)|void
| func_77202_a()|NBTTagCompound
| func_77203_a(ItemStack arg0, ItemStack arg1, int arg2)|MerchantRecipe
| get(int i)|Object
| indexOf(Object o)|int
| iterator()|Iterator\<E>
| lastIndexOf(Object o)|int
| listIterator(int i)|ListIterator\<E>
| listIterator()|ListIterator\<E>
| parallelStream()|Stream\<E>
| remove(Object o)|boolean
| remove(int i)|Object
| removeAll(Collection\<?> c)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| replaceAll(UnaryOperator\<E> u)|void
| retainAll(Collection\<?> c)|boolean
| set(int arg0, Object arg1)|Object
| size()|int
| sort(Comparator\<? super E> c)|void
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| subList(int arg0, int arg1)|List\<E>
| toArray()|Object[]
| toArray(Object[] o)|Object[]
| trimToSize()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MerchantRecipe

|Class
|--
|net.minecraft.village.MerchantRecipe

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_180320_f()|int
| func_180321_e()|int
| func_180322_j()|boolean
| func_77390_a(NBTTagCompound n)|void
| func_77394_a()|ItemStack
| func_77395_g()|NBTTagCompound
| func_77396_b()|ItemStack
| func_77397_d()|ItemStack
| func_77398_c()|boolean
| func_77399_f()|void
| func_82783_a(int i)|void
| func_82784_g()|boolean
| func_82785_h()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TileEntityCommandBlock$Mode

|Class
|--
|net.minecraft.tileentity.TileEntityCommandBlock$Mode

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityAnimal

|Class
|--
|net.minecraft.entity.passive.EntityAnimal

---

|Extends
|--
|EntityAgeable
|Animals

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_110153_bc|float
|  field_110158_av|int
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_184617_aD|int
|  field_184618_aE|float
|  field_184619_aG|float
|  field_184622_au|EnumHand
|  field_184627_bm|ItemStack
|  field_184628_bn|int
|  field_190534_ay|int
|  field_191988_bg|float
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_70696_bz|EntityLivingBase
|  field_70701_bs|float
|  field_70702_br|float
|  field_70703_bu|boolean
|  field_70704_bt|float
|  field_70714_bg|EntityAITasks
|  field_70715_bh|EntityAITasks
|  field_70718_bc|int
|  field_70720_be|int
|  field_70721_aZ|float
|  field_70725_aQ|int
|  field_70726_aT|float
|  field_70727_aS|float
|  field_70728_aV|int
|  field_70732_aI|float
|  field_70733_aJ|float
|  field_70737_aN|int
|  field_70738_aO|int
|  field_70739_aP|float
|  field_70747_aH|float
|  field_70755_b|EntityLivingBase
|  field_70757_a|int
|  field_70758_at|float
|  field_70759_as|float
|  field_70760_ar|float
|  field_70761_aq|float
|  field_70769_ao|float
|  field_70770_ap|float
|  field_70771_an|int
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_82175_bq|boolean
|  field_98038_p|boolean
|  itemInUseMaxDuration|int
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| curePotionEffects(ItemStack i)|void
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_104002_bU()|boolean
| func_110124_au()|UUID
| func_110138_aP()|float
| func_110139_bj()|float
| func_110140_aT()|AbstractAttributeMap
| func_110142_aN()|CombatTracker
| func_110143_aJ()|float
| func_110144_aD()|EntityLivingBase
| func_110145_l(Entity e)|void
| func_110148_a(Attribute a)|AttributeInstance
| func_110149_m(float f)|void
| func_110160_i(boolean arg0, boolean arg1)|void
| func_110162_b(Entity arg0, boolean arg1)|void
| func_110163_bv()|void
| func_110166_bE()|Entity
| func_110167_bD()|boolean
| func_110173_bK()|boolean
| func_110174_bM()|float
| func_110175_bO()|boolean
| func_110177_bN()|void
| func_110195_a(int i)|void
| func_130011_c(Entity e)|void
| func_130014_f_()|World
| func_142013_aG()|int
| func_142015_aE()|int
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_146082_f(EntityPlayer e)|void
| func_152111_bt()|void
| func_152112_bu()|void
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_175446_cd()|boolean
| func_175449_a(BlockPos arg0, int arg1)|void
| func_175501_a(int arg0, boolean arg1)|void
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180482_a(DifficultyInstance arg0, EntityLivingData arg1)|EntityLivingData
| func_180484_a(BlockPos b)|float
| func_180485_d(BlockPos b)|boolean
| func_180486_cf()|BlockPos
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_184582_a(EntityEquipmentSlot e)|ItemStack
| func_184583_d(DamageSource d)|boolean
| func_184585_cz()|boolean
| func_184586_b(EnumHand e)|ItemStack
| func_184587_cr()|boolean
| func_184589_d(Potion p)|void
| func_184591_cq()|EnumHandSide
| func_184592_cb()|ItemStack
| func_184595_k(double arg0, double arg1, double arg2)|boolean
| func_184596_c(Potion p)|PotionEffect
| func_184597_cx()|void
| func_184598_c(EnumHand e)|void
| func_184599_cB()|int
| func_184600_cs()|EnumHand
| func_184602_cy()|void
| func_184603_cC()|boolean
| func_184605_cv()|int
| func_184607_cu()|ItemStack
| func_184609_a(EnumHand e)|void
| func_184611_a(EnumHand arg0, ItemStack arg1)|void
| func_184612_cw()|int
| func_184613_cA()|boolean
| func_184614_ca()|ItemStack
| func_184638_cS()|boolean
| func_184641_n(boolean b)|void
| func_184642_a(EntityEquipmentSlot arg0, float arg1)|void
| func_184643_a(PathNodeType p)|float
| func_184644_a(PathNodeType arg0, float arg1)|void
| func_184645_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184646_p(float f)|void
| func_184649_cE()|int
| func_184652_a(EntityPlayer e)|boolean
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_189748_bU()|DamageSource
| func_190530_aW()|boolean
| func_190630_a(EntityEquipmentSlot e)|boolean
| func_190631_cK()|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_191986_a(float arg0, float arg1, float arg2)|void
| func_191987_a(BlockPos arg0, boolean arg1)|void
| func_191989_p(float f)|void
| func_191993_do()|EntityPlayerMP
| func_193076_bZ()|Map\<Potion, PotionEffect>
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70058_J()|boolean
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70601_bi()|boolean
| func_70603_bj()|float
| func_70604_c(EntityLivingBase e)|void
| func_70605_aq()|EntityMoveHelper
| func_70606_j(float f)|void
| func_70608_bn()|boolean
| func_70613_aW()|boolean
| func_70615_aA()|void
| func_70617_f_()|boolean
| func_70624_b(EntityLivingBase e)|void
| func_70625_a(Entity arg0, float arg1, float arg2)|void
| func_70627_aG()|int
| func_70631_g_()|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70635_at()|EntitySenses
| func_70636_d()|void
| func_70637_d(boolean b)|void
| func_70638_az()|EntityLivingBase
| func_70641_bl()|int
| func_70642_aH()|void
| func_70643_av()|EntityLivingBase
| func_70644_a(Potion p)|boolean
| func_70645_a(DamageSource d)|void
| func_70646_bf()|int
| func_70648_aU()|boolean
| func_70651_bq()|Collection\<PotionEffect>
| func_70652_k(Entity e)|boolean
| func_70653_a(Entity arg0, float arg1, double arg2, double arg3)|void
| func_70654_ax()|int
| func_70656_aK()|void
| func_70657_f(float f)|void
| func_70658_aO()|int
| func_70659_e(float f)|void
| func_70660_b(Potion p)|PotionEffect
| func_70661_as()|PathNavigate
| func_70662_br()|boolean
| func_70668_bt()|EnumCreatureAttribute
| func_70669_a(ItemStack i)|void
| func_70671_ap()|EntityLookHelper
| func_70674_bp()|void
| func_70676_i(float f)|Vec3d
| func_70678_g(float f)|float
| func_70681_au()|Random
| func_70683_ar()|EntityJumpHelper
| func_70685_l(Entity e)|boolean
| func_70686_a(Class\<? extends net.minecraft.entity.EntityLivingBase> c)|boolean
| func_70687_e(PotionEffect p)|boolean
| func_70689_ay()|float
| func_70690_d(PotionEffect p)|void
| func_70691_i(float f)|void
| func_70781_l()|boolean
| func_70873_a(int i)|void
| func_70874_b()|int
| func_70875_t()|void
| func_70877_b(ItemStack i)|boolean
| func_70878_b(EntityAnimal e)|boolean
| func_70880_s()|boolean
| func_71001_a(Entity arg0, int arg1)|void
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_82171_bF()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_85034_r(int i)|void
| func_85035_bI()|int
| func_90011_a(EntityAgeable e)|EntityAgeable
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_94060_bK()|EntityLivingBase
| func_94061_f(boolean b)|void
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| func_98052_bS()|boolean
| func_98053_h(boolean b)|void
| func_98054_a(boolean b)|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderFaceForward(EntityPlayer e)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## InventoryChangedListener

|Interface
|--
|net.minecraft.inventory.IInventoryChangedListener

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_76316_a(Inventory i)|void

---

## JumpingMount

|Interface
|--
|net.minecraft.entity.IJumpingMount

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_110206_u(int i)|void
| func_184775_b(int i)|void
| func_184776_b()|boolean
| func_184777_r_()|void

---

## EntityAgeable

|Class
|--
|net.minecraft.entity.EntityAgeable

---

|Extends
|--
|EntityCreature

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_110153_bc|float
|  field_110158_av|int
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_184617_aD|int
|  field_184618_aE|float
|  field_184619_aG|float
|  field_184622_au|EnumHand
|  field_184627_bm|ItemStack
|  field_184628_bn|int
|  field_190534_ay|int
|  field_191988_bg|float
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_70696_bz|EntityLivingBase
|  field_70701_bs|float
|  field_70702_br|float
|  field_70703_bu|boolean
|  field_70704_bt|float
|  field_70714_bg|EntityAITasks
|  field_70715_bh|EntityAITasks
|  field_70718_bc|int
|  field_70720_be|int
|  field_70721_aZ|float
|  field_70725_aQ|int
|  field_70726_aT|float
|  field_70727_aS|float
|  field_70728_aV|int
|  field_70732_aI|float
|  field_70733_aJ|float
|  field_70737_aN|int
|  field_70738_aO|int
|  field_70739_aP|float
|  field_70747_aH|float
|  field_70755_b|EntityLivingBase
|  field_70757_a|int
|  field_70758_at|float
|  field_70759_as|float
|  field_70760_ar|float
|  field_70761_aq|float
|  field_70769_ao|float
|  field_70770_ap|float
|  field_70771_an|int
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_82175_bq|boolean
|  field_98038_p|boolean
|  itemInUseMaxDuration|int
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| curePotionEffects(ItemStack i)|void
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_104002_bU()|boolean
| func_110124_au()|UUID
| func_110138_aP()|float
| func_110139_bj()|float
| func_110140_aT()|AbstractAttributeMap
| func_110142_aN()|CombatTracker
| func_110143_aJ()|float
| func_110144_aD()|EntityLivingBase
| func_110145_l(Entity e)|void
| func_110148_a(Attribute a)|AttributeInstance
| func_110149_m(float f)|void
| func_110160_i(boolean arg0, boolean arg1)|void
| func_110162_b(Entity arg0, boolean arg1)|void
| func_110163_bv()|void
| func_110166_bE()|Entity
| func_110167_bD()|boolean
| func_110173_bK()|boolean
| func_110174_bM()|float
| func_110175_bO()|boolean
| func_110177_bN()|void
| func_110195_a(int i)|void
| func_130011_c(Entity e)|void
| func_130014_f_()|World
| func_142013_aG()|int
| func_142015_aE()|int
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_152111_bt()|void
| func_152112_bu()|void
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_175446_cd()|boolean
| func_175449_a(BlockPos arg0, int arg1)|void
| func_175501_a(int arg0, boolean arg1)|void
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180482_a(DifficultyInstance arg0, EntityLivingData arg1)|EntityLivingData
| func_180484_a(BlockPos b)|float
| func_180485_d(BlockPos b)|boolean
| func_180486_cf()|BlockPos
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_184582_a(EntityEquipmentSlot e)|ItemStack
| func_184583_d(DamageSource d)|boolean
| func_184585_cz()|boolean
| func_184586_b(EnumHand e)|ItemStack
| func_184587_cr()|boolean
| func_184589_d(Potion p)|void
| func_184591_cq()|EnumHandSide
| func_184592_cb()|ItemStack
| func_184595_k(double arg0, double arg1, double arg2)|boolean
| func_184596_c(Potion p)|PotionEffect
| func_184597_cx()|void
| func_184598_c(EnumHand e)|void
| func_184599_cB()|int
| func_184600_cs()|EnumHand
| func_184602_cy()|void
| func_184603_cC()|boolean
| func_184605_cv()|int
| func_184607_cu()|ItemStack
| func_184609_a(EnumHand e)|void
| func_184611_a(EnumHand arg0, ItemStack arg1)|void
| func_184612_cw()|int
| func_184613_cA()|boolean
| func_184614_ca()|ItemStack
| func_184638_cS()|boolean
| func_184641_n(boolean b)|void
| func_184642_a(EntityEquipmentSlot arg0, float arg1)|void
| func_184643_a(PathNodeType p)|float
| func_184644_a(PathNodeType arg0, float arg1)|void
| func_184645_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184646_p(float f)|void
| func_184649_cE()|int
| func_184652_a(EntityPlayer e)|boolean
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_189748_bU()|DamageSource
| func_190530_aW()|boolean
| func_190630_a(EntityEquipmentSlot e)|boolean
| func_190631_cK()|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_191986_a(float arg0, float arg1, float arg2)|void
| func_191987_a(BlockPos arg0, boolean arg1)|void
| func_191989_p(float f)|void
| func_193076_bZ()|Map\<Potion, PotionEffect>
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70058_J()|boolean
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70601_bi()|boolean
| func_70603_bj()|float
| func_70604_c(EntityLivingBase e)|void
| func_70605_aq()|EntityMoveHelper
| func_70606_j(float f)|void
| func_70608_bn()|boolean
| func_70613_aW()|boolean
| func_70615_aA()|void
| func_70617_f_()|boolean
| func_70624_b(EntityLivingBase e)|void
| func_70625_a(Entity arg0, float arg1, float arg2)|void
| func_70627_aG()|int
| func_70631_g_()|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70635_at()|EntitySenses
| func_70636_d()|void
| func_70637_d(boolean b)|void
| func_70638_az()|EntityLivingBase
| func_70641_bl()|int
| func_70642_aH()|void
| func_70643_av()|EntityLivingBase
| func_70644_a(Potion p)|boolean
| func_70645_a(DamageSource d)|void
| func_70646_bf()|int
| func_70648_aU()|boolean
| func_70651_bq()|Collection\<PotionEffect>
| func_70652_k(Entity e)|boolean
| func_70653_a(Entity arg0, float arg1, double arg2, double arg3)|void
| func_70654_ax()|int
| func_70656_aK()|void
| func_70657_f(float f)|void
| func_70658_aO()|int
| func_70659_e(float f)|void
| func_70660_b(Potion p)|PotionEffect
| func_70661_as()|PathNavigate
| func_70662_br()|boolean
| func_70668_bt()|EnumCreatureAttribute
| func_70669_a(ItemStack i)|void
| func_70671_ap()|EntityLookHelper
| func_70674_bp()|void
| func_70676_i(float f)|Vec3d
| func_70678_g(float f)|float
| func_70681_au()|Random
| func_70683_ar()|EntityJumpHelper
| func_70685_l(Entity e)|boolean
| func_70686_a(Class\<? extends net.minecraft.entity.EntityLivingBase> c)|boolean
| func_70687_e(PotionEffect p)|boolean
| func_70689_ay()|float
| func_70690_d(PotionEffect p)|void
| func_70691_i(float f)|void
| func_70781_l()|boolean
| func_70873_a(int i)|void
| func_70874_b()|int
| func_71001_a(Entity arg0, int arg1)|void
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_82171_bF()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_85034_r(int i)|void
| func_85035_bI()|int
| func_90011_a(EntityAgeable e)|EntityAgeable
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_94060_bK()|EntityLivingBase
| func_94061_f(boolean b)|void
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| func_98052_bS()|boolean
| func_98053_h(boolean b)|void
| func_98054_a(boolean b)|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderFaceForward(EntityPlayer e)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TileEntityStructure$Mode

|Class
|--
|net.minecraft.tileentity.TileEntityStructure$Mode

---

|Extends
|--
|Enum
|StringSerializable

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_176610_l()|String
| func_185110_a()|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## InventoryBasic

|Class
|--
|net.minecraft.inventory.InventoryBasic

---

|Extends
|--
|Inventory

---

|Methods|Return Type
|--|--
| func_110132_b(InventoryChangedListener i)|void
| func_110133_a(String s)|void
| func_110134_a(InventoryChangedListener i)|void
| func_145748_c_()|TextComponent
| func_145818_k_()|boolean
| func_174885_b(int arg0, int arg1)|void
| func_174886_c(EntityPlayer e)|void
| func_174887_a_(int i)|int
| func_174888_l()|void
| func_174889_b(EntityPlayer e)|void
| func_174890_g()|int
| func_174894_a(ItemStack i)|ItemStack
| func_191420_l()|boolean
| func_70005_c_()|String
| func_70296_d()|void
| func_70297_j_()|int
| func_70298_a(int arg0, int arg1)|ItemStack
| func_70299_a(int arg0, ItemStack arg1)|void
| func_70300_a(EntityPlayer e)|boolean
| func_70301_a(int i)|ItemStack
| func_70302_i_()|int
| func_70304_b(int i)|ItemStack
| func_94041_b(int arg0, ItemStack arg1)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TileEntityEnderChest

|Class
|--
|net.minecraft.tileentity.TileEntityEnderChest

---

|Extends
|--
|TileEntity
|Tickable

---

|Fields|Type
|--|--
|  field_145972_a|float
|  field_145973_j|int
|  field_145975_i|float
|  renderBoundingBox|AxisAlignedBB
|  tileData|NBTTagCompound

---

|Methods|Return Type
|--|--
| canRenderBreaking()|boolean
| deserializeNBT(NBTBase n)|void
| deserializeNBT(NBTTagCompound n)|void
| func_145748_c_()|TextComponent
| func_145828_a(CrashReportCategory c)|void
| func_145829_t()|void
| func_145830_o()|boolean
| func_145831_w()|World
| func_145832_p()|int
| func_145833_n()|double
| func_145834_a(World w)|void
| func_145835_a(double arg0, double arg1, double arg2)|double
| func_145836_u()|void
| func_145837_r()|boolean
| func_145838_q()|Block
| func_145839_a(NBTTagCompound n)|void
| func_145842_c(int arg0, int arg1)|boolean
| func_145843_s()|void
| func_145969_a()|void
| func_145970_b()|void
| func_145971_a(EntityPlayer e)|boolean
| func_174877_v()|BlockPos
| func_174878_a(BlockPos b)|void
| func_183000_F()|boolean
| func_189515_b(NBTTagCompound n)|NBTTagCompound
| func_189517_E_()|NBTTagCompound
| func_189518_D_()|SPacketUpdateTileEntity
| func_189667_a(Rotation r)|void
| func_189668_a(Mirror m)|void
| func_70296_d()|void
| func_73660_a()|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| handleUpdateTag(NBTTagCompound n)|void
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| hasFastRenderer()|boolean
| onChunkUnload()|void
| onDataPacket(NetworkManager arg0, SPacketUpdateTileEntity arg1)|void
| onLoad()|void
| restrictNBTCopy()|boolean
| serializeNBT()|NBTBase
| serializeNBT()|NBTTagCompound
| shouldRefresh(World arg0, BlockPos arg1, BlockState arg2, BlockState arg3)|boolean
| shouldRenderInPass(int i)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AppleCoreFoodStats

|Interface
|--
|squeek.applecore.asm.util.IAppleCoreFoodStats

---

|Extends
|--

---

|Fields|Type
|--|--
|  exhaustion|float
|  foodTimer|int
|  player|EntityPlayer
|  starveTimer|int

---

|Methods|Return Type
|--|--
| setPrevFoodLevel(int i)|void
| setSaturation(float f)|void

---

## ItemFood

|Class
|--
|net.minecraft.item.ItemFood

---

|Extends
|--
|Item

---

|Fields|Type
|--|--
|  creativeTabs|CreativeTabs[]
|  delegate|RegistryDelegate\<T>
|  field_77851_ca|PotionEffect
|  field_77852_bZ|boolean
|  field_77853_b|int
|  field_77854_c|float
|  field_77855_a|int
|  field_77856_bY|boolean
|  field_77858_cd|float
|  registryName|ResourceLocation
|  registryType|Class\<T>
|  repairable|boolean
|  tileEntityItemStackRenderer|TileEntityItemStackRenderer

---

|Methods|Return Type
|--|--
| canApplyAtEnchantingTable(ItemStack arg0, Enchantment arg1)|boolean
| canContinueUsing(ItemStack arg0, ItemStack arg1)|boolean
| canDestroyBlockInCreative(World arg0, BlockPos arg1, ItemStack arg2, EntityPlayer arg3)|boolean
| canDisableShield(ItemStack arg0, ItemStack arg1, EntityLivingBase arg2, EntityLivingBase arg3)|boolean
| canHarvestBlock(BlockState arg0, ItemStack arg1)|boolean
| createEntity(World arg0, Entity arg1, ItemStack arg2)|Entity
| doesSneakBypassUse(ItemStack arg0, BlockAccess arg1, BlockPos arg2, EntityPlayer arg3)|boolean
| func_111205_h(EntityEquipmentSlot e)|Multimap\<String, AttributeModifier>
| func_111207_a(ItemStack arg0, EntityPlayer arg1, EntityLivingBase arg2, EnumHand arg3)|boolean
| func_150893_a(ItemStack arg0, BlockState arg1)|float
| func_150895_a(CreativeTabs arg0, NonNullList\<ItemStack> arg1)|void
| func_150897_b(BlockState b)|boolean
| func_150905_g(ItemStack i)|int
| func_150906_h(ItemStack i)|float
| func_179215_a(NBTTagCompound n)|boolean
| func_179218_a(ItemStack arg0, World arg1, BlockState arg2, BlockPos arg3, EntityLivingBase arg4)|boolean
| func_180614_a(EntityPlayer arg0, World arg1, BlockPos arg2, EnumHand arg3, EnumFacing arg4, float arg5, float arg6, float arg7)|EnumActionResult
| func_185040_i()|boolean
| func_185043_a(ResourceLocation arg0, ItemPropertyGetter arg1)|void
| func_185045_a(ResourceLocation r)|ItemPropertyGetter
| func_185070_a(PotionEffect arg0, float arg1)|ItemFood
| func_190903_i()|ItemStack
| func_194125_a(CreativeTabs c)|boolean
| func_77612_l()|int
| func_77613_e(ItemStack i)|EnumRarity
| func_77614_k()|boolean
| func_77615_a(ItemStack arg0, World arg1, EntityLivingBase arg2, int arg3)|void
| func_77616_k(ItemStack i)|boolean
| func_77619_b()|int
| func_77622_d(ItemStack arg0, World arg1, EntityPlayer arg2)|void
| func_77624_a(ItemStack arg0, World arg1, List\<String> arg2, TooltipFlag arg3)|void
| func_77625_d(int i)|Item
| func_77626_a(ItemStack i)|int
| func_77627_a(boolean b)|Item
| func_77629_n_()|boolean
| func_77634_r()|boolean
| func_77636_d(ItemStack i)|boolean
| func_77637_a(CreativeTabs c)|Item
| func_77639_j()|int
| func_77640_w()|CreativeTabs
| func_77642_a(Item i)|Item
| func_77643_m_()|boolean
| func_77644_a(ItemStack arg0, EntityLivingBase arg1, EntityLivingBase arg2)|boolean
| func_77645_m()|boolean
| func_77647_b(int i)|int
| func_77651_p()|boolean
| func_77653_i(ItemStack i)|String
| func_77654_b(ItemStack arg0, World arg1, EntityLivingBase arg2)|ItemStack
| func_77655_b(String s)|Item
| func_77656_e(int i)|Item
| func_77657_g(ItemStack i)|String
| func_77658_a()|String
| func_77659_a(World arg0, EntityPlayer arg1, EnumHand arg2)|ActionResult\<ItemStack>
| func_77661_b(ItemStack i)|EnumAction
| func_77662_d()|boolean
| func_77663_a(ItemStack arg0, World arg1, Entity arg2, int arg3, boolean arg4)|void
| func_77664_n()|Item
| func_77667_c(ItemStack i)|String
| func_77668_q()|Item
| func_77845_h()|boolean
| func_77848_i()|ItemFood
| func_82788_x()|boolean
| func_82789_a(ItemStack arg0, ItemStack arg1)|boolean
| getAnimationParameters(ItemStack arg0, World arg1, EntityLivingBase arg2)|ImmutableMap\<String, TimeValue>
| getArmorModel(EntityLivingBase arg0, ItemStack arg1, EntityEquipmentSlot arg2, ModelBiped arg3)|ModelBiped
| getArmorTexture(ItemStack arg0, Entity arg1, EntityEquipmentSlot arg2, String arg3)|String
| getAttributeModifiers(EntityEquipmentSlot arg0, ItemStack arg1)|Multimap\<String, AttributeModifier>
| getContainerItem(ItemStack i)|ItemStack
| getCreatorModId(ItemStack i)|String
| getDamage(ItemStack i)|int
| getDurabilityForDisplay(ItemStack i)|double
| getEntityLifespan(ItemStack arg0, World arg1)|int
| getEquipmentSlot(ItemStack i)|EntityEquipmentSlot
| getFontRenderer(ItemStack i)|FontRenderer
| getForgeRarity(ItemStack i)|Rarity
| getHarvestLevel(ItemStack arg0, String arg1, EntityPlayer arg2, BlockState arg3)|int
| getHighlightTip(ItemStack arg0, String arg1)|String
| getHorseArmorTexture(EntityLiving arg0, ItemStack arg1)|String
| getHorseArmorType(ItemStack i)|HorseArmorType
| getItemBurnTime(ItemStack i)|int
| getItemEnchantability(ItemStack i)|int
| getItemStackLimit(ItemStack i)|int
| getMaxDamage(ItemStack i)|int
| getMetadata(ItemStack i)|int
| getNBTShareTag(ItemStack i)|NBTTagCompound
| getRGBDurabilityForDisplay(ItemStack i)|int
| getSmeltingExperience(ItemStack i)|float
| getToolClasses(ItemStack i)|Set\<String>
| getXpRepairRatio(ItemStack i)|float
| hasContainerItem(ItemStack i)|boolean
| hasCustomEntity(ItemStack i)|boolean
| initCapabilities(ItemStack arg0, NBTTagCompound arg1)|CapabilityProvider
| isBeaconPayment(ItemStack i)|boolean
| isBookEnchantable(ItemStack arg0, ItemStack arg1)|boolean
| isDamaged(ItemStack i)|boolean
| isShield(ItemStack arg0, EntityLivingBase arg1)|boolean
| isValidArmor(ItemStack arg0, EntityEquipmentSlot arg1, Entity arg2)|boolean
| onArmorTick(World arg0, EntityPlayer arg1, ItemStack arg2)|void
| onBlockStartBreak(ItemStack arg0, BlockPos arg1, EntityPlayer arg2)|boolean
| onDroppedByPlayer(ItemStack arg0, EntityPlayer arg1)|boolean
| onEntityItemUpdate(EntityItem e)|boolean
| onEntitySwing(EntityLivingBase arg0, ItemStack arg1)|boolean
| onHorseArmorTick(World arg0, EntityLiving arg1, ItemStack arg2)|void
| onItemUseFirst(EntityPlayer arg0, World arg1, BlockPos arg2, EnumFacing arg3, float arg4, float arg5, float arg6, EnumHand arg7)|EnumActionResult
| onLeftClickEntity(ItemStack arg0, EntityPlayer arg1, Entity arg2)|boolean
| onUsingTick(ItemStack arg0, EntityLivingBase arg1, int arg2)|void
| readNBTShareTag(ItemStack arg0, NBTTagCompound arg1)|void
| renderHelmetOverlay(ItemStack arg0, EntityPlayer arg1, ScaledResolution arg2, float arg3)|void
| setDamage(ItemStack arg0, int arg1)|void
| setHarvestLevel(String arg0, int arg1)|void
| setNoRepair()|Item
| shouldCauseBlockBreakReset(ItemStack arg0, ItemStack arg1)|boolean
| shouldCauseReequipAnimation(ItemStack arg0, ItemStack arg1, boolean arg2)|boolean
| showDurabilityBar(ItemStack i)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumPacketDirection

|Class
|--
|net.minecraft.network.EnumPacketDirection

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EnumConnectionState

|Class
|--
|net.minecraft.network.EnumConnectionState

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_150759_c()|int
| func_179244_a(EnumPacketDirection arg0, int arg1)|Packet\<?>
| func_179246_a(EnumPacketDirection arg0, Packet\<?> arg1)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityHanging

|Class
|--
|net.minecraft.entity.EntityHanging

---

|Extends
|--
|Entity

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_174860_b|EnumFacing
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_190534_ay|int
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_98038_p|boolean
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_110124_au()|UUID
| func_110128_b(Entity e)|void
| func_130014_f_()|World
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_174857_n()|BlockPos
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_184523_o()|void
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_190530_aW()|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70518_d()|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70676_i(float f)|Vec3d
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_82329_d()|int
| func_82330_g()|int
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityAITasks$EntityAITaskEntry

|Class
|--
|net.minecraft.entity.ai.EntityAITasks$EntityAITaskEntry

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_188524_c|boolean
|  field_75731_b|int
|  field_75733_a|EntityAIBase

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityAIBase

|Class
|--
|net.minecraft.entity.ai.EntityAIBase

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_75246_d()|void
| func_75247_h()|int
| func_75248_a(int i)|void
| func_75249_e()|void
| func_75250_a()|boolean
| func_75251_c()|void
| func_75252_g()|boolean
| func_75253_b()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityMoveHelper$Action

|Class
|--
|net.minecraft.entity.ai.EntityMoveHelper$Action

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Path

|Class
|--
|net.minecraft.pathfinding.Path

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_186309_a(int arg0, PathPoint arg1)|void
| func_186310_f()|Vec3d
| func_189964_i()|PathPoint
| func_189965_h()|PathPoint[]
| func_189966_g()|PathPoint[]
| func_75870_c()|PathPoint
| func_75871_b(int i)|void
| func_75872_c(int i)|void
| func_75873_e()|int
| func_75874_d()|int
| func_75875_a()|void
| func_75876_a(Path p)|boolean
| func_75877_a(int i)|PathPoint
| func_75878_a(Entity e)|Vec3d
| func_75879_b()|boolean
| func_75881_a(Entity arg0, int arg1)|Vec3d
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NodeProcessor

|Class
|--
|net.minecraft.pathfinding.NodeProcessor

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_176163_a()|void
| func_186315_a(BlockAccess arg0, EntityLiving arg1)|void
| func_186316_c(boolean b)|void
| func_186317_a(boolean b)|void
| func_186318_b()|PathPoint
| func_186319_a(BlockAccess arg0, int arg1, int arg2, int arg3, EntityLiving arg4, int arg5, int arg6, int arg7, boolean arg8, boolean arg9)|PathNodeType
| func_186320_a(PathPoint[] arg0, PathPoint arg1, PathPoint arg2, float arg3)|int
| func_186321_b(boolean b)|void
| func_186322_e()|boolean
| func_186323_c()|boolean
| func_186324_d()|boolean
| func_186325_a(double arg0, double arg1, double arg2)|PathPoint
| func_186330_a(BlockAccess arg0, int arg1, int arg2, int arg3)|PathNodeType
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ModelBox

|Class
|--
|net.minecraft.client.model.ModelBox

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_78246_f|float
|  field_78247_g|String
|  field_78248_d|float
|  field_78249_e|float
|  field_78250_b|float
|  field_78251_c|float
|  field_78252_a|float
|  field_78254_i|TexturedQuad[]

---

|Methods|Return Type
|--|--
| func_178780_a(BufferBuilder arg0, float arg1)|void
| func_78244_a(String s)|ModelBox
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ModelUpdater

|Class
|--
|net.optifine.entity.model.anim.ModelUpdater

---

|Extends
|--

---

|Methods|Return Type
|--|--
| initialize(ModelResolver m)|boolean
| update()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Command

|Interface
|--
|net.minecraft.command.ICommand

---

|Extends
|--
|Comparable

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| func_184881_a(MinecraftServer arg0, CommandSender arg1, String[] arg2)|void
| func_184882_a(MinecraftServer arg0, CommandSender arg1)|boolean
| func_184883_a(MinecraftServer arg0, CommandSender arg1, String[] arg2, BlockPos arg3)|List\<String>
| func_71514_a()|List\<String>
| func_71517_b()|String
| func_71518_a(CommandSender c)|String
| func_82358_a(String[] arg0, int arg1)|boolean

---

## Event$Result

|Class
|--
|net.minecraftforge.fml.common.eventhandler.Event$Result

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RewardType$GuiProvider

|Interface
|--
|com.feed_the_beast.ftbquests.quest.reward.RewardType$GuiProvider

---

|Extends
|--

---

|Methods|Return Type
|--|--
| openCreationGui(OpenableGui arg0, Quest arg1, Consumer\<Reward> arg2)|void

---

## RewardType$Provider

|Interface
|--
|com.feed_the_beast.ftbquests.quest.reward.RewardType$Provider

---

|Extends
|--

---

|Methods|Return Type
|--|--
| create(Quest q)|Reward

---

## TaskType$GuiProvider

|Interface
|--
|com.feed_the_beast.ftbquests.quest.task.TaskType$GuiProvider

---

|Extends
|--

---

|Methods|Return Type
|--|--
| openCreationGui(OpenableGui arg0, Quest arg1, Consumer\<Task> arg2)|void

---

## TaskType$Provider

|Interface
|--
|com.feed_the_beast.ftbquests.quest.task.TaskType$Provider

---

|Extends
|--

---

|Methods|Return Type
|--|--
| create(Quest q)|Task

---

## TileWithTeam

|Class
|--
|com.feed_the_beast.ftbquests.tile.TileWithTeam

---

|Extends
|--
|TileBase

---

|Fields|Type
|--|--
|  blockState|BlockState
|  brokenByCreative|boolean
|  dimPos|BlockDimPos
|  indestructible|boolean
|  renderBoundingBox|AxisAlignedBB
|  team|String
|  tileData|NBTTagCompound

---

|Methods|Return Type
|--|--
| canRenderBreaking()|boolean
| checkIfDirty()|void
| createState(BlockState b)|BlockState
| deserializeNBT(NBTBase n)|void
| deserializeNBT(NBTTagCompound n)|void
| func_145748_c_()|TextComponent
| func_145818_k_()|boolean
| func_145828_a(CrashReportCategory c)|void
| func_145829_t()|void
| func_145830_o()|boolean
| func_145831_w()|World
| func_145832_p()|int
| func_145833_n()|double
| func_145834_a(World w)|void
| func_145835_a(double arg0, double arg1, double arg2)|double
| func_145836_u()|void
| func_145837_r()|boolean
| func_145838_q()|Block
| func_145839_a(NBTTagCompound n)|void
| func_145842_c(int arg0, int arg1)|boolean
| func_145843_s()|void
| func_174877_v()|BlockPos
| func_174878_a(BlockPos b)|void
| func_183000_F()|boolean
| func_189515_b(NBTTagCompound n)|NBTTagCompound
| func_189517_E_()|NBTTagCompound
| func_189518_D_()|SPacketUpdateTileEntity
| func_189667_a(Rotation r)|void
| func_189668_a(Mirror m)|void
| func_70005_c_()|String
| func_70296_d()|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| handleUpdateTag(NBTTagCompound n)|void
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| hasFastRenderer()|boolean
| isOwner(EntityPlayer e)|boolean
| notifyNeighbors()|void
| onChunkUnload()|void
| onContentsChanged(boolean b)|void
| onDataPacket(NetworkManager arg0, SPacketUpdateTileEntity arg1)|void
| onLoad()|void
| onUpdatePacket(EnumSaveType e)|void
| playSound(SoundEvent arg0, SoundCategory arg1, float arg2, float arg3)|void
| readFromItem(ItemStack i)|void
| restrictNBTCopy()|boolean
| serializeNBT()|NBTBase
| serializeNBT()|NBTTagCompound
| setIDFromPlacer(EntityLivingBase e)|void
| shouldRefresh(World arg0, BlockPos arg1, BlockState arg2, BlockState arg3)|boolean
| shouldRenderInPass(int i)|boolean
| updateComparator()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeToItem(ItemStack i)|void
| writeToPickBlock(ItemStack i)|void

---

## ConfigCallback

|Interface
|--
|com.feed_the_beast.ftblib.lib.config.IConfigCallback

---

|Extends
|--

---

|Methods|Return Type
|--|--
| onConfigSaved(ConfigGroup arg0, CommandSender arg1)|void

---

## TaskScreen

|Interface
|--
|com.feed_the_beast.ftbquests.tile.ITaskScreen

---

|Extends
|--
|Screen

---

|Fields|Type
|--|--
|  offsetX|int
|  offsetY|int
|  offsetZ|int
|  paint|BlockState
|  screen|TileTaskScreenCore

---

|Methods|Return Type
|--|--
| paint(BlockState arg0, EnumFacing arg1, boolean arg2)|void

---

## EnumSaveType

|Class
|--
|com.feed_the_beast.ftblib.lib.tile.EnumSaveType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>
|  full|boolean
|  item|boolean
|  save|boolean

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TileBase

|Class
|--
|com.feed_the_beast.ftblib.lib.tile.TileBase

---

|Extends
|--
|TileEntity
|WorldNameable
|ChangeCallback

---

|Fields|Type
|--|--
|  blockState|BlockState
|  brokenByCreative|boolean
|  dimPos|BlockDimPos
|  renderBoundingBox|AxisAlignedBB
|  tileData|NBTTagCompound

---

|Methods|Return Type
|--|--
| canRenderBreaking()|boolean
| checkIfDirty()|void
| createState(BlockState b)|BlockState
| deserializeNBT(NBTBase n)|void
| deserializeNBT(NBTTagCompound n)|void
| func_145748_c_()|TextComponent
| func_145818_k_()|boolean
| func_145828_a(CrashReportCategory c)|void
| func_145829_t()|void
| func_145830_o()|boolean
| func_145831_w()|World
| func_145832_p()|int
| func_145833_n()|double
| func_145834_a(World w)|void
| func_145835_a(double arg0, double arg1, double arg2)|double
| func_145836_u()|void
| func_145837_r()|boolean
| func_145838_q()|Block
| func_145839_a(NBTTagCompound n)|void
| func_145842_c(int arg0, int arg1)|boolean
| func_145843_s()|void
| func_174877_v()|BlockPos
| func_174878_a(BlockPos b)|void
| func_183000_F()|boolean
| func_189515_b(NBTTagCompound n)|NBTTagCompound
| func_189517_E_()|NBTTagCompound
| func_189518_D_()|SPacketUpdateTileEntity
| func_189667_a(Rotation r)|void
| func_189668_a(Mirror m)|void
| func_70005_c_()|String
| func_70296_d()|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| handleUpdateTag(NBTTagCompound n)|void
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| hasFastRenderer()|boolean
| notifyNeighbors()|void
| onChunkUnload()|void
| onContentsChanged(boolean b)|void
| onDataPacket(NetworkManager arg0, SPacketUpdateTileEntity arg1)|void
| onLoad()|void
| onUpdatePacket(EnumSaveType e)|void
| playSound(SoundEvent arg0, SoundCategory arg1, float arg2, float arg3)|void
| readFromItem(ItemStack i)|void
| restrictNBTCopy()|boolean
| serializeNBT()|NBTBase
| serializeNBT()|NBTTagCompound
| shouldRefresh(World arg0, BlockPos arg1, BlockState arg2, BlockState arg3)|boolean
| shouldRenderInPass(int i)|boolean
| updateComparator()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void
| writeToItem(ItemStack i)|void
| writeToPickBlock(ItemStack i)|void

---

## DisplayInfo

|Class
|--
|net.minecraft.advancements.DisplayInfo

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_192290_a(PacketBuffer p)|void
| func_192291_d()|FrameType
| func_192292_a(float arg0, float arg1)|void
| func_192293_c()|ResourceLocation
| func_192296_f()|float
| func_192297_a()|TextComponent
| func_192298_b()|ItemStack
| func_192299_e()|float
| func_193220_i()|boolean
| func_193222_b()|TextComponent
| func_193223_h()|boolean
| func_193224_j()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AdvancementRewards

|Class
|--
|net.minecraft.advancements.AdvancementRewards

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_192113_a(EntityPlayerMP e)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Criterion

|Class
|--
|net.minecraft.advancements.Criterion

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_192140_a(PacketBuffer p)|void
| func_192143_a()|CriterionInstance
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Advancement$Builder

|Class
|--
|net.minecraft.advancements.Advancement$Builder

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_192056_a(ResourceLocation r)|Advancement
| func_192057_a(PacketBuffer p)|void
| func_192058_a(Function\<ResourceLocation, Advancement> f)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ClickEvent

|Class
|--
|net.minecraft.util.text.event.ClickEvent

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_150668_b()|String
| func_150669_a()|ClickEvent$Action
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## HoverEvent

|Class
|--
|net.minecraft.util.text.event.HoverEvent

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_150701_a()|HoverEvent$Action
| func_150702_b()|TextComponent
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MetadataSectionSerializer

|Interface
|--
|net.minecraft.client.resources.data.IMetadataSectionSerializer

---

|Extends
|--
|JsonDeserializer

---

|Methods|Return Type
|--|--
| deserialize(JsonElement arg0, Type arg1, JsonDeserializationContext arg2)|Object
| func_110483_a()|String

---

## SVertexBuilder

|Class
|--
|net.optifine.shaders.SVertexBuilder

---

|Extends
|--

---

|Methods|Return Type
|--|--
| calcNormal(BufferBuilder arg0, int arg1)|void
| popEntity()|void
| pushEntity(long l)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BufferBuilder$State

|Class
|--
|net.minecraft.client.renderer.BufferBuilder$State

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_179013_a()|int[]
| func_179014_c()|int
| func_179016_d()|VertexFormat
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockStateMapper

|Class
|--
|net.minecraft.client.renderer.block.statemap.BlockStateMapper

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178446_a()|Map\<BlockState, ModelResourceLocation>
| func_178447_a(Block arg0, StateMapper arg1)|void
| func_178448_a(Block[] b)|void
| func_188181_b(Block b)|Map\<BlockState, ModelResourceLocation>
| func_188182_a(Block b)|Set\<ResourceLocation>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## StateMapper

|Interface
|--
|net.minecraft.client.renderer.block.statemap.IStateMapper

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178130_a(Block b)|Map\<BlockState, ModelResourceLocation>

---

## ItemCameraTransforms

|Class
|--
|net.minecraft.client.renderer.block.model.ItemCameraTransforms

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_178353_d|ItemTransformVec3f
|  field_178354_e|ItemTransformVec3f
|  field_181699_o|ItemTransformVec3f
|  field_181700_p|ItemTransformVec3f
|  field_188036_k|ItemTransformVec3f
|  field_188037_l|ItemTransformVec3f
|  field_188038_m|ItemTransformVec3f
|  field_188039_n|ItemTransformVec3f

---

|Methods|Return Type
|--|--
| func_181687_c(ItemCameraTransforms$TransformType i)|boolean
| func_181688_b(ItemCameraTransforms$TransformType i)|ItemTransformVec3f
| func_181689_a(ItemCameraTransforms$TransformType i)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemOverrideList

|Class
|--
|net.minecraft.client.renderer.block.model.ItemOverrideList

---

|Extends
|--

---

|Fields|Type
|--|--
|  overrides|ImmutableList\<ItemOverride>

---

|Methods|Return Type
|--|--
| func_188021_a(ItemStack arg0, World arg1, EntityLivingBase arg2)|ResourceLocation
| handleItemState(BakedModel arg0, ItemStack arg1, World arg2, EntityLivingBase arg3)|BakedModel
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Pair

|Class
|--
|org.apache.commons.lang3.tuple.Pair

---

|Extends
|--
|Map$Entry
|Comparable
|Serializable

---

|Fields|Type
|--|--
|  key|Object
|  left|Object
|  right|Object
|  value|Object

---

|Methods|Return Type
|--|--
| compareTo(Pair\<L, R> p)|int
| compareTo(Object o)|int
| toString(String s)|String
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AabbFrame

|Class
|--
|net.optifine.render.AabbFrame

---

|Extends
|--
|AxisAlignedBB

---

|Fields|Type
|--|--
|  field_72334_f|double
|  field_72336_d|double
|  field_72337_e|double
|  field_72338_b|double
|  field_72339_c|double
|  field_72340_a|double

---

|Methods|Return Type
|--|--
| func_111270_a(AxisAlignedBB a)|AxisAlignedBB
| func_181656_b()|boolean
| func_186660_b(Vec3d v)|boolean
| func_186662_g(double d)|AxisAlignedBB
| func_186664_h(double d)|AxisAlignedBB
| func_186666_e(double d)|AxisAlignedBB
| func_186667_c(Vec3d v)|boolean
| func_186668_a(double arg0, double arg1, double arg2, double arg3, double arg4, double arg5)|boolean
| func_186669_d(Vec3d v)|boolean
| func_186670_a(BlockPos b)|AxisAlignedBB
| func_189972_c()|Vec3d
| func_189973_a(Vec3d arg0, Vec3d arg1)|boolean
| func_191194_a(Vec3d v)|AxisAlignedBB
| func_191195_a(double arg0, double arg1, double arg2)|AxisAlignedBB
| func_191500_a(AxisAlignedBB a)|AxisAlignedBB
| func_72314_b(double arg0, double arg1, double arg2)|AxisAlignedBB
| func_72316_a(AxisAlignedBB arg0, double arg1)|double
| func_72317_d(double arg0, double arg1, double arg2)|AxisAlignedBB
| func_72318_a(Vec3d v)|boolean
| func_72320_b()|double
| func_72321_a(double arg0, double arg1, double arg2)|AxisAlignedBB
| func_72322_c(AxisAlignedBB arg0, double arg1)|double
| func_72323_b(AxisAlignedBB arg0, double arg1)|double
| func_72326_a(AxisAlignedBB a)|boolean
| func_72327_a(Vec3d arg0, Vec3d arg1)|RayTraceResult
| isBoundingBoxInFrustumFully(Camera arg0, int arg1)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CompiledChunk

|Class
|--
|net.minecraft.client.renderer.chunk.CompiledChunk

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178485_b()|List\<TileEntity>
| func_178486_a(BlockRenderLayer b)|void
| func_178487_c()|BufferBuilder$State
| func_178488_a(SetVisibility s)|void
| func_178489_a()|boolean
| func_178490_a(TileEntity t)|void
| func_178491_b(BlockRenderLayer b)|boolean
| func_178492_d(BlockRenderLayer b)|boolean
| func_178493_c(BlockRenderLayer b)|void
| func_178494_a(BufferBuilder$State b)|void
| func_178495_a(EnumFacing arg0, EnumFacing arg1)|boolean
| getAnimatedSprites(BlockRenderLayer b)|BitSet
| setAnimatedSprites(BlockRenderLayer arg0, BitSet arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ChunkCompileTaskGenerator

|Class
|--
|net.minecraft.client.renderer.chunk.ChunkCompileTaskGenerator

---

|Extends
|--
|Comparable

---

|Methods|Return Type
|--|--
| compareTo(ChunkCompileTaskGenerator c)|int
| compareTo(Object o)|int
| func_178535_a(ChunkCompileTaskGenerator$Status c)|void
| func_178536_b()|RenderChunk
| func_178537_h()|boolean
| func_178538_g()|ChunkCompileTaskGenerator$Type
| func_178539_a(Runnable r)|void
| func_178540_f()|ReentrantLock
| func_178541_a(RegionRenderCacheBuilder r)|void
| func_178542_e()|void
| func_178543_a(CompiledChunk c)|void
| func_178544_c()|CompiledChunk
| func_178545_d()|RegionRenderCacheBuilder
| func_178546_a()|ChunkCompileTaskGenerator$Status
| func_188228_i()|double
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ISound$AttenuationType

|Class
|--
|net.minecraft.client.audio.ISound$AttenuationType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_148586_a()|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Sound

|Class
|--
|net.minecraft.client.audio.Sound

---

|Extends
|--
|SoundEventAccessor

---

|Methods|Return Type
|--|--
| func_148720_g()|Object
| func_148720_g()|Sound
| func_148721_a()|int
| func_188719_a()|ResourceLocation
| func_188721_b()|ResourceLocation
| func_188722_g()|Sound$Type
| func_188723_h()|boolean
| func_188724_c()|float
| func_188725_d()|float
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Shader

|Class
|--
|net.minecraft.client.shader.Shader

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_148050_b|Framebuffer
|  field_148052_a|Framebuffer

---

|Methods|Return Type
|--|--
| func_148041_a(String arg0, Object arg1, int arg2, int arg3)|void
| func_148042_a(float f)|void
| func_148043_c()|ShaderManager
| func_148044_b()|void
| func_148045_a(Matrix4f m)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RegionRenderCacheBuilder

|Class
|--
|net.minecraft.client.renderer.RegionRenderCacheBuilder

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_179038_a(BlockRenderLayer b)|BufferBuilder
| func_179039_a(int i)|BufferBuilder
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## VboRange

|Class
|--
|net.optifine.render.VboRange

---

|Extends
|--

---

|Fields|Type
|--|--
|  next|VboRange
|  node|LinkedList$Node\<VboRange>
|  position|int
|  positionNext|int
|  prev|VboRange
|  size|int

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## VboRegion

|Class
|--
|net.optifine.render.VboRegion

---

|Extends
|--

---

|Fields|Type
|--|--
|  positionTop|int

---

|Methods|Return Type
|--|--
| bindBuffer()|void
| bufferData(ByteBuffer arg0, VboRange arg1)|void
| deleteGlBuffers()|void
| drawArrays(VboRange v)|void
| finishDraw(VboRenderList v)|void
| unbindBuffer()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## VertexFormatElement

|Class
|--
|net.minecraft.client.renderer.vertex.VertexFormatElement

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_177367_b()|VertexFormatElement$EnumType
| func_177368_f()|int
| func_177369_e()|int
| func_177370_d()|int
| func_177374_g()|boolean
| func_177375_c()|VertexFormatElement$EnumUsage
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockModelRenderer$AmbientOcclusionFace

|Class
|--
|net.minecraft.client.renderer.BlockModelRenderer$AmbientOcclusionFace

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_187491_a(BlockAccess arg0, BlockState arg1, BlockPos arg2, EnumFacing arg3, float[] arg4, BitSet arg5)|void
| setMaxBlockLight()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockPosM

|Class
|--
|net.optifine.BlockPosM

---

|Extends
|--
|BlockPos

---

|Methods|Return Type
|--|--
| compareTo(Vec3i v)|int
| compareTo(Object o)|int
| func_177951_i(Vec3i v)|double
| func_177952_p()|int
| func_177954_c(double arg0, double arg1, double arg2)|double
| func_177955_d(Vec3i v)|BlockPos
| func_177955_d(Vec3i v)|Vec3i
| func_177956_o()|int
| func_177957_d(double arg0, double arg1, double arg2)|double
| func_177958_n()|int
| func_177963_a(double arg0, double arg1, double arg2)|BlockPos
| func_177964_d(int i)|BlockPos
| func_177965_g(int i)|BlockPos
| func_177967_a(EnumFacing arg0, int arg1)|BlockPos
| func_177968_d()|BlockPos
| func_177970_e(int i)|BlockPos
| func_177971_a(Vec3i v)|BlockPos
| func_177972_a(EnumFacing e)|BlockPos
| func_177973_b(Vec3i v)|BlockPos
| func_177974_f()|BlockPos
| func_177976_e()|BlockPos
| func_177977_b()|BlockPos
| func_177978_c()|BlockPos
| func_177979_c(int i)|BlockPos
| func_177981_b(int i)|BlockPos
| func_177982_a(int arg0, int arg1, int arg2)|BlockPos
| func_177984_a()|BlockPos
| func_177985_f(int i)|BlockPos
| func_177986_g()|long
| func_185332_f(int arg0, int arg1, int arg2)|double
| func_185334_h()|BlockPos
| func_190942_a(Rotation r)|BlockPos
| setXyz(double arg0, double arg1, double arg2)|void
| setXyz(int arg0, int arg1, int arg2)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ListQuadsOverlay

|Class
|--
|net.optifine.model.ListQuadsOverlay

---

|Extends
|--

---

|Methods|Return Type
|--|--
| addQuad(BakedQuad arg0, BlockState arg1)|void
| clear()|void
| getBlockState(int i)|BlockState
| getListQuadsSingle(BakedQuad b)|List\<BakedQuad>
| getQuad(int i)|BakedQuad
| size()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Long2ObjectFunction

|Interface
|--
|it.unimi.dsi.fastutil.longs.Long2ObjectFunction

---

|Extends
|--
|Function

---

|Methods|Return Type
|--|--
| clear()|void
| containsKey(long l)|boolean
| containsKey(Object o)|boolean
| defaultReturnValue(Object o)|void
| defaultReturnValue()|Object
| get(long l)|Object
| get(Object o)|Object
| put(long arg0, Object arg1)|Object
| put(Object arg0, Object arg1)|Object
| remove(long l)|Object
| remove(Object o)|Object
| size()|int

---

## LongSet

|Interface
|--
|it.unimi.dsi.fastutil.longs.LongSet

---

|Extends
|--
|LongCollection
|Set

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(long l)|boolean
| add(Object o)|boolean
| add(Object o)|boolean
| addAll(LongCollection l)|boolean
| addAll(Collection\<? extends E> c)|boolean
| addAll(Collection\<? extends E> c)|boolean
| clear()|void
| clear()|void
| contains(long l)|boolean
| contains(Object o)|boolean
| contains(Object o)|boolean
| containsAll(LongCollection l)|boolean
| containsAll(Collection\<?> c)|boolean
| containsAll(Collection\<?> c)|boolean
| forEach(Consumer\<? super T> c)|void
| iterator()|LongIterator
| iterator()|Iterator\<E>
| iterator()|Iterator\<T>
| iterator()|Iterator\<E>
| longIterator()|LongIterator
| parallelStream()|Stream\<E>
| rem(long l)|boolean
| remove(long l)|boolean
| remove(Object o)|boolean
| remove(Object o)|boolean
| removeAll(LongCollection l)|boolean
| removeAll(Collection\<?> c)|boolean
| removeAll(Collection\<?> c)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| retainAll(LongCollection l)|boolean
| retainAll(Collection\<?> c)|boolean
| retainAll(Collection\<?> c)|boolean
| size()|int
| size()|int
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| toArray(long[] l)|long[]
| toArray(Object[] o)|Object[]
| toArray()|Object[]
| toArray()|Object[]
| toArray(Object[] o)|Object[]
| toLongArray()|long[]
| toLongArray(long[] l)|long[]

---

## EntityTameable

|Class
|--
|net.minecraft.entity.passive.EntityTameable

---

|Extends
|--
|EntityAnimal
|EntityOwnable

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_110153_bc|float
|  field_110158_av|int
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_184617_aD|int
|  field_184618_aE|float
|  field_184619_aG|float
|  field_184622_au|EnumHand
|  field_184627_bm|ItemStack
|  field_184628_bn|int
|  field_190534_ay|int
|  field_191988_bg|float
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_70696_bz|EntityLivingBase
|  field_70701_bs|float
|  field_70702_br|float
|  field_70703_bu|boolean
|  field_70704_bt|float
|  field_70714_bg|EntityAITasks
|  field_70715_bh|EntityAITasks
|  field_70718_bc|int
|  field_70720_be|int
|  field_70721_aZ|float
|  field_70725_aQ|int
|  field_70726_aT|float
|  field_70727_aS|float
|  field_70728_aV|int
|  field_70732_aI|float
|  field_70733_aJ|float
|  field_70737_aN|int
|  field_70738_aO|int
|  field_70739_aP|float
|  field_70747_aH|float
|  field_70755_b|EntityLivingBase
|  field_70757_a|int
|  field_70758_at|float
|  field_70759_as|float
|  field_70760_ar|float
|  field_70761_aq|float
|  field_70769_ao|float
|  field_70770_ap|float
|  field_70771_an|int
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_82175_bq|boolean
|  field_98038_p|boolean
|  itemInUseMaxDuration|int
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| curePotionEffects(ItemStack i)|void
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_104002_bU()|boolean
| func_110124_au()|UUID
| func_110138_aP()|float
| func_110139_bj()|float
| func_110140_aT()|AbstractAttributeMap
| func_110142_aN()|CombatTracker
| func_110143_aJ()|float
| func_110144_aD()|EntityLivingBase
| func_110145_l(Entity e)|void
| func_110148_a(Attribute a)|AttributeInstance
| func_110149_m(float f)|void
| func_110160_i(boolean arg0, boolean arg1)|void
| func_110162_b(Entity arg0, boolean arg1)|void
| func_110163_bv()|void
| func_110166_bE()|Entity
| func_110167_bD()|boolean
| func_110173_bK()|boolean
| func_110174_bM()|float
| func_110175_bO()|boolean
| func_110177_bN()|void
| func_110195_a(int i)|void
| func_130011_c(Entity e)|void
| func_130014_f_()|World
| func_142013_aG()|int
| func_142015_aE()|int
| func_142018_a(EntityLivingBase arg0, EntityLivingBase arg1)|boolean
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_146082_f(EntityPlayer e)|void
| func_152111_bt()|void
| func_152112_bu()|void
| func_152114_e(EntityLivingBase e)|boolean
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_175446_cd()|boolean
| func_175449_a(BlockPos arg0, int arg1)|void
| func_175501_a(int arg0, boolean arg1)|void
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180482_a(DifficultyInstance arg0, EntityLivingData arg1)|EntityLivingData
| func_180484_a(BlockPos b)|float
| func_180485_d(BlockPos b)|boolean
| func_180486_cf()|BlockPos
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_184582_a(EntityEquipmentSlot e)|ItemStack
| func_184583_d(DamageSource d)|boolean
| func_184585_cz()|boolean
| func_184586_b(EnumHand e)|ItemStack
| func_184587_cr()|boolean
| func_184589_d(Potion p)|void
| func_184591_cq()|EnumHandSide
| func_184592_cb()|ItemStack
| func_184595_k(double arg0, double arg1, double arg2)|boolean
| func_184596_c(Potion p)|PotionEffect
| func_184597_cx()|void
| func_184598_c(EnumHand e)|void
| func_184599_cB()|int
| func_184600_cs()|EnumHand
| func_184602_cy()|void
| func_184603_cC()|boolean
| func_184605_cv()|int
| func_184607_cu()|ItemStack
| func_184609_a(EnumHand e)|void
| func_184611_a(EnumHand arg0, ItemStack arg1)|void
| func_184612_cw()|int
| func_184613_cA()|boolean
| func_184614_ca()|ItemStack
| func_184638_cS()|boolean
| func_184641_n(boolean b)|void
| func_184642_a(EntityEquipmentSlot arg0, float arg1)|void
| func_184643_a(PathNodeType p)|float
| func_184644_a(PathNodeType arg0, float arg1)|void
| func_184645_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184646_p(float f)|void
| func_184649_cE()|int
| func_184652_a(EntityPlayer e)|boolean
| func_184753_b()|UUID
| func_184754_b(UUID u)|void
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_189748_bU()|DamageSource
| func_190530_aW()|boolean
| func_190630_a(EntityEquipmentSlot e)|boolean
| func_190631_cK()|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_191986_a(float arg0, float arg1, float arg2)|void
| func_191987_a(BlockPos arg0, boolean arg1)|void
| func_191989_p(float f)|void
| func_191993_do()|EntityPlayerMP
| func_193076_bZ()|Map\<Potion, PotionEffect>
| func_193101_c(EntityPlayer e)|void
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70058_J()|boolean
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70601_bi()|boolean
| func_70603_bj()|float
| func_70604_c(EntityLivingBase e)|void
| func_70605_aq()|EntityMoveHelper
| func_70606_j(float f)|void
| func_70608_bn()|boolean
| func_70613_aW()|boolean
| func_70615_aA()|void
| func_70617_f_()|boolean
| func_70624_b(EntityLivingBase e)|void
| func_70625_a(Entity arg0, float arg1, float arg2)|void
| func_70627_aG()|int
| func_70631_g_()|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70635_at()|EntitySenses
| func_70636_d()|void
| func_70637_d(boolean b)|void
| func_70638_az()|EntityLivingBase
| func_70641_bl()|int
| func_70642_aH()|void
| func_70643_av()|EntityLivingBase
| func_70644_a(Potion p)|boolean
| func_70645_a(DamageSource d)|void
| func_70646_bf()|int
| func_70648_aU()|boolean
| func_70651_bq()|Collection\<PotionEffect>
| func_70652_k(Entity e)|boolean
| func_70653_a(Entity arg0, float arg1, double arg2, double arg3)|void
| func_70654_ax()|int
| func_70656_aK()|void
| func_70657_f(float f)|void
| func_70658_aO()|int
| func_70659_e(float f)|void
| func_70660_b(Potion p)|PotionEffect
| func_70661_as()|PathNavigate
| func_70662_br()|boolean
| func_70668_bt()|EnumCreatureAttribute
| func_70669_a(ItemStack i)|void
| func_70671_ap()|EntityLookHelper
| func_70674_bp()|void
| func_70676_i(float f)|Vec3d
| func_70678_g(float f)|float
| func_70681_au()|Random
| func_70683_ar()|EntityJumpHelper
| func_70685_l(Entity e)|boolean
| func_70686_a(Class\<? extends net.minecraft.entity.EntityLivingBase> c)|boolean
| func_70687_e(PotionEffect p)|boolean
| func_70689_ay()|float
| func_70690_d(PotionEffect p)|void
| func_70691_i(float f)|void
| func_70781_l()|boolean
| func_70873_a(int i)|void
| func_70874_b()|int
| func_70875_t()|void
| func_70877_b(ItemStack i)|boolean
| func_70878_b(EntityAnimal e)|boolean
| func_70880_s()|boolean
| func_70902_q()|EntityLivingBase
| func_70902_q()|Entity
| func_70903_f(boolean b)|void
| func_70904_g(boolean b)|void
| func_70906_o()|boolean
| func_70907_r()|EntityAISit
| func_70909_n()|boolean
| func_71001_a(Entity arg0, int arg1)|void
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_82171_bF()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_85034_r(int i)|void
| func_85035_bI()|int
| func_90011_a(EntityAgeable e)|EntityAgeable
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_94060_bK()|EntityLivingBase
| func_94061_f(boolean b)|void
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| func_98052_bS()|boolean
| func_98053_h(boolean b)|void
| func_98054_a(boolean b)|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderFaceForward(EntityPlayer e)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## EntityAISit

|Class
|--
|net.minecraft.entity.ai.EntityAISit

---

|Extends
|--
|EntityAIBase

---

|Methods|Return Type
|--|--
| func_75246_d()|void
| func_75247_h()|int
| func_75248_a(int i)|void
| func_75249_e()|void
| func_75250_a()|boolean
| func_75251_c()|void
| func_75252_g()|boolean
| func_75253_b()|boolean
| func_75270_a(boolean b)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SpectatorMenuRecipient

|Interface
|--
|net.minecraft.client.gui.spectator.ISpectatorMenuRecipient

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_175257_a(SpectatorMenu s)|void

---

## SpectatorMenu

|Class
|--
|net.minecraft.client.gui.spectator.SpectatorMenu

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178641_d()|void
| func_178642_a()|List\<SpectatorMenuObject>
| func_178643_a(int i)|SpectatorMenuObject
| func_178644_b(int i)|void
| func_178645_b()|SpectatorMenuObject
| func_178646_f()|SpectatorDetails
| func_178647_a(SpectatorMenuView s)|void
| func_178648_e()|int
| func_178650_c()|SpectatorMenuView
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BossInfoClient

|Class
|--
|net.minecraft.client.gui.BossInfoClient

---

|Extends
|--
|BossInfo

---

|Methods|Return Type
|--|--
| func_186734_i()|boolean
| func_186735_a(float f)|void
| func_186736_g()|BossInfo$Color
| func_186737_d()|UUID
| func_186738_f()|float
| func_186739_a(TextComponent t)|void
| func_186740_h()|BossInfo$Overlay
| func_186741_a(boolean b)|BossInfo
| func_186742_b(boolean b)|BossInfo
| func_186743_c(boolean b)|BossInfo
| func_186744_e()|TextComponent
| func_186745_a(BossInfo$Color b)|void
| func_186746_a(BossInfo$Overlay b)|void
| func_186747_j()|boolean
| func_186748_k()|boolean
| func_186765_a(SPacketUpdateBossInfo s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MapData

|Class
|--
|net.minecraft.world.storage.MapData

---

|Extends
|--
|WorldSavedData

---

|Fields|Type
|--|--
|  field_186210_e|boolean
|  field_191096_f|boolean
|  field_76190_i|String
|  field_76196_g|List\<MapData$MapInfo>
|  field_76197_d|byte
|  field_76198_e|byte[]
|  field_76199_b|int
|  field_76200_c|int
|  field_76201_a|int
|  field_76203_h|Map\<String, MapDecoration>

---

|Methods|Return Type
|--|--
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_176052_a(ItemStack arg0, World arg1, EntityPlayer arg2)|Packet\<?>
| func_176053_a(int arg0, int arg1)|void
| func_176054_a(double arg0, double arg1, int arg2)|void
| func_189551_b(NBTTagCompound n)|NBTTagCompound
| func_76184_a(NBTTagCompound n)|void
| func_76185_a()|void
| func_76186_a(boolean b)|void
| func_76188_b()|boolean
| func_76191_a(EntityPlayer arg0, ItemStack arg1)|void
| func_82568_a(EntityPlayer e)|MapData$MapInfo
| serializeNBT()|NBTBase
| serializeNBT()|NBTTagCompound
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MapItemRenderer$Instance

|Class
|--
|net.minecraft.client.gui.MapItemRenderer$Instance

---

|Extends
|--

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## KeyConflictContext

|Interface
|--
|net.minecraftforge.client.settings.IKeyConflictContext

---

|Extends
|--

---

|Fields|Type
|--|--
|  active|boolean

---

|Methods|Return Type
|--|--
| conflicts(KeyConflictContext k)|boolean

---

## KeyModifier

|Class
|--
|net.minecraftforge.client.settings.KeyModifier

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  active|boolean
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| getLocalizedComboName(int i)|String
| matches(int i)|boolean
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TutorialStep

|Interface
|--
|net.minecraft.client.tutorial.ITutorialStep

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_193245_a()|void
| func_193246_a(WorldClient arg0, RayTraceResult arg1)|void
| func_193247_a(MovementInput m)|void
| func_193248_b()|void
| func_193249_a(MouseHelper m)|void
| func_193250_a(WorldClient arg0, BlockPos arg1, BlockState arg2, float arg3)|void
| func_193251_c()|void
| func_193252_a(ItemStack i)|void

---

## SPacketUpdateScore$Action

|Class
|--
|net.minecraft.network.play.server.SPacketUpdateScore$Action

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketPlayerListItem$AddPlayerData

|Class
|--
|net.minecraft.network.play.server.SPacketPlayerListItem$AddPlayerData

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_179960_c()|GameType
| func_179961_d()|TextComponent
| func_179962_a()|GameProfile
| func_179963_b()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketPlayerListItem$Action

|Class
|--
|net.minecraft.network.play.server.SPacketPlayerListItem$Action

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketMultiBlockChange$BlockUpdateData

|Class
|--
|net.minecraft.network.play.server.SPacketMultiBlockChange$BlockUpdateData

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_180088_c()|BlockState
| func_180089_b()|short
| func_180090_a()|BlockPos
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketEntityProperties$Snapshot

|Class
|--
|net.minecraft.network.play.server.SPacketEntityProperties$Snapshot

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_151408_c()|Collection\<AttributeModifier>
| func_151409_a()|String
| func_151410_b()|double
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketCombatEvent$Event

|Class
|--
|net.minecraft.network.play.server.SPacketCombatEvent$Event

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketTitle$Type

|Class
|--
|net.minecraft.network.play.server.SPacketTitle$Type

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BossInfo$Color

|Class
|--
|net.minecraft.world.BossInfo$Color

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketUpdateBossInfo$Operation

|Class
|--
|net.minecraft.network.play.server.SPacketUpdateBossInfo$Operation

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BossInfo$Overlay

|Class
|--
|net.minecraft.world.BossInfo$Overlay

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketPlayerPosLook$EnumFlags

|Class
|--
|net.minecraft.network.play.server.SPacketPlayerPosLook$EnumFlags

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SPacketRecipeBook$State

|Class
|--
|net.minecraft.network.play.server.SPacketRecipeBook$State

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AdvancementProgress

|Class
|--
|net.minecraft.advancements.AdvancementProgress

---

|Extends
|--
|Comparable

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(AdvancementProgress a)|int
| func_192099_a(Map\<String, Criterion> arg0, String[][] arg1)|void
| func_192101_b(String s)|boolean
| func_192102_e()|Iterable\<String>
| func_192103_c()|float
| func_192104_a(PacketBuffer p)|void
| func_192105_a()|boolean
| func_192106_c(String s)|CriterionProgress
| func_192107_d()|Iterable\<String>
| func_192108_b()|boolean
| func_192109_a(String s)|boolean
| func_193126_d()|String
| func_193128_g()|Date
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ClientAdvancementManager$IListener

|Interface
|--
|net.minecraft.client.multiplayer.ClientAdvancementManager$IListener

---

|Extends
|--
|AdvancementList$Listener

---

|Methods|Return Type
|--|--
| func_191928_b(Advancement a)|void
| func_191929_d(Advancement a)|void
| func_191930_a()|void
| func_191931_a(Advancement a)|void
| func_191932_c(Advancement a)|void
| func_191933_a(Advancement arg0, AdvancementProgress arg1)|void
| func_193982_e(Advancement a)|void

---

## AdvancementList

|Class
|--
|net.minecraft.advancements.AdvancementList

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_192083_a(Map\<ResourceLocation, Advancement$Builder> m)|void
| func_192084_a(ResourceLocation r)|Advancement
| func_192085_a(Set\<ResourceLocation> s)|void
| func_192086_a(AdvancementList$Listener a)|void
| func_192087_a()|void
| func_192088_b()|Iterable\<Advancement>
| func_192089_c()|Iterable\<Advancement>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SoundManager$SoundSystemStarterThread

|Class
|--
|net.minecraft.client.audio.SoundManager$SoundSystemStarterThread

---

|Extends
|--
|SoundSystem

---

|Fields|Type
|--|--
|  listenerData|ListenerData
|  masterVolume|float
|  randomNumberGenerator|Random
|  this$0|SoundManager

---

|Methods|Return Type
|--|--
| activate(String s)|void
| backgroundMusic(String arg0, String arg1, boolean arg2)|void
| backgroundMusic(String arg0, URL arg1, String arg2, boolean arg3)|void
| changeDopplerFactor(float f)|void
| changeDopplerVelocity(float f)|void
| checkFadeVolumes()|void
| cleanup()|void
| CommandQueue(CommandObject c)|boolean
| cull(String s)|void
| dequeueSound(String arg0, String arg1)|void
| fadeOut(String arg0, URL arg1, String arg2, long arg3)|void
| fadeOut(String arg0, String arg1, long arg2)|void
| fadeOutIn(String arg0, String arg1, long arg2, long arg3)|void
| fadeOutIn(String arg0, URL arg1, String arg2, long arg3, long arg4)|void
| feedRawAudioData(String arg0, byte[] arg1)|void
| flush(String s)|void
| getPitch(String s)|float
| getVolume(String s)|float
| interruptCommandThread()|void
| loadSound(URL arg0, String arg1)|void
| loadSound(byte[] arg0, AudioFormat arg1, String arg2)|void
| loadSound(String s)|void
| millisecondsPlayed(String s)|float
| moveListener(float arg0, float arg1, float arg2)|void
| newLibrary(Class c)|boolean
| newSource(boolean arg0, String arg1, String arg2, boolean arg3, float arg4, float arg5, float arg6, int arg7, float arg8)|void
| newSource(boolean arg0, String arg1, URL arg2, String arg3, boolean arg4, float arg5, float arg6, float arg7, int arg8, float arg9)|void
| newStreamingSource(boolean arg0, String arg1, String arg2, boolean arg3, float arg4, float arg5, float arg6, int arg7, float arg8)|void
| newStreamingSource(boolean arg0, String arg1, URL arg2, String arg3, boolean arg4, float arg5, float arg6, float arg7, int arg8, float arg9)|void
| pause(String s)|void
| play(String s)|void
| playing(String s)|boolean
| playing()|boolean
| queueSound(String arg0, String arg1)|void
| queueSound(String arg0, URL arg1, String arg2)|void
| quickPlay(boolean arg0, URL arg1, String arg2, boolean arg3, float arg4, float arg5, float arg6, int arg7, float arg8)|String
| quickPlay(boolean arg0, String arg1, boolean arg2, float arg3, float arg4, float arg5, int arg6, float arg7)|String
| quickStream(boolean arg0, URL arg1, String arg2, boolean arg3, float arg4, float arg5, float arg6, int arg7, float arg8)|String
| quickStream(boolean arg0, String arg1, boolean arg2, float arg3, float arg4, float arg5, int arg6, float arg7)|String
| rawDataStream(AudioFormat arg0, boolean arg1, String arg2, float arg3, float arg4, float arg5, int arg6, float arg7)|void
| removeSource(String s)|void
| removeTemporarySources()|void
| rewind(String s)|void
| setAttenuation(String arg0, int arg1)|void
| setDistOrRoll(String arg0, float arg1)|void
| setListenerAngle(float f)|void
| setListenerOrientation(float arg0, float arg1, float arg2, float arg3, float arg4, float arg5)|void
| setListenerPosition(float arg0, float arg1, float arg2)|void
| setListenerVelocity(float arg0, float arg1, float arg2)|void
| setLooping(String arg0, boolean arg1)|void
| setPitch(String arg0, float arg1)|void
| setPosition(String arg0, float arg1, float arg2, float arg3)|void
| setPriority(String arg0, boolean arg1)|void
| setTemporary(String arg0, boolean arg1)|void
| setVelocity(String arg0, float arg1, float arg2, float arg3)|void
| setVolume(String arg0, float arg1)|void
| stop(String s)|void
| switchLibrary(Class c)|boolean
| turnListener(float f)|void
| unloadSound(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TickableSound

|Interface
|--
|net.minecraft.client.audio.ITickableSound

---

|Extends
|--
|Sound
|Tickable

---

|Methods|Return Type
|--|--
| func_147649_g()|float
| func_147650_b()|ResourceLocation
| func_147651_i()|float
| func_147652_d()|int
| func_147653_e()|float
| func_147654_h()|float
| func_147655_f()|float
| func_147656_j()|ISound$AttenuationType
| func_147657_c()|boolean
| func_147667_k()|boolean
| func_184364_b()|Sound
| func_184365_d()|SoundCategory
| func_184366_a(SoundHandler s)|SoundEventAccessor
| func_73660_a()|void

---

## SoundEventAccessor

|Interface
|--
|net.minecraft.client.audio.ISoundEventAccessor

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_148720_g()|Object
| func_148721_a()|int

---

## ModelPart

|Interface
|--
|net.minecraftforge.common.model.IModelPart

---

|Extends
|--

---

## EntityRenderer

|Interface
|--
|net.optifine.entity.model.IEntityRenderer

---

|Extends
|--

---

|Fields|Type
|--|--
|  entityClass|Class
|  locationTextureCustom|ResourceLocation

---

|Methods|Return Type
|--|--

---

## RenderLivingBase

|Class
|--
|net.minecraft.client.renderer.entity.RenderLivingBase

---

|Extends
|--
|Render

---

|Fields|Type
|--|--
|  entityClass|Class
|  field_177097_h|List\<net.minecraft.client.renderer.entity.layers.LayerRenderer\<T>>
|  field_76989_e|float
|  field_77045_g|ModelBase
|  layerRenderers|List\<net.minecraft.client.renderer.entity.layers.LayerRenderer\<T>>
|  locationTextureCustom|ResourceLocation
|  renderAgeInTicks|float
|  renderEntity|EntityLivingBase
|  renderHeadPitch|float
|  renderHeadYaw|float
|  renderLimbSwing|float
|  renderLimbSwingAmount|float
|  renderPartialTicks|float
|  renderScaleFactor|float

---

|Methods|Return Type
|--|--
| func_110776_a(ResourceLocation r)|void
| func_177067_a(EntityLivingBase arg0, double arg1, double arg2, double arg3)|void
| func_177067_a(Entity arg0, double arg1, double arg2, double arg3)|void
| func_177068_d()|RenderManager
| func_177071_a(Entity arg0, Camera arg1, double arg2, double arg3, double arg4)|boolean
| func_177087_b()|ModelBase
| func_177094_a(LayerRenderer l)|boolean
| func_188295_H_()|boolean
| func_188297_a(boolean b)|void
| func_188300_b(Entity arg0, double arg1, double arg2, double arg3, float arg4, float arg5)|void
| func_188322_c(EntityLivingBase arg0, float arg1)|float
| func_76979_b(Entity arg0, double arg1, double arg2, double arg3, float arg4, float arg5)|void
| func_76983_a()|FontRenderer
| func_76986_a(EntityLivingBase arg0, double arg1, double arg2, double arg3, float arg4, float arg5)|void
| func_76986_a(Entity arg0, double arg1, double arg2, double arg3, float arg4, float arg5)|void
| func_82422_c()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ModelPlayer

|Class
|--
|net.minecraft.client.model.ModelPlayer

---

|Extends
|--
|ModelBiped

---

|Fields|Type
|--|--
|  field_178720_f|ModelRenderer
|  field_178721_j|ModelRenderer
|  field_178722_k|ModelRenderer
|  field_178723_h|ModelRenderer
|  field_178724_i|ModelRenderer
|  field_178730_v|ModelRenderer
|  field_178731_d|ModelRenderer
|  field_178732_b|ModelRenderer
|  field_178733_c|ModelRenderer
|  field_178734_a|ModelRenderer
|  field_187075_l|ModelBiped$ArmPose
|  field_187076_m|ModelBiped$ArmPose
|  field_78089_u|int
|  field_78090_t|int
|  field_78091_s|boolean
|  field_78092_r|List\<ModelRenderer>
|  field_78093_q|boolean
|  field_78095_p|float
|  field_78115_e|ModelRenderer
|  field_78116_c|ModelRenderer
|  field_78117_n|boolean

---

|Methods|Return Type
|--|--
| func_178686_a(ModelBase m)|void
| func_178719_a(boolean b)|void
| func_178727_b(float f)|void
| func_178728_c(float f)|void
| func_187073_a(float arg0, EnumHandSide arg1)|void
| func_78084_a(String s)|TextureOffset
| func_78086_a(EntityLivingBase arg0, float arg1, float arg2, float arg3)|void
| func_78087_a(float arg0, float arg1, float arg2, float arg3, float arg4, float arg5, Entity arg6)|void
| func_78088_a(Entity arg0, float arg1, float arg2, float arg3, float arg4, float arg5, float arg6)|void
| func_85181_a(Random r)|ModelRenderer
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## LayerRenderer

|Interface
|--
|net.minecraft.client.renderer.entity.layers.LayerRenderer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_177141_a(EntityLivingBase arg0, float arg1, float arg2, float arg3, float arg4, float arg5, float arg6, float arg7)|void
| func_177142_b()|boolean

---

## ItemMeshDefinition

|Interface
|--
|net.minecraft.client.renderer.ItemMeshDefinition

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178113_a(ItemStack i)|ModelResourceLocation

---

## ModelResourceLocation

|Class
|--
|net.minecraft.client.renderer.block.model.ModelResourceLocation

---

|Extends
|--
|ResourceLocation

---

|Fields|Type
|--|--
|  field_110625_b|String
|  field_110626_a|String

---

|Methods|Return Type
|--|--
| compareTo(ResourceLocation r)|int
| compareTo(Object o)|int
| func_110623_a()|String
| func_110624_b()|String
| func_177518_c()|String
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## VertexProducer

|Interface
|--
|net.minecraftforge.client.model.pipeline.IVertexProducer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| pipe(VertexConsumer v)|void

---

## QuadBounds

|Class
|--
|net.optifine.model.QuadBounds

---

|Extends
|--

---

|Fields|Type
|--|--
|  maxX|float
|  maxY|float
|  maxZ|float
|  minX|float
|  minY|float
|  minZ|float

---

|Methods|Return Type
|--|--
| isFaceQuad(EnumFacing e)|boolean
| isFullQuad(EnumFacing e)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## VertexConsumer

|Interface
|--
|net.minecraftforge.client.model.pipeline.IVertexConsumer

---

|Extends
|--

---

|Fields|Type
|--|--
|  vertexFormat|VertexFormat

---

|Methods|Return Type
|--|--
| put(int arg0, float[] arg1)|void
| setApplyDiffuseLighting(boolean b)|void
| setQuadOrientation(EnumFacing e)|void
| setQuadTint(int i)|void
| setTexture(TextureAtlasSprite t)|void

---

## IToast$Visibility

|Class
|--
|net.minecraft.client.gui.toasts.IToast$Visibility

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_194169_a(SoundHandler s)|void
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ServerStatusResponse$Players

|Class
|--
|net.minecraft.network.ServerStatusResponse$Players

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_151330_a(GameProfile[] g)|void
| func_151331_c()|GameProfile[]
| func_151332_a()|int
| func_151333_b()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ServerStatusResponse$Version

|Class
|--
|net.minecraft.network.ServerStatusResponse$Version

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_151303_a()|String
| func_151304_b()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PlayerProfileCache$ProfileEntry

|Class
|--
|net.minecraft.server.management.PlayerProfileCache$ProfileEntry

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_152668_a()|GameProfile
| func_152670_b()|Date
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Agent

|Class
|--
|com.mojang.authlib.Agent

---

|Extends
|--

---

|Fields|Type
|--|--
|  name|String
|  version|int

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ProfileLookupCallback

|Interface
|--
|com.mojang.authlib.ProfileLookupCallback

---

|Extends
|--

---

|Methods|Return Type
|--|--
| onProfileLookupFailed(GameProfile arg0, Exception arg1)|void
| onProfileLookupSucceeded(GameProfile g)|void

---

## CommandHandler

|Class
|--
|net.minecraft.command.CommandHandler

---

|Extends
|--
|CommandManager

---

|Fields|Type
|--|--
|  field_71561_b|Set\<Command>

---

|Methods|Return Type
|--|--
| func_180524_a(CommandSender arg0, String arg1, BlockPos arg2)|List\<String>
| func_71555_a()|Map\<String, Command>
| func_71556_a(CommandSender arg0, String arg1)|int
| func_71557_a(CommandSender c)|List\<Command>
| func_71560_a(Command c)|Command
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CommandListener

|Interface
|--
|net.minecraft.command.ICommandListener

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_152372_a(CommandSender arg0, Command arg1, int arg2, String arg3, Object[] arg4)|void

---

## UserListWhitelist

|Class
|--
|net.minecraft.server.management.UserListWhitelist

---

|Extends
|--
|UserList

---

|Methods|Return Type
|--|--
| func_152678_f()|void
| func_152683_b(Object o)|UserListEntry
| func_152684_c(Object o)|void
| func_152685_a()|String[]
| func_152686_a(boolean b)|void
| func_152687_a(UserListEntry u)|void
| func_152689_b()|boolean
| func_152706_a(String s)|GameProfile
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## UserListOps

|Class
|--
|net.minecraft.server.management.UserListOps

---

|Extends
|--
|UserList

---

|Methods|Return Type
|--|--
| func_152678_f()|void
| func_152683_b(Object o)|UserListEntry
| func_152684_c(Object o)|void
| func_152685_a()|String[]
| func_152686_a(boolean b)|void
| func_152687_a(UserListEntry u)|void
| func_152689_b()|boolean
| func_152700_a(String s)|GameProfile
| func_183026_b(GameProfile g)|boolean
| func_187452_a(GameProfile g)|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## UserListBans

|Class
|--
|net.minecraft.server.management.UserListBans

---

|Extends
|--
|UserList

---

|Methods|Return Type
|--|--
| func_152678_f()|void
| func_152683_b(Object o)|UserListEntry
| func_152684_c(Object o)|void
| func_152685_a()|String[]
| func_152686_a(boolean b)|void
| func_152687_a(UserListEntry u)|void
| func_152689_b()|boolean
| func_152702_a(GameProfile g)|boolean
| func_152703_a(String s)|GameProfile
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## UserListIPBans

|Class
|--
|net.minecraft.server.management.UserListIPBans

---

|Extends
|--
|UserList

---

|Methods|Return Type
|--|--
| func_152678_f()|void
| func_152683_b(Object o)|UserListEntry
| func_152684_c(Object o)|void
| func_152685_a()|String[]
| func_152686_a(boolean b)|void
| func_152687_a(UserListEntry u)|void
| func_152689_b()|boolean
| func_152708_a(SocketAddress s)|boolean
| func_152709_b(SocketAddress s)|UserListIPBansEntry
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AbstractInt2ByteFunction

|Class
|--
|it.unimi.dsi.fastutil.ints.AbstractInt2ByteFunction

---

|Extends
|--
|Int2ByteFunction
|Serializable

---

|Methods|Return Type
|--|--
| clear()|void
| containsKey(Object o)|boolean
| containsKey(int i)|boolean
| defaultReturnValue(byte b)|void
| defaultReturnValue()|byte
| get(Object o)|byte
| get(Object o)|Object
| get(int i)|byte
| put(int arg0, byte arg1)|byte
| put(int arg0, byte arg1)|byte
| put(Object arg0, Object arg1)|Object
| remove(int i)|byte
| remove(Object o)|byte
| remove(Object o)|Object
| size()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Int2ByteMap

|Interface
|--
|it.unimi.dsi.fastutil.ints.Int2ByteMap

---

|Extends
|--
|Int2ByteFunction
|Map

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| clear()|void
| clear()|void
| compute(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| computeIfAbsent(Object arg0, Function\<? super K, ? extends V> arg1)|Object
| computeIfPresent(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| containsKey(int i)|boolean
| containsKey(Object o)|boolean
| containsKey(Object o)|boolean
| containsValue(byte b)|boolean
| containsValue(Object o)|boolean
| defaultReturnValue(byte b)|void
| defaultReturnValue()|byte
| entrySet()|ObjectSet\<java.util.Map$Entry\<java.lang.Integer, java.lang.Byte>>
| entrySet()|Set\<java.util.Map$Entry\<K, V>>
| forEach(BiConsumer\<? super K, ? super V> b)|void
| get(int i)|byte
| get(Object o)|Object
| get(Object o)|Object
| getOrDefault(Object arg0, Object arg1)|Object
| int2ByteEntrySet()|ObjectSet\<Int2ByteMap$Entry>
| keySet()|IntSet
| keySet()|Set\<K>
| merge(Object arg0, Object arg1, BiFunction\<? super V, ? super V, ? extends V> arg2)|Object
| put(int arg0, byte arg1)|byte
| put(Object arg0, Object arg1)|Object
| put(Object arg0, Object arg1)|Object
| putAll(Map\<? extends K, ? extends V> m)|void
| putIfAbsent(Object arg0, Object arg1)|Object
| remove(int i)|byte
| remove(Object o)|Object
| remove(Object o)|Object
| remove(Object arg0, Object arg1)|boolean
| replace(Object arg0, Object arg1)|Object
| replace(Object arg0, Object arg1, Object arg2)|boolean
| replaceAll(BiFunction\<? super K, ? super V, ? extends V> b)|void
| size()|int
| size()|int
| values()|ByteCollection
| values()|Collection\<V>

---

## Int2ByteMap$Entry

|Interface
|--
|it.unimi.dsi.fastutil.ints.Int2ByteMap$Entry

---

|Extends
|--
|Map$Entry

---

|Fields|Type
|--|--
|  byteValue|byte
|  intKey|int
|  key|Object
|  value|Object

---

|Methods|Return Type
|--|--

---

## ObjectIterator

|Interface
|--
|it.unimi.dsi.fastutil.objects.ObjectIterator

---

|Extends
|--
|Iterator

---

|Methods|Return Type
|--|--
| forEachRemaining(Consumer\<? super E> c)|void
| hasNext()|boolean
| next()|Object
| remove()|void
| skip(int i)|int

---

## ByteIterable

|Interface
|--
|it.unimi.dsi.fastutil.bytes.ByteIterable

---

|Extends
|--
|Iterable

---

|Methods|Return Type
|--|--
| forEach(Consumer\<? super T> c)|void
| iterator()|ByteIterator
| iterator()|Iterator\<T>
| spliterator()|Spliterator\<T>

---

## ByteIterator

|Interface
|--
|it.unimi.dsi.fastutil.bytes.ByteIterator

---

|Extends
|--
|Iterator

---

|Methods|Return Type
|--|--
| forEachRemaining(Consumer\<? super E> c)|void
| hasNext()|boolean
| next()|Object
| nextByte()|byte
| remove()|void
| skip(int i)|int

---

## AbstractIntCollection

|Class
|--
|it.unimi.dsi.fastutil.ints.AbstractIntCollection

---

|Extends
|--
|AbstractCollection
|IntCollection

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(int i)|boolean
| add(int i)|boolean
| add(Object o)|boolean
| addAll(IntCollection i)|boolean
| addAll(Collection\<? extends java.lang.Integer> c)|boolean
| clear()|void
| contains(int i)|boolean
| contains(Object o)|boolean
| containsAll(Collection\<?> c)|boolean
| containsAll(IntCollection i)|boolean
| forEach(Consumer\<? super T> c)|void
| intIterator()|IntIterator
| iterator()|Iterator
| iterator()|IntIterator
| parallelStream()|Stream\<E>
| rem(int i)|boolean
| rem(Object o)|boolean
| remove(Object o)|boolean
| removeAll(Collection\<?> c)|boolean
| removeAll(IntCollection i)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| retainAll(Collection\<?> c)|boolean
| retainAll(IntCollection i)|boolean
| size()|int
| size()|int
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| toArray()|Object[]
| toArray(Object[] o)|Object[]
| toArray(int[] i)|int[]
| toIntArray()|int[]
| toIntArray(int[] i)|int[]
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## IntIterable

|Interface
|--
|it.unimi.dsi.fastutil.ints.IntIterable

---

|Extends
|--
|Iterable

---

|Methods|Return Type
|--|--
| forEach(Consumer\<? super T> c)|void
| iterator()|IntIterator
| iterator()|Iterator\<T>
| spliterator()|Spliterator\<T>

---

## AbstractInt2ObjectFunction

|Class
|--
|it.unimi.dsi.fastutil.ints.AbstractInt2ObjectFunction

---

|Extends
|--
|Int2ObjectFunction
|Serializable

---

|Methods|Return Type
|--|--
| clear()|void
| containsKey(Object o)|boolean
| containsKey(int i)|boolean
| defaultReturnValue(Object o)|void
| defaultReturnValue()|Object
| get(Object o)|Object
| get(int i)|Object
| put(int arg0, Object arg1)|Object
| put(Object arg0, Object arg1)|Object
| put(int arg0, Object arg1)|Object
| remove(int i)|Object
| remove(Object o)|Object
| size()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Int2ObjectMap

|Interface
|--
|it.unimi.dsi.fastutil.ints.Int2ObjectMap

---

|Extends
|--
|Int2ObjectFunction
|Map

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| clear()|void
| clear()|void
| compute(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| computeIfAbsent(Object arg0, Function\<? super K, ? extends V> arg1)|Object
| computeIfPresent(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| containsKey(int i)|boolean
| containsKey(Object o)|boolean
| containsKey(Object o)|boolean
| containsValue(Object o)|boolean
| defaultReturnValue(Object o)|void
| defaultReturnValue()|Object
| entrySet()|ObjectSet\<java.util.Map$Entry\<java.lang.Integer, V>>
| entrySet()|Set\<java.util.Map$Entry\<K, V>>
| forEach(BiConsumer\<? super K, ? super V> b)|void
| get(int i)|Object
| get(Object o)|Object
| get(Object o)|Object
| getOrDefault(Object arg0, Object arg1)|Object
| int2ObjectEntrySet()|ObjectSet\<it.unimi.dsi.fastutil.ints.Int2ObjectMap$Entry\<V>>
| keySet()|IntSet
| keySet()|Set\<K>
| merge(Object arg0, Object arg1, BiFunction\<? super V, ? super V, ? extends V> arg2)|Object
| put(int arg0, Object arg1)|Object
| put(Object arg0, Object arg1)|Object
| put(Object arg0, Object arg1)|Object
| putAll(Map\<? extends K, ? extends V> m)|void
| putIfAbsent(Object arg0, Object arg1)|Object
| remove(int i)|Object
| remove(Object o)|Object
| remove(Object o)|Object
| remove(Object arg0, Object arg1)|boolean
| replace(Object arg0, Object arg1)|Object
| replace(Object arg0, Object arg1, Object arg2)|boolean
| replaceAll(BiFunction\<? super K, ? super V, ? extends V> b)|void
| size()|int
| size()|int
| values()|ObjectCollection\<V>
| values()|Collection\<V>

---

## ObjectIterable

|Interface
|--
|it.unimi.dsi.fastutil.objects.ObjectIterable

---

|Extends
|--
|Iterable

---

|Methods|Return Type
|--|--
| forEach(Consumer\<? super T> c)|void
| iterator()|ObjectIterator\<K>
| iterator()|Iterator\<T>
| spliterator()|Spliterator\<T>

---

## OpenableGui

|Interface
|--
|com.feed_the_beast.ftblib.lib.gui.IOpenableGui

---

|Extends
|--
|Runnable

---

|Methods|Return Type
|--|--
| closeContextMenu()|void
| closeGui(boolean b)|void
| closeGui()|void
| openContextMenu(Panel p)|void
| openGui()|void
| openGuiLater()|void
| run()|void

---

## MouseButton

|Class
|--
|com.feed_the_beast.ftblib.lib.util.misc.MouseButton

---

|Extends
|--

---

|Fields|Type
|--|--
|  id|int
|  left|boolean
|  middle|boolean
|  right|boolean

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NetHandlerPlayServer

|Interface
|--
|net.minecraft.network.play.INetHandlerPlayServer

---

|Extends
|--
|NetHandler

---

|Methods|Return Type
|--|--
| func_147231_a(TextComponent t)|void
| func_147338_a(CPacketEnchantItem c)|void
| func_147339_a(CPacketConfirmTransaction c)|void
| func_147340_a(CPacketUseEntity c)|void
| func_147341_a(CPacketTabComplete c)|void
| func_147342_a(CPacketClientStatus c)|void
| func_147343_a(CPacketUpdateSign c)|void
| func_147344_a(CPacketCreativeInventoryAction c)|void
| func_147345_a(CPacketPlayerDigging c)|void
| func_147346_a(CPacketPlayerTryUseItem c)|void
| func_147347_a(CPacketPlayer c)|void
| func_147348_a(CPacketPlayerAbilities c)|void
| func_147349_a(CPacketCustomPayload c)|void
| func_147351_a(CPacketClickWindow c)|void
| func_147352_a(CPacketClientSettings c)|void
| func_147353_a(CPacketKeepAlive c)|void
| func_147354_a(CPacketChatMessage c)|void
| func_147355_a(CPacketHeldItemChange c)|void
| func_147356_a(CPacketCloseWindow c)|void
| func_147357_a(CPacketEntityAction c)|void
| func_147358_a(CPacketInput c)|void
| func_175086_a(CPacketResourcePackStatus c)|void
| func_175087_a(CPacketAnimation c)|void
| func_175088_a(CPacketSpectate c)|void
| func_184337_a(CPacketPlayerTryUseItemOnBlock c)|void
| func_184338_a(CPacketVehicleMove c)|void
| func_184339_a(CPacketConfirmTeleport c)|void
| func_184340_a(CPacketSteerBoat c)|void
| func_191984_a(CPacketRecipeInfo c)|void
| func_194027_a(CPacketSeenAdvancements c)|void
| func_194308_a(CPacketPlaceRecipe c)|void

---

## CPacketEnchantItem

|Class
|--
|net.minecraft.network.play.client.CPacketEnchantItem

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149537_d()|int
| func_149539_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketConfirmTransaction

|Class
|--
|net.minecraft.network.play.client.CPacketConfirmTransaction

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149532_c()|int
| func_149533_d()|short
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketUseEntity

|Class
|--
|net.minecraft.network.play.client.CPacketUseEntity

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayServer n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149564_a(World w)|Entity
| func_149565_c()|CPacketUseEntity$Action
| func_179712_b()|Vec3d
| func_186994_b()|EnumHand
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketTabComplete

|Class
|--
|net.minecraft.network.play.client.CPacketTabComplete

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayServer n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149419_c()|String
| func_179709_b()|BlockPos
| func_186989_c()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketClientStatus

|Class
|--
|net.minecraft.network.play.client.CPacketClientStatus

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149435_c()|CPacketClientStatus$State
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketUpdateSign

|Class
|--
|net.minecraft.network.play.client.CPacketUpdateSign

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayServer n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_179722_a()|BlockPos
| func_187017_b()|String[]
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketCreativeInventoryAction

|Class
|--
|net.minecraft.network.play.client.CPacketCreativeInventoryAction

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149625_d()|ItemStack
| func_149627_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketPlayerDigging

|Class
|--
|net.minecraft.network.play.client.CPacketPlayerDigging

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayServer n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_179714_b()|EnumFacing
| func_179715_a()|BlockPos
| func_180762_c()|CPacketPlayerDigging$Action
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketPlayerTryUseItem

|Class
|--
|net.minecraft.network.play.client.CPacketPlayerTryUseItem

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_187028_a()|EnumHand
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketPlayer

|Class
|--
|net.minecraft.network.play.client.CPacketPlayer

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149465_i()|boolean
| func_186996_b(double d)|double
| func_186997_a(double d)|double
| func_186998_b(float f)|float
| func_186999_a(float f)|float
| func_187000_c(double d)|double
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketPlayerAbilities

|Class
|--
|net.minecraft.network.play.client.CPacketPlayerAbilities

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149483_b(boolean b)|void
| func_149484_f()|boolean
| func_149485_a(float f)|void
| func_149486_e()|boolean
| func_149488_d()|boolean
| func_149490_a(boolean b)|void
| func_149491_c(boolean b)|void
| func_149492_b(float f)|void
| func_149493_d(boolean b)|void
| func_149494_c()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketCustomPayload

|Class
|--
|net.minecraft.network.play.client.CPacketCustomPayload

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayServer n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149559_c()|String
| func_180760_b()|PacketBuffer
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketClickWindow

|Class
|--
|net.minecraft.network.play.client.CPacketClickWindow

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayServer n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149543_e()|int
| func_149544_d()|int
| func_149546_g()|ItemStack
| func_149547_f()|short
| func_149548_c()|int
| func_186993_f()|ClickType
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketKeepAlive

|Class
|--
|net.minecraft.network.play.client.CPacketKeepAlive

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149460_c()|long
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketChatMessage

|Class
|--
|net.minecraft.network.play.client.CPacketChatMessage

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149439_c()|String
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketHeldItemChange

|Class
|--
|net.minecraft.network.play.client.CPacketHeldItemChange

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149614_c()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketCloseWindow

|Class
|--
|net.minecraft.network.play.client.CPacketCloseWindow

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketEntityAction

|Class
|--
|net.minecraft.network.play.client.CPacketEntityAction

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149512_e()|int
| func_180764_b()|CPacketEntityAction$Action
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketInput

|Class
|--
|net.minecraft.network.play.client.CPacketInput

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayServer n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_149617_f()|boolean
| func_149618_e()|boolean
| func_149620_c()|float
| func_192620_b()|float
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketResourcePackStatus

|Class
|--
|net.minecraft.network.play.client.CPacketResourcePackStatus

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketAnimation

|Class
|--
|net.minecraft.network.play.client.CPacketAnimation

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_187018_a()|EnumHand
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketSpectate

|Class
|--
|net.minecraft.network.play.client.CPacketSpectate

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_179727_a(WorldServer w)|Entity
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketPlayerTryUseItemOnBlock

|Class
|--
|net.minecraft.network.play.client.CPacketPlayerTryUseItemOnBlock

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayServer n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_187020_f()|float
| func_187022_c()|EnumHand
| func_187023_a()|BlockPos
| func_187024_b()|EnumFacing
| func_187025_e()|float
| func_187026_d()|float
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketVehicleMove

|Class
|--
|net.minecraft.network.play.client.CPacketVehicleMove

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayServer n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_187002_b()|double
| func_187003_c()|double
| func_187004_a()|double
| func_187005_e()|float
| func_187006_d()|float
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketConfirmTeleport

|Class
|--
|net.minecraft.network.play.client.CPacketConfirmTeleport

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_186987_a()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketSteerBoat

|Class
|--
|net.minecraft.network.play.client.CPacketSteerBoat

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayServer n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_187012_a()|boolean
| func_187014_b()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketRecipeInfo

|Class
|--
|net.minecraft.network.play.client.CPacketRecipeInfo

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayServer n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_192624_c()|boolean
| func_192625_d()|boolean
| func_193648_b()|Recipe
| func_194156_a()|CPacketRecipeInfo$Purpose
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketSeenAdvancements

|Class
|--
|net.minecraft.network.play.client.CPacketSeenAdvancements

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandlerPlayServer n)|void
| func_148833_a(NetHandler n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_194162_b()|CPacketSeenAdvancements$Action
| func_194165_c()|ResourceLocation
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketPlaceRecipe

|Class
|--
|net.minecraft.network.play.client.CPacketPlaceRecipe

---

|Extends
|--
|Packet

---

|Methods|Return Type
|--|--
| func_148833_a(NetHandler n)|void
| func_148833_a(NetHandlerPlayServer n)|void
| func_148837_a(PacketBuffer p)|void
| func_148840_b(PacketBuffer p)|void
| func_194317_b()|Recipe
| func_194318_a()|int
| func_194319_c()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TupleIntJsonSerializable

|Class
|--
|net.minecraft.util.TupleIntJsonSerializable

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_151187_b()|JsonSerializable
| func_151188_a(int i)|void
| func_151189_a()|int
| func_151190_a(JsonSerializable j)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TeleporterDimPos

|Class
|--
|com.feed_the_beast.ftblib.lib.math.TeleporterDimPos

---

|Extends
|--
|Teleporter

---

|Fields|Type
|--|--
|  dim|int
|  posX|double
|  posY|double
|  posZ|double
|  vanilla|boolean

---

|Methods|Return Type
|--|--
| block()|BlockDimPos
| placeEntity(World arg0, Entity arg1, float arg2)|void
| teleport(Entity e)|Entity
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ChunkDimPos

|Class
|--
|com.feed_the_beast.ftblib.lib.math.ChunkDimPos

---

|Extends
|--

---

|Fields|Type
|--|--
|  blockX|int
|  blockZ|int
|  chunkPos|ChunkPos
|  dim|int
|  posX|int
|  posZ|int

---

|Methods|Return Type
|--|--
| equalsChunkDimPos(ChunkDimPos c)|boolean
| getBlockPos(int i)|BlockDimPos
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## IntListIterator

|Interface
|--
|it.unimi.dsi.fastutil.ints.IntListIterator

---

|Extends
|--
|ListIterator
|IntBidirectionalIterator

---

|Methods|Return Type
|--|--
| add(int i)|void
| add(Object o)|void
| back(int i)|int
| forEachRemaining(Consumer\<? super E> c)|void
| hasNext()|boolean
| hasNext()|boolean
| hasPrevious()|boolean
| hasPrevious()|boolean
| next()|Object
| next()|Object
| nextIndex()|int
| nextInt()|int
| previous()|Object
| previous()|Object
| previousIndex()|int
| previousInt()|int
| remove()|void
| remove()|void
| set(int i)|void
| set(Object o)|void
| skip(int i)|int
| skip(int i)|int

---

## ServerPlayer

|Class
|--
|dev.latvian.kubejs.player.ServerPlayerJS

---

|Extends
|--
|Player

---

|Fields|Type
|--|--
|  absorptionAmount|float
|  alive|boolean
|  ambientCreature|boolean
|  animal|boolean
|  attackingEntity|LivingEntity
|  block Block position of the entity|Block
|  boss|boolean
|  child|boolean
|  creativeMode|boolean
|  customName Custom display name|String
|  customNameAlwaysVisible Custom display name will always be visible above head|boolean
|  data Temporary data, mods can attach objects to this|AttachedData
|  displayName|Text
|  elytraFlying|boolean
|  eyeHeight|float
|  facing|EnumFacing
|  fake|boolean
|  fallDistance|float
|  foodLevel|int
|  frame|boolean
|  fullNBT Entity NBT|NBTCompound
|  glowing|boolean
|  hasCustomName Checks if custom display name is set|boolean
|  health|float
|  horizontalFacing|EnumFacing
|  id|UUID
|  idleTime|int
|  inventory|Inventory
|  invisible|boolean
|  item|ItemStack
|  lastAttackedEntity|LivingEntity
|  lastAttackedEntityTime|int
|  lastDamageSource|DamageSource
|  living|boolean
|  mainHandItem|ItemStack
|  maxHealth|float
|  minecraftEntity|Entity
|  minecraftLivingEntity|EntityLivingBase
|  minecraftPlayer|EntityPlayer
|  miningBlock|boolean
|  monster|boolean
|  motionX|double
|  motionY|double
|  motionZ|double
|  mouseItem|ItemStack
|  movementSpeed|float
|  name|String
|  nbt|NBTCompound
|  noClip|boolean
|  noGravity|boolean
|  offHandItem|ItemStack
|  onGround|boolean
|  onLadder|boolean
|  oP|boolean
|  openInventory|Container
|  passengers|EntityArrayList
|  pitch|float
|  player|boolean
|  potionEffects|EntityPotionEffects
|  profile|GameProfile
|  reachDistance|double
|  recursivePassengers|EntityArrayList
|  revengeTarget|LivingEntity
|  revengeTimer|int
|  ridingEntity|Entity
|  selectedSlot|int
|  server|Server
|  silent|boolean
|  sleeping|boolean
|  sneaking|boolean
|  spectator|boolean
|  sprinting|boolean
|  stats|PlayerStats
|  stepHeight|float
|  tags|Set\<String>
|  teamID Scoreboard team ID|String
|  ticksExisted|int
|  type|ID
|  undead|boolean
|  waterCreature|boolean
|  world|World
|  x|double
|  xp|int
|  xpLevel|int
|  y|double
|  yaw|float
|  z|double

---

|Methods|Return Type
|--|--
| addExhaustion(float f)|void
| addFood(int food, float modifier)|void
| addMotion(double x, double y, double z)|void
| addXP(int xp)|void
| addXPLevels(int levels)|void
| attack(float hp)|void
| attack(String source, float hp)|void
| ban(String arg0, String arg1, long arg2)|void
| boostElytraFlight()|void
| canEntityBeSeen(Entity entity)|boolean
| closeInventory()|void
| closeOverlay(String s)|void
| closeOverlay(Overlay o)|void
| damageHeldItem()|void
| damageHeldItem(EnumHand hand, int amount)|void
| dismountRidingEntity()|void
| extinguish()|void
| getEquipment(EntityEquipmentSlot slot)|ItemStack
| getHeldItem(EnumHand hand)|ItemStack
| getNBTData(String key) Get specific value from custom NBT|NBTBase
| give(ItemStack item)|void
| giveInHand(ItemStack item)|void
| hasClientMod()|boolean
| heal(float hp)|void
| isHoldingInAnyHand(Ingredient ingredient)|boolean
| isOnSameTeam(Entity entity) Checks if this entity is on the same scoreboard team as another entity|boolean
| isOnScoreboardTeam(String teamID) Checks if this entity is on scoreboard team|boolean
| isPassenger(Entity entity)|boolean
| kick()|void
| kick(Text t)|void
| kill()|void
| openOverlay(Overlay o)|void
| playSound(Object id, float volume, float pitch) Play sound at entity. Must be played from server side|void
| playSound(Object id) Play sound at entity. Must be played from server side|void
| rayTrace()|Map\<String, Object>
| rayTrace(double distance)|Map\<String, Object>
| removePassengers()|void
| revokeAdvancement(Object o)|void
| runCommand(String command) Runs command as if the sender was running it, ignoring permissions|int
| sendData(String channel, Object data)|void
| sendInventoryUpdate()|void
| setEquipment(EntityEquipmentSlot slot, ItemStack item)|void
| setHeldItem(EnumHand hand, ItemStack item)|void
| setMotion(double x, double y, double z)|void
| setNBTData(String key, Object nbt) Set specific value in custom NBT|void
| setOnFire(int seconds) Sets entity on fire for x seconds|void
| setPosition(double x, double y, double z)|void
| setPosition(Block block)|void
| setPositionAndRotation(double x, double y, double z, float yaw, float pitch)|void
| setRotation(float yaw, float pitch)|void
| setStatusMessage(Object message)|void
| spawn()|void
| startRiding(Entity entity, boolean force)|boolean
| swingArm(EnumHand hand)|void
| tell(Text message) Tell message in chat|void
| unlockAdvancement(Object o)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## VillageDoorInfo

|Class
|--
|net.minecraft.village.VillageDoorInfo

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_179846_b(BlockPos b)|int
| func_179847_f()|int
| func_179848_a(BlockPos b)|int
| func_179849_a(int i)|void
| func_179850_c(BlockPos b)|boolean
| func_179851_i()|boolean
| func_179852_d()|BlockPos
| func_179853_a(boolean b)|void
| func_179855_g()|int
| func_179856_e()|BlockPos
| func_188567_j()|EnumFacing
| func_75466_d()|void
| func_75468_f()|int
| func_75470_e()|void
| func_75473_b()|int
| func_75474_b(int arg0, int arg1, int arg2)|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockStateContainer

|Class
|--
|net.minecraft.world.chunk.BlockStateContainer

---

|Extends
|--
|BlockStatePaletteResizer

---

|Methods|Return Type
|--|--
| func_186008_a(int arg0, BlockState arg1)|int
| func_186009_b(PacketBuffer p)|void
| func_186010_a(PacketBuffer p)|void
| func_186013_a(int arg0, int arg1, int arg2, BlockState arg3)|void
| func_186016_a(int arg0, int arg1, int arg2)|BlockState
| func_186017_a(byte[] arg0, NibbleArray arg1)|NibbleArray
| func_186018_a()|int
| func_186019_a(byte[] arg0, NibbleArray arg1, NibbleArray arg2)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## NibbleArray

|Class
|--
|net.minecraft.world.chunk.NibbleArray

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_177480_a(int i)|int
| func_177481_a()|byte[]
| func_177482_a(int arg0, int arg1)|void
| func_76581_a(int arg0, int arg1, int arg2, int arg3)|void
| func_76582_a(int arg0, int arg1, int arg2)|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WorldGenFlowers

|Class
|--
|net.minecraft.world.gen.feature.WorldGenFlowers

---

|Extends
|--
|WorldGenerator

---

|Methods|Return Type
|--|--
| func_175904_e()|void
| func_175914_a(BlockFlower arg0, BlockFlower$EnumFlowerType arg1)|void
| func_180709_b(World arg0, Random arg1, BlockPos arg2)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BlockFlower$EnumFlowerColor

|Class
|--
|net.minecraft.block.BlockFlower$EnumFlowerColor

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_180346_a()|BlockFlower
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## LootPool

|Class
|--
|net.minecraft.world.storage.loot.LootPool

---

|Extends
|--

---

|Fields|Type
|--|--
|  bonusRolls|RandomValueRange
|  field_186453_a|List\<LootEntry>
|  frozen|boolean
|  name|String
|  rolls|RandomValueRange

---

|Methods|Return Type
|--|--
| addEntry(LootEntry l)|void
| freeze()|void
| func_186449_b(Collection\<ItemStack> arg0, Random arg1, LootContext arg2)|void
| getEntry(String s)|LootEntry
| removeEntry(String s)|LootEntry
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## LootContext

|Class
|--
|net.minecraft.world.storage.loot.LootContext

---

|Extends
|--

---

|Fields|Type
|--|--
|  lootingModifier|int
|  world|WorldServer

---

|Methods|Return Type
|--|--
| func_186490_b(LootTable l)|void
| func_186491_f()|float
| func_186492_c()|Entity
| func_186493_a()|Entity
| func_186494_a(LootContext$EntityTarget l)|Entity
| func_186495_b()|Entity
| func_186496_a(LootTable l)|boolean
| func_186497_e()|LootTableManager
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PlacementSettings

|Class
|--
|net.minecraft.world.gen.structure.template.PlacementSettings

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_186212_b()|Mirror
| func_186213_g()|StructureBoundingBox
| func_186214_a(Mirror m)|PlacementSettings
| func_186215_c()|Rotation
| func_186217_a()|PlacementSettings
| func_186218_a(ChunkPos c)|PlacementSettings
| func_186219_f()|Block
| func_186220_a(Rotation r)|PlacementSettings
| func_186221_e()|boolean
| func_186222_a(boolean b)|PlacementSettings
| func_186223_a(StructureBoundingBox s)|PlacementSettings
| func_186225_a(Block b)|PlacementSettings
| func_186226_b(boolean b)|PlacementSettings
| func_186227_h()|boolean
| func_189946_a(float f)|PlacementSettings
| func_189947_a(BlockPos b)|Random
| func_189948_f()|float
| func_189949_a(long l)|PlacementSettings
| func_189950_a(Random r)|PlacementSettings
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TemplateProcessor

|Interface
|--
|net.minecraft.world.gen.structure.template.ITemplateProcessor

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_189943_a(World arg0, BlockPos arg1, Template$BlockInfo arg2)|Template$BlockInfo

---

## FunctionObject$Entry

|Interface
|--
|net.minecraft.command.FunctionObject$Entry

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_194145_a(FunctionManager arg0, CommandSender arg1, ArrayDeque\<FunctionManager$QueuedCommand> arg2, int arg3)|void

---

## Int2IntMap

|Interface
|--
|it.unimi.dsi.fastutil.ints.Int2IntMap

---

|Extends
|--
|Int2IntFunction
|Map

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| clear()|void
| clear()|void
| compute(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| computeIfAbsent(Object arg0, Function\<? super K, ? extends V> arg1)|Object
| computeIfPresent(Object arg0, BiFunction\<? super K, ? super V, ? extends V> arg1)|Object
| containsKey(int i)|boolean
| containsKey(Object o)|boolean
| containsKey(Object o)|boolean
| containsValue(int i)|boolean
| containsValue(Object o)|boolean
| defaultReturnValue(int i)|void
| defaultReturnValue()|int
| entrySet()|ObjectSet\<java.util.Map$Entry\<java.lang.Integer, java.lang.Integer>>
| entrySet()|Set\<java.util.Map$Entry\<K, V>>
| forEach(BiConsumer\<? super K, ? super V> b)|void
| get(int i)|int
| get(Object o)|Object
| get(Object o)|Object
| getOrDefault(Object arg0, Object arg1)|Object
| int2IntEntrySet()|ObjectSet\<Int2IntMap$Entry>
| keySet()|IntSet
| keySet()|Set\<K>
| merge(Object arg0, Object arg1, BiFunction\<? super V, ? super V, ? extends V> arg2)|Object
| put(int arg0, int arg1)|int
| put(Object arg0, Object arg1)|Object
| put(Object arg0, Object arg1)|Object
| putAll(Map\<? extends K, ? extends V> m)|void
| putIfAbsent(Object arg0, Object arg1)|Object
| remove(int i)|int
| remove(Object o)|Object
| remove(Object o)|Object
| remove(Object arg0, Object arg1)|boolean
| replace(Object arg0, Object arg1)|Object
| replace(Object arg0, Object arg1, Object arg2)|boolean
| replaceAll(BiFunction\<? super K, ? super V, ? extends V> b)|void
| size()|int
| size()|int
| values()|IntCollection
| values()|Collection\<V>

---

## Animals

|Interface
|--
|net.minecraft.entity.passive.IAnimals

---

|Extends
|--

---

## EntityCreature

|Class
|--
|net.minecraft.entity.EntityCreature

---

|Extends
|--
|EntityLiving

---

|Fields|Type
|--|--
|  addedToWorld|boolean
|  capturedDrops|ArrayList\<EntityItem>
|  captureDrops|boolean
|  entityData|NBTTagCompound
|  field_110153_bc|float
|  field_110158_av|int
|  field_181016_an|BlockPos
|  field_184239_as|Entity
|  field_184617_aD|int
|  field_184618_aE|float
|  field_184619_aG|float
|  field_184622_au|EnumHand
|  field_184627_bm|ItemStack
|  field_184628_bn|int
|  field_190534_ay|int
|  field_191988_bg|float
|  field_70116_cv|long
|  field_70117_cu|long
|  field_70118_ct|long
|  field_70122_E|boolean
|  field_70123_F|boolean
|  field_70124_G|boolean
|  field_70125_A|float
|  field_70126_B|float
|  field_70127_C|float
|  field_70128_L|boolean
|  field_70130_N|float
|  field_70131_O|float
|  field_70132_H|boolean
|  field_70133_I|boolean
|  field_70136_U|double
|  field_70137_T|double
|  field_70138_W|float
|  field_70140_Q|float
|  field_70141_P|float
|  field_70142_S|double
|  field_70143_R|float
|  field_70144_Y|float
|  field_70145_X|boolean
|  field_70156_m|boolean
|  field_70158_ak|boolean
|  field_70159_w|double
|  field_70160_al|boolean
|  field_70161_v|double
|  field_70162_ai|int
|  field_70163_u|double
|  field_70164_aj|int
|  field_70165_t|double
|  field_70166_s|double
|  field_70167_r|double
|  field_70169_q|double
|  field_70170_p|World
|  field_70172_ad|int
|  field_70173_aa|int
|  field_70175_ag|boolean
|  field_70176_ah|int
|  field_70177_z|float
|  field_70178_ae|boolean
|  field_70179_y|double
|  field_70180_af|EntityDataManager
|  field_70181_x|double
|  field_70696_bz|EntityLivingBase
|  field_70701_bs|float
|  field_70702_br|float
|  field_70703_bu|boolean
|  field_70704_bt|float
|  field_70714_bg|EntityAITasks
|  field_70715_bh|EntityAITasks
|  field_70718_bc|int
|  field_70720_be|int
|  field_70721_aZ|float
|  field_70725_aQ|int
|  field_70726_aT|float
|  field_70727_aS|float
|  field_70728_aV|int
|  field_70732_aI|float
|  field_70733_aJ|float
|  field_70737_aN|int
|  field_70738_aO|int
|  field_70739_aP|float
|  field_70747_aH|float
|  field_70755_b|EntityLivingBase
|  field_70757_a|int
|  field_70758_at|float
|  field_70759_as|float
|  field_70760_ar|float
|  field_70761_aq|float
|  field_70769_ao|float
|  field_70770_ap|float
|  field_70771_an|int
|  field_71087_bX|boolean
|  field_71088_bW|int
|  field_71093_bK|int
|  field_82151_R|float
|  field_82153_h|int
|  field_82175_bq|boolean
|  field_98038_p|boolean
|  itemInUseMaxDuration|int
|  persistentID|UUID
|  updateBlocked|boolean

---

|Methods|Return Type
|--|--
| canRiderInteract()|boolean
| canTrample(World arg0, Block arg1, BlockPos arg2, float arg3)|boolean
| changeDimension(int arg0, Teleporter arg1)|Entity
| curePotionEffects(ItemStack i)|void
| deserializeNBT(NBTTagCompound n)|void
| deserializeNBT(NBTBase n)|void
| func_104002_bU()|boolean
| func_110124_au()|UUID
| func_110138_aP()|float
| func_110139_bj()|float
| func_110140_aT()|AbstractAttributeMap
| func_110142_aN()|CombatTracker
| func_110143_aJ()|float
| func_110144_aD()|EntityLivingBase
| func_110145_l(Entity e)|void
| func_110148_a(Attribute a)|AttributeInstance
| func_110149_m(float f)|void
| func_110160_i(boolean arg0, boolean arg1)|void
| func_110162_b(Entity arg0, boolean arg1)|void
| func_110163_bv()|void
| func_110166_bE()|Entity
| func_110167_bD()|boolean
| func_110173_bK()|boolean
| func_110174_bM()|float
| func_110175_bO()|boolean
| func_110177_bN()|void
| func_130011_c(Entity e)|void
| func_130014_f_()|World
| func_142013_aG()|int
| func_142015_aE()|int
| func_145747_a(TextComponent t)|void
| func_145748_c_()|TextComponent
| func_145769_d(int i)|void
| func_145770_h(double arg0, double arg1, double arg2)|boolean
| func_145773_az()|boolean
| func_145778_a(Item arg0, int arg1, float arg2)|EntityItem
| func_145779_a(Item arg0, int arg1)|EntityItem
| func_145782_y()|int
| func_145818_k_()|boolean
| func_152111_bt()|void
| func_152112_bu()|void
| func_174791_d()|Vec3d
| func_174792_t_()|boolean
| func_174793_f()|Entity
| func_174794_a(CommandResultStats$Type arg0, int arg1)|void
| func_174805_g(boolean b)|void
| func_174807_aT()|CommandResultStats
| func_174810_b(boolean b)|void
| func_174811_aO()|EnumFacing
| func_174812_G()|void
| func_174813_aQ()|AxisAlignedBB
| func_174814_R()|boolean
| func_174816_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3, float arg4)|boolean
| func_174817_o(Entity e)|void
| func_174818_b(BlockPos b)|double
| func_174820_d(int arg0, ItemStack arg1)|boolean
| func_174821_h(boolean b)|void
| func_174822_a(double arg0, float arg1)|RayTraceResult
| func_174824_e(float f)|Vec3d
| func_174826_a(AxisAlignedBB a)|void
| func_174827_a(EntityPlayerMP e)|boolean
| func_174828_a(BlockPos arg0, float arg1, float arg2)|void
| func_174829_m()|void
| func_174830_Y()|void
| func_174831_c(BlockPos b)|double
| func_174832_aS()|boolean
| func_174833_aM()|boolean
| func_175446_cd()|boolean
| func_175449_a(BlockPos arg0, int arg1)|void
| func_180425_c()|BlockPos
| func_180426_a(double arg0, double arg1, double arg2, float arg3, float arg4, int arg5, boolean arg6)|void
| func_180427_aV()|boolean
| func_180428_a(Explosion arg0, World arg1, BlockPos arg2, BlockState arg3)|float
| func_180430_e(float arg0, float arg1)|void
| func_180431_b(DamageSource d)|boolean
| func_180432_n(Entity e)|void
| func_180482_a(DifficultyInstance arg0, EntityLivingData arg1)|EntityLivingData
| func_180484_a(BlockPos b)|float
| func_180485_d(BlockPos b)|boolean
| func_180486_cf()|BlockPos
| func_180799_ab()|boolean
| func_181012_aH()|EnumFacing
| func_181013_g(float f)|void
| func_181014_aG()|Vec3d
| func_181015_d(BlockPos b)|void
| func_184102_h()|MinecraftServer
| func_184172_bi()|EnumFacing
| func_184174_b(boolean b)|void
| func_184176_by()|SoundCategory
| func_184177_bl()|AxisAlignedBB
| func_184178_b(EntityPlayerMP e)|void
| func_184179_bs()|Entity
| func_184180_b(Class\<T> c)|Collection\<T>
| func_184182_bu()|Collection\<Entity>
| func_184185_a(SoundEvent arg0, float arg1, float arg2)|void
| func_184186_bw()|boolean
| func_184187_bx()|Entity
| func_184188_bt()|List\<Entity>
| func_184189_br()|boolean
| func_184190_l(Entity e)|void
| func_184191_r(Entity e)|boolean
| func_184192_z()|EnumPushReaction
| func_184193_aE()|Iterable\<ItemStack>
| func_184194_a(Team t)|boolean
| func_184195_f(boolean b)|void
| func_184196_w(Entity e)|boolean
| func_184197_b(String s)|boolean
| func_184198_c(NBTTagCompound n)|boolean
| func_184199_a(EntityPlayer arg0, Vec3d arg1, EnumHand arg2)|EnumActionResult
| func_184201_a(EntityEquipmentSlot arg0, ItemStack arg1)|void
| func_184202_aL()|boolean
| func_184203_c(EntityPlayerMP e)|void
| func_184204_a(int i)|Entity
| func_184205_a(Entity arg0, boolean arg1)|boolean
| func_184206_a(DataParameter\<?> d)|void
| func_184207_aI()|boolean
| func_184208_bv()|Entity
| func_184209_aF()|Iterable\<ItemStack>
| func_184210_p()|void
| func_184211_a(String s)|boolean
| func_184212_Q()|EntityDataManager
| func_184213_bq()|boolean
| func_184214_aD()|Iterable\<ItemStack>
| func_184215_y(Entity e)|boolean
| func_184216_O()|Set\<String>
| func_184217_a(Mirror m)|float
| func_184218_aH()|boolean
| func_184220_m(Entity e)|boolean
| func_184221_a(UUID u)|void
| func_184222_aU()|boolean
| func_184223_x(Entity e)|boolean
| func_184224_h(boolean b)|void
| func_184226_ay()|void
| func_184229_a(Rotation r)|float
| func_184230_a(EntityPlayer arg0, EnumHand arg1)|boolean
| func_184232_k(Entity e)|void
| func_184582_a(EntityEquipmentSlot e)|ItemStack
| func_184583_d(DamageSource d)|boolean
| func_184585_cz()|boolean
| func_184586_b(EnumHand e)|ItemStack
| func_184587_cr()|boolean
| func_184589_d(Potion p)|void
| func_184591_cq()|EnumHandSide
| func_184592_cb()|ItemStack
| func_184595_k(double arg0, double arg1, double arg2)|boolean
| func_184596_c(Potion p)|PotionEffect
| func_184597_cx()|void
| func_184598_c(EnumHand e)|void
| func_184599_cB()|int
| func_184600_cs()|EnumHand
| func_184602_cy()|void
| func_184603_cC()|boolean
| func_184605_cv()|int
| func_184607_cu()|ItemStack
| func_184609_a(EnumHand e)|void
| func_184611_a(EnumHand arg0, ItemStack arg1)|void
| func_184612_cw()|int
| func_184613_cA()|boolean
| func_184614_ca()|ItemStack
| func_184638_cS()|boolean
| func_184641_n(boolean b)|void
| func_184642_a(EntityEquipmentSlot arg0, float arg1)|void
| func_184643_a(PathNodeType p)|float
| func_184644_a(PathNodeType arg0, float arg1)|void
| func_184646_p(float f)|void
| func_184649_cE()|int
| func_184652_a(EntityPlayer e)|boolean
| func_189511_e(NBTTagCompound n)|NBTTagCompound
| func_189512_bd()|String
| func_189651_aD()|Vec3d
| func_189652_ae()|boolean
| func_189653_aC()|Vec2f
| func_189654_d(boolean b)|void
| func_189748_bU()|DamageSource
| func_190530_aW()|boolean
| func_190630_a(EntityEquipmentSlot e)|boolean
| func_190631_cK()|boolean
| func_191953_am()|boolean
| func_191956_a(Entity arg0, int arg1, DamageSource arg2)|void
| func_191958_b(float arg0, float arg1, float arg2, float arg3)|void
| func_191986_a(float arg0, float arg1, float arg2)|void
| func_191987_a(BlockPos arg0, boolean arg1)|void
| func_191989_p(float f)|void
| func_193076_bZ()|Map\<Potion, PotionEffect>
| func_70003_b(int arg0, String arg1)|boolean
| func_70005_c_()|String
| func_70011_f(double arg0, double arg1, double arg2)|double
| func_70012_b(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70013_c()|float
| func_70014_b(NBTTagCompound n)|void
| func_70015_d(int i)|void
| func_70016_h(double arg0, double arg1, double arg2)|void
| func_70020_e(NBTTagCompound n)|void
| func_70021_al()|Entity[]
| func_70024_g(double arg0, double arg1, double arg2)|void
| func_70026_G()|boolean
| func_70027_ad()|boolean
| func_70028_i(Entity e)|boolean
| func_70029_a(World w)|void
| func_70030_z()|void
| func_70031_b(boolean b)|void
| func_70032_d(Entity e)|float
| func_70033_W()|double
| func_70034_d(float f)|void
| func_70037_a(NBTTagCompound n)|void
| func_70038_c(double arg0, double arg1, double arg2)|boolean
| func_70039_c(NBTTagCompound n)|boolean
| func_70040_Z()|Vec3d
| func_70042_X()|double
| func_70045_F()|boolean
| func_70046_E()|AxisAlignedBB
| func_70047_e()|float
| func_70050_g(int i)|void
| func_70051_ag()|boolean
| func_70055_a(Material m)|boolean
| func_70057_ab()|void
| func_70058_J()|boolean
| func_70066_B()|void
| func_70067_L()|boolean
| func_70068_e(Entity e)|double
| func_70070_b()|int
| func_70071_h_()|void
| func_70072_I()|boolean
| func_70074_a(EntityLivingBase e)|void
| func_70075_an()|boolean
| func_70077_a(EntityLightningBolt e)|void
| func_70079_am()|float
| func_70080_a(double arg0, double arg1, double arg2, float arg3, float arg4)|void
| func_70082_c(float arg0, float arg1)|void
| func_70086_ai()|int
| func_70089_S()|boolean
| func_70090_H()|boolean
| func_70091_d(MoverType arg0, double arg1, double arg2, double arg3)|void
| func_70092_e(double arg0, double arg1, double arg2)|double
| func_70093_af()|boolean
| func_70094_T()|boolean
| func_70095_a(boolean b)|void
| func_70097_a(DamageSource arg0, float arg1)|boolean
| func_70098_U()|void
| func_70099_a(ItemStack arg0, float arg1)|EntityItem
| func_70100_b_(EntityPlayer e)|void
| func_70103_a(byte b)|void
| func_70104_M()|boolean
| func_70106_y()|void
| func_70107_b(double arg0, double arg1, double arg2)|void
| func_70108_f(Entity e)|void
| func_70110_aj()|void
| func_70111_Y()|float
| func_70112_a(double d)|boolean
| func_70114_g(Entity e)|AxisAlignedBB
| func_70601_bi()|boolean
| func_70603_bj()|float
| func_70604_c(EntityLivingBase e)|void
| func_70605_aq()|EntityMoveHelper
| func_70606_j(float f)|void
| func_70608_bn()|boolean
| func_70613_aW()|boolean
| func_70615_aA()|void
| func_70617_f_()|boolean
| func_70624_b(EntityLivingBase e)|void
| func_70625_a(Entity arg0, float arg1, float arg2)|void
| func_70627_aG()|int
| func_70631_g_()|boolean
| func_70634_a(double arg0, double arg1, double arg2)|void
| func_70635_at()|EntitySenses
| func_70636_d()|void
| func_70637_d(boolean b)|void
| func_70638_az()|EntityLivingBase
| func_70641_bl()|int
| func_70642_aH()|void
| func_70643_av()|EntityLivingBase
| func_70644_a(Potion p)|boolean
| func_70645_a(DamageSource d)|void
| func_70646_bf()|int
| func_70648_aU()|boolean
| func_70651_bq()|Collection\<PotionEffect>
| func_70652_k(Entity e)|boolean
| func_70653_a(Entity arg0, float arg1, double arg2, double arg3)|void
| func_70654_ax()|int
| func_70656_aK()|void
| func_70657_f(float f)|void
| func_70658_aO()|int
| func_70659_e(float f)|void
| func_70660_b(Potion p)|PotionEffect
| func_70661_as()|PathNavigate
| func_70662_br()|boolean
| func_70668_bt()|EnumCreatureAttribute
| func_70669_a(ItemStack i)|void
| func_70671_ap()|EntityLookHelper
| func_70674_bp()|void
| func_70676_i(float f)|Vec3d
| func_70678_g(float f)|float
| func_70681_au()|Random
| func_70683_ar()|EntityJumpHelper
| func_70685_l(Entity e)|boolean
| func_70686_a(Class\<? extends net.minecraft.entity.EntityLivingBase> c)|boolean
| func_70687_e(PotionEffect p)|boolean
| func_70689_ay()|float
| func_70690_d(PotionEffect p)|void
| func_70691_i(float f)|void
| func_70781_l()|boolean
| func_71001_a(Entity arg0, int arg1)|void
| func_82142_c(boolean b)|void
| func_82143_as()|int
| func_82145_z()|int
| func_82147_ab()|int
| func_82149_j(Entity e)|void
| func_82150_aj()|boolean
| func_82171_bF()|boolean
| func_85029_a(CrashReportCategory c)|void
| func_85031_j(Entity e)|boolean
| func_85034_r(int i)|void
| func_85035_bI()|int
| func_90999_ad()|boolean
| func_94059_bO()|boolean
| func_94060_bK()|EntityLivingBase
| func_94061_f(boolean b)|void
| func_95999_t()|String
| func_96092_aw()|boolean
| func_96094_a(String s)|void
| func_96124_cp()|Team
| func_98034_c(EntityPlayer e)|boolean
| func_98052_bS()|boolean
| func_98053_h(boolean b)|void
| getCapability(Capability\<T> arg0, EnumFacing arg1)|Object
| getPickedResult(RayTraceResult r)|ItemStack
| hasCapability(Capability\<?> arg0, EnumFacing arg1)|boolean
| isCreatureType(EnumCreatureType arg0, boolean arg1)|boolean
| onAddedToWorld()|void
| onRemovedFromWorld()|void
| resetEntityId()|void
| serializeNBT()|NBTTagCompound
| serializeNBT()|NBTBase
| shouldDismountInWater(Entity e)|boolean
| shouldRenderInPass(int i)|boolean
| shouldRiderFaceForward(EntityPlayer e)|boolean
| shouldRiderSit()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PathPoint

|Class
|--
|net.minecraft.pathfinding.PathPoint

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_186284_j|float
|  field_186285_k|float
|  field_186286_l|float
|  field_186287_m|PathNodeType
|  field_75833_f|float
|  field_75834_g|float
|  field_75835_d|int
|  field_75836_e|float
|  field_75837_b|int
|  field_75838_c|int
|  field_75839_a|int
|  field_75841_h|PathPoint
|  field_75842_i|boolean

---

|Methods|Return Type
|--|--
| func_186281_c(PathPoint p)|float
| func_186283_a(int arg0, int arg1, int arg2)|PathPoint
| func_75829_a(PathPoint p)|float
| func_75831_a()|boolean
| func_75832_b(PathPoint p)|float
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## TexturedQuad

|Class
|--
|net.minecraft.client.model.TexturedQuad

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_78237_b|int
|  field_78239_a|PositionTextureVertex[]

---

|Methods|Return Type
|--|--
| func_178765_a(BufferBuilder arg0, float arg1)|void
| func_78235_a()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ModelResolver

|Interface
|--
|net.optifine.entity.model.anim.IModelResolver

---

|Extends
|--
|ExpressionResolver

---

|Methods|Return Type
|--|--
| getExpression(String s)|Expression
| getModelRenderer(String s)|ModelRenderer
| getModelVariable(String s)|ModelVariableFloat

---

## Screen

|Interface
|--
|com.feed_the_beast.ftbquests.tile.IScreen

---

|Extends
|--
|Paintable

---

|Fields|Type
|--|--
|  offsetX|int
|  offsetY|int
|  offsetZ|int
|  paint|BlockState

---

|Methods|Return Type
|--|--
| paint(BlockState arg0, EnumFacing arg1, boolean arg2)|void

---

## ChangeCallback

|Interface
|--
|com.feed_the_beast.ftblib.lib.tile.IChangeCallback

---

|Extends
|--

---

|Methods|Return Type
|--|--
| onContentsChanged(boolean b)|void

---

## FrameType

|Class
|--
|net.minecraft.advancements.FrameType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_192307_a()|String
| func_192309_b()|int
| func_193229_c()|TextFormatting
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CriterionInstance

|Interface
|--
|net.minecraft.advancements.ICriterionInstance

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_192244_a()|ResourceLocation

---

## ClickEvent$Action

|Class
|--
|net.minecraft.util.text.event.ClickEvent$Action

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_150673_b()|String
| func_150674_a()|boolean
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## HoverEvent$Action

|Class
|--
|net.minecraft.util.text.event.HoverEvent$Action

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_150685_b()|String
| func_150686_a()|boolean
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemTransformVec3f

|Class
|--
|net.minecraft.client.renderer.block.model.ItemTransformVec3f

---

|Extends
|--
|ModelState

---

|Fields|Type
|--|--
|  field_178363_d|Vector3f
|  field_178364_b|Vector3f
|  field_178365_c|Vector3f

---

|Methods|Return Type
|--|--
| apply(Optional\<? extends net.minecraftforge.common.model.IModelPart> o)|Optional\<TRSRTransformation>
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ItemOverride

|Class
|--
|net.minecraft.client.renderer.block.model.ItemOverride

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_188026_a()|ResourceLocation
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SetVisibility

|Class
|--
|net.minecraft.client.renderer.chunk.SetVisibility

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178618_a(boolean b)|void
| func_178619_a(EnumFacing arg0, EnumFacing arg1, boolean arg2)|void
| func_178620_a(Set\<EnumFacing> s)|void
| func_178621_a(EnumFacing arg0, EnumFacing arg1)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ChunkCompileTaskGenerator$Status

|Class
|--
|net.minecraft.client.renderer.chunk.ChunkCompileTaskGenerator$Status

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ChunkCompileTaskGenerator$Type

|Class
|--
|net.minecraft.client.renderer.chunk.ChunkCompileTaskGenerator$Type

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Sound$Type

|Class
|--
|net.minecraft.client.audio.Sound$Type

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ShaderManager

|Class
|--
|net.minecraft.client.shader.ShaderManager

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_147984_b(String s)|ShaderUniform
| func_147985_d()|void
| func_147986_h()|int
| func_147988_a()|void
| func_147989_e()|ShaderLoader
| func_147991_a(String s)|ShaderUniform
| func_147992_a(String arg0, Object arg1)|void
| func_147993_b()|void
| func_147994_f()|ShaderLoader
| func_147995_c()|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## LinkedList$Node

|Class
|--
|net.optifine.util.LinkedList$Node

---

|Extends
|--

---

|Fields|Type
|--|--
|  item|Object
|  next|LinkedList$Node\<T>
|  prev|LinkedList$Node\<T>

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## VboRenderList

|Class
|--
|net.minecraft.client.renderer.VboRenderList

---

|Extends
|--
|ChunkRenderContainer

---

|Methods|Return Type
|--|--
| func_178001_a(BlockRenderLayer b)|void
| func_178002_a(RenderChunk arg0, BlockRenderLayer arg1)|void
| func_178003_a(RenderChunk r)|void
| func_178004_a(double arg0, double arg1, double arg2)|void
| func_178010_a()|void
| preRenderRegion(int arg0, int arg1, int arg2)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## VertexFormatElement$EnumType

|Class
|--
|net.minecraft.client.renderer.vertex.VertexFormatElement$EnumType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_177395_a()|int
| func_177396_b()|String
| func_177397_c()|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## VertexFormatElement$EnumUsage

|Class
|--
|net.minecraft.client.renderer.vertex.VertexFormatElement$EnumUsage

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_177384_a()|String
| name()|String
| ordinal()|int
| postDraw(VertexFormat arg0, int arg1, int arg2, ByteBuffer arg3)|void
| preDraw(VertexFormat arg0, int arg1, int arg2, ByteBuffer arg3)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Function

|Interface
|--
|it.unimi.dsi.fastutil.Function

---

|Extends
|--

---

|Methods|Return Type
|--|--
| clear()|void
| containsKey(Object o)|boolean
| get(Object o)|Object
| put(Object arg0, Object arg1)|Object
| remove(Object o)|Object
| size()|int

---

## LongCollection

|Interface
|--
|it.unimi.dsi.fastutil.longs.LongCollection

---

|Extends
|--
|Collection
|LongIterable

---

|Fields|Type
|--|--
|  empty|boolean

---

|Methods|Return Type
|--|--
| add(long l)|boolean
| add(Object o)|boolean
| addAll(LongCollection l)|boolean
| addAll(Collection\<? extends E> c)|boolean
| clear()|void
| contains(long l)|boolean
| contains(Object o)|boolean
| containsAll(LongCollection l)|boolean
| containsAll(Collection\<?> c)|boolean
| forEach(Consumer\<? super T> c)|void
| iterator()|LongIterator
| iterator()|Iterator\<E>
| iterator()|Iterator\<T>
| longIterator()|LongIterator
| parallelStream()|Stream\<E>
| rem(long l)|boolean
| remove(Object o)|boolean
| removeAll(LongCollection l)|boolean
| removeAll(Collection\<?> c)|boolean
| removeIf(Predicate\<? super E> p)|boolean
| retainAll(LongCollection l)|boolean
| retainAll(Collection\<?> c)|boolean
| size()|int
| spliterator()|Spliterator\<E>
| stream()|Stream\<E>
| toArray(long[] l)|long[]
| toArray(Object[] o)|Object[]
| toArray()|Object[]
| toLongArray()|long[]
| toLongArray(long[] l)|long[]

---

## LongIterator

|Interface
|--
|it.unimi.dsi.fastutil.longs.LongIterator

---

|Extends
|--
|Iterator

---

|Methods|Return Type
|--|--
| forEachRemaining(Consumer\<? super E> c)|void
| hasNext()|boolean
| next()|Object
| nextLong()|long
| remove()|void
| skip(int i)|int

---

## EntityOwnable

|Interface
|--
|net.minecraft.entity.IEntityOwnable

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_184753_b()|UUID
| func_70902_q()|Entity

---

## SpectatorMenuObject

|Interface
|--
|net.minecraft.client.gui.spectator.ISpectatorMenuObject

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178661_a(SpectatorMenu s)|void
| func_178662_A_()|boolean
| func_178663_a(float arg0, int arg1)|void
| func_178664_z_()|TextComponent

---

## SpectatorDetails

|Class
|--
|net.minecraft.client.gui.spectator.categories.SpectatorDetails

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178680_a(int i)|SpectatorMenuObject
| func_178681_b()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## SpectatorMenuView

|Interface
|--
|net.minecraft.client.gui.spectator.ISpectatorMenuView

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_178669_a()|List\<SpectatorMenuObject>
| func_178670_b()|TextComponent

---

## BossInfo

|Class
|--
|net.minecraft.world.BossInfo

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_186734_i()|boolean
| func_186735_a(float f)|void
| func_186736_g()|BossInfo$Color
| func_186737_d()|UUID
| func_186738_f()|float
| func_186739_a(TextComponent t)|void
| func_186740_h()|BossInfo$Overlay
| func_186741_a(boolean b)|BossInfo
| func_186742_b(boolean b)|BossInfo
| func_186743_c(boolean b)|BossInfo
| func_186744_e()|TextComponent
| func_186745_a(BossInfo$Color b)|void
| func_186746_a(BossInfo$Overlay b)|void
| func_186747_j()|boolean
| func_186748_k()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MapData$MapInfo

|Class
|--
|net.minecraft.world.storage.MapData$MapInfo

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_76211_a|EntityPlayer
|  field_82569_d|int

---

|Methods|Return Type
|--|--
| func_176101_a(ItemStack i)|Packet\<?>
| func_176102_a(int arg0, int arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## MapDecoration

|Class
|--
|net.minecraft.world.storage.MapDecoration

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_176110_a()|byte
| func_176111_d()|byte
| func_176112_b()|byte
| func_176113_c()|byte
| func_191179_b()|MapDecoration$Type
| func_191180_f()|boolean
| render(int i)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CriterionProgress

|Class
|--
|net.minecraft.advancements.CriterionProgress

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_192148_e()|JsonElement
| func_192150_a(PacketBuffer p)|void
| func_192151_a()|boolean
| func_192153_b()|void
| func_192154_c()|void
| func_193140_d()|Date
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## AdvancementList$Listener

|Interface
|--
|net.minecraft.advancements.AdvancementList$Listener

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_191928_b(Advancement a)|void
| func_191929_d(Advancement a)|void
| func_191930_a()|void
| func_191931_a(Advancement a)|void
| func_191932_c(Advancement a)|void

---

## SoundSystem

|Class
|--
|paulscode.sound.SoundSystem

---

|Extends
|--

---

|Fields|Type
|--|--
|  listenerData|ListenerData
|  masterVolume|float
|  randomNumberGenerator|Random

---

|Methods|Return Type
|--|--
| activate(String s)|void
| backgroundMusic(String arg0, String arg1, boolean arg2)|void
| backgroundMusic(String arg0, URL arg1, String arg2, boolean arg3)|void
| changeDopplerFactor(float f)|void
| changeDopplerVelocity(float f)|void
| checkFadeVolumes()|void
| cleanup()|void
| CommandQueue(CommandObject c)|boolean
| cull(String s)|void
| dequeueSound(String arg0, String arg1)|void
| fadeOut(String arg0, URL arg1, String arg2, long arg3)|void
| fadeOut(String arg0, String arg1, long arg2)|void
| fadeOutIn(String arg0, String arg1, long arg2, long arg3)|void
| fadeOutIn(String arg0, URL arg1, String arg2, long arg3, long arg4)|void
| feedRawAudioData(String arg0, byte[] arg1)|void
| flush(String s)|void
| getPitch(String s)|float
| getVolume(String s)|float
| interruptCommandThread()|void
| loadSound(URL arg0, String arg1)|void
| loadSound(byte[] arg0, AudioFormat arg1, String arg2)|void
| loadSound(String s)|void
| millisecondsPlayed(String s)|float
| moveListener(float arg0, float arg1, float arg2)|void
| newLibrary(Class c)|boolean
| newSource(boolean arg0, String arg1, String arg2, boolean arg3, float arg4, float arg5, float arg6, int arg7, float arg8)|void
| newSource(boolean arg0, String arg1, URL arg2, String arg3, boolean arg4, float arg5, float arg6, float arg7, int arg8, float arg9)|void
| newStreamingSource(boolean arg0, String arg1, String arg2, boolean arg3, float arg4, float arg5, float arg6, int arg7, float arg8)|void
| newStreamingSource(boolean arg0, String arg1, URL arg2, String arg3, boolean arg4, float arg5, float arg6, float arg7, int arg8, float arg9)|void
| pause(String s)|void
| play(String s)|void
| playing()|boolean
| playing(String s)|boolean
| queueSound(String arg0, String arg1)|void
| queueSound(String arg0, URL arg1, String arg2)|void
| quickPlay(boolean arg0, URL arg1, String arg2, boolean arg3, float arg4, float arg5, float arg6, int arg7, float arg8)|String
| quickPlay(boolean arg0, String arg1, boolean arg2, float arg3, float arg4, float arg5, int arg6, float arg7)|String
| quickStream(boolean arg0, URL arg1, String arg2, boolean arg3, float arg4, float arg5, float arg6, int arg7, float arg8)|String
| quickStream(boolean arg0, String arg1, boolean arg2, float arg3, float arg4, float arg5, int arg6, float arg7)|String
| rawDataStream(AudioFormat arg0, boolean arg1, String arg2, float arg3, float arg4, float arg5, int arg6, float arg7)|void
| removeSource(String s)|void
| removeTemporarySources()|void
| rewind(String s)|void
| setAttenuation(String arg0, int arg1)|void
| setDistOrRoll(String arg0, float arg1)|void
| setListenerAngle(float f)|void
| setListenerOrientation(float arg0, float arg1, float arg2, float arg3, float arg4, float arg5)|void
| setListenerPosition(float arg0, float arg1, float arg2)|void
| setListenerVelocity(float arg0, float arg1, float arg2)|void
| setLooping(String arg0, boolean arg1)|void
| setPitch(String arg0, float arg1)|void
| setPosition(String arg0, float arg1, float arg2, float arg3)|void
| setPriority(String arg0, boolean arg1)|void
| setTemporary(String arg0, boolean arg1)|void
| setVelocity(String arg0, float arg1, float arg2, float arg3)|void
| setVolume(String arg0, float arg1)|void
| stop(String s)|void
| switchLibrary(Class c)|boolean
| turnListener(float f)|void
| unloadSound(String s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ListenerData

|Class
|--
|paulscode.sound.ListenerData

---

|Extends
|--

---

|Fields|Type
|--|--
|  angle|float
|  lookAt|Vector3D
|  position|Vector3D
|  up|Vector3D
|  velocity|Vector3D

---

|Methods|Return Type
|--|--
| setAngle(float f)|void
| setData(ListenerData l)|void
| setData(Vector3D arg0, Vector3D arg1, Vector3D arg2, float arg3)|void
| setData(float arg0, float arg1, float arg2, float arg3, float arg4, float arg5, float arg6, float arg7, float arg8, float arg9)|void
| setOrientation(Vector3D arg0, Vector3D arg1)|void
| setOrientation(float arg0, float arg1, float arg2, float arg3, float arg4, float arg5)|void
| setPosition(Vector3D v)|void
| setPosition(float arg0, float arg1, float arg2)|void
| setVelocity(float arg0, float arg1, float arg2)|void
| setVelocity(Vector3D v)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CommandObject

|Class
|--
|paulscode.sound.CommandObject

---

|Extends
|--

---

|Fields|Type
|--|--
|  boolArgs|boolean[]
|  buffer|byte[]
|  classArgs|Class[]
|  Command|int
|  floatArgs|float[]
|  intArgs|int[]
|  longArgs|long[]
|  objectArgs|Object[]
|  stringArgs|String[]

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## UserList

|Class
|--
|net.minecraft.server.management.UserList

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_152678_f()|void
| func_152683_b(Object o)|UserListEntry
| func_152684_c(Object o)|void
| func_152685_a()|String[]
| func_152686_a(boolean b)|void
| func_152687_a(UserListEntry u)|void
| func_152689_b()|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## UserListEntry

|Class
|--
|net.minecraft.server.management.UserListEntry

---

|Extends
|--

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## UserListIPBansEntry

|Class
|--
|net.minecraft.server.management.UserListIPBansEntry

---

|Extends
|--
|UserListEntryBan

---

|Methods|Return Type
|--|--
| func_73680_d()|Date
| func_73686_f()|String
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Int2ByteFunction

|Interface
|--
|it.unimi.dsi.fastutil.ints.Int2ByteFunction

---

|Extends
|--
|Function

---

|Methods|Return Type
|--|--
| clear()|void
| containsKey(int i)|boolean
| containsKey(Object o)|boolean
| defaultReturnValue(byte b)|void
| defaultReturnValue()|byte
| get(int i)|byte
| get(Object o)|Object
| put(int arg0, byte arg1)|byte
| put(Object arg0, Object arg1)|Object
| remove(int i)|byte
| remove(Object o)|Object
| size()|int

---

## Int2ObjectFunction

|Interface
|--
|it.unimi.dsi.fastutil.ints.Int2ObjectFunction

---

|Extends
|--
|Function

---

|Methods|Return Type
|--|--
| clear()|void
| containsKey(int i)|boolean
| containsKey(Object o)|boolean
| defaultReturnValue(Object o)|void
| defaultReturnValue()|Object
| get(int i)|Object
| get(Object o)|Object
| put(int arg0, Object arg1)|Object
| put(Object arg0, Object arg1)|Object
| remove(int i)|Object
| remove(Object o)|Object
| size()|int

---

## Panel

|Class
|--
|com.feed_the_beast.ftblib.lib.gui.Panel

---

|Extends
|--
|Widget

---

|Fields|Type
|--|--
|  attachedScrollbar|PanelScrollBar
|  contentHeight|int
|  contentHeightExtra|int
|  contentWidth|int
|  contentWidthExtra|int
|  defaultScrollVertical|boolean
|  enabled|boolean
|  gui|GuiBase
|  height|int
|  ingredientUnderMouse|Object
|  mouseOver|boolean
|  mouseOverAnyWidget|boolean
|  mouseX|int
|  mouseY|int
|  offset|boolean
|  onlyInteractWithWidgetsInside|boolean
|  onlyRenderWidgetsInside|boolean
|  parent|Panel
|  partialTicks|float
|  posX|int
|  posY|int
|  screen|ScaledResolution
|  scrollStep|int
|  scrollX|int
|  scrollY|int
|  title|String
|  unicode|boolean
|  widgets|List\<Widget>
|  widgetType|WidgetType
|  width|int
|  x|int
|  y|int

---

|Methods|Return Type
|--|--
| acceptGhostIngredient(Object o)|void
| add(Widget w)|void
| addAll(Iterable\<? extends com.feed_the_beast.ftblib.lib.gui.Widget> i)|void
| addMouseOverText(List\<String> l)|void
| addWidgets()|void
| align(WidgetLayout w)|int
| alignWidgets()|void
| checkMouseOver(int arg0, int arg1)|boolean
| clearWidgets()|void
| closeContextMenu()|void
| closeGui(boolean b)|void
| closeGui()|void
| collidesWith(int arg0, int arg1, int arg2, int arg3)|boolean
| draw(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawBackground(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawOffsetBackground(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawWidget(Theme arg0, Widget arg1, int arg2, int arg3, int arg4, int arg5, int arg6)|void
| getWidget(int i)|Widget
| handleClick(String s)|boolean
| handleClick(String arg0, String arg1)|boolean
| isGhostIngredientTarget(Object o)|boolean
| keyPressed(int arg0, char arg1)|boolean
| keyReleased(int i)|void
| mousePressed(MouseButton m)|boolean
| mouseReleased(MouseButton m)|void
| mouseScrolled(int i)|boolean
| movePanelScroll(int arg0, int arg1)|boolean
| onClosed()|void
| openContextMenu(Panel p)|void
| openGui()|void
| openGuiLater()|void
| refreshWidgets()|void
| run()|void
| scrollPanel(int i)|boolean
| setHeight(int i)|void
| setPos(int arg0, int arg1)|void
| setPosAndSize(int arg0, int arg1, int arg2, int arg3)|Widget
| setSize(int arg0, int arg1)|void
| setWidth(int i)|void
| shouldAddMouseOverText()|boolean
| shouldDraw()|boolean
| tick()|void
| updateMouseOver(int arg0, int arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketUseEntity$Action

|Class
|--
|net.minecraft.network.play.client.CPacketUseEntity$Action

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketClientStatus$State

|Class
|--
|net.minecraft.network.play.client.CPacketClientStatus$State

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketPlayerDigging$Action

|Class
|--
|net.minecraft.network.play.client.CPacketPlayerDigging$Action

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketEntityAction$Action

|Class
|--
|net.minecraft.network.play.client.CPacketEntityAction$Action

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketRecipeInfo$Purpose

|Class
|--
|net.minecraft.network.play.client.CPacketRecipeInfo$Purpose

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## CPacketSeenAdvancements$Action

|Class
|--
|net.minecraft.network.play.client.CPacketSeenAdvancements$Action

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## JsonSerializable

|Interface
|--
|net.minecraft.util.IJsonSerializable

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_151003_a()|JsonElement
| func_152753_a(JsonElement j)|void

---

## IntBidirectionalIterator

|Interface
|--
|it.unimi.dsi.fastutil.ints.IntBidirectionalIterator

---

|Extends
|--
|IntIterator
|ObjectBidirectionalIterator

---

|Methods|Return Type
|--|--
| back(int i)|int
| forEachRemaining(Consumer\<? super E> c)|void
| hasNext()|boolean
| hasPrevious()|boolean
| next()|Object
| nextInt()|int
| previous()|Object
| previousInt()|int
| remove()|void
| skip(int i)|int
| skip(int i)|int

---

## BlockStatePaletteResizer

|Interface
|--
|net.minecraft.world.chunk.IBlockStatePaletteResizer

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_186008_a(int arg0, BlockState arg1)|int

---

## BlockFlower

|Class
|--
|net.minecraft.block.BlockFlower

---

|Extends
|--
|BlockBush

---

|Fields|Type
|--|--
|  delegate|RegistryDelegate\<T>
|  field_149763_I|float
|  field_149765_K|float
|  field_149772_a|CreativeTabs
|  field_149781_w|float
|  field_149782_v|float
|  field_176227_L|BlockStateContainer
|  registryName|ResourceLocation
|  registryType|Class\<T>

---

|Methods|Return Type
|--|--
| addDestroyEffects(World arg0, BlockPos arg1, ParticleManager arg2)|boolean
| addHitEffects(BlockState arg0, World arg1, RayTraceResult arg2, ParticleManager arg3)|boolean
| addLandingEffects(BlockState arg0, WorldServer arg1, BlockPos arg2, BlockState arg3, EntityLivingBase arg4, int arg5)|boolean
| addRunningEffects(BlockState arg0, World arg1, BlockPos arg2, Entity arg3)|boolean
| beginLeavesDecay(BlockState arg0, World arg1, BlockPos arg2)|void
| canBeConnectedTo(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean
| canBeReplacedByLeaves(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| canConnectRedstone(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| canCreatureSpawn(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityLiving$SpawnPlacementType arg3)|boolean
| canEntityDestroy(BlockState arg0, BlockAccess arg1, BlockPos arg2, Entity arg3)|boolean
| canHarvestBlock(BlockAccess arg0, BlockPos arg1, EntityPlayer arg2)|boolean
| canPlaceTorchOnTop(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| canRenderInLayer(BlockState arg0, BlockRenderLayer arg1)|boolean
| canSilkHarvest(World arg0, BlockPos arg1, BlockState arg2, EntityPlayer arg3)|boolean
| canSustainLeaves(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| canSustainPlant(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3, Plantable arg4)|boolean
| createTileEntity(World arg0, BlockState arg1)|TileEntity
| doesSideBlockChestOpening(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| doesSideBlockRendering(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| func_149637_q(BlockState b)|boolean
| func_149638_a(Entity e)|float
| func_149645_b(BlockState b)|EnumBlockRenderType
| func_149647_a(CreativeTabs c)|Block
| func_149652_G()|boolean
| func_149653_t()|boolean
| func_149656_h(BlockState b)|EnumPushReaction
| func_149659_a(Explosion e)|boolean
| func_149662_c(BlockState b)|boolean
| func_149663_c(String s)|Block
| func_149666_a(CreativeTabs arg0, NonNullList\<ItemStack> arg1)|void
| func_149667_c(Block b)|boolean
| func_149675_a(boolean b)|Block
| func_149679_a(int arg0, Random arg1)|int
| func_149686_d(BlockState b)|boolean
| func_149688_o(BlockState b)|Material
| func_149698_L()|boolean
| func_149703_v()|boolean
| func_149708_J()|CreativeTabs
| func_149710_n(BlockState b)|boolean
| func_149711_c(float f)|Block
| func_149713_g(int i)|Block
| func_149715_a(float f)|Block
| func_149716_u()|boolean
| func_149717_k(BlockState b)|int
| func_149721_r(BlockState b)|boolean
| func_149722_s()|Block
| func_149730_j(BlockState b)|boolean
| func_149732_F()|String
| func_149738_a(World w)|int
| func_149739_a()|String
| func_149740_M(BlockState b)|boolean
| func_149744_f(BlockState b)|boolean
| func_149745_a(Random r)|int
| func_149750_m(BlockState b)|int
| func_149751_l(BlockState b)|boolean
| func_149752_b(float f)|Block
| func_176194_O()|BlockStateContainer
| func_176195_g(BlockState arg0, World arg1, BlockPos arg2)|float
| func_176196_c(World arg0, BlockPos arg1)|boolean
| func_176197_a(World arg0, BlockPos arg1, Entity arg2, Vec3d arg3)|Vec3d
| func_176198_a(World arg0, BlockPos arg1, EnumFacing arg2)|boolean
| func_176199_a(World arg0, BlockPos arg1, Entity arg2)|void
| func_176200_f(BlockAccess arg0, BlockPos arg1)|boolean
| func_176201_c(BlockState b)|int
| func_176203_a(int i)|BlockState
| func_176205_b(BlockAccess arg0, BlockPos arg1)|boolean
| func_176206_d(World arg0, BlockPos arg1, BlockState arg2)|void
| func_176208_a(World arg0, BlockPos arg1, BlockState arg2, EntityPlayer arg3)|void
| func_176209_a(BlockState arg0, boolean arg1)|boolean
| func_176211_b(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|int
| func_176213_c(World arg0, BlockPos arg1, BlockState arg2)|void
| func_176214_u(BlockState b)|boolean
| func_176216_a(World arg0, Entity arg1)|void
| func_176218_Q()|Block$EnumOffsetType
| func_176221_a(BlockState arg0, BlockAccess arg1, BlockPos arg2)|BlockState
| func_176223_P()|BlockState
| func_176224_k(World arg0, BlockPos arg1)|void
| func_176225_a(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| func_176226_b(World arg0, BlockPos arg1, BlockState arg2, int arg3)|void
| func_176494_l()|Property\<BlockFlower$EnumFlowerType>
| func_176495_j()|BlockFlower$EnumFlowerColor
| func_180633_a(World arg0, BlockPos arg1, BlockState arg2, EntityLivingBase arg3, ItemStack arg4)|void
| func_180634_a(World arg0, BlockPos arg1, BlockState arg2, Entity arg3)|void
| func_180636_a(BlockState arg0, World arg1, BlockPos arg2, Vec3d arg3, Vec3d arg4)|RayTraceResult
| func_180637_b(World arg0, BlockPos arg1, int arg2)|void
| func_180639_a(World arg0, BlockPos arg1, BlockState arg2, EntityPlayer arg3, EnumHand arg4, EnumFacing arg5, float arg6, float arg7, float arg8)|boolean
| func_180640_a(BlockState arg0, World arg1, BlockPos arg2)|AxisAlignedBB
| func_180641_l(BlockState arg0, World arg1, BlockPos arg2)|int
| func_180642_a(World arg0, BlockPos arg1, EnumFacing arg2, float arg3, float arg4, float arg5, int arg6, EntityLivingBase arg7)|BlockState
| func_180645_a(World arg0, BlockPos arg1, BlockState arg2, Random arg3)|void
| func_180646_a(BlockState arg0, BlockAccess arg1, BlockPos arg2)|AxisAlignedBB
| func_180647_a(BlockState arg0, EntityPlayer arg1, World arg2, BlockPos arg3)|float
| func_180649_a(World arg0, BlockPos arg1, EntityPlayer arg2)|void
| func_180650_b(World arg0, BlockPos arg1, BlockState arg2, Random arg3)|void
| func_180651_a(BlockState b)|int
| func_180652_a(World arg0, BlockPos arg1, Explosion arg2)|void
| func_180653_a(World arg0, BlockPos arg1, BlockState arg2, float arg3, int arg4)|void
| func_180655_c(BlockState arg0, World arg1, BlockPos arg2, Random arg3)|void
| func_180656_a(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|int
| func_180657_a(World arg0, EntityPlayer arg1, BlockPos arg2, BlockState arg3, TileEntity arg4, ItemStack arg5)|void
| func_180658_a(World arg0, BlockPos arg1, Entity arg2, float arg3)|void
| func_180659_g(BlockState arg0, BlockAccess arg1, BlockPos arg2)|MapColor
| func_180660_a(BlockState arg0, Random arg1, int arg2)|Item
| func_180663_b(World arg0, BlockPos arg1, BlockState arg2)|void
| func_180664_k()|BlockRenderLayer
| func_180671_f(World arg0, BlockPos arg1, BlockState arg2)|boolean
| func_181623_g()|boolean
| func_185467_w()|SoundType
| func_185471_a(BlockState arg0, Mirror arg1)|BlockState
| func_185473_a(World arg0, BlockPos arg1, BlockState arg2)|ItemStack
| func_185477_a(BlockState arg0, World arg1, BlockPos arg2, AxisAlignedBB arg3, List\<AxisAlignedBB> arg4, Entity arg5, boolean arg6)|void
| func_185481_k(BlockState b)|boolean
| func_185484_c(BlockState arg0, BlockAccess arg1, BlockPos arg2)|int
| func_185485_f(BlockState b)|float
| func_185496_a(BlockState arg0, BlockAccess arg1, BlockPos arg2)|AxisAlignedBB
| func_185499_a(BlockState arg0, Rotation arg1)|BlockState
| func_189539_a(BlockState arg0, World arg1, BlockPos arg2, int arg3, int arg4)|boolean
| func_189540_a(BlockState arg0, World arg1, BlockPos arg2, Block arg3, BlockPos arg4)|void
| func_189872_a(BlockState arg0, Entity arg1)|boolean
| func_190946_v(BlockState b)|boolean
| func_190948_a(ItemStack arg0, World arg1, List\<String> arg2, TooltipFlag arg3)|void
| func_190949_e(BlockState arg0, BlockAccess arg1, BlockPos arg2)|Vec3d
| func_193383_a(BlockAccess arg0, BlockState arg1, BlockPos arg2, EnumFacing arg3)|BlockFaceShape
| getAiPathNodeType(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityLiving arg3)|PathNodeType
| getAiPathNodeType(BlockState arg0, BlockAccess arg1, BlockPos arg2)|PathNodeType
| getBeaconColorMultiplier(BlockState arg0, World arg1, BlockPos arg2, BlockPos arg3)|float[]
| getBedDirection(BlockState arg0, BlockAccess arg1, BlockPos arg2)|EnumFacing
| getBedSpawnPosition(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityPlayer arg3)|BlockPos
| getBlockLiquidHeight(World arg0, BlockPos arg1, BlockState arg2, Material arg3)|float
| getDrops(BlockAccess arg0, BlockPos arg1, BlockState arg2, int arg3)|List\<ItemStack>
| getDrops(NonNullList\<ItemStack> arg0, BlockAccess arg1, BlockPos arg2, BlockState arg3, int arg4)|void
| getEnchantPowerBonus(World arg0, BlockPos arg1)|float
| getExpDrop(BlockState arg0, BlockAccess arg1, BlockPos arg2, int arg3)|int
| getExplosionResistance(World arg0, BlockPos arg1, Entity arg2, Explosion arg3)|float
| getExtendedState(BlockState arg0, BlockAccess arg1, BlockPos arg2)|BlockState
| getFireSpreadSpeed(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|int
| getFlammability(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|int
| getFogColor(World arg0, BlockPos arg1, BlockState arg2, Entity arg3, Vec3d arg4, float arg5)|Vec3d
| getHarvestLevel(BlockState b)|int
| getHarvestTool(BlockState b)|String
| getLightOpacity(BlockState arg0, BlockAccess arg1, BlockPos arg2)|int
| getLightValue(BlockState arg0, BlockAccess arg1, BlockPos arg2)|int
| getPickBlock(BlockState arg0, RayTraceResult arg1, World arg2, BlockPos arg3, EntityPlayer arg4)|ItemStack
| getPlant(BlockAccess arg0, BlockPos arg1)|BlockState
| getPlantType(BlockAccess arg0, BlockPos arg1)|EnumPlantType
| getSlipperiness(BlockState arg0, BlockAccess arg1, BlockPos arg2, Entity arg3)|float
| getSoundType(BlockState arg0, World arg1, BlockPos arg2, Entity arg3)|SoundType
| getStateAtViewpoint(BlockState arg0, BlockAccess arg1, BlockPos arg2, Vec3d arg3)|BlockState
| getStateForPlacement(World arg0, BlockPos arg1, EnumFacing arg2, float arg3, float arg4, float arg5, int arg6, EntityLivingBase arg7, EnumHand arg8)|BlockState
| getValidRotations(World arg0, BlockPos arg1)|EnumFacing[]
| getWeakChanges(BlockAccess arg0, BlockPos arg1)|boolean
| hasTileEntity(BlockState b)|boolean
| isAABBInsideLiquid(World arg0, BlockPos arg1, AxisAlignedBB arg2)|Boolean
| isAABBInsideMaterial(World arg0, BlockPos arg1, AxisAlignedBB arg2, Material arg3)|Boolean
| isAir(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| isBeaconBase(BlockAccess arg0, BlockPos arg1, BlockPos arg2)|boolean
| isBed(BlockState arg0, BlockAccess arg1, BlockPos arg2, Entity arg3)|boolean
| isBedFoot(BlockAccess arg0, BlockPos arg1)|boolean
| isBurning(BlockAccess arg0, BlockPos arg1)|boolean
| isEntityInsideMaterial(BlockAccess arg0, BlockPos arg1, BlockState arg2, Entity arg3, double arg4, Material arg5, boolean arg6)|Boolean
| isFertile(World arg0, BlockPos arg1)|boolean
| isFireSource(World arg0, BlockPos arg1, EnumFacing arg2)|boolean
| isFlammable(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean
| isFoliage(BlockAccess arg0, BlockPos arg1)|boolean
| isLadder(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityLivingBase arg3)|boolean
| isLeaves(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| isNormalCube(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| isReplaceableOreGen(BlockState arg0, BlockAccess arg1, BlockPos arg2, Predicate\<BlockState> arg3)|boolean
| isSideSolid(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| isStickyBlock(BlockState b)|boolean
| isToolEffective(String arg0, BlockState arg1)|boolean
| isWood(BlockAccess arg0, BlockPos arg1)|boolean
| observedNeighborChange(BlockState arg0, World arg1, BlockPos arg2, Block arg3, BlockPos arg4)|void
| onBlockExploded(World arg0, BlockPos arg1, Explosion arg2)|void
| onNeighborChange(BlockAccess arg0, BlockPos arg1, BlockPos arg2)|void
| onPlantGrow(BlockState arg0, World arg1, BlockPos arg2, BlockPos arg3)|void
| quantityDropped(BlockState arg0, int arg1, Random arg2)|int
| recolorBlock(World arg0, BlockPos arg1, EnumFacing arg2, EnumDyeColor arg3)|boolean
| removedByPlayer(BlockState arg0, World arg1, BlockPos arg2, EntityPlayer arg3, boolean arg4)|boolean
| rotateBlock(World arg0, BlockPos arg1, EnumFacing arg2)|boolean
| setBedOccupied(BlockAccess arg0, BlockPos arg1, EntityPlayer arg2, boolean arg3)|void
| setDefaultSlipperiness(float f)|void
| setHarvestLevel(String arg0, int arg1, BlockState arg2)|void
| setHarvestLevel(String arg0, int arg1)|void
| shouldCheckWeakPower(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## RandomValueRange

|Class
|--
|net.minecraft.world.storage.loot.RandomValueRange

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_186507_b(Random r)|float
| func_186509_a()|float
| func_186510_a(int i)|boolean
| func_186511_a(Random r)|int
| func_186512_b()|float
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## LootEntry

|Class
|--
|net.minecraft.world.storage.loot.LootEntry

---

|Extends
|--

---

|Fields|Type
|--|--
|  entryName|String
|  field_186364_c|int
|  field_186365_d|int

---

|Methods|Return Type
|--|--
| func_186361_a(float f)|int
| func_186363_a(Collection\<ItemStack> arg0, Random arg1, LootContext arg2)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## LootContext$EntityTarget

|Class
|--
|net.minecraft.world.storage.loot.LootContext$EntityTarget

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Template$BlockInfo

|Class
|--
|net.minecraft.world.gen.structure.template.Template$BlockInfo

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_186242_a|BlockPos
|  field_186243_b|BlockState
|  field_186244_c|NBTTagCompound

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## FunctionManager$QueuedCommand

|Class
|--
|net.minecraft.advancements.FunctionManager$QueuedCommand

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_194222_a(ArrayDeque\<FunctionManager$QueuedCommand> arg0, int arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Int2IntFunction

|Interface
|--
|it.unimi.dsi.fastutil.ints.Int2IntFunction

---

|Extends
|--
|Function

---

|Methods|Return Type
|--|--
| clear()|void
| containsKey(int i)|boolean
| containsKey(Object o)|boolean
| defaultReturnValue(int i)|void
| defaultReturnValue()|int
| get(int i)|int
| get(Object o)|Object
| put(int arg0, int arg1)|int
| put(Object arg0, Object arg1)|Object
| remove(int i)|int
| remove(Object o)|Object
| size()|int

---

## Int2IntMap$Entry

|Interface
|--
|it.unimi.dsi.fastutil.ints.Int2IntMap$Entry

---

|Extends
|--
|Map$Entry

---

|Fields|Type
|--|--
|  intKey|int
|  intValue|int
|  key|Object
|  value|Object

---

|Methods|Return Type
|--|--

---

## PositionTextureVertex

|Class
|--
|net.minecraft.client.model.PositionTextureVertex

---

|Extends
|--

---

|Fields|Type
|--|--
|  field_78241_b|float
|  field_78242_c|float
|  field_78243_a|Vec3d

---

|Methods|Return Type
|--|--
| func_78240_a(float arg0, float arg1)|PositionTextureVertex
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ExpressionResolver

|Interface
|--
|net.optifine.expr.IExpressionResolver

---

|Extends
|--

---

|Methods|Return Type
|--|--
| getExpression(String s)|Expression

---

## Expression

|Interface
|--
|net.optifine.expr.IExpression

---

|Extends
|--

---

|Fields|Type
|--|--
|  expressionType|ExpressionType

---

|Methods|Return Type
|--|--

---

## ModelVariableFloat

|Class
|--
|net.optifine.entity.model.anim.ModelVariableFloat

---

|Extends
|--
|ExpressionFloat

---

|Fields|Type
|--|--
|  expressionType|ExpressionType
|  value|float

---

|Methods|Return Type
|--|--
| eval()|float
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Paintable

|Interface
|--
|com.latmod.mods.itemfilters.api.IPaintable

---

|Extends
|--

---

|Fields|Type
|--|--
|  paint|BlockState

---

|Methods|Return Type
|--|--
| paint(BlockState arg0, EnumFacing arg1, boolean arg2)|void

---

## ModelState

|Interface
|--
|net.minecraftforge.common.model.IModelState

---

|Extends
|--

---

|Methods|Return Type
|--|--
| apply(Optional\<? extends net.minecraftforge.common.model.IModelPart> o)|Optional\<TRSRTransformation>

---

## TRSRTransformation

|Class
|--
|net.minecraftforge.common.model.TRSRTransformation

---

|Extends
|--
|ModelState
|Transformation

---

|Fields|Type
|--|--
|  identity|boolean
|  leftRot|Quat4f
|  matrix|Matrix4f
|  rightRot|Quat4f
|  scale|Vector3f
|  translation|Vector3f

---

|Methods|Return Type
|--|--
| apply(Optional\<? extends net.minecraftforge.common.model.IModelPart> o)|Optional\<TRSRTransformation>
| compose(TRSRTransformation t)|TRSRTransformation
| getUVLockTransform(EnumFacing e)|TRSRTransformation
| inverse()|TRSRTransformation
| rotate(EnumFacing e)|EnumFacing
| rotate(EnumFacing arg0, int arg1)|int
| slerp(TRSRTransformation arg0, float arg1)|TRSRTransformation
| toItemTransform()|ItemTransformVec3f
| transformNormal(Vector3f v)|void
| transformPosition(Vector4f v)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ShaderUniform

|Class
|--
|net.minecraft.client.shader.ShaderUniform

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_148081_a(float arg0, float arg1, float arg2, float arg3)|void
| func_148083_a(int arg0, int arg1, int arg2, int arg3)|void
| func_148084_b(int i)|void
| func_148086_a()|String
| func_148087_a(float arg0, float arg1)|void
| func_148088_a(Matrix4f m)|void
| func_148090_a(float f)|void
| func_148092_b(float arg0, float arg1, float arg2, float arg3)|void
| func_148093_b()|void
| func_148094_a(float arg0, float arg1, float arg2, float arg3, float arg4, float arg5, float arg6, float arg7, float arg8, float arg9, float arg10, float arg11, float arg12, float arg13, float arg14, float arg15)|void
| func_148095_a(float arg0, float arg1, float arg2)|void
| func_148097_a(float[] f)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ShaderLoader

|Class
|--
|net.minecraft.client.shader.ShaderLoader

---

|Extends
|--

---

|Methods|Return Type
|--|--
| func_148054_b(ShaderManager s)|void
| func_148055_a()|String
| func_148056_a(ShaderManager s)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## LongIterable

|Interface
|--
|it.unimi.dsi.fastutil.longs.LongIterable

---

|Extends
|--
|Iterable

---

|Methods|Return Type
|--|--
| forEach(Consumer\<? super T> c)|void
| iterator()|LongIterator
| iterator()|Iterator\<T>
| spliterator()|Spliterator\<T>

---

## MapDecoration$Type

|Class
|--
|net.minecraft.world.storage.MapDecoration$Type

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| func_191160_b()|boolean
| func_191161_d()|int
| func_191162_c()|boolean
| func_191163_a()|byte
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Vector3D

|Class
|--
|paulscode.sound.Vector3D

---

|Extends
|--

---

|Fields|Type
|--|--
|  x|float
|  y|float
|  z|float

---

|Methods|Return Type
|--|--
| add(Vector3D arg0, Vector3D arg1)|Vector3D
| add(Vector3D v)|Vector3D
| clone()|Vector3D
| clone()|Object
| cross(Vector3D v)|Vector3D
| cross(Vector3D arg0, Vector3D arg1)|Vector3D
| dot(Vector3D arg0, Vector3D arg1)|float
| dot(Vector3D v)|float
| length()|float
| normalize()|void
| subtract(Vector3D v)|Vector3D
| subtract(Vector3D arg0, Vector3D arg1)|Vector3D
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## UserListEntryBan

|Class
|--
|net.minecraft.server.management.UserListEntryBan

---

|Extends
|--
|UserListEntry

---

|Methods|Return Type
|--|--
| func_73680_d()|Date
| func_73686_f()|String
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## Widget

|Class
|--
|com.feed_the_beast.ftblib.lib.gui.Widget

---

|Extends
|--
|GuiWrapper

---

|Fields|Type
|--|--
|  enabled|boolean
|  gui|GuiBase
|  height|int
|  ingredientUnderMouse|Object
|  mouseOver|boolean
|  mouseX|int
|  mouseY|int
|  parent|Panel
|  partialTicks|float
|  posX|int
|  posY|int
|  screen|ScaledResolution
|  title|String
|  widgetType|WidgetType
|  width|int
|  x|int
|  y|int

---

|Methods|Return Type
|--|--
| acceptGhostIngredient(Object o)|void
| addMouseOverText(List\<String> l)|void
| checkMouseOver(int arg0, int arg1)|boolean
| closeContextMenu()|void
| closeGui(boolean b)|void
| closeGui()|void
| collidesWith(int arg0, int arg1, int arg2, int arg3)|boolean
| draw(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| handleClick(String s)|boolean
| handleClick(String arg0, String arg1)|boolean
| isGhostIngredientTarget(Object o)|boolean
| keyPressed(int arg0, char arg1)|boolean
| keyReleased(int i)|void
| mousePressed(MouseButton m)|boolean
| mouseReleased(MouseButton m)|void
| mouseScrolled(int i)|boolean
| onClosed()|void
| openContextMenu(Panel p)|void
| openGui()|void
| openGuiLater()|void
| run()|void
| setHeight(int i)|void
| setPos(int arg0, int arg1)|void
| setPosAndSize(int arg0, int arg1, int arg2, int arg3)|Widget
| setSize(int arg0, int arg1)|void
| setWidth(int i)|void
| shouldAddMouseOverText()|boolean
| shouldDraw()|boolean
| tick()|void
| updateMouseOver(int arg0, int arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## PanelScrollBar

|Class
|--
|com.feed_the_beast.ftblib.lib.gui.PanelScrollBar

---

|Extends
|--
|ScrollBar

---

|Fields|Type
|--|--
|  enabled|boolean
|  gui|GuiBase
|  height|int
|  ingredientUnderMouse|Object
|  maxValue|int
|  minValue|int
|  mouseOver|boolean
|  mouseX|int
|  mouseY|int
|  panel|Panel
|  parent|Panel
|  partialTicks|float
|  plane|ScrollBar$Plane
|  posX|int
|  posY|int
|  screen|ScaledResolution
|  scrollBarSize|int
|  scrollStep|int
|  title|String
|  value|int
|  widgetType|WidgetType
|  width|int
|  x|int
|  y|int

---

|Methods|Return Type
|--|--
| acceptGhostIngredient(Object o)|void
| addMouseOverText(List\<String> l)|void
| canMouseScroll()|boolean
| canMouseScrollPlane()|boolean
| checkMouseOver(int arg0, int arg1)|boolean
| closeContextMenu()|void
| closeGui(boolean b)|void
| closeGui()|void
| collidesWith(int arg0, int arg1, int arg2, int arg3)|boolean
| draw(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawBackground(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawScrollBar(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| getValueI(int i)|int
| handleClick(String s)|boolean
| handleClick(String arg0, String arg1)|boolean
| isGhostIngredientTarget(Object o)|boolean
| keyPressed(int arg0, char arg1)|boolean
| keyReleased(int i)|void
| mousePressed(MouseButton m)|boolean
| mouseReleased(MouseButton m)|void
| mouseScrolled(int i)|boolean
| onClosed()|void
| onMoved()|void
| openContextMenu(Panel p)|void
| openGui()|void
| openGuiLater()|void
| run()|void
| setCanAlwaysScroll(boolean b)|void
| setCanAlwaysScrollPlane(boolean b)|void
| setHeight(int i)|void
| setPos(int arg0, int arg1)|void
| setPosAndSize(int arg0, int arg1, int arg2, int arg3)|Widget
| setSize(int arg0, int arg1)|void
| setWidth(int i)|void
| shouldAddMouseOverText()|boolean
| shouldDraw()|boolean
| showValueOnMouseOver()|boolean
| tick()|void
| updateMouseOver(int arg0, int arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## GuiBase

|Class
|--
|com.feed_the_beast.ftblib.lib.gui.GuiBase

---

|Extends
|--
|Panel
|OpenableGui

---

|Fields|Type
|--|--
|  attachedScrollbar|PanelScrollBar
|  contentHeight|int
|  contentHeightExtra|int
|  contentWidth|int
|  contentWidthExtra|int
|  contextMenu|Panel
|  defaultScrollVertical|boolean
|  enabled|boolean
|  fixUnicode|boolean
|  gui|GuiBase
|  height|int
|  ingredientUnderMouse|Object
|  mouseOver|boolean
|  mouseOverAnyWidget|boolean
|  mouseX|int
|  mouseY|int
|  offset|boolean
|  onlyInteractWithWidgetsInside|boolean
|  onlyRenderWidgetsInside|boolean
|  parent|Panel
|  partialTicks|float
|  posX|int
|  posY|int
|  prevScreen|GuiScreen
|  screen|ScaledResolution
|  scrollStep|int
|  scrollX|int
|  scrollY|int
|  theme|Theme
|  title|String
|  unicode|boolean
|  widgets|List\<Widget>
|  widgetType|WidgetType
|  width|int
|  wrapper|GuiScreen
|  x|int
|  y|int

---

|Methods|Return Type
|--|--
| acceptGhostIngredient(Object o)|void
| add(Widget w)|void
| addAll(Iterable\<? extends com.feed_the_beast.ftblib.lib.gui.Widget> i)|void
| addMouseOverText(List\<String> l)|void
| addWidgets()|void
| align(WidgetLayout w)|int
| alignWidgets()|void
| checkMouseOver(int arg0, int arg1)|boolean
| clearWidgets()|void
| closeContextMenu()|void
| closeGui(boolean b)|void
| closeGui()|void
| collidesWith(int arg0, int arg1, int arg2, int arg3)|boolean
| doesGuiPauseGame()|boolean
| draw(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawBackground(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawDefaultBackground()|boolean
| drawForeground(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawOffsetBackground(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawWidget(Theme arg0, Widget arg1, int arg2, int arg3, int arg4, int arg5, int arg6)|void
| getWidget(int i)|Widget
| handleClick(String arg0, String arg1)|boolean
| handleClick(String s)|boolean
| initGui()|void
| isGhostIngredientTarget(Object o)|boolean
| keyPressed(int arg0, char arg1)|boolean
| keyReleased(int i)|void
| mousePressed(MouseButton m)|boolean
| mouseReleased(MouseButton m)|void
| mouseScrolled(int i)|boolean
| movePanelScroll(int arg0, int arg1)|boolean
| onBack()|void
| onClosed()|void
| onClosedByKey(int i)|boolean
| onInit()|boolean
| onPostInit()|void
| openContextMenu(Panel p)|void
| openContextMenu(List\<ContextMenuItem> l)|ContextMenu
| openGui()|void
| openGuiLater()|void
| openYesNo(String arg0, String arg1, Runnable arg2)|void
| openYesNoFull(String arg0, String arg1, YesNoCallback arg2)|void
| refreshWidgets()|void
| run()|void
| scrollPanel(int i)|boolean
| setHeight(int i)|void
| setPos(int arg0, int arg1)|void
| setPosAndSize(int arg0, int arg1, int arg2, int arg3)|Widget
| setSize(int arg0, int arg1)|void
| setWidth(int i)|void
| shouldAddMouseOverText()|boolean
| shouldDraw()|boolean
| tick()|void
| updateGui(int arg0, int arg1, float arg2)|void
| updateMouseOver(int arg0, int arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WidgetType

|Class
|--
|com.feed_the_beast.ftblib.lib.gui.WidgetType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## WidgetLayout

|Interface
|--
|com.feed_the_beast.ftblib.lib.gui.WidgetLayout

---

|Extends
|--

---

|Methods|Return Type
|--|--
| align(Panel p)|int

---

## Theme

|Class
|--
|com.feed_the_beast.ftblib.lib.gui.Theme

---

|Extends
|--

---

|Fields|Type
|--|--
|  font|FontRenderer
|  fontHeight|int
|  invertedContentColor|Color4I

---

|Methods|Return Type
|--|--
| createDataFrom(TextComponent arg0, int arg1)|List\<GuiBase$PositionedTextData>
| drawButton(int arg0, int arg1, int arg2, int arg3, WidgetType arg4)|void
| drawCheckbox(int arg0, int arg1, int arg2, int arg3, WidgetType arg4, boolean arg5, boolean arg6)|void
| drawCheckboxBackground(int arg0, int arg1, int arg2, int arg3, boolean arg4)|void
| drawContainerSlot(int arg0, int arg1, int arg2, int arg3)|void
| drawContextMenuBackground(int arg0, int arg1, int arg2, int arg3)|void
| drawGui(int arg0, int arg1, int arg2, int arg3, WidgetType arg4)|void
| drawHorizontalTab(int arg0, int arg1, int arg2, int arg3, boolean arg4)|void
| drawPanelBackground(int arg0, int arg1, int arg2, int arg3)|void
| drawScrollBar(int arg0, int arg1, int arg2, int arg3, WidgetType arg4, boolean arg5)|void
| drawScrollBarBackground(int arg0, int arg1, int arg2, int arg3, WidgetType arg4)|void
| drawSlot(int arg0, int arg1, int arg2, int arg3, WidgetType arg4)|void
| drawString(String arg0, int arg1, int arg2, int arg3)|int
| drawString(String arg0, int arg1, int arg2, Color4I arg3, int arg4)|int
| drawString(String arg0, int arg1, int arg2)|int
| drawTextBox(int arg0, int arg1, int arg2, int arg3)|void
| drawWidget(int arg0, int arg1, int arg2, int arg3, WidgetType arg4)|void
| getContentColor(WidgetType w)|Color4I
| getStringWidth(String s)|int
| listFormattedStringToWidth(String arg0, int arg1)|List\<String>
| popFontUnicode()|void
| pushFontUnicode(boolean b)|void
| trimStringToWidth(String arg0, int arg1)|String
| trimStringToWidthReverse(String arg0, int arg1)|String
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ObjectBidirectionalIterator

|Interface
|--
|it.unimi.dsi.fastutil.objects.ObjectBidirectionalIterator

---

|Extends
|--
|ObjectIterator
|BidirectionalIterator

---

|Methods|Return Type
|--|--
| back(int i)|int
| forEachRemaining(Consumer\<? super E> c)|void
| hasNext()|boolean
| hasPrevious()|boolean
| next()|Object
| previous()|Object
| remove()|void
| skip(int i)|int

---

## BlockBush

|Class
|--
|net.minecraft.block.BlockBush

---

|Extends
|--
|Block
|Plantable

---

|Fields|Type
|--|--
|  delegate|RegistryDelegate\<T>
|  field_149763_I|float
|  field_149765_K|float
|  field_149772_a|CreativeTabs
|  field_149781_w|float
|  field_149782_v|float
|  field_176227_L|BlockStateContainer
|  registryName|ResourceLocation
|  registryType|Class\<T>

---

|Methods|Return Type
|--|--
| addDestroyEffects(World arg0, BlockPos arg1, ParticleManager arg2)|boolean
| addHitEffects(BlockState arg0, World arg1, RayTraceResult arg2, ParticleManager arg3)|boolean
| addLandingEffects(BlockState arg0, WorldServer arg1, BlockPos arg2, BlockState arg3, EntityLivingBase arg4, int arg5)|boolean
| addRunningEffects(BlockState arg0, World arg1, BlockPos arg2, Entity arg3)|boolean
| beginLeavesDecay(BlockState arg0, World arg1, BlockPos arg2)|void
| canBeConnectedTo(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean
| canBeReplacedByLeaves(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| canConnectRedstone(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| canCreatureSpawn(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityLiving$SpawnPlacementType arg3)|boolean
| canEntityDestroy(BlockState arg0, BlockAccess arg1, BlockPos arg2, Entity arg3)|boolean
| canHarvestBlock(BlockAccess arg0, BlockPos arg1, EntityPlayer arg2)|boolean
| canPlaceTorchOnTop(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| canRenderInLayer(BlockState arg0, BlockRenderLayer arg1)|boolean
| canSilkHarvest(World arg0, BlockPos arg1, BlockState arg2, EntityPlayer arg3)|boolean
| canSustainLeaves(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| canSustainPlant(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3, Plantable arg4)|boolean
| createTileEntity(World arg0, BlockState arg1)|TileEntity
| doesSideBlockChestOpening(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| doesSideBlockRendering(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| func_149637_q(BlockState b)|boolean
| func_149638_a(Entity e)|float
| func_149645_b(BlockState b)|EnumBlockRenderType
| func_149647_a(CreativeTabs c)|Block
| func_149652_G()|boolean
| func_149653_t()|boolean
| func_149656_h(BlockState b)|EnumPushReaction
| func_149659_a(Explosion e)|boolean
| func_149662_c(BlockState b)|boolean
| func_149663_c(String s)|Block
| func_149666_a(CreativeTabs arg0, NonNullList\<ItemStack> arg1)|void
| func_149667_c(Block b)|boolean
| func_149675_a(boolean b)|Block
| func_149679_a(int arg0, Random arg1)|int
| func_149686_d(BlockState b)|boolean
| func_149688_o(BlockState b)|Material
| func_149698_L()|boolean
| func_149703_v()|boolean
| func_149708_J()|CreativeTabs
| func_149710_n(BlockState b)|boolean
| func_149711_c(float f)|Block
| func_149713_g(int i)|Block
| func_149715_a(float f)|Block
| func_149716_u()|boolean
| func_149717_k(BlockState b)|int
| func_149721_r(BlockState b)|boolean
| func_149722_s()|Block
| func_149730_j(BlockState b)|boolean
| func_149732_F()|String
| func_149738_a(World w)|int
| func_149739_a()|String
| func_149740_M(BlockState b)|boolean
| func_149744_f(BlockState b)|boolean
| func_149745_a(Random r)|int
| func_149750_m(BlockState b)|int
| func_149751_l(BlockState b)|boolean
| func_149752_b(float f)|Block
| func_176194_O()|BlockStateContainer
| func_176195_g(BlockState arg0, World arg1, BlockPos arg2)|float
| func_176196_c(World arg0, BlockPos arg1)|boolean
| func_176197_a(World arg0, BlockPos arg1, Entity arg2, Vec3d arg3)|Vec3d
| func_176198_a(World arg0, BlockPos arg1, EnumFacing arg2)|boolean
| func_176199_a(World arg0, BlockPos arg1, Entity arg2)|void
| func_176200_f(BlockAccess arg0, BlockPos arg1)|boolean
| func_176201_c(BlockState b)|int
| func_176203_a(int i)|BlockState
| func_176205_b(BlockAccess arg0, BlockPos arg1)|boolean
| func_176206_d(World arg0, BlockPos arg1, BlockState arg2)|void
| func_176208_a(World arg0, BlockPos arg1, BlockState arg2, EntityPlayer arg3)|void
| func_176209_a(BlockState arg0, boolean arg1)|boolean
| func_176211_b(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|int
| func_176213_c(World arg0, BlockPos arg1, BlockState arg2)|void
| func_176214_u(BlockState b)|boolean
| func_176216_a(World arg0, Entity arg1)|void
| func_176218_Q()|Block$EnumOffsetType
| func_176221_a(BlockState arg0, BlockAccess arg1, BlockPos arg2)|BlockState
| func_176223_P()|BlockState
| func_176224_k(World arg0, BlockPos arg1)|void
| func_176225_a(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| func_176226_b(World arg0, BlockPos arg1, BlockState arg2, int arg3)|void
| func_180633_a(World arg0, BlockPos arg1, BlockState arg2, EntityLivingBase arg3, ItemStack arg4)|void
| func_180634_a(World arg0, BlockPos arg1, BlockState arg2, Entity arg3)|void
| func_180636_a(BlockState arg0, World arg1, BlockPos arg2, Vec3d arg3, Vec3d arg4)|RayTraceResult
| func_180637_b(World arg0, BlockPos arg1, int arg2)|void
| func_180639_a(World arg0, BlockPos arg1, BlockState arg2, EntityPlayer arg3, EnumHand arg4, EnumFacing arg5, float arg6, float arg7, float arg8)|boolean
| func_180640_a(BlockState arg0, World arg1, BlockPos arg2)|AxisAlignedBB
| func_180641_l(BlockState arg0, World arg1, BlockPos arg2)|int
| func_180642_a(World arg0, BlockPos arg1, EnumFacing arg2, float arg3, float arg4, float arg5, int arg6, EntityLivingBase arg7)|BlockState
| func_180645_a(World arg0, BlockPos arg1, BlockState arg2, Random arg3)|void
| func_180646_a(BlockState arg0, BlockAccess arg1, BlockPos arg2)|AxisAlignedBB
| func_180647_a(BlockState arg0, EntityPlayer arg1, World arg2, BlockPos arg3)|float
| func_180649_a(World arg0, BlockPos arg1, EntityPlayer arg2)|void
| func_180650_b(World arg0, BlockPos arg1, BlockState arg2, Random arg3)|void
| func_180651_a(BlockState b)|int
| func_180652_a(World arg0, BlockPos arg1, Explosion arg2)|void
| func_180653_a(World arg0, BlockPos arg1, BlockState arg2, float arg3, int arg4)|void
| func_180655_c(BlockState arg0, World arg1, BlockPos arg2, Random arg3)|void
| func_180656_a(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|int
| func_180657_a(World arg0, EntityPlayer arg1, BlockPos arg2, BlockState arg3, TileEntity arg4, ItemStack arg5)|void
| func_180658_a(World arg0, BlockPos arg1, Entity arg2, float arg3)|void
| func_180659_g(BlockState arg0, BlockAccess arg1, BlockPos arg2)|MapColor
| func_180660_a(BlockState arg0, Random arg1, int arg2)|Item
| func_180663_b(World arg0, BlockPos arg1, BlockState arg2)|void
| func_180664_k()|BlockRenderLayer
| func_180671_f(World arg0, BlockPos arg1, BlockState arg2)|boolean
| func_181623_g()|boolean
| func_185467_w()|SoundType
| func_185471_a(BlockState arg0, Mirror arg1)|BlockState
| func_185473_a(World arg0, BlockPos arg1, BlockState arg2)|ItemStack
| func_185477_a(BlockState arg0, World arg1, BlockPos arg2, AxisAlignedBB arg3, List\<AxisAlignedBB> arg4, Entity arg5, boolean arg6)|void
| func_185481_k(BlockState b)|boolean
| func_185484_c(BlockState arg0, BlockAccess arg1, BlockPos arg2)|int
| func_185485_f(BlockState b)|float
| func_185496_a(BlockState arg0, BlockAccess arg1, BlockPos arg2)|AxisAlignedBB
| func_185499_a(BlockState arg0, Rotation arg1)|BlockState
| func_189539_a(BlockState arg0, World arg1, BlockPos arg2, int arg3, int arg4)|boolean
| func_189540_a(BlockState arg0, World arg1, BlockPos arg2, Block arg3, BlockPos arg4)|void
| func_189872_a(BlockState arg0, Entity arg1)|boolean
| func_190946_v(BlockState b)|boolean
| func_190948_a(ItemStack arg0, World arg1, List\<String> arg2, TooltipFlag arg3)|void
| func_190949_e(BlockState arg0, BlockAccess arg1, BlockPos arg2)|Vec3d
| func_193383_a(BlockAccess arg0, BlockState arg1, BlockPos arg2, EnumFacing arg3)|BlockFaceShape
| getAiPathNodeType(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityLiving arg3)|PathNodeType
| getAiPathNodeType(BlockState arg0, BlockAccess arg1, BlockPos arg2)|PathNodeType
| getBeaconColorMultiplier(BlockState arg0, World arg1, BlockPos arg2, BlockPos arg3)|float[]
| getBedDirection(BlockState arg0, BlockAccess arg1, BlockPos arg2)|EnumFacing
| getBedSpawnPosition(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityPlayer arg3)|BlockPos
| getBlockLiquidHeight(World arg0, BlockPos arg1, BlockState arg2, Material arg3)|float
| getDrops(BlockAccess arg0, BlockPos arg1, BlockState arg2, int arg3)|List\<ItemStack>
| getDrops(NonNullList\<ItemStack> arg0, BlockAccess arg1, BlockPos arg2, BlockState arg3, int arg4)|void
| getEnchantPowerBonus(World arg0, BlockPos arg1)|float
| getExpDrop(BlockState arg0, BlockAccess arg1, BlockPos arg2, int arg3)|int
| getExplosionResistance(World arg0, BlockPos arg1, Entity arg2, Explosion arg3)|float
| getExtendedState(BlockState arg0, BlockAccess arg1, BlockPos arg2)|BlockState
| getFireSpreadSpeed(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|int
| getFlammability(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|int
| getFogColor(World arg0, BlockPos arg1, BlockState arg2, Entity arg3, Vec3d arg4, float arg5)|Vec3d
| getHarvestLevel(BlockState b)|int
| getHarvestTool(BlockState b)|String
| getLightOpacity(BlockState arg0, BlockAccess arg1, BlockPos arg2)|int
| getLightValue(BlockState arg0, BlockAccess arg1, BlockPos arg2)|int
| getPickBlock(BlockState arg0, RayTraceResult arg1, World arg2, BlockPos arg3, EntityPlayer arg4)|ItemStack
| getPlant(BlockAccess arg0, BlockPos arg1)|BlockState
| getPlantType(BlockAccess arg0, BlockPos arg1)|EnumPlantType
| getSlipperiness(BlockState arg0, BlockAccess arg1, BlockPos arg2, Entity arg3)|float
| getSoundType(BlockState arg0, World arg1, BlockPos arg2, Entity arg3)|SoundType
| getStateAtViewpoint(BlockState arg0, BlockAccess arg1, BlockPos arg2, Vec3d arg3)|BlockState
| getStateForPlacement(World arg0, BlockPos arg1, EnumFacing arg2, float arg3, float arg4, float arg5, int arg6, EntityLivingBase arg7, EnumHand arg8)|BlockState
| getValidRotations(World arg0, BlockPos arg1)|EnumFacing[]
| getWeakChanges(BlockAccess arg0, BlockPos arg1)|boolean
| hasTileEntity(BlockState b)|boolean
| isAABBInsideLiquid(World arg0, BlockPos arg1, AxisAlignedBB arg2)|Boolean
| isAABBInsideMaterial(World arg0, BlockPos arg1, AxisAlignedBB arg2, Material arg3)|Boolean
| isAir(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| isBeaconBase(BlockAccess arg0, BlockPos arg1, BlockPos arg2)|boolean
| isBed(BlockState arg0, BlockAccess arg1, BlockPos arg2, Entity arg3)|boolean
| isBedFoot(BlockAccess arg0, BlockPos arg1)|boolean
| isBurning(BlockAccess arg0, BlockPos arg1)|boolean
| isEntityInsideMaterial(BlockAccess arg0, BlockPos arg1, BlockState arg2, Entity arg3, double arg4, Material arg5, boolean arg6)|Boolean
| isFertile(World arg0, BlockPos arg1)|boolean
| isFireSource(World arg0, BlockPos arg1, EnumFacing arg2)|boolean
| isFlammable(BlockAccess arg0, BlockPos arg1, EnumFacing arg2)|boolean
| isFoliage(BlockAccess arg0, BlockPos arg1)|boolean
| isLadder(BlockState arg0, BlockAccess arg1, BlockPos arg2, EntityLivingBase arg3)|boolean
| isLeaves(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| isNormalCube(BlockState arg0, BlockAccess arg1, BlockPos arg2)|boolean
| isReplaceableOreGen(BlockState arg0, BlockAccess arg1, BlockPos arg2, Predicate\<BlockState> arg3)|boolean
| isSideSolid(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| isStickyBlock(BlockState b)|boolean
| isToolEffective(String arg0, BlockState arg1)|boolean
| isWood(BlockAccess arg0, BlockPos arg1)|boolean
| observedNeighborChange(BlockState arg0, World arg1, BlockPos arg2, Block arg3, BlockPos arg4)|void
| onBlockExploded(World arg0, BlockPos arg1, Explosion arg2)|void
| onNeighborChange(BlockAccess arg0, BlockPos arg1, BlockPos arg2)|void
| onPlantGrow(BlockState arg0, World arg1, BlockPos arg2, BlockPos arg3)|void
| quantityDropped(BlockState arg0, int arg1, Random arg2)|int
| recolorBlock(World arg0, BlockPos arg1, EnumFacing arg2, EnumDyeColor arg3)|boolean
| removedByPlayer(BlockState arg0, World arg1, BlockPos arg2, EntityPlayer arg3, boolean arg4)|boolean
| rotateBlock(World arg0, BlockPos arg1, EnumFacing arg2)|boolean
| setBedOccupied(BlockAccess arg0, BlockPos arg1, EntityPlayer arg2, boolean arg3)|void
| setDefaultSlipperiness(float f)|void
| setHarvestLevel(String arg0, int arg1, BlockState arg2)|void
| setHarvestLevel(String arg0, int arg1)|void
| shouldCheckWeakPower(BlockState arg0, BlockAccess arg1, BlockPos arg2, EnumFacing arg3)|boolean
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ExpressionType

|Class
|--
|net.optifine.expr.ExpressionType

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ExpressionFloat

|Interface
|--
|net.optifine.expr.IExpressionFloat

---

|Extends
|--
|Expression

---

|Fields|Type
|--|--
|  expressionType|ExpressionType

---

|Methods|Return Type
|--|--
| eval()|float

---

## Transformation

|Interface
|--
|net.minecraftforge.common.model.ITransformation

---

|Extends
|--

---

|Fields|Type
|--|--
|  matrix|Matrix4f

---

|Methods|Return Type
|--|--
| rotate(EnumFacing e)|EnumFacing
| rotate(EnumFacing arg0, int arg1)|int

---

## GuiWrapper

|Interface
|--
|com.feed_the_beast.ftblib.lib.gui.IGuiWrapper

---

|Extends
|--
|OpenableGui

---

|Fields|Type
|--|--
|  gui|GuiBase

---

|Methods|Return Type
|--|--
| closeContextMenu()|void
| closeGui(boolean b)|void
| closeGui()|void
| openContextMenu(Panel p)|void
| openGui()|void
| openGuiLater()|void
| run()|void

---

## ScrollBar

|Class
|--
|com.feed_the_beast.ftblib.lib.gui.ScrollBar

---

|Extends
|--
|Widget

---

|Fields|Type
|--|--
|  enabled|boolean
|  gui|GuiBase
|  height|int
|  ingredientUnderMouse|Object
|  maxValue|int
|  minValue|int
|  mouseOver|boolean
|  mouseX|int
|  mouseY|int
|  parent|Panel
|  partialTicks|float
|  plane|ScrollBar$Plane
|  posX|int
|  posY|int
|  screen|ScaledResolution
|  scrollBarSize|int
|  scrollStep|int
|  title|String
|  value|int
|  widgetType|WidgetType
|  width|int
|  x|int
|  y|int

---

|Methods|Return Type
|--|--
| acceptGhostIngredient(Object o)|void
| addMouseOverText(List\<String> l)|void
| canMouseScroll()|boolean
| canMouseScrollPlane()|boolean
| checkMouseOver(int arg0, int arg1)|boolean
| closeContextMenu()|void
| closeGui(boolean b)|void
| closeGui()|void
| collidesWith(int arg0, int arg1, int arg2, int arg3)|boolean
| draw(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawBackground(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawScrollBar(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| getValueI(int i)|int
| handleClick(String s)|boolean
| handleClick(String arg0, String arg1)|boolean
| isGhostIngredientTarget(Object o)|boolean
| keyPressed(int arg0, char arg1)|boolean
| keyReleased(int i)|void
| mousePressed(MouseButton m)|boolean
| mouseReleased(MouseButton m)|void
| mouseScrolled(int i)|boolean
| onClosed()|void
| onMoved()|void
| openContextMenu(Panel p)|void
| openGui()|void
| openGuiLater()|void
| run()|void
| setCanAlwaysScroll(boolean b)|void
| setCanAlwaysScrollPlane(boolean b)|void
| setHeight(int i)|void
| setPos(int arg0, int arg1)|void
| setPosAndSize(int arg0, int arg1, int arg2, int arg3)|Widget
| setSize(int arg0, int arg1)|void
| setWidth(int i)|void
| shouldAddMouseOverText()|boolean
| shouldDraw()|boolean
| showValueOnMouseOver()|boolean
| tick()|void
| updateMouseOver(int arg0, int arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ScrollBar$Plane

|Class
|--
|com.feed_the_beast.ftblib.lib.gui.ScrollBar$Plane

---

|Extends
|--
|Enum

---

|Fields|Type
|--|--
|  declaringClass|Class\<E>
|  isVertical|boolean

---

|Methods|Return Type
|--|--
| compareTo(Object o)|int
| compareTo(Enum e)|int
| name()|String
| ordinal()|int
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ContextMenuItem

|Class
|--
|com.feed_the_beast.ftblib.lib.gui.ContextMenuItem

---

|Extends
|--
|Comparable

---

|Fields|Type
|--|--
|  callback|Runnable
|  closeMenu|boolean
|  enabled|BooleanSupplier
|  icon|Icon
|  title|String
|  yesNoText|String

---

|Methods|Return Type
|--|--
| addMouseOverText(List\<String> l)|void
| compareTo(Object o)|int
| compareTo(ContextMenuItem c)|int
| createWidget(ContextMenu c)|Widget
| drawIcon(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| onClicked(Panel arg0, MouseButton arg1)|void
| setCloseMenu(boolean b)|ContextMenuItem
| setEnabled(boolean b)|ContextMenuItem
| setEnabled(BooleanSupplier b)|ContextMenuItem
| setYesNo(String s)|ContextMenuItem
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## ContextMenu

|Class
|--
|com.feed_the_beast.ftblib.lib.gui.ContextMenu

---

|Extends
|--
|Panel

---

|Fields|Type
|--|--
|  attachedScrollbar|PanelScrollBar
|  contentHeight|int
|  contentHeightExtra|int
|  contentWidth|int
|  contentWidthExtra|int
|  defaultScrollVertical|boolean
|  enabled|boolean
|  gui|GuiBase
|  hasIcons|boolean
|  height|int
|  ingredientUnderMouse|Object
|  items|List\<ContextMenuItem>
|  mouseOver|boolean
|  mouseOverAnyWidget|boolean
|  mouseX|int
|  mouseY|int
|  offset|boolean
|  onlyInteractWithWidgetsInside|boolean
|  onlyRenderWidgetsInside|boolean
|  parent|Panel
|  partialTicks|float
|  posX|int
|  posY|int
|  screen|ScaledResolution
|  scrollStep|int
|  scrollX|int
|  scrollY|int
|  title|String
|  unicode|boolean
|  widgets|List\<Widget>
|  widgetType|WidgetType
|  width|int
|  x|int
|  y|int

---

|Methods|Return Type
|--|--
| acceptGhostIngredient(Object o)|void
| add(Widget w)|void
| addAll(Iterable\<? extends com.feed_the_beast.ftblib.lib.gui.Widget> i)|void
| addMouseOverText(List\<String> l)|void
| addWidgets()|void
| align(WidgetLayout w)|int
| alignWidgets()|void
| checkMouseOver(int arg0, int arg1)|boolean
| clearWidgets()|void
| closeContextMenu()|void
| closeGui(boolean b)|void
| closeGui()|void
| collidesWith(int arg0, int arg1, int arg2, int arg3)|boolean
| draw(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawBackground(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawOffsetBackground(Theme arg0, int arg1, int arg2, int arg3, int arg4)|void
| drawWidget(Theme arg0, Widget arg1, int arg2, int arg3, int arg4, int arg5, int arg6)|void
| getWidget(int i)|Widget
| handleClick(String s)|boolean
| handleClick(String arg0, String arg1)|boolean
| isGhostIngredientTarget(Object o)|boolean
| keyPressed(int arg0, char arg1)|boolean
| keyReleased(int i)|void
| mousePressed(MouseButton m)|boolean
| mouseReleased(MouseButton m)|void
| mouseScrolled(int i)|boolean
| movePanelScroll(int arg0, int arg1)|boolean
| onClosed()|void
| openContextMenu(Panel p)|void
| openGui()|void
| openGuiLater()|void
| refreshWidgets()|void
| run()|void
| scrollPanel(int i)|boolean
| setHeight(int i)|void
| setPos(int arg0, int arg1)|void
| setPosAndSize(int arg0, int arg1, int arg2, int arg3)|Widget
| setSize(int arg0, int arg1)|void
| setWidth(int i)|void
| shouldAddMouseOverText()|boolean
| shouldDraw()|boolean
| tick()|void
| updateMouseOver(int arg0, int arg1)|void
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## YesNoCallback

|Interface
|--
|com.feed_the_beast.ftblib.lib.gui.misc.YesNoCallback

---

|Extends
|--

---

|Methods|Return Type
|--|--
| onButtonClicked(boolean b)|void

---

## GuiBase$PositionedTextData

|Class
|--
|com.feed_the_beast.ftblib.lib.gui.GuiBase$PositionedTextData

---

|Extends
|--

---

|Fields|Type
|--|--
|  clickEvent|ClickEvent
|  height|int
|  hoverEvent|HoverEvent
|  insertion|String
|  posX|int
|  posY|int
|  width|int

---

|Methods|Return Type
|--|--
| wait(long arg0, int arg1)|void
| wait(long l)|void

---

## BidirectionalIterator

|Interface
|--
|it.unimi.dsi.fastutil.BidirectionalIterator

---

|Extends
|--
|Iterator

---

|Methods|Return Type
|--|--
| forEachRemaining(Consumer\<? super E> c)|void
| hasNext()|boolean
| hasPrevious()|boolean
| next()|Object
| previous()|Object
| remove()|void

---

