#!/usr/bin/env python3

"""
Clear and Execute Plugin for iTerm2.

This plugin provides a key binding for iTerm2 that clears the screen and then
executes the command when you press Shift+Enter.

Usage:
- Select a command on the terminal and press Shift+Enter to execute it.

Requirements:
- iTerm2 3.4 or later
"""

import iterm2


async def clear_and_execute(session):
    """Clear the screen and execute the command in the current session."""
    # Clear the screen
    await session.async_send_text("\033[2J\033[H")

    # Get the current command and execute it
    command = await session.async_get_current_command()
    await session.async_send_text(command)


async def main(connection):
    """Register the key binding for the plugin."""
    # Define the key binding
    key_binding = "Shift-Enter"

    # Get the app and create a key binding for the plugin
    app = await iterm2.async_get_app(connection)
    key_bindings = await app.async_get_key_bindings()
    new_binding = iterm2.KeyBinding(key_binding, "Clear and Execute", clear_and_execute)
    key_bindings.add_binding(new_binding)

    # Register the key binding
    await app.async_set_key_bindings(key_bindings)


# Start the event loop
iterm2.run_until_complete(main)
