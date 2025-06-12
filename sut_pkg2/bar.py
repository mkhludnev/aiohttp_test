


def sut(cnt):
    if cnt>0:
        import sut_pkg2
        recuse_res = sut_pkg2.sut(cnt-1)
        print("recurse call "+ str(recuse_res))
        return 1 + recuse_res
    return 1