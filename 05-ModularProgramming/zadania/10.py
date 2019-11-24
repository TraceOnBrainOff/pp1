import QuadraticEquation

wsp = QuadraticEquation.czytajWspolczynniki()
dt = QuadraticEquation.obliczDelte(wsp)
pierw = QuadraticEquation.obliczPierwiastki(wsp, dt)
QuadraticEquation.wyswietlPierwiastki(pierw)
