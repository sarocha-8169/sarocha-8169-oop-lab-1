taekwondo_olympics2020_w49k = {
    "Gold" : {'Thailand'},
    "Silver" : {'Spain'},
    "Bronze" : {'Israel'}
}

if __name__ == '__main__':
    print("The list of medals in Taekwondo Olympics 2020 women 49 kilogram :")
    for num, value in taekwondo_olympics2020_w49k.items():
        for items in value:
            print("%s received %s medal"%(items, num))
    print("The dictionary of medals is", taekwondo_olympics2020_w49k)        