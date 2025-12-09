from services.rahasto import Rahasto


def main():
    pankki = Rahasto(0)
    pankki.nayta_asiakkaat_ja_varat()
    pankki.lisaa_asiakas_rahastoon("topias tumpelo", 100000)
    pankki.lisaa_asiakas_rahastoon("tiia luulonen", 500000)
    pankki.nayta_asiakkaat_ja_varat()
    print(pankki)
    pankki.muuta_asiakkaan_saldo("tiia luulonen", 500000)
    pankki.maksa_asiakkaalle_kaikki("topias tumpelo")
    pankki.pyorita_vuosi_rahastoa()
    print(pankki)
    pankki.maksa_asiakkaalle_rahaa("tiia luulonen", 500000)
    print(pankki)
    pankki.nayta_asiakkaat_ja_varat()


if __name__ == "__main__":
    main()
