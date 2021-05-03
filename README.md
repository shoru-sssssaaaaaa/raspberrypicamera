# RaspberryPiCamera

![raspberrycamera (1)](https://user-images.githubusercontent.com/52835270/116867609-7413a780-ac48-11eb-92cf-8a10312626cc.png)
The programs in this repository provide a function to stream video from a USB camera using [MJPG-streamer](https://sourceforge.net/projects/mjpg-streamer/) and send screenshots to [LINE](https://line.me/en/) with cron.

Some examples of usage are

- Monitoring your front door
- Monitoring the office desk to check the mail.

## Prerequisites

### Tools

- RaspberryPi Model B+
- USB Web Camera
- [MJPG-streamer](https://sourceforge.net/projects/mjpg-streamer/)
- cron
- [LINE Notify](https://notify-bot.line.me/en/)

### Environment variables

| Name       | Required? | Description                          |
| ---------- | --------- | ------------------------------------ |
| ID         | Yes       | User ID for access to MJPG Streamer  |
| PW         | Yes       | Password for access to MJPG Streamer |
| DIR        | Yes       | Absolute directory path to this repo |
| LINE_TOKEN | Yes       | Token for the Line notify            |

## How to setup?

1.  Run the following script.
    ```
    sh setup.sh
    ```
1.  Generate a token for [LINE Notify](https://notify-bot.line.me/en/) and set environment variables.
1.  Run the following script.
    ```
    sh start_streaming.sh
    ```
1.  Configure crontab with `crontab -e`. (See `example-crontab` file)
