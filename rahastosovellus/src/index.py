from rahasto import Rahasto

def main():
    print("hello world!")
    pankki = Rahasto(0)
    pankki.lisaa_asiakas_rahastoon("topias tallberg", 100000)
    pankki.lisaa_asiakas_rahastoon("tiia luukkonen", 500000)
    pankki.lisaa_asiakas_rahastoon("lipevä kala", 50000)
    print(pankki)
    pankki.lisaa_saldoa_asiakkaalle("topias tallberg", 50)
    pankki.lisaa_saldoa_asiakkaalle("tiia luukkonen", 500000)
    print(pankki)
    pankki.maksa_asiakkaalle_rahaa("tiia luukkonen", 500000)
    pankki.maksa_asiakkaalle_kaikki("topias tallberg")
    print(pankki)


if __name__ == "__main__":
    main()
