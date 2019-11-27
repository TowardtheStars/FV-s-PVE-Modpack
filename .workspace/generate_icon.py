

import base64, json
import csv
import os, sys

"""
{
    "name":"黑暗石按钮",
    "englishName":"Darkstone Button",
    "registerName":"abyssalcraft:dsbutton",
    "metadata":0,
    "OredictList":[],
    "CreativeTabName":"红石",
    "type":"Block",
    "maxStackSize":64,
    "maxDurability":1,
    "smallIcon":"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAnElEQVR42u2UUQ6CMBBESRCWbm1RVIQYvf8ta2eTcgHSfs1LJlB+3nQpdB0hhBBygueyJ2Rbv5Zm4hgfJh4uYnm/PimGxZ5Vl0OGTOLTnIvseedYj+OU3OTrFwj+ZqJt/Vlwj6CAiNYvgJFDWIpA2vdDuwJzuJvcazwKqLsek6heoIhxFXG2e5TABJp9BeUVqIZ8GDXxh0QIIeQMf2W/Peu2TfMIAAAAAElFTkSuQmCC",
    "largeIcon":"iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAACiElEQVR42u3Z207bQBQFUCQKCUlz446q9v//Mo0tTTQcZqamqmo7rCXtlwbyMHs3sc3VFQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjGe/fzrmcSJfxOP92zGWn/L6/NMQLrn4mLz4GCd2wcWnHPbPfUoD2O8e+zjBCy4+Ji8+xoleQPE33xZ9SuW/PP04J5afv4cTnnHxMbH4mNZ7OvGJ2G4fjimxpO3m/pxYfqv4/Pe65O+5WKz6OPkJFf8hocA8nyk+TyreAEb2obSs+OVi/S5Di28N4W657mMAI9us983SYvkpu9Mwar/zdrrqr712e7s8l28AExlAypAhdMXH5MXH5MWn1AawuvtuAGMOoDWEdOtWGsD94aVPaQBdyXn5pQF0xadoZAIDyIdQe4CTFx+Tik+pDSCWbwATG0AqKpb/+vzrnFh+XnxtAPFj3wBGtF5tj11aA0jJi48pFW8AMxpAaQixyPTvQ4s3gBkOID3Raw2g9Fop19c3fQxghgPo8rcD6IpN5RvAxKWy/8UA8mJLA6jd+xvABAZQSiw4v0ZolR8H0PrZVHwaiUZGHsBuc+hTG0DKkAGkcls/G78eNDKRAXSJ/9OHDiAvvzaA2h2CRv73ReB61xxA/pH/pwHkH/u1AcRHwQYwgQGktAbQpTaAxeLuXfmlAdT+FqD4CQ2gz6ncoQPoik+pDaD0PZ8PQAMTHEDt8XD+Wl5+aQCtCz3Fz2QA8f5/yACWp8KX4Y7Ad/ychtC40GsNIBVfG4ATnssQGgPIPwlS8avVpk9tAE50xkNoPQpOxdcG4AQvxGcH4MQueAitATihLyIOwIkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADCi3yM0HU9k6aNfAAAAAElFTkSuQmCC"
},
{
    "name":"生成 深渊食尸鬼",
    "englishName":"Spawn Depths Ghoul",
    "registerName":"minecraft:spawn_egg",
    "metadata":0,
    "OredictList":[],
    "CreativeTabName":"杂项",
    "type":"Item",
    "maxStackSize":64,
    "maxDurability":1,
    "smallIcon":"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABTElEQVR42u3UzU7CQBQF4M4b8NNGoPwEdkpCW2rcom58AZ7AyFYhYoSwMsG9UYyyABNfFOOZngmOaYyAKa3c5Fs0Ib2H25lrGLva1Yplt48Xn/bOjuAfBMhmF8ucxyuo33eAgdRvkhMgeKHI5aR8XqpUwJveAIMYliVlMlJyArCxbUvlMvhvQ3CfeyAKBdjc4YwqAA9V4+ESOHK9cXN2C+6kB/Vx54uVg2xNAI7Wnw3g8H0EfPZe+8BDapgmxDcAG3PRqAbB6EW1Ct60D+oTFYugB/h1kMgD6IvHfbkGUasBD53z1AUGIL0xWac+xCAAV2gwSmfSBX8+AK5eUSrBTwH4h8yWCzEIELKIOHK1kkOuHZ+VVEpadxNGFmD/7hzYQG/MEX8LkE5LsQ3A4gKhsGt2ML4A66QJazfemgBhgdSIg2urGv91RR4gcfUB6m/wCw5XQ0AAAAAASUVORK5CYII=",
    "largeIcon":"iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAACY0lEQVR42u3cy05TYRiF4e474NCGQzkEZkpiW2qcqky4Aa6AyBQhYsQ4MsG5UYwyQBNvFIc6Wp/JDtW2z5usYRPS/2Hyp3t3OpIkSZIkSZIkSZIkSVNW/+jZXdrK4ZM43yAAAkAACAABIAAEgCbY8vJdmw0+vYzb+3ASVwEq/wYBIAAEgAAQAAJAAOivD7hZXc1bW8vb3o4b3byOq4B0er28paU8AAAAAAAAAAAAAAAAAAAAAAAA4DeA6oD7/bytrbjxj7dxwy/ncc36epwfnAAAAAAAAAAAAAAAAAAAAAAwTwCqH1Q8+ngaV13ktD3g/ds3ccPr87i9q5NWm3kgAAAAAAAAAAAAAAAAAAAAAADwx6qLlvHtZdzjn+/iqs+Pvl3EVT9I6XS7cQAAAAAAAAAAAAAAAAAAAAAAMEsAqgOuXtBQHkBx0dPs7MSNbi7iyouojY24tgCmHggAAAAAAAAAAAAAAAAAAAAAcwWg7Qsehl9fxTW7u3HVDzoGn8/iKgDV2h5wtd7BOA4AAAAAAAAAAAAAAAAAAAAAACZa9SLE4qJkcH0WN/5+GVe96LHZ3Iz71wCqf6Du02EcAAAAAAAAAAAAAAAAAAAAAABM03MD1RdcXeSUL5K85wc7qs+XW1jIm/UngwAAAAAAAAAAAAAAAAAAAACYKwAP3h/HVQfQ9oCri5jWABYX8wAAAAAAAAAAAAAAAAAAAAAAYIYAVFUvQKh23w9mPLx6Edd7vh839wcMAAAAAAAAAAAAAAAAAAAAAAATBFRexBQPtpQHLAAEgAAQAAJAAAgASZIkSZKk/69fvI0Bgn7iuSUAAAAASUVORK5CYII="
}


"""

json_dir = "./export"
icon_dir = "./.workspace/icons"

if not os.path.exists(icon_dir):
    os.mkdir(icon_dir)

def export_icon(mod_filename:str):
    file = open(os.path.join(json_dir, mod_filename), mode="r", encoding="utf-8")
    json_obj = json.loads("[" + file.read() + "]")
    file.close()
    mod_name = mod_filename.split("_item")[0]
    mod_dir = os.path.join(icon_dir, mod_name)
    if not os.path.exists(mod_dir):
        os.mkdir(mod_dir)
    _name_json_file = open(os.path.join(mod_dir, "_names.json"), "w", encoding="utf-8")
    _name_dict = {}
    for item_info in json_obj:
        resource_location = item_info.get("registerName").split(":")
        icon_name = resource_location[0] + "__" + resource_location[1] + "__" + str(item_info.get("metadata"))
        icon_file_path = os.path.join(mod_dir, icon_name) + ".png"
        if not os.path.exists(icon_file_path):
            icon_file = open(icon_file_path, "wb")
            smallIcon = base64.b64decode(item_info.get("smallIcon"))
            icon_file.write(smallIcon)
            icon_file.close()
        _name_dict[item_info.get("registerName") + ":%d" % item_info.get("metadata")] = item_info.get("name")
    json.dump(_name_dict, _name_json_file, ensure_ascii=False)
    _name_json_file.close()
    

item_json_list = [filename for filename in os.listdir(json_dir) if os.path.splitext(filename)[0][-4:] == "item"]
    
for item_json in item_json_list:
    print("Exporting icons from file %s" % item_json)
    export_icon(item_json)
    print("Finished exporting icons from file %s" % item_json)



