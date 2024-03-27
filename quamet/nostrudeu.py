import asyncio

async def execute_move(move: str):
    """
    Executes a move in the game.

    Args:
        move: The move to execute.
    """

    # Get the current game state.
    game_state = await get_game_state()

    # Validate and execute the move.
    if is_move_valid(move, game_state):
        game_state = execute_move_internal(move, game_state)
        await update_game_state(game_state)
    else:
        raise ValueError(f"Invalid move: {move}")
