from skpy import Skype, SkypeApiException

user = "YOUR SKYPE USER HERE"
pwd = "YOUR PASSWORD HERE"

sk = Skype(user, pwd)
chts = sk.chats.recent()
elements = {}
while chts:
  for el in chts:
    if el.startswith("19"):
      elements[el] = chts.get(el).topic

  chts = sk.chats.recent()

for k,v in elements.items():
  try:
    print("Saying bye to: ", k)
    sk.chats.chat(k).sendMsg("PS. https://github.com/Faresis/skype-groups-remover/blob/main/remove_skype_groups.py")
    print("Leaving: ", k) 
    sk.chats.chat(k).leave()
    print("Left successfully!")
    sk.chats.chat(k).delete()
    print("Deleted successfully!")
  except SkypeApiException as sae:
    print("Failed! :(")
    print("\tCaused by:", sae)
