# tagtools
I use this collection of small tools to maintain the metadata of my FLAC
collection. They are added as I write them, and are probably full of bugs.
Please use these scripts with caution!

## discogs_fetch
This tool fetches metadata from discogs, and prints relevant vorbis comments to
stdout. If a discogs release url is supplied, the tool fetches that release.
Otherwise, the arguments will be used to search discogs for a relevant release.
Example:
```
~> discogs_fetch https://www.discogs.com/Wes-Montgomery-Boss-Guitar/release/10966161

PERFORMER=Jimmy Cobb (Drums)
ENGINEER=Ray Fowler
PERFORMER=Wes Montgomery (Guitar)
PERFORMER=Mel Rhyne (Organ)
GENRE=Jazz
STYLE=Hard Bop

~> simon@german-machine ~> discogs_fetch beethoven symphonie no. 5 karajan berliner philharmoniker
Release 0:
        https://www.discogs.com/Beethoven-Karajan-Berliner-Philharmoniker-Symphonie-No6-Pastorale/release/3283755
        Symphonie No.6 »Pastorale«
        Ludwig van Beethoven, Herbert von Karajan, Berliner Philharmoniker
Release 1:
        https://www.discogs.com/Beethoven-Berliner-Philharmoniker-Herbert-von-Karajan-Symphonie-No5/release/11116488
        Symphonie No.5
        Ludwig van Beethoven, Berliner Philharmoniker, Herbert von Karajan
[...]
> 0

CONDUCTOR=Herbert von Karajan
ENGINEER=Günter Hermanns
ENSEMBLE=Berliner Philharmoniker
GENRE=Classical
STYLE=Romantic
~>
```

## musicbrainzperformer.py
Works similarly to `discogs_fetch`, but fetches data from discogs. The argument
is a musicbrainz recording id. Example:
```
~> musicbrainzperformer.py d9d96859-587a-44a3-bbe5-4f7c42adf601
PERFORMER=Ralph Burns (vibraphone)
PERFORMER=Kenny Clarke (drums)
PERFORMER=Barry Galbraith (guitar)
PERFORMER=Milt Jackson (vibraphone)
PERFORMER=John Lewis (piano)
PERFORMER=Oscar Pettiford (bass)
RECORDINGLOCATION=New York
RECORDINGDATE=1956-01-21
~>
```

## tagappend
Can be used to manually append tags to flac files. The tool will open a
temporary text file in `vim`. When `vim` exits, the content of the text file
will get appended to each flac file. Example:
```
~/music/Davis, Miles/Kind of Blue> tagappend *.flac
# Append in vim
ARTIST=Miles Davis
# Save file in vim
~/music/Davis, Miles/Kind of Blue>
```

## tagclean
Removes duplicate or tags with empty value. This script does not handle
multiline tags, and will exit on those. Example:
```
~> tagclean file_with_duplicate_tags.flac
```

## tagedit
Opens the metadata of a flac file in a temporary file using `vim`. Once vim
exits, the content of the temporary file is used to replace the previous
metadata of the flac file. Example:
```
~> tagedit test.flac
```

## tageditmany
Edits the value of one particular tag for multiple flac files, using vim. The
lines in the temporary file that is opened in vim are of the format
`TAG|file.flac`. I use this tool to add a tag that is similar to an existing
tag. For example, I will run `tageditmany TITLE *.flac`, and use a regular
expression to rewrite the `TITLE` tags to `WORK` tags, for discs with multiple
classical works on them.

## taggrep
Grep for metadata, case insensitive, among one or more flac files. Example:
```
~> taggrep '^PERFORMER=John Coltrane' *.flac
```

## taglintclassical, taglintjazz, and taglint
Suggests missing tags for classical or jazz music. Also highlights emtpy or
duplicate tags. Example:
```
~> taglintclassical *.flac
some_file.flac  PERFORMER
``` 
This means that `some_file.flac` does not have a `PERFORMER` tag.

The `taglint` script is an implementation detail for `taglintclassical` and
`taglintjazz`.

## tagmusicbrainz
Uses `musicbrainzperformer.py` to populate tags for files automatically. This
script only works if the files already have a `MUSICBRAINZ_TRACKID` tag. The
first argument of the script determines if the script writes the tags to the
flac files, or to stdout.
Example:
```
~> tagmusicbrainz no *.flac
~/music/Davis, Miles/Kind of Blue> tagmusicbrainz no *.flac
01 So What.flac
PERFORMER=Cannonball Adderley (alto saxophone)
PERFORMER=Paul Chambers (double bass)
PERFORMER=Jimmy Cobb (drums)
PERFORMER=John Coltrane (tenor saxophone)
PERFORMER=Miles Davis (trumpet)
PERFORMER=Bill Evans (piano)
RECORDINGLOCATION=CBS 30th Street Studio, 207 East 30th Street, Manhattan, New
York City
RECORDINGDATE=1959-03-02
[...]
~/music/Davis, Miles/Kind of Blue> tagmusicbrainz yes *.flac
~/music/Davis, Miles/Kind of Blue>
```
