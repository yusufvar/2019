def kembalian(uang,barang):
    susuk=uang-barang
    daf=[500,1000,2000,5000,10000,20000,50000]
    ha=[]

    while susuk != 0:
        if susuk in daf:
            ha.append(susuk)
            susuk=0;
        elif susuk>max(daf):
            susuk-=max(daf)
            ha.append(max(daf))
        elif susuk<max(daf) and susuk>min(daf):
            temp=[]
            for y in daf:
                if y<susuk:
                    temp.append(y)
            susuk-=max(temp)
            ha.append(max(temp))
        else:
            ha.append(susuk)
            susuk=0
    
    print(ha)

kembalian(50000,15500)