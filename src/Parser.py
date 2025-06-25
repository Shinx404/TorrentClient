import bencodepy
import hashlib

def ParseTorrent(filePath):
    with open(filePath, 'rb') as f:
        torrentData = f.read()

    decoded = bencodepy.decode(torrentData)
    info = decoded[b'info']
    infoHash = hashlib.sha1(bencodepy.encode(info)).hexdigest()

    name = info.get(b'name', b'').decode()

    if b'files' in info:
        files = []
        for f in info[b'files']:
            path = "/".join(p.decode() for p in f[b'path'])
            files.append({'path': path, 'length': f[b'length']})
    else:
        files = [{'path': name, 'length': info[b'length']}]

    return {
        'name': name,
        'info_hash': infoHash,
        'files': files
    }
