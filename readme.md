## SyncBot

Sync a subreddit's posts with facebook.

# Setup

1. Clone this repo
```
$ git clone https://github.com/Gr3atWh173/sync_bot.git
```
2. cd into it
```
$ cd sync_bot
```
3. Install dependencies
```
$ pip install -r requirements.txt
```
4. Open config in an editor and assign values to the constants
  - In order to get facebook page token:
    - Goto [Facebook Graph API Explorer](https://developers.facebook.com/tools/explorer/)
    - In the drop down menu, select 'Get User Access Token'
    - Tick "manage_pages", "publish_pages" and "pages_show_list" permissions
    - Click on get access token
    - Now from the dropdown, select your page
    - Copy the access token into the config file
5. Now, you're ready to run the bot file!

