# Clear and Execute Plugin for iTerm2

This plugin provides a key binding for iTerm2 that clears the screen and then executes the command when you press Shift+Enter.

## Installation

### Requirements

- iTerm2 3.4 or later

### Using Oh My Zsh

If you're using [Oh My Zsh](https://ohmyz.sh/), you can install the plugin using the following steps:

1. Clone this repository into `$ZSH_CUSTOM/plugins`:

    ```sh
    git clone https://github.com/username/clear-and-execute.git $ZSH_CUSTOM/plugins/clear-and-execute
    ```

2. Add `clear-and-execute` to the `plugins` array in your `.zshrc` file:

    ```sh
    plugins=(clear-and-execute)
    ```

3. Restart your terminal.

### Manual Installation

If you're not using Oh My Zsh, you can manually install the plugin using the following steps:

1. Clone this repository:

    ```sh
    git clone https://github.com/username/clear-and-execute.git
    ```

2. Copy the `clear_and_execute.py` file to your iTerm2 scripts directory:

    ```sh
    cp clear-and-execute/clear_and_execute.py ~/Library/Application\ Support/iTerm2/Scripts/
    ```

3. Create a new script configuration file for the plugin:

    ```sh
    echo "[ITerm2]
    Name=Clear and Execute
    Path=~/Library/Application Support/iTerm2/Scripts/clear_and_execute.py
    Enable=True
    " > ~/Library/Application\ Support/iTerm2/Scripts/Clear\ and\ Execute.plist
    ```

4. Register the key binding for the plugin:

    ```sh
    defaults write com.googlecode.iterm2 NSUserKeyEquivalents -dict-add 'Clear and Execute' '@\U000d'
    ```

5. Restart iTerm2 to apply the changes.

## Usage

Once the plugin is installed, you can use the Shift+Enter key binding to clear the screen and execute the command.

## License

This plugin is released under the MIT License. See [LICENSE](LICENSE) for details.
