from PyBitTorrent import TorrentClient

def ClientProcess(file):
    client = TorrentClient(file)
    client.start()