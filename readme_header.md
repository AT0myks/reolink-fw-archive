# Reolink firmware archive

* [Download guide](#download-guide)
* [Contributing](#contributing)
* [Issues](#issues)
* [Firmwares](#firmwares)

This is an (incomplete) archive of Reolink firmwares.

I made this for a few reasons:
- I like having a firmware history that I can upgrade/downgrade to
- might help in case of reverse engineering
- only the latest firmware for a product is displayed on Reolink's download center,
[for some reason](https://community.reolink.com/post/7520)
- this means that in case a new firmware causes issues for you,
you can't even rollback unless you kept the previous one
or manage to find a link to it somewhere on the internet
- I think it's easier than their website and it shows everything in one place
- I've seen a fair amount of people asking "Do I have the latest firmware for my device?"
- allows users not to have to search or ask for a specific firmware
- easier than using the [Wayback Machine](https://web.archive.org/) 

I started working on this around the beginning of August 2022
so from then on all the firmware information comes directly from the live Reolink website.
Older firmwares mainly come from the Wayback Machine.
The rest comes from searching through both subreddits (using [Async PRAW](https://github.com/praw-dev/asyncpraw))
and from a bit of manual search.
The code used can be found in `main.py`, except the Reddit part which is not included here.

`missing.txt` contains some firmwares that I'm pretty sure exist
(if the users correctly reported their device info) but do not appear here.

The archive is auto updated automatically every day at around 4:20 AM and PM UTC.

I cannot guarantee that the info shown here is completely accurate.
All I can say is that it comes straight from the sources with minimal edits in some cases.

## Download guide

Be careful as some firmwares are beta.
You should not apply a beta firmware unless you are a beta tester and/or know what you're doing.

As long as you make sure to check that the firmware you're looking at
matches your device's model AND hardware version, you should have no problem updating.
Usually the hardware version here will be the exact same as shown in your device's info,
but sometimes one or the other will have a few characters missing at the end.
This is normal and can be ignored, unless your device is the RLC-510A or RLC-520A in which case
they both have 2 hardware versions where the second one is the same but has the `_V2` suffix.

A few things:
- models are sorted in alphanumeric order
- firmwares are sorted by date in descending order
- the date shown is not the release date of the firmware but its build date
- a PAK file is a firmware file
- a PAK file targets a single combination of device model/hardware version.
Sometimes you can install a firmware on another device and it will "work"
(because they have very similar hardware) but it is obviously not recommended
- some links (I think 3) point to a ZIP that has multiple PAK files.
Make sure to pick the right one
- some ZIPs (I think also 3) have twice the same PAK
- most download links are direct download
- if the link is a Google Drive link,
chances are it's a beta firmware. Check the notes and sources before updating

Install at your own risk.
I do not (and cannot) go out of my way to check if every firmware is stable.
If a firmware is unstable you can use the
[discussions](https://github.com/AT0myks/reolink-fw-archive/discussions) to report it.
If enough people report the same problem and it is not an isolated case,
an issue can be opened and a note could be added to the firmware to warn future users.

I offer no guarantee,
and I am not [Reolink support](https://support.reolink.com/hc/en-us/),
so please do not ask about issues related to the firmwares themselves.
If you encounter a problem after a firmware update you can discuss it but you should
[submit a request](https://support.reolink.com/hc/en-us/requests/new?ticket_form_id=4461044255641).
You can also check the official [subreddit](https://www.reddit.com/r/reolinkcam/)
to see if other users are reporting a similar issue.

## Contributing

If you see a problem or something missing,
feel free to open an issue/PR to add/fix things.

- `devices.json` can be modified to include a model or hardware version
that does not appear yet on the live website (this must be done before adding a firmware for a new device).
Pick a unique id > 100000 for each model and hardware version
(see [here](https://github.com/AT0myks/reolink-fw-archive/commit/bff34f99e453affebef27a41db6ad202f2777cf6#diff-5fcf8ac7e21bcf37430cb6e5095c2680de90403c93cf4f5f8c39f42156789358)
for an example)
- `firmwares_manual.json` can be modified to manually add a firmware,
for example a beta firmware.
It can also be used to add additional info to an existing firmware like its changelog
- the main reason to edit `pak_info.json` is to manually add info for RLN36 firmwares.
It could also be used to mark a firmware as beta and/or unstable
- there shouldn't be anything to fix in `firmwares_live.json`
- if you want to manually add a firmware for a PR,
clone the repo and run `main.py add url` (see `main.py add -h` for help)

Reolink support can provide firmwares when contacted.
If you have a firmware (or just a mirror link) that does not appear here,
you can open a PR or put in in the
[discussions](https://github.com/AT0myks/reolink-fw-archive/discussions) so that it can be added.
This can help other users who won't have to contact Reolink.
If you can give details about what changes have been made to the firmware,
it would be a nice bonus.

## Issues

- Reolink Duo PoE product URL is wrong, it points to Reolink Duo 2 PoE (to be fixed on their side)
- for some reason some images are not displayed in the readme (GitHub only?)

## Firmwares

\* means the device is discontinued.
