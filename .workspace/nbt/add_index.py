import python_nbt.nbt as nbt
from python_nbt import JavaInteger

chapters = ["61404d4e", "a2d67590", "b2a6a21a", "9a4d850c", "f764b037", "92df22db", "2ccc878e"]

file = nbt.read_from_nbt_file("./config/ftbquests/normal/chapters/index.nbt")

print(hex(JavaInteger.number_bits))
print(file['index'])
[file['index'].append(JavaInteger.to_signed(idx, base=16)) for idx in chapters if idx not in file['index']]
print(file['index'])

nbt.write_to_nbt_file("./.workspace/nbt/index.nbt", file)