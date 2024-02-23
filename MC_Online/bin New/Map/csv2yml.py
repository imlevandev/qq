if __name__ == '__main__':
    Randoms = [[]for i in range(20)]
    with open("all.csv", "r") as f:
        lines = f.readlines()
        with open("Map.yml", "w") as outf:
            for line in lines[1:]:
                cells = line.strip().split(",")
                MapID = int(cells[0])
                MapName = cells[1]
                Head = int(cells[2])
                End = int(cells[3])
                Loop = int(cells[4])
                Round = int(cells[5])
                Loop = True if Loop == 1 else False
                outf.write(f"""- ID: {MapID}
  Name: {MapName}
  Head: {Head}
  End: {End}
  Loop: {Loop}
  Round: {Round}\n""")
                for i in range(6, len(cells)):
                    RandomIndex = i-6
                    assert cells[i] in ["0", "1", ""], f"MapID:{MapID} MapName:{MapName} Round:{Round} Loop:{Loop} RandomIndex:{RandomIndex} cells[i]:{cells[i]}"
                    if cells[i] == "1":
                        Randoms[RandomIndex].append(MapID)
        assert len(Randoms[0])>0, f"全部随机是空的！"
        with open("RandomMaps.yml", 'w') as outf:
            for i in range(len(Randoms)):
                if len(Randoms[i]) == 0:
                    print(f"ID为{i}的随机是空的！用全部随机替代！")
                tmp = Randoms[i] if Randoms[i] else Randoms[0]
                s = f"[{','.join(map(str, tmp))}]"
                outf.write(f"""- ID: {i}
  Maps: {s}\n""")
                