total, one, two = sum(A)/3, 0, 0
        for x in A:
            if one != total: one += x
            elif two != total: two += x
            else: break
        return one == two