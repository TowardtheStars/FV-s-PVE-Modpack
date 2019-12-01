import pynbt as nbt
import os, random

root = "./config/ftbquests/normal/chapters"

id_list = []

def add_dir(path):
    for directory in os.listdir(path):
        if directory not in ['chapter.nbt', 'index.nbt']:
            if os.path.isdir(os.path.join(path, directory)):
                add_dir(os.path.join(path, directory))
            else:
                directory = os.path.splitext(directory)[0]
            id_list.append(directory)

add_dir(root)

def gen_id(n=0):
    while n in id_list or n == 0 or n == 1:
        n = random.randint(2, 0xffffffff)
    id_list.append(hex(n)[2:])
    return hex(n)[2:]
    
aridGarden = [
    "harvestcraft:cactusfruititem",
    "harvestcraft:agaveitem",
    "harvestcraft:sisalitem",
    "harvestcraft:cassavaitem",
    "harvestcraft:chickpeaitem",
    "harvestcraft:lentilitem",
    "minecraft:cactus",
]

frostGarden = [
    "harvestcraft:raspberryitem",
    "harvestcraft:oatsitem",
    "harvestcraft:ryeitem",
    "harvestcraft:celeryitem",
    "harvestcraft:peasitem",
    "harvestcraft:beetitem",
    "harvestcraft:rutabagaitem",
    "harvestcraft:broccoliitem",
    "harvestcraft:caulifloweritem",
    "harvestcraft:cabbageitem",
    "harvestcraft:spinachitem",
    "harvestcraft:cottonitem",
    "harvestcraft:huckleberryitem",
    "harvestcraft:kohlrabiitem",
    "harvestcraft:quinoaitem",
]

#  [default: [harvestcraft:whitemushroomitem], [harvestcraft:blackberryitem], [harvestcraft:zucchiniitem], [harvestcraft:radishitem], [harvestcraft:rhubarbitem], [harvestcraft:tealeafitem], [harvestcraft:garlicitem], [harvestcraft:sweetpotatoitem], [harvestcraft:turnipitem], [harvestcraft:spiceleafitem], [harvestcraft:beanitem], [harvestcraft:leekitem], [harvestcraft:scallionitem], [harvestcraft:tomatoitem], [harvestcraft:juteitem]]
shadedGarden = [
    "harvestcraft:whitemushroomitem",
    "harvestcraft:blackberryitem",
    "harvestcraft:zucchiniitem",
    "harvestcraft:radishitem",
    "harvestcraft:rhubarbitem",
    "harvestcraft:tealeafitem",
    "harvestcraft:garlicitem",
    "harvestcraft:sweetpotatoitem",
    "harvestcraft:turnipitem",
    "harvestcraft:spiceleafitem",
    "harvestcraft:beanitem",
    "harvestcraft:leekitem",
    "harvestcraft:scallionitem",
    "harvestcraft:tomatoitem",
    "harvestcraft:juteitem",
]

soggyGarden = [
    "harvestcraft:brusselsproutitem",
    "harvestcraft:spiceleafitem",
    "harvestcraft:blueberryitem",
    "harvestcraft:asparagusitem",
    "harvestcraft:cranberryitem",
    "harvestcraft:riceitem",
    "harvestcraft:seaweeditem",
    "harvestcraft:waterchestnutitem",
    "harvestcraft:okraitem",
    "harvestcraft:cottonitem",
    "harvestcraft:kaleitem",
    "harvestcraft:milletitem",
    "harvestcraft:jicamaitem",
    "harvestcraft:greengrapeitem",
    "harvestcraft:mulberryitem",
]

tropicalGarden = [
    "harvestcraft:grapeitem",
    "harvestcraft:pineappleitem",
    "harvestcraft:kiwiitem",
    "harvestcraft:sesameseedsitem",
    "harvestcraft:curryleafitem",
    "harvestcraft:bambooshootitem",
    "harvestcraft:cantaloupeitem",
    "harvestcraft:gingeritem",
    "harvestcraft:coffeebeanitem",
    "harvestcraft:soybeanitem",
    "harvestcraft:eggplantitem",
    "harvestcraft:kenafitem",
    "harvestcraft:arrowrootitem",
    "harvestcraft:taroitem",
]

windyGarden = [
    "harvestcraft:strawberryitem",
    "harvestcraft:barleyitem",
    "harvestcraft:cornitem",
    "harvestcraft:cucumberitem",
    "harvestcraft:wintersquashitem",
    "harvestcraft:mustardseedsitem",
    "harvestcraft:onionitem",
    "harvestcraft:parsnipitem",
    "harvestcraft:peanutitem",
    "minecraft:potato",
    "minecraft:carrot",
    "harvestcraft:lettuceitem",
    "harvestcraft:artichokeitem",
    "harvestcraft:bellpepperitem",
    "harvestcraft:chilipepperitem",
    "minecraft:wheat",
    "harvestcraft:flaxitem",
    "harvestcraft:amaranthitem",
    "harvestcraft:elderberryitem",
]

gardens = [aridGarden, frostGarden, shadedGarden, soggyGarden, tropicalGarden, windyGarden]
garden_names = ['贫瘠', '严寒', '荫蔽', '湿润', '热带', '多风']
base_chapter = gen_id(0x61404d4e)

chapters = [gen_id(int(i, base=16)) for i in ["a2d67590", "b2a6a21a", "9a4d850c", "f764b037", "92df22db", "2ccc878e"]]
for i in range(len(chapters)):
    chapter = chapters[i]
    chapter_dir = os.path.join(root, chapter)
    if not os.path.exists(chapter_dir):
        os.mkdir(chapter_dir)
    chapter_tag = nbt.NBTFile()
    chapter_tag['group'] = nbt.TAG_Int(int(base_chapter, base=16))
    chapter_tag['always_invisible'] = nbt.TAG_Byte(0)
    chapter_tag['title'] = nbt.TAG_String(garden_names[i] + "特产")
    chapter_tag['description'] = nbt.TAG_List(tag_type=nbt.TAG_String)
    chapter_tag['description'].insert(0, nbt.TAG_String("集齐%s菜园掉落的所有农作物." % garden_names[i]))
    
    print(chapter_tag.pretty())
    chapter_tag.write_file(filename=os.path.join(chapter_dir, "chapter.nbt"))