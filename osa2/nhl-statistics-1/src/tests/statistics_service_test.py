import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_etsi_olemanton_pelaaja(self):
        self.stats.search("Sundin")

    def test_etsi_oleva_pelaaja(self):
        pelaaja = self.stats.search("Semenko")
        self.assertEqual(str(pelaaja), "Semenko EDM 4 + 12 = 16")
    
    def test_top(self):
        pelaajat = self.stats.top(2)
        self.assertEqual(str(pelaajat[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(str(pelaajat[1]), "Lemieux PIT 45 + 54 = 99")

    def test_team(self):
        pelaajat = self.stats.team("EDM")
        self.assertEqual(str(pelaajat[0]), "Semenko EDM 4 + 12 = 16")
        self.assertEqual(str(pelaajat[1]), "Kurri EDM 37 + 53 = 90")
        self.assertEqual(str(pelaajat[2]), "Gretzky EDM 35 + 89 = 124")

