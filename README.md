# TorrentClient

## Intro

This is a simple torrent file client with the sole purpose of slowly learning how the technologies function using Python, I might move to writing it in C++ once I am comfortable enough.  

## Parsing

The parser is extremely simple, it just takes the given file and reads the content, then decoding it using bencodepy (since I didn't want to get too deeply into parsing and stuff.). it then takes each attribute and decodes it from the SHA1, then reading the info and returning it as a dictionary.