newlist=[]

def addtask():
    task=input("Görev ekleyin:")
    newlist.append(task)
    print("Görev başarıyla eklendi!")

def removetask():
    task=input("Görev silmek istediğinizi girin:")
    if task in newlist:
        newlist.remove(task)
        print("Görev başarıyla silindi!")
    else:
        print("Görev bulunamadı!")

def listtasks():
    if len(newlist)==0:
        print("Görev listesi boş!")
    else:
        print("Görevler:")
        for i in newlist:
            print(i)

while True:
    print("\n1. Görev ekle")
    print("2. Görev sil")
    print("3. Görevleri listele")
    print("4. çıkış")
    sonuç=input("Seçiminiz:(1/2/3/4)")

    if sonuç=="1":
        addtask()
    elif sonuç=="2":
        removetask()
    elif sonuç=="3":
        listtasks()
    elif sonuç=="4":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz giriş!")
                
