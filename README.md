# Description

I really hate notification in general and I do not allow my browser to give me any notifications. I would however like to get notified when a youtuber adds a new video.
Silly project that gives you gnome notifications when a youtuber submits new content.

Add a list of youtuber names to a file `.oshiraserc`. The names should be taken from `https://youtube.com/c/<YOUTUBER NAME>/videos`

The file should look something like this

```
pewdiepie
mrbeast6000
...
```

# Running

run application as daemon

```sh
PYTHONHASHSEED=0 python main.py -d
```

or when you want it to run

```sh
PYTHONHASHSEED=0 python main.py
```

This is still under active development and only works with gnome at the moment. Im working on a port to macOS and making a pip package for it but everything takes time.

# Future goal

I would like to be notified when a new podcast is uploaded and when new videos are online.
