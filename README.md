# Reolink firmware archive

* [Download guide](#download-guide)
* [Contributing](#contributing)
* [Issues](#issues)
* [Get notified of new firmwares](#get-notified-of-new-firmwares)
* [Download all the firmwares](#download-all-the-firmwares)
* [Firmwares](#firmwares)

This is an unofficial and incomplete collection of Reolink firmware download links.

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

Disclaimer: a small number of links have not been provided by Reolink

Most of the links are original ones, that point to files hosted by Reolink.
They mainly come from the live website,
and archives of old website pages (like their support pages).
There is also a certain amount of official links from Google Drive,
which they sometimes use for beta firmwares.
The rest are links that are either shared by Reolink, or by users who have been sent links
(via email after contacting support for example).
When the link comes from an archived page, the source is available in the notes.

The non-original links are files hosted by third-party users.
A few are hosted by myself on Google Drive.
These are files that were provided by Reolink but that we don't have the original link to anymore.
When there is no original link for a firmware, a warning is shown in the notes.
You are free to not trust these files and ignore them.
If you want to play it safe, simply go to the
[Download Center](https://reolink.com/download-center/).

Be careful as some firmwares are beta.
You should not apply a beta firmware unless you are a beta tester and/or know what you're doing.
Check the notes and sources before updating.
A warning will appear for beta firmwares.

As long as you make sure to check that the firmware you're looking at
matches your device's model AND hardware version, you should have no problem updating*.
Usually the hardware version here will be the exact same as shown in your device's info,
but sometimes one or the other will have a few characters missing at the end.
This is normal and can be ignored, unless your device is the RLC-510A or RLC-520A in which case
they both have 2 hardware versions where the second one has the same name but with the `_V2` suffix.

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
- any link might die at any time

Install at your own risk.
I do not (and cannot) go out of my way to check if every firmware is stable.
If a firmware is unstable you can use the
[discussions](https://github.com/AT0myks/reolink-fw-archive/discussions/categories/firmware-issues) to report it.
If enough people report the same problem and it is not an isolated case,
an issue can be opened and a note could be added to the firmware to warn future users.

I offer no guarantee,
and I am not [Reolink support](https://support.reolink.com/hc/en-us/),
so please do not open issues related to the firmwares themselves.
If you encounter a problem after a firmware update you can discuss it but you should
[submit a request](https://support.reolink.com/hc/en-us/requests/new?ticket_form_id=4461044255641).
You can also check the official [subreddit](https://www.reddit.com/r/reolinkcam/)
to see if other users are reporting a similar issue.

\* I have read about cases where even with the right firmware, the device rejects the
file. I am not sure if this is user error or a bug in the device's current firmware.
Some users report success after renaming the file. If you encounter this issue,
please describe it in the discussions as I would like to know more about it.

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
[discussions](https://github.com/AT0myks/reolink-fw-archive/discussions/categories/firmware-sharing) so that it can be added.
This can help other users who won't have to contact Reolink.
If you can give details about what changes have been made to the firmware,
it would be a nice bonus.

## Issues

- Reolink Duo PoE product URL is wrong, it points to Reolink Duo 2 PoE (to be fixed on their side)
- for some reason some images are not displayed in the readme (GitHub only?)

## Get notified of new firmwares

This requires a GitHub account.

In the top right of the page click `Watch`, then `Custom`, tick `Releases` and apply.

![notif](https://raw.githubusercontent.com/AT0myks/reolink-fw-archive/main/img/notif.jpg)

You should receive an email next time new firmwares are published by Reolink.

## Download all the firmwares

See [here](https://github.com/AT0myks/reolink-fw-archive/wiki).

## Firmwares

\* means the device is discontinued.

<details>
  <summary>B1200</summary>

[Product page](https://reolink.com/product/rlk8-1200b4-a/)

  ### IPC_52316M12MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2174_23050800](https://home-cdn.reolink.us/wp-content/uploads/2023/05/110627161683786436.5166.zip?download_name=B1200_23050800.zip) | 2023‑05‑08 | <ol><li>Add four-in-one (binning_mode) function, which provides image mode selection in night mode. This function can be found in the Advanced settings of the Display interface.</li><li>Optimize the clarity of OSD strokes; solve the problem that the OSD display is not clear in some scenarios.</li><li>Optimize the day and night switching function.</li><li>Optimize the Smart detection function.<ol type="a"><li>Upgrade the smart model.</li><li>Improve the recognition accuracy of person, vehicle, and pets, and optimize the problem of static smart false positives.</li></ol></li><li>Solve the problem of deviation in adjusting the brightness of the screen.</li><li>Solve the problem that the detection area does not fit after the mirror image is flipped.</li><li>Fix the bug that the night vision frame rate is incorrect in some scenes.</li></ol> | 
[v3.1.0.1105_23030900](https://home-cdn.reolink.us/wp-content/uploads/2023/03/141102511678791771.4471.zip?download_name=B1200_23030900.zip) | 2023‑03‑09 | Optimized the image quality of some scenes and fixed other known bugs | 

</details>

<details>
  <summary>B400 (Add-ons) *</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2018/08/store/rlc-410-5MP.png" width="150">

[Product page](https://reolink.com/product/b400/)

  ### IPC_5128M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.183_21012800](https://home-cdn.reolink.us/files/firmware/20210128firmware/B400_183_21012800.zip)<br />[v3.0.0.183_21012800](https://home-cdn.reolink.us/wp-content/uploads/2021/02/010356171612151777.6123.zip?download_name=firmware_B400_v300183_21012800.zip) | 2021‑01‑28 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed the bug that IPC failed to reconnect to the NVR after powering off when setting certain time zones.</li><li>Fixed some known bugs.</li></ol> | If your camera B400's hardware version does not begin with IPC_5128M, please wait for the new firmware release.<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.136_20120900](https://reolink-storage.s3.amazonaws.com/website/firmware/20201210firmware/B400_136_20120900.zip) | 2020‑12‑09 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210126120322/https://support.reolink.com/hc/en-us/articles/900004952643-12-09-2020-Firmware-for-B400-D400-B500-D500-B800-D800)
[v2.0.0.16_20041560](https://reolink-storage.s3.amazonaws.com/website/firmware/20200415firmware/B400_16_20041560(1).zip) | 2020‑04‑15 | <ol><li>Fixed the freezing issue under the complex environment of live view and playback.</li><li>Optimized system performance.</li></ol> | [Archive](https://web.archive.org/web/20210805173433/https://support.reolink.com/hc/en-us/articles/900000662366-04-15-2020-Firmware-for-B400-D400-D420-IPC-5128M-IPC-5174M-)

  ### IPC_5174MP8M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.183_21012800](https://reolink-storage.s3.amazonaws.com/website/firmware/20210128firmware/B400_183_21012800+(1).zip) | 2021‑01‑28 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed the bug that IPC failed to reconnect to the NVR after powering off when setting certain time zones.</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210616134733/https://support.reolink.com/hc/en-us/articles/900004952643-28-01-2021-Firmware-for-B400-D400-D420-B500-D500-B800-D800)
[v3.0.0.136_20121000](https://reolink-storage.s3.amazonaws.com/website/firmware/20201210firmware/B400_136_20121000.zip) | 2020‑12‑10 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210126120322/https://support.reolink.com/hc/en-us/articles/900004952643-12-09-2020-Firmware-for-B400-D400-B500-D500-B800-D800)
[v2.0.0.16_20041550](https://reolink-storage.s3.amazonaws.com/website/firmware/20200415firmware/B400_16_20041560(1).zip) | 2020‑04‑15 | <ol><li>Fixed the freezing issue under the complex environment of live view and playback.</li><li>Optimized system performance.</li></ol> | [Archive](https://web.archive.org/web/20210805173433/https://support.reolink.com/hc/en-us/articles/900000662366-04-15-2020-Firmware-for-B400-D400-D420-IPC-5128M-IPC-5174M-)

</details>

<details>
  <summary>B500 (Add-ons) *</summary>

  ### IPC_5158M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.183_21012814](https://home-cdn.reolink.us/files/firmware/20210128firmware/B500_183_21012814.zip)<br />[v3.0.0.183_21012814](https://home-cdn.reolink.us/wp-content/uploads/2021/02/010422061612153326.4775.zip?download_name=firmware_B500_v300183.zip) | 2021‑01‑28 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed the bug that IPC failed to reconnect to the NVR after powering off when setting certain time zones.</li><li>Fixed some known bugs.</li></ol> | If your camera B500's hardware version does not begin with IPC_5158M5M, please wait for the new firmware release.
[v3.0.0.136_20120914](https://reolink-storage.s3.amazonaws.com/website/firmware/20201210firmware/B500_136+_20120914.zip) | 2020‑12‑09 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210126120322/https://support.reolink.com/hc/en-us/articles/900004952643-12-09-2020-Firmware-for-B400-D400-B500-D500-B800-D800)

  ### IPC_515B8M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.183_21012814](https://home-cdn.reolink.us/files/firmware/20210128firmware/B500_183_21012814+(1).zip)<br />[v3.0.0.183_21012814](https://home-cdn.reolink.us/wp-content/uploads/2021/02/010418121612153092.6544.zip?download_name=firmware_B500_v300183.zip) | 2021‑01‑28 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed the bug that IPC failed to reconnect to the NVR after powering off when setting certain time zones.</li><li>Fixed some known bugs.</li></ol> | If your camera B500's hardware version does not begin with IPC_515B8M5M, please wait for the new firmware release.<br />.If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.136_20120914](https://reolink-storage.s3.amazonaws.com/website/firmware/20201210firmware/B500_136_20120914.zip) | 2020‑12‑09 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210126120322/https://support.reolink.com/hc/en-us/articles/900004952643-12-09-2020-Firmware-for-B400-D400-B500-D500-B800-D800)

  ### IPC_515B8M5M_V2
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2379_23062900](https://home-cdn.reolink.us/wp-content/uploads/2023/09/120318021694488682.1128.zip?download_name=B500_v3102379_23062900.zip) | 2023‑06‑29 | <ol><li>Optimize smart detection. Animal detction is added.</li><li>Optimize recording.</li><li>Optimize night vision.</li><li>Optimize the detection zone setting.</li><li>Optimze the Brightness &amp; Shadows setting.</li><li>Optimize some network features and fix some bugs</li></ol> | 

</details>

<details>
  <summary>B800 (Add-ons) *</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2019/02/b800-400.png" width="150">

[Product page](https://reolink.com/product/b800/)

  ### IPC_5158M8M_V2
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2379_23062702](https://home-cdn.reolink.us/wp-content/uploads/2023/09/120404371694491477.9399.zip?download_name=B800_v3102379_23062702.zip) | 2023‑06‑27 | <ol><li>Optimize smart detection. Animal detction is added.</li><li>Optimize recording.</li><li>Optimize night vision.</li><li>Optimize the detection zone setting.</li><li>Optimze the Brightness &amp; Shadows setting.</li><li>Optimize some network features and fix some bugs</li></ol> | 

  ### IPC_5158MP8M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.183_21012800](https://home-cdn.reolink.us/files/firmware/20210128firmware/B800_183_21012800.zip)<br />[v3.0.0.183_21012800](https://home-cdn.reolink.us/wp-content/uploads/2021/02/010459481612155588.6254.zip?download_name=firmware_B800_v300183.zip) | 2021‑01‑28 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed the bug that IPC failed to reconnect to the NVR after powering off when setting certain time zones.</li><li>Fixed some known bugs.</li></ol> | If your camera B800's hardware version does not begin with IPC_5158MP8M, please wait for the new firmware release.<br />.If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.136_20120900](https://reolink-storage.s3.amazonaws.com/website/firmware/20201210firmware/B800_136_20120900.zip) | 2020‑12‑09 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210126120322/https://support.reolink.com/hc/en-us/articles/900004952643-12-09-2020-Firmware-for-B400-D400-B500-D500-B800-D800)
[v2.0.0.17_20042200](https://reolink-storage.s3.amazonaws.com/website/firmware/20200422firmware/B800_17_20042200.zip) | 2020‑04‑22 | <ol><li>Fixed the freezing issue under the complex environment of live view and playback.</li><li>Optimized system performance.</li></ol> | [Archive](https://web.archive.org/web/20210726205241/https://support.reolink.com/hc/en-us/articles/900000744606-04-22-2020-Firmware-for-B800-D800-IPC-5158MP8M-)

</details>

<details>
  <summary>C1 *</summary>

[Product page](https://reolink.com/product/c1/)

  ### IPC_36S16MHSM
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1389_18081414](https://cdn.reolink.com/files/firmware/20180814firmware/C1_1389_18081414.zip)<br />[v2.0.0.1389_18081414](https://home-cdn.reolink.us/files/firmware/20180814firmware/C1_1389_18081414.zip)<br />[v2.0.0.1389_18081414](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/C1_1389_18081414.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020714](https://cdn.reolink.com/files/firmware/20180402firmware/C1_1288_18020714.zip)<br />[v2.0.0.1288_18020714](https://home-cdn.reolink.us/files/firmware/20180402firmware/C1_1288_18020714.zip)<br />[v2.0.0.1288_18020714](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/C1_1288_18020714.zip) | 2018‑02‑07 |  | 
[v2.0.0.889_17083000](https://cdn.reolink.com/files/firmware/889_1708/C1_889_17083000.zip)<br />[v2.0.0.889_17083000](https://home-cdn.reolink.us/files/firmware/889_1708/C1_889_17083000.zip)<br />[v2.0.0.889_17083000](https://s3.amazonaws.com/reolink-storage/website/firmware/889_1708/C1_889_17083000.zip) | 2017‑08‑30 |  | 
[v2.0.0.842_17052400](https://s3.amazonaws.com/reolink-storage/website/firmware/842_170524/C1_842_17052400.zip) | 2017‑05‑24 |  | 
[v2.0.0.675_17032700](https://s3.amazonaws.com/reolink-storage/website/firmware/675_170317/C1_675_17032700.zip) | 2017‑03‑27 |  | 

</details>

<details>
  <summary>C1-Pro *</summary>

[Product page](https://reolink.com/product/c1-pro/)

  ### IPC_3816MPT
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1441_19032105](https://s3.amazonaws.com/reolink-storage/website/firmware/20190321firmware/C1-Pro_1441_19032105.zip) | 2019‑03‑21 | Fixed security flaws. | [Archive](https://web.archive.org/web/20210805103139/https://support.reolink.com/hc/en-us/articles/360021715373-03-21-2019-Firmware-for-Reolink-IP-Cameras-IPC-3816M-)
[v2.0.0.1389_18081405](https://cdn.reolink.com/files/firmware/20180814firmware/C1-Pro_1389_18081405.zip)<br />[v2.0.0.1389_18081405](https://home-cdn.reolink.us/files/firmware/20180814firmware/C1-Pro_1389_18081405.zip)<br />[v2.0.0.1389_18081405](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/C1-Pro_1389_18081405.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020705](https://cdn.reolink.com/files/firmware/20180402firmware/C1-Pro_1288_18020705.zip)<br />[v2.0.0.1288_18020705](https://home-cdn.reolink.us/files/firmware/20180402firmware/C1-Pro_1288_18020705.zip)<br />[v2.0.0.1288_18020705](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/C1-Pro_1288_18020705.zip) | 2018‑02‑07 |  | 
[v2.0.0.889_17083009](https://s3.amazonaws.com/reolink-storage/website/firmware/889_1708/C1-Pro-889_1708300.zip) | 2017‑08‑30 |  | 

  ### IPC_51316M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.136_20121103](https://drive.google.com/uc?id=1U19KqoRH11GHrpvzlqjgG7SbnyQ6HF7s&confirm=t) | 2020‑12‑11 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/k4cym7/c1_pro_firmware_question/)<br />[Source 2](https://www.reddit.com/r/reolinkcam/comments/k6u5me/c2_pro_eol_less_than_2_years_no_more_firmware/giej4k9/)
[v3.0.0.121_20111903](https://drive.google.com/uc?id=1QqluF6z09XUu8ZUppidZb_k7Jz0gS809&confirm=t)<br />[v3.0.0.121_20111903](https://support.reolink.com/attachments/token/uhbOsutx7SUg1lLF13NuA0hvD/?name=IPC_51316M.121_20111903.C1-Pro.ov4689.4MP.WIFI1021.PT.REOLINK.IPC_51316M) | 2020‑11‑19 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/k4cym7/c1_pro_firmware_question/)
[v2.0.0.448_19061405](https://reolink-storage.s3.amazonaws.com/website/firmware/20190614firmware/C1-Pro_448_19061405(1).zip) | 2019‑06‑14 | <ol><li>Fixed the issue where the WiFi can't reconnect after rebooting.</li><li>Fixed the issue where the sound becomes smaller after frequently switching the audio.</li><li>Add the smart home feature (Google Home).</li><li>Optimize the breathing effect.</li><li>Fixed the drop issue where RTSP previewing.</li><li>Fixed the IR-cut switching failure problem on part of cameras.</li><li>Add power LED control function to C1 Pro.</li><li>Add manually trigger and automatic voice alarm function to C1 Pro.</li></ol> | [Archive](https://web.archive.org/web/20210805171119/https://support.reolink.com/hc/en-us/articles/360025688034-06-14-2019-Firmware-for-Reolink-IP-Cameras-IPC-51316M-)

</details>

<details>
  <summary>C2 *</summary>

[Product page](https://reolink.com/product/c2-series/)

  ### IPC_3816MPT
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1441_19032104](https://s3.amazonaws.com/reolink-storage/website/firmware/20190321firmware/C2_1441_19032104.zip) | 2019‑03‑21 | Fixed security flaws. | [Archive](https://web.archive.org/web/20210805103139/https://support.reolink.com/hc/en-us/articles/360021715373-03-21-2019-Firmware-for-Reolink-IP-Cameras-IPC-3816M-)
[v2.0.0.1389_18081404](https://cdn.reolink.com/files/firmware/20180814firmware/C2_1389_18081404.zip)<br />[v2.0.0.1389_18081404](https://home-cdn.reolink.us/files/firmware/20180814firmware/C2_1389_18081404.zip)<br />[v2.0.0.1389_18081404](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/C2_1389_18081404.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020704](https://cdn.reolink.com/files/firmware/20180402firmware/C2_1288_18020704.zip)<br />[v2.0.0.1288_18020704](https://home-cdn.reolink.us/files/firmware/20180402firmware/C2_1288_18020704.zip)<br />[v2.0.0.1288_18020704](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/C2_1288_18020704.zip) | 2018‑02‑07 |  | 
[v2.0.0.889_17083009](https://s3.amazonaws.com/reolink-storage/website/firmware/889_1708/C2_889_17083009.zip) | 2017‑08‑30 |  | 
[v2.0.0.842_17052409](https://s3.amazonaws.com/reolink-storage/website/firmware/842_170524/C2_842_17052409.zip) | 2017‑05‑24 |  | 
[v2.0.0.675_17032709](https://s3.amazonaws.com/reolink-storage/website/firmware/675_170317/C2_675_17032709.zip) | 2017‑03‑27 |  | 

</details>

<details>
  <summary>C2-Pro *</summary>

[Product page](https://reolink.com/product/c2-pro/)

  ### IPC_51516M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.136_20121107](https://drive.google.com/uc?id=1O3VmNf3UMLrsItcwiUEEPyRNXdyqfhhq&confirm=t) | 2020‑12‑11 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/k6u5me/c2_pro_eol_less_than_2_years_no_more_firmware/giej4k9/)<br />[Source 2](https://www.reddit.com/r/reolinkcam/comments/kfs32v/comment/gtwsd7x/)
[v2.0.0.654_20040908](https://reolink-storage.s3.amazonaws.com/website/firmware/20200409firmware/C2-Pro_654_20040908.zip) | 2020‑04‑09 | <ol><li>Extended the max password length of Email, FTP, and DDNS to 128 digits.</li><li>Updated the max cruise time to 300 seconds.</li></ol> | [Archive](https://web.archive.org/web/20210803033747/https://support.reolink.com/hc/en-us/articles/900000854106-04-09-2020-Firmware-for-Reolink-Auto-focus-IP-Cameras-IPC-51516M-)
[v2.0.0.477_19071504](https://reolink-storage.s3.amazonaws.com/website/firmware/20190715firmware/C2-Pro_477_19071504.zip) | 2019‑07‑15 | <ol><li>Add the smart home feature (Google Home).</li><li>Fixed AF learning table compatibility issues.</li><li>Improved P2P connectivity.</li><li>Fixed the IR-cut switching failure problem on part of cameras.</li><li>Modified the AF library and optimize the AF focus.</li><li>Optimize noise problems of PTZ audio.</li><li>Add power LED control function to C2 Pro.</li><li>Add manually trigger and automatic voice alarm function to C2 Pro.</li><li>Fixed the issue where the WiFi can't reconnect after rebooting.</li></ol> | [Archive](https://web.archive.org/web/20190905192627/https://support.reolink.com/hc/en-us/articles/360032028313-07-15-2019-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)

</details>

<details>
  <summary>CX410</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2023/05/160656001684220160.3717.png" width="150">

[Product page](https://reolink.com/us/product/cx410/)

  ### IPC_NT1NA44MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2501_23072503](https://home-cdn.reolink.us/wp-content/uploads/2023/09/010311281693537888.5417.zip?download_name=CX410_2501_23072503.zip) | 2023‑07‑25 | <ol><li>Optimize the Spolight modes</li><li>Optimize the night vision</li><li>Add HDR switch</li><li>Fix some known bugs</li></ol> | 

</details>

<details>
  <summary>D1200</summary>

[Product page](https://reolink.com/product/rlk8-1200d4-a/)

  ### IPC_52316M12MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2174_23050801](https://home-cdn.reolink.us/wp-content/uploads/2023/05/110632191683786739.9125.zip?download_name=D1200_23050801.zip) | 2023‑05‑08 | <ol><li>Add four-in-one (binning_mode) function, which provides image mode selection in night mode. This function can be found in the Advanced settings of the Display interface.</li><li>Optimize the clarity of OSD strokes; solve the problem that the OSD display is not clear in some scenarios.</li><li>Optimize the day and night switching function.</li><li>Optimize the Smart detection function.<ol type="a"><li>Upgrade the smart model.</li><li>Improve the recognition accuracy of person, vehicle, and pets, and optimize the problem of static smart false positives.</li></ol></li><li>Solve the problem of deviation in adjusting the brightness of the screen.</li><li>Solve the problem that the detection area does not fit after the mirror image is flipped.</li><li>Fix the bug that the night vision frame rate is incorrect in some scenes.</li></ol> | 
[v3.1.0.1105_23030901](https://home-cdn.reolink.us/wp-content/uploads/2023/03/141104001678791840.9366.zip?download_name=D1200_23030901.zip) | 2023‑03‑09 | Optimized the image quality of some scenes and fixed other known bugs | 

</details>

<details>
  <summary>D400 (Add-ons) *</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2018/05/rlc-420-340.png" width="150">

[Product page](https://reolink.com/product/d400/)

  ### IPC_5128M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.183_21012801](https://home-cdn.reolink.us/files/firmware/20210128firmware/D400_183_21012801.zip)<br />[v3.0.0.183_21012801](https://home-cdn.reolink.us/wp-content/uploads/2021/02/010436131612154173.5661.zip?download_name=firmware_D400_v300183.zip) | 2021‑01‑28 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed the bug that IPC failed to reconnect to the NVR after powering off when setting certain time zones.</li><li>Fixed some known bugs.</li></ol> | If your camera D400's hardware version does not begin with IPC_5128M, please wait for the new firmware release.<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.136_20120901](https://reolink-storage.s3.amazonaws.com/website/firmware/20201210firmware/D400_136_20120901.zip) | 2020‑12‑09 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210126120322/https://support.reolink.com/hc/en-us/articles/900004952643-12-09-2020-Firmware-for-B400-D400-B500-D500-B800-D800)
[v2.0.0.16_20041561](https://reolink-storage.s3.amazonaws.com/website/firmware/20200415firmware/D400_16_20041561(1).zip) | 2020‑04‑15 | <ol><li>Fixed the freezing issue under the complex environment of live view and playback.</li><li>Optimized system performance.</li></ol> | [Archive](https://web.archive.org/web/20210805173433/https://support.reolink.com/hc/en-us/articles/900000662366-04-15-2020-Firmware-for-B400-D400-D420-IPC-5128M-IPC-5174M-)

  ### IPC_5174MP8M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.183_21012801](https://home-cdn.reolink.us/files/firmware/20210128firmware/D400_183_21012801+(2).zip) | 2021‑01‑28 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed the bug that IPC failed to reconnect to the NVR after powering off when setting certain time zones.</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210616134733/https://support.reolink.com/hc/en-us/articles/900004952643-28-01-2021-Firmware-for-B400-D400-D420-B500-D500-B800-D800)
[v3.0.0.136_20121001](https://reolink-storage.s3.amazonaws.com/website/firmware/20201210firmware/D400_136_20121001.zip) | 2020‑12‑10 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210126120322/https://support.reolink.com/hc/en-us/articles/900004952643-12-09-2020-Firmware-for-B400-D400-B500-D500-B800-D800)
[v2.0.0.16_20041551](https://reolink-storage.s3.amazonaws.com/website/firmware/20200415firmware/D400_16_20041561(1).zip) | 2020‑04‑15 | <ol><li>Fixed the freezing issue under the complex environment of live view and playback.</li><li>Optimized system performance.</li></ol> | [Archive](https://web.archive.org/web/20210805173433/https://support.reolink.com/hc/en-us/articles/900000662366-04-15-2020-Firmware-for-B400-D400-D420-IPC-5128M-IPC-5174M-)

</details>

<details>
  <summary>D420 *</summary>

  ### IPC_5128M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.183_21012802](https://reolink-storage.s3.amazonaws.com/website/firmware/20210128firmware/D420.183_21012802.zip) | 2021‑01‑28 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed the bug that IPC failed to reconnect to the NVR after powering off when setting certain time zones.</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210616134733/https://support.reolink.com/hc/en-us/articles/900004952643-28-01-2021-Firmware-for-B400-D400-D420-B500-D500-B800-D800)
[v2.0.0.16_20041562](https://reolink-storage.s3.amazonaws.com/website/firmware/20200415firmware/D420_16_20041562.zip) | 2020‑04‑15 | <ol><li>Fixed the freezing issue under the complex environment of live view and playback.</li><li>Optimized system performance.</li></ol> | [Archive](https://web.archive.org/web/20210805173433/https://support.reolink.com/hc/en-us/articles/900000662366-04-15-2020-Firmware-for-B400-D400-D420-IPC-5128M-IPC-5174M-)

  ### IPC_5174MP8M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.183_21012802](https://reolink-storage.s3.amazonaws.com/website/firmware/20210128firmware/D420_183_21012802.(1).zip) | 2021‑01‑28 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed the bug that IPC failed to reconnect to the NVR after powering off when setting certain time zones.</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210616134733/https://support.reolink.com/hc/en-us/articles/900004952643-28-01-2021-Firmware-for-B400-D400-D420-B500-D500-B800-D800)

</details>

<details>
  <summary>D500 (Add-ons) *</summary>

  ### IPC_5158M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.183_21012815](https://home-cdn.reolink.us/files/firmware/20210128firmware/D500_183_21012815.zip)<br />[v3.0.0.183_21012815](https://home-cdn.reolink.us/wp-content/uploads/2021/02/010456561612155416.1477.zip?download_name=firmware_D500_v300183.zip) | 2021‑01‑28 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed some known bugs.</li></ol> | If your cameraD500's hardware version does not begin with IPC_5158M5M, please wait for the new firmware release.
[v3.0.0.136_20120915](https://reolink-storage.s3.amazonaws.com/website/firmware/20201210firmware/D500_136_+20120915.zip) | 2020‑12‑09 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210126120322/https://support.reolink.com/hc/en-us/articles/900004952643-12-09-2020-Firmware-for-B400-D400-B500-D500-B800-D800)

  ### IPC_515B8M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.183_21012815](https://home-cdn.reolink.us/files/firmware/20210128firmware/D500_183_21012815+(2).zip)<br />[v3.0.0.183_21012815](https://home-cdn.reolink.us/wp-content/uploads/2022/06/170431531655440313.0447.zip?download_name=firmware_D500_v300183_21012815.zip) | 2021‑01‑28 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed the bug that IPC failed to reconnect to the NVR after powering off when setting certain time zones.</li><li>Fixed some known bugs.</li></ol> | If your cameraD500's hardware version does not begin with IPC_515B8M5M, please wait for the new firmware release.
[v3.0.0.136_20120915](https://home-cdn.reolink.us/files/firmware/20210128firmware/D500_183_21012815+(2).zip)<br />[v3.0.0.136_20120915](https://reolink-storage.s3.amazonaws.com/website/firmware/20201210firmware/D500_136_20120915.zip) | 2020‑12‑09 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed the bug that IPC failed to reconnect to the NVR after powering off when setting certain time zones.</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210616134733/https://support.reolink.com/hc/en-us/articles/900004952643-28-01-2021-Firmware-for-B400-D400-D420-B500-D500-B800-D800)

  ### IPC_515B8M5M_V2
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2379_23062901](https://home-cdn.reolink.us/wp-content/uploads/2023/09/120313091694488389.8595.zip?download_name=D500_v3102379_23062901.zip) | 2023‑06‑29 | <ol><li>Optimize smart detection. Animal detction is added.</li><li>Optimize recording.</li><li>Optimize night vision.</li><li>Optimize the detection zone setting.</li><li>Optimze the Brightness &amp; Shadows setting.</li><li>Optimize some network features and fix some bugs</li></ol> | 

</details>

<details>
  <summary>D800 (Add-ons) *</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2022/01/130955131642067713.6912.png" width="150">

[Product page](https://reolink.com/product/d800/)

  ### IPC_5158M8M_V2
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2379_23062703](https://home-cdn.reolink.us/wp-content/uploads/2023/09/120401221694491282.9054.zip?download_name=D800_v3102379_23062703.zip) | 2023‑06‑27 | <ol><li>Optimize smart detection. Animal detction is added.</li><li>Optimize recording.</li><li>Optimize night vision.</li><li>Optimize the detection zone setting.</li><li>Optimze the Brightness &amp; Shadows setting.</li><li>Optimize some network features and fix some bugs</li></ol> | 

  ### IPC_5158MP8M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.183_21012801](https://home-cdn.reolink.us/wp-content/uploads/2021/02/010502501612155770.6573.zip?download_name=firmware_D800_v300183.zip)<br />[v3.0.0.183_21012801](https://reolink-storage.s3.amazonaws.com/website/firmware/20210128firmware/D800_183_21012801.zip) | 2021‑01‑28 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed the bug that IPC failed to reconnect to the NVR after powering off when setting certain time zones.</li><li>Fixed some known bugs.</li></ol> | If your camera D800's hardware version does not begin with IPC_5158MP8M, please wait for the new firmware release.
[v3.0.0.136_20120901](https://reolink-storage.s3.amazonaws.com/website/firmware/20201210firmware/D800_136_20120901.zip) | 2020‑12‑09 | <ol><li>Optimize the effect of the day and night switch.</li><li>Optimize network transmission.</li><li>Optimize the alert caused by the Day and Night switching.</li><li>When obtaining the IP address by DHCP, the hostname will be changed to the device name (OSD name).</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210126120322/https://support.reolink.com/hc/en-us/articles/900004952643-12-09-2020-Firmware-for-B400-D400-B500-D500-B800-D800)
[v2.0.0.17_20042201](https://reolink-storage.s3.amazonaws.com/website/firmware/20200422firmware/D800_17_20042201.zip) | 2020‑04‑22 | <ol><li>Fixed the freezing issue under the complex environment of live view and playback.</li><li>Optimized system performance.</li></ol> | [Archive](https://web.archive.org/web/20210726205241/https://support.reolink.com/hc/en-us/articles/900000744606-04-22-2020-Firmware-for-B800-D800-IPC-5158MP8M-)

</details>

<details>
  <summary>E1</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2019/05/e1-pro-400.png" width="150">

[Product page](https://reolink.com/product/e1/)

  ### IPC_517SD5
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2356_23062000](https://home-cdn.reolink.us/wp-content/uploads/2023/08/301024131693391053.6834.zip?download_name=517_SD5_2356_23062000.zip) | 2023‑06‑20 | <ol><li>Optimize the network feature</li><li>Update the web UI version</li><li>Optimize the PTZ function</li><li>Optimize the WiFi connection</li><li>Fix some known bugs</li></ol> | 
[v3.0.0.597_21091045](https://drive.google.com/uc?id=1jhwoGJVCX6wslKBQsa1cpO6AQXNyxFjo&confirm=t) | 2021‑09‑10 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/rdm8cl/where_is_the_firmware_for_e1_wifi_camera/hofyqqt/)<br />[Source 2](https://drive.google.com/drive/folders/1hqBOSZ_KK6UUR6km2smkAWADVogVTAyb)
[v3.0.0.115_20102200](https://home-cdn.reolink.us/wp-content/uploads/2020/12/200448021608439682.2159.zip?download_name=firmware_E1_115_20102200.zip)<br />[v3.0.0.115_20102200](https://reolink-storage.s3.amazonaws.com/website/firmware/20201022firmware+/E1_115_20102200.zip) | 2020‑10‑22 | <ol><li>Added the preset feature.</li><li>Fixed the problem that the email test fails when the email password is blank.</li><li>Optimized cloud transmission performance.</li><li>Optimized the network transmission protocol.</li><li>Fixed some known bugs.</li></ol> | This firmware is ONLY for E1(with hardware version IPC_517SD5).<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.42_20062900](https://reolink-storage.s3.amazonaws.com/website/firmware/20200629firmware/E1_42_20062900.zip) | 2020‑06‑29 | <ol><li>Added multiple languages for the voice prompt when scanning the QR code to set up the camera.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed the bug when connecting the camera in different Vlan via Reolink app/client.</li></ol> | [Archive](https://web.archive.org/web/20200926093027/https://support.reolink.com/hc/en-us/articles/900001664643-06-29-2020-Firmware-for-E1-IPC-517SD5-and-E1-Pro-513SD5-)

  ### IPC_566SD53MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2647_23083100](https://home-cdn.reolink.us/wp-content/uploads/2023/10/090413121696824792.4352.zip?download_name=E1_v3102647_23083100.zip) | 2023‑08‑31 | <ol><li>Optimize smart detection</li><li>Optimize the network module</li><li>Optimize calibration</li><li>Optimize recording</li><li>Fix some known bugs</li></ol> | 

</details>

<details>
  <summary>E1 Outdoor</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/03/050715191614928519.1298.png" width="150">

[Product page](https://reolink.com/product/e1-outdoor/)

  ### IPC_523SD8
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.1643_23041100](https://support-d.reolink.com/attachments/token/OGUN4y1IYPT4H54LKgv4FrnPk/?name=IPC_523SD8.1643_23041100.E1-Outdoor.OV05A10.5MP.WIFI1021.PTZ.REOLINK.pak) | 2023‑04‑11 |  | 
[v3.1.0.1643_22122400](https://support.reolink.com/attachments/token/earovP2n9ndB7vFrzTAbtAQsS/?name=IPC_523SD8.1643_22122400.E1-Outdoor.OV05A10.5MP.WIFI1021.PTZ.REOLINK.pak) | 2022‑12‑24 |  | [Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/5)
[v3.1.0.1584_22120966](https://support-d.reolink.com/attachments/token/rngyK0yBtNIqpdAEaAuUDtfVr/?name=IPC_523SD8.1584_22120966.E1-Outdoor.OV05A10.5MP.WIFI1021.PTZ.REOLINK.pak) | 2022‑12‑09 |  | [Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/11)
[v3.1.0.1348_220922660](https://drive.google.com/uc?id=12gn4NVw4v_DABQ8b_XKmQJ3tUFId2n7y&confirm=t) | 2022‑09‑22 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)
[v3.1.0.989_22071306](https://drive.google.com/uc?id=1iduVRpBXk2vw4L7V4cSASzkSbDl0upBX&confirm=t) | 2022‑07‑13 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)
[v3.1.0.956_22041506](https://drive.google.com/uc?id=1piUxktFScSkI622ThgOzKexD1UdgFPI4&confirm=t) | 2022‑04‑15 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)
[v3.1.0.804_22012406](https://support-d.reolink.com/attachments/token/3FVDyr7FnfXKiHrbI3ihfGwzW/?name=IPC_523SD8.804_22012406.E1-Outdoor.OV05A10.5MP.WIFI1021.PTZ.REOLINK%28open_ai_trace%29.pak) | 2022‑01‑24 | Supports animal detection | [Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/16)
[v3.1.0.804_22011506](https://support.reolink.com/attachments/token/7k5v4dY8P7nXXGfNynLxQNkOh/?name=IPC_523SD8.804_22011506.E1-Outdoor.OV05A10.5MP.WIFI1021.PTZ.REOLINK.pak) | 2022‑01‑15 |  | [Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/9)
[v3.0.0.197_21022706](https://reolink-storage.s3.amazonaws.com/website/firmware/20210227firmware/E1-Outdoor.197_21022706..zip) | 2021‑02‑27 | <ol><li>Solved the problem that some APP versions are not compatible with the automatic tracking function and the spotlight function.</li><li>Optimized the auto tracking function.</li><li>Optimized the PTZ function.</li><li>Optimized Person and Vehicle Detection.</li></ol> | [Archive](https://web.archive.org/web/20210613000536/https://support.reolink.com/hc/en-us/articles/900005803523-27th-Feb-2021-Firmware-for-E1-Outdoor-IPC-523SD8-)

  ### IPC_566SD85MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2649_23083102](https://home-cdn.reolink.us/wp-content/uploads/2023/10/090316201696821380.1856.zip?download_name=E1Outdoor_v3102649_23083102.zip) | 2023‑08‑31 | <ol><li>Optimize smart detection</li><li>Optimize auto-tracking</li><li>Optimize the network module</li><li>Optimize calibration</li><li>Optimize recording</li><li>Fix some known bugs</li></ol> | 

</details>

<details>
  <summary>E1 Outdoor Pro</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2023/05/160805511684224351.237.png" width="150">

[Product page](https://reolink.com/__/product/e1-outdoor-pro/)

  ### IPC_560SD88MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2515_23072809](https://home-cdn.reolink.us/wp-content/uploads/2023/08/291037231693305443.7283.zip?download_name=E1_Outdoor_Pro_2515_23072809.zip) | 2023‑07‑28 |  | 1. Optimize and solve some known bugs of the WiFi connection<br />2. Optimize Auto-tracking <br />3. Optimize Auto-focus<br />4. Optimzie Email Alert<br />5. Solve other known bugs

</details>

<details>
  <summary>E1 Pro</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2019/05/e1-pro-400.png" width="150">

[Product page](https://reolink.com/product/e1-pro/)

  ### IPC_513SD5
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2356_23062004](https://home-cdn.reolink.us/wp-content/uploads/2023/08/301124021693394642.2934.zip?download_name=513_SD5_2356_23062004.zip) | 2023‑06‑20 | <ol><li>Optimize the network feature</li><li>Update the web UI version</li><li>Optimize the PTZ function</li><li>Optimize the WiFi connection</li><li>Fix some known bugs</li></ol> | 
[v3.0.0.716_21112404](https://home-cdn.reolink.us/wp-content/uploads/2021/11/291041471638182507.8213.zip?download_name=E1_Pro_v30021112404_IPC_513SD5.zip) | 2021‑11‑24 | <ol><li>Modify the initialization process, prompting the scan to be modified from the sound effect to five languages.</li><li>Optimize the P2P connection and modify the P2P connection failure problem in some scenarios.</li><li>Modify the blueish problem of the image in some specific scenes.</li></ol> | This firmware is ONLY for E1 Pro(with hardware version IPC_513SD5).<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.660_21102001](https://drive.google.com/uc?id=1OxQCm36F1QbiDukz-NLZX8i6CloN8C7-&confirm=t) | 2021‑10‑20 | I-frame beta test. Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/qkdgyr/beta_firmware_test_for_iframe_iframe_for_nonai/)<br />[Source 2](https://drive.google.com/drive/folders/16IwkW1C_jHfOG34pe6RSn9kpNZ36lT_G)
[v3.0.0.597_21091001](https://drive.google.com/uc?id=1SzB1uQotnCk47q2iDTFJnV3-9faJ0xOC&confirm=t) | 2021‑09‑10 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/rdm8cl/where_is_the_firmware_for_e1_wifi_camera/hofyqqt/)<br />[Source 2](https://drive.google.com/drive/folders/1hqBOSZ_KK6UUR6km2smkAWADVogVTAyb)
[v3.0.0.183_21012804](https://home-cdn.reolink.us/wp-content/uploads/2021/02/010523421612157022.3287.zip)<br />[v3.0.0.183_21012804](https://reolink-storage.s3.amazonaws.com/website/firmware/20210128firmware/E1_Pro_183_21012804.zip) | 2021‑01‑28 | <ol><li>Fixed the problem that the email test fails when the email password is blank.</li><li>Optimized cloud transmission performance.</li><li>Optimized the network transmission protocol.</li><li>Solved the problem that you cannot use VLAN to access the camera after setting a static IP when the camera is connected by WiFi.</li><li>Fixed the bug that IPC failed to reconnect to the NVR after powering off when setting certain time zones.</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210801112229/https://support.reolink.com/hc/en-us/articles/900004231023-28-01-2021-Firmware-for-E1-Pro-513SD5-)
[v3.0.0.116_20110204](https://reolink-storage.s3.amazonaws.com/website/firmware/20201102firmware/E1-Pro_116_20110204..zip) | 2020‑11‑02 | <ol><li>Fixed the problem that the email test fails when the email password is blank.</li><li>Optimized cloud transmission performance.</li><li>Optimized the network transmission protocol.</li><li>Solved the problem that you cannot use VLAN to access the camera after setting a static IP when the camera is connected by WiFi.</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210121082446/https://support.reolink.com/hc/en-us/articles/900004231023-11-02-2020-Firmware-for-E1-Pro-513SD5-)
[v3.0.0.115_20102204](https://reolink-storage.s3.amazonaws.com/website/firmware/20201022firmware+/E1-Pro_115_20102204.zip) | 2020‑10‑22 | <ol><li>Fixed the problem that the email test fails when the email password is blank.</li><li>Optimized cloud transmission performance.</li><li>Optimized the network transmission protocol.</li><li>Fixed some known bugs.</li></ol> | [Archive](https://web.archive.org/web/20201101042158/https://support.reolink.com/hc/en-us/articles/900004231023-10-22-2020-Firmware-for-E1-Pro-513SD5-)
[v3.0.0.102_20091604](https://reolink-storage.s3.amazonaws.com/website/firmware/20200916firmware/E1-Pro_102_20091604.zip) | 2020‑09‑16 | <ol><li>Optimized the day and night mode switching function</li><li>Added the preset feature</li><li>Fixed the problem that the email-test failed with the empty email password</li><li>Optimize network delay when previewing the camera</li><li>Fixed some known bugs</li></ol> | [Archive](https://web.archive.org/web/20201023210911/https://support.reolink.com/hc/en-us/articles/900002595986-09-16-2020-Firmware-for-E1-Pro-513SD5-)
[v3.0.0.93_20090400](https://reolink-storage.s3.amazonaws.com/website/firmware/20200904firmware/E1_Pro_93_20090400.zip) | 2020‑09‑04 | <ol><li>Optimized the day and night mode switching function</li><li>Added the preset feature</li><li>Fixed the problem that the email-test failed with the empty email password</li><li>Optimize network delay when previewing the camera</li><li>Fixed the bug that FTP uploading may fail sometimes</li><li>Fixed some known bugs</li></ol> | [Archive](https://web.archive.org/web/20200919120514/https://support.reolink.com/hc/en-us/articles/900002595986-09-04-2020-Firmware-for-E1-Pro-513SD5-)
[v3.0.0.42_20062904](https://reolink-storage.s3.amazonaws.com/website/firmware/20200629firmware/E1_Pro_42_20062904.zip) | 2020‑06‑29 | <ol><li>Added multiple languages for the voice prompt when scanning the QR code to set up the camera.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed the bug when connecting the camera in different Vlan via Reolink app/client.</li></ol> | [Archive](https://web.archive.org/web/20200926093027/https://support.reolink.com/hc/en-us/articles/900001664643-06-29-2020-Firmware-for-E1-IPC-517SD5-and-E1-Pro-513SD5-)

  ### IPC_515SD5
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2356_23062013](https://home-cdn.reolink.us/wp-content/uploads/2023/10/071023341696674214.9101.zip?download_name=515_E1_Pro_v3002356_23062013.zip) | 2023‑06‑20 | <ol><li>Optimize the network feature</li><li>Update the web UI version</li><li>Optimize the PTZ function</li><li>Optimize the WiFi connection</li><li>Fix some known bugs</li></ol> | 
[v3.0.0.716_21112413](https://home-cdn.reolink.us/wp-content/uploads/2021/11/291057541638183474.2118.zip?download_name=E1_Pro_v30071621112413_IPC_515SD5.zip) | 2021‑11‑24 | <ol><li>Modify the initialization process, prompting the scan to be modified from the sound effect to five languages.</li><li>Optimize the P2P connection and modify the P2P connection failure problem in some scenarios.</li><li>Modify the blueish problem of the image in some specific scenes.</li></ol> | This firmware is ONLY for E1 Pro(with hardware version IPC_515SD5).<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.597_21091002](https://drive.google.com/uc?id=1UVDXKww4SU8MOvSZBP0uCL7o3dTgzZiH&confirm=t) | 2021‑09‑10 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/rdm8cl/where_is_the_firmware_for_e1_wifi_camera/hofyqqt/)<br />[Source 2](https://drive.google.com/drive/folders/1hqBOSZ_KK6UUR6km2smkAWADVogVTAyb)

  ### IPC_566SD54MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2647_23083100](https://home-cdn.reolink.us/wp-content/uploads/2023/10/090405421696824342.4095.zip?download_name=E1Pro_v3102647_23083100.zip) | 2023‑08‑31 | <ol><li>Optimize smart detection</li><li>Optimize auto-tracking</li><li>Optimize the network module</li><li>Optimize calibration</li><li>Optimize recording</li><li>Fix some known bugs</li></ol> | 

</details>

<details>
  <summary>E1 Zoom</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2019/10/e1-zoom-400.png" width="150">

[Product page](https://reolink.com/product/e1-zoom/)

  ### IPC_515BSD6
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2356_23062008](https://home-cdn.reolink.us/wp-content/uploads/2023/10/071029021696674542.422.zip?download_name=515B_E1_Zoom_v3002356_23062008.zip) | 2023‑06‑20 | <ol><li>Optimize the network feature</li><li>Update the web UI version</li><li>Optimize the PTZ function</li><li>Optimize the WiFi connection</li><li>Fix some known bugs</li></ol> | 
[v3.0.0.1107_22070508](https://home-cdn.reolink.us/wp-content/uploads/2022/07/080710341657264234.6572.zip?download_name=E1_ZOOM_22070508_IPC_515BSD6.zip) | 2022‑07‑05 | Optimized related network protocols and fixed some known bugs | This firmware is ONLY for E1 Zoom(with hardware version IPC_515BSD6)<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.716_21112408](https://home-cdn.reolink.us/wp-content/uploads/2021/11/291048341638182914.0673.zip) | 2021‑11‑24 |  | 
[v3.0.0.597_21091009](https://drive.google.com/uc?id=132BesT6cPA8Tgd-wqaTH6s-PpEuAqx-H&confirm=t) | 2021‑09‑10 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/rdm8cl/where_is_the_firmware_for_e1_wifi_camera/hofyqqt/)<br />[Source 2](https://drive.google.com/drive/folders/1hqBOSZ_KK6UUR6km2smkAWADVogVTAyb)
[v3.0.0.247_21040708](https://reolink-storage.s3.amazonaws.com/website/firmware/20210407firmware/E1+ZOOM-515BSD6.247_21040708..zip) | 2021‑04‑07 | <ol><li>Solved the problem that the camera switches back and forth between day and night mode in some specific scenarios.</li><li>Solved the problem that the camera cannot connect to WIFI with some specific channels.</li><li>Fixed other bugs.</li></ol> | [Archive](https://web.archive.org/web/20210728224903/https://support.reolink.com/hc/en-us/articles/900005622046-7th-April-2021-Firmware-for-E1-Zoom-IPC-515SD6-and-IPC-515BSD6-)
[v3.0.0.136_20121108](https://home-cdn.reolink.us/files/firmware/20201211firmware/E1+ZOOM_136_20121108.zip)<br />[v3.0.0.136_20121108](https://home-cdn.reolink.us/wp-content/uploads/2020/12/211158091608551889.5292.zip) | 2020‑12‑11 | <ol><li>Added the new web terminal that supports the HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added preset function.</li><li>Optimized network transmission protocol.</li><li>Optimized day and night switching effect.</li><li>Solved the problem that FTP recording doesn't have a pre-recorded function.</li><li>Solved the problem of an email test with an empty password.</li><li>Optimized Cloud Storage function.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as an email attachment.</li><li>Solved other known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210805181808/https://support.reolink.com/hc/en-us/articles/900003979146-12-11-2020-Firmware-for-E1-Zoom-IPC-515SD6-and-IPC-515BSD6-)

  ### IPC_515SD6
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2356_23062008](https://home-cdn.reolink.us/wp-content/uploads/2023/08/301127531693394873.8292.zip?download_name=515_SD6_2356_23062008.zip) | 2023‑06‑20 | <ol><li>Optimize the network feature</li><li>Update the web UI version</li><li>Optimize the PTZ function</li><li>Optimize the WiFi connection</li><li>Fix some known bugs</li></ol> | 
[v3.0.0.1107_22070508](https://home-cdn.reolink.us/wp-content/uploads/2022/07/080708321657264112.3591.zip?download_name=E1_ZOOM_22070508_IPC_515SD6.zip) | 2022‑07‑05 | Optimized related network protocols and fixed some known bugs | This firmware is ONLY for E1 Zoom(with hardware version IPC_515SD6)<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.716_21112408](https://drive.google.com/uc?id=16Q-iOSTpnkYaJoxzvFeY6YQbrOGbty12&confirm=t) | 2021‑11‑24 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/10)
[v3.0.0.597_21091001](https://drive.google.com/uc?id=1joiIhpBkjSymwCz_enqBNa_Ilt8Vg7uV&confirm=t) | 2021‑09‑10 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/rdm8cl/where_is_the_firmware_for_e1_wifi_camera/hofyqqt/)<br />[Source 2](https://drive.google.com/drive/folders/1hqBOSZ_KK6UUR6km2smkAWADVogVTAyb)
[v3.0.0.247_21040708](https://home-cdn.reolink.us/wp-content/uploads/2021/04/120703111618210991.6493.zip)<br />[v3.0.0.247_21040708](https://reolink-storage.s3.amazonaws.com/website/firmware/20210407firmware/E1+ZOOM.IPC_515SD6.247_21040708.zip) | 2021‑04‑07 | <ol><li>Solved the problem that the camera switches back and forth between day and night mode in some specific scenarios.</li><li>Solved the problem that the camera cannot connect to WIFI with some specific channels.</li><li>Fixed other bugs.</li></ol> | [Archive](https://web.archive.org/web/20210728224903/https://support.reolink.com/hc/en-us/articles/900005622046-7th-April-2021-Firmware-for-E1-Zoom-IPC-515SD6-and-IPC-515BSD6-)
[v3.0.0.136_20121108](https://home-cdn.reolink.us/files/firmware/20201211firmware/E1ZOOM_136_20121108.zip) | 2020‑12‑11 | <ol><li>Added the new web terminal that supports the HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added preset function.</li><li>Optimized network transmission protocol.</li><li>Optimized day and night switching effect.</li><li>Solved the problem that FTP recording doesn't have a pre-recorded function.</li><li>Solved the problem of an email test with an empty password.</li><li>Optimized Cloud Storage function.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as an email attachment.</li><li>Solved other known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210805181808/https://support.reolink.com/hc/en-us/articles/900003979146-12-11-2020-Firmware-for-E1-Zoom-IPC-515SD6-and-IPC-515BSD6-)
[v3.0.0.65_20071008](https://reolink-storage.s3.amazonaws.com/website/firmware/20200721firmware/E1-Zoom-5MP_65_20071008.zip) | 2020‑07‑10 | <ol><li>Added multiple languages for the voice prompt when scanning the QR code to set up the camera.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed the bug when connecting the camera in different Vlan via Reolink app/client.</li><li>Fixed the bug that FTP upload file failed.</li></ol> | [Archive](https://web.archive.org/web/20210805182235/https://support.reolink.com/hc/en-us/articles/900001850003-07-10-2020-Firmware-for-E1-Zoom-IPC-515SD6-)

  ### IPC_566SD65MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2649_23083102](https://home-cdn.reolink.us/wp-content/uploads/2023/10/090251351696819895.8968.zip?download_name=E1Zoom_v3102649_23083102.zip) | 2023‑08‑31 | <ol><li>Optimize smart detection</li><li>Optimize auto-tracking</li><li>Optimize the network module</li><li>Optimize calibration</li><li>Optimize recording</li><li>Fix some known bugs</li></ol> | 
[v3.1.0.1975_23042102](https://home-cdn.reolink.us/wp-content/uploads/2023/05/310820071685521207.4716.zip?download_name=E1_Zoom_v3101975_23042102_IPC_566SD65MP.zip) | 2023‑04‑21 | <ol><li>Optimize the focusing effect under night vision.</li><li>Solve other known bugs.</li></ol> | 

  ### IPC_566SD664M5MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2649_23083101](https://home-cdn.reolink.us/wp-content/uploads/2023/09/190238051695091085.1403.zip?download_name=E1Zoom_v3102649_23083101.zip) | 2023‑08‑31 | <ol><li>Optimize smart detection</li><li>Optimize auto-tracking</li><li>Optimize the network module</li><li>Optimize calibration</li><li>Optimize recording</li><li>Fix some known bugs</li></ol> | 
[v3.1.0.1975_23041200](https://home-cdn.reolink.us/wp-content/uploads/2023/04/150416541681532214.4008.zip?download_name=E1_Zoom_v3101975_23041200_IPC_566SD664M5MP.zip) | 2023‑04‑12 | <ol><li>Optimize the focusing effect under night vision.</li><li>Optimize some network functions.</li><li>Optimize the PTZ function.</li><li>Solve other known bugs.</li></ol> | 

</details>

<details>
  <summary>RLC-1210A *</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/07/050242471625452967.3365.png" width="150">

[Product page](https://reolink.com/product/rlc-1210a/)

  ### IPC_523128M12MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.861_22030104](https://home-cdn.reolink.us/wp-content/uploads/2022/03/041044531646390693.3551.zip?download_name=RLC_1210A_22030104.zip) | 2022‑03‑01 | <ol><li>Optimize the problem of screen flickering under high color temperature, such as under snow illumination</li><li>Optimize some other bugs</li></ol> | 1.Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading
[v3.0.0.250_21040804](https://home-cdn.reolink.us/wp-content/uploads/2021/06/170838571623919137.6027.zip) | 2021‑04‑08 |  | 
[v3.0.0.177_21012104](https://reolink-storage.s3.amazonaws.com/website/firmware/20210121firmware/RLC_1210A_177_21012104.zip) | 2021‑01‑21 | <ol><li>Corrected the text in the alert email.</li><li>Solved the problem that the MD status of API URL always displaying as triggered.</li><li>Solved the problem that failed to download videos via the Reolink client.</li><li>Solve the problem that online upgrading may fail sometimes.</li><li>Added a new web terminal that supports the HTML5 player.</li></ol> | [Archive](https://web.archive.org/web/20210805172232/https://support.reolink.com/hc/en-us/articles/900005240343-21st-Jan-2021-Firmware-for-RLC-1210A-and-RLC-1220A)
[v3.0.0.160_21011304](https://reolink-storage.s3.amazonaws.com/website/firmware/20210127firmware/RLC-1210A_160_21011304.zip) | 2021‑01‑13 | <ol><li>Corrected the text in the alert email.</li><li>Solved the problem that the MD status of API URL always displaying as triggered.</li><li>Solved the problem that failed to download videos via the Reolink client.</li><li>Solve the problem that online upgrading may fail sometimes.</li><li>Added a new web terminal that supports the HTML5 player.</li></ol> | [Archive](https://web.archive.org/web/20210204074215/https://support.reolink.com/hc/en-us/articles/900005240343-01-13-2021-Firmware-for-RLC-1210A-and-RLC-1220A)

</details>

<details>
  <summary>RLC-1212A</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2022/01/210404441642737884.1225.png" width="150">

[Product page](https://reolink.com/product/rlc-1212a/)

  ### IPC_523B18128M12MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2174_23050815](https://home-cdn.reolink.us/wp-content/uploads/2023/06/050705371685948737.5325.zip?download_name=RLC_1212A_23050815.zip) | 2023‑05‑08 | <ol><li>Add four-in-one (binning_mode) function, which provides image mode selection in night mode. This function can be found in the Advanced settings of the Display interface.</li><li>Update the web Client version.</li><li>Require new version of Reolink Client.Reolink Client(versions released before 20210805) connection is not supported.</li><li>Optimize RTSP, ONVIF connection performance.</li><li>Optimize the clarity of OSD strokes; solve the problem that the OSD display is not clear in some scenarios.</li><li>Optimize the day and night switching function.</li><li>Optimize video recording strategy.</li><li>Optimize email alarm accuracy.</li><li>Optimize the Smart detection function.<ol type="a"><li>Upgrade the smart model.</li><li>Improve the recognition accuracy of person, vehicle, and pets, and optimize the problem of static smart false positives.</li></ol></li><li>Solve the problem of probabilistic certificate import failure.</li><li>Solve the problem of deviation in adjusting the brightness of the screen.</li><li>Solve the problem that the detection area does not fit after the mirror image is flipped.</li><li>Optimize related network protocols and some known bugs.</li><li>Solve the probabilistic problem that the number of videos or pictures generated by time-lapse snapshots is inaccurate.</li><li>Fix the bug that the night vision frame rate is incorrect in some scenes.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.

  ### IPC_523B1812MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.1109_22070715](https://support.reolink.com/attachments/token/pdvEwEbxYvZIXPW0tJgROequl/?name=IPC_523B1812MP.1109_22070715.RLC-1212A.OS12D40.12MP.REOLINK.pak) | 2022‑07‑07 |  | :warning: This is a beta firmware
[v3.1.0.956_22041515](https://drive.google.com/uc?id=1KmIKncd3wkDI_D-uArWmnISt-Ff3Ba_R&confirm=t) | 2022‑04‑15 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)
[v3.1.0.861_22030365](https://drive.google.com/uc?id=1Kst8SYU3oWziuap3VJHJCeP_kqfP2iC0&confirm=t) | 2022‑03‑03 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)
[v3.1.0.819_22020915](https://drive.google.com/uc?id=1ZaUeysbu3c4LOs9EZNDgNZz8b3_asYdR&confirm=t) | 2022‑02‑09 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)

</details>

<details>
  <summary>RLC-1220A *</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/07/310158421627696722.9425.png" width="150">

[Product page](https://reolink.com/product/rlc-1220a/)

  ### IPC_523128M12MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.861_22030105](https://home-cdn.reolink.us/wp-content/uploads/2022/03/041047121646390832.6154.zip?download_name=RLC_1220A_22030105.zip) | 2022‑03‑01 | <ol><li>Optimize the problem of screen flickering under high color temperature, such as under snow illumination</li><li>Optimize some other bugs</li></ol> | 1.Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading
[v3.0.0.250_21040805](https://home-cdn.reolink.us/wp-content/uploads/2021/06/170837491623919069.6493.zip) | 2021‑04‑08 |  | 
[v3.0.0.177_21012105](https://reolink-storage.s3.amazonaws.com/website/firmware/20210121firmware/RLC-1220A.177_21012105..zip) | 2021‑01‑21 | <ol><li>Corrected the text in the alert email.</li><li>Solved the problem that the MD status of API URL always displaying as triggered.</li><li>Solved the problem that failed to download videos via the Reolink client.</li><li>Solve the problem that online upgrading may fail sometimes.</li><li>Added a new web terminal that supports the HTML5 player.</li></ol> | [Archive](https://web.archive.org/web/20210805172232/https://support.reolink.com/hc/en-us/articles/900005240343-21st-Jan-2021-Firmware-for-RLC-1210A-and-RLC-1220A)
[v3.0.0.160_21011305](https://reolink-storage.s3.amazonaws.com/website/firmware/20210127firmware/RLC-1220A_160_21011305.zip) | 2021‑01‑13 | <ol><li>Corrected the text in the alert email.</li><li>Solved the problem that the MD status of API URL always displaying as triggered.</li><li>Solved the problem that failed to download videos via the Reolink client.</li><li>Solve the problem that online upgrading may fail sometimes.</li><li>Added a new web terminal that supports the HTML5 player.</li></ol> | [Archive](https://web.archive.org/web/20210204074215/https://support.reolink.com/hc/en-us/articles/900005240343-01-13-2021-Firmware-for-RLC-1210A-and-RLC-1220A)

</details>

<details>
  <summary>RLC-1224A</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2022/01/210404571642737897.3887.png" width="150">

[Product page](https://reolink.com/product/rlc-1224a/)

  ### IPC_523D8128M12MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2174_23050816](https://home-cdn.reolink.us/wp-content/uploads/2023/06/050720121685949612.7354.zip?download_name=RLC_1224A_23050816.zip) | 2023‑05‑08 | <ol><li>Add four-in-one (binning_mode) function, which provides image mode selection in night mode. This function can be found in the Advanced settings of the Display interface.</li><li>Update the web Client version.</li><li>Require new version of Reolink Client.Reolink Client(versions released before 20210805) connection is not supported.</li><li>Optimize RTSP, ONVIF connection performance.</li><li>Optimize the clarity of OSD strokes; solve the problem that the OSD display is not clear in some scenarios.</li><li>Optimize the day and night switching function.</li><li>Optimize video recording strategy.</li><li>Optimize email alarm accuracy.</li><li>Optimize the Smart detection function.<ol type="a"><li>Upgrade the smart model.</li><li>Improve the recognition accuracy of person, vehicle, and pets, and optimize the problem of static smart false positives.</li></ol></li><li>Solve the problem of probabilistic certificate import failure.</li><li>Solve the problem of deviation in adjusting the brightness of the screen.</li><li>Solve the problem that the detection area does not fit after the mirror image is flipped.</li><li>Optimize related network protocols and some known bugs.</li><li>Solve the probabilistic problem that the number of videos or pictures generated by time-lapse snapshots is inaccurate.</li><li>Fix the bug that the night vision frame rate is incorrect in some scenes.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.

</details>

<details>
  <summary>RLC-210 *</summary>

  ### IPC_36S16M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1212_16091400](https://cdn.reolink.com/files/firmware/210/RLC-210_160914.zip)<br />[v2.0.0.1212_16091400](https://home-cdn.reolink.us/files/firmware/210/RLC-210_160914.zip)<br />[v2.0.0.1212_16091400](https://s3.amazonaws.com/reolink-storage/website/firmware/210/RLC-210_160914.zip) | 2016‑09‑14 |  | 

</details>

<details>
  <summary>RLC-210W *</summary>

  ### IPC_35S8M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1312_18032101](https://cdn.reolink.com/files/firmware/20180402firmware/RLC-210W_18032101.zip)<br />[v2.0.0.1312_18032101](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLC-210W_18032101.zip)<br />[v2.0.0.1312_18032101](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLC-210W_18032101.zip) | 2018‑03‑21 |  | 

  ### IPC_36S16M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1270_16102600](https://s3.amazonaws.com/reolink-storage/website/firmware/210w/RLC-210W_161026.zip) | 2016‑10‑26 |  | 

</details>

<details>
  <summary>RLC-410 *</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2018/08/store/rlc-410-5MP.png" width="150">

[Product page](https://reolink.com/product/rlc-410/)

  ### IPC_3816M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1441_19032101](https://s3.amazonaws.com/reolink-storage/website/firmware/20190321firmware/RLC-410_1441_19032101.zip)<br />[v2.0.0.1441_19032101](https://www.dropbox.com/s/0i00nzgce1y5shh/RLC-410_1441_19032101%20%281%29.zip?dl=1) | 2019‑03‑21 | Fixed security flaws. | [Archive](https://web.archive.org/web/20210805103139/https://support.reolink.com/hc/en-us/articles/360021715373-03-21-2019-Firmware-for-Reolink-IP-Cameras-IPC-3816M-)
[v2.0.0.1389_18081401](https://cdn.reolink.com/files/firmware/20180814firmware/RLC-410_1389_18081401.zip)<br />[v2.0.0.1389_18081401](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLC-410_1389_18081401.zip)<br />[v2.0.0.1389_18081401](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLC-410_1389_18081401.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020701](https://cdn.reolink.com/files/firmware/20180402firmware/RLC-410_1288_18020701.zip)<br />[v2.0.0.1288_18020701](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLC-410_1288_18020701.zip)<br />[v2.0.0.1288_18020701](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLC-410_1288_18020701.zip) | 2018‑02‑07 |  | 
[v2.0.0.889_17083001](https://s3.amazonaws.com/reolink-storage/website/firmware/889_1708/RLC-410_889_17083001.zip) | 2017‑08‑30 | <ol><li>Adds prompt to choose the suitable video stream type based on your network (except Reolink battery powered IP cameras).</li><li>The default stream types for 4MP and 2MP IP camera video preview are Balanced and Fluent respectively (except Reolink battery powered IP cameras).</li><li>Fixes some other bugs.</li></ol> | [Source 1](https://reolink.com/wp-content/uploads/2017/09/cant-upgrade-camera.docx)
[v2.0.0.842_17052401](https://s3.amazonaws.com/reolink-storage/website/firmware/842_170524/RLC-410_842_17052401.zip) | 2017‑05‑24 |  | 
[v2.0.0.675_17032701](https://s3.amazonaws.com/reolink-storage/website/firmware/675_170317/RLC-410_675_17032701.zip) | 2017‑03‑27 |  | 

  ### IPC_51316M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2356_23062000](https://home-cdn.reolink.us/wp-content/uploads/2023/10/071005051696673105.1104.zip?download_name=513_410_v3002356_23062000.zip) | 2023‑06‑20 | <ol><li>Optimize the network feature</li><li>Update the web UI version</li><li>Fix some known bugs</li></ol> | 
[v3.0.0.136_20121100](https://home-cdn.reolink.us/wp-content/uploads/2020/12/171217251608207445.3523.zip?download_name=firmware_RLC_410_v300136_20121100.zip)<br />[v3.0.0.136_20121100](https://reolink-storage.s3.amazonaws.com/website/firmware/20201211firmware/RLC-410_136_20121100.zip) | 2020‑12‑11 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function.</li><li>Optimized network transmission protocol to improve network security.</li><li>Optimized P2P connection.</li><li>Solved the problem that FTP recording doesn't have pre-recorded function.</li><li>Solved the problem of email test with an empty password and some mail sending bugs.</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system.</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Optimized day and night switching effect.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment.</li><li>Solved other known bugs</li></ol> | If your camera's hardware version does not begin with IPC_51316M, please wait for the new firmware release.<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.121_20111900](https://home-cdn.reolink.us/files/firmware/20201119firmware+/RLC-410_121_20111900.zip) | 2020‑11‑19 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function</li><li>Optimized network transmission protocol to improve network security</li><li>Optimized P2P connection</li><li>Solved the problem that FTP recording doesn't have pre-recorded function</li><li>Solved the problem of email test with an empty password and some mail sending bugs</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when the it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20201128103126/https://support.reolink.com/hc/en-us/articles/900004648143-11-19-2020-Firmware-for-Reolink-IP-Cameras-IPC-51316M-)
[v3.0.0.65_20071000](https://reolink-storage.s3.amazonaws.com/website/firmware/20200721firmware/RLC-410-4MP_65_20071000.zip) | 2020‑07‑10 | <ol><li>Fixed the bug that FTP upload file failed.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed other bugs.</li></ol> | [Archive](https://web.archive.org/web/20201128232515/https://support.reolink.com/hc/en-us/articles/900001840826-07-10-2020-Firmware-for-Reolink-IP-Cameras-IPC-51316M-)
[v2.0.0.448_19061402](https://reolink-storage.s3.amazonaws.com/website/firmware/20190614firmware/RLC-410_448_19061402(1).zip) | 2019‑06‑14 | <ol><li>Fixed the issue where the WiFi can't reconnect after rebooting.</li><li>Fixed the issue where the sound becomes smaller after frequently switching the audio.</li><li>Add the smart home feature (Google Home).</li><li>Optimize the breathing effect.</li><li>Fixed the drop issue where RTSP previewing.</li><li>Fixed the IR-cut switching failure problem on part of cameras.</li><li>Add power LED control function to C1 Pro.</li><li>Add manually trigger and automatic voice alarm function to C1 Pro.</li></ol> | [Archive](https://web.archive.org/web/20210805171119/https://support.reolink.com/hc/en-us/articles/360025688034-06-14-2019-Firmware-for-Reolink-IP-Cameras-IPC-51316M-)
[v2.0.0.354_19031110](https://s3.amazonaws.com/reolink-storage/website/firmware/20190311firmware/RLC-410_354_19031110.zip) | 2019‑03‑11 | <ol><li>Add the 30 FPS under the NTSC Standard.</li><li>Fix the bugs on the FTP for some servers.</li><li>Fix the bug on the WiFi connection.</li><li>Fix other bugs.</li></ol> | [Archive](https://web.archive.org/web/20190524055802/https://support.reolink.com/hc/en-us/articles/360008850853-03-11-2019-Firmware-for-Reolink-IP-Cameras-IPC-51316M-IPC-51516M-)

  ### IPC_51516M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2356_23062000](https://home-cdn.reolink.us/wp-content/uploads/2023/10/071013521696673632.8127.zip?download_name=515_410_5MP_v3002356_23062000.zip) | 2023‑06‑20 | <ol><li>Optimize the network feature</li><li>Update the web UI version</li><li>Optimize the WiFi connection</li><li>Fix some known bugs</li></ol> | 
[v3.0.0.660_21102203](https://drive.google.com/uc?id=19mWhnq5P506J2vzFSupzz74CEu_TwpdR&confirm=t) | 2021‑10‑22 | I-frame beta test. Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/qkdgyr/beta_firmware_test_for_iframe_iframe_for_nonai/)<br />[Source 2](https://drive.google.com/drive/folders/16IwkW1C_jHfOG34pe6RSn9kpNZ36lT_G)
[v3.0.0.136_20121100](https://home-cdn.reolink.us/files/firmware/20201211firmware/RLC-410-5MP_136_20121100.zip)<br />[v3.0.0.136_20121100](https://home-cdn.reolink.us/wp-content/uploads/2020/12/171226261608207986.0292.zip?download_name=firmware_RLC_410_5MP_v300136.zip) | 2020‑12‑11 | <ol><li>Optimized day and night switching effect.</li><li>Optimized network transmission protocol to improve network security.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment.</li><li>Solved other known bugs</li></ol> | If your camera's hardware version does not begin with IPC_51516M5M, please wait for the new firmware release.<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.116_20103100](https://home-cdn.reolink.us/files/firmware/20201031firmware/RLC-410-5MP_116_20103102.zip) | 2020‑10‑31 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function</li><li>Optimized network transmission protocol to improve network security</li><li>Optimized P2P connection</li><li>Solved the problem that FTP recording doesn't have pre-recorded function</li><li>Solved the problem of email test with an empty password and some mail sending bugs</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when the it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20210803040404/https://support.reolink.com/hc/en-us/articles/900004398063-10-31-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M5M-)
[v3.0.0.65_20071000](https://reolink-storage.s3.amazonaws.com/website/firmware/20200721firmware/RLC-410-5MP_65_20071000.zip) | 2020‑07‑10 | <ol><li>Fixed the bug that FTP upload file failed.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed other bugs.</li></ol> | [Archive](https://web.archive.org/web/20201128230059/https://support.reolink.com/hc/en-us/articles/900001840706-07-10-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v3.0.0.20_20052300](https://reolink-storage.s3.amazonaws.com/website/firmware/20200523firmware/RLC-410-5MP_20_20052300.zip) | 2020‑05‑23 |  | 
[v2.0.0.647_20031401](https://reolink-storage.s3.amazonaws.com/website/firmware/20200314firmware/RLC-410-5MP_647_20031401.zip) | 2020‑03‑14 |  | 
[v2.0.0.448_19061407](https://reolink-storage.s3.amazonaws.com/website/firmware/20190614firmware/RLC-410-5MP_448_19061407.zip) | 2019‑06‑14 | <ol><li>Add the smart home feature (Google Home).</li><li>Fixed AF learning table compatibility issues.</li><li>Improved P2P connectivity.</li><li>Fixed the IR-cut switching failure problem on part of cameras.</li><li>Modified the AF library and optimize the AF focus.</li><li>Optimize noise problems of PTZ audio.</li><li>Add power LED control function to C2 Pro.</li><li>Add manually trigger and automatic voice alarm function to C2 Pro.</li><li>Fixed the issue where the WiFi can't reconnect after rebooting.</li></ol> | [Archive](https://web.archive.org/web/20190905192627/https://support.reolink.com/hc/en-us/articles/360032028313-07-15-2019-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.354_19031100](https://s3.amazonaws.com/reolink-storage/website/firmware/20190311firmware/RLC-410-5MP_354_19031100.zip) | 2019‑03‑11 | <ol><li>Add the 30 FPS under the NTSC Standard.</li><li>Fix the bugs on the FTP for some servers.</li><li>Fix the bug on the WiFi connection.</li><li>Fix other bugs.</li></ol> | [Archive](https://web.archive.org/web/20190524055802/https://support.reolink.com/hc/en-us/articles/360008850853-03-11-2019-Firmware-for-Reolink-IP-Cameras-IPC-51316M-IPC-51516M-)

  ### IPC_515B16M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2356_23062000](https://home-cdn.reolink.us/wp-content/uploads/2023/10/080201431696730503.2979.zip?download_name=515B_410_5MP_v3002356_23062000.zip) | 2023‑06‑20 | <ol><li>Optimize the network feature</li><li>Update the web UI version</li><li>Fix some known bugs</li></ol> | 
[v3.0.0.625_21101106](https://drive.google.com/uc?id=1MGcRIKiOusHWERGxuZhL4G0H6GdSQUQe&confirm=t)<br />[v3.0.0.625_21101106](https://drive.google.com/uc?id=1QPhxZadDX_HN-qUAYXdnyMAdA5QJ_YAW&confirm=t) | 2021‑10‑11 | I-frame beta test. Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/qkdgyr/beta_firmware_test_for_iframe_iframe_for_nonai/)<br />[Source 2](https://drive.google.com/drive/folders/16IwkW1C_jHfOG34pe6RSn9kpNZ36lT_G)<br />[Source 3](https://www.reddit.com/r/reolinkcam/comments/p9wwx8/082321_new_firmware_update_for_all_ai_cameras/i4y5f12/)<br />[Source 4](https://www.reddit.com/r/reolinkcam/comments/u1ri3n/rlc811a_firmware_that_supports_iframe/)<br />[Source 5](https://drive.google.com/drive/folders/1geZXbRUuUHP2WIajjV3MygUmtQPR7Tq4)
[v3.0.0.136_20121100](https://home-cdn.reolink.us/wp-content/uploads/2020/12/290909151609232955.3772.zip?download_name=firmware_RLC_410_5MP_v300136.zip)<br />[v3.0.0.136_20121100](https://reolink-storage.s3.amazonaws.com/website/firmware/20210106+firmware/RLC-410-5MP_v300136_20121100.zip) | 2020‑12‑11 | <ol><li>Optimized day and night switching effect</li><li>Optimized network transmission.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solve the problem that there is no interval in the email settings on the web.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment.</li><li>Solved other known bugs</li></ol> | This firmware is ONLY for RLC-410-5MP(with hardware version IPC_515B16M5M)<br /> If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.

</details>

<details>
  <summary>RLC-410S *</summary>

[Product page](https://reolink.com/product/rlc-410s/)

  ### IPC_3816M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1441_19032102](https://s3.amazonaws.com/reolink-storage/website/firmware/20190321firmware/RLC-410S_1441_19032102.zip) | 2019‑03‑21 | Fixed security flaws. | [Archive](https://web.archive.org/web/20210805103139/https://support.reolink.com/hc/en-us/articles/360021715373-03-21-2019-Firmware-for-Reolink-IP-Cameras-IPC-3816M-)
[v2.0.0.1389_18081402](https://cdn.reolink.com/files/firmware/20180814firmware/RLC-410S_1389_18081402.zip)<br />[v2.0.0.1389_18081402](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLC-410S_1389_18081402.zip)<br />[v2.0.0.1389_18081402](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLC-410S_1389_18081402.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020702](https://cdn.reolink.com/files/firmware/20180402firmware/RLC-410S_1288_18020702.zip)<br />[v2.0.0.1288_18020702](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLC-410S_1288_18020702.zip)<br />[v2.0.0.1288_18020702](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLC-410S_1288_18020702.zip) | 2018‑02‑07 |  | 
[v2.0.0.889_17083002](https://s3.amazonaws.com/reolink-storage/website/firmware/889_1708/RLC-410S_889_17083002.zip) | 2017‑08‑30 |  | 
[v2.0.0.842_17052402](https://s3.amazonaws.com/reolink-storage/website/firmware/842_170524/RLC-410S_842_17052402.zip) | 2017‑05‑24 |  | 
[v2.0.0.675_17032702](https://s3.amazonaws.com/reolink-storage/website/firmware/675_170317/RLC-410S_675_17032702.zip) | 2017‑03‑27 |  | 

</details>

<details>
  <summary>RLC-410W</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2022/01/210755201642751720.2811.png" width="150">

[Product page](https://reolink.com/product/rlc-410w/)

  ### IPC_30K128M4MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.739_22042505](https://home-cdn.reolink.us/wp-content/uploads/2022/04/261218011650975481.5286.zip?download_name=RLC_410W_22042505.zip) | 2022‑04‑25 | <ol><li>Fixed a random configuration loss issue caused by restarts</li><li>Fixed some other bugs</li></ol> | This firmware is ONLY for RLC-410W(with hardware version IPC_30K128M4MP)<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.

  ### IPC_51316M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2356_23062002](https://home-cdn.reolink.us/wp-content/uploads/2023/08/301129191693394959.8303.zip?download_name=513_410W_2356_23062002.zip) | 2023‑06‑20 | <ol><li>Optimize the network feature</li><li>Update the web UI version</li><li>Optimize the WiFi connection</li><li>Fix some known bugs</li></ol> | 
[v3.0.0.757_21121503](https://github.com/AT0myks/reolink-fw-archive/files/11315740/IPC_51316M.757_21121503.RLC-410W.ov4689.4MP.WIFI1021.REOLINK.zip)<br />[v3.0.0.757_21121503](https://support-d.reolink.com/attachments/token/4SXDbC9daidjZw02rDj36QeLb/?name=IPC_51316M.757_21121503.RLC-410W.ov4689.4MP.WIFI1021.REOLINK.pak) | 2021‑12‑15 | Add the option to change the I-frame interval | :warning: This firmware might not work with some of the older units. Check source 1 for details.<br />[Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/12)
[v3.0.0.389_21062202](https://drive.google.com/uc?id=1Ed6EOOnWPG31IHnIB3xTvEEU6rtl9X1S&confirm=t)<br />[v3.0.0.389_21062202](https://drive.google.com/uc?id=1qCkdqhuGttK6mXdMUfQ1DTt9oHWNqBgc&confirm=t)<br />[v3.0.0.389_21062202](https://support.reolink.com/attachments/token/nc3CeREjMm2KJVOgvcqeICchw/?name=IPC_51316M.389_21062202.RLC-410W.ov4689.4MP.WIFI1021.REOLINK.pak) | 2021‑06‑22 |  | :warning: This firmware does not work with some of the older units. Check source 4 for details.<br />[Source 1](https://www.reddit.com/r/reolink/comments/sly78j/rlc410w_black_4mp_firmware_upgrade_issues/hw0wt1o/)<br />[Source 2](https://www.reddit.com/r/reolink/comments/wdo326/firmware_upgrade_for_rlc410w/iijdj0r/)<br />[Source 3](https://community.reolink.com/topic/2627/warning-of-firmware-upgrade-of-the-rlc410w/7)<br />[Source 4](https://github.com/AT0myks/reolink-fw-archive/discussions/12#discussioncomment-5721267)
[v3.0.0.136_20121102](https://home-cdn.reolink.us/wp-content/uploads/2020/12/171255541608209754.8148.zip)<br />[v3.0.0.136_20121102](https://reolink-storage.s3.amazonaws.com/website/firmware/20201211firmware/RLC-410W-20121102.zip) | 2020‑12‑11 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function</li><li>Optimized network transmission protocol to improve network security</li><li>Optimized P2P connection</li><li>Solved the problem that FTP recording doesn't have pre-recorded function</li><li>Solved the problem of email test with an empty password and some mail sending bugs</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Optimized day and night switching effect</li><li>Solved the problem that the DHCP hostname is eth0 on the router</li><li>Solved the problem that there is no email interval in the email setting on the web</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20210805103719/https://support.reolink.com/hc/en-us/articles/900004648143-12-11-2020-Firmware-for-Reolink-IP-Cameras-IPC-51316M-)
[v3.0.0.121_20111902](https://home-cdn.reolink.us/files/firmware/20201119firmware+/RLC-410W_121_20111902.zip) | 2020‑11‑19 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function</li><li>Optimized network transmission protocol to improve network security</li><li>Optimized P2P connection</li><li>Solved the problem that FTP recording doesn't have pre-recorded function</li><li>Solved the problem of email test with an empty password and some mail sending bugs</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when the it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20201128103126/https://support.reolink.com/hc/en-us/articles/900004648143-11-19-2020-Firmware-for-Reolink-IP-Cameras-IPC-51316M-)
[v3.0.0.65_20071002](https://reolink-storage.s3.amazonaws.com/website/firmware/20200721firmware/RLC-410W-4MP_65_20071002.zip) | 2020‑07‑10 | <ol><li>Fixed the bug that FTP upload file failed.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed other bugs.</li></ol> | [Archive](https://web.archive.org/web/20201128232515/https://support.reolink.com/hc/en-us/articles/900001840826-07-10-2020-Firmware-for-Reolink-IP-Cameras-IPC-51316M-)
[v2.0.0.648_20031403](https://support.reolink.com/attachments/token/qy0kAe4SiRauPY1rO8fDI9Uvc/?name=RLC-410W_648_20031403.zip) | 2020‑03‑14 |  | [Source 1](https://www.reddit.com/r/reolink/comments/wdo326/firmware_upgrade_for_rlc410w/)
[v2.0.0.448_19061404](https://reolink-storage.s3.amazonaws.com/website/firmware/20190614firmware/RLC-410W_448_19061404.zip) | 2019‑06‑14 | <ol><li>Fixed the issue where the WiFi can't reconnect after rebooting.</li><li>Fixed the issue where the sound becomes smaller after frequently switching the audio.</li><li>Add the smart home feature (Google Home).</li><li>Optimize the breathing effect.</li><li>Fixed the drop issue where RTSP previewing.</li><li>Fixed the IR-cut switching failure problem on part of cameras.</li><li>Add power LED control function to C1 Pro.</li><li>Add manually trigger and automatic voice alarm function to C1 Pro.</li></ol> | [Archive](https://web.archive.org/web/20210805171119/https://support.reolink.com/hc/en-us/articles/360025688034-06-14-2019-Firmware-for-Reolink-IP-Cameras-IPC-51316M-)
[v2.0.0.354_19031112](https://s3.amazonaws.com/reolink-storage/website/firmware/20190311firmware/RLC-410W_354_19031112.zip) | 2019‑03‑11 | <ol><li>Add the 30 FPS under the NTSC Standard.</li><li>Fix the bugs on the FTP for some servers.</li><li>Fix the bug on the WiFi connection.</li><li>Fix other bugs.</li></ol> | [Archive](https://web.archive.org/web/20190524055802/https://support.reolink.com/hc/en-us/articles/360008850853-03-11-2019-Firmware-for-Reolink-IP-Cameras-IPC-51316M-IPC-51516M-)

  ### IPC_51516M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2356_23062002](https://home-cdn.reolink.us/wp-content/uploads/2023/10/071015131696673713.4592.zip?download_name=515_410W_5MP_v3002356_23062002.zip) | 2023‑06‑20 | <ol><li>Optimize the network feature</li><li>Update the web UI version</li><li>Optimize the WiFi connection</li><li>Fix some known bugs</li></ol> | 
[v3.0.0.136_20121102](https://home-cdn.reolink.us/wp-content/uploads/2020/12/181032201608287540.9848.zip?download_name=firmware_RLC_410W_5MP_v300136.zip)<br />[v3.0.0.136_20121102](https://reolink-storage.s3.amazonaws.com/website/firmware/20201211firmware/RLC-410W-5MP_136_20121102.zip) | 2020‑12‑11 | <ol><li>Optimized day and night switching effect.</li><li>Optimized network transmission protocol to improve network security.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment</li><li>Solved other known bugs</li></ol> | If your camera's hardware version does not begin with IPC_51516M5M, please wait for the new firmware release.<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.116_20103102](https://home-cdn.reolink.us/files/firmware/20201031firmware/RLC-410W-5MP_116_20103102.zip) | 2020‑10‑31 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function</li><li>Optimized network transmission protocol to improve network security</li><li>Optimized P2P connection</li><li>Solved the problem that FTP recording doesn't have pre-recorded function</li><li>Solved the problem of email test with an empty password and some mail sending bugs</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when the it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20210803040404/https://support.reolink.com/hc/en-us/articles/900004398063-10-31-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M5M-)
[v3.0.0.65_20071002](https://reolink-storage.s3.amazonaws.com/website/firmware/20200721firmware/RLC-410W-5MP_65_20071002.zip) | 2020‑07‑10 | <ol><li>Fixed the bug that FTP upload file failed.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed other bugs.</li></ol> | [Archive](https://web.archive.org/web/20201128230059/https://support.reolink.com/hc/en-us/articles/900001840706-07-10-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.448_19061409](https://reolink-storage.s3.amazonaws.com/website/firmware/20190614firmware/RLC-410W-5MP_448_19061409.zip) | 2019‑06‑14 | <ol><li>Add the smart home feature (Google Home).</li><li>Fixed AF learning table compatibility issues.</li><li>Improved P2P connectivity.</li><li>Fixed the IR-cut switching failure problem on part of cameras.</li><li>Modified the AF library and optimize the AF focus.</li><li>Optimize noise problems of PTZ audio.</li><li>Add power LED control function to C2 Pro.</li><li>Add manually trigger and automatic voice alarm function to C2 Pro.</li><li>Fixed the issue where the WiFi can't reconnect after rebooting.</li></ol> | [Archive](https://web.archive.org/web/20190905192627/https://support.reolink.com/hc/en-us/articles/360032028313-07-15-2019-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.354_19031102](https://s3.amazonaws.com/reolink-storage/website/firmware/20190311firmware/RLC-410W-5MP_354_19031102.zip) | 2019‑03‑11 | <ol><li>Add the 30 FPS under the NTSC Standard.</li><li>Fix the bugs on the FTP for some servers.</li><li>Fix the bug on the WiFi connection.</li><li>Fix other bugs.</li></ol> | [Archive](https://web.archive.org/web/20190524055802/https://support.reolink.com/hc/en-us/articles/360008850853-03-11-2019-Firmware-for-Reolink-IP-Cameras-IPC-51316M-IPC-51516M-)

  ### IPC_515B16M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2356_23062002](https://home-cdn.reolink.us/wp-content/uploads/2023/10/071027451696674465.9311.zip?download_name=515B_410W_5MP_v3002356_23062002.zip) | 2023‑06‑20 | <ol><li>Optimize the network feature</li><li>Update the web UI version</li><li>Optimize the WiFi connection</li><li>Fix some known bugs</li></ol> | 
[v3.0.0.136_20121102](https://home-cdn.reolink.us/wp-content/uploads/2020/12/291114121609240452.8288.zip?download_name=firmware_RLC_410W_V300136.zip)<br />[v3.0.0.136_20121102](https://reolink-storage.s3.amazonaws.com/website/firmware/20210106+firmware/RLC-410W-5MP_V300136_20121102.zip) | 2020‑12‑11 | <ol><li>Optimized day and night switching effect</li><li>Optimized network transmission.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment.</li><li>Solved other known bugs</li></ol> | This firmware is ONLY for RLC-410W-5MP(with hardware version IPC_515B16M5M)<br /> If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.

</details>

<details>
  <summary>RLC-410WS *</summary>

[Product page](https://reolink.com/product/rlc-410ws/)

  ### IPC_3816M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1441_19032103](https://s3.amazonaws.com/reolink-storage/website/firmware/20190321firmware/RLC-410WS_1441_19032103.zip) | 2019‑03‑21 | Fixed security flaws. | [Archive](https://web.archive.org/web/20210805103139/https://support.reolink.com/hc/en-us/articles/360021715373-03-21-2019-Firmware-for-Reolink-IP-Cameras-IPC-3816M-)
[v2.0.0.1389_18081403](https://cdn.reolink.com/files/firmware/20180814firmware/RLC-410WS_1389_18081403.zip)<br />[v2.0.0.1389_18081403](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLC-410WS_1389_18081403.zip)<br />[v2.0.0.1389_18081403](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLC-410WS_1389_18081403.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020703](https://cdn.reolink.com/files/firmware/20180402firmware/RLC-410WS_1288_18020703.zip)<br />[v2.0.0.1288_18020703](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLC-410WS_1288_18020703.zip)<br />[v2.0.0.1288_18020703](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLC-410WS_1288_18020703.zip) | 2018‑02‑07 |  | 
[v2.0.0.889_17083003](https://s3.amazonaws.com/reolink-storage/website/firmware/889_1708/RLC-410WS_889_17083003.zip) | 2017‑08‑30 |  | 
[v2.0.0.842_17052403](https://s3.amazonaws.com/reolink-storage/website/firmware/842_170524/RLC-410WS_842_17052403.zip) | 2017‑05‑24 |  | 
[v2.0.0.675_17032703](https://s3.amazonaws.com/reolink-storage/website/firmware/675_170317/RLC-410WS_675_17032703.zip) | 2017‑03‑27 |  | 

</details>

<details>
  <summary>RLC-411 *</summary>

[Product page](https://reolink.com/product/rlc-411/)

  ### IPC_3816M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1441_19032106](https://s3.amazonaws.com/reolink-storage/website/firmware/20190321firmware/RLC-411_1441_19032106.zip) | 2019‑03‑21 | Fixed security flaws. | [Archive](https://web.archive.org/web/20210805103139/https://support.reolink.com/hc/en-us/articles/360021715373-03-21-2019-Firmware-for-Reolink-IP-Cameras-IPC-3816M-)
[v2.0.0.1389_18081406](https://cdn.reolink.com/files/firmware/20180814firmware/RLC-411_1389_18081406.zip)<br />[v2.0.0.1389_18081406](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLC-411_1389_18081406.zip)<br />[v2.0.0.1389_18081406](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLC-411_1389_18081406.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020706](https://cdn.reolink.com/files/firmware/20180402firmware/RLC-411_1288_18020706.zip)<br />[v2.0.0.1288_18020706](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLC-411_1288_18020706.zip)<br />[v2.0.0.1288_18020706](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLC-411_1288_18020706.zip) | 2018‑02‑07 |  | 
[v2.0.0.1055_17110900](https://s3.amazonaws.com/reolink-storage/website/firmware/1711firmware/IPC_3816M.1055_17110900.RLC-411.IMX326.5MP.AF.zip) | 2017‑11‑09 |  | 
[v2.0.0.842_17052404](https://s3.amazonaws.com/reolink-storage/website/firmware/842_170524/RLC-411_842_17052404.zip) | 2017‑05‑24 |  | 
[v2.0.0.675_17032704](https://s3.amazonaws.com/reolink-storage/website/firmware/675_170317/RLC-411_675_17032704.zip) | 2017‑03‑27 |  | 

</details>

<details>
  <summary>RLC-411S *</summary>

[Product page](https://reolink.com/product/rlc-411s/)

  ### IPC_3816M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1441_19032107](https://s3.amazonaws.com/reolink-storage/website/firmware/20190321firmware/RLC-411S_1441_19032107.zip) | 2019‑03‑21 | Fixed security flaws. | [Archive](https://web.archive.org/web/20210805103139/https://support.reolink.com/hc/en-us/articles/360021715373-03-21-2019-Firmware-for-Reolink-IP-Cameras-IPC-3816M-)
[v2.0.0.1389_18081407](https://cdn.reolink.com/files/firmware/20180814firmware/RLC-411S_1389_18081407.zip)<br />[v2.0.0.1389_18081407](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLC-411S_1389_18081407.zip)<br />[v2.0.0.1389_18081407](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLC-411S_1389_18081407.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020707](https://cdn.reolink.com/files/firmware/20180402firmware/RLC-411S_1288_18020707.zip)<br />[v2.0.0.1288_18020707](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLC-411S_1288_18020707.zip)<br />[v2.0.0.1288_18020707](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLC-411S_1288_18020707.zip) | 2018‑02‑07 |  | 
[v2.0.0.1055_17110901](https://s3.amazonaws.com/reolink-storage/website/firmware/1711firmware/IPC_3816M.1055_17110901.RLC-411S.IMX326.5MP.AF.zip) | 2017‑11‑09 |  | 
[v2.0.0.842_17052406](https://s3.amazonaws.com/reolink-storage/website/firmware/842_170524/RLC-411S_842_17052406.zip) | 2017‑05‑24 |  | 
[v2.0.0.675_17032706](https://s3.amazonaws.com/reolink-storage/website/firmware/675_170317/RLC-411S_675_17032706.zip) | 2017‑03‑27 |  | 

</details>

<details>
  <summary>RLC-411WS *</summary>

[Product page](https://reolink.com/product/rlc-411ws/)

  ### IPC_3816M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1441_19032108](https://s3.amazonaws.com/reolink-storage/website/firmware/20190321firmware/RLC-411WS_1441_19032108.zip) | 2019‑03‑21 | Fixed security flaws. | [Archive](https://web.archive.org/web/20210805103139/https://support.reolink.com/hc/en-us/articles/360021715373-03-21-2019-Firmware-for-Reolink-IP-Cameras-IPC-3816M-)
[v2.0.0.1389_18081408](https://cdn.reolink.com/files/firmware/20180814firmware/RLC-411WS_1389_18081408.zip)<br />[v2.0.0.1389_18081408](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLC-411WS_1389_18081408.zip)<br />[v2.0.0.1389_18081408](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLC-411WS_1389_18081408.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020708](https://cdn.reolink.com/files/firmware/20180402firmware/RLC-411WS_1288_18020708.zip)<br />[v2.0.0.1288_18020708](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLC-411WS_1288_18020708.zip)<br />[v2.0.0.1288_18020708](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLC-411WS_1288_18020708.zip) | 2018‑02‑07 |  | 
[v2.0.0.1055_17110902](https://s3.amazonaws.com/reolink-storage/website/firmware/1711firmware/IPC_3816M.1055_17110902.RLC-411WS.IMX326.5MP.WIFI.AF.REOLINK.zip) | 2017‑11‑09 |  | 
[v2.0.0.842_17052407](https://s3.amazonaws.com/reolink-storage/website/firmware/842_170524/RLC-411WS_842_17052407.zip) | 2017‑05‑24 |  | 
[v2.0.0.675_17032707](https://s3.amazonaws.com/reolink-storage/website/firmware/675_170317/RLC-411WS_675_17032707.zip) | 2017‑03‑27 |  | 

</details>

<details>
  <summary>RLC-420 *</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2018/08/store/rlc-420.png" width="150">

[Product page](https://reolink.com/product/rlc-420/)

  ### IPC_3816M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1441_19032100](https://s3.amazonaws.com/reolink-storage/website/firmware/20190321firmware/RLC-420_1441_19032100.zip) | 2019‑03‑21 | Fixed security flaws. | [Archive](https://web.archive.org/web/20210805103139/https://support.reolink.com/hc/en-us/articles/360021715373-03-21-2019-Firmware-for-Reolink-IP-Cameras-IPC-3816M-)
[v2.0.0.1389_18081400](https://cdn.reolink.com/files/firmware/20180814firmware/RLC-420_1389_18081400.zip)<br />[v2.0.0.1389_18081400](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLC-420_1389_18081400.zip)<br />[v2.0.0.1389_18081400](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLC-420_1389_18081400.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020700](https://cdn.reolink.com/files/firmware/20180402firmware/RLC-420_1288_18020700.zip)<br />[v2.0.0.1288_18020700](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLC-420_1288_18020700.zip)<br />[v2.0.0.1288_18020700](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLC-420_1288_18020700.zip) | 2018‑02‑07 |  | 
[v2.0.0.889_17083000](https://s3.amazonaws.com/reolink-storage/website/firmware/889_1708/RLC-420_889_17083000.zip) | 2017‑08‑30 |  | 
[v2.0.0.842_17052400](https://s3.amazonaws.com/reolink-storage/website/firmware/842_170524/RLC-420_842_17052400.zip) | 2017‑05‑24 |  | 
[v2.0.0.675_17032700](https://s3.amazonaws.com/reolink-storage/website/firmware/675_170317/RLC-420_675_170372700.zip) | 2017‑03‑27 |  | 

  ### IPC_51316M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.136_20121101](https://home-cdn.reolink.us/wp-content/uploads/2020/12/171231591608208319.6475.zip?download_name=firmware_RLC_42_v300136.zip)<br />[v3.0.0.136_20121101](https://reolink-storage.s3.amazonaws.com/website/firmware/20201211firmware/RLC-420_136_20121101.zip) | 2020‑12‑11 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function.</li><li>Optimized network transmission protocol to improve network security.</li><li>Optimized P2P connection.</li><li>Solved the problem that FTP recording doesn't have pre-recorded function.</li><li>Solved the problem of email test with an empty password and some mail sending bugs.</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system.</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Optimized day and night switching effect.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment.</li><li>Solved other known bugs</li></ol> | If your camera's hardware version does not begin with IPC_51316M, please wait for the new firmware release.<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.121_20111901](https://home-cdn.reolink.us/files/firmware/20201119firmware+/RLC-420_121_20111901.zip) | 2020‑11‑19 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function</li><li>Optimized network transmission protocol to improve network security</li><li>Optimized P2P connection</li><li>Solved the problem that FTP recording doesn't have pre-recorded function</li><li>Solved the problem of email test with an empty password and some mail sending bugs</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when the it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20201128103126/https://support.reolink.com/hc/en-us/articles/900004648143-11-19-2020-Firmware-for-Reolink-IP-Cameras-IPC-51316M-)
[v3.0.0.65_20071001](https://reolink-storage.s3.amazonaws.com/website/firmware/20200721firmware/RLC-420-4MP_65_20071001.zip) | 2020‑07‑10 | <ol><li>Fixed the bug that FTP upload file failed.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed other bugs.</li></ol> | [Archive](https://web.archive.org/web/20201128232515/https://support.reolink.com/hc/en-us/articles/900001840826-07-10-2020-Firmware-for-Reolink-IP-Cameras-IPC-51316M-)
[v2.0.0.448_19061403](https://reolink-storage.s3.amazonaws.com/website/firmware/20190614firmware/RLC-420_448_19061403(1).zip) | 2019‑06‑14 | <ol><li>Fixed the issue where the WiFi can't reconnect after rebooting.</li><li>Fixed the issue where the sound becomes smaller after frequently switching the audio.</li><li>Add the smart home feature (Google Home).</li><li>Optimize the breathing effect.</li><li>Fixed the drop issue where RTSP previewing.</li><li>Fixed the IR-cut switching failure problem on part of cameras.</li><li>Add power LED control function to C1 Pro.</li><li>Add manually trigger and automatic voice alarm function to C1 Pro.</li></ol> | [Archive](https://web.archive.org/web/20210805171119/https://support.reolink.com/hc/en-us/articles/360025688034-06-14-2019-Firmware-for-Reolink-IP-Cameras-IPC-51316M-)
[v2.0.0.354_19031111](https://s3.amazonaws.com/reolink-storage/website/firmware/20190311firmware/RLC-420_354_19031111.zip) | 2019‑03‑11 | <ol><li>Add the 30 FPS under the NTSC Standard.</li><li>Fix the bugs on the FTP for some servers.</li><li>Fix the bug on the WiFi connection.</li><li>Fix other bugs.</li></ol> | [Archive](https://web.archive.org/web/20190524055802/https://support.reolink.com/hc/en-us/articles/360008850853-03-11-2019-Firmware-for-Reolink-IP-Cameras-IPC-51316M-IPC-51516M-)

  ### IPC_51516M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.660_21110805](https://drive.google.com/uc?id=1jlweolf-P1nhFP11TZtDp29wWu2U60jW&confirm=t) | 2021‑11‑08 | I-frame beta test. Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/qkdgyr/beta_firmware_test_for_iframe_iframe_for_nonai/)<br />[Source 2](https://drive.google.com/drive/folders/16IwkW1C_jHfOG34pe6RSn9kpNZ36lT_G)
[v3.0.0.589_21091583](https://reolink.zendesk.com/attachments/token/HkpMqwJfjdnSOxAmn5pm6w9rZ/?name=IPC_51516M5M.589_21091583.RLC-420-5MP.SC5035.5MP.REOLINK.pak) | 2021‑09‑15 | Update LIVE555 to v2020.08.12 to fix the stale TCP session bug. | [Source 1](https://github.com/scottlamb/retina/issues/17#issuecomment-921178057)
[v3.0.0.136_20121101](https://home-cdn.reolink.us/wp-content/uploads/2020/12/171246331608209193.7489.zip?download_name=firmware_RLC_420_5MP_v300136.zip)<br />[v3.0.0.136_20121101](https://reolink-storage.s3.amazonaws.com/website/firmware/20201211firmware/RLC-420-5MP_136_20121101.zip) | 2020‑12‑11 | <ol><li>Optimized day and night switching effect.</li><li>Optimized network transmission protocol to improve network security.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment.</li><li>Solved other known bugs</li></ol> | If your camera's hardware version does not begin with IPC_51516M5M, please wait for the new firmware release.<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.116_20103101](https://home-cdn.reolink.us/files/firmware/20201031firmware/RLC-420-5MP_16_20103101.zip) | 2020‑10‑31 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function</li><li>Optimized network transmission protocol to improve network security</li><li>Optimized P2P connection</li><li>Solved the problem that FTP recording doesn't have pre-recorded function</li><li>Solved the problem of email test with an empty password and some mail sending bugs</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when the it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20210803040404/https://support.reolink.com/hc/en-us/articles/900004398063-10-31-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M5M-)
[v3.0.0.65_20071001](https://reolink-storage.s3.amazonaws.com/website/firmware/20200721firmware/RLC-420-5MP_65_20071001.zip) | 2020‑07‑10 | <ol><li>Fixed the bug that FTP upload file failed.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed other bugs.</li></ol> | [Archive](https://web.archive.org/web/20201128230059/https://support.reolink.com/hc/en-us/articles/900001840706-07-10-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.448_19061408](https://reolink-storage.s3.amazonaws.com/website/firmware/20190614firmware/RLC-420-5MP_448_19061408.zip) | 2019‑06‑14 | <ol><li>Add the smart home feature (Google Home).</li><li>Fixed AF learning table compatibility issues.</li><li>Improved P2P connectivity.</li><li>Fixed the IR-cut switching failure problem on part of cameras.</li><li>Modified the AF library and optimize the AF focus.</li><li>Optimize noise problems of PTZ audio.</li><li>Add power LED control function to C2 Pro.</li><li>Add manually trigger and automatic voice alarm function to C2 Pro.</li><li>Fixed the issue where the WiFi can't reconnect after rebooting.</li></ol> | [Archive](https://web.archive.org/web/20190905192627/https://support.reolink.com/hc/en-us/articles/360032028313-07-15-2019-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.354_19031101](https://s3.amazonaws.com/reolink-storage/website/firmware/20190311firmware/RLC-420-5MP_354_19031101.zip) | 2019‑03‑11 | <ol><li>Add the 30 FPS under the NTSC Standard.</li><li>Fix the bugs on the FTP for some servers.</li><li>Fix the bug on the WiFi connection.</li><li>Fix other bugs.</li></ol> | [Archive](https://web.archive.org/web/20190524055802/https://support.reolink.com/hc/en-us/articles/360008850853-03-11-2019-Firmware-for-Reolink-IP-Cameras-IPC-51316M-IPC-51516M-)

  ### IPC_515B16M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.625_21101107](https://drive.google.com/uc?id=1_6tuBVb9yMyKmBdbNvcdfi0jg6N2QXWc&confirm=t) | 2021‑10‑11 | I-frame beta test. Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/qkdgyr/beta_firmware_test_for_iframe_iframe_for_nonai/)<br />[Source 2](https://drive.google.com/drive/folders/16IwkW1C_jHfOG34pe6RSn9kpNZ36lT_G)
[v3.0.0.136_20121101](https://home-cdn.reolink.us/wp-content/uploads/2020/12/291354341609250074.6128.zip?download_name=firmware_RLC_420_5MP_v300136.zip)<br />[v3.0.0.136_20121101](https://reolink-storage.s3.amazonaws.com/website/firmware/20210106+firmware/RLC-420-5MP_v300136_20121101.zip) | 2020‑12‑11 | <ol><li>Optimized day and night switching effect</li><li>Optimized network transmission.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment.</li><li>Solved other known bugs</li></ol> | This firmware is ONLY for RLC-420-5MP(with hardware version IPC_515B16M5M)<br /> If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.

</details>

<details>
  <summary>RLC-422 *</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2018/08/store/rlc-422.png" width="150">

[Product page](https://reolink.com/product/rlc-422/)

  ### IPC_3816M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1441_19032109](https://s3.amazonaws.com/reolink-storage/website/firmware/20190321firmware/RLC-422_1441_19032109.zip) | 2019‑03‑21 | Fixed security flaws. | [Archive](https://web.archive.org/web/20210805103139/https://support.reolink.com/hc/en-us/articles/360021715373-03-21-2019-Firmware-for-Reolink-IP-Cameras-IPC-3816M-)
[v2.0.0.1389_18081409](https://cdn.reolink.com/files/firmware/20180814firmware/RLC-422_1389_18081409.zip)<br />[v2.0.0.1389_18081409](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLC-422_1389_18081409.zip)<br />[v2.0.0.1389_18081409](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLC-422_1389_18081409.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020709](https://cdn.reolink.com/files/firmware/20180402firmware/RLC-422_1288_18020709.zip)<br />[v2.0.0.1288_18020709](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLC-422_1288_18020709.zip)<br />[v2.0.0.1288_18020709](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLC-422_1288_18020709.zip) | 2018‑02‑07 |  | 
[v2.0.0.1055_17110903](https://s3.amazonaws.com/reolink-storage/website/firmware/1711firmware/IPC_3816M.1055_17110903.RLC-422.IMX326.5MP.AF.REOLINK.zip) | 2017‑11‑09 |  | 
[v2.0.0.842_17052405](https://s3.amazonaws.com/reolink-storage/website/firmware/842_170524/RLC-422_842_17052405.zip) | 2017‑05‑24 |  | 
[v2.0.0.675_17032705](https://s3.amazonaws.com/reolink-storage/website/firmware/675_170317/RLC-422_675_17032705.zip) | 2017‑03‑27 |  | 

  ### IPC_51516M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.136_20121105](https://home-cdn.reolink.us/wp-content/uploads/2020/12/171240351608208835.2679.zip?download_name=firmware_RLC_422_v300136.zip)<br />[v3.0.0.136_20121105](https://reolink-storage.s3.amazonaws.com/website/firmware/20201211firmware/RLC-422_136_20121105.zip) | 2020‑12‑11 | <ol><li>Optimized day and night switching effect.</li><li>Optimized network transmission protocol to improve network security.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment.</li><li>Solved other known bugs</li></ol> | If your camera's hardware version does not begin with IPC_51516M, please wait for the new firmware release.<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.116_20103105](https://home-cdn.reolink.us/files/firmware/20201031firmware/RLC-422_116_20103105.zip) | 2020‑10‑31 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function</li><li>Optimized network transmission protocol to improve network security</li><li>Optimized P2P connection</li><li>Solved the problem that FTP recording doesn't have pre-recorded function</li><li>Solved the problem of email test with an empty password and some mail sending bugs</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when the it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20210803040404/https://support.reolink.com/hc/en-us/articles/900004398063-10-31-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M5M-)
[v3.0.0.65_20071400](https://reolink-storage.s3.amazonaws.com/website/firmware/20200721firmware/RLC-422-5MP_65_20071400.zip) | 2020‑07‑14 | <ol><li>Fixed the bug that FTP upload file failed.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed other bugs.</li></ol> | [Archive](https://web.archive.org/web/20201128230059/https://support.reolink.com/hc/en-us/articles/900001840706-07-10-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.654_20040906](https://reolink-storage.s3.amazonaws.com/website/firmware/20200409firmware/RLC-422_654_20040906.zip) | 2020‑04‑09 | <ol><li>Extended the max password length of Email, FTP, and DDNS to 128 digits.</li><li>Updated the max cruise time to 300 seconds.</li></ol> | [Archive](https://web.archive.org/web/20210803033747/https://support.reolink.com/hc/en-us/articles/900000854106-04-09-2020-Firmware-for-Reolink-Auto-focus-IP-Cameras-IPC-51516M-)
[v2.0.0.477_19071502](https://reolink-storage.s3.amazonaws.com/website/firmware/20190715firmware/RLC-422_477_19071502.zip) | 2019‑07‑15 | <ol><li>Add the smart home feature (Google Home).</li><li>Fixed AF learning table compatibility issues.</li><li>Improved P2P connectivity.</li><li>Fixed the IR-cut switching failure problem on part of cameras.</li><li>Modified the AF library and optimize the AF focus.</li><li>Optimize noise problems of PTZ audio.</li><li>Add power LED control function to C2 Pro.</li><li>Add manually trigger and automatic voice alarm function to C2 Pro.</li><li>Fixed the issue where the WiFi can't reconnect after rebooting.</li></ol> | [Archive](https://web.archive.org/web/20190905192627/https://support.reolink.com/hc/en-us/articles/360032028313-07-15-2019-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.354_19031105](https://s3.amazonaws.com/reolink-storage/website/firmware/20190311firmware/RLC-422_354_19031105.zip) | 2019‑03‑11 | <ol><li>Add the 30 FPS under the NTSC Standard.</li><li>Fix the bugs on the FTP for some servers.</li><li>Fix the bug on the WiFi connection.</li><li>Fix other bugs.</li></ol> | [Archive](https://web.archive.org/web/20190524055802/https://support.reolink.com/hc/en-us/articles/360008850853-03-11-2019-Firmware-for-Reolink-IP-Cameras-IPC-51316M-IPC-51516M-)

</details>

<details>
  <summary>RLC-422W *</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2018/08/store/rlc-422w.png" width="150">

[Product page](https://reolink.com/product/rlc-422w/)

  ### IPC_3816M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1441_19032110](https://s3.amazonaws.com/reolink-storage/website/firmware/20190321firmware/RLC-422W_1441_19032110.zip) | 2019‑03‑21 | Fixed security flaws. | [Archive](https://web.archive.org/web/20210805103139/https://support.reolink.com/hc/en-us/articles/360021715373-03-21-2019-Firmware-for-Reolink-IP-Cameras-IPC-3816M-)
[v2.0.0.1389_18081410](https://cdn.reolink.com/files/firmware/20180814firmware/RLC-422W_1389_18081410.zip)<br />[v2.0.0.1389_18081410](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLC-422W_1389_18081410.zip)<br />[v2.0.0.1389_18081410](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLC-422W_1389_18081410.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020710](https://cdn.reolink.com/files/firmware/20180402firmware/RLC-422W_1288_18020710.zip)<br />[v2.0.0.1288_18020710](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLC-422W_1288_18020710.zip)<br />[v2.0.0.1288_18020710](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLC-422W_1288_18020710.zip) | 2018‑02‑07 |  | 
[v2.0.0.1055_17110904](https://s3.amazonaws.com/reolink-storage/website/firmware/1711firmware/IPC_3816M.1055_17110904.RLC-422W.IMX326.5MP.WIFI.AF.REOLINK.zip) | 2017‑11‑09 |  | 

  ### IPC_51516M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.136_20121106](https://home-cdn.reolink.us/wp-content/uploads/2020/12/181037371608287857.4113.zip?download_name=firmware_RLC_422W_v300136.zip)<br />[v3.0.0.136_20121106](https://reolink-storage.s3.amazonaws.com/website/firmware/20201211firmware/RLC-422W_136_20121106.zip) | 2020‑12‑11 | <ol><li>Optimized day and night switching effect.</li><li>Optimized network transmission protocol to improve network security.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment</li><li>Solved other known bugs</li></ol> | If your camera's hardware version does not begin with IPC_51516M5M, please wait for the new firmware release.<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.116_20103106](https://home-cdn.reolink.us/files/firmware/20201031firmware/RLC-422W_116_20103106.zip) | 2020‑10‑31 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function</li><li>Optimized network transmission protocol to improve network security</li><li>Optimized P2P connection</li><li>Solved the problem that FTP recording doesn't have pre-recorded function</li><li>Solved the problem of email test with an empty password and some mail sending bugs</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when the it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20210803040404/https://support.reolink.com/hc/en-us/articles/900004398063-10-31-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M5M-)
[v3.0.0.65_20071401](https://reolink-storage.s3.amazonaws.com/website/firmware/20200721firmware/RLC-422W-5MP_65_20071401.zip) | 2020‑07‑14 | <ol><li>Fixed the bug that FTP upload file failed.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed other bugs.</li></ol> | [Archive](https://web.archive.org/web/20201128230059/https://support.reolink.com/hc/en-us/articles/900001840706-07-10-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.654_20040907](https://reolink-storage.s3.amazonaws.com/website/firmware/20200409firmware/RLC-422W_654_20040907.zip) | 2020‑04‑09 | <ol><li>Extended the max password length of Email, FTP, and DDNS to 128 digits.</li><li>Updated the max cruise time to 300 seconds.</li></ol> | [Archive](https://web.archive.org/web/20210803033747/https://support.reolink.com/hc/en-us/articles/900000854106-04-09-2020-Firmware-for-Reolink-Auto-focus-IP-Cameras-IPC-51516M-)
[v2.0.0.477_19071503](https://reolink-storage.s3.amazonaws.com/website/firmware/20190715firmware/RLC-422W_477_19071503.zip) | 2019‑07‑15 | <ol><li>Add the smart home feature (Google Home).</li><li>Fixed AF learning table compatibility issues.</li><li>Improved P2P connectivity.</li><li>Fixed the IR-cut switching failure problem on part of cameras.</li><li>Modified the AF library and optimize the AF focus.</li><li>Optimize noise problems of PTZ audio.</li><li>Add power LED control function to C2 Pro.</li><li>Add manually trigger and automatic voice alarm function to C2 Pro.</li><li>Fixed the issue where the WiFi can't reconnect after rebooting.</li></ol> | [Archive](https://web.archive.org/web/20190905192627/https://support.reolink.com/hc/en-us/articles/360032028313-07-15-2019-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.354_19031106](https://s3.amazonaws.com/reolink-storage/website/firmware/20190311firmware/RLC-422W_354_19031106.zip) | 2019‑03‑11 | <ol><li>Add the 30 FPS under the NTSC Standard.</li><li>Fix the bugs on the FTP for some servers.</li><li>Fix the bug on the WiFi connection.</li><li>Fix other bugs.</li></ol> | [Archive](https://web.archive.org/web/20190524055802/https://support.reolink.com/hc/en-us/articles/360008850853-03-11-2019-Firmware-for-Reolink-IP-Cameras-IPC-51316M-IPC-51516M-)

</details>

<details>
  <summary>RLC-423 *</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2018/08/store/rlc-423.png" width="150">

[Product page](https://reolink.com/product/rlc-423/)

  ### IPC_3816M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1441_19032111](https://s3.amazonaws.com/reolink-storage/website/firmware/20190321firmware/RLC-423_1441_19032111.zip) | 2019‑03‑21 | Fixed security flaws. | [Archive](https://web.archive.org/web/20210805103139/https://support.reolink.com/hc/en-us/articles/360021715373-03-21-2019-Firmware-for-Reolink-IP-Cameras-IPC-3816M-)
[v2.0.0.1389_18081411](https://cdn.reolink.com/files/firmware/20180814firmware/RLC-423_1389_18081411.zip)<br />[v2.0.0.1389_18081411](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLC-423_1389_18081411.zip)<br />[v2.0.0.1389_18081411](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLC-423_1389_18081411.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020711](https://cdn.reolink.com/files/firmware/20180402firmware/RLC-423_1288_18020711.zip)<br />[v2.0.0.1288_18020711](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLC-423_1288_18020711.zip)<br />[v2.0.0.1288_18020711](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLC-423_1288_18020711.zip) | 2018‑02‑07 |  | 
[v2.0.0.1124_17120705](https://s3.amazonaws.com/reolink-storage/website/firmware/1711firmware/IPC_3816M.1124_17120705.RLC-423.IMX326.5MP.PTZ.REOLINK.zip) | 2017‑12‑07 |  | 
[v2.0.0.842_17052408](https://s3.amazonaws.com/reolink-storage/website/firmware/842_170524/RLC-423_842_17052408.zip) | 2017‑05‑24 |  | 
[v2.0.0.675_17032708](https://s3.amazonaws.com/reolink-storage/website/firmware/675_170317/RLC-423_675_17032708.zip) | 2017‑03‑27 |  | 

  ### IPC_51516M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.146_20122309](https://home-cdn.reolink.us/wp-content/uploads/2020/12/300432481609302768.493.zip?download_name=firmware_RLC_423_v300146_20122309.zip)<br />[v3.0.0.146_20122309](https://reolink-storage.s3.amazonaws.com/website/firmware/20201223firmware/RLC-423_146_20122309.zip) | 2020‑12‑23 | <ol><li>Added the new web terminal that supports the HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function.</li><li>Optimized network transmission.</li><li>Optimized P2P connection.</li><li>Solved the problem that FTP recording doesn't have pre-recorded function.</li><li>Solved the problem of email test with an empty password and some mail sending bugs.</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when the it's connected to WiFi.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as an email attachment.</li><li>Solved other known bugs.</li></ol> | This firmware is ONLY for RLC-423(with hardware version IPC_51516M5M)<br /> If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v2.0.0.489_19072600](https://reolink-storage.s3.amazonaws.com/website/firmware/20190715firmware/RLC-423_489_19072600.zip) | 2019‑07‑26 | <ol><li>Add the smart home feature (Google Home).</li><li>Fixed AF learning table compatibility issues.</li><li>Improved P2P connectivity.</li><li>Fixed the IR-cut switching failure problem on part of cameras.</li><li>Modified the AF library and optimize the AF focus.</li><li>Optimize noise problems of PTZ audio.</li><li>Add power LED control function to C2 Pro.</li><li>Add manually trigger and automatic voice alarm function to C2 Pro.</li><li>Fixed the issue where the WiFi can't reconnect after rebooting.</li></ol> | [Archive](https://web.archive.org/web/20190905192627/https://support.reolink.com/hc/en-us/articles/360032028313-07-15-2019-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)

</details>

<details>
  <summary>RLC-423S *</summary>

[Product page](https://reolink.com/product/rlc-423s/)

  ### IPC_3816M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1441_19032112](https://s3.amazonaws.com/reolink-storage/website/firmware/20190321firmware/RLC-423S_1441_19032112.zip) | 2019‑03‑21 | Fixed security flaws. | [Archive](https://web.archive.org/web/20210805103139/https://support.reolink.com/hc/en-us/articles/360021715373-03-21-2019-Firmware-for-Reolink-IP-Cameras-IPC-3816M-)
[v2.0.0.1389_18081412](https://cdn.reolink.com/files/firmware/20180814firmware/RLC-423S_1389_18081412.zip)<br />[v2.0.0.1389_18081412](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLC-423S_1389_18081412.zip)<br />[v2.0.0.1389_18081412](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLC-423S_1389_18081412.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020712](https://cdn.reolink.com/files/firmware/20180402firmware/RLC-423S_1288_18020712.zip)<br />[v2.0.0.1288_18020712](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLC-423S_1288_18020712.zip)<br />[v2.0.0.1288_18020712](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLC-423S_1288_18020712.zip) | 2018‑02‑07 |  | 
[v2.0.0.1055_17110905](https://s3.amazonaws.com/reolink-storage/website/firmware/1711firmware/IPC_3816M.1055_17110905.RLC-423S.IMX326.5MP.PTZ.REOLINK.zip) | 2017‑11‑09 |  | 

</details>

<details>
  <summary>RLC-423WS *</summary>

[Product page](https://reolink.com/product/rlc-423ws/)

  ### IPC_3816M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.1441_19032113](https://s3.amazonaws.com/reolink-storage/website/firmware/20190321firmware/RLC-423WS_1441_19032113.zip) | 2019‑03‑21 | Fixed security flaws. | [Archive](https://web.archive.org/web/20210805103139/https://support.reolink.com/hc/en-us/articles/360021715373-03-21-2019-Firmware-for-Reolink-IP-Cameras-IPC-3816M-)
[v2.0.0.1389_18081413](https://cdn.reolink.com/files/firmware/20180814firmware/RLC-423WS_1389_18081413.zip)<br />[v2.0.0.1389_18081413](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLC-423WS_1389_18081413.zip)<br />[v2.0.0.1389_18081413](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLC-423WS_1389_18081413.zip) | 2018‑08‑14 |  | 
[v2.0.0.1288_18020713](https://cdn.reolink.com/files/firmware/20180402firmware/RLC-423WS_1288_18020713.zip)<br />[v2.0.0.1288_18020713](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLC-423WS_1288_18020713.zip)<br />[v2.0.0.1288_18020713](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLC-423WS_1288_18020713.zip) | 2018‑02‑07 |  | 
[v2.0.0.1055_17110906](https://s3.amazonaws.com/reolink-storage/website/firmware/1711firmware/IPC_3816M.1055_17110906.RLC-423WS.IMX326.5MP.WIFI.PTZ.REOLINK.zip) | 2017‑11‑09 |  | 

</details>

<details>
  <summary>RLC-510A</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2020/07/rlc-510a-340.png" width="150">

[Product page](https://reolink.com/product/rlc-510a/)

  ### IPC_523128M5MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.951_22041567](https://home-cdn.reolink.us/wp-content/uploads/2022/04/151157321650023852.8099.zip?download_name=RLC_510A_22041567.zip) | 2022‑04‑15 | <ol><li>Upgraded ONVIF protocol to version 21.06</li><li>Solved the issue of no audio output on some platforms using ONVIF</li><li>Added the fixed FPS setting: The FPS won't be reduced automatically at night</li><li>Added multiple selection for the iFrame setting</li><li>Solved the problem that FTP parameters do not take effect under WEB access</li><li>Upgraded AI model to reduce false negatives and false positives</li><li>Added the function of synchronously prohibiting Push after disabling the UID</li><li>Added the security policy of login lockout</li><li>Solved some bugs of FTP</li><li>Solved some bugs of Email alert</li><li>Solved the problem of failing to adjust the threshold setting</li><li>Modified the display script of anti-flicker</li></ol> | 1.Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading
[v3.1.0.598_21091302](https://drive.google.com/uc?id=1V2djJmvlPl_U-YZLOAQaMytn74EE7Ad_&confirm=t) | 2021‑09‑13 | Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/ptupxs/tester_wanted_for_the_beta_test_for_new_ai/)<br />[Source 2](https://drive.google.com/drive/folders/1S1KCRPH7u0BQ02D2drxLTmnsb7tyD17v)
[v3.0.0.494_21073002](https://drive.google.com/uc?id=1DzqvLN7SEhHzGJjrcOaUgEur__o0IJWT&confirm=t) | 2021‑07‑30 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)
[v3.0.0.177_21012102](https://home-cdn.reolink.us/wp-content/uploads/2021/01/290802021611907322.7966.zip) | 2021‑01‑21 |  | 
[v3.0.0.160_21010802](https://reolink-storage.s3.amazonaws.com/website/firmware/20210112firmware/RLC-510A_160_21010802.zip) | 2021‑01‑08 | <ol><li>Corrected the text in the alert email.</li><li>Solved the problem that the MD status of API URL always displaying as triggered.</li><li>Solved the problem that failed to download videos via the Reolink client.</li><li>Solved other known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210801104604/https://support.reolink.com/hc/en-us/articles/900004125186-01-12-2021-Firmware-for-RLC-520A-RLC-510A-RLC-820A-RLC-810A)
[v3.0.0.124_20112602](https://home-cdn.reolink.us/files/firmware/20201126Firmware/RLC-510A_124_20112602.zip)<br />[v3.0.0.124_20112602](https://home-cdn.reolink.us/wp-content/uploads/2020/12/070722251607325745.3307.zip) | 2020‑11‑26 | <ol><li>Solved the problem that common users cannot turn on push notifications.</li><li>Frame rate adjustment: For 8MP cameras, the highest frame rate of any resolution is 25 frames.</li><li>Supporting Clear H265 stream in ONVIF, RTSP preview for 8MP cameras.</li><li>Solved H265 freezing issue on Blue Iris.</li><li>MD filters Human/Vehicle detection false alerts and MD area is synchronized by the Human/Vehicle detection.</li><li>Enhanced SD card driver to solve the problem that some SD cards cannot be recognized.</li><li>Solved the flickering problem when set to the lowest exposure value (50Hz).</li></ol> | [Archive](https://web.archive.org/web/20210725182423/https://support.reolink.com/hc/en-us/articles/900003792966-11-26-2020-Firmware-for-RLC-510A-RLC-520A-RLC-810A-RLC-820A-IPC-523128M-)

  ### IPC_523128M5MP_V2
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2109_23051501](https://support-d.reolink.com/attachments/token/axfGH42kwt74trKrKFysXe2Mg/?name=IPC_523128M5MP_V2.2109_23051501.RLC-510A.OV05A10.5MP.REOLINK.pak) | 2023‑05‑15 | Fix live video delay in Synology Surveillance Station | [Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/18)
[v3.1.0.1228_22082200](https://support.reolink.com/attachments/token/UmdVaKU7erG8omgOIiciOZWcr/?name=IPC_523128M5MP_V2.1228_22082200.RLC-510A.OV05A10.5MP.REOLINK.pak) | 2022‑08‑22 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/y5awnz/firmware_for_rlc510a_v2/)<br />[Source 2](https://community.reolink.com/topic/3501/no-firmware-for-my-new-rlc-510a-cameras/4)

</details>

<details>
  <summary>RLC-510WA</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/rlc-510wa-400.png?v=1614674123709" width="150">

[Product page](https://reolink.com/product/rlc-510wa/)

  ### IPC_523128M5MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.1387_22100633](https://support.reolink.com/attachments/token/1ISbkfiJ3uJ2rganejlK6JUvG/?name=IPC_523128M5MP.1387_22100633.RLC-510WA.OV05A10.5MP.WIFI1021.REOLINK.pak) | 2022‑10‑06 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/10iv3di/comment/j5osusf)
[v3.1.0.956_22041512](https://drive.google.com/uc?id=1ENIQ_7cGWGygM1wSZjiIHuRPD_IrIuCz&confirm=t)<br />[v3.1.0.956_22041512](https://drive.google.com/uc?id=1Ja75a3z85qZpcpoTwcDVzPGUtTGtTEj6&confirm=t) | 2022‑04‑15 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />If you get an error when updating, see [here](https://github.com/AT0myks/reolink-fw-archive/issues/2#issuecomment-1416773844).<br />[Source 1](https://github.com/AT0myks/reolink-fw-archive/issues/2)
[v3.1.0.764_21121712](https://home-cdn.reolink.us/wp-content/uploads/2022/01/191101291642590089.08.zip?download_name=RLC_510WA_21121712.zip) | 2021‑12‑17 | <ol><li>Optimized AI detection function<ol type="a"><li>Upgraded the AI model to improve the recognition accuracy of people, cars, and pets (the  new features of 8MP models), and optimized static AI false alarm issue</li><li>Increased the AI delay alarm function, which can reduce dynamic misjudgments caused by flying insects, rain, etc. by adjusting the delay gear</li><li>Optimized the alarm area settings to reduce false alarms in the shielded area</li><li>Optimized the AI sensitivity setting: It will not send AI alarm when the AI detection sensitivity is 0</li><li>Optimized the false alarms caused by day and night switching and lighting changes, and solved the problem that the spotlight will repeatedly turn on and off in some scenes</li><li>Optimized the automatic tracking function to solve the chaotic tracking problem of the camera in some scenarios</li><li>Added the vertical tracking function for RLC- 523WA, RLC-823A</li></ol></li><li>Added AI smart detection type option for spotlight, so you can choose AI type for the smart spotlight</li><li>Optimized FTP function<ol type="a"><li>Supported FTPS encryption to improve the security of FTP transfer files</li><li>Optimized the FTP transfer file type:You can choose to transfer only video, only pictures, and transfer both videos and pictures to the FTP server</li><li>Increased Overwrite function for picture only and video only function</li><li>Added 2s/5s/10s interval options for FTP capture picture</li><li>Optimized the upload file directory function: You can choose to folder by day/month, or save all files in the same folder</li></ol></li><li>Optimized the push function and increased the push interval setting function</li><li>Increased the Test error code function for the Email, FTP, push settings, which could help find the cause of the error</li><li>Added switch for RTSP, ONVIF, HTTP, HTTPS service. Users can turn on and off the corresponding network services as needed</li><li>Increased the function of locking the device: The device will be locked for 2 seconds after logging in with an incorrect password to improve login security and prevent malicious attacks</li><li>Added web certificate import function</li><li>Updated RTSP version</li><li>Optimized the AF algorithm to solve the problem of unclear focus in some scenes</li><li>Optimized pre-record time of videos and solved the problem of too long pre-record time in some scenes</li><li>Added day and night switching threshold adjustment function</li></ol> | 1. Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading
[v3.1.0.598_21091312](https://drive.google.com/uc?id=1YIf7hTGX1rHQPYLr1Ct-fALh_0SKNYbw&confirm=t) | 2021‑09‑13 | Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/ptupxs/tester_wanted_for_the_beta_test_for_new_ai/)<br />[Source 2](https://drive.google.com/drive/folders/1S1KCRPH7u0BQ02D2drxLTmnsb7tyD17v)

</details>

<details>
  <summary>RLC-511 *</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2018/08/store/rlc-511.png" width="150">

[Product page](https://reolink.com/product/rlc-511/)

  ### IPC_51516M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2356_23062003](https://home-cdn.reolink.us/wp-content/uploads/2023/10/071016061696673766.8846.zip?download_name=515_511_v3002356_23062003.zip) | 2023‑06‑20 | <ol><li>Optimize the network feature</li><li>Update the web UI version</li><li>Fix some known bugs</li></ol> | 
[v3.0.0.757_21121504](https://support.reolink.com/attachments/token/EsHhHRib4QhMDTE4SI1kINMw3/?name=IPC_51516M5M.757_21121504.RLC-511.OV05A10.5MP.AF.REOLINK.pak) | 2021‑12‑15 | Fixed I-frame switch button | [Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/13)
[v3.0.0.142_20121803](https://home-cdn.reolink.us/wp-content/uploads/2020/12/241015551608804955.4244.zip?download_name=firmware_RLC_511_v300142_20121803.zip)<br />[v3.0.0.142_20121803](https://reolink-storage.s3.amazonaws.com/website/firmware/20201218firmware/RLC-511_142_20121803.zip) | 2020‑12‑18 | <ol><li>Optimized day and night switching effect.</li><li>Optimized network transmission protocol to improve network security.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment</li><li>Solved other known bugs</li></ol> | If your camera's hardware version does not begin with IPC_51516M5M, please wait for the new firmware release.<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.136_20121103](https://reolink-storage.s3.amazonaws.com/website/firmware/20201211firmware/RLC-511_136_20121103.zip) | 2020‑12‑11 | <ol><li>Optimized day and night switching effect</li><li>Optimized network transmission protocol to improve network security</li><li>Solved the problem that the DHCP hostname is eth0 on the router</li><li>Solved the problem that there is no email interval in the email setting on the web</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20201218101824/https://support.reolink.com/hc/en-us/articles/900004823943-12-11-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v3.0.0.116_20103103](https://home-cdn.reolink.us/files/firmware/20201031firmware/RLC-511_116_20103103.zip) | 2020‑10‑31 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function</li><li>Optimized network transmission protocol to improve network security</li><li>Optimized P2P connection</li><li>Solved the problem that FTP recording doesn't have pre-recorded function</li><li>Solved the problem of email test with an empty password and some mail sending bugs</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when the it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20210803040404/https://support.reolink.com/hc/en-us/articles/900004398063-10-31-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M5M-)
[v3.0.0.65_20071003](https://reolink-storage.s3.amazonaws.com/website/firmware/20200721firmware/RLC-511-5MP_65_20071003.zip) | 2020‑07‑10 | <ol><li>Fixed the bug that FTP upload file failed.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed other bugs.</li></ol> | [Archive](https://web.archive.org/web/20201128230059/https://support.reolink.com/hc/en-us/articles/900001840706-07-10-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.654_20040904](https://reolink-storage.s3.amazonaws.com/website/firmware/20200409firmware/RLC-511_654_20040904.zip) | 2020‑04‑09 | <ol><li>Extended the max password length of Email, FTP, and DDNS to 128 digits.</li><li>Updated the max cruise time to 300 seconds.</li></ol> | [Archive](https://web.archive.org/web/20210803033747/https://support.reolink.com/hc/en-us/articles/900000854106-04-09-2020-Firmware-for-Reolink-Auto-focus-IP-Cameras-IPC-51516M-)
[v2.0.0.477_19071500](https://reolink-storage.s3.amazonaws.com/website/firmware/20190715firmware/RLC-511_477_19071500.zip) | 2019‑07‑15 | <ol><li>Add the smart home feature (Google Home).</li><li>Fixed AF learning table compatibility issues.</li><li>Improved P2P connectivity.</li><li>Fixed the IR-cut switching failure problem on part of cameras.</li><li>Modified the AF library and optimize the AF focus.</li><li>Optimize noise problems of PTZ audio.</li><li>Add power LED control function to C2 Pro.</li><li>Add manually trigger and automatic voice alarm function to C2 Pro.</li><li>Fixed the issue where the WiFi can't reconnect after rebooting.</li></ol> | [Archive](https://web.archive.org/web/20190905192627/https://support.reolink.com/hc/en-us/articles/360032028313-07-15-2019-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.354_19031103](https://s3.amazonaws.com/reolink-storage/website/firmware/20190311firmware/RLC-511_354_19031103.zip) | 2019‑03‑11 | <ol><li>Add the 30 FPS under the NTSC Standard.</li><li>Fix the bugs on the FTP for some servers.</li><li>Fix the bug on the WiFi connection.</li><li>Fix other bugs.</li></ol> | [Archive](https://web.archive.org/web/20190524055802/https://support.reolink.com/hc/en-us/articles/360008850853-03-11-2019-Firmware-for-Reolink-IP-Cameras-IPC-51316M-IPC-51516M-)

</details>

<details>
  <summary>RLC-511W *</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2018/08/store/rlc-511w.png" width="150">

[Product page](https://reolink.com/product/rlc-511w/)

  ### IPC_51516M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2356_23062004](https://home-cdn.reolink.us/wp-content/uploads/2023/10/071022541696674174.2287.zip?download_name=515_511W_v3002356_23062004.zip) | 2023‑06‑20 | <ol><li>Optimize the network feature</li><li>Update the web UI version</li><li>Optimize the WiFi connection</li><li>Fix some known bugs</li></ol> | 
[v3.0.0.142_20121804](https://home-cdn.reolink.us/wp-content/uploads/2020/12/241017111608805031.3025.zip?download_name=firmwareRLC_511W_v300142_20121804.zip)<br />[v3.0.0.142_20121804](https://reolink-storage.s3.amazonaws.com/website/firmware/20201218firmware/RLC-511W_142_20121804.zip) | 2020‑12‑18 | <ol><li>Optimized day and night switching effect.</li><li>Optimized network transmission protocol to improve network security.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment</li><li>Solved other known bugs</li></ol> | If your camera's hardware version does not begin with IPC_51516M5M, please wait for the new firmware release.<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.136_20121104](https://reolink-storage.s3.amazonaws.com/website/firmware/20201211firmware/RLC-511W_136_2012104.zip) | 2020‑12‑11 | <ol><li>Optimized day and night switching effect</li><li>Optimized network transmission protocol to improve network security</li><li>Solved the problem that the DHCP hostname is eth0 on the router</li><li>Solved the problem that there is no email interval in the email setting on the web</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20201218101824/https://support.reolink.com/hc/en-us/articles/900004823943-12-11-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v3.0.0.116_20103104](https://home-cdn.reolink.us/files/firmware/20201031firmware/RLC-511W_116_20103104.zip) | 2020‑10‑31 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function</li><li>Optimized network transmission protocol to improve network security</li><li>Optimized P2P connection</li><li>Solved the problem that FTP recording doesn't have pre-recorded function</li><li>Solved the problem of email test with an empty password and some mail sending bugs</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when the it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20210803040404/https://support.reolink.com/hc/en-us/articles/900004398063-10-31-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M5M-)
[v3.0.0.65_20071004](https://reolink-storage.s3.amazonaws.com/website/firmware/20200721firmware/RLC-511W-5MP_65_20071004.zip) | 2020‑07‑10 | <ol><li>Fixed the bug that FTP upload file failed.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed other bugs.</li></ol> | [Archive](https://web.archive.org/web/20201128230059/https://support.reolink.com/hc/en-us/articles/900001840706-07-10-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.654_20040905](https://reolink-storage.s3.amazonaws.com/website/firmware/20200409firmware/RLC-511W_654_20040905.zip) | 2020‑04‑09 | <ol><li>Extended the max password length of Email, FTP, and DDNS to 128 digits.</li><li>Updated the max cruise time to 300 seconds.</li></ol> | [Archive](https://web.archive.org/web/20210803033747/https://support.reolink.com/hc/en-us/articles/900000854106-04-09-2020-Firmware-for-Reolink-Auto-focus-IP-Cameras-IPC-51516M-)
[v2.0.0.477_19071501](https://reolink-storage.s3.amazonaws.com/website/firmware/20190715firmware/RLC-511W_477_19071501.zip) | 2019‑07‑15 | <ol><li>Add the smart home feature (Google Home).</li><li>Fixed AF learning table compatibility issues.</li><li>Improved P2P connectivity.</li><li>Fixed the IR-cut switching failure problem on part of cameras.</li><li>Modified the AF library and optimize the AF focus.</li><li>Optimize noise problems of PTZ audio.</li><li>Add power LED control function to C2 Pro.</li><li>Add manually trigger and automatic voice alarm function to C2 Pro.</li><li>Fixed the issue where the WiFi can't reconnect after rebooting.</li></ol> | [Archive](https://web.archive.org/web/20190905192627/https://support.reolink.com/hc/en-us/articles/360032028313-07-15-2019-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.354_19031104](https://s3.amazonaws.com/reolink-storage/website/firmware/20190311firmware/RLC-511W_354_19031104.zip) | 2019‑03‑11 | <ol><li>Add the 30 FPS under the NTSC Standard.</li><li>Fix the bugs on the FTP for some servers.</li><li>Fix the bug on the WiFi connection.</li><li>Fix other bugs.</li></ol> | [Archive](https://web.archive.org/web/20190524055802/https://support.reolink.com/hc/en-us/articles/360008850853-03-11-2019-Firmware-for-Reolink-IP-Cameras-IPC-51316M-IPC-51516M-)

</details>

<details>
  <summary>RLC-511WA</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/03/050711201614928280.545.png" width="150">

[Product page](https://reolink.com/product/rlc-511wa/)

  ### IPC_523128M5MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.956_22041509](https://home-cdn.reolink.us/wp-content/uploads/2022/04/220905421650618342.128.zip?download_name=RLC_511WA_22041509.zip) | 2022‑04‑15 | <ol><li>Upgraded ONVIF protocol to version 21.06</li><li>Solved the issue of no audio output on some platforms using ONVIF</li><li>Added the fixed FPS setting: The FPS won't be reduced automatically at night</li><li>Added multiple selection for the iFrame setting</li><li>Solved the problem that FTP parameters do not take effect under WEB access</li><li>Upgraded AI model to reduce false negatives and false positives</li><li>Added the function of synchronously prohibiting Push after disabling the UID</li><li>Added the security policy of login lockout</li><li>Solved some bugs of FTP</li><li>Solved some bugs of Email alert</li><li>Solved the problem of failing to adjust the threshold setting</li><li>Modified the display script of anti-flicker</li></ol> | 1.Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading

</details>

<details>
  <summary>RLC-520 *</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2022/04/180839551650271195.8689.png" width="150">

[Product page](https://reolink.com/product/rlc-520/)

  ### IPC_51516M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.660_21102210](https://drive.google.com/uc?id=1OxYUaRVwHu1p3S2lJ-8Cnw7QIDYQ55uZ&confirm=t)<br />[v3.0.0.660_21102210](https://drive.google.com/uc?id=1yghPki0FwNI8n51QDBiOuFYZy7LllArZ&confirm=t) | 2021‑10‑22 | I-frame beta test. Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/qkdgyr/beta_firmware_test_for_iframe_iframe_for_nonai/)<br />[Source 2](https://drive.google.com/drive/folders/16IwkW1C_jHfOG34pe6RSn9kpNZ36lT_G)<br />[Source 3](https://www.reddit.com/r/reolinkcam/comments/p9wwx8/082321_new_firmware_update_for_all_ai_cameras/i4y5f12/)<br />[Source 4](https://www.reddit.com/r/reolinkcam/comments/u1ri3n/rlc811a_firmware_that_supports_iframe/)<br />[Source 5](https://drive.google.com/drive/folders/1geZXbRUuUHP2WIajjV3MygUmtQPR7Tq4)
[v3.0.0.136_20121112](https://home-cdn.reolink.us/wp-content/uploads/2020/12/180831011608280261.4311.zip?download_name=firmware_RLC_520_v300136.zip)<br />[v3.0.0.136_20121112](https://reolink-storage.s3.amazonaws.com/website/firmware/20201211firmware/RLC-520_136_20121112.zip) | 2020‑12‑11 | <ol><li>Optimized day and night switching effect.</li><li>Optimized network transmission protocol to improve network security.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment</li><li>Solved other known bugs</li></ol> | If your camera's hardware version does not begin with IPC_51516M5M, please wait for the new firmware release.<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.116_20103112](https://home-cdn.reolink.us/files/firmware/20201031firmware/RLC-520_116_20103102.zip)<br />[v3.0.0.116_20103112](https://home-cdn.reolink.us/files/firmware/20201031firmware/RLC-520_116_20103112.zip) | 2020‑10‑31 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function</li><li>Optimized network transmission protocol to improve network security</li><li>Optimized P2P connection</li><li>Solved the problem that FTP recording doesn't have pre-recorded function</li><li>Solved the problem of email test with an empty password and some mail sending bugs</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when the it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20210803040404/https://support.reolink.com/hc/en-us/articles/900004398063-10-31-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M5M-)
[v3.0.0.65_20071012](https://reolink-storage.s3.amazonaws.com/website/firmware/20200721firmware/RLC-520-5MP_65_20071012.zip) | 2020‑07‑10 | <ol><li>Fixed the bug that FTP upload file failed.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed other bugs.</li></ol> | [Archive](https://web.archive.org/web/20201128230059/https://support.reolink.com/hc/en-us/articles/900001840706-07-10-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.647_20031413](https://home-cdn.reolink.us/files/firmware/20200314firmware/RLC-520_647_20031413.zip) | 2020‑03‑14 |  | 

  ### IPC_515B16M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.660_21111507](https://drive.google.com/uc?id=1PQMIWXS6mEELsirf4k1fkQMxz9z7j_pJ&confirm=t) | 2021‑11‑15 | I-frame beta test. Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/qkdgyr/beta_firmware_test_for_iframe_iframe_for_nonai/)<br />[Source 2](https://drive.google.com/drive/folders/16IwkW1C_jHfOG34pe6RSn9kpNZ36lT_G)
[v3.0.0.136_20121112](https://home-cdn.reolink.us/wp-content/uploads/2020/12/291300341609246834.5876.zip?download_name=firmware_RLC_520_v300136.zip)<br />[v3.0.0.136_20121112](https://reolink-storage.s3.amazonaws.com/website/firmware/20210106+firmware/RLC-520_v300136_20121112.zip) | 2020‑12‑11 | <ol><li>Optimized day and night switching effect</li><li>Optimized network transmission.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment.</li><li>Solved other known bugs</li></ol> | This firmware is ONLY for RLC-520(with hardware version IPC_515B16M5M)<br /> If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.

</details>

<details>
  <summary>RLC-520A</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/12/200329491639970989.7717.png" width="150">

[Product page](https://reolink.com/product/rlc-520a/)

  ### IPC_523128M5MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.951_22041566](https://home-cdn.reolink.us/wp-content/uploads/2022/04/151159241650023964.2105.zip?download_name=RLC_520A_22041566.zip) | 2022‑04‑15 | <ol><li>Upgraded ONVIF protocol to version 21.06</li><li>Solved the issue of no audio output on some platforms using ONVIF</li><li>Added the fixed FPS setting: The FPS won't be reduced automatically at night</li><li>Added multiple selection for the iFrame setting</li><li>Solved the problem that FTP parameters do not take effect under WEB access</li><li>Upgraded AI model to reduce false negatives and false positives</li><li>Added the function of synchronously prohibiting Push after disabling the UID</li><li>Added the security policy of login lockout</li><li>Solved some bugs of FTP</li><li>Solved some bugs of Email alert</li><li>Solved the problem of failing to adjust the threshold setting</li><li>Modified the display script of anti-flicker</li></ol> | 1.Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading
[v3.0.0.660_21102102](https://drive.google.com/uc?id=1hPrhIcoK26rSxUdZEw4ACwZ6Yo75HwZj&confirm=t) | 2021‑10‑21 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/p9wwx8/082321_new_firmware_update_for_all_ai_cameras/i4y5f12/)<br />[Source 2](https://www.reddit.com/r/reolinkcam/comments/u1ri3n/rlc811a_firmware_that_supports_iframe/)<br />[Source 3](https://drive.google.com/drive/folders/1geZXbRUuUHP2WIajjV3MygUmtQPR7Tq4)
[v3.1.0.598_21091300](https://drive.google.com/uc?id=1U3uioO-z3cLfqPKy0eK_vWDavrZuAI6a&confirm=t) | 2021‑09‑13 | Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/ptupxs/tester_wanted_for_the_beta_test_for_new_ai/)<br />[Source 2](https://drive.google.com/drive/folders/1S1KCRPH7u0BQ02D2drxLTmnsb7tyD17v)
[v3.0.0.160_21010800](https://reolink-storage.s3.amazonaws.com/website/firmware/20210112firmware/RLC-520A_160_21010800.zip) | 2021‑01‑08 | <ol><li>Corrected the text in the alert email.</li><li>Solved the problem that the MD status of API URL always displaying as triggered.</li><li>Solved the problem that failed to download videos via the Reolink client.</li><li>Solved other known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210801104604/https://support.reolink.com/hc/en-us/articles/900004125186-01-12-2021-Firmware-for-RLC-520A-RLC-510A-RLC-820A-RLC-810A)
[v3.0.0.124_20112600](https://home-cdn.reolink.us/files/firmware/20201126Firmware/RLC-520A_124_20112600.zip) | 2020‑11‑26 | <ol><li>Solved the problem that common users cannot turn on push notifications.</li><li>Frame rate adjustment: For 8MP cameras, the highest frame rate of any resolution is 25 frames.</li><li>Supporting Clear H265 stream in ONVIF, RTSP preview for 8MP cameras.</li><li>Solved H265 freezing issue on Blue Iris.</li><li>MD filters Human/Vehicle detection false alerts and MD area is synchronized by the Human/Vehicle detection.</li><li>Enhanced SD card driver to solve the problem that some SD cards cannot be recognized.</li><li>Solved the flickering problem when set to the lowest exposure value (50Hz).</li></ol> | [Archive](https://web.archive.org/web/20210725182423/https://support.reolink.com/hc/en-us/articles/900003792966-11-26-2020-Firmware-for-RLC-510A-RLC-520A-RLC-810A-RLC-820A-IPC-523128M-)

  ### IPC_523128M5MP_V2
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2368_23062701](https://support-d.reolink.com/attachments/token/t4dIPW2Qw4zgWGliwvDCbFSGK/?name=IPC_523128M5MP_V2.2368_23062701.RLC-520A.OV05A10.5MP.REOLINK.pak) | 2023‑06‑27 | Add pet detection | [Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/25)
[v3.1.0.1228_22082201](https://support.reolink.com/attachments/token/tb9cE1rSuu2Iat6TBCs14Y9ld/?name=IPC_523128M5MP_V2.1228_22082201.RLC-520A.OV05A10.5MP.REOLINK.pak) | 2022‑08‑22 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/xpb5jy/firmware_update_520a_fail/iqc2hqf/)<br />[Source 2](https://www.reddit.com/r/reolinkcam/comments/xq2bh6/how_long_has_the_rlc520a_v2_been_available/iqq99u0/)

</details>

<details>
  <summary>RLC-522 *</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2020/02/rlc-522-340.png" width="150">

[Product page](https://reolink.com/product/rlc-522/)

  ### IPC_51516M5M
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.757_21121512](https://support.reolink.com/attachments/token/iSWMzBTCkhptip2tj4jFFUoXo/?name=IPC_51516M5M.757_21121512.RLC-522.OV05A10.5MP.AF.D7.REOLINK.pak) | 2021‑12‑15 | Fixed I-frame switch button | [Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/13)
[v3.0.0.136_20121111](https://home-cdn.reolink.us/wp-content/uploads/2020/12/181027371608287257.9469.zip?download_name=firmware_RLC_522_v300136.zip)<br />[v3.0.0.136_20121111](https://reolink-storage.s3.amazonaws.com/website/firmware/20201211firmware/RLC-522_136_20121111.zip) | 2020‑12‑11 | <ol><li>Optimized day and night switching effect.</li><li>Optimized network transmission protocol to improve network security.</li><li>Solved the problem that the DHCP hostname is eth0 on the router.</li><li>Solved the problem that there is no email interval in the email setting on the web.</li><li>Solved the problem of copywriting in the received email when only pictures are configured as email attachment</li><li>Solved other known bugs</li></ol> | If your camera's hardware version does not begin with IPC_51516M5M, please wait for the new firmware release.<br />If you don't want to restore your camera settings to factory status, please uncheck/ don't enable the" update configuration File" option.
[v3.0.0.116_20103111](https://home-cdn.reolink.us/files/firmware/20201031firmware/RLC-522_116_20103111.zip) | 2020‑10‑31 | <ol><li>Added the new web terminal that supports HTML5 player, which mainly solved the Flash expiring problem.</li><li>Added the SD card 7*24 hours recording function</li><li>Optimized network transmission protocol to improve network security</li><li>Optimized P2P connection</li><li>Solved the problem that FTP recording doesn't have pre-recorded function</li><li>Solved the problem of email test with an empty password and some mail sending bugs</li><li>Solved the problem that FTP test failed and unable to upload pictures under Linux system</li><li>Solved the problem of two default routes, mainly to solve the problem that the camera cannot be connected to the VPN network when the it's connected to WiFi</li><li>Solved the false alert issue which is caused when using PTZ function.</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20210803040404/https://support.reolink.com/hc/en-us/articles/900004398063-10-31-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M5M-)
[v3.0.0.65_20071011](https://reolink-storage.s3.amazonaws.com/website/firmware/20200721firmware/RLC-522-5MP_65_20071011.zip) | 2020‑07‑10 | <ol><li>Fixed the bug that FTP upload file failed.</li><li>Added the thumbnail function-Reolink APP will display the image of each motion event during playback.</li><li>Fixed other bugs.</li></ol> | [Archive](https://web.archive.org/web/20201128230059/https://support.reolink.com/hc/en-us/articles/900001840706-07-10-2020-Firmware-for-Reolink-IP-Cameras-IPC-51516M-)
[v2.0.0.654_20040912](https://reolink-storage.s3.amazonaws.com/website/firmware/20200409firmware/RLC-522_654_20040912.zip) | 2020‑04‑09 | <ol><li>Extended the max password length of Email, FTP, and DDNS to 128 digits.</li><li>Updated the max cruise time to 300 seconds.</li></ol> | [Archive](https://web.archive.org/web/20210803033747/https://support.reolink.com/hc/en-us/articles/900000854106-04-09-2020-Firmware-for-Reolink-Auto-focus-IP-Cameras-IPC-51516M-)

</details>

<details>
  <summary>RLC-523WA</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/08/110250321628650232.2949.png" width="150">

[Product page](https://reolink.com/product/rlc-523wa/)

  ### IPC_523128M5MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2447_23071208](https://home-cdn.reolink.us/wp-content/uploads/2023/08/220431011692678661.2779.zip?download_name=RLC_523WA_2447_23071208.zip) | 2023‑07‑12 | <ol><li>Optimize WiFi Connection</li><li>Optimize the Patrol Feature</li><li>Fix some known bugs</li></ol> | 
[v3.1.0.2217_23051710](https://home-cdn.reolink.us/wp-content/uploads/2023/06/130205271686621927.9606.zip?download_name=523WA_v3102217_23051710_v10031.zip)<br />[v3.1.0.2217_23051710](https://support-d.reolink.com/attachments/token/KCvCCwPiYAQo4QMF77Bx6LAO6/?name=IPC_523128M5MP.2217_23051710.RLC-523WA.OV05A10.5MP.WIFI1021.PTZ.REOLINK.pak) | 2023‑05‑17 | <ol><li>Optimize network connection effect</li><li>Optimize the smart tracking effect</li><li>Optimize the AF focus function</li><li>Update the web version and optimize some UI displays</li><li>Fix some known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.1.0.1584_22120967](https://drive.google.com/uc?id=1txqFSJOccVge1nrUlYDKYKPfHEwbEEmJ&confirm=t) | 2022‑12‑09 | <ol><li>Added auto-tracking horizontal range. (Only for APP/Web.)</li><li>Added the auto-tracking schedule. (Only for APP/Web.)</li><li>Added the time settings to stop tracking and returning to the monitor point after the object stops and disappears. (Only for APP/Web)</li><li>Optimized AI model and multi-objective tracking experience.</li><li>Added preview images in Preset point. (PTZ)</li><li>Updated Web UI and added adaption to the above setting.</li></ol> | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/zkwfro/rlc823a_rlc523wa_tracking_beta_40_firmware_added/)<br />[Source 2](https://drive.google.com/drive/folders/1fuS2acVGEdhR1njItb87iaBZ550MWz2o)
[v3.1.0.1169_22091307](https://drive.google.com/uc?id=1vKRzh4aCHoy7Lq7zb1a_2si-Zh_rrBOs&confirm=t) | 2022‑09‑13 | Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/xe2pwk/rlc823a_rlc523wa_new_tracking_beta_firmware_and/)<br />[Source 2](https://community.reolink.com/topic/4092/rlc-823a-rlc-523wa-new-tracking-beta-firmware-and-new-tracking-features-plan)<br />[Source 3](https://drive.google.com/drive/folders/17l4qXHhWpnTgHkbthQhvmx1Q9wa8_O4e)
[v3.1.0.1169_22080508](https://drive.google.com/uc?id=1c1ZnOHFuFJZObfgL7XHwmxPjj-fFD07D&confirm=t) | 2022‑08‑05 | <ol><li>Solved the issue that the image got purple after switching between day and night modes.</li><li>Solved the issue that the IR didn't work after switching between day and night modes.</li><li>Optimized auto-tracking.</li></ol> | :warning: This is a beta firmware<br />Check the sources for details<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/wj9kxw/rlc823a_rlc523wa_beta_firmware_night_mode_issue/)<br />[Source 2](https://community.reolink.com/topic/3903/rlc-823a-rlc-523wa-beta-firmware-night-mode-issue-solved-and-auto-tracking-optimization)<br />[Source 3](https://drive.google.com/drive/folders/1QbwfJn7ik0AHFWKnM67umGWT5XWVea-d)
[v3.1.0.850_22032204](https://drive.google.com/uc?id=1yzP4iT5DMvKGJHHjmDuMk3_MDrIc4Zmv&confirm=t) | 2022‑03‑22 | Check the sources for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/tgax4i/rlc823a_rlc523wa_beta_firmware_pan_tilt/)<br />[Source 2](https://www.reddit.com/r/reolinkcam/comments/tm0ud7/continuous_updatefollow_up_of_the_rlc823a/)<br />[Source 3](https://community.reolink.com/topic/3116/rlc-823a-rlc-523wa-beta-firmware-pan-tilt-auto-tracking-optimization-updated-guard-point-issue-solved)
[v3.1.0.804_22011510](https://home-cdn.reolink.us/wp-content/uploads/2022/01/191103561642590236.7798.zip?download_name=RLC_523WA_22011510.zip) | 2022‑01‑15 | <ol><li>Optimized AI detection function<ol type="a"><li>Upgraded the AI model to improve the recognition accuracy of people, cars, and pets (the  new features of 8MP models), and optimized static AI false alarm issue</li><li>Increased the AI delay alarm function, which can reduce dynamic misjudgments caused by flying insects, rain, etc. by adjusting the delay gear</li><li>Optimized the alarm area settings to reduce false alarms in the shielded area</li><li>Optimized the AI sensitivity setting: It will not send AI alarm when the AI detection sensitivity is 0</li><li>Optimized the false alarms caused by day and night switching and lighting changes, and solved the problem that the spotlight will repeatedly turn on and off in some scenes</li><li>Optimized the automatic tracking function to solve the chaotic tracking problem of the camera in some scenarios</li><li>Added the vertical tracking function for RLC- 523WA, RLC-823A</li></ol></li><li>Added AI smart detection type option for spotlight, so you can choose AI type for the smart spotlight</li><li>Optimized FTP function<ol type="a"><li>Supported FTPS encryption to improve the security of FTP transfer files</li><li>Optimized the FTP transfer file type:You can choose to transfer only video, only pictures, and transfer both videos and pictures to the FTP server</li><li>Increased Overwrite function for picture only and video only function</li><li>Added 2s/5s/10s interval options for FTP capture picture</li><li>Optimized the upload file directory function: You can choose to folder by day/month, or save all files in the same folder</li></ol></li><li>Optimized the push function and increased the push interval setting function</li><li>Increased the Test error code function for the Email, FTP, push settings, which could help find the cause of the error</li><li>Added switch for RTSP, ONVIF, HTTP, HTTPS service. Users can turn on and off the corresponding network services as needed</li><li>Increased the function of locking the device: The device will be locked for 2 seconds after logging in with an incorrect password to improve login security and prevent malicious attacks</li><li>Added web certificate import function</li><li>Updated RTSP version</li><li>Optimized the AF algorithm to solve the problem of unclear focus in some scenes</li><li>Optimized pre-record time of videos and solved the problem of too long pre-record time in some scenes</li><li>Added day and night switching threshold adjustment function</li></ol> | 1. Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading
[v3.1.0.598_21091310](https://drive.google.com/uc?id=1C6hA0m8QlVuXenm7vyO5TtkhZzjD1uMs&confirm=t) | 2021‑09‑13 | Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/ptupxs/tester_wanted_for_the_beta_test_for_new_ai/)<br />[Source 2](https://drive.google.com/drive/folders/1S1KCRPH7u0BQ02D2drxLTmnsb7tyD17v)

</details>

<details>
  <summary>RLC-542WA</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/09/030134011630632841.2152.png" width="150">

[Product page](https://reolink.com/product/rlc-542wa/)

  ### IPC_523D95MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.1983_23040623](https://drive.google.com/uc?id=1RCume3f77oYMbZ3oD06cyD9O6F--uFiC&confirm=t) | 2023‑04‑06 | Add the option to change the I-frame interval | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/14)
[v3.1.0.764_21121718](https://home-cdn.reolink.us/wp-content/uploads/2022/01/191102001642590120.5321.zip?download_name=RLC_542WA_21121718.zip) | 2021‑12‑17 | <ol><li>Optimized AI detection function<ol type="a"><li>Upgraded the AI model to improve the recognition accuracy of people, cars, and pets (the  new features of 8MP models), and optimized static AI false alarm issue</li><li>Increased the AI delay alarm function, which can reduce dynamic misjudgments caused by flying insects, rain, etc. by adjusting the delay gear</li><li>Optimized the alarm area settings to reduce false alarms in the shielded area</li><li>Optimized the AI sensitivity setting: It will not send AI alarm when the AI detection sensitivity is 0</li><li>Optimized the false alarms caused by day and night switching and lighting changes, and solved the problem that the spotlight will repeatedly turn on and off in some scenes</li><li>Optimized the automatic tracking function to solve the chaotic tracking problem of the camera in some scenarios</li><li>Added the vertical tracking function for RLC- 523WA, RLC-823A</li></ol></li><li>Added AI smart detection type option for spotlight, so you can choose AI type for the smart spotlight</li><li>Optimized FTP function<ol type="a"><li>Supported FTPS encryption to improve the security of FTP transfer files</li><li>Optimized the FTP transfer file type:You can choose to transfer only video, only pictures, and transfer both videos and pictures to the FTP server</li><li>Increased Overwrite function for picture only and video only function</li><li>Added 2s/5s/10s interval options for FTP capture picture</li><li>Optimized the upload file directory function: You can choose to folder by day/month, or save all files in the same folder</li></ol></li><li>Optimized the push function and increased the push interval setting function</li><li>Increased the Test error code function for the Email, FTP, push settings, which could help find the cause of the error</li><li>Added switch for RTSP, ONVIF, HTTP, HTTPS service. Users can turn on and off the corresponding network services as needed</li><li>Increased the function of locking the device: The device will be locked for 2 seconds after logging in with an incorrect password to improve login security and prevent malicious attacks</li><li>Added web certificate import function</li><li>Updated RTSP version</li><li>Optimized the AF algorithm to solve the problem of unclear focus in some scenes</li><li>Optimized pre-record time of videos and solved the problem of too long pre-record time in some scenes</li><li>Added day and night switching threshold adjustment function</li></ol> | 1. Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading

</details>

<details>
  <summary>RLC-810A</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2020/07/rlc-810a-340.png" width="150">

[Product page](https://reolink.com/product/rlc-810a/)

  ### IPC_523128M8MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.1162_22072805](https://support.reolink.com/attachments/token/bKSdFp6o2FVWqOb0PvEejh7l2/?name=IPC_523128M8MP.1162_22072805.RLC-810A.IMX415.8MP.REOLINK.pak) | 2022‑07‑28 | Potential fix for the presence of artifacts in the RTSP stream | [Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/4)
[v3.1.0.956_22041503](https://home-cdn.reolink.us/wp-content/uploads/2022/04/181045241650278724.5249.zip?download_name=RLC_810A_22041503.zip) | 2022‑04‑15 | <ol><li>Upgraded ONVIF protocol to version 21.06</li><li>Solved the issue of no audio output on some platforms using ONVIF</li><li>Added the fixed FPS setting: The FPS won't be reduced automatically at night</li><li>Added multiple selection for the iFrame setting</li><li>Solved the problem that FTP parameters do not take effect under WEB access</li><li>Upgraded AI model to reduce false negatives and false positives</li><li>Added the function of synchronously prohibiting Push after disabling the UID</li><li>Added the security policy of login lockout</li><li>Solved some bugs of FTP</li><li>Solved some bugs of Email alert</li><li>Solved the problem of failing to adjust the threshold setting</li><li>Modified the display script of anti-flicker</li></ol> | 1.Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading
[v3.1.0.598_21091303](https://drive.google.com/uc?id=1TrHuNZC4Vk0DSc8oRa7nvP8XpA7INnL9&confirm=t) | 2021‑09‑13 | Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/ptupxs/tester_wanted_for_the_beta_test_for_new_ai/)<br />[Source 2](https://drive.google.com/drive/folders/1S1KCRPH7u0BQ02D2drxLTmnsb7tyD17v)
[v3.0.0.494_21073003](https://drive.google.com/uc?id=1Muea9bYzb6_0o2afvIBxH9dVfXd7WYEx&confirm=t)<br />[v3.0.0.494_21073003](https://home-cdn.reolink.us/wp-content/uploads/2021/08/201015421629454542.8734.zip) | 2021‑07‑30 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/p9wwx8/082321_new_firmware_update_for_all_ai_cameras/hb9iass/)<br />[Source 2](https://www.reddit.com/r/reolinkcam/comments/x4ga2a/comment/j7298vl)
[v3.0.0.250_21040803](https://home-cdn.reolink.us/wp-content/uploads/2021/06/170832521623918772.091.zip) | 2021‑04‑08 |  | 
[v3.0.0.177_21012103](https://home-cdn.reolink.us/wp-content/uploads/2021/01/290759321611907172.1659.zip)<br />[v3.0.0.177_21012103](https://reolink-storage.s3.amazonaws.com/website/firmware/20210121firmware/RLC_810A177_21012103.zip) | 2021‑01‑21 | <ol><li>Corrected the text in an alert email</li><li>Solved the problem that the MD status of API URL always displaying as triggered.</li><li>Solved the problem that failed to download videos via Reolink client.</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20210612235120/https://support.reolink.com/hc/en-us/articles/900004600266-21st-Jan-2021-Firmware-for-RLC-820A-RLC-810A)
[v3.0.0.160_21010803](https://reolink-storage.s3.amazonaws.com/website/firmware/20210112firmware/RLC-810A_160_21010803.zip) | 2021‑01‑08 | <ol><li>Corrected the text in the alert email.</li><li>Solved the problem that the MD status of API URL always displaying as triggered.</li><li>Solved the problem that failed to download videos via the Reolink client.</li><li>Solved other known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210801104604/https://support.reolink.com/hc/en-us/articles/900004125186-01-12-2021-Firmware-for-RLC-520A-RLC-510A-RLC-820A-RLC-810A)
[v3.0.0.124_20112603](https://home-cdn.reolink.us/files/firmware/20201126Firmware/RLC-810A_124_20112603.zip)<br />[v3.0.0.124_20112603](https://home-cdn.reolink.us/wp-content/uploads/2020/12/070944151607334255.147.zip) | 2020‑11‑26 | <ol><li>Solved the problem that common users cannot turn on push notifications.</li><li>Frame rate adjustment: For 8MP cameras, the highest frame rate of any resolution is 25 frames.</li><li>Supporting Clear H265 stream in ONVIF, RTSP preview for 8MP cameras.</li><li>Solved H265 freezing issue on Blue Iris.</li><li>MD filters Human/Vehicle detection false alerts and MD area is synchronized by the Human/Vehicle detection.</li><li>Enhanced SD card driver to solve the problem that some SD cards cannot be recognized.</li><li>Solved the flickering problem when set to the lowest exposure value (50Hz).</li></ol> | [Archive](https://web.archive.org/web/20210725182423/https://support.reolink.com/hc/en-us/articles/900003792966-11-26-2020-Firmware-for-RLC-510A-RLC-520A-RLC-810A-RLC-820A-IPC-523128M-)

  ### IPC_56064M8MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2368_23062505](https://home-cdn.reolink.us/wp-content/uploads/2023/08/110422361691727756.2053.zip?download_name=RLC_810A_2368_23062505.zip) | 2023‑06‑25 | <ol><li>Optimize IPC HDR function for adapting Reolink Client</li><li>Optimize the accuracy of email alarm</li><li>Optimize the image stability of day&amp;night mode switching</li><li>Optimize the stability of logging and previewing via the Web Client.</li><li>Solve other known bugs</li></ol> | 

</details>

<details>
  <summary>RLC-811A</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/03/050713171614928397.8822.png" width="150">

[Product page](https://reolink.com/product/rlc-811a/)

  ### IPC_523128M8MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2109_23051509](https://support-d.reolink.com/attachments/token/2b7ckPNIxn5zkQsdd3l5OkGcf/?name=IPC_523128M8MP.2109_23051509.RLC-811A.IMX415.8MP.AF.REOLINK.pak) | 2023‑05‑15 | <ol><li>New web interface</li><li>Possibility to connect IoT devices (eg. floodlight)</li><li>Ability to turn on "Illegal login lockout" under Advanced / User Management</li></ol> | Changes are given in comparison to v3.1.0.989<br />[Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/27)
[v3.1.0.989_22051908](https://home-cdn.reolink.us/wp-content/uploads/2022/10/251116081666696568.0877.zip?download_name=RLC_811A_989_22051908.zip)<br />[v3.1.0.989_22051908](https://support.reolink.com/attachments/token/MFdl4XblzOXg1IMWGGD8YHLhI/?name=IPC_523128M8MP.989_22051908.RLC-811A.IMX415.8MP.AF.REOLINK.pak) | 2022‑05‑19 | <ol><li>Updated the Web Client</li><li>The device name for the camera is not allowed to set to blank</li><li>Support setting time when the camera is connected by ONVIF (including time, time zone; DST setting is not supported)</li></ol> | 
[v3.1.0.956_22042008](https://home-cdn.reolink.us/wp-content/uploads/2022/04/220902031650618123.0652.zip?download_name=RLC_811A_22042008.zip) | 2022‑04‑20 | <ol><li>Upgraded ONVIF protocol to version 21.06</li><li>Solved the issue of no audio output on some platforms using ONVIF</li><li>Added the fixed FPS setting: The FPS won't be reduced automatically at night</li><li>Added multiple selection for the iFrame setting</li><li>Solved the problem that FTP parameters do not take effect under WEB access</li><li>Upgraded AI model to reduce false negatives and false positives</li><li>Added the function of synchronously prohibiting Push after disabling the UID</li><li>Added the security policy of login lockout</li><li>Solved some bugs of FTP</li><li>Solved some bugs of Email alert</li><li>Solved the problem of failing to adjust the threshold setting</li><li>Modified the display script of anti-flicker</li></ol> | 1.Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading
[v3.1.0.819_22020908](https://drive.google.com/uc?id=1bEmSi4106MCelekEc_Gu7pUlX0byDklC&confirm=t) | 2022‑02‑09 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/p9wwx8/082321_new_firmware_update_for_all_ai_cameras/i4y5f12/)<br />[Source 2](https://www.reddit.com/r/reolinkcam/comments/u1ri3n/rlc811a_firmware_that_supports_iframe/)<br />[Source 3](https://drive.google.com/drive/folders/1geZXbRUuUHP2WIajjV3MygUmtQPR7Tq4)
[v3.1.0.764_21121708](https://home-cdn.reolink.us/wp-content/uploads/2022/01/191049021642589342.9917.zip) | 2021‑12‑17 |  | 
[v3.1.0.598_21091308](https://drive.google.com/uc?id=12q_sIyYAm_uY8nGpSrOK9HKeJhwS2NPU&confirm=t) | 2021‑09‑13 | Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/ptupxs/tester_wanted_for_the_beta_test_for_new_ai/)<br />[Source 2](https://drive.google.com/drive/folders/1S1KCRPH7u0BQ02D2drxLTmnsb7tyD17v)
[v3.0.0.494_21073008](https://home-cdn.reolink.us/wp-content/uploads/2021/08/250156141629856574.003.zip) | 2021‑07‑30 |  | 
[v3.0.0.250_21040808](https://home-cdn.reolink.us/wp-content/uploads/2021/06/170836261623918986.2035.zip) | 2021‑04‑08 |  | 

</details>

<details>
  <summary>RLC-812A</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/07/230838461627029526.281.png" width="150">

[Product page](https://reolink.com/product/rlc-812a/)

  ### IPC_523B188MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.920_22040613](https://home-cdn.reolink.us/wp-content/uploads/2022/04/080932031649410323.7369.zip?download_name=RLC_812A_22040613.zip) | 2022‑04‑06 | <ol><li>Add auto mode for spotlight</li><li>Optimize images</li></ol> | 1.Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading

</details>

<details>
  <summary>RLC-81PA</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2023/05/250937451685007465.3074.png" width="150">

[Product page](https://reolink.com/product/rlc-81pa/)

  ### IPC_56064M8MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2557_23080802](https://home-cdn.reolink.us/wp-content/uploads/2023/09/190805551695110755.9205.zip?download_name=RLC_81PA_2557_23080802.zip) | 2023‑08‑08 | <ol><li>Optimize smart detection</li><li>Support horizontal auto-tracking</li><li>Fix some known bugs</li></ol> | 

</details>

<details>
  <summary>RLC-820A</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/07/310158421627696722.9425.png" width="150">

[Product page](https://reolink.com/product/rlc-820a/)

  ### IPC_523128M8MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.1387_22100622](https://support-d.reolink.com/attachments/token/9fhG99webOHErfL1GES7y7ZFU/?name=IPC_523128M8MP.1387_22100622.RLC-820A.IMX415.8MP.REOLINK.pak) | 2022‑10‑06 | Proper FTPS support | :exclamation: FTPS issue<br />Check the source for details<br />[Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/28)
[v3.1.0.956_22041501](https://home-cdn.reolink.us/wp-content/uploads/2022/04/181046431650278803.8671.zip?download_name=RLC_820A_22041501.zip) | 2022‑04‑15 | <ol><li>Upgraded ONVIF protocol to version 21.06</li><li>Solved the issue of no audio output on some platforms using ONVIF</li><li>Added the fixed FPS setting: The FPS won't be reduced automatically at night</li><li>Added multiple selection for the iFrame setting</li><li>Solved the problem that FTP parameters do not take effect under WEB access</li><li>Upgraded AI model to reduce false negatives and false positives</li><li>Added the function of synchronously prohibiting Push after disabling the UID</li><li>Added the security policy of login lockout</li><li>Solved some bugs of FTP</li><li>Solved some bugs of Email alert</li><li>Solved the problem of failing to adjust the threshold setting</li><li>Modified the display script of anti-flicker</li></ol> | 1.Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading
[v3.0.0.660_21101902](https://drive.google.com/uc?id=11fygt9xmdRZjqTrT9hQ9KkCf9ZFelPQj&confirm=t) | 2021‑10‑19 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/p9wwx8/082321_new_firmware_update_for_all_ai_cameras/i4y5f12/)<br />[Source 2](https://www.reddit.com/r/reolinkcam/comments/u1ri3n/rlc811a_firmware_that_supports_iframe/)<br />[Source 3](https://drive.google.com/drive/folders/1geZXbRUuUHP2WIajjV3MygUmtQPR7Tq4)
[v3.1.0.598_21091301](https://drive.google.com/uc?id=1f6NlVsCOpGHY04Vf-OuN4ZYHesf4-Dut&confirm=t) | 2021‑09‑13 | Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/ptupxs/tester_wanted_for_the_beta_test_for_new_ai/)<br />[Source 2](https://drive.google.com/drive/folders/1S1KCRPH7u0BQ02D2drxLTmnsb7tyD17v)
[v3.0.0.494_21073001](https://drive.google.com/uc?id=1Y1_0PZ2G-3-1AVzWjsdmx180TdK-coLC&confirm=t) | 2021‑07‑30 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/p9wwx8/082321_new_firmware_update_for_all_ai_cameras/hb9iass/)
[v3.0.0.412_21063001](https://home-cdn.reolink.us/wp-content/uploads/2021/07/130706021626159962.9614.zip) | 2021‑06‑30 |  | 
[v3.0.0.251_21040912](https://support.reolink.com/attachments/token/RWjfZKeQp51lsSwq8vIG4BZlC/?name=IPC_523128M8MP.251_21040912.RLC-820A.IMX415.8MP.REOLINK.pak) | 2021‑04‑09 |  | [Source 1](https://github.com/fwestenberg/reolink_dev/issues/86#issuecomment-850187682)
[v3.0.0.177_21012101](https://reolink-storage.s3.amazonaws.com/website/firmware/20210121firmware/RLC_820A177_21012101.zip) | 2021‑01‑21 | <ol><li>Corrected the text in an alert email</li><li>Solved the problem that the MD status of API URL always displaying as triggered.</li><li>Solved the problem that failed to download videos via Reolink client.</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20210612235120/https://support.reolink.com/hc/en-us/articles/900004600266-21st-Jan-2021-Firmware-for-RLC-820A-RLC-810A)
[v3.0.0.160_21010801](https://reolink-storage.s3.amazonaws.com/website/firmware/20210112firmware/RLC-820A_160_21010801.zip) | 2021‑01‑08 | <ol><li>Corrected the text in the alert email.</li><li>Solved the problem that the MD status of API URL always displaying as triggered.</li><li>Solved the problem that failed to download videos via the Reolink client.</li><li>Solved other known bugs.</li></ol> | [Archive](https://web.archive.org/web/20210801104604/https://support.reolink.com/hc/en-us/articles/900004125186-01-12-2021-Firmware-for-RLC-520A-RLC-510A-RLC-820A-RLC-810A)
[v3.0.0.124_20112601](https://home-cdn.reolink.us/files/firmware/20201126Firmware/RLC-820A_124_20112601.zip) | 2020‑11‑26 | <ol><li>Solved the problem that common users cannot turn on push notifications.</li><li>Frame rate adjustment: For 8MP cameras, the highest frame rate of any resolution is 25 frames.</li><li>Supporting Clear H265 stream in ONVIF, RTSP preview for 8MP cameras.</li><li>Solved H265 freezing issue on Blue Iris.</li><li>MD filters Human/Vehicle detection false alerts and MD area is synchronized by the Human/Vehicle detection.</li><li>Enhanced SD card driver to solve the problem that some SD cards cannot be recognized.</li><li>Solved the flickering problem when set to the lowest exposure value (50Hz).</li></ol> | [Archive](https://web.archive.org/web/20210725182423/https://support.reolink.com/hc/en-us/articles/900003792966-11-26-2020-Firmware-for-RLC-510A-RLC-520A-RLC-810A-RLC-820A-IPC-523128M-)

  ### IPC_56064M8MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2368_23062508](https://home-cdn.reolink.us/wp-content/uploads/2023/08/110430021691728202.6612.zip?download_name=RLC_820A_2368_23062508.zip) | 2023‑06‑25 | <ol><li>Optimize IPC HDR function for adapting Reolink Client</li><li>Optimize the accuracy of email alarm</li><li>Optimize the image stability of day&amp;night mode switching</li><li>Optimize the stability of logging and previewing via the Web Client.</li><li>Solve other known bugs</li></ol> | 

</details>

<details>
  <summary>RLC-822A</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2020/12/rlc-822a-400.png?v=1612231155490" width="150">

[Product page](https://reolink.com/product/rlc-822a/)

  ### IPC_523128M8MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.1643_22122401](https://support-d.reolink.com/attachments/token/sOqgLVUdAieuQbPLBkepxTNDt/?name=IPC_523128M8MP.1643_22122401.RLC-822A.IMX415.8MP.AF.REOLINK.pak) | 2022‑12‑24 | Optimize focusing function and some connection issues | [Source 1](https://www.reddit.com/r/reolinkcam/comments/14hvlsj/comment/jpo2llf)
[v3.1.0.989_22081907](https://home-cdn.reolink.us/wp-content/uploads/2022/10/251121381666696898.9487.zip?download_name=RLC_822A_989_22081907.zip) | 2022‑08‑19 | <ol><li>Updated the Web Client</li><li>The device name for the camera is not allowed to set to blank</li><li>Support setting time when the camera is connected by ONVIF (including time, time zone; DST setting is not supported)</li><li>Optimized AF focusing function for RLC-822A</li></ol> | 
[v3.1.0.956_22041507](https://home-cdn.reolink.us/wp-content/uploads/2022/04/220903111650618191.8255.zip?download_name=RLC_822A_22041507.zip) | 2022‑04‑15 | <ol><li>Upgraded ONVIF protocol to version 21.06</li><li>Solved the issue of no audio output on some platforms using ONVIF</li><li>Added the fixed FPS setting: The FPS won't be reduced automatically at night</li><li>Added multiple selection for the iFrame setting</li><li>Solved the problem that FTP parameters do not take effect under WEB access</li><li>Upgraded AI model to reduce false negatives and false positives</li><li>Added the function of synchronously prohibiting Push after disabling the UID</li><li>Added the security policy of login lockout</li><li>Solved some bugs of FTP</li><li>Solved some bugs of Email alert</li><li>Solved the problem of failing to adjust the threshold setting</li><li>Modified the display script of anti-flicker</li></ol> | 1.Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading
[v3.1.0.598_21091307](https://drive.google.com/uc?id=1b06v0rxvlDwjsI4EG4YyJdNoVJEwdjEa&confirm=t) | 2021‑09‑13 | Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/ptupxs/tester_wanted_for_the_beta_test_for_new_ai/)<br />[Source 2](https://drive.google.com/drive/folders/1S1KCRPH7u0BQ02D2drxLTmnsb7tyD17v)
[v3.0.0.412_21063007](https://home-cdn.reolink.us/wp-content/uploads/2021/07/130709041626160144.8842.zip) | 2021‑06‑30 |  | 

</details>

<details>
  <summary>RLC-823A</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/05/200630021621492202.9127.png" width="150">

[Product page](https://reolink.com/product/rlc-823a/)

  ### IPC_523128M8MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2217_23051711](https://home-cdn.reolink.us/wp-content/uploads/2023/06/130219191686622759.7987.zip?download_name=823A_v3102217_23051711_v10031.zip) | 2023‑05‑17 | <ol><li>Optimize network connection effect</li><li>Optimize the smart tracking effect</li><li>Optimize the AF focus function</li><li>Update the web version and optimize some UI displays</li><li>Fix some known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.1.0.1584_22120968](https://drive.google.com/uc?id=1BDEwz2NVhJaQLvZJ11aElQzm-APxNP8a&confirm=t) | 2022‑12‑09 | <ol><li>Added auto-tracking horizontal range. (Only for APP/Web.)</li><li>Added the auto-tracking schedule. (Only for APP/Web.)</li><li>Added the time settings to stop tracking and returning to the monitor point after the object stops and disappears. (Only for APP/Web)</li><li>Optimized AI model and multi-objective tracking experience.</li><li>Added preview images in Preset point. (PTZ)</li><li>Updated Web UI and added adaption to the above setting.</li></ol> | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/zkwfro/rlc823a_rlc523wa_tracking_beta_40_firmware_added/)<br />[Source 2](https://drive.google.com/drive/folders/1fuS2acVGEdhR1njItb87iaBZ550MWz2o)
[v3.1.0.1169_22091308](https://drive.google.com/uc?id=1neJkmtONo1i8V81hrN3JlQORgwB1HykR&confirm=t) | 2022‑09‑13 | Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/xe2pwk/rlc823a_rlc523wa_new_tracking_beta_firmware_and/)<br />[Source 2](https://community.reolink.com/topic/4092/rlc-823a-rlc-523wa-new-tracking-beta-firmware-and-new-tracking-features-plan)<br />[Source 3](https://drive.google.com/drive/folders/17l4qXHhWpnTgHkbthQhvmx1Q9wa8_O4e)
[v3.1.0.1169_22080509](https://drive.google.com/uc?id=1lByHFKuGseR1vTthDcgAeXLlwB9Dg-BD&confirm=t) | 2022‑08‑05 | <ol><li>Solved the issue that the image got purple after switching between day and night modes.</li><li>Solved the issue that the IR didn't work after switching between day and night modes.</li><li>Optimized auto-tracking.</li></ol> | :warning: This is a beta firmware<br />Check the sources for details<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/wj9kxw/rlc823a_rlc523wa_beta_firmware_night_mode_issue/)<br />[Source 2](https://community.reolink.com/topic/3903/rlc-823a-rlc-523wa-beta-firmware-night-mode-issue-solved-and-auto-tracking-optimization)<br />[Source 3](https://drive.google.com/drive/folders/1QbwfJn7ik0AHFWKnM67umGWT5XWVea-d)
[v3.1.0.1137_22072210](https://drive.google.com/uc?id=1SgWWUCQgOjiCW7Ov39P5xcIzPnb7VL4o&confirm=t) | 2022‑07‑22 |  | :warning: This is a beta firmware<br />:exclamation: Night mode issue<br />Check the source for details<br />[Source 1](https://community.reolink.com/topic/3830/updated-night-mode-issue-solved-beta-test-rlc-823a-rlc-523wa-beta-firmware-with-new-tracking-strategy/5)<br />[Source 2](https://drive.google.com/drive/folders/1jwsTrEvpSqXXWf8r4g6oC6Q41n5vvEzb)
[v3.1.0.989_22051911](https://home-cdn.reolink.us/wp-content/uploads/2022/10/251119471666696787.084.zip?download_name=RLC_823A_989_22051911.zip)<br />[v3.1.0.989_22051911](https://support.reolink.com/attachments/token/ktALcT7yl11qQIFLmol31EtMn/?name=IPC_523128M8MP.989_22051911.RLC-823A.IMX415.8MP.PTZ.REOLINK.pak) | 2022‑05‑19 | <ol><li>Updated the Web Client</li><li>The device name for the camera is not allowed to set to blank</li><li>Solved the problem of PT probabilistic failure</li><li>Support setting time when the camera is connected by ONVIF (including time, time zone; DST setting is not supported)</li></ol> | 
[v3.1.0.956_22041511](https://home-cdn.reolink.us/wp-content/uploads/2022/04/220907081650618428.3113.zip?download_name=RLC_823A_22041511.zip) | 2022‑04‑15 | <ol><li>Upgraded ONVIF protocol to version 21.06</li><li>Solved the issue of no audio output on some platforms using ONVIF</li><li>Added the fixed FPS setting: The FPS won't be reduced automatically at night</li><li>Added multiple selection for the iFrame setting</li><li>Solved the problem that FTP parameters do not take effect under WEB access</li><li>Upgraded AI model to reduce false negatives and false positives</li><li>Added the function of synchronously prohibiting Push after disabling the UID</li><li>Added the security policy of login lockout</li><li>Solved some bugs of FTP</li><li>Solved some bugs of Email alert</li><li>Solved the problem of failing to adjust the threshold setting</li><li>Modified the display script of anti-flicker</li><li>Solved the problem that the 823A cannot return to the stop position after restarting</li><li>Optimized the Auto-tracking function</li></ol> | 1.Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading
[v3.1.0.850_22032205](https://drive.google.com/uc?id=18e9JfVLO5jQ_JclcOMgKvrLfimDtd0ZG&confirm=t) | 2022‑03‑22 | Check the sources for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/tgax4i/rlc823a_rlc523wa_beta_firmware_pan_tilt/)<br />[Source 2](https://www.reddit.com/r/reolinkcam/comments/tm0ud7/continuous_updatefollow_up_of_the_rlc823a/)<br />[Source 3](https://community.reolink.com/topic/3116/rlc-823a-rlc-523wa-beta-firmware-pan-tilt-auto-tracking-optimization-updated-guard-point-issue-solved)
[v3.1.0.598_21091311](https://drive.google.com/uc?id=1FEB_upO0eVlOSKTEI68ufIm1HwhZOO7X&confirm=t) | 2021‑09‑13 | Check the source for details | :warning: This is a beta firmware<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/ptupxs/tester_wanted_for_the_beta_test_for_new_ai/)<br />[Source 2](https://drive.google.com/drive/folders/1S1KCRPH7u0BQ02D2drxLTmnsb7tyD17v)

</details>

<details>
  <summary>RLC-823A 16X</summary>

<img src="https://reolink.com/wp-content/uploads/2022/06/280949171656409757.1757.png" width="150">

[Product page](https://reolink.com/product/rlc-823a-16x/)

  ### IPC_523SD10
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2347_23061923](https://home-cdn.reolink.us/wp-content/uploads/2023/07/130312241689217944.9992.zip?download_name=RLC_823A_16X_23061923.zip) | 2023‑06‑19 | <ol><li>Optimize and solve the AF probabilistic focus failure</li><li>Optimize the FTP function</li><li>Optimize the Smart detection function</li><li>Optimize the ONVIF function</li><li>Solve some bugs with email alarms</li><li>Update Web Client content</li><li>Modify the cruise mechanism: If the cruise is interrupted by auto-tracking, the cruise will restart after the tracking stops and returns to the guard position for 10S.</li></ol> | 
[v3.1.0.1933_23032822](https://home-cdn.reolink.us/wp-content/uploads/2023/04/110650141681195814.9281.zip?download_name=RLC_823A_16X_23032822.zip) | 2023‑03‑28 | <ol><li>Update content on Web Client</li><li>Optimize ONVIF function</li><li>Fix some bugs in email alerts</li></ol> | 
[v3.1.0.1646_22122622](https://home-cdn.reolink.us/wp-content/uploads/2022/12/300258361672369116.5271.zip?download_name=RLC_823A_16X_22122622.zip) | 2022‑12‑26 | <ol><li>Added auto-tracking function</li><li>Optimized PT control effect</li><li>Added 3D Zoom function. (Supported on the Web Client, and will be supported on Reolink App/Client too after subsequent updates)</li><li>Added multiple image modes.</li><li>Optimized the image effect and solved the problem of color cast in some scenes</li><li>Optimized AF focusing effect</li><li>Solved other known bugs</li></ol> | 

</details>

<details>
  <summary>RLC-824A</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/08/050939301628156370.5693.png" width="150">

[Product page](https://reolink.com/product/rlc-824a/)

  ### IPC_523D88MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.920_22040614](https://home-cdn.reolink.us/wp-content/uploads/2022/04/080933231649410403.839.zip?download_name=RLC_824A_22040614.zip) | 2022‑04‑06 | <ol><li>Add auto mode for spotlight</li><li>Optimize images</li></ol> | 1.Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading

</details>

<details>
  <summary>RLC-830A</summary>

<img src="https://reolink.com/wp-content/uploads/2023/01/130709541673593794.6172.png" width="150">

[Product page](https://reolink.com/product/rlc-830a/)

  ### IPC_560SD78MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.2515_23082406](https://home-cdn.reolink.us/wp-content/uploads/2023/09/260155301695693330.9187.zip?download_name=RLC_830A_23082406.zip) | 2023‑08‑24 | <ol><li>Optimize the tracking algorithm and support vertical tracking</li><li>Add the animal detection function</li><li>Optimize smart detection</li><li>Fix some known bugs</li></ol> | 
[v3.1.0.2318_23060906](https://home-cdn.reolink.us/wp-content/uploads/2023/06/131028421686652122.492.zip?download_name=RLC_830A_23060906.zip) | 2023‑06‑09 | <ol><li>Optimize the tracking algorithm and support vertical tracking</li><li>Add the animal detection function</li></ol> | 

</details>

<details>
  <summary>RLC-842A</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/09/021016231630577783.2975.png" width="150">

[Product page](https://reolink.com/product/rlc-842a/)

  ### IPC_523D98MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.1.0.989_22051917](https://support.reolink.com/attachments/token/JH134V6um9pX3cfBwBhTz0l60/?name=IPC_523D98MP.989_22051917.RLC-842A.IMX415.8MP.AF.REOLINK.pak) | 2022‑05‑19 | Fixed ONVIF issue and I-frame switch button | [Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/13)
[v3.1.0.764_21121717](https://home-cdn.reolink.us/wp-content/uploads/2022/01/191052081642589528.6241.zip?download_name=RLC_842A_21121717.zip) | 2021‑12‑17 | <ol><li>Optimized AI detection function<ol type="a"><li>Upgraded the AI model to improve the recognition accuracy of people, cars, and pets (the  new features of 8MP models), and optimized static AI false alarm issue</li><li>Increased the AI delay alarm function, which can reduce dynamic misjudgments caused by flying insects, rain, etc. by adjusting the delay gear</li><li>Optimized the alarm area settings to reduce false alarms in the shielded area</li><li>Optimized the AI sensitivity setting: It will not send AI alarm when the AI detection sensitivity is 0</li><li>Optimized the false alarms caused by day and night switching and lighting changes, and solved the problem that the spotlight will repeatedly turn on and off in some scenes</li><li>Optimized the automatic tracking function to solve the chaotic tracking problem of the camera in some scenarios</li><li>Added the vertical tracking function for RLC- 523WA, RLC-823A</li></ol></li><li>Added AI smart detection type option for spotlight, so you can choose AI type for the smart spotlight</li><li>Optimized FTP function<ol type="a"><li>Supported FTPS encryption to improve the security of FTP transfer files</li><li>Optimized the FTP transfer file type:You can choose to transfer only video, only pictures, and transfer both videos and pictures to the FTP server</li><li>Increased Overwrite function for picture only and video only function</li><li>Added 2s/5s/10s interval options for FTP capture picture</li><li>Optimized the upload file directory function: You can choose to folder by day/month, or save all files in the same folder</li></ol></li><li>Optimized the push function and increased the push interval setting function</li><li>Increased the Test error code function for the Email, FTP, push settings, which could help find the cause of the error</li><li>Added switch for RTSP, ONVIF, HTTP, HTTPS service. Users can turn on and off the corresponding network services as needed</li><li>Increased the function of locking the device: The device will be locked for 2 seconds after logging in with an incorrect password to improve login security and prevent malicious attacks</li><li>Added web certificate import function</li><li>Updated RTSP version</li><li>Optimized the AF algorithm to solve the problem of unclear focus in some scenes</li><li>Optimized pre-record time of videos and solved the problem of too long pre-record time in some scenes</li><li>Added day and night switching threshold adjustment function</li></ol> | 1. Due to the addition of new functions and the modification of some functions, it's suggested  to check the Update Configuration File option when upgrading, or restore the camera after the firmware upgrading

</details>

<details>
  <summary>RLN16-410 (NVR)</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2017/11/rln16-410.png" width="150">

[Product page](https://reolink.com/product/rln16-410/?attribute_pa_version=rln16-410)

  ### H3MB02
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.4732_1728_21062800](https://home-cdn.reolink.us/wp-content/uploads/2022/11/150658471668495527.8315.zip?download_name=RLN16_410_21062800.zip) | 2021‑06‑28 | <ol><li>Optimized UI display and interaction</li><li>Fixed the large deviation problem when you use the mouse to choose the MD area</li><li>Added the function of controlling IPC spotlight on the NVR</li><li>Fixed the issue that it displays Error icon on the screen when the buzzer sounds</li></ol> | 
[v2.0.0.4725_1724_20120700](https://home-cdn.reolink.us/wp-content/uploads/2020/12/160325521608089152.8522.zip)<br />[v2.0.0.4725_1724_20120700](https://reolink-storage.s3.amazonaws.com/website/firmware/20201220firmware/RLN16-410_20201220.zip) | 2020‑12‑07 | <ol><li>Added the new web terminal that supports the HTML5 player, which mainly solved the Flash expiring problem.</li><li>Solved the problem that Reolink App failed to obtain the PTZ configuration on some IPC.</li><li>Fixed the wrong subject of the reminder email when the hard disk is full.</li></ol> | [Archive](https://web.archive.org/web/20210728201554/https://support.reolink.com/hc/en-us/articles/900003949986-12-07-2020-Firmware-for-Reolink-RLN4-RLN8-410-RLN8-410-E-and-RLN16-410-H3MB02-)
[v2.0.0.4712_1722_20092900](https://reolink-storage.s3.amazonaws.com/website/firmware/20200928firmware+/RLN16-410-20092900.zip) | 2020‑09‑29 | <ol><li>Improved the overall performance of the network and enhance communication reliability</li><li>Solved the problem that P2P connection is lost occasionally during long time connection, and the NVR needs to be restarted to restore the connection</li><li>Optimized system performance and fixed some other bugs</li></ol> | [Archive](https://web.archive.org/web/20210805123857/https://support.reolink.com/hc/en-us/articles/900002938243-09-28-2020-Firmware-for-Reolink-RLN8-410-E-RLN4-410-and-RLN16-410)
[v2.0.0.4700_1719_20022616100](https://reolink-storage.s3.amazonaws.com/website/firmware/20200226firmware/RLN16-410_0226.zip) | 2020‑02‑26 | <ol><li>Unified the version of the NVRs that have the UID number beginning with XCP and 9527.</li><li>Updated the file managing system (fixing the bug of the HDD showing 0GB)</li><li>Updated the max patrol time of the RLC-423 PTZ dome camera to 300 seconds.</li><li>Fixed the bug of FTP uploading not following the size set.</li><li>Updated the web version and fixed some bugs on the web browser access.</li><li>Fixed the bug of the stutter in live view and playback (mainly due to camera's complex scene).</li><li>Fixed some other bugs.</li></ol> | [Archive](https://web.archive.org/web/20210620010534/https://support.reolink.com/hc/en-us/articles/900000296143-02-26-2020-Firmware-for-Reolink-RLN16-410-H3MB02-)
[v2.0.0.4679_1708_19082316100](https://reolink-storage.s3.amazonaws.com/website/firmware/20190823firmware/RLN16-410_0823.zip) | 2019‑08‑23 | <ol><li>Add the function of creating subdirectories by date in FTP.</li><li>Add the function that the DDNS server address can be set.</li><li>Add the function that IPC can control the IR LED when connecting to the NVR.</li><li>Move the language settings page forward in the process of Wizard Setup.</li><li>Remove configuration import function.</li><li>The username has to consist of 3~31 numbers, letters, and underscores.</li><li>Add a 7+1 polling mechanism in the LiveView interface.</li><li>Add Russian and German language options.</li><li>The password of the admin supports input spaces.</li><li>Fixed the download timeout failure in web Client.</li><li>Improved the clip function in web Client.</li><li>Optimize the NVR interface display.</li></ol> | [Archive](https://web.archive.org/web/20210726185430/https://support.reolink.com/hc/en-us/articles/360034504874-08-23-2019-Firmware-for-Reolink-RLN8-410-and-RLN16-410-Only-for-NVR-with-UID-95270000XXXXXXXX-)
[v2.0.0.4509_1606_18081116100](https://cdn.reolink.com/files/firmware/20180814firmware/RLN16-410_180811.zip)<br />[v2.0.0.4509_1606_18081116100](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLN16-410_180811.zip)<br />[v2.0.0.4509_1606_18081116100](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLN16-410_180811.zip) | 2018‑08‑11 |  | [Archive](https://web.archive.org/web/20210724050558/https://support.reolink.com/hc/en-us/articles/360012551153-08-11-2018-Firmware-for-Reolink-NVRs)
[v2.0.0.4468_1572_18030616100](https://cdn.reolink.com/files/firmware/20180402firmware/RLN16-410_180306.zip)<br />[v2.0.0.4468_1572_18030616100](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLN16-410_180306.zip)<br />[v2.0.0.4468_1572_18030616100](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLN16-410_180306.zip) | 2018‑03‑06 |  | 
[v2.0.0.4265_1489_1709141](https://s3.amazonaws.com/reolink-storage/website/firmware/rln16/RLN16_170914.zip) | 2017‑09‑14 |  | 
[v2.0.0.4265_1489](https://s3.amazonaws.com/reolink-storage/website/firmware/842_170524/RLN16-410_170605.zip) | 2017‑06‑05 |  | 
[v2.0.0.4240_1468](https://s3.amazonaws.com/reolink-storage/website/firmware/rln16/RLN16-410_170407.zip) | 2017‑04‑07 |  | 

  ### H3MB18
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.3.0.226_23031645](https://home-cdn.reolink.us/wp-content/uploads/2023/03/290837251680079045.0602.zip?download_name=RLN16_410_23031645.zip) | 2023‑03‑16 | <ol><li>Optimize the interface and interaction.</li><li>Compatible with fisheye series models.</li><li>Compatible with RLC-81PA model.</li><li>Support configuring auto-tracking and AI audio noise reduction settings for TrackMix series camera.</li><li>Support configuring splicing settings for Duo 2 series.</li><li>Support the 3D positioning function for RLC-823A 16X.</li><li>Support switches to control status light and the visitor button not trigger the horn control for Reolink Doorbell series.</li><li>Optimize privacy mask UI.</li><li>Add login lock function.</li><li>Add downlink port network segment configuration function.</li><li>Add IOT device timing constant light time point sorting.</li><li>Update RTSP.</li><li>Upgrade ONVIF version.</li><li>Update web client.</li><li>Solved other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.2.0.218_23020154](https://home-cdn.reolink.us/wp-content/uploads/2023/02/100651111676011871.9586.zip?download_name=RLN16_410_23020154.zip) | 2023‑02‑01 | <ol><li>Optimize the interface and interaction.</li><li>Add the function of keeping video recordings for the latest 1day.</li><li>Adapted to RLC-81MA models.</li><li>Optimize network related settings.</li><li>Update web client.</li><li>Solved other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.2.0.214_22120248](https://home-cdn.reolink.us/wp-content/uploads/2022/12/031000031670061603.2279.zip?download_name=RLN16_410_22120248.zip) | 2022‑12‑02 | <ol><li>Optimized experience for preview and playback</li><li>Adapted to Reolink Video Doorbell</li><li>Adapted to Reolink Floodlight series cameras</li><li>Solved the adaptation problem of TrackMix series and Duo2 series cameras</li><li>Solved the problem that common users cannot enable push</li><li>Solved the problem that Doorbell cameras cannot load the audio interface on iOS App when connected to Reolink NVR</li><li>Solved the problem that the FTP function of the NVR can not be saved when setting it via iOS App</li><li>Solved the problem that the video section after 00:00(UTC) cannot be searched out when using  the Clip function</li><li>Optimize network related settings.</li><li>Update web client</li><li>Solved other known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.2.0.212_22111848](https://home-cdn.reolink.us/wp-content/uploads/2022/11/181156111668772571.0089.zip?download_name=RLN16_410_22111848.zip) | 2022‑11‑18 | <ol><li>Optimized experience for preview and playback</li><li>Adapted to Reolink Floodlight series cameras</li><li>Solved the adaptation problem of TrackMix series and Duo2 series cameras</li><li>Solved the problem that common users cannot enable push</li><li>Solved the problem that Doorbell cameras cannot load the audio interface on iOS App when connected to Reolink NVR</li><li>Solved the problem that the FTP function of the NVR can not be saved when setting it via iOS App</li><li>Solved the problem that the video section after 00:00(UTC) cannot be searched out when using  the Clip function</li><li>Update web client</li><li>Solved other known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.1.0.211_22102414](https://home-cdn.reolink.us/wp-content/uploads/2022/10/261022101666779730.2575.zip?download_name=RLN16_410_211_22102414.zip) | 2022‑10‑24 | <ol><li>Adapted to Reolink Video Doorbell</li><li>Optimized the experience of Preview and Playback</li><li>Update web client</li><li>Fix other known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.200_22081549](https://home-cdn.reolink.us/wp-content/uploads/2022/08/171010511660731051.7874.zip?download_name=RLN16_410_22081549.zip) | 2022‑08‑15 | <ol><li>Solved the problem of pixelated image in complex scenes.</li><li>Optimize the interface and interaction.</li><li>Add the option to enable or disable the status reminder icon displayed on the preview screen.</li><li>Solve the problem that the login box input will disappear automatically after 30s.</li><li>Add the function of setting IPC Day/Night switching thresholds.</li><li>Add the function of setting a siren schedule for IPC camera.</li><li>Add the function of customizing the siren of the camera connected to the NVR through the Reolink App</li><li>Add push test and the settings for the interval time</li><li>Optimize network related settings</li><li>Add zoom function on the playback page, and add full-screen playback function</li><li>Fix bug in Hebrew</li><li>Add Portuguese</li><li>Add the function of keeping video recordings for the latest 2days, 3days, 7 days, 14 days and 30 days</li><li>Adapt to more new models, such as: Duo series, Duo2 series, TrackMix series, etc.</li><li>Support multi-screen display mode, which adapts to connect multiple (Duo series, TrackMix) series IPCs to the NVR, but the total number of cameras cannot exceed 16 devices respectively</li><li>Update web client</li><li>Update to support using ONVIF to access NVR's H.256 bit rate</li><li>Supporting picture-in-picture preview for Reolink Trackmix camera</li><li>Added person, vehicle and pet options for Spotlight Auto Night mode</li><li>Added configuration options of Fixed Frame Rate and Auto Frame Rate</li><li>Fix other known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.199_22080948](https://drive.google.com/uc?id=1ZqEroWfIPGIUNSbFeEtfNRmMIqzlkKud&confirm=t) | 2022‑08‑09 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)
[v3.0.0.198_22072813](https://home-cdn.reolink.us/wp-content/uploads/2022/07/291257301659099450.3337.zip?download_name=RLN16_410_22072813.zip) | 2022‑07‑28 | <ol><li>Optimize the interface and interaction.</li><li>Add the option to enable or disable the status reminder icon displayed on the preview screen.</li><li>Solve the problem that the login box input will disappear automatically after 30s.</li><li>Add the function of setting IPC Day/Night switching thresholds.</li><li>Add the function of setting a siren schedule for IPC camera.</li><li>Add the function of customizing the siren of the camera connected to the NVR through the Reolink App</li><li>Add push test and the settings for the interval time</li><li>Optimize network related settings</li><li>Add zoom function on the playback page, and add full-screen playback function</li><li>Fix bug in Hebrew</li><li>Add Portuguese</li><li>Add the function of keeping video recordings for the latest 7 days, 14 days and 30 days</li><li>Support multi-screen display mode, which adapts to connect multiple (Duo series, TrackMix) series IPCs to the NVR, but the total number of cameras cannot exceed 16 devices respectively.</li><li>Update web client</li><li>Update to support using ONVIF to access NVR's H.256 bit rate</li><li>Fix other known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.186_22062406](https://drive.google.com/uc?id=1Wst49S5Tip-zcw37oASQaYTuc7Vwrto0&confirm=t) | 2022‑06‑24 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izny0re)
[v3.0.0.159_21122455](https://drive.google.com/uc?id=179EHGr6vh2i-Qaen1B38DZxEry_s8twg&confirm=t) | 2021‑12‑24 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/ti9o8u/image_upside_down_after_firmware_upgrade_rlc820a/i1hh2qf/)<br />[Source 2](https://www.reddit.com/r/reolinkcam/comments/u1yji2/client_v872_update_changed_to_save_the_stream/)<br />[Source 3](https://community.reolink.com/topic/3267/client-v8-7-2-update-changed-to-save-the-clear-stream-mode-setting)
[v3.0.0.148_21100910](https://home-cdn.reolink.us/wp-content/uploads/2021/10/150631251634279485.9265.zip) | 2021‑10‑09 |  | 
[v3.0.0.123_21031206](https://home-cdn.reolink.us/wp-content/uploads/2021/03/210325321616297132.1638.zip)<br />[v3.0.0.123_21031206](https://reolink-storage.s3.amazonaws.com/website/firmware/20210312firmware/RLN16-410.123_21031206.zip) | 2021‑03‑12 | <ol><li>Optimized UI interaction</li><li>Optimized email test error codes and copywriting</li><li>Solved HDD SMART display error</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20210801111909/https://support.reolink.com/hc/en-us/articles/900006218883-21st-Mar-2021-Firmware-for-Reolink-RLN8-410-H3MB18-or-N2MB02-and-RLN16-410-H3MB18-)
[v3.0.0.118_21020447](https://home-cdn.reolink.us/wp-content/uploads/2021/02/061051061612608666.808.zip)<br />[v3.0.0.118_21020447](https://reolink-storage.s3.amazonaws.com/website/firmware/20210206firmware/RLN16-410.118_21020446.zip) | 2021‑02‑04 | Solve the problem that the IPC probably cannot connect to NVR after powering off and restarting NVR. | [Archive](https://web.archive.org/web/20210803030929/https://support.reolink.com/hc/en-us/articles/900004388326-6th-Feb-2021-Firmware-for-Reolink-RLN8-410-and-RLN16-410-H3MB18-)
[v3.0.0.82_20102145](https://reolink-storage.s3.amazonaws.com/website/firmware/20201021firmware/RLN16-410_20102145.zip) | 2020‑10‑21 | <ol><li>Added function that can support 12MP cameras</li><li>Added a new web terminal that supports HTML5 player, which mainly solves the problem when FLASH expires</li><li>Newly added Smart Playback function (fast playback with continuous recording, normal speed playback with motion events).</li><li>Added the help prompt message when the email configuration is wrong</li><li>Solved the problem that NVR keeps restarting under special network environment in Beta version</li><li>Solved the problem when connecting PTZ cameras or setting preset points in the Beta version</li><li>Solved the problem that the old version cameras failed to obtain configuration information in the Beta version</li><li>Solved the problem of probabilistic AI recording without pre-recording</li><li>Solved the problem that the alarm is triggered for a short time (about 1 second) and the recording is not recorded probabilistically</li><li>Solved the problem of UI interaction and display errors</li><li>Fulfilled the suggestions and needs of users</li><li>Fixed other known bugs and optimized performance</li></ol> | [Archive](https://web.archive.org/web/20210129185403/https://support.reolink.com/hc/en-us/articles/900003335926-10-21-2020-Firmware-for-Reolink-RLN8-410-and-RLN16-410-H3MB18-)
[v3.0.0.59_20081248](https://reolink-storage.s3.amazonaws.com/website/firmware/20200812firmware/RLN16-410_20081248.zip) | 2020‑08‑12 | <ol><li>Adopt new UI and new interaction methods</li><li>Support upgrading automatically online function (via Reolink APP)</li><li>Optimize system performance</li></ol> | [Archive](https://web.archive.org/web/20201011161357/https://support.reolink.com/hc/en-us/articles/900002407106-08-12-2020-Firmware-for-Reolink-RLN8-410-and-RLN16-410-H3MB18-)
[v2.0.0.268_20042502](https://reolink-storage.s3.amazonaws.com/website/firmware/20200425firmware/RLN16-410_0425.zip) | 2020‑04‑25 | <ol><li>Fixed the bug that the camera frame rate cannot be configured with 25 fps.</li><li>Optimized the system performance of the NVR system.</li><li>Fixed some other bugs.</li></ol> | [Archive](https://web.archive.org/web/20200809001138/https://support.reolink.com/hc/en-us/articles/900000937423-04-25-2020-Firmware-for-Reolink-RLN16-410-H3MB18-)

  ### N6MB01
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.3.0.226_23031621](https://home-cdn.reolink.us/wp-content/uploads/2023/03/171057041679050624.0931.zip?download_name=RLN16_410_226_23031621.zip) | 2023‑03‑16 | <ol><li>Optimize the interface and interaction.</li><li>Compatible with fisheye series models.</li><li>Compatible with RLC-81PA model.</li><li>Support configuring auto-tracking and AI audio noise reduction settings for TrackMix series camera.</li><li>Support configuring splicing settings for Duo 2 series.</li><li>Support the 3D positioning function for RLC-823A 16X.</li><li>Support switches to control status light and the visitor button not trigger the horn control for Reolink Doorbell series.</li><li>Optimize privacy mask UI.</li><li>Add login lock function.</li><li>Add downlink port network segment configuration function.</li><li>Add IOT device timing constant light time point sorting.</li><li>Update RTSP.</li><li>Upgrade ONVIF version.</li><li>Update web client.</li><li>Solved other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.2.0.218_23011215](https://home-cdn.reolink.us/wp-content/uploads/2023/01/131015231673604923.4271.zip?download_name=RLN16_410_23011215.zip) | 2023‑01‑12 | <ol><li>Optimize the interface and interaction.</li><li>Optimized experience for preview and playback.</li><li>Add the function of keeping video recordings for the latest 1day.</li><li>Adapted to Reolink Video Doorbell.</li><li>Adapted to Reolink Floodlight series cameras.</li><li>Adapted to RLC-81MA models.</li><li>Solved the adaptation problem of TrackMix series and Duo2 series cameras.</li><li>Solved the problem that common users cannot enable push.</li><li>Solved the problem that Doorbell cameras cannot load the audio interface on iOS App when connected to Reolink NVR.</li><li>Solved the problem that the FTP function of the NVR can not be saved when setting it via iOS App.</li><li>Solved the problem that the video section after 00:00(UTC) cannot be searched out when using  the Clip function.</li><li>Optimize network related settings.</li><li>Update web client.</li><li>Solved other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.211_22102119](https://home-cdn.reolink.us/wp-content/uploads/2022/10/240910021666602602.7142.zip?download_name=RLN16_410_22102119.zip) | 2022‑10‑21 | <ol><li>Optimize the interface and interaction.</li><li>Support RTSP url access with the h264 field.</li><li>Update web client.</li><li>Add the function of keeping video recordings for the latest 2days, 3days, 7 days, 14 days and 30 days.</li><li>Added three full-screen playback modes for TrackMix series.</li><li>Added person, vehicle and pet options for Spotlight Auto Night mode.</li><li>Added configuration options of Fixed Frame Rate and Auto Frame Rate.</li><li>Solved the adaptation problem of TrackMix series and Duo 2 series.</li><li>Added interface copywriting to solve interface text errors.</li><li>Fix other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.201_22082208](https://home-cdn.reolink.us/wp-content/uploads/2022/08/261034021661510042.3577.zip?download_name=RLN16_410_22082208.zip) | 2022‑08‑22 | <ol><li>Optimize the interface and interaction.</li><li>Support RTSP url access with the h264 field.</li><li>Update web client.</li><li>Add the function of keeping video recordings for the latest 2days, 3days, 7 days, 14 days and 30 days.</li><li>Added three full-screen playback modes for TrackMix series.</li><li>Added person, vehicle and pet options for Spotlight Auto Night mode.</li><li>Added configuration options of Fixed Frame Rate and Auto Frame Rate.</li><li>Solved the adaptation problem of TrackMix series and Duo 2 series.</li><li>Fix other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.

</details>

<details>
  <summary>RLN36 (NVR)</summary>

<img src="https://reolink.com/wp-content/uploads/2022/04/180832461650270766.9435.png" width="150">

[Product page](https://reolink.com/product/rln36/)

  ### N5MB01
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.3.0.226_23031612](https://home-cdn.reolink.us/wp-content/uploads/2023/03/171057511679050671.2953.zip?download_name=RLN36_226_23031612.zip) | 2023‑03‑16 | <ol><li>Optimize the interface and interaction.</li><li>Compatible with fisheye series models.</li><li>Compatible with RLC-81PA model.</li><li>Support configuring auto-tracking and AI audio noise reduction settings for TrackMix series camera.</li><li>Support configuring splicing settings for Duo 2 series.</li><li>Support the 3D positioning function for RLC-823A 16X.</li><li>Support switches to control status light and the visitor button not trigger the horn control for Reolink Doorbell series.</li><li>Optimize privacy mask UI.</li><li>Add login lock function.</li><li>Add downlink port network segment configuration function.</li><li>Add IOT device timing constant light time point sorting.</li><li>Update RTSP.</li><li>Upgrade ONVIF version.</li><li>Update web client.</li><li>Solved other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.2.0.218_23011219](https://home-cdn.reolink.us/wp-content/uploads/2023/01/131012031673604723.2428.zip?download_name=RLN36_218_23011219.zip) | 2023‑01‑12 | <ol><li>Optimize the interface and interaction.</li><li>Optimized experience for preview and playback.</li><li>Add the function of keeping video recordings for the latest 1day.</li><li>Adapted to Reolink Video Doorbell.</li><li>Adapted to Reolink Floodlight series cameras.</li><li>Adapted to RLC-81MA models.</li><li>Solved the adaptation problem of TrackMix series and Duo2 series cameras.</li><li>Solved the problem that common users cannot enable push.</li><li>Solved the problem that Doorbell cameras cannot load the audio interface on iOS App when connected to Reolink NVR.</li><li>Solved the problem that the FTP function of the NVR can not be saved when setting it via iOS App.</li><li>Solved the problem that the video section after 00:00(UTC) cannot be searched out when using  the Clip function.</li><li>Optimize network related settings.</li><li>Update IO Alarm related settings.</li><li>Update web client.</li><li>Solved other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.211_22102136](https://home-cdn.reolink.us/wp-content/uploads/2022/10/240912131666602733.2786.zip?download_name=RLN36_211_22102136.zip) | 2022‑10‑21 | <ol><li>Optimize the interface and interaction.</li><li>Add the function of keeping video recordings for the latest 2days, 3days, 7 days, 14 days and 30 days.</li><li>Adapt to more new models, such as: Duo series, Duo2 series, TrackMix series, etc.</li><li>Update web client.</li><li>Added person, vehicle and pet options for Spotlight Auto Night mode.</li><li>Added configuration options of Fixed Frame Rate and Auto Frame Rate.</li><li>Update IO Alarm related settings.</li><li>Added interface copywriting to solve interface text errors.</li><li>Fix other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.205_22091310](https://home-cdn.reolink.us/wp-content/uploads/2022/09/140343241663127004.8487.zip?download_name=RLN36_205_22091310.zip) | 2022‑09‑13 | <ol><li>Optimize the interface and interaction.</li><li>Add the function of keeping video recordings for the latest 2days, 3days, 7 days, 14 days and 30 days.</li><li>Adapt to more new models, such as: Duo series, Duo2 series, TrackMix series, etc.</li><li>Update web client.</li><li>Added person, vehicle and pet options for Spotlight Auto Night mode.</li><li>Added configuration options of Fixed Frame Rate and Auto Frame Rate.</li><li>Update IO Alarm related settings.</li><li>Fix other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.

</details>

<details>
  <summary>RLN4-210W (NVR) *</summary>

  ### H2MB09
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.4529_1615_18090804100](https://cdn.reolink.com/files/firmware/20180814firmware/RLN4-210W_180908.zip)<br />[v2.0.0.4529_1615_18090804100](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLN4-210W_180908.zip)<br />[v2.0.0.4529_1615_18090804100](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLN4-210W_180908.zip) | 2018‑09‑08 |  | [Archive](https://web.archive.org/web/20210724050558/https://support.reolink.com/hc/en-us/articles/360012551153-08-11-2018-Firmware-for-Reolink-NVRs)

  ### H2MB11
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.4472_1582_18032004100](https://cdn.reolink.com/files/firmware/20180402firmware/RLN4-210W_180320.zip)<br />[v2.0.0.4472_1582_18032004100](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLN4-210W_180320.zip)<br />[v2.0.0.4472_1582_18032004100](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLN4-210W_180320.zip) | 2018‑03‑20 |  | 
[v2.0.0.4269_1490](https://s3.amazonaws.com/reolink-storage/website/firmware/rlnw4/RLK4-210W_170602.zip) | 2017‑06‑02 |  | 
[v2.0.0.4210_1448](https://s3.amazonaws.com/reolink-storage/website/firmware/rlnw4/RLK4-210W_161219.zip) | 2016‑12‑19 |  | 

</details>

<details>
  <summary>RLN4-410 (NVR) *</summary>

  ### H3MB02
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.4265_1489](https://cdn.reolink.com/files/firmware/842_170524/RLN4-410_170605.zip)<br />[v2.0.0.4265_1489](https://home-cdn.reolink.us/files/firmware/842_170524/RLN4-410_170605.zip)<br />[v2.0.0.4265_1489](https://s3.amazonaws.com/reolink-storage/website/firmware/842_170524/RLN4-410_170605.zip) | 2017‑06‑05 |  | 
[v2.0.0.4210_1447](https://cdn.reolink.com/files/firmware/rln4/RLN4-410_161219.zip)<br />[v2.0.0.4210_1447](https://home-cdn.reolink.us/files/firmware/rln4/RLN4-410_161219.zip)<br />[v2.0.0.4210_1447](https://s3.amazonaws.com/reolink-storage/website/firmware/rln4/RLN4-410_161219.zip) | 2016‑12‑19 |  | 

  ### H3MB17
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.274_20120700](https://reolink-storage.s3.amazonaws.com/website/firmware/20201220firmware/RLN4-410_20201220.zip) | 2020‑12‑07 | <ol><li>Added the new web terminal that supports the HTML5 player, which mainly solved the Flash expiring problem.</li><li>Solved the problem that Reolink App failed to obtain the PTZ configuration on some IPC.</li><li>Fixed the wrong subject of the reminder email when the hard disk is full.</li></ol> | [Archive](https://web.archive.org/web/20210728201554/https://support.reolink.com/hc/en-us/articles/900003949986-12-07-2020-Firmware-for-Reolink-RLN4-RLN8-410-RLN8-410-E-and-RLN16-410-H3MB02-)
[v2.0.0.271_20092800](https://reolink-storage.s3.amazonaws.com/website/firmware/20200928firmware+/RLN4-410-20092800.zip) | 2020‑09‑28 | <ol><li>Improved the overall performance of the network and enhance communication reliability</li><li>Solved the problem that P2P connection is lost occasionally during long time connection, and the NVR needs to be restarted to restore the connection</li><li>Optimized system performance and fixed some other bugs</li></ol> | [Archive](https://web.archive.org/web/20210805123857/https://support.reolink.com/hc/en-us/articles/900002938243-09-28-2020-Firmware-for-Reolink-RLN8-410-E-RLN4-410-and-RLN16-410)
[v2.0.0.269_20042900](https://reolink-storage.s3.amazonaws.com/website/firmware/20200429firmware/RLN4_042900.zip) | 2020‑04‑29 | <ol><li>Fixed the bug of the HDD showing 0GB or not formatted error.</li><li>Fixed the bug that the camera frame rate cannot be configured with 25 fps.</li><li>Added the self-verification mechanism under the new firmware upgrade process to avoid upgraded the wrong firmware version.</li><li>Fixed the freezing issue under the complex environment of live view and playback.</li><li>Optimized system performance and fixed some other bugs</li></ol> | [Archive](https://web.archive.org/web/20210805123029/https://support.reolink.com/hc/en-us/articles/900000976886-04-29-2020-Firmware-for-Reolink-RLN8-410-RLN8-410-E-and-RLN4)

</details>

<details>
  <summary>RLN8-410 (NVR)</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2018/08/store/rln8-16-410.png" width="150">

[Product page](https://reolink.com/product/rln8-410/?attribute_pa_version=rln8-410)

  ### H3MB02
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.4732_1728_21062800](https://home-cdn.reolink.us/wp-content/uploads/2022/11/150726101668497170.4503.zip?download_name=RLN8_410_21062800.zip) | 2021‑06‑28 | <ol><li>Optimized UI display and interaction</li><li>Fixed the large deviation problem when you use the mouse to choose the MD area</li><li>Added the function of controlling IPC spotlight on the NVR</li><li>Fixed the issue that it displays Error icon on the screen when the buzzer sounds</li></ol> | 
[v2.0.0.4725_1724_20120700](https://home-cdn.reolink.us/wp-content/uploads/2020/12/170415051608178505.0706.zip)<br />[v2.0.0.4725_1724_20120700](https://reolink-storage.s3.amazonaws.com/website/firmware/20201220firmware/RLN8-410_20201220.zip) | 2020‑12‑07 | <ol><li>Added the new web terminal that supports the HTML5 player, which mainly solved the Flash expiring problem.</li><li>Solved the problem that Reolink App failed to obtain the PTZ configuration on some IPC.</li><li>Fixed the wrong subject of the reminder email when the hard disk is full.</li></ol> | [Archive](https://web.archive.org/web/20210728201554/https://support.reolink.com/hc/en-us/articles/900003949986-12-07-2020-Firmware-for-Reolink-RLN4-RLN8-410-RLN8-410-E-and-RLN16-410-H3MB02-)
[v2.0.0.4679_1708_19082308100](https://reolink-storage.s3.amazonaws.com/website/firmware/20190823firmware/RLN8-410_0823.zip) | 2019‑08‑23 | <ol><li>Add the function of creating subdirectories by date in FTP.</li><li>Add the function that the DDNS server address can be set.</li><li>Add the function that IPC can control the IR LED when connecting to the NVR.</li><li>Move the language settings page forward in the process of Wizard Setup.</li><li>Remove configuration import function.</li><li>The username has to consist of 3~31 numbers, letters, and underscores.</li><li>Add a 7+1 polling mechanism in the LiveView interface.</li><li>Add Russian and German language options.</li><li>The password of the admin supports input spaces.</li><li>Fixed the download timeout failure in web Client.</li><li>Improved the clip function in web Client.</li><li>Optimize the NVR interface display.</li></ol> | [Archive](https://web.archive.org/web/20210726185430/https://support.reolink.com/hc/en-us/articles/360034504874-08-23-2019-Firmware-for-Reolink-RLN8-410-and-RLN16-410-Only-for-NVR-with-UID-95270000XXXXXXXX-)
[v2.0.0.4509_1606_18081108100](https://cdn.reolink.com/files/firmware/20180814firmware/RLN8-410_180811.zip)<br />[v2.0.0.4509_1606_18081108100](https://home-cdn.reolink.us/files/firmware/20180814firmware/RLN8-410_180811.zip)<br />[v2.0.0.4509_1606_18081108100](https://s3.amazonaws.com/reolink-storage/website/firmware/20180814firmware/RLN8-410_180811.zip) | 2018‑08‑11 |  | [Archive](https://web.archive.org/web/20210724050558/https://support.reolink.com/hc/en-us/articles/360012551153-08-11-2018-Firmware-for-Reolink-NVRs)
[v2.0.0.4468_1572_18030608100](https://cdn.reolink.com/files/firmware/20180402firmware/RLN8-410_180306.zip)<br />[v2.0.0.4468_1572_18030608100](https://home-cdn.reolink.us/files/firmware/20180402firmware/RLN8-410_180306.zip)<br />[v2.0.0.4468_1572_18030608100](https://s3.amazonaws.com/reolink-storage/website/firmware/20180402firmware/RLN8-410_180306.zip) | 2018‑03‑06 |  | 
[v2.0.0.4265_1489_1709142](https://s3.amazonaws.com/reolink-storage/website/firmware/rln8/RLN8-410_170914.zip) | 2017‑09‑14 |  | 
[v2.0.0.4265_1489](https://home-cdn.reolink.us/files/firmware/842_170524/RLN8-410_170605.zip)<br />[v2.0.0.4265_1489](https://s3.amazonaws.com/reolink-storage/website/firmware/842_170524/RLN8-410_170605.zip) | 2017‑06‑05 |  | 
[v2.0.0.4240_1468](https://s3.amazonaws.com/reolink-storage/website/firmware/rln8/RLN8-410_170407.zip) | 2017‑04‑07 |  | 

  ### H3MB16
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.280_21060101](https://drive.google.com/uc?id=1oXXUt4uVyFLVsMje8vtpTFa9nLak2mbs&confirm=t)<br />[v2.0.0.280_21060101](https://home-cdn.reolink.us/wp-content/uploads/2022/11/150700251668495625.1457.zip?download_name=RLN8_410_E_21060101.zip) | 2021‑06‑01 | <ol><li>Optimized UI display and interaction</li><li>Fixed the large deviation problem when you use the mouse to choose the MD area</li><li>Modified the push text in Chinese</li><li>Fixed bugs related with Push</li></ol> | 
[v2.0.0.274_20120701](https://drive.google.com/uc?id=1W89WeSbU47kHsG0mIuNHbm8QTk4a0-RQ&confirm=t)<br />[v2.0.0.274_20120701](https://home-cdn.reolink.us/wp-content/uploads/2020/12/110806061607673966.7966.zip)<br />[v2.0.0.274_20120701](https://reolink-storage.s3.amazonaws.com/website/firmware/20201220firmware/RLN8-410-E_20201220.zip)<br />[v2.0.0.274_20120701](https://support.reolink.com/attachments/token/42qcxM28AbR6Hlri7IVDc0Dlm/?name=HI3536CV100_NVR_8IP_REOLINK_L300_274_20120701.4K.pak) | 2020‑12‑07 | <ol><li>Added the new web terminal that supports the HTML5 player, which mainly solved the Flash expiring problem.</li><li>Solved the problem that Reolink App failed to obtain the PTZ configuration on some IPC.</li><li>Fixed the wrong subject of the reminder email when the hard disk is full.</li></ol> | [Archive](https://web.archive.org/web/20210728201554/https://support.reolink.com/hc/en-us/articles/900003949986-12-07-2020-Firmware-for-Reolink-RLN4-RLN8-410-RLN8-410-E-and-RLN16-410-H3MB02-)
[v2.0.0.271_20092801](https://reolink-storage.s3.amazonaws.com/website/firmware/20200928firmware+/RLN8-410-E-20092801.zip) | 2020‑09‑28 | <ol><li>Improved the overall performance of the network and enhance communication reliability</li><li>Solved the problem that P2P connection is lost occasionally during long time connection, and the NVR needs to be restarted to restore the connection</li><li>Optimized system performance and fixed some other bugs</li></ol> | [Archive](https://web.archive.org/web/20210805123857/https://support.reolink.com/hc/en-us/articles/900002938243-09-28-2020-Firmware-for-Reolink-RLN8-410-E-RLN4-410-and-RLN16-410)
[v2.0.0.269_20042901](https://reolink-storage.s3.amazonaws.com/website/firmware/20200429firmware/RLN8-410-E_042901.zip) | 2020‑04‑29 | <ol><li>Fixed the bug of the HDD showing 0GB or not formatted error.</li><li>Fixed the bug that the camera frame rate cannot be configured with 25 fps.</li><li>Added the self-verification mechanism under the new firmware upgrade process to avoid upgraded the wrong firmware version.</li><li>Fixed the freezing issue under the complex environment of live view and playback.</li><li>Optimized system performance and fixed some other bugs</li></ol> | [Archive](https://web.archive.org/web/20210805123029/https://support.reolink.com/hc/en-us/articles/900000976886-04-29-2020-Firmware-for-Reolink-RLN8-410-RLN8-410-E-and-RLN4)
[v2.0.0.142_19090408101](https://reolink-storage.s3.amazonaws.com/website/firmware/20190904firmware/RLN8-410-E_090401.zip) | 2019‑09‑04 |  | [Source 1](https://www.reddit.com/r/reolink/comments/endw89/rln8410e_firmware_question_upgrade/)

  ### N2MB02 or H3MB18
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.3.0.226_23031644](https://home-cdn.reolink.us/wp-content/uploads/2023/03/290832531680078773.1966.zip?download_name=RLN8_410_23031644.zip) | 2023‑03‑16 | <ol><li>Optimize the interface and interaction.</li><li>Compatible with fisheye series models.</li><li>Compatible with RLC-81PA model.</li><li>Support configuring auto-tracking and AI audio noise reduction settings for TrackMix series camera.</li><li>Support configuring splicing settings for Duo 2 series.</li><li>Support the 3D positioning function for RLC-823A 16X.</li><li>Support switches to control status light and the visitor button not trigger the horn control for Reolink Doorbell series.</li><li>Optimize privacy mask UI.</li><li>Add login lock function.</li><li>Add downlink port network segment configuration function.</li><li>Add IOT device timing constant light time point sorting.</li><li>Update RTSP.</li><li>Upgrade ONVIF version.</li><li>Update web client.</li><li>Solved other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.2.0.218_23020153](https://home-cdn.reolink.us/wp-content/uploads/2023/02/100655171676012117.5954.zip?download_name=RLN8_410_23020153.zip) | 2023‑02‑01 | <ol><li>Optimize the interface and interaction.</li><li>Add the function of keeping video recordings for the latest 1day.</li><li>Adapted to RLC-81MA models.</li><li>Optimize network related settings.</li><li>Update web client.</li><li>Solved other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.2.0.214_22120247](https://home-cdn.reolink.us/wp-content/uploads/2022/12/031002041670061724.1328.zip?download_name=RLN8_410_22120247.zip) | 2022‑12‑02 | <ol><li>Optimized experience for preview and playback</li><li>Adapted to Reolink Video Doorbell</li><li>Adapted to Reolink Floodlight series cameras</li><li>Solved the adaptation problem of TrackMix series and Duo2 series cameras</li><li>Solved the problem that common users cannot enable push</li><li>Solved the problem that Doorbell cameras cannot load the audio interface on iOS App when connected to Reolink NVR</li><li>Solved the problem that the FTP function of the NVR can not be saved when setting it via iOS App</li><li>Solved the problem that the video section after 00:00(UTC) cannot be searched out when using  the Clip function</li><li>Optimize network related settings.</li><li>Update web client</li><li>Solved other known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.2.0.212_22111847](https://home-cdn.reolink.us/wp-content/uploads/2022/11/181214381668773678.1587.zip?download_name=RLN8_410_22111847.zip) | 2022‑11‑18 | <ol><li>Optimized experience for preview and playback</li><li>Adapted to Reolink Floodlight series cameras</li><li>Solved the adaptation problem of TrackMix series and Duo2 series cameras</li><li>Solved the problem that common users cannot enable push</li><li>Solved the problem that scrollview function doesn't work for the RLN8-410 under 8-multiple screens</li><li>Solved the problem that Doorbell cameras cannot load the audio interface on iOS App when connected to Reolink NVR</li><li>Solved the problem that the FTP function of the NVR can not be saved when setting it via iOS App</li><li>Solved the problem that the video section after 00:00(UTC) cannot be searched out when using  the Clip function</li><li>Update web client</li><li>Solved other known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.1.0.211_22102413](https://home-cdn.reolink.us/wp-content/uploads/2022/10/261024191666779859.0167.zip?download_name=RLN8_410_211_22102413.zip) | 2022‑10‑24 | <ol><li>Adapted to Reolink Video Doorbell</li><li>Optimized the experience of Preview and Playback</li><li>Update web client</li><li>Fix other known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.200_22081548](https://home-cdn.reolink.us/wp-content/uploads/2022/08/171015501660731350.9864.zip?download_name=RLN8_410_22081548.zip) | 2022‑08‑15 | <ol><li>Solved the problem of pixelated image in complex scenes.</li><li>Optimize the interface and interaction.</li><li>Add the option to enable or disable the status reminder icon displayed on the preview screen.</li><li>Solve the problem that the login box input will disappear automatically after 30s.</li><li>Add the function of setting IPC Day/Night switching thresholds.</li><li>Add the function of setting a siren schedule for IPC camera.</li><li>Add the function of customizing the siren of the camera connected to the NVR through the Reolink App</li><li>Add push test and the settings for the interval time</li><li>Optimize network related settings</li><li>Add zoom function on the playback page, and add full-screen playback function</li><li>Fix bug in Hebrew</li><li>Add Portuguese</li><li>Add the function of keeping video recordings for the latest 2days, 3days, 7 days, 14 days and 30 days</li><li>Adapt to more new models, such as: Duo series, Duo2 series, TrackMix series, etc.</li><li>Update web client</li><li>Update to support using ONVIF to access NVR's H.256 bit rate</li><li>Supporting picture-in-picture preview for Reolink Trackmix camera</li><li>Added person, vehicle and pet options for Spotlight Auto Night mode</li><li>Added configuration options of Fixed Frame Rate and Auto Frame Rate</li><li>Fix other known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.159_21122454](https://drive.google.com/uc?id=1KFINfp9wxFFdT7Wvyn4xPPiUHWb6Ckhq&confirm=t) | 2021‑12‑24 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/ti9o8u/image_upside_down_after_firmware_upgrade_rlc820a/i1hh2qf/)<br />[Source 2](https://www.reddit.com/r/reolinkcam/comments/u1yji2/client_v872_update_changed_to_save_the_stream/)<br />[Source 3](https://www.reddit.com/r/reolinkcam/comments/vtakeh/where_is_old_firmware_for_rlc810a820a/ifhg6l7/)<br />[Source 4](https://community.reolink.com/topic/3267/client-v8-7-2-update-changed-to-save-the-clear-stream-mode-setting)
[v3.0.0.148_21100909](https://home-cdn.reolink.us/wp-content/uploads/2021/10/130933571634117637.7477.zip?download_name=RLN8_410_148_21100909.zip) | 2021‑10‑09 | <ol><li>Optimized UI display and interaction.</li><li>Solved the problem that the camera prompts "connecting" instead of "connection succeeded" when it's added to the NVR.</li><li>Solved the problem of failing to set flip for some channels via web browser .</li><li>Optimized the reporting of MD and AI status.</li><li>Optimized backup download status query via web browser.</li></ol> | 1.It is just a firmware for NVR.<br />2.If your NVR's model number is not RLN8-410 with hardware version N2MB02,please wait for the new firmware release.
[v3.0.0.130_21060706](https://drive.google.com/uc?id=1yerGhUO78-QeAuT1sye87NXmr7-t_De0&confirm=t) | 2021‑06‑07 | <ol><li>Optimized UI display and interaction</li><li>Solved the problem that only the videos recorded before 5 mins could be found when searching the recordings in Fluent mode via Reolink App</li><li>Added Korean language</li><li>In the Backup interface, the online channels are selected by default for channel selection, and all video types are selected by default.</li><li>Added a key for switching between uppercase and lowercase in the English keyboard</li><li>Added the refreshing channel list function in the channel adding interface</li><li>Added an entry for NTP settings in the system time setting page. NTP automatic synchronization option is turned on by default.</li><li>Added the spotlight function to the menu on the preview interface</li><li>Adapted to the spotlight function: Added the option to turn on the light based on the scheduled time or night vision for Human/Vehicle detection cameras</li><li>Added the function of audio alarm in the preview menu</li><li>Added volume adjustment function for the ip cameras</li><li>Added Human/Vehicle detection sensitivity, target size setting, automatic tracking related function configuration pages</li><li>Supported the 2-way audio function via Reolink Client for the cameras connected to the NVR</li><li>The login box will disappear automatically after 30s</li><li>Changed the account of the login window to username</li><li>Solved the problem that when configuring the local record settings via Reolink Client, the recording schedule on the NVR will also be changed</li><li>Solved other known issues.</li></ol> | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izn37dj)
[v3.0.0.123_21031205](https://home-cdn.reolink.us/wp-content/uploads/2021/03/210317591616296679.4752.zip)<br />[v3.0.0.123_21031205](https://reolink-storage.s3.amazonaws.com/website/firmware/20210312firmware/RLN8-410.123_21031205.zip) | 2021‑03‑12 | <ol><li>Optimized UI interaction</li><li>Optimized email test error codes and copywriting</li><li>Solved HDD SMART display error</li><li>Solved other known bugs</li></ol> | [Archive](https://web.archive.org/web/20210801111909/https://support.reolink.com/hc/en-us/articles/900006218883-21st-Mar-2021-Firmware-for-Reolink-RLN8-410-H3MB18-or-N2MB02-and-RLN16-410-H3MB18-)
[v3.0.0.118_21020446](https://home-cdn.reolink.us/wp-content/uploads/2021/02/061051201612608680.3376.zip)<br />[v3.0.0.118_21020446](https://reolink-storage.s3.amazonaws.com/website/firmware/20210206firmware/RLN8-410.118_21020446..zip) | 2021‑02‑04 | Solve the problem that the IPC probably cannot connect to NVR after powering off and restarting NVR. | [Archive](https://web.archive.org/web/20210803030929/https://support.reolink.com/hc/en-us/articles/900004388326-6th-Feb-2021-Firmware-for-Reolink-RLN8-410-and-RLN16-410-H3MB18-)
[v3.0.0.82_20102144](https://reolink-storage.s3.amazonaws.com/website/firmware/20201021firmware/RLN8-410_20102144.zip) | 2020‑10‑21 | <ol><li>Added function that can support 12MP cameras</li><li>Added a new web terminal that supports HTML5 player, which mainly solves the problem when FLASH expires</li><li>Newly added Smart Playback function (fast playback with continuous recording, normal speed playback with motion events).</li><li>Added the help prompt message when the email configuration is wrong</li><li>Solved the problem that NVR keeps restarting under special network environment in Beta version</li><li>Solved the problem when connecting PTZ cameras or setting preset points in the Beta version</li><li>Solved the problem that the old version cameras failed to obtain configuration information in the Beta version</li><li>Solved the problem of probabilistic AI recording without pre-recording</li><li>Solved the problem that the alarm is triggered for a short time (about 1 second) and the recording is not recorded probabilistically</li><li>Solved the problem of UI interaction and display errors</li><li>Fulfilled the suggestions and needs of users</li><li>Fixed other known bugs and optimized performance</li></ol> | [Archive](https://web.archive.org/web/20210129185403/https://support.reolink.com/hc/en-us/articles/900003335926-10-21-2020-Firmware-for-Reolink-RLN8-410-and-RLN16-410-H3MB18-)
[v3.0.0.59_20081247](https://reolink-storage.s3.amazonaws.com/website/firmware/20200812firmware/RLN8-410_20081247.zip) | 2020‑08‑12 | <ol><li>Adopt new UI and new interaction methods</li><li>Support upgrading automatically online function (via Reolink APP)</li><li>Optimize system performance</li></ol> | [Archive](https://web.archive.org/web/20201011161357/https://support.reolink.com/hc/en-us/articles/900002407106-08-12-2020-Firmware-for-Reolink-RLN8-410-and-RLN16-410-H3MB18-)

  ### N3MB01
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.3.0.226_23031609](https://home-cdn.reolink.us/wp-content/uploads/2023/03/290835361680078936.0569.zip?download_name=RLN8_410_23031609.zip) | 2023‑03‑16 | <ol><li>Optimize the interface and interaction.</li><li>Compatible with fisheye series models.</li><li>Compatible with RLC-81PA model.</li><li>Support configuring auto-tracking and AI audio noise reduction settings for TrackMix series camera.</li><li>Support configuring splicing settings for Duo 2 series.</li><li>Support the 3D positioning function for RLC-823A 16X.</li><li>Support switches to control status light and the visitor button not trigger the horn control for Reolink Doorbell series.</li><li>Optimize privacy mask UI.</li><li>Add login lock function.</li><li>Add downlink port network segment configuration function.</li><li>Add IOT device timing constant light time point sorting.</li><li>Update RTSP.</li><li>Upgrade ONVIF version.</li><li>Update web client.</li><li>Solved other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.2.0.218_23020151](https://home-cdn.reolink.us/wp-content/uploads/2023/02/100653511676012031.3054.zip?download_name=RLN8_410_23020151.zip) | 2023‑02‑01 | <ol><li>Optimize the interface and interaction.</li><li>Add the function of keeping video recordings for the latest 1day.</li><li>Adapted to RLC-81MA models.</li><li>Optimize network related settings.</li><li>Update web client.</li><li>Solved other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.2.0.214_22120252](https://home-cdn.reolink.us/wp-content/uploads/2022/12/031003431670061823.207.zip?download_name=RLN8_410_22120252.zip) | 2022‑12‑02 | <ol><li>Optimized experience for preview and playback</li><li>Adapted to Reolink Video Doorbell</li><li>Adapted to Reolink Floodlight series cameras</li><li>Solved the adaptation problem of TrackMix series and Duo2 series cameras</li><li>Solved the problem that common users cannot enable push</li><li>Solved the problem that Doorbell cameras cannot load the audio interface on iOS App when connected to Reolink NVR</li><li>Solved the problem that the FTP function of the NVR can not be saved when setting it via iOS App</li><li>Solved the problem that the video section after 00:00(UTC) cannot be searched out when using  the Clip function</li><li>Optimize network related settings.</li><li>Update web client</li><li>Solved other known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.2.0.212_22111814](https://home-cdn.reolink.us/wp-content/uploads/2022/11/181216081668773768.0982.zip?download_name=RLN8_410_22111814.zip) | 2022‑11‑18 | <ol><li>Optimized experience for preview and playback</li><li>Adapted to Reolink Floodlight series cameras</li><li>Solved the adaptation problem of TrackMix series and Duo2 series cameras</li><li>Solved the problem that common users cannot enable push</li><li>Solved the problem that Doorbell cameras cannot load the audio interface on iOS App when connected to Reolink NVR</li><li>Solved the problem that the FTP function of the NVR can not be saved when setting it via iOS App</li><li>Solved the problem that the video section after 00:00(UTC) cannot be searched out when using  the Clip function</li><li>Update web client</li><li>Solved other known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.1.0.211_22102439](https://home-cdn.reolink.us/wp-content/uploads/2022/10/261025391666779939.6375.zip?download_name=RLN8_410_211_22102439.zip) | 2022‑10‑24 | <ol><li>Adapted to Reolink Video Doorbell</li><li>Optimized the experience of Preview and Playback</li><li>Update web client</li><li>Fix other known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.200_22081500](https://home-cdn.reolink.us/wp-content/uploads/2022/08/171013581660731238.9332.zip?download_name=RLN8_410_22081500.zip)<br />[v3.0.0.200_22081500](https://support.reolink.com/attachments/token/AxTAL3n6yku95GsepijEsOAqA/?name=NT98323_NVR_8IP_REOLINK_L300_200_22081500.pak) | 2022‑08‑15 | <ol><li>Solved the problem of pixelated image in complex scenes.</li><li>Optimize the interface and interaction.</li><li>Add the option to enable or disable the status reminder icon displayed on the preview screen.</li><li>Solve the problem that the login box input will disappear automatically after 30s.</li><li>Add the function of setting IPC Day/Night switching thresholds.</li><li>Add the function of setting a siren schedule for IPC camera.</li><li>Add the function of customizing the siren of the camera connected to the NVR through the Reolink App</li><li>Add push test and the settings for the interval time</li><li>Optimize network related settings</li><li>Add zoom function on the playback page, and add full-screen playback function</li><li>Fix bug in Hebrew</li><li>Add Portuguese</li><li>Add the function of keeping video recordings for the latest 2days, 3days, 7 days, 14 days and 30 days</li><li>Adapt to more new models, such as: Duo series, Duo2 series, TrackMix series, etc.</li><li>Support multi-screen display mode, which adapts to connect multiple (Duo series, TrackMix) series IPCs to the NVR, but the total number of cameras cannot exceed 8 devices respectively</li><li>Update web client</li><li>Update to support using ONVIF to access NVR's H.256 bit rate</li><li>Supporting picture-in-picture preview for Reolink Trackmix camera</li><li>Added person, vehicle and pet options for Spotlight Auto Night mode</li><li>Added configuration options of Fixed Frame Rate and Auto Frame Rate</li><li>Fix other known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.198_22072853](https://home-cdn.reolink.us/wp-content/uploads/2022/07/291255561659099356.2154.zip?download_name=RLN8_410_22072853.zip) | 2022‑07‑28 | <ol><li>Optimize the interface and interaction.</li><li>Add the option to enable or disable the status reminder icon displayed on the preview screen.</li><li>Solve the problem that the login box input will disappear automatically after 30s.</li><li>Add the function of setting IPC Day/Night switching thresholds.</li><li>Add the function of setting a siren schedule for IPC camera.</li><li>Add the function of customizing the siren of the camera connected to the NVR through the Reolink App</li><li>Add push test and the settings for the interval time</li><li>Optimize network related settings</li><li>Add zoom function on the playback page, and add full-screen playback function</li><li>Fix bug in Hebrew</li><li>Add Portuguese</li><li>Add the function of keeping video recordings for the latest 7 days, 14 days and 30 days</li><li>Support multi-screen display mode, which adapts to connect multiple (Duo series, TrackMix) series IPCs to the NVR, but the total number of cameras cannot exceed 8 devices respectively</li><li>Update web client</li><li>Update to support using ONVIF to access NVR's H.256 bit rate</li><li>Fix other known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.159_21122405](https://drive.google.com/uc?id=1KFOOcHHMen1oDJJM0i9WD-VNwcnJjMYD&confirm=t)<br />[v3.0.0.159_21122405](https://www.mediafire.com/file/hfzxqwpw120233r/NT98323_NVR_8IP_REOLINK_L300_159_21122405.pak/file) | 2021‑12‑24 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/ti9o8u/image_upside_down_after_firmware_upgrade_rlc820a/i1hh2qf/)<br />[Source 2](https://www.reddit.com/r/reolinkcam/comments/u1yji2/client_v872_update_changed_to_save_the_stream/)<br />[Source 3](https://www.reddit.com/r/reolinkcam/comments/visjrg/does_anyone_have_the_link_to_old_firmwares_for/idf44s0/)<br />[Source 4](https://community.reolink.com/topic/3267/client-v8-7-2-update-changed-to-save-the-clear-stream-mode-setting)
[v3.0.0.148_21101146](https://home-cdn.reolink.us/wp-content/uploads/2021/10/130910331634116233.1488.zip) | 2021‑10‑11 |  | 

  ### N7MB01
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.3.0.226_23031632](https://home-cdn.reolink.us/wp-content/uploads/2023/03/171053171679050397.8891.zip?download_name=RLN8_410_226_23031632.zip) | 2023‑03‑16 | <ol><li>Optimize the interface and interaction.</li><li>Compatible with fisheye series models.</li><li>Compatible with RLC-81PA model.</li><li>Support configuring auto-tracking and AI audio noise reduction settings for TrackMix series camera.</li><li>Support configuring splicing settings for Duo 2 series.</li><li>Support the 3D positioning function for RLC-823A 16X.</li><li>Support switches to control status light and the visitor button not trigger the horn control for Reolink Doorbell series.</li><li>Optimize privacy mask UI.</li><li>Add login lock function.</li><li>Add downlink port network segment configuration function.</li><li>Add IOT device timing constant light time point sorting.</li><li>Update RTSP.</li><li>Upgrade ONVIF version.</li><li>Update web client.</li><li>Solved other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.2.0.218_23011221](https://home-cdn.reolink.us/wp-content/uploads/2023/01/131018291673605109.1073.zip?download_name=RLN8_410_23011221.zip) | 2023‑01‑12 | <ol><li>Optimize the interface and interaction.</li><li>Optimized experience for preview and playback.</li><li>Add the function of keeping video recordings for the latest 1day.</li><li>Adapted to Reolink Video Doorbell.</li><li>Adapted to Reolink Floodlight series cameras.</li><li>Adapted to RLC-81MA models.</li><li>Solved the adaptation problem of TrackMix series and Duo2 series cameras.</li><li>Solved the problem that common users cannot enable push.</li><li>Solved the problem that Doorbell cameras cannot load the audio interface on iOS App when connected to Reolink NVR.</li><li>Solved the problem that the FTP function of the NVR can not be saved when setting it via iOS App.</li><li>Solved the problem that the video section after 00:00(UTC) cannot be searched out when using  the Clip function.</li><li>Optimize network related settings.</li><li>Update web client.</li><li>Solved other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.211_22102113](https://home-cdn.reolink.us/wp-content/uploads/2022/10/240908121666602492.1096.zip?download_name=RLN8_410_22102113.zip) | 2022‑10‑21 | <ol><li>Optimize the interface and interaction.</li><li>Support RTSP url access with the h264 field.</li><li>Update web client.</li><li>Add the function of keeping video recordings for the latest 2days, 3days, 7 days, 14 days and 30 days.</li><li>Added three full-screen playback modes for TrackMix series.</li><li>Added person, vehicle and pet options for Spotlight Auto Night mode.</li><li>Added configuration options of Fixed Frame Rate and Auto Frame Rate.</li><li>Solved the adaptation problem of TrackMix series and Duo 2 series.</li><li>Added interface copywriting to solve interface text errors.</li><li>Fix other known bugs.</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.

</details>

<details>
  <summary>Reolink Duo 2 POE</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/09/100416541631247414.8092.png" width="150">

[Product page](https://reolink.com/product/reolink-duo-poe/)

  ### IPC_529B17B8MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.1889_23031700](https://home-cdn.reolink.us/wp-content/uploads/2023/03/241045311679654731.5333.zip?download_name=Reolink_Duo_2_PoE_23031700.zip) | 2023‑03‑17 | <ol><li>Optimize stitching effect</li><li>Optimize related network services</li><li>Optimize image effect</li><li>Fix other known bugs</li></ol> | 
[v3.0.0.1337_22091900](https://home-cdn.reolink.us/wp-content/uploads/2022/09/221016131663841773.7559.zip?download_name=Reolink_Duo_2_POE_220919.zip) | 2022‑09‑19 | <ol><li>Solved the problem of AI probabilistic failure under night vision</li><li>Solved the problem of failure to capture picture by alert email in complex scenarios</li><li>Optimized the search strategy for playback</li><li>Optimized the MD sensitivity under night vision</li><li>Solved the problem that the number of WiFi signals cannot display on Reolink Client when the camera is connected by WiFi</li><li>Solved the problem that there is no pet mark in playback after enabling pet detection</li><li>Optimized the lighting speed of the spotlight under night vision</li></ol> | Note: This firmware will not work with your Reolink Duo Floodlight PoE or Reolink Duo Floodlight WiFi, if you need new firmware of  Reolink Duo Floodlight PoE or Reolink Duo Floodlight WiFi, please contact Reolink support to help.

</details>

<details>
  <summary>Reolink Duo 2 WiFi</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/09/100410331631247033.8797.png" width="150">

[Product page](https://reolink.com/product/reolink-duo-wifi/)

  ### IPC_529B17B8MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.1889_23031701](https://home-cdn.reolink.us/wp-content/uploads/2023/03/241046301679654790.9233.zip?download_name=Reolink_Duo_2_WiFi_23031701.zip) | 2023‑03‑17 | <ol><li>Optimize stitching effect</li><li>Optimize related network services</li><li>Optimize image effect</li><li>Fix other known bugs</li></ol> | 
[v3.0.0.1391_22101061](https://drive.google.com/uc?id=1YOtVF851NRX9AuRx_o7rtchyJMRMnXDm&confirm=t) | 2022‑10‑10 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)
[v3.0.0.1337_22091901](https://home-cdn.reolink.us/wp-content/uploads/2022/09/221021161663842076.2251.zip?download_name=Reolink_Duo_2_WiFi_220919.zip) | 2022‑09‑19 | <ol><li>Solved the problem of AI probabilistic failure under night vision</li><li>Solved the problem of failure to capture picture by alert email in complex scenarios</li><li>Optimized the search strategy for playback</li><li>Optimized the MD sensitivity under night vision</li><li>Solved the problem that the number of WiFi signals cannot display on Reolink Client when the camera is connected by WiFi</li><li>Solved the problem that there is no pet mark in playback after enabling pet detection</li><li>Optimized the lighting speed of the spotlight under night vision</li></ol> | Note: This firmware will not work with your Reolink Duo Floodlight PoE or Reolink Duo Floodlight WiFi, if you need new firmware of  Reolink Duo Floodlight PoE or Reolink Duo Floodlight WiFi, please contact Reolink support to help.

</details>

<details>
  <summary>Reolink Duo Floodlight PoE</summary>

<img src="https://reolink.com/wp-content/uploads/2022/11/230220051669170005.8162.png" width="150">

[Product page](https://reolink.com/product/reolink-duo-floodlight-poe/)

  ### IPC_529B17B8MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.1889_23031702](https://home-cdn.reolink.us/wp-content/uploads/2023/03/241052211679655141.5445.zip?download_name=Reolink_Duo_Floodlight_PoE_23031702.zip) | 2023‑03‑17 | <ol><li>Optimize stitching effect</li><li>Optimize related network services</li><li>Optimize image effect</li><li>Fix other known bugs</li></ol> | 

</details>

<details>
  <summary>Reolink Duo Floodlight WiFi</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2022/09/130846161663058776.1316.png" width="150">

[Product page](https://reolink.com/product/reolink-duo-floodlight-wifi/)

  ### IPC_529B17B8MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.1889_23031703](https://home-cdn.reolink.us/wp-content/uploads/2023/03/241054031679655243.856.zip?download_name=Reolink_Duo_Floodlight_WiFi_23031703.zip) | 2023‑03‑17 | <ol><li>Optimize stitching effect</li><li>Optimize related network services</li><li>Optimize image effect</li><li>Fix other known bugs</li></ol> | 

</details>

<details>
  <summary>Reolink Duo PoE</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/09/100416541631247414.8092.png" width="150">

[Product page](https://reolink.com/product/reolink-duo-poe/)

  ### IPC_528B174MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.1388_22100600](https://home-cdn.reolink.us/wp-content/uploads/2022/10/110156061665453366.7113.zip?download_name=Reolink_Duo_PoE_221006.zip) | 2022‑10‑06 | <ol><li>Update the web version</li><li>Optimize the AI detection function<ol type="a"><li>Upgrade AI model to support pets</li><li>Improve the recognition accuracy of people, cars, and pets, and optimize static AI false positives</li><li>Increase the AI delay alarm function, which can reduce the dynamic misjudgment caused by flying insects, rain and other reasons by adjusting the delay gear</li><li>Optimize the problem of false alarms caused by day and night switching and lighting changes, and solve the problem that white lights are repeatedly turned on and off in some scenes</li></ol></li><li>Optimize night vision images</li><li>Increase the AI detection type of intelligent white light</li><li>Add gop setting function</li><li>Add night vision frame drop function</li><li>Optimized related network protocols and some known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.1171_22073000](https://drive.google.com/uc?id=1VTg9hrY-bvZZyIYac_IGW4WZUhKDkyXh&confirm=t) | 2022‑07‑30 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)<br />[Source 2](https://drive.google.com/drive/folders/1ik8oU1CjskF_V-blh7-dub0K70LSBgqi)
[v3.0.0.684_21110100](https://drive.google.com/uc?id=1Bxyn42psnj3j5BZyuZGqik2NmVMdFYYA&confirm=t) | 2021‑11‑01 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)<br />[Source 2](https://drive.google.com/drive/folders/1ik8oU1CjskF_V-blh7-dub0K70LSBgqi)

</details>

<details>
  <summary>Reolink Duo WiFi</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2021/09/100410331631247033.8797.png" width="150">

[Product page](https://reolink.com/product/reolink-duo-wifi-v1/)

  ### IPC_528B174MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.1388_22100601](https://home-cdn.reolink.us/wp-content/uploads/2022/10/110159161665453556.8234.zip?download_name=Reolink_Duo_WiFi_221006.zip) | 2022‑10‑06 | <ol><li>Update the web version</li><li>Optimize the AI detection function<ol type="a"><li>Upgrade AI model to support pets</li><li>Improve the recognition accuracy of people, cars, and pets, and optimize static AI false positives</li><li>Increase the AI delay alarm function, which can reduce the dynamic misjudgment caused by flying insects, rain and other reasons by adjusting the delay gear</li><li>Optimize the problem of false alarms caused by day and night switching and lighting changes, and solve the problem that white lights are repeatedly turned on and off in some scenes</li></ol></li><li>Optimize night vision images</li><li>Increase the AI detection type of intelligent white light</li><li>Add gop setting function</li><li>Add night vision frame drop function</li><li>Optimized related network protocols and some known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.1171_22073001](https://drive.google.com/uc?id=1LESBv5_TQwMZWM8KRvDHXa1fjmA-Ekhq&confirm=t) | 2022‑07‑30 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)<br />[Source 2](https://drive.google.com/drive/folders/1ik8oU1CjskF_V-blh7-dub0K70LSBgqi)
[v3.0.0.684_21110101](https://drive.google.com/uc?id=11QQZYhNyTaNtXKoIYlcA9qUj0oK3F5Ts&confirm=t) | 2021‑11‑01 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)<br />[Source 2](https://drive.google.com/drive/folders/1ik8oU1CjskF_V-blh7-dub0K70LSBgqi)

</details>

<details>
  <summary>Reolink Lumus</summary>

<img src="https://home-cdn.reolink.us/wp-content/assets/2020/01/reolink-lumus-340.png" width="150">

[Product page](https://reolink.com/product/reolink-lumus/)

  ### IPC_325C7
Version | Date | Changes | Notes
--- | --- | --- | ---
[v2.0.0.705_21052800](https://github.com/AT0myks/reolink-fw-archive/files/11149143/IPC_325C7.705_21052800.IMX307.2MP.WIFI7601.REOLINK.zip) | 2021‑05‑28 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://github.com/AT0myks/reolink-fw-archive/discussions/6)
[v2.0.0.687_20102800](https://reolink-storage.s3.amazonaws.com/website/firmware/20201028firmware/Reolink+Lumus_687_20102800.zip) | 2020‑10‑28 | <ol><li>Added multiple languages for the voice prompt when scanning the QR code to set up the camera</li><li>Added Normal recording schedule</li><li>Optimized motion detection performance to reduce false alarms</li><li>Fixed some other bugs.</li></ol> | [Archive](https://web.archive.org/web/20210725025557/https://support.reolink.com/hc/en-us/articles/900002618206-10-28-2020-Firmware-for-Reolink-Lumus-IPC-325C7-)
[v2.0.0.684_20091500](https://reolink-storage.s3.amazonaws.com/website/firmware/20200915firmware/Reolink-Lumus_684_20091500.zip) | 2020‑09‑15 | <ol><li>Added multiple languages for the voice prompt when scanning the QR code to set up the camera</li><li>Added Normal recording schedule</li><li>Optimized motion detection performance to reduce false alarms</li><li>Fixed some other bugs.</li></ol> | [Archive](https://web.archive.org/web/20201021192944/https://support.reolink.com/hc/en-us/articles/900002618206-09-15-2020-Firmware-for-Reolink-Lumus-IPC-325C7-)
[v2.0.0.680_20082500](https://reolink-storage.s3.amazonaws.com/website/firmware/20200825firmware/Reolink-Lumus_680_20082500.zip) | 2020‑08‑25 | <ol><li>Added multiple languages for the voice prompt when scanning the QR code to set up the camera</li><li>Added Normal recording schedule</li><li>Optimized motion detection performance to reduce false alarms</li><li>Fixed some other bugs.</li></ol> | [Archive](https://web.archive.org/web/20200919133639/https://support.reolink.com/hc/en-us/articles/900002618206-08-25-2020-Firmware-for-Reolink-Lumus-IPC-325C7-)
[v2.0.0.642_20030600](https://reolink-storage.s3.amazonaws.com/website/firmware/20200306firmware/Reolink+Lumus_642_20030600.zip) | 2020‑03‑06 | <ol><li>Optimized WiFi connection ability</li><li>Optimized the Day&amp;Night mode feature.</li><li>Lowered down the volume of the speaker when setting up the camera.</li><li>Fixed the bug of camera auto-reboot when sending the email alert.</li></ol> | [Archive](https://web.archive.org/web/20200804203639/https://support.reolink.com/hc/en-us/articles/900000312623-03-06-2020-Firmware-for-Reolink-Lumus-IPC-325C7-)

</details>

<details>
  <summary>Reolink TrackMix PoE</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2022/06/280627521656397672.1918.png" width="150">

[Product page](https://reolink.com/product/reolink-trackmix-poe/)

  ### IPC_529SD78MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.1817_23022700](https://home-cdn.reolink.us/wp-content/uploads/2023/02/280900161677574816.5116.zip?download_name=Reolink_TrackMix_PoE_23022700.zip) | 2023‑02‑27 | <ol><li>Added intelligent audio noise reduction function</li><li>Optimized auto-tracking function</li><li>Fixed the problem that the brightness cannot recover after you change it from Manual back to Auto mode in the Brightness&amp;Shadows settings.</li><li>Fixed other known bugs.</li></ol> | 
[v3.0.0.1584_22120100](https://home-cdn.reolink.us/wp-content/uploads/2022/12/120355501670817350.5671.zip?download_name=Reolink_TrackMix_PoE_22120100.zip) | 2022‑12‑01 | <ol><li>Added intelligent audio noise reduction function.</li><li>Optimized auto-tracking function.</li><li>Fixed the problem that the brightness cannot recover after you change it from Manual back to Auto mode in the Brightness&amp;Shadows settings.</li><li>Fixed other known bugs.</li></ol> | 
[v3.0.0.1514_22111400](https://home-cdn.reolink.us/wp-content/uploads/2022/11/160814371668586477.9388.zip?download_name=Reolink_TrackMix_PoE_22111400.zip) | 2022‑11‑14 | <ol><li>Added the schedule setting for Auto-tracking function</li><li>Added the horizontal tracking range setting for Auto-tracking</li><li>Optimized Auto-tracking effect</li><li>Optimized the picture smear problem when the PT motor is moving</li><li>Added the time settings to stop tracking and returning to the monitor point after the object stops and disappears.</li><li>Added the function of importing and exporting preset images</li><li>Added fixed frame rate and monitor point settings on the Web Client</li><li>Fixed other bugs</li></ol> | 
[v3.0.0.1123_22071300](https://drive.google.com/uc?id=1HDpfdZ-8cx7A3piGWE9QgfmIYW7T5_bp&confirm=t) | 2022‑07‑13 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)
[v3.0.0.1080_22062200](https://drive.google.com/uc?id=12bti2liLQQQ-Ua4RjnEGOkCBZL-M2WDU&confirm=t) | 2022‑06‑22 |  | [Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)
[v3.0.0.1046_22061302](https://drive.google.com/uc?id=1jty6joBXXYKB68oY0DsW8QnKvHL9E2ou&confirm=t) | 2022‑06‑13 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://www.reddit.com/r/reolinkcam/comments/zhktis/comment/izoohjp)

</details>

<details>
  <summary>Reolink TrackMix WiFi</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2022/06/280627421656397662.0035.png" width="150">

[Product page](https://reolink.com/product/reolink-trackmix-wifi/)

  ### IPC_529SD78MP
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.1817_23022701](https://home-cdn.reolink.us/wp-content/uploads/2023/02/280858031677574683.5361.zip?download_name=Reolink_TrackMix_WiFi_23022701.zip) | 2023‑02‑27 | <ol><li>Added intelligent audio noise reduction function</li><li>Optimized auto-tracking function</li><li>Fixed the problem that the brightness cannot recover after you change it from Manual back to Auto mode in the Brightness&amp;Shadows settings.</li><li>Fixed other known bugs</li></ol> | 
[v3.0.0.1584_22120101](https://home-cdn.reolink.us/wp-content/uploads/2022/12/120357311670817451.1817.zip?download_name=Reolink_TrackMix_WiFi_22120101.zip) | 2022‑12‑01 | <ol><li>Added intelligent audio noise reduction function.</li><li>Optimized auto-tracking function.</li><li>Fixed the problem that the brightness cannot recover after you change it from Manual back to Auto mode in the Brightness&amp;Shadows settings.</li><li>Fixed other known bugs.</li></ol> | 
[v3.0.0.1514_22111401](https://home-cdn.reolink.us/wp-content/uploads/2022/11/160815571668586557.1557.zip?download_name=Reolink_TrackMix_WiFi_22111401.zip) | 2022‑11‑14 | <ol><li>Added the schedule setting for Auto-tracking function</li><li>Added the horizontal tracking range setting for Auto-tracking</li><li>Optimized Auto-tracking effect</li><li>Optimized the picture smear problem when the PT motor is moving</li><li>Added the time settings to stop tracking and returning to the monitor point after the object stops and disappears.</li><li>Added the function of importing and exporting preset images</li><li>Added fixed frame rate and monitor point settings on the Web Client</li><li>Fixed other bugs</li></ol> | 

</details>

<details>
  <summary>Reolink Video Doorbell PoE</summary>

<img src="https://home-cdn.reolink.us/wp-content/uploads/2022/05/170610101652767810.7304.png" width="150">

[Product page](https://reolink.com/product/reolink-video-doorbell/)

  ### DB_566128M5MP_P
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2033_23041302](https://home-cdn.reolink.us/wp-content/uploads/2023/05/080159231683511163.4286.zip?download_name=DB_POE_v3002033_23041302.zip) | 2023‑04‑13 | <ol><li>Release new smart home functions:</li><li>Support preview, 2-way audio, notification, voice wake-up on Alexa (notification will be available after finishing Cloud update);</li><li>Support preview, notification, and voice wake-up on Google Home (notification will be available after finishing Cloud update);</li><li>Support GOP settings.</li><li>Remove the original automatic frame drop, incorporate multi-level frame drop, and support frame rate control function</li><li>Support adjustable range of CDS value</li><li>Support working with IOT devices</li><li>Add status light control button for doorbell camera (Available to the App version of 4.37 or later)</li><li>Add ringing control switch for doorbell camera (Available to the App version of 4.37 or later)</li><li>Fix known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.2017_23041202](https://home-cdn.reolink.us/wp-content/uploads/2023/04/121133571681299237.2878.zip?download_name=DB_POE_0412.zip) | 2023‑04‑12 | <ol><li>Release new smart home functions:</li><li>Support preview, 2-way audio, notification, voice wake-up on Alexa (notification will be available after finishing Cloud update);</li><li>Support preview, notification, and voice wake-up on Google Home (notification will be available after finishing Cloud update);</li><li>Support GOP settings.</li><li>Remove the original automatic frame drop, incorporate multi-level frame drop, and support frame rate control function</li><li>Support adjustable range of CDS value</li><li>Support working with IOT devices</li><li>Add status light control button for doorbell camera (Available to the App version of 4.37 or later)</li><li>Add ringing control switch for doorbell camera (Available to the App version of 4.37 or later)</li><li>Fix known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.1859_23030902](https://home-cdn.reolink.us/wp-content/uploads/2023/04/030245401680489940.8505.zip?download_name=Doorbell_POE_230309.zip) | 2023‑03‑09 | <ol><li>Release new smart home functions:</li><li>Support preview, 2-way audio, notification, voice wake-up on Alexa (notification will be available after finishing Cloud update);</li><li>Support preview, notification, and voice wake-up on Google Home (notification will be available after finishing Cloud update);</li><li>Support GOP settings.</li><li>Remove the original automatic frame drop, incorporate multi-level frame drop, and support frame rate control function</li><li>Support adjustable range of CDS value</li><li>Support working with IOT devices</li><li>Add status light control button for doorbell camera (Available to the App version of 4.37 or later)</li><li>Add ringing control switch for doorbell camera (Available to the App version of 4.37 or later)</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.1459_22102808](https://drive.google.com/uc?id=1Z5vL1hYEu_mT7Nj0eqTcmm2egwKVqOkh&confirm=t) | 2022‑10‑28 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://github.com/JimStar/reolink_cctv/issues/49#issuecomment-1305070003)

</details>

<details>
  <summary>Reolink Video Doorbell WiFi</summary>

<img src="https://reolink.com/wp-content/uploads/2022/05/170610101652767810.7304.png" width="150">

[Product page](https://reolink.com/product/reolink-video-doorbell-wifi/)

  ### DB_566128M5MP_W
Version | Date | Changes | Notes
--- | --- | --- | ---
[v3.0.0.2033_23041300](https://home-cdn.reolink.us/wp-content/uploads/2023/05/080150541683510654.3453.zip?download_name=DB_WIFI_v3002033_23041300.zip) | 2023‑04‑13 | <ol><li>Release new smart home functions:</li><li>Support preview, 2-way audio, notification, voice wake-up on Alexa (notification will be available after finishing Cloud update);</li><li>Support preview, notification, and voice wake-up on Google Home (notification will be available after finishing Cloud update);</li><li>Support GOP settings.</li><li>Remove the original automatic frame drop, incorporate multi-level frame drop, and support frame rate control function</li><li>Support adjustable range of CDS value</li><li>Support working with IOT devices</li><li>Add status light control button for doorbell camera (Available to the App version of 4.37 or later)</li><li>Add ringing control switch for doorbell camera (Available to the App version of 4.37 or later)</li><li>Fix known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.2017_23041200](https://home-cdn.reolink.us/wp-content/uploads/2023/04/121132011681299121.0701.zip?download_name=DB_WIFI_0412.zip) | 2023‑04‑12 | <ol><li>Release new smart home functions:</li><li>Support preview, 2-way audio, notification, voice wake-up on Alexa (notification will be available after finishing Cloud update);</li><li>Support preview, notification, and voice wake-up on Google Home (notification will be available after finishing Cloud update);</li><li>Support GOP settings.</li><li>Remove the original automatic frame drop, incorporate multi-level frame drop, and support frame rate control function</li><li>Support adjustable range of CDS value</li><li>Support working with IOT devices</li><li>Add status light control button for doorbell camera (Available to the App version of 4.37 or later)</li><li>Add ringing control switch for doorbell camera (Available to the App version of 4.37 or later)</li><li>Fix known bugs</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.1859_23030900](https://home-cdn.reolink.us/wp-content/uploads/2023/04/030234101680489250.782.zip?download_name=Doorbell_WiFi_230309.zip) | 2023‑03‑09 | <ol><li>Release new smart home functions:</li><li>Support preview, 2-way audio, notification, voice wake-up on Alexa (notification will be available after finishing Cloud update);</li><li>Support preview, notification, and voice wake-up on Google Home (notification will be available after finishing Cloud update);</li><li>Support GOP settings.</li><li>Remove the original automatic frame drop, incorporate multi-level frame drop, and support frame rate control function</li><li>Support adjustable range of CDS value</li><li>Support working with IOT devices</li><li>Add status light control button for doorbell camera (Available to the App version of 4.37 or later)</li><li>Add ringing control switch for doorbell camera (Available to the App version of 4.37 or later)</li></ol> | Recommendation for upgrade: Because there are many updates in this version, it is recommended to check the Reset Configuration option when upgrading.
[v3.0.0.1459_22102806](https://drive.google.com/uc?id=1ZAoBVMKyKzr6T6NMoZvI5MT2T4lgYCY_&confirm=t) | 2022‑10‑28 |  | :warning: The only available links for this firmware are hosted by users and not Reolink themselves<br />[Source 1](https://github.com/JimStar/reolink_cctv/issues/49#issuecomment-1305070003)

</details>

