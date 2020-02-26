import Image


def viacGrafov(sirka, vyska,*args):

    def vytvor():
        return Image.new('RGB', (sirka, vyska), "white")

    graf = vytvor()
    sirka, vyska = graf.size

    black = (0, 0, 0)

    def vytvorGraf():
        positiveColors = [(50, 205, 50), (255, 255, 0), (127, 255, 0), (124, 252, 0), (255, 215, 0),
                 (0, 250, 154), (127, 255, 212), (0, 255, 255), (124, 252, 0)]
        negativeColors = [(178, 34, 34), (0, 0, 255), (255, 0, 0), (220, 20, 50), (255, 69, 0),
                          (0, 20, 255), (20, 0, 255), (0, 0, 0), (128, 0, 128)]
        najmensiaHodnota = min(args)

        medzera = 5
        pocetGrafov = len(args)
        najvacsiaHodnota = max(args)
        rozdiel = vyska - najvacsiaHodnota - 1
        sirkaGrafu = int(sirka / pocetGrafov) - 1

        def vykresliGrafDecrease(zacVyska, konVyska):

            for vrchnaHrana in range(zacVyska - 1, konVyska, -1):
                graf.putpixel((konPozicia, vrchnaHrana), black)
                graf.putpixel((startPozicia, vrchnaHrana), black)

            for bocnaHrana in range(startPozicia, konPozicia):
                graf.putpixel((bocnaHrana, zacVyska - 1), black)
                graf.putpixel((bocnaHrana, konVyska), black)

        def vykresliGrafIncrease(zacVyska, konVyska):
            for vrchnaHrana in range(zacVyska, konVyska):
                graf.putpixel((konPozicia, vrchnaHrana), black)
                graf.putpixel((startPozicia, vrchnaHrana), black)

            for bocnaHrana in range(startPozicia, konPozicia):
                graf.putpixel((bocnaHrana, zacVyska), black)
                graf.putpixel((bocnaHrana, konVyska), black)

        if najmensiaHodnota < 0:
            zeroPoint = vyska - abs(najmensiaHodnota)

            if najvacsiaHodnota < 0 and najmensiaHodnota < 0:
                rozdiel = vyska - abs(najmensiaHodnota) - 1

                for aktualnyGraf in range(0, pocetGrafov):
                    startPozicia = (sirkaGrafu * (aktualnyGraf - 1)) + medzera
                    konPozicia = (aktualnyGraf * sirkaGrafu) - medzera
                    hodnotaGrafu = abs(args[aktualnyGraf])
                    finalHodnota = hodnotaGrafu + rozdiel
                    vykresliGrafIncrease(1, finalHodnota)
                    for y in range(startPozicia, konPozicia):
                        for vrchnaHrana in range(2, finalHodnota):
                            graf.putpixel((y, vrchnaHrana), (negativeColors[aktualnyGraf]))
            else:
                # ZERO POINT
                for x in range(0, sirka-1):
                    graf.putpixel((x, zeroPoint), black)

                for aktualnyGraf in range(0, pocetGrafov):
                    startPozicia = (sirkaGrafu * (aktualnyGraf-1)) + medzera
                    konPozicia = (aktualnyGraf * sirkaGrafu) - medzera

                    if args[aktualnyGraf] < 0:

                        hodnotaGrafu = abs(args[aktualnyGraf]) + zeroPoint
                        minusovyRozdiel = vyska - (zeroPoint + abs(najmensiaHodnota)) - 1
                        finalHodnota = hodnotaGrafu + minusovyRozdiel
                        vykresliGrafIncrease(zeroPoint, finalHodnota)
                        for y in range(startPozicia+1, konPozicia):
                            for vrchnaHrana in range(zeroPoint+1, finalHodnota):
                                graf.putpixel((y, vrchnaHrana), (negativeColors[aktualnyGraf]))

                    else:
                        hodnotaGrafu = args[aktualnyGraf] + rozdiel
                        finalHodnota = vyska - hodnotaGrafu
                        vykresliGrafDecrease(zeroPoint, finalHodnota)
                        for y in range(startPozicia+1, konPozicia):
                            for vrchnaHrana in range(zeroPoint-1, finalHodnota,  -1):
                                graf.putpixel((y, vrchnaHrana), (positiveColors[aktualnyGraf]))

        if najmensiaHodnota > 0:
            for aktualnyGraf in range(0, pocetGrafov):
                startPozicia = (sirkaGrafu * (aktualnyGraf - 1)) + medzera
                konPozicia = (aktualnyGraf * sirkaGrafu) - medzera
                hodnotaGrafu = args[aktualnyGraf] + rozdiel
                finalHodnota = vyska - hodnotaGrafu
                for y in range(startPozicia, konPozicia):
                    for vrchnaHrana in range(vyska - 2, finalHodnota - 1, -1):
                        graf.putpixel((y, vrchnaHrana), (positiveColors[aktualnyGraf]))
                vykresliGrafDecrease(vyska, finalHodnota)

    vytvorGraf()
    graf.show()


viacGrafov(500, 500, 100, -200, 50, 80, -200)


