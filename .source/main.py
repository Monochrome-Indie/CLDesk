# My custom pymenu module, I copied the code here because it is so small and i could not get it to import from the dependencies directory.

def menu():
  return []
def menuItem(name):
  return name
def itemAppend(menuName, item):
  menuName.append(item)
def show(menuName):
  optionNum = 0
  for item in menuName:
    optionNum += 1
    print("[" + str(optionNum) + "]", item)
  option = input("\n>> ")
  try:
    return int(option) - 1
  except:
    return "err"

rootModesMenu = menu()

rootModes = {
    "testOp": "Test Option"
}

itemAppend(rootModesMenu, rootModes)

rootMode = show(rootModesMenu)