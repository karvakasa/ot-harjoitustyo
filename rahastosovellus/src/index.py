from rahasto import Rahasto


def main():
    print("hello world!")
    pankki = Rahasto(0)
    pankki.lisaa_asiakas_rahastoon("topias tallberg", 100000)
    pankki.lisaa_asiakas_rahastoon("tiia luukkonen", 500000)
    print(pankki)


if __name__ == "__main__":
    main()
