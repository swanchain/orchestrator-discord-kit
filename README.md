# Discord User Information Exporter

This Python script exports user information from all guilds connected to your Discord bot and saves it to a CSV file named `userInfo.csv`. The following user information is collected and saved to the file:

- User name
- User discriminator
- User ID
- Whether or not the user is a bot
- User creation date
- User status

## Setup

Before running the script, you'll need to set up a few things:

1. Install the required Python packages by running `pip install -r requirements.txt`.
2. Create a new Discord bot and get its token. You can do this in the [Discord Developer Portal](https://discord.com/developers/applications).
3. Invite the bot to the guilds you want to export user information from. You'll need the `Administrator` permission to do this.
4. Create a `.env` file in the same directory as the script with the following content:

    - discord_token=Your bot's token
    - discord_guild_id=The ID of the guild you want to export user information from

## Usage

To run the script, simply execute the `main.py` file with the following command:

    python main.py

The script will automatically generate the `userInfo.csv` file in the same directory as the script.

## Troubleshooting

If you encounter any issues while running the script, check the following:

- Make sure the bot is properly connected to the guild and has the necessary permissions.
- Check that the `discord_guild_id` in the `.env` file is correct.
- Ensure that you have the necessary permissions to create and write to files in the script's directory.

## Disclaimer

This script is provided as-is, without any warranty or guarantee of any kind. Use it at your own risk.
